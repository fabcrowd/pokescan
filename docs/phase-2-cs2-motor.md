# Phase 2 — CS2 Motorized Eject Spec

Servo-driven card eject for the CS2 hopper. Replaces the manual push in Phase-2a.

---

## Overview

An SG90 micro-servo mounts on the hopper front face via `cs2_motor_bracket.stl`. A crank arm (`cs2_crank_arm.stl`) attaches to the servo D-flat shaft at z=28mm; a push rod (`cs2_push_rod.stl`) links the crank tip to a card-exit anchor at z=6mm (the 15×4mm exit slot). A full 90° arm swing ejects one card through the slot. A rubber O-ring roller (`cs2_roller.stl`) on a 6mm steel shaft beneath the exit slot guides the card out.

---

## Hardware BOM

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| SG90 micro-servo | 22.5×12×22mm body, 5V, ~1.8 kg·cm, D-flat shaft 4.7mm | 1 | Standard RC hobby servo; TowerPro SG90 or clone |
| M3×8 SHCS | M3, 8mm socket head | 4 | Mount bracket to hopper front face (bx=±15mm, bz=18mm+36mm) |
| 6mm steel shaft | 6mm OD, 30mm long | 1 | Roller axle; cut from 6mm rod stock |
| 3mm steel pin | 3mm OD, 10mm long | 2 | Crank arm tip ↔ push rod pivot |
| Rubber O-ring | ~8mm OD, 1mm section | 2–3 | Slide over roller stubs for grip; glue or press-fit |
| Dupont / JST lead | 3-pin servo extension, 150mm | 1 | Connects servo to controller |
| Zip ties | 2.5mm width | 2 | Secure servo wiring to bracket slots |

---

## Print specs

| STL | Dims (mm) | Qty | Material | Orientation | Infill | Notes |
|-----|-----------|-----|----------|-------------|--------|-------|
| `cs2_motor_bracket.stl` | 42×15×32 | 1 | PLA or PETG | Flat (plate face down) | 30% | Structural — 4 bolt holes, must not crack under servo torque |
| `cs2_roller.stl` | 8 OD × 15 | 1 | **PETG** | Upright (axis vertical) | 40% | PETG for wear resistance; press-fit bore 5.8mm on 6mm shaft |
| `cs2_crank_arm.stl` | 29×9×6 | 1 | PLA | Flat (hub base down) | 30% | D-flat bore 4.7mm+CL; print flat, Z=6mm |
| `cs2_push_rod.stl` | 31×5×3 | 1 | PLA | Flat | 20% | Thin — use brim; 3mm pin sockets at each end |

Print `cs2_crank_arm.stl` first to test D-flat bore fit on the servo shaft. If tight, increase bore radius by 0.05mm and reprint.

---

## Servo sourcing

SG90 servos are available from:
- Adafruit, Sparkfun, Pololu (US)
- HobbyKing, LCSC (international)
- Amazon / eBay — "SG90 micro servo" (clone acceptable for prototype)

Buy 2 — one to install, one spare for bench testing the crank geometry.

---

## Servo bracket geometry

From `design/cs2_motor_bracket.py`:

| Constant | Value | Description |
|----------|-------|-------------|
| PLATE_W | 42mm | Plate width (X) |
| PLATE_T | 3mm | Plate thickness (Y into hopper wall) |
| PLATE_H | 32mm | Plate height (Z) |
| CRADLE_OW | 28mm | Cradle outer width (servo body + clearance) |
| CRADLE_OD | 12mm | Cradle depth (servo body 12mm) |
| CHAN_Z0 | 17mm | Servo body base Z |
| CHAN_H | 23mm | Servo channel height (body 22mm + 1mm) |
| SHAFT_Z | 28mm | Servo shaft Z above bracket base |
| BOSS_BX | ±15mm | Bolt hole X positions |
| BOSS_BZ | 18mm, 36mm | Bolt hole Z positions |

Bolt hole positions match `cs2_hopper.py` boss holes exactly (bx=±15mm, bz=18mm+36mm).

---

## Crank arm geometry

From `design/cs2_card_pusher.py`:

| Constant | Value | Description |
|----------|-------|-------------|
| SHAFT_Z | 28mm | Servo shaft Z (arm pivot) |
| ARM_L | 22mm | Moment arm length (= SHAFT_Z − EXIT_Z) |
| EXIT_Z | 6mm | Exit slot Z centre |
| HUB_OD | 9mm | Hub boss outer diameter |
| HUB_L | 6mm | Hub boss depth on shaft |
| BORE_R | 2.5mm | D-flat bore radius (4.7/2 + 0.15mm CL) |
| PIN_D | 3mm | Pin socket diameter (tip → push rod) |
| ROD_L | 31mm | Push rod length (√(22² + 22²) ≈ 31.1mm) |

At full 90° throw, arm tip descends from (22, y, 28mm) → (0, y, 6mm), exactly reaching the exit slot centre.

---

## Assembly sequence

1. **Roller install**: press-fit cs2_roller onto 6mm shaft; slide into channel slot at base of exit slot (z≈6mm). Snap O-ring over roller stub ends.
2. **Bracket mount**: bolt cs2_motor_bracket to hopper front face with 4× M3×8 (loctite on threads). Torque: hand-tight + 1/4 turn.
3. **Servo mount**: slide SG90 into bracket cradle, channel side first. Route wiring through zip-tie slots; close with 2 zip ties.
4. **Crank arm**: press cs2_crank_arm D-flat bore onto servo shaft at 0° position (arm pointing in +X, hopper side). Confirm arm tip is at z≈28mm, x≈22mm.
5. **Push rod**: insert 3mm pins into crank tip socket and anchor bracket socket. Connect push rod between pins.
6. **Test sweep**: command servo 0° → 90° and verify arm tip reaches z=6mm at the exit slot opening.
7. **Card test**: load 3 cards in hopper, command eject sweep; verify push rod tip enters at z=6mm
   and contacts bottom card. Card exits through the hopper exit opening (see Open Items below).

---

## Open Items — Phase-2 CAD required before print

All items resolved in cs2_hopper.py v4 (2026-06-28):

| Item | Resolution |
|------|-----------|
| Card exit opening in hopper wall | EXIT_W widened 15→90mm (= SLOT_L). Front wall now has 90×4mm opening at z=4mm — card (88mm) exits with 1mm clearance each side through the same front-face opening as the push-rod arm. |
| Hopper SHAFT_Z 8mm → 12.5mm (roller v2) | SHAFT_Z updated; peg holes moved z=17→19mm (2mm clearance from shaft top at z=15.5mm). |

**Hopper halves are now ready to reprint.** Use `design/output/cs2_hopper_left.stl` and `cs2_hopper_right.stl` (v4).

---

## Dependencies

- `cs2_card_pusher.py` — designed (v1, 2026-06-28). Crank arm + push rod STLs exported to `design/output/`.
- `cs2_motor_bracket.py` — validated (v1). Bracket STL exported. Print hold removed.
- `cs2_roller.py` — validated (v1). Roller STL exported.
- Controller (ESP32 / Arduino) — not yet specified. See `docs/phase-3a-servo-feeder.md` for open questions on power and trigger logic.
