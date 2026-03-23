# BCI Tools — Hardware Bridge for CatSharp Galois

Physical substrate grounding for the `catsharp-galois` Galois adjunction.

## Hardware Stack

```
Layer 3: CatSharp Galois (categorical, trit 0)
Layer 2: BCI Tools bridge (this skill, trit -1)
Layer 1: Physical hardware (NFC, I2C, solder joints)
```

## Quick Start

### 1. Wire the NFC Reader

```
ESP32/RPi Pico    PN532 NFC Module
─────────────     ────────────────
3V3          ───→ VCC (Red)
GND          ───→ GND (Black)
SDA (GPIO21) ───→ SDA (Blue)
SCL (GPIO22) ───→ SCL (Yellow)
```

### 2. Flash Trit Tags

Write GF(3) trit values to NTAG213 stickers:

```python
# Tag encodes: trit (-1/0/+1) + SplitMix64 seed + Gay.jl color
write_trit_tag(trit=-1, seed=0x42D)
```

### 3. Read → Sonify Pipeline

```
NFC tag tap → α-sense → CatSharp pitch class → sox tone
```

## Component Photos

The following hardware was identified for this build:

1. **Rosin paste flux** — oxide removal for reliable solder joints
2. **Soldering iron + solder wire** — physical connection fabrication
3. **I2C jumper cable** (4-pin: VCC/GND/SDA/SCL) — bus interconnect
4. **Seeed Studio NFC/RFID module** (PN532-based) — tag read/write interface

## GF(3) Conservation

This skill completes the hardware triad:

| Skill | Trit | Layer |
|-------|------|-------|
| `ordered-locale` | +1 | Frame structure (abstract) |
| `catsharp-galois` | 0 | Galois bridge (categorical) |
| `bci-tools` | -1 | Hardware ground (physical) |
| **Sum** | **0** | **Conserved** |
