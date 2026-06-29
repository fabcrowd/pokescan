# Brainstorm: Manual-first operation for CS2 hopper

## Goal
The printed CS2 hopper must work in Phase-1 (no servo, no roller, no motor bracket, no crank/push-rod)
without ergonomic problems caused by the Phase-2 features built into the hopper geometry.

---

## What Phase-2 features exist in the hopper now (v4)

| Feature | Phase-2 purpose | Phase-1 impact |
|---------|----------------|----------------|
| 6mm shaft holes in end walls at z=12.5mm | Roller axle seats here | Open holes above card level — no Phase-1 impact |
| 4x M3 boss holes in front face at z=18/36mm | Motor bracket mounts here | Empty holes — no Phase-1 impact |
| 90x4mm exit slot in front wall at z=4mm | Card + push-rod exit | **Problem**: card at z=4mm is flush with open slot; may slide out on its own if table not level |

---

## Core problem: no manual card control

In Phase 2, the servo/push-rod ejects exactly one card at a time.
In Phase 1, there is NO equivalent mechanism. User issues:

1. **Accidental card exit**: With a 90x4mm opening at card floor level, a card in the hopper
   can slide out if the table tilts or the user bumps the scanner. There is nothing retaining it.

2. **No ergonomic ejection**: To remove a scanned card the user must either:
   - Reach down into a 70mm-deep hopper from the top (awkward, fingernail required)
   - Tilt the entire scanner assembly to slide the card toward the exit slot

3. **No single-card isolation**: Without the roller, all stacked cards can move together.
   If stacking multiple cards, pushing one card might push all of them.

---

## Option A — Thumb-push access hole in back wall (RECOMMENDED)

Add a 20x15mm oval/rectangular cutout in the BACK wall (y=+OUTER_W/2) at card height
(centred at z=~12mm, x=0). User inserts thumb from behind, pushes bottom card toward
the exit slot at y=-OUTER_W/2.

Pros:
- No separate part needed — just a hole in the existing back wall
- Ergonomic single-card push in the correct ejection direction (-Y)
- Works identically in Phase 2 (thumb hole doesn't conflict with any Phase-2 parts)
- Cards cannot accidentally exit (gravity keeps them resting on floor; they need active push)

Cons:
- Weakens back wall slightly; wall is 3.5mm thick so the cutout is in 3.5mm PLA
- Needs to be split carefully across left/right halves at x=0

Dimensions: centred at x=0, z=12mm, cutout 20mm wide x 15mm tall.
Each half gets a 10x15mm notch at its inner face (x=0).

---

## Option B — Exit slot cover plug (separate print)

A simple 90x4x3.5mm PLA plug that fills the exit slot in Phase-1 mode.
User pulls plug out when they want to eject a card (tilts or uses thumb), reinserts after.

Pros:
- Prevents accidental card loss
- No change to hopper geometry

Cons:
- Extra part to manage and lose
- Still no ergonomic ejection method

---

## Option C — Integrated card stop lip (geometry change)

Add a 1mm-tall internal lip at the bottom of the exit slot (z=4mm inside face).
Cards must be pushed with ~gentle force to overcome the lip; they don't slide out freely.

Pros:
- Single part, no accessories
- Cards stay put until deliberately ejected

Cons:
- Lip must be precise (too tall = hard to eject; too short = no benefit)
- May interfere with Phase-2 push-rod tip clearance

---

## Option D — Back-wall finger notch only (minimal change)

Simpler than Option A: just a 15x10mm semi-circle notch at the top of the back wall
inner face (not a full hole) so the user can hook a fingernail under the card stack and
lift it out without the hopper tipping.

---

## Recommendation

**Option A (thumb-push hole) + minor documentation.**

The 20x15mm back-wall cutout solves the ejection ergonomics without any separate part.
Card gravity keeps the card on the floor; it won't exit accidentally through the front.
Phase-2 parts remain bolt-on extras that add automation without removing manual capability.

Additionally add a sentence to docs/cs2_assembly.md noting that Phase-2 parts are optional
and Phase-1 (manual scan) requires only the hopper halves, platform, and wall sections.

---

## Implementation scope

1. cs2_hopper.py v5: add thumb-access hole in back wall (PART=0/1/2 all affected — hole
   spans the x=0 seam so both halves get a half-hole).
2. cs2_verify.py: no new dimension checks needed (hole doesn't affect bed fit).
3. docs/cs2_assembly.md: note that Phase-2 hardware is optional.
4. HANDOFF.md: update hopper entry to v5, add Phase-1 manual-operation note.
