# Phase 3a — Servo Feeder (Original Stand) Planning Spec

Servo-driven card feed through the existing `PUSHER_SLOT` horn slot in the `card_lane_left` STL.

This is a **planning document only** — no CAD has been created for Phase-3a yet.
For the CS2 hopper motorized eject, see `docs/phase-2-cs2-motor.md`.

---

## Overview

The original stand (built from `build_woodstand.py`) has a gravity card lane (`card_lane_left/right`). Phase-2a adds a manual feeder. Phase-3a automates the push step with an SG90 servo mounted inside the column base or stand foot, driving a horn arm through the `PUSHER_SLOT` cut in `card_lane_left`.

---

## Geometry constraints

All constants from `old designs/root/build_woodstand.py`:

| Constant | Value | Description |
|----------|-------|-------------|
| `PUSHER_SLOT_W` | 20mm | Horn slot width (X) in card_lane_left; servo arm sweeps through this gap |
| `LANE_RAMP_TOP` | 22mm | Z height of the ramp deck at the hopper end (slot is at ramp_top ± 1.5mm) |
| `LANE_RAMP_END_GX` | 48mm | Global X where ramp ends and flat scan zone begins |
| `LANE_RAMP_JOIN_Z` | 8mm | Z where right-side ramp descends to scan floor |
| `LANE_GX0` | -21mm | Global X origin of card lane left face |

### Horn slot position (card_lane_left interior)

From `build_woodstand.py` lane builder code:

```
Slot: x = 4.0 .. 4.0 + PUSHER_SLOT_W = 4 .. 24mm (local lane coords)
      z = LANE_RAMP_TOP - 1.5 .. LANE_RAMP_TOP + 3.0 = 20.5 .. 25mm
      Slot height: 4.5mm (enough for a 4mm arm + 0.5mm CL)
```

Global X: `LANE_GX0 + 4.0` = `-21 + 4` = **-17mm** (slot left edge, world coords)

### SG90 servo placement constraint

- Servo body 22.5×12×22mm must fit inside the column base or stand foot cavity
- Shaft must be within arm reach of the slot (shaft centre ≤ ARM_L from slot entry)
- Stand foot outer: 50×40×50mm (from `build_woodstand.py` FOOT_W/FOOT_H) — servo fits on its side
- Column inner: not yet measured — verify before placing servo in column stack

---

## Hardware BOM (provisional)

| Item | Spec | Qty | Notes |
|------|------|-----|-------|
| SG90 micro-servo | 22.5×12×22mm, 5V, 1.8 kg·cm | 1 | Same spec as Phase-2 CS2 servo |
| Servo mount bracket | TBD — Phase-3a CAD task | 1 | Mounts servo inside stand foot or base |
| Horn pusher arm | TBD — Phase-3a CAD task | 1 | Long horn reaching through PUSHER_SLOT |
| M2×6 SHCS | M2, 6mm | 4 | SG90 mounting screws |
| Servo horn | Standard cross horn (included with SG90) | 1 | Extend with printed arm |
| ESP32 / Arduino Nano | 5V capable; 1 PWM output | 1 | Servo controller |
| USB or LiPo 5V supply | 5V 1A | 1 | Shared with phone charger or separate |

---

## Parts to design (Phase-3a CAD tasks)

| Script | Description | Engine |
|--------|-------------|--------|
| `design/cs3a_servo_mount.py` | Bracket inside stand foot; M2 holes for SG90; aligns shaft with PUSHER_SLOT | build123d |
| `design/cs3a_pusher_arm.py` | Extended horn arm: press-fit on SG90 cross hub, sweeps through PUSHER_SLOT to push card | build123d |

Both scripts should follow the CS2 `cs2_card_pusher.py` pattern:
- `PART=0` assembly, `PART=1` bracket, `PART=2` arm
- `show_object(result)` for AgentCAD render loop
- Validate with `py design/cs2_verify.py` after adding new checks

---

## Mechanism description

1. Cards sit in `card_lane_left` gravity ramp, stacked above the scan nest.
2. Servo arm (at rest) is retracted through the horn slot — cards rest against it as a gate.
3. On trigger: servo sweeps forward (0° → 90°), arm pushes bottom card from ramp plateau across the slot, past LANE_RAMP_END_GX=48mm, down the right-side ramp to scan nest.
4. Servo retracts. Next card falls down the ramp and rests against the arm.

Stroke needed: arm tip must travel from slot entry (x=4mm local) to LANE_RAMP_END_GX (x=48mm local) — approx 44mm horizontal. Straight sweep sufficient; SG90 90° arm at ~22mm ARM_L gives 22mm tip travel — a longer 44mm horn arm is needed, OR a two-segment linkage.

**Design decision needed**: single long horn (44mm arm — exceeds SG90 torque limit at 1.8 kg·cm) OR a slider-crank mechanism (short arm, long push rod) similar to CS2 design. Slider-crank preferred.

---

## Open questions

| Question | Notes |
|----------|-------|
| Servo placement: foot vs base vs column | Foot has most volume (50×40mm); base is larger but has ballast cavity |
| Power source | USB from phone charger on shelf? Separate 5V pack? |
| Controller | ESP32 (WiFi trigger) vs Arduino Nano (button trigger) vs direct wired to phone |
| Trigger mechanism | Button on stand, timed interval, iPhone Shortcuts API, or phone screen tap |
| Stroke mechanism | Long horn (high torque demand) vs slider-crank linkage |
| Card magazine interface | Phase-3a feed from card_lane hopper end or from Phase-2 CS2 magazine dock? |

---

## Relationship to other phases

| Phase | Scope |
|-------|-------|
| Phase-2a | Manual feeder: hopper (cs2_hopper.py) + gravity lane — complete |
| Phase-2 CS2 | Motorized eject from CS2 hopper via SG90 servo — see `docs/phase-2-cs2-motor.md` |
| **Phase-3a** | **This document — servo feed through original stand PUSHER_SLOT — design only** |
| Phase-3b | Full integration: magazine dock + automatic eject + phone trigger (not yet scoped) |
