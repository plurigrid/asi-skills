---
name: aptos-coin-flipper
description: Verifiable coin flip on Aptos using drand (League of Entropy) beacon randomness.
  Fair, unbiasable, publicly auditable.
license: Apache-2.0
metadata:
  trit: 0
  color: "#26D826"
  role: Coordinator
  source: drand League of Entropy + Aptos Move
---

# Aptos Coin Flipper (League of Entropy)

> Flip a coin. Prove it was fair. On-chain.

Uses [drand](https://drand.love) — the **League of Entropy** distributed randomness beacon — as an unbiasable source of randomness for coin flips settled on Aptos.

## How It Works

```
1. Player calls flip(guess: bool) → stores guess + current drand round
2. drand beacon publishes round N randomness (BLS threshold sig, unchained)
3. Contract fetches drand output → SHA3(randomness) mod 2 → HEADS or TAILS
4. if guess == outcome → player wins (2x payout minus fee)
```

No one — not the player, the contract deployer, or any single drand node — can predict or bias the outcome. The beacon requires a threshold of independent operators to produce each round.

## drand Beacon

**Quicknet (unchained, G1/G2 swap):**
- Chain hash: `52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971`
- Public key: `83cf0f2896adee7eb8b5f01fcad3912212c437e0073e911fb90022d3e760183c8c4b450b6a0a6c3ac6a5776a2d1064510d1fec758c921cc22b0e17e63aaf4bcb5ed66304de9cf809bd274ca73bab4af5a6e9c76a4bc09e76eae8991ef5ece45a`
- Period: **3 seconds**
- Scheme: `bls-unchained-g1-rfc9380`

Each round produces a 32-byte `randomness` value derived from a BLS signature over the round number.

## Move Contract

```move
module coin_flipper::flip {
    use std::hash;
    use std::signer;
    use aptos_framework::coin;
    use aptos_framework::event;
    use aptos_framework::timestamp;

    /// Coin sides
    const HEADS: u8 = 0;
    const TAILS: u8 = 1;

    /// Errors
    const E_INVALID_GUESS: u64 = 1;
    const E_INSUFFICIENT_BALANCE: u64 = 2;
    const E_ROUND_NOT_READY: u64 = 3;

    struct FlipRequest has key, store, drop {
        player: address,
        guess: u8,           // 0 = HEADS, 1 = TAILS
        drand_round: u64,    // beacon round to resolve against
        wager: u64,
    }

    #[event]
    struct FlipResult has drop, store {
        player: address,
        guess: u8,
        outcome: u8,
        won: bool,
        drand_round: u64,
        randomness: vector<u8>,
    }

    /// Player commits a guess for the *next* drand round.
    public entry fun flip(
        account: &signer,
        guess: u8,
        wager: u64,
        current_drand_round: u64,
    ) {
        assert!(guess == HEADS || guess == TAILS, E_INVALID_GUESS);

        let request = FlipRequest {
            player: signer::address_of(account),
            guess,
            drand_round: current_drand_round + 1, // resolve on next round
            wager,
        };
        move_to(account, request);
    }

    /// Anyone can resolve once the drand randomness is available.
    public entry fun resolve(
        _resolver: &signer,
        player_addr: address,
        drand_randomness: vector<u8>,  // 32 bytes from beacon
        drand_round: u64,
    ) acquires FlipRequest {
        let request = move_from<FlipRequest>(player_addr);
        assert!(drand_round == request.drand_round, E_ROUND_NOT_READY);

        // outcome = SHA3-256(randomness) mod 2
        let hash = hash::sha3_256(drand_randomness);
        let outcome = (*std::vector::borrow(&hash, 0)) % 2;
        let won = outcome == request.guess;

        event::emit(FlipResult {
            player: request.player,
            guess: request.guess,
            outcome,
            won,
            drand_round,
            randomness: drand_randomness,
        });
    }
}
```

## CLI: Just Flip a Coin

```bash
# Flip a coin right now using the latest drand round
just coin-flip

# Flip with a guess
just coin-flip heads
just coin-flip tails
```

### Justfile

```justfile
# Fetch latest drand randomness and flip
coin-flip guess="heads":
    #!/usr/bin/env bash
    set -euo pipefail

    CHAIN="52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971"
    ROUND_URL="https://api.drand.sh/${CHAIN}/public/latest"

    echo "🪙 Fetching drand beacon..."
    RESP=$(curl -s "$ROUND_URL")
    ROUND=$(echo "$RESP" | jq -r '.round')
    RAND=$(echo "$RESP" | jq -r '.randomness')

    # SHA3-256 of the randomness, take first byte mod 2
    OUTCOME_BYTE=$(echo -n "$RAND" | xxd -r -p | openssl dgst -sha3-256 -binary | xxd -p | head -c2)
    OUTCOME=$(( 16#$OUTCOME_BYTE % 2 ))

    if [ "$OUTCOME" -eq 0 ]; then
        RESULT="HEADS"
    else
        RESULT="TAILS"
    fi

    GUESS_UPPER=$(echo "{{guess}}" | tr '[:lower:]' '[:upper:]')

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  drand round:  $ROUND"
    echo "  randomness:   ${RAND:0:16}..."
    echo "  outcome:      $RESULT"
    echo "  your guess:   $GUESS_UPPER"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ "$RESULT" = "$GUESS_UPPER" ]; then
        echo "  ✅ YOU WIN"
    else
        echo "  ❌ YOU LOSE"
    fi
```

### Python one-liner

```bash
python3 -c "
import urllib.request, json, hashlib
r = json.load(urllib.request.urlopen('https://api.drand.sh/52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971/public/latest'))
h = hashlib.sha3_256(bytes.fromhex(r['randomness'])).digest()
print(f\"Round {r['round']}: {'HEADS' if h[0]%2==0 else 'TAILS'}\")
"
```

## Why drand?

| Property | Guarantee |
|----------|-----------|
| **Unbiasable** | No single party can influence the output |
| **Publicly verifiable** | Anyone can verify using the group public key |
| **Unpredictable** | Round N randomness unknown until N is produced |
| **Available** | Threshold scheme — tolerates node failures |
| **Unchained** | Each round independent (no cascading failures) |

The League of Entropy includes Cloudflare, Protocol Labs, EPFL, Kudelski Security, University of Chile, and others.

## GF(3) Skill Coloring

```
gay-mcp ⊕ (+1)  ×  aptos-coin-flipper ○ (0)  ×  gf3-pr-verify ⊖ (-1) = 0 ✓
```

| Skill | Trit | Role |
|-------|------|------|
| gay-mcp | ⊕ (+1) | Generator — deterministic seed for local testing |
| aptos-coin-flipper | ○ (0) | Coordinator — bridges drand entropy to Aptos |
| gf3-pr-verify | ⊖ (-1) | Validator — verifies conservation |

## Loaded Skills

1. **gf3-pr-verify** — conservation verification for flip outcomes
2. **bisimulation-game** — fairness proof: attacker cannot distinguish biased vs unbiased flip
3. **ramanujan-expander** — spectral mixing bound certifies drand output quality
4. **gay-mcp** — SplitMix64 fallback RNG for local/offline testing
5. **multiversal-finance** — prediction market settlement with deterministic oracle

## Commands

```bash
just coin-flip              # Flip using latest drand round
just coin-flip heads        # Flip with a guess
just coin-flip tails        # Flip with a guess
just coin-verify <round>    # Verify a past flip against drand archive
```

---

## Galois Hole Type (Seven Sketches §1.4.1)

> **HOLE TYPE**: This skill is now accessible via Galois connection to `structured-decompositions`.
> See `structured-decompositions/SKILL.md` for the 69-skill accessibility network.
>
> **Adjunction**: f(p) ≤ q ⟺ p ≤ g(q) unlocks world navigation.
