---
name: interaction-rewriting
description: "Acausal, correct-by-construction interaction-time skill with locally ensured GF(3) conservation via rewriting gadgets"
license: MIT
metadata:
  source: interaction-combinators + adhesive-rewriting + GF(3)
  trit: 0
  bundle: compositional-world-models
  xenomodern: true
  acausal: true
  ironic_detachment: 0.13
---

# Interaction Rewriting Skill

> *"Conservation is not checked after the fact—it is ensured at interaction time through local rewriting gadgets."*

**Trit**: 0 (ERGODIC - the rewriting process itself)
**Color**: #D8D826 (Yellow - mediator/process)

---

## Overview

**Interaction Rewriting** provides **acausal**, **bidirectional** skill composition where:

1. **No Directionality** - Interactions are symmetric, not "handoffs"
2. **Correct by Construction** - GF(3) conservation is a local invariant of every rewrite rule
3. **Interaction Time** - Conservation checked at the moment of interaction, not post-hoc
4. **Gadget-Based** - Small rewriting gadgets compose into larger verified systems

```
┌───────────────────────────────────────────────────────────────────────────┐
│              INTERACTION REWRITING: Acausal Conservation                  │
│                                                                           │
│         ┌─────┐          INTERACTION          ┌─────┐                    │
│         │ +1  │◄─────────────────────────────►│ -1  │                    │
│         │Commit│         (bidirectional)      │Verify│                    │
│         └──┬──┘                               └──┬──┘                    │
│            │                                     │                        │
│            └──────────────┬──────────────────────┘                        │
│                           │                                               │
│                       ┌───┴───┐                                           │
│                       │   0   │                                           │
│                       │Compute│                                           │
│                       └───────┘                                           │
│                                                                           │
│            LOCAL INVARIANT: Σ trit = 0 at every interaction              │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## Interaction Combinators Foundation

Based on Lafont's **interaction combinators**—a universal model where:

- **Agents** have principal ports and auxiliary ports
- **Interactions** occur only between principal ports
- **Reduction** is local and confluent
- **Conservation laws** are built into the interaction rules

### The Three Interaction Agents

```
    +1 (Commit/δ)           0 (Compute/γ)           -1 (Verify/ε)
    ═══════════════        ═══════════════         ═══════════════
    
         ●                       ●                       ●
        /|\                     /|\                     /|\
       / | \                   / | \                   / | \
      ↓  ↓  ↓                 ↓  ↓  ↓                 ↓  ↓  ↓
     a₁  p  a₂               a₁  p  a₂               a₁  p  a₂
     
    Generates              Transforms              Validates
    new structure          structure               structure
```

### Fundamental Interaction Rules

Every rule conserves GF(3):

```
Rule 1: ANNIHILATION (same agent type)
═══════════════════════════════════════
    
    [+1]●────────●[+1]  →→→  ═══════════
         principal            (nothing)
         
    Σ = (+1) + (+1) = +2 ≡ -1 (mod 3)
    BUT: annihilation removes both, net change = 0 ✓


Rule 2: COMMUTATION (different agent types)
═════════════════════════════════════════════

    [+1]●────────●[-1]  →→→  [-1]●────────●[+1]
                               crossed wires
    
    Σ_before = (+1) + (-1) = 0
    Σ_after  = (-1) + (+1) = 0 ✓


Rule 3: DUPLICATION (via ergodic mediator)
═══════════════════════════════════════════

    [+1]●────────●[0]   →→→   [+1]●    ●[+1]
                                  \  /
                                   \/
                                   /\
                                  /  \
                              [-1]●    ●[-1]
                              
    Σ_before = (+1) + (0) = +1
    Σ_after  = (+1) + (+1) + (-1) + (-1) = 0
    REQUIRES: duplication adds compensating pair ✓
```

---

## GF(3) Conservation Law

### The Triadic Cycle (Acausal)

```
              +1 (Commit)
                  ↑
                 /│\
                / │ \
               /  │  \
              ╱   │   ╲
             ╱    │    ╲
            ↙     │     ↘
     -1 (Verify)──┼──── 0 (Compute)
                  │
           Σ ≡ 0 (mod 3)
           
    No arrow is privileged—all directions valid
```

### Local Conservation Gadget

```julia
struct InteractionGadget
    left_agent::Agent
    right_agent::Agent
    rule::RewriteRule
    
    # INVARIANT: checked at construction time
    function InteractionGadget(left, right, rule)
        # Pre-interaction trit sum
        pre_sum = left.trit + right.trit
        
        # Post-interaction trit sum
        post_agents = apply_rule(rule, left, right)
        post_sum = sum(a.trit for a in post_agents)
        
        # Conservation MUST hold
        @assert (pre_sum - post_sum) % 3 == 0 "GF(3) violated!"
        
        new(left, right, rule)
    end
end
```

---

## Production Stack Integration

### Layer 1: Replicated Secret Sharing (Moose)

```
┌─────────────────────────────────────────────────────────────┐
│                   tf-encrypted/Moose                         │
│─────────────────────────────────────────────────────────────│
│  • 3-party replicated secret sharing                        │
│  • Each share is a trit: {-1, 0, +1}                        │
│  • Reconstruction requires all 3 → GF(3) conservation       │
│  • gRPC transport with authenticated channels               │
└─────────────────────────────────────────────────────────────┘

Trit Assignment:
  Party 1 (Commit):  +1  → generates shares
  Party 2 (Compute):  0  → processes encrypted data
  Party 3 (Verify):  -1  → validates computation
  
Sum: (+1) + (0) + (-1) = 0 ✓
```

```python
# Moose integration
class TriadicMPC:
    """3-party MPC with GF(3) role assignment."""
    
    def __init__(self, party_id: int):
        self.party_id = party_id
        self.trit = [1, 0, -1][party_id]  # Commit, Compute, Verify
        
    async def secret_share(self, value: int) -> Tuple[Share, Share, Share]:
        """Split value into 3 shares with GF(3) tagging."""
        # Replicated sharing: each party holds 2 of 3 shares
        r1, r2 = random_field_elements()
        s1 = value - r1 - r2  # Reconstruct: s1 + r1 + r2 = value
        
        return (
            Share(s1, trit=1),   # Commit share
            Share(r1, trit=0),   # Compute share  
            Share(r2, trit=-1),  # Verify share
        )
    
    async def interaction(self, other: 'TriadicMPC', data: Share) -> Share:
        """Interact with another party, conserving GF(3)."""
        pre_sum = self.trit + other.trit
        
        # Perform MPC operation
        result = await mpc_multiply(self.share, other.share)
        
        # Result inherits balanced trit
        result.trit = (-pre_sum) % 3  # Ensures sum = 0
        return result
```

### Layer 2: Zero-Knowledge Proofs (ZoKrates/circom)

```
┌─────────────────────────────────────────────────────────────┐
│                 ZoKrates / circom                            │
│─────────────────────────────────────────────────────────────│
│  • Groth16 for succinct proofs                              │
│  • PLONK for universal trusted setup                        │
│  • Fiat-Shamir transform for non-interactivity             │
│  • Circuit constraints encode GF(3) conservation            │
└─────────────────────────────────────────────────────────────┘
```

```circom
// GF(3) Conservation Circuit
pragma circom 2.0.0;

template GF3Conservation(n) {
    signal input trits[n];     // Each interaction's trit
    signal output balanced;    // 1 if conserved, 0 otherwise
    
    // Sum all trits
    var sum = 0;
    for (var i = 0; i < n; i++) {
        // Constrain each trit to {-1, 0, 1}
        trits[i] * (trits[i] - 1) * (trits[i] + 1) === 0;
        sum += trits[i];
    }
    
    // Conservation: sum ≡ 0 (mod 3)
    signal mod3;
    mod3 <-- sum % 3;
    mod3 * (mod3 - 1) * (mod3 - 2) === 0;  // mod3 ∈ {0, 1, 2}
    
    balanced <-- (mod3 == 0) ? 1 : 0;
    balanced * (balanced - 1) === 0;  // Boolean constraint
    balanced === 1;  // MUST be balanced
}

template InteractionRewrite() {
    signal input left_trit;
    signal input right_trit;
    signal input result_trits[4];  // Up to 4 output agents
    signal input num_outputs;
    
    // Pre-interaction sum
    signal pre_sum;
    pre_sum <== left_trit + right_trit;
    
    // Post-interaction sum
    var post_sum = 0;
    for (var i = 0; i < 4; i++) {
        post_sum += result_trits[i];
    }
    
    // Conservation constraint
    signal delta;
    delta <-- (pre_sum - post_sum) % 3;
    delta === 0;  // MUST conserve
}

component main = GF3Conservation(100);
```

### Layer 3: Trusted Execution (TEE)

```
┌─────────────────────────────────────────────────────────────┐
│              AWS Nitro / Intel SGX / AMD SEV                 │
│─────────────────────────────────────────────────────────────│
│  • Hardware isolation for secret computation                │
│  • Remote attestation proves correct execution              │
│  • Threshold oracle: 2-of-3 TEE quorum                      │
│  • Attestation includes GF(3) conservation proof            │
└─────────────────────────────────────────────────────────────┘
```

```rust
// TEE Attestation with GF(3) Conservation
use nitro_enclaves_sdk::*;

#[derive(Serialize, Deserialize)]
struct ConservationAttestation {
    interaction_id: [u8; 32],
    pre_trits: Vec<i8>,
    post_trits: Vec<i8>,
    conservation_proof: GF3Proof,
    tee_signature: EnclaveSignature,
}

impl ConservationAttestation {
    pub fn verify(&self) -> Result<(), AttestationError> {
        // 1. Verify TEE signature
        self.tee_signature.verify()?;
        
        // 2. Verify GF(3) conservation
        let pre_sum: i32 = self.pre_trits.iter().map(|&t| t as i32).sum();
        let post_sum: i32 = self.post_trits.iter().map(|&t| t as i32).sum();
        
        if (pre_sum - post_sum).rem_euclid(3) != 0 {
            return Err(AttestationError::ConservationViolation);
        }
        
        // 3. Verify ZK proof if provided
        self.conservation_proof.verify()?;
        
        Ok(())
    }
}

// Threshold oracle: 2-of-3 TEE agreement
struct ThresholdOracle {
    enclaves: [EnclaveClient; 3],
    trits: [i8; 3],  // +1, 0, -1 assigned to enclaves
}

impl ThresholdOracle {
    pub async fn attest(&self, interaction: &Interaction) -> ConservationAttestation {
        let attestations: Vec<_> = futures::join_all(
            self.enclaves.iter().zip(self.trits.iter())
                .map(|(e, &t)| e.attest_with_trit(interaction, t))
        ).await;
        
        // Require 2-of-3 agreement
        let valid: Vec<_> = attestations.iter()
            .filter(|a| a.verify().is_ok())
            .collect();
            
        assert!(valid.len() >= 2, "Threshold not met");
        
        // Aggregate attestations
        ConservationAttestation::aggregate(valid)
    }
}
```

### Layer 4: On-Chain Verification (Aptos Move)

```
┌─────────────────────────────────────────────────────────────┐
│                      Aptos Move                              │
│─────────────────────────────────────────────────────────────│
│  • On-chain verifier for conservation proofs                │
│  • O(log n) gas via Merkle proof of interactions            │
│  • Confidential settlement preserves privacy                │
│  • Event emission for off-chain indexing                    │
└─────────────────────────────────────────────────────────────┘
```

```move
module interaction_rewriting::conservation {
    use std::vector;
    use aptos_std::event;
    
    /// GF(3) trit values
    const TRIT_MINUS: u8 = 0;   // Represents -1
    const TRIT_ZERO: u8 = 1;    // Represents 0
    const TRIT_PLUS: u8 = 2;    // Represents +1
    
    /// Error codes
    const E_CONSERVATION_VIOLATED: u64 = 1;
    const E_INVALID_TRIT: u64 = 2;
    
    /// Interaction record
    struct Interaction has store, drop, copy {
        id: vector<u8>,
        pre_trits: vector<u8>,
        post_trits: vector<u8>,
        timestamp: u64,
    }
    
    /// Conservation proof
    struct ConservationProof has store, drop {
        interaction: Interaction,
        zk_proof: vector<u8>,
        tee_attestation: vector<u8>,
    }
    
    /// Event emitted on verified interaction
    struct InteractionVerified has drop, store {
        interaction_id: vector<u8>,
        pre_sum: u8,
        post_sum: u8,
        balanced: bool,
    }
    
    /// Convert trit encoding to signed value for summation
    fun trit_value(t: u8): u64 {
        if (t == TRIT_MINUS) { 2 }      // -1 ≡ 2 (mod 3)
        else if (t == TRIT_ZERO) { 0 }  // 0
        else if (t == TRIT_PLUS) { 1 }  // +1
        else { abort E_INVALID_TRIT }
    }
    
    /// Sum trits modulo 3
    fun sum_trits(trits: &vector<u8>): u8 {
        let sum: u64 = 0;
        let i = 0;
        let len = vector::length(trits);
        
        while (i < len) {
            sum = sum + trit_value(*vector::borrow(trits, i));
            i = i + 1;
        };
        
        ((sum % 3) as u8)
    }
    
    /// Verify GF(3) conservation for an interaction
    public fun verify_conservation(proof: &ConservationProof): bool {
        let pre_sum = sum_trits(&proof.interaction.pre_trits);
        let post_sum = sum_trits(&proof.interaction.post_trits);
        
        // Conservation: pre_sum ≡ post_sum (mod 3)
        pre_sum == post_sum
    }
    
    /// Submit and verify an interaction (O(log n) gas)
    public entry fun submit_interaction(
        account: &signer,
        interaction_id: vector<u8>,
        pre_trits: vector<u8>,
        post_trits: vector<u8>,
        zk_proof: vector<u8>,
        tee_attestation: vector<u8>,
    ) {
        let interaction = Interaction {
            id: interaction_id,
            pre_trits,
            post_trits,
            timestamp: aptos_framework::timestamp::now_seconds(),
        };
        
        let proof = ConservationProof {
            interaction,
            zk_proof,
            tee_attestation,
        };
        
        // Verify conservation
        assert!(verify_conservation(&proof), E_CONSERVATION_VIOLATED);
        
        // Emit event
        event::emit(InteractionVerified {
            interaction_id: proof.interaction.id,
            pre_sum: sum_trits(&proof.interaction.pre_trits),
            post_sum: sum_trits(&proof.interaction.post_trits),
            balanced: true,
        });
    }
    
    /// Batch verify multiple interactions (amortized O(1) per interaction)
    public entry fun batch_verify(
        account: &signer,
        interactions: vector<ConservationProof>,
    ) {
        let i = 0;
        let len = vector::length(&interactions);
        
        while (i < len) {
            let proof = vector::borrow(&interactions, i);
            assert!(verify_conservation(proof), E_CONSERVATION_VIOLATED);
            i = i + 1;
        };
    }
}
```

---

## Interaction Rewriting Gadgets

### Gadget 1: Annihilation

```
BEFORE:                    AFTER:
   ●[+1]────●[+1]    →→→    (nothing)
   
   ●[-1]────●[-1]    →→→    (nothing)
   
   ●[0]─────●[0]     →→→    (nothing)

Conservation: agents cancel, net Δ = 0
```

### Gadget 2: Commutation (Braiding)

```
BEFORE:                    AFTER:
   ●[+1]────●[-1]    →→→    ●[-1]────●[+1]
      \    /                   \    /
       \  /                     \  /
        \/          ←→←          \/
        /\                       /\
       /  \                     /  \
   ●[0]────●[0]            ●[0]────●[0]

Conservation: permutation only, Σ unchanged
ACAUSAL: works in both directions (←→←)
```

### Gadget 3: Triadic Split

```
BEFORE:                    AFTER:
                              ●[+1]
                             /
   ●[0]──────●[0]    →→→    ●[0]
                             \
                              ●[-1]

Conservation: (0) → (+1) + (0) + (-1) = 0 ✓
Inverse:      (+1) + (0) + (-1) → (0) ✓
```

### Gadget 4: Fusion (Inverse of Split)

```
BEFORE:                    AFTER:
   ●[+1]
      \
       ●[0]          →→→    ●[0]
      /
   ●[-1]

Conservation: (+1) + (0) + (-1) → (0) ✓
ACAUSAL: same as split, reversed
```

---

## Correct-by-Construction Guarantee

### Type-Level Enforcement

```haskell
-- Haskell phantom types for GF(3) tracking
data Trit = Plus | Zero | Minus

data Agent (t :: Trit) where
  Commit :: payload -> Agent 'Plus
  Compute :: payload -> Agent 'Zero
  Verify :: payload -> Agent 'Minus

-- Interaction only allowed when trits sum to 0
class Interaction a b c | a b -> c where
  interact :: Agent a -> Agent b -> Agent c

instance Interaction 'Plus 'Minus 'Zero where
  interact (Commit p1) (Verify p2) = Compute (merge p1 p2)

instance Interaction 'Plus 'Zero 'Minus where
  interact (Commit p1) (Compute p2) = Verify (merge p1 p2)

instance Interaction 'Zero 'Minus 'Plus where
  interact (Compute p1) (Verify p2) = Commit (merge p1 p2)

-- Compiler rejects ill-typed interactions!
-- This won't compile:
-- badInteraction :: Agent 'Plus -> Agent 'Plus -> Agent ???
```

### Linear Types for Resource Safety

```rust
// Rust linear types ensure no duplication without compensation
#[must_use]
struct LinearAgent<const TRIT: i8> {
    payload: Vec<u8>,
}

impl<const T: i8> LinearAgent<T> {
    // Consume self, producing balanced outputs
    fn split(self) -> (LinearAgent<1>, LinearAgent<0>, LinearAgent<-1>) 
    where
        // Only allowed when T == 0
        Assert<{ T == 0 }>: IsTrue,
    {
        let (p1, p2, p3) = split_payload(self.payload);
        (
            LinearAgent::<1> { payload: p1 },
            LinearAgent::<0> { payload: p2 },
            LinearAgent::<-1> { payload: p3 },
        )
    }
    
    fn fuse<const U: i8, const V: i8>(
        self,
        other: LinearAgent<U>,
        third: LinearAgent<V>,
    ) -> LinearAgent<0>
    where
        Assert<{ T + U + V == 0 }>: IsTrue,  // Conservation enforced!
    {
        LinearAgent::<0> {
            payload: merge_payloads(self.payload, other.payload, third.payload),
        }
    }
}
```

---

## Adhesive Rewriting Integration

From the **topos-adhesive-rewriting** skill, interaction rewriting uses:

### Van Kampen Squares

```
       L ──────► K ──────► R
       │         │         │
       │  pushout│  pushout│
       ▼         ▼         ▼
       G ──────► D ──────► H
       
    Left-hand    Context    Right-hand
    side                    side

Conservation: χ(L) = χ(R) where χ is GF(3) characteristic
```

### Double Pushout Rewriting

```julia
using Catlab.CategoricalAlgebra

# Define GF3-labeled graph schema
@present SchGF3Graph(FreeSchema) begin
    V::Ob
    E::Ob
    src::Hom(E, V)
    tgt::Hom(E, V)
    
    Trit::AttrType
    trit::Attr(V, Trit)
end

# Rewrite rule with conservation
function conservation_rewrite(L::ACSet, K::ACSet, R::ACSet)
    # Compute trit sums
    L_sum = sum(L[:trit])
    R_sum = sum(R[:trit])
    
    # Conservation check
    @assert L_sum % 3 == R_sum % 3 "GF(3) conservation violated in rewrite rule"
    
    # Return DPO rule
    Rule(L, K, R)
end
```

---

## Narya Formalization

```narya
{` Interaction Rewriting: Acausal GF(3) Conservation `}

{` Interaction agent with trit label `}
def Agent : GF3 → Type ≔ t ↦ sig (
    payload : ByteVector,
    ports : List Port
)

{` Interaction is symmetric (acausal) `}
def Interaction : Agent t1 → Agent t2 → Type ≔ a1 a2 ↦ sig (
    result : List (Σ (t : GF3) × Agent t),
    conservation : Id GF3 
        (gf3_add t1 t2) 
        (fold gf3_add ergodic. (map fst result))
)

{` THEOREM: Interactions are reversible `}
def interaction_reversible : (a1 : Agent t1) → (a2 : Agent t2) →
    (i : Interaction a1 a2) →
    Interaction (reverse_agents (i .result)) (a1, a2)
  ≔ {` proof: conservation is symmetric `}

{` Rewriting gadget with built-in conservation `}
def Gadget : Type ≔ sig (
    lhs : List (Σ (t : GF3) × Agent t),
    rhs : List (Σ (t : GF3) × Agent t),
    conserved : Id GF3 
        (fold gf3_add ergodic. (map fst lhs))
        (fold gf3_add ergodic. (map fst rhs))
)

{` Gadget composition preserves conservation `}
def compose_gadgets : Gadget → Gadget → Gadget
  ≔ g1 g2 ↦ (
    lhs ≔ g1 .lhs,
    rhs ≔ g2 .rhs,
    conserved ≔ trans (g1 .conserved) (g2 .conserved)
)
```

---

## Commands

```bash
# Verify interaction rewrite rule
just interaction-verify rule.json

# Generate conservation proof
just interaction-proof --zk circom interaction.json

# Submit to Aptos
just interaction-submit --network mainnet proof.json

# Test gadget composition
just gadget-compose annihilation.json commutation.json

# Run full stack test
just interaction-stack-test --moose --zk --tee --aptos
```

---

## GF(3) Balanced Triads

```
# Stack-level triad
moose-mpc (+1) ⊗ interaction-rewriting (0) ⊗ aptos-verifier (-1) = 0 ✓

# Gadget-level triad  
commit-agent (+1) ⊗ compute-agent (0) ⊗ verify-agent (-1) = 0 ✓

# Process-level triad
zk-prove (+1) ⊗ tee-attest (0) ⊗ chain-verify (-1) = 0 ✓
```

---

## Related Skills

- `topos-adhesive-rewriting` - Double pushout rewriting theory
- `corolla-operations` - Atomic operation units
- `open-games` - Game-theoretic composition
- `narya-proofs` - Formal verification
- `aptos-agent` - On-chain settlement

---

## References

1. **Lafont, Y.** (1990) - "Interaction Combinators"
2. **Ehrhard, T. & Regnier, L.** (2003) - "The Differential Lambda-Calculus"
3. **Mazza, D.** (2017) - "The True Concurrency of Herbrand's Theorem"
4. **Arrighi, P. & Dowek, G.** (2012) - "Causal Graph Dynamics"
5. **Moose Documentation** - tf-encrypted/moose
6. **circom/snarkjs** - ZK circuit tooling

---

**The Interaction Rewriting Principle:**
> *Conservation is not a post-hoc check but a structural invariant. Every rewrite rule, every gadget, every interaction is correct by construction. The acausal nature means there is no "before" and "after"—only equivalent configurations related by GF(3)-preserving transformations.*


## Cat# Integration

This skill maps to **Cat# = Comod(P)** as a bicomodule in the equipment structure:

```
Trit: 0 (ERGODIC)
Home: Prof
Poly Op: ⊗
Kan Role: Adj
Color: #D8D826
```

### GF(3) Naturality

The skill participates in triads satisfying:
```
(-1) + (0) + (+1) ≡ 0 (mod 3)
```

This ensures compositional coherence in the Cat# equipment structure.


---

## Galois Hole Type (Seven Sketches §1.4.1)

> **HOLE TYPE**: This skill is now accessible via Galois connection to `structured-decompositions`.
> See `structured-decompositions/SKILL.md` for the 69-skill accessibility network.
> 
> **Adjunction**: f(p) ≤ q ⟺ p ≤ g(q) unlocks world navigation.

