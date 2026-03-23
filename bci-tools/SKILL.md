---
name: bci-tools
description: "Brain-Computer Interface hardware bridge: CatSharp Galois adjunctions grounded to physical substrates via Seeed Studio NFC, I2C/SPI connectors, and solder-level prototyping"
trit: -1
color: "#7B2FBE"
triggers:
  - bci
  - brain computer interface
  - hardware bridge
  - nfc seeed
  - neural interface
  - catsharp hardware
---

# BCI Tools Skill

**Trit**: -1 (MINUS - Grounding/Absorber)
**Color**: #7B2FBE (Violet-Purple)

## Overview

Bridges the CatSharp Galois adjunction (α ⊣ γ) from categorical abstraction down to **physical hardware substrates**. Where `catsharp-galois` operates on pitch classes and hyperedges, `bci-tools` grounds those signals into voltage, NFC tags, and solder joints.

```
           α (abstract)
    BODY ──────────────→ MIND
      ↑                    │
      │                    │ γ (concretize)
      │    ┌────────────┐  │
      └────│ BCI Tools  │──┘
           │ (Hardware)  │
           └────────────┘

    GF(3): catsharp-galois(0) + bci-tools(-1) + ordered-locale(+1) = 0 ✓
```

- **BODY** (HERE): Physical hardware — NFC readers, I2C buses, solder connections
- **MIND** (ELSEWHERE): CatSharp categorical abstractions, Galois adjunctions
- **BRIDGE**: BCI Tools — the grounding functor γ that concretizes abstract trits into hardware signals

## Hardware Component Inventory

### Seeed Studio NFC/RFID Module

| Parameter | Value |
|-----------|-------|
| Protocol | ISO 14443A/B, ISO 15693 |
| Interface | I2C / SPI |
| Frequency | 13.56 MHz |
| GF(3) Role | Tag read = +1 (sense), idle = 0 (wait), tag write = -1 (ground) |

### I2C/SPI Connector Cable

| Wire | Color | Function | Trit Mapping |
|------|-------|----------|--------------|
| VCC | Red | Power supply | +1 (generation) |
| GND | Black | Ground return | -1 (absorption) |
| SDA/MOSI | Blue | Data line | 0 (ergodic transfer) |
| SCL/SCLK | Yellow | Clock line | 0 (ergodic sync) |

### Soldering Infrastructure

| Component | Purpose | GF(3) Phase |
|-----------|---------|-------------|
| Rosin paste flux | Surface preparation | -1 (MINUS: clean/absorb oxide) |
| Solder wire | Joint creation | +1 (PLUS: generate connection) |
| Iron tip | Heat transfer | 0 (ERGODIC: bridge thermal energy) |

## Galois Connection: Hardware ↔ Category

The adjunction grounds abstract CatSharp operations to physical signals:

```
γ-ground : CatSharp Hyperedge → Hardware Signal
α-sense  : Hardware Signal → CatSharp Hyperedge

γ-ground(:generation)     = VCC HIGH  (NFC tag detected)
γ-ground(:verification)   = CLK EDGE  (I2C acknowledge)
γ-ground(:transformation) = DATA BYTE (SPI transfer)

α-sense(NFC_UID)     = {:hyperedge :generation,  :trit +1}
α-sense(I2C_ACK)     = {:hyperedge :verification, :trit  0}
α-sense(SPI_BYTE)    = {:hyperedge :transformation, :trit -1}
```

### Adjunction Verification

```clojure
(defn γ-ground
  "Ground functor: CatSharp → Hardware signal"
  [hyperedge]
  (case (:hyperedge hyperedge)
    :generation     {:signal :nfc-detect  :voltage 3.3 :trit  1}
    :verification   {:signal :i2c-ack     :voltage 0.0 :trit  0}
    :transformation {:signal :spi-byte    :voltage nil :trit -1}))

(defn α-sense
  "Sense functor: Hardware signal → CatSharp"
  [hw-signal]
  (let [trit (case (:signal hw-signal)
               :nfc-detect  1
               :i2c-ack     0
               :spi-byte   -1)]
    {:type :elsewhere
     :hyperedge (case trit
                  1  :generation
                  0  :verification
                  -1 :transformation)
     :source-trit trit}))

;; Roundtrip: α(γ(e)) ≤ e and h ≤ γ(α(h))
(defn verify-bci-adjunction [hyperedge hw-signal]
  (and (= hyperedge (α-sense (γ-ground hyperedge)))
       (= (:trit hw-signal) (:trit (γ-ground (α-sense hw-signal))))))
```

## NFC Tag Protocol

Each NFC tag encodes a GF(3) trit bundle:

```
Tag Memory Layout (NTAG213, 144 bytes):
┌─────────────┬──────────┬───────────┬──────────────┐
│ Byte 0-3    │ Byte 4   │ Byte 5-8  │ Byte 9+      │
│ UID (4B)    │ Trit χ   │ Seed (4B) │ Payload      │
│             │ {FF,00,01}│ SplitMix64│ Gay.jl color │
└─────────────┴──────────┴───────────┴──────────────┘

Trit encoding:
  0xFF → -1 (MINUS)
  0x00 →  0 (ERGODIC)
  0x01 → +1 (PLUS)
```

### Tag Read/Write Cycle

```python
import board
import busio
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)

def read_trit_tag():
    """α-sense: Read NFC tag → CatSharp trit"""
    uid = pn532.read_passive_target()
    if uid is None:
        return None
    data = pn532.ntag2xx_read_block(4)
    trit_byte = data[0]
    trit = {0xFF: -1, 0x00: 0, 0x01: 1}[trit_byte]
    seed = int.from_bytes(data[1:5], 'big')
    return {"trit": trit, "seed": seed, "uid": uid.hex()}

def write_trit_tag(trit, seed):
    """γ-ground: Write CatSharp trit → NFC tag"""
    uid = pn532.read_passive_target()
    if uid is None:
        raise IOError("No tag present")
    trit_byte = {-1: 0xFF, 0: 0x00, 1: 0x01}[trit]
    data = bytes([trit_byte]) + seed.to_bytes(4, 'big')
    pn532.ntag2xx_write_block(4, data[:4])
```

## I2C Bus Topology

```
                    ┌──────────┐
                    │  MCU     │
                    │ (ESP32)  │
                    └────┬─────┘
                         │ I2C Bus (SDA + SCL)
           ┌─────────────┼─────────────┐
           │             │             │
    ┌──────┴──────┐ ┌────┴────┐ ┌─────┴─────┐
    │ NFC Reader  │ │ LED     │ │ Sensor    │
    │ PN532 (0x24)│ │ Driver  │ │ Array     │
    │ trit: +1    │ │ trit: 0 │ │ trit: -1  │
    │ (sense)     │ │ (bridge)│ │ (absorb)  │
    └─────────────┘ └─────────┘ └───────────┘

    Σ trits = (+1) + (0) + (-1) = 0 ✓
```

## GF(3) Triads

```
bci-tools (-1) ⊗ catsharp-galois (0) ⊗ ordered-locale (+1) = 0 ✓
bci-tools (-1) ⊗ catsharp-sonification (0) ⊗ gay-mcp (+1) = 0 ✓  (hypothetical)
```

## Commands

```bash
# Scan for NFC tags and report trit values
just bci-scan

# Write a trit bundle to NFC tag
just bci-write trit=-1 seed=0x42D

# Bridge: read NFC → CatSharp sonification
just bci-sonify

# Verify hardware Galois adjunction roundtrip
just bci-verify
```

## Bill of Materials

| Item | Qty | Purpose |
|------|-----|---------|
| Seeed Studio NFC/RFID module (PN532) | 1 | Tag read/write |
| I2C jumper cable (4-pin) | 1 | Bus connection |
| Rosin paste flux | 1 | Solder prep |
| Lead-free solder wire | 1 | Joint creation |
| ESP32 or RPi Pico | 1 | MCU host |
| NTAG213 NFC stickers | N | Trit-encoded tags |

## Related Skills

- `catsharp-galois` (0): The abstract Galois adjunction this skill grounds
- `catsharp-sonification` (0): Sonify the signals read from hardware
- `ordered-locale` (+1): Frame structure completing the GF(3) triad
- `gay-mcp` (-1): SplitMix64 seed generation for NFC tag payloads

## References

- Seeed Studio PN532 NFC/RFID Module Datasheet
- NXP NTAG213/215/216 Application Note
- Adafruit CircuitPython PN532 Library
- Mazzola, G. *The Topos of Music* (2002) — categorical grounding
- Powers (1973) — Behavior: The Control of Perception


## Scientific Skill Interleaving

This skill connects to the K-Dense-AI/claude-scientific-skills ecosystem:

### Graph Theory
- **networkx** [O] via bicomodule
  - Universal graph hub

### Bibliography References

- `neuroscience`: BCI hardware grounding
- `category-theory`: Galois adjunction formalization

## Cat# Integration

This skill maps to **Cat# = Comod(P)** as a bicomodule in the equipment structure:

```
Trit: -1 (MINUS)
Home: Prof
Poly Op: ⊗
Kan Role: Adj
Color: #7B2FBE
```

### GF(3) Naturality

The skill participates in triads satisfying:
```
(-1) + (0) + (+1) ≡ 0 (mod 3)
```

This ensures compositional coherence in the Cat# equipment structure.


---

## Galois Hole Type (Seven Sketches S1.4.1)

> **HOLE TYPE**: This skill is now accessible via Galois connection to `structured-decompositions`.
> See `structured-decompositions/SKILL.md` for the 69-skill accessibility network.
>
> **Adjunction**: f(p) ≤ q ⟺ p ≤ g(q) unlocks world navigation.
