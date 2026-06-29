# CS2 Card Scanner — Assembly Guide

## Parts required

| Part | File | Qty | Material | Notes |
|------|------|-----|----------|-------|
| Hopper left | cs2_hopper_left.stl | 1 | Black PLA | Print upright |
| Hopper right | cs2_hopper_right.stl | 1 | Black PLA | Print upright |
| Wall bot left | cs2_wall_bot_left.stl | 1 | Black PLA | Print upright |
| Wall bot right | cs2_wall_bot_right.stl | 1 | Black PLA | Print upright |
| Wall top left | cs2_wall_top_left.stl | 1 | Black PLA | Print upright |
| Wall top right | cs2_wall_top_right.stl | 1 | Black PLA | Print upright |
| Platform | cs2_platform.stl | 1 | Black PLA | Print flat |
| Alignment peg | cs2_peg.stl | 1 plate | PETG pref. | 4 pegs; use 2 |
| Fit test | cs2_fit_test.stl | 1 | Same PLA | Print FIRST |

**Optional accessories (cross-pol / diffuser):**

| Part | File | Qty | Material |
|------|------|-----|----------|
| Aperture polarizer clip | cs2_pol_clip.stl | 1 | White or clear PLA |
| Phone camera polarizer frame | cs2_phone_pol.stl | 1 | White or clear PLA |
| Torch diffuser plate | cs2_diffuser.stl | 1 | **White PLA only** |

## Hardware BOM

| Item | Qty | Spec |
|------|-----|------|
| M3×30 socket-head bolt | 8 | 2 platform-to-wall + 6 wall section joins |
| M3×20 socket-head bolt | 4 | 2 hopper half joins + 2 spare |
| M3 hex nut | 12 | All bolt receivers |
| 3mm alignment peg | 2 | Cut from cs2_peg.stl (10mm long) |
| CA glue (thin) | few drops | Wall-to-hopper bond |

## Step 0 — Print fit test FIRST

Print `cs2_fit_test.stl` before any full parts. Two features:

**Feature A — peg and bolt holes (left block, 18×16×20mm):**
- Thread M3×20 bolt through the 3.4mm hole (X-direction). Must pass freely.
- Push a 3mm peg into the 3.0mm blind hole (Z=14mm). Should seat snug with thumb pressure.
- If peg is too tight: increase `PEG_D` in `cs2_peg.py` by 0.05mm steps; re-export and reprint.
- If bolt binds: increase `BOLT_D` in `cs2_platform.py` / `cs2_wall.py` by 0.05mm; re-export.

**Feature B — pol_clip press-fit ring (right block, 44×38×8mm):**
- Press `cs2_pol_clip.stl` plug (35.6×29.6mm) into the 36×30mm aperture from below.
- Should seat with firm thumb pressure and hold without glue.
- Too tight: increase `PLUG_W` / `PLUG_D` in `cs2_pol_clip.py` by 0.1mm.
- Too loose: decrease by 0.1mm.

## Step 1 — Assemble hopper halves

1. Push one 10mm peg into each of the two seam holes on the left half (front and back walls, Z=17mm).
2. Align right half onto the pegs.
3. Thread M3×20 bolts through the two X-direction bolt holes (Z=25mm). Start nuts finger-tight.
4. Check card slot is flush and square, then tighten bolts.

The assembled hopper is 97×72×50mm. The card slot is 90×65mm; standard 88×63mm cards drop in with 1mm clearance per side.

## Step 2 — Assemble wall column

Wall prints in four sections (two bot + two top, each ≈49.5mm wide). Each pair is joined at the seam.

1. Align bot-left and bot-right at the X seam.
2. Thread M3×30 bolts through the three Z-direction seam holes; add nuts and snug down.
3. Repeat for top-left and top-right.
4. Stack bot section (Z=0..87mm) and top section (Z=87..174mm); thread three M3×30 bolts through the stacking holes; tighten.

The completed wall column is 97×14×174mm.

## Step 3 — Attach wall to hopper

The wall column front face seats against the hopper back face (0.1mm design gap — close enough to be snug in print).

1. Apply thin CA glue to the hopper back face (full width, 97mm).
2. Press the wall front face firmly against the hopper back face.
3. Hold 60 seconds; cure 5 minutes before handling.

The wall bottom rests on the same table surface as the hopper, so Z alignment is automatic.

> **Phase 2 note:** A bolt-down wall flange will replace the CA bond. The current Phase 1 bond is permanent but strong (97mm glue line).

## Step 4 — Mount platform at target height

Choose a bolt-hole height (see height table below). The wall has four sets of bolt holes:

| Bolt hole Z | PLAT_Z | Cam-to-card | Use case |
|-------------|--------|-------------|----------|
| 104mm | 100mm | 104mm | Ultra-close macro |
| 129mm | 125mm | 129mm | **Recommended standard** |
| 154mm | 150mm | 154mm | Wider field of view |
| 169mm | 165mm | 169mm | Near-maximum height |

1. Push the platform back edge (at Y=36mm) flush against the wall front face.
2. Platform Y-bolt holes are at Z=4mm from platform bottom (Y-direction, X=±22mm).
3. Thread M3×30 bolts in through the platform back edge; engage the wall holes.
4. Add M3 nuts on the wall back face; tighten until platform is level.

Platform should be level (use a card as a feeler gauge — it should slide in without binding).

## Step 5 — iPhone 16 Pro placement

The iPhone 16 Pro (71.5×149.6×8.25mm) rests face-down on the platform.

- **Camera protrusion:** The iPhone 16 Pro camera module protrudes 3.9mm from the back. This protrudes into the 36×30mm aperture tunnel (8mm deep). ✓
- **X-centering:** The phone (71.5mm) overhangs the platform (68mm) by 1.75mm each side; gravity centres it in X.
- **Y-positioning:** Slide the phone until you can see the camera lens through the aperture when viewed from below. The aperture is 30mm deep in Y — there is ample margin. Look through the aperture from the card side; the camera lens should be visible.
- **Orientation:** Action-button edge or charging-port edge facing the wall — either works. Confirm camera is visible through aperture before scanning.

## Step 6 — Standard scanning (no accessories)

1. Place card face-up in the hopper slot. Card rests at Z=4mm on the hopper floor.
2. Place iPhone face-down on platform, camera over aperture (Step 5).
3. Open Apple Camera in Photo mode. Pinch to enable macro or use ultra-wide lens.
4. Card is at 104–169mm below the camera (depending on height). Ultra-wide macro range: 20–140mm.
5. The camera app will auto-focus. Take the photo.

Recommended height: **129mm** (PLAT_Z=125mm). At this distance the ultra-wide camera covers a 63×88mm card with ~10% margin each side.

## Step 7 — Torch diffuser (optional, recommended for standard cards)

The `cs2_diffuser.stl` white PLA plate catches the phone torch and scatters it into the hopper, replacing harsh single-point illumination with large-area soft-box fill.

1. Place diffuser flat on platform top (68×75mm plate, 1.5mm thick).
2. Align aperture in diffuser with platform aperture (one correct orientation — notch is asymmetric).
3. Place iPhone on diffuser. Phone now sits 1.5mm higher; negligible focus shift (<1.2% at 125mm).
4. Enable torch in Camera app (or use a separate torch app). The white PLA scatters the light.

**Use diffuser for:** Standard cards, non-foil cards, any card that is not holographic.

## Step 8 — Cross-polarization (optional, for holo/foil cards)

Holographic and foil cards produce specular glare that obscures card detail. Cross-polarization eliminates this.

**What you need:**
- `cs2_pol_clip.stl` (aperture side, installed in platform aperture)
- `cs2_phone_pol.stl` (lens side, held over iPhone camera)
- Two pieces of linear polarizing film: one 30×24mm, one 30×24mm
- Rubber band

**Setup:**
1. Cut two pieces of linear polarizing film to 30×24mm.
2. Insert one film piece into the `cs2_pol_clip` top pocket (film sits in the aperture, camera side).
3. Press `cs2_pol_clip` plug into the platform aperture from below. Flange seats flush on platform bottom.
4. Insert the second film piece into the `cs2_phone_pol` recess.
5. Place `cs2_phone_pol` over the iPhone camera cluster, film touching camera glass. Loop rubber band over iPhone corners to hold in place.
6. **Rotate one film 90°** relative to the other. This is the cross-polarization angle that kills specular reflection.
7. With torch on: glare from holo/foil will disappear; card detail becomes visible.

**Diffuser + cross-pol:** You can use the diffuser plate AND the pol_clip together. Install pol_clip first, then diffuser on top of platform, then phone. Both accessories stack without interference.

## Phase 2 — Motorized card eject (future)

The hopper is pre-provisioned for a motor-driven card eject mechanism. Do not attempt Phase 2 until Phase 1 is fully assembled and tested.

**Parts required (Phase 2):**
- `cs2_roller.stl` — 4× drive rollers (PETG, press-fit on 6mm rod)
- 6mm smooth rod, 100mm long (hardware store — look for "6mm steel rod" or M6 rod)
- N20 gear motor, 6V, 30–60 RPM output (10×12×20mm body)
- `cs2_motor_bracket.stl` — motor mount bracket (**not yet designed**)

**Mechanism:** The roller (8mm OD) sits on the 6mm shaft at z=8mm. Its bottom face is at z=4mm — exactly card floor level. With a 0.8mm card under it, the roller compresses the card by 0.8mm and drives it forward through the 15×4mm exit slot when the motor rotates.

**Roller installation:**
1. Source a 6mm smooth rod, 100–110mm long.
2. Slide two rollers onto the rod at x=−7.5mm and x=+7.5mm (over the exit slot center).
3. Apply a drop of CA glue at each roller bore before pressing home.
4. Feed rod through one hopper end wall shaft hole, through both rollers, through the other shaft hole.
5. Motor couples to one rod end (coupling bracket TBD in Phase 2 design).

## Rebuild STLs

```
# Re-export all CS2 STLs (if constants change after fit test):
py design/cs2_hopper.py    # PART=1 left, PART=2 right
py design/cs2_platform.py  # PART=0
py design/cs2_wall.py      # PART=1..4 (four sections)
py design/cs2_peg.py       # PART=0 print plate
py design/cs2_pol_clip.py  # PART=0
py design/cs2_phone_pol.py # PART=0
py design/cs2_diffuser.py  # PART=0
py design/cs2_roller.py    # PART=1 print plate (Phase 2)
```

Or run all via AgentCAD with the corresponding `.py` script.

## Verification

```
py design/cs2_verify.py
```

Runs 31 checks (dimensions, clearances, alignment, peg positions, bolt holes). All should PASS before printing.
