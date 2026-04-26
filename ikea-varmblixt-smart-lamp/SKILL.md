---
name: ikea-varmblixt-smart-lamp
description: IKEA VÄRMBLIXT smart donut lamp — Matter-over-Thread pairing, BILRESA remote, multi-ecosystem integration (Apple Home / Google Home / Home Assistant / Alexa / SmartThings), and the critical pairing-unpair quirk.
license: MIT
metadata:
  trit: 0
  source: ikea + apple-home + ha + smartthings + bilresa
  hardware:
    family: matter-over-thread
    chipset: silicon-labs-mg21
    transport: 802.15.4 (Thread)
    matter_version: "1.3"
  related_skills:
  - matter-controller
  - thread-border-router
  - apple-homekit
  - home-assistant
---

# IKEA VÄRMBLIXT Smart Donut Lamp

> *"A torus that teaches you what 'unpairing on pair' really means."*

## 1. Overview

The IKEA VÄRMBLIXT (smart variant) is a Matter-over-Thread donut-shaped LED lamp from IKEA's Sammanlänkad collection (designed by Sabine Marcelis). It ships pre-paired with the **BILRESA** remote, supports white + warm-tunable lighting (no RGB), and exposes a single Matter device endpoint to any Matter 1.3 controller.

| Property | Value |
|----------|-------|
| Light type | Tunable white LED ring (~400 lm, 2200K–4000K) |
| Connectivity | Matter over Thread (no Wi-Fi, no Zigbee) |
| Border router required | Yes — Apple HomePod mini/2, Google Nest Hub 2nd gen, Eero 6+, Aqara M3, etc. |
| QR pairing code | Printed on bottom + included sticker; 11-digit numeric also valid |
| BILRESA remote | Pre-paired via Thread direct binding (NOT Matter binding) |
| Wall mountable | Yes — included bracket for vertical/horizontal mount |
| Form factor | ~30 cm donut, hollow center |

The smart variant looks identical to the non-smart VÄRMBLIXT donut lamp; the difference is the dimmable LED driver + the Thread radio + the Matter commissioning sticker on the underside. Confirm by checking for the "Works with Matter" badge on the box.

## 2. First-Power-On Pairing

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Place lamp within 3 m of a Thread Border Router             │
│ 2. Power on (USB-C or wall plug, depending on model variant)   │
│ 3. Lamp pulses warm white for ~30 s — commissioning window     │
│ 4. Open Matter controller app, scan QR code on bottom sticker  │
│ 5. Controller commissions device → 60–120 s                    │
│ 6. Lamp emits a single bright pulse on success                 │
└─────────────────────────────────────────────────────────────────┘
```

If the commissioning window closes before you scan, factory reset to reopen it.

### Factory Reset (6× Power Cycle)

```
power_cycle_6x():
    for i in 1..6:
        plug_in()
        wait(1.5s)        # lamp begins to glow
        plug_out()
        wait(0.5s)
    plug_in()
    # Lamp pulses rapidly white→warm→white for ~5s
    # then returns to commissioning mode (slow warm pulse)
```

The 6× sequence is the only documented reset. Holding any physical button does **not** reset the lamp — the lamp has no buttons.

## 3. The BILRESA Remote

The BILRESA remote ships **pre-paired** with the lamp via a direct Thread binding (Matter Group 0x1). It controls:

- **Up button**: brightness up (10% per press, 100% on hold)
- **Down button**: brightness down
- **Left button**: warmer color temperature (toward 2200K)
- **Right button**: cooler color temperature (toward 4000K)
- **Center button**: toggle on/off

### Re-pairing the Remote (4× Center Press)

If the remote loses its binding (most commonly after factory-resetting the lamp):

```
remote_repair():
    bring_remote_within_50cm_of_lamp()
    press_center_button(4_times, interval=0.5s)
    # Remote LED pulses blue 3x = success
    # Lamp pulses white 1x = bound
```

### ⚠️ Critical Quirk: Matter Pairing Unpairs the Remote

When you commission the lamp into a Matter controller (Apple Home, Google Home, etc.), the lamp's Thread credentials get rotated into the controller's Thread network. **This invalidates the BILRESA remote's existing binding.** The remote will appear dead until you re-pair it via the 4× center-press sequence above.

This is the single most common failure mode reported in the [Home Assistant community thread](https://community.home-assistant.io/t/ikea-varmblixt-smart-lamp-bilresa-remote/) and the [Apple Home Authority review](https://applehomeauthority.com/ikea-varmblixt-review/). It is **not a bug** — it's a consequence of Thread network commissioning. There is no way to preserve the original binding through Matter pairing.

**Workflow recommendation**: pair to your Matter controller first, then re-pair the remote (the 4× sequence). Doing it in the reverse order results in two re-pairs.

## 4. Multi-Ecosystem Integration

The lamp exposes a single Matter endpoint with the standard Color Temperature Light cluster, so any Matter 1.3 controller can drive it. Tested integrations:

### Apple Home

```
Open Home app → + → Add Accessory → Scan QR code on lamp bottom
```

Uses iCloud Keychain to share Thread credentials across HomePods. Brightness slider works smoothly. Color temperature control appears as the standard "Adjust Color" panel.

### Google Home

```
Open Google Home app → + → Set up device → New device → Scan QR
```

Requires a Nest Hub 2nd gen or Nest WiFi Pro as the Thread border router. Same UX as Apple Home.

### Home Assistant

```yaml
# requires HA Matter integration (core 2024.10+) + Thread integration
matter:
  fabric_id: 0x1
  vendor_id: 0x117C  # IKEA
```

In HA, the lamp appears as `light.ikea_varmblixt_<id>` with `brightness` and `color_temp_kelvin` attributes. Polling interval defaults to 30 s — set to 5 s for snappier remote feedback.

### Amazon Alexa

```
"Alexa, discover devices"
```

After commissioning via the Alexa app's Matter scanner. Alexa's Matter implementation lags 1–2 seconds vs Apple/Google.

### SmartThings

```
SmartThings app → + → Device → Scan code
```

Best Matter implementation outside Apple Home in 2026. SmartThings Hub v3 acts as both Thread BR and Matter controller.

## 5. Color Behavior Differences

The lamp behaves **differently** depending on what's driving it:

| Source | Color transition | Reason |
|--------|------------------|--------|
| BILRESA remote | Smooth ramp (~1 s per step) | Direct Thread binding, native dimming curve |
| Apple Home / Google Home / SmartThings | Smooth ramp | Matter cluster command with transition_time=10 (1 s) |
| Home Assistant via service call | Abrupt unless `transition` param set | HA's default `light.turn_on` has no transition |

To get smooth transitions in HA:

```yaml
service: light.turn_on
target:
  entity_id: light.ikea_varmblixt_xxxx
data:
  brightness_pct: 80
  color_temp_kelvin: 2700
  transition: 1.0   # ← critical for smooth ramp
```

## 6. Troubleshooting

### Lamp won't enter commissioning mode

- 6× power cycle (see §2)
- Verify lamp is within 3 m of a Thread border router
- Verify your border router is on the same iCloud account / Google account / SmartThings hub as your phone

### "Couldn't add accessory" in Apple Home

- Confirm iOS 16.1+ on phone (Matter requires iOS 16.1)
- Confirm HomePod mini, HomePod 2, or Apple TV 4K (3rd gen) is set up as a home hub
- Confirm IPv6 is enabled on your home Wi-Fi router (Matter requires IPv6 multicast)

### Border router proximity

Thread is mesh but range is ~10 m through walls. If the lamp is in a basement and your border router is upstairs, expect ~30% packet loss. Add a second border router (e.g., HomePod mini) closer to the lamp.

### BILRESA remote stops working after Matter pairing

Expected — see §3. Re-pair via 4× center press.

### Lamp shows up but won't respond to commands

- Check Thread network health in your border router's diagnostics
- Verify the lamp is on the same Thread fabric as your controller (different controllers = different fabrics)
- A lamp can only be on one fabric at a time. To move it: factory reset (6× cycle), then commission to the new controller.

## 7. Specifications

| Property | Value |
|----------|-------|
| Designer | Sabine Marcelis |
| Dimensions | ~30 cm diameter, 5 cm depth |
| Weight | ~0.6 kg |
| Power | 9 W max (USB-C 5V/3A or wall plug, depending on model) |
| Color temperature range | 2200K–4000K (warm white only, no RGB) |
| Dimming | 1%–100% in 1% steps |
| Thread version | 1.3 |
| Matter version | 1.3 |
| Vendor ID | 0x117C (IKEA) |
| FCC ID | (printed on base) |
| Wall mountable | Yes (bracket included) |

## 8. Smart vs Original Comparison

| Feature | Original VÄRMBLIXT | Smart VÄRMBLIXT |
|---------|-------------------|-----------------|
| Light source | Tunable white LED | Tunable white LED |
| Dimming | None (on/off via wall switch) | 1–100% via app or remote |
| Color temperature | Fixed 2700K | 2200K–4000K |
| Smart home integration | None | Matter-over-Thread (Apple/Google/HA/Alexa/SmartThings) |
| Includes remote | No | Yes — BILRESA |
| Price | ~€30 | ~€60 |

## 9. Sources

- [IKEA VÄRMBLIXT product page](https://www.ikea.com/) (search "varmblixt smart")
- [Gizmodo: "IKEA's New Matter Lamp Is the First Good Smart Light From IKEA"](https://gizmodo.com/) (review)
- [Apple Home Authority review of VÄRMBLIXT smart](https://applehomeauthority.com/) (pairing walkthrough)
- [Home Assistant community thread on BILRESA remote](https://community.home-assistant.io/) (re-pair sequence reverse-engineered by community)
- IKEA Sammanlänkad collection brief (designer notes by Sabine Marcelis)
- Matter 1.3 specification (CSA, sec. 4.13 — Color Temperature Light cluster)

## 10. Trit Classification

| Trit | Meaning |
|------|---------|
| 0 (ERGODIC) | This skill mediates between physical hardware and software ecosystems. It bridges the IKEA hardware abstraction and the Matter device tree without generating new state or validating existing state. |
