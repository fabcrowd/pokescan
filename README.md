# Card Scanner Stand — iPhone 16 Pro + Toybox

A **plastic-modular copy stand on a single wood-dowel spine** for scanning trading cards (Pokémon, MTG, sports, etc.) with a phone camera app (Delver, ManaBox, Collectr, etc.). Everything prints and slide-fits together (no screws); one 8 mm wood dowel is the only wood part, and pulling it flat-packs the whole stand.

The design targets two hard constraints that generic MakerWorld/Thingiverse stands ignore:

1. **Toybox Alpha 3 build volume** — **70 × 80 × 90 mm** (script uses conservative **68 × 78 × 88** usable). Large parts **split** with sliding dovetails (sides) + tongue-and-groove (bottom).
2. **iPhone 16 Pro optics** — the main (Fusion) wide camera has a large minimum focus distance and a **focus dead zone**; the LED torch sits on-axis next to the lens and creates **holo/foil glare** unless the light path is shaped.

---

## Current recommended architecture

**Plastic-modular column** on one **8 mm wood dowel** + **adjustable cam-lever phone head** + **rotating cross-polarizer** + **flow-through card lane** (Phase-2 feeder ready). Every part fits the Toybox bed; slide-fit joints, no screws.

| Part | Material | Role |
|------|----------|------|
| `base_left/right.stl` | Print ×1 each | Split ballast base (120×72 mm assembled); dovetail + T&G joinery |
| `column_segment.stl` ×3 | Print | 34×34 posts; boss/recess slide-nest; vertical dowel bore |
| `head_post.stl` | Print | Scaled runway + **D-index flat** (rotation key) |
| `head_clamp.stl` | Print | Bilateral split collar; shelf pins + scale pointer |
| `cam_lever.stl` + `clamp_pin.stl` | Print | Flip-down eccentric lever |
| `phone_shelf_left/right.stl` | Print ×1 each | Split shelf (68×68 mm assembled); camera opening toward card |
| `torch_deflector.stl` | Print | Off-axis baffle (**black** PLA) |
| `polarizer_base.stl` + `polarizer_dial.stl` | Print | Rotating lens polarizer (**black** base) |
| `card_lane_left/right.stl` | Print ×1 each | Gravity ramp → flat scan nest; magazine dock rails + latch notch |
| `card_magazine_left/right.stl` | Print ×3 sets | Modular card magazine cartridge halves (snap-in, gravity feed) |
| `card_magazine_lid.stl` | Print ×6 | Snap-on lid per half (keeps stack aligned during transport) |
| `nest_frame.stl` | Print ×1 | Phase-2a scan deck frame with U-channels |
| `nest_tray_ramp.stl` / `nest_tray_bin.stl` | Print ×1 each | Phase-2a slide-out tray halves (butt-join at centre) |
| `nest_stop.stl` | Print ×1 | Phase-2a hard return stop tab |
| 8 mm dowel | Wood (only wood part) | Spine through base → segments → head_post socket |

```
Side view (conceptual)

  ┌─────────────── iPhone 16 Pro (camera down)
  │   [polarizer dial rotates] + torch deflector cartridge
  ╞═══════════════ phone_shelf (on head_clamp pins)
 ┌┴┐ head_clamp ← slides on head_post scale; cam_lever locks
 │ ║ ║ head_post runway (55 mm travel, engraved ticks)
 │ ║ ║
 │ ║ ║ ← 8 mm wood dowel
 │ ║ ║   column_segment ×3
 ┌┴─╨─┴┐ base              card_lane: hopper lip ↘ ramp ↘ scan nest (z0) ↘ bin step
 └─────┘                   [horn slot — Phase-2a gate linkage; see docs/phase-2a-manual-feeder.md]
  Lens 296–331 mm (3 segments, clamp range) — ≥260 mm ✓
  verify_assembly() checks lens XY over scan nest (≤2 mm)
```

---

## CS30 Arch v13 — Integrated Phone Arch + Gravity Ramp (current)

`design/cs30_arch.py` — a **Card Slinger 3.0-inspired arch** that wraps the `photo_box` light enclosure. Five printable parts (black PLA), two M3 bolts, two M3 hex nuts. No wood. No separate mount needed — the arch legs stand on the table with wide foot plates that abut the photo_box walls for lateral location.

```
Side view

  ┌───────────────────────── phone bridge (two halves, camera aperture 36×30mm)
  │    ←  dual sockets snap onto two carriage pegs (x=41mm + x=57mm)
  ╞═══════╤═════╤══════════ carriages lock with M3 knob (5mm rack pitch)
  │       │     │
  │       │     │  arch legs (2 sections each, 82mm+82mm = 164mm)
  │       │     │
  ╞═══════╧═════╧══════════ legs clip to photo_box left/right walls (8mm thick)
  [  photo_box v25 (84×44×44mm, LED-lit, white PLA)  ]
  ← gravity ramp clips to front end cap → cards slide to scan window →
```

### Part list and print settings (v13)

| STL | Qty | Bed dims | Orientation | Profile | Infill | Brim | Notes |
|-----|-----|----------|-------------|---------|--------|------|-------|
| `cs30_fit_test.stl` | 1 | 68×16×30mm | Flat (Z-up) | Recommended | 15% gyroid | None | **Print FIRST** (~18 min); validates (A) carriage-on-leg, (B) bridge peg, (C) ramp C-clip, **(D) M3 bolt/nut trap** |
| `cs30_ramp.stl` | 1 | 68×70.7×32.6mm | Flat (floor down) | Recommended | 15% gyroid | None | 20° gravity ramp; C-clip foot snaps onto photo_box front end cap (3mm); self-supporting |
| `cs30_arch_leg_section.stl` | **4** | **14×24×87mm** | Standing (Z-up, **foot plate down**) | Recommended | 20% gyroid | **NO** | 2 per leg, stack → 164mm; 24mm foot plate is bed face; corner notches clear photo_box end cap; inner face abuts wall; **no brim — 1mm bed margin** |
| `cs30_phone_bridge_half.stl` | **2** | 60×78×10mm | Flat (plate face down) | Better Quality | 20% gyroid | **NO** | 6mm plate; blind carriage sockets (5mm + 1mm floor); butt join at x=0; **no brim — 1mm bed margin** |
| `cs30_arch_carriage.stl` | **2** | 30×16×55mm | +Y face down (C-channel up) | Better Quality | 25% gyroid | ON | Slot 14.6×12.3mm clears rack teeth; nut trap 5.7mm; finer layers improve bore + slot |
| `cs30_lock_knob.stl` | **2** | 19.2×20×8mm | Flat (bottom face down) | Better Quality | 20% gyroid | None | **Top-face** socket (outer face when assembled) captures M3×30mm bolt head; six grip flats; indicator groove on top |

All parts: black PLA. 3 perimeter walls, 0.2mm layers. No supports.

### Hardware (v13)

| Item | Qty | Role |
|------|-----|------|
| M3×**30mm** socket-head bolt (ISO 4762) | 2× | Through carriage ±X; clamps leg — 30mm needed (25mm falls 2mm short of nut) |
| M3 hex nut | 2× | Drops into square nut trap on carriage +X face |

### Fit test procedure

Print `cs30_fit_test.stl` flat. Four features on one 68×16×30mm part:

| Feature | Test | Pass | Fail → adjust |
|---------|------|------|---------------|
| **(A) Leg stub** (left, x=-22) | Slide printed carriage C-channel down over 14×10mm column | Slides freely, ~0.3mm play | `CARR_CL` 0.3→0.4mm, reprint |
| **(B) Peg base** (centre) | Press bridge half sockets over 3mm-radius pegs at ±8mm | Snaps on with light thumb pressure, no wobble | `SEC_PEG_CL` 0.3→0.35mm, reprint |
| **(C) End cap stub** (right, x=+21) | Press ramp C-clip foot over 3mm plate | Snaps with single push, stays held | `EC_SOCK_CL` 0.3→0.4mm, reprint |
| **(D) Nut trap stub** (far right, x=+30..39) | Thread M3×**30mm** bolt through 3.4mm hole; drop M3 hex nut into 5.7×5.7mm pocket | Bolt passes freely; nut drops flush with fingers | Bolt binds → `BOLT_D` 3.4→3.6mm; nut jams → `NUT_TRAP_CL` 0.2→0.35mm; reprint |

### Assembly sequence

See `docs/cs30_assembly.md` for the full 8-step guide. Quick overview:

1. Build photo_box (see `docs/photo_box_assembly.md`)
2. Drop M3 nut into each carriage trap; insert M3×30mm bolt from -X face, thread into nut; slide lock knob onto bolt head
3. Slide one carriage onto each leg section from the top
4. Stack two leg sections per side (male peg → female socket, press flush)
5. Stand each leg stack beside the photo_box left/right walls — foot plate (24mm wide) rests on table; inner x-face of foot abuts photo_box wall outer face for lateral location
6. Slide both carriages to the same rack tooth mark; tighten both knobs
7. Press both bridge halves down onto carriage pegs; halves meet at centreline
8. Snap ramp C-clip foot over photo_box front end cap (3mm body)

### Height adjustment

| Rack mark | Bridge height | Camera → card | Focus mode |
|-----------|--------------|---------------|------------|
| 30mm | 85mm | **81mm (8.1cm)** | Ultra-wide macro ✓ |
| 50mm | 105mm | **101mm (10.1cm)** | Ultra-wide macro ✓ |
| 70mm | 125mm | **121mm (12.1cm)** | Ultra-wide macro ✓ **(recommended)** |
| 80mm | 135mm | **131mm (13.1cm)** | Ultra-wide macro ✓ |
| 85mm | 140mm | **136mm (13.6cm)** | Ultra-wide macro ✓ (safe limit) |
| 90mm | 145mm | **141mm (14.1cm)** | Ultra-wide macro (borderline — may switch lens) |
| 95mm | 150mm | **146mm (14.6cm)** | ⚠ Borderline — test before batch scanning |

Camera → card = bridge height − 4mm (card face at FLOOR_T=4mm above table). Bridge height = rack mark + 55mm (CARR_H=50 + SEC_PEG_H=5). Maximum physical rack mark = 114mm (column height 164mm − CARR_H 50mm). Dead zone for iPhone 16 Pro main camera begins around 14cm; ultra-wide macro covers 2cm–14cm.

**Recommended range: rack marks 30–85mm** — keeps camera-to-card under 136mm, safely within ultra-wide macro territory. At rack mark 90mm the camera-to-card distance is 141mm, which is borderline (iOS may auto-switch to the main lens). Rack mark 70mm (≈12cm) gives the best framing balance. Use 2× digital zoom in Apple Camera or Magnifier for tighter crops without moving closer.

Each tooth = 5mm. Loosen both knobs → slide to mark → tighten → recheck level.

> **App compatibility at macro range:** Apple Camera (auto-switches to ultra-wide macro below ~14cm) and Magnifier work at any rack mark. Third-party scanner apps (Delver Lens, ManaBox, Collectr) may stay on the main camera and blur — test at rack mark 50 before committing to a batch scan.

### Clearance reference (v13)

| Interface | Constant | Value |
|-----------|----------|-------|
| Carriage C-channel → leg | `CARR_CL` | 0.3mm/face |
| Bridge socket → carriage peg | `SEC_PEG_CL` | 0.3mm radius |
| Ramp C-clip → end cap body | `EC_SOCK_CL` | 0.3mm/face |
| M3 bolt clearance | `BOLT_D` | 3.4mm |

### Rebuild cs30_arch STLs

```bash
# AgentCAD (Claude Code):
#   mcp__agentcad__run("design/cs30_arch.py", "rebuild", params="PART=N")
#   PART=0 = assembly preview  1=ramp  2=leg_section  3=bridge_half  4=carriage  5=lock_knob

# Direct:
uvx --from build123d --with bd_warehouse python design/cs30_arch.py
# Set PART=N at top of script; STLs land in design/output/cs30_*.stl
```

### System verification

After changing any constant in `photo_box.py` or `cs30_arch.py`, run the constraint checker to confirm clearances, optics, and macro focus range are still valid:

```bash
py design/cs30_verify.py
```

19 checks across 6 categories (camera-to-card range, geometric clearances, aperture vignetting, LED channel depth, foot plate notch, bridge alignment). Exits 0 on pass, 1 on failure. Takes under 1 second — no build123d or AgentCAD required.

---

## CS2 — Card Scanner v2 (C-Stand + Hopper, Toybox-native)

`design/cs2_*.py` — a **Card Slinger 2-inspired vertical platform stand** with an open-top card hopper and a height-adjustable phone shelf. All parts fit the Toybox bed without modification. No wood. No arch structure. Card drops in face-up; phone rests on shelf above looking down through a 36×30 mm aperture.

```
Side view

  ┌──────────────────────────────────── iPhone 16 Pro (face down)
  │   camera aperture: 36×30mm
  ╞══════════════════════════════════ platform (68×75×8mm, adjustable)
  │                                    bolts to wall at 4 heights: 100/125/150/165mm
  │  ┌─────────────────────────┐
  │  │   wall column           │  97×14×174mm (2 sections × 2 halves)
  │  │   (black PLA, upright)  │
  │  └─────────────────────────┘
  [  hopper (97×72×50mm, 2 halves)  ]
     open-top card slot: 90×65mm
     card face at z=4mm (FLOOR_T)
```

### Part list (all black PLA unless noted)

| STL | Dims (mm) | Qty | Orientation | Notes |
|-----|-----------|-----|-------------|-------|
| **`cs2_fit_test.stl`** | 64×38×20 | 1 | Flat | **Print FIRST** — validates peg fit + pol_clip aperture press-fit |
| `cs2_hopper_left.stl` | 48.5×72×70 | 1 | Upright | Left half of card hopper (v3, 70mm, ~160 cards); Phase 2 shaft holes + exit slot |
| `cs2_hopper_right.stl` | 48.5×72×70 | 1 | Upright | Right half |
| `cs2_platform.stl` | 68×75×8 | 1 | Flat | Phone shelf; Y-direction M3 bolt holes at x=±22mm |
| `cs2_wall_bot_left.stl` | 49.5×20×88 | 1 | Upright | Bottom-left wall section |
| `cs2_wall_bot_right.stl` | 49.5×20×88 | 1 | Upright | Bottom-right wall section |
| `cs2_wall_top_left.stl` | 49.5×14×88 | 1 | Upright | Top-left wall section |
| `cs2_wall_top_right.stl` | 49.5×14×88 | 1 | Upright | Top-right wall section |
| `cs2_peg.stl` | 10×10×10 | 1 plate | Flat | 4× 3mm alignment pegs; use 2 for hopper join (PETG preferred) |
| `cs2_pol_clip.stl` | 44×38×8 | 1 | Flat | **White PLA** — optional; polarizer film clip for aperture |
| `cs2_phone_pol.stl` | 44×38×3 | 1 | Flat | **White PLA** — optional; matched phone-camera polarizer frame |
| `cs2_diffuser.stl` | 68×75×1.5 | 1 | Flat + **brim** | **White PLA** — optional; torch scatter plate for diffuse fill light |

All parts: 3 perimeter walls, 0.2mm layers, 20% infill, no supports.

### Hardware BOM (per scanner)

| Item | Qty | Spec | Use |
|------|-----|------|-----|
| M3×30mm socket-head bolt | 8 | ISO 4762 | Platform-to-wall (2) + wall section joins (6) |
| M3×20mm socket-head bolt | 6 | ISO 4762 | Hopper half joins (2) + spare |
| M3 hex nut | 14 | standard | All bolt receivers |
| 3mm dowel pin | 2 | from `cs2_peg.stl` | Hopper seam alignment |
| CA glue | small tube | cyanoacrylate | Wall flange to hopper back face (Phase 1) |

### Fit test procedure

Print `cs2_fit_test.stl` flat — same PLA colour as target parts (pigment affects shrink).

| Feature | Test | Pass | Fail → adjust |
|---------|------|------|---------------|
| **(A) Hole block** (left, x=−22) | Insert 3mm dowel (cut from `cs2_peg.stl`) into blind hole at z=14mm; thread M3×20mm bolt through at z=8mm | Dowel slides in with light thumb push; bolt passes freely | Dowel too tight → `PEG_D` in `cs2_peg.py` +0.05mm steps; reprint peg plate |
| **(B) Aperture ring** (right, x=+20) | Press `cs2_pol_clip` plug (35.6×29.6mm) into the 36×30mm opening from below | Firms up with thumb pressure; stays without adhesive | Too tight → `PLUG_W`/`PLUG_D` in `cs2_pol_clip.py` +0.1mm; too loose → −0.1mm; reprint clip |

### Assembly sequence

See **`docs/cs2_assembly.md`** for the full step-by-step guide including fit test procedure, accessory setup, and iPhone placement notes.

Quick reference:
1. **Join hopper halves:** align seam at x=0; insert 2× 3mm dowel pegs (front + back, z=17mm); thread 2× M3×20mm bolts at z=25mm.
2. **Build wall column:** join 4 sections into bot + top pairs (3× M3×30mm per seam); join left+right sides.
3. **Attach wall to hopper:** CA glue wall front face to hopper back face; hold 60 s.
4. **Mount platform:** M3×30mm bolts through platform back edge (Y-direction, x=±22mm, z=4mm from bottom); thread into wall; nut on wall back face.
5. **Scan:** card face-up in hopper; phone face-down on platform, camera over aperture.

> **Workflow speed:** drop a full load (≈120 cards, or ≈160 with the 70mm tall v3 hopper) through the centering insert (`cs2_centering_insert.stl`) — cards self-align in under a second. Scan + manual eject: ~900 cards/hour. With Phase-2 motorised eject and separator: ~600–900 cards/hour realistic. See `docs/workflow-speed.md` for the full capacity table and toss-and-scan steps.

### Height settings

| Platform position (mm) | Camera→card clearance | Notes |
|------------------------|----------------------|-------|
| 100 | 104mm (10.4cm) | Ultra-wide macro ✓ |
| 125 | 129mm (12.9cm) | Ultra-wide macro ✓ **(recommended)** |
| 150 | 154mm (15.4cm) | Borderline macro — test before batch |
| 165 | 169mm (16.9cm) | Main camera territory |

Camera→card = platform Z + PLAT_T(8) − FLOOR_T(4). Ultra-wide macro range: 2cm–14cm.

### Lighting accessories (optional)

**Diffuser plate** (`cs2_diffuser.stl` — white PLA, 68×75×1.5mm): Lay flat on the platform top; phone rests on the diffuser. The phone torch hits the white PLA surface and scatters sideways into the hopper, converting the harsh point-source torch into broad soft-box fill light. The 36×30mm aperture cut-out aligns with the platform aperture exactly. Use brim in slicer — 1.5mm thin part at 68mm bed width warps without it.

**Cross-polarization** (`cs2_pol_clip.stl` + `cs2_phone_pol.stl` — holographic/foil cards only): Print both in white PLA. Cut two 30×24mm squares from a linear polarizing film sheet. Insert one square into each clip's recess. Rotate one square 90° relative to the other. Slip `cs2_pol_clip` into the platform aperture from below; hold `cs2_phone_pol` over the phone camera with a rubber band through the 4 corner holes. Kills specular glare on holo/foil surfaces.

**Recommended combinations:**
- Standard cards: diffuser plate only
- Holo/foil cards: diffuser plate + cross-pol pair

### Rebuild CS2 STLs

```bash
# Set PART=N at top of each script, then run via AgentCAD or directly:
uvx --from build123d python design/cs2_hopper.py   # PART=1 left / PART=2 right
uvx --from build123d python design/cs2_wall.py     # PART=1..4 for four sections
uvx --from build123d python design/cs2_platform.py # PART=0 single piece
```

### Verify CS2 geometry

```bash
py design/cs2_verify.py
```

31 checks: bed fit, card clearance, aperture alignment, platform height range, shaft hole clearance, wall coverage, bolt alignment, peg clearance. Exits 0 on pass.

---

## v2: Rack-Pinion Adjustable Stand *(superseded by CS30 Arch v5)*

`design/rack_stand_v2.py` — a **Card Slinger-inspired** stand with a rack-and-pinion height adjustment column. Eight printable parts (including one tolerance test block), two M3 bolts, and a rubber band. No wood required.

```
Card flow + camera geometry

  y = 0 mm  ← user inserts card here (tray_back funnel entry)
  y = 44 mm ← camera aims here  (card centre; tray split join)
  y = 88 mm ← back of tray / stand column base (STAND_Y = CARD_L)

  z-stack (lowest carriage position = 260 mm lens height):
    z=0        table
    z=0..13.5  card tray (tray_back y=0..44, tray_front y=44..88)
    z=13.5     foot bottom rests on tray wall tops (x = ±32..35 mm)
    z=13.5..45.5  stand foot body (70×50×32 mm)
    z=45.5..49.5  foot D-peg → rack section 1 socket
    z=45.5..285.5 rack column (3 × 80 mm sections)
    z=205.5+   phone carriage (section 3 minimum; slides on column, locked with M3 side-bolt)
    z=+CAR_H   phone platform (bolted to carriage with 2× M3×8)
    260..290 mm  lens height range (carriage adjustable within section 3) ✓
```

### Part list and print settings (v2)

| STL | Bed dims | Orientation | Profile | Infill | Qty | Notes |
|-----|----------|-------------|---------|--------|-----|-------|
| `rs2_fit_test.stl` | 42×38×20 mm | Flat (base down) | Recommended | 15% | 1× | **Print FIRST** (with knob) — verify all 5 features before main set |
| `rs2_rack_section.stl` | 26×26×84 mm | Standing (Z-up, teeth on +Y face) | **Better Quality** | 25% | 3× | Finer layers give cleaner tooth faces |
| `rs2_stand_foot.stl` | 70×50×36 mm | **Rotate 90° in slicer** — 70 mm along Y | Recommended | 15% | 1× | 70 mm > 68 mm bed X; rotate to 50×70; 4× dimples on base align with tray wall tops for rubber feet |
| `rs2_tray_front.stl` | 70×50×13.5 mm | **Rotate 90° in slicer** | Recommended | 15% | 1× | Collection half (y=44..88); card-stop tab at y=86..88 mm; **tapered funnel** at join face (y=44) guides cards across seam |
| `rs2_tray_back.stl` | 70×44×13.5 mm | **Rotate 90° in slicer** | Recommended | 15% | 1× | Entry half (y=0..44); **tapered funnel** at user entry (y=0): 68 mm wide → 64 mm over 10 mm, ≈11° per side |
| `rs2_phone_carriage.stl` | 37×47×50 mm | Flat (bore opening up) | **Better Quality** | 25% | 1× | Higher infill for cantilever load; finer layers improve bore roundness |
| `rs2_phone_platform.stl` | 65×75×25 mm | Face-down (pegs/lips point up, no supports) | Recommended | 20% | 1× | M3 countersink pockets on top face |
| `rs2_pinion_knob.stl` | 30×30×42 mm | Standing (disc at top) | **Better Quality** | 25% | 1× | Finer layers on gear teeth and grip grooves |

All parts: 3 perimeter walls, 4 top/bottom layers, **brim** (Toybox has no heated bed). No supports needed for any part in the listed orientation.

### Hardware (v2)

| Item | Qty | Role |
|------|-----|------|
| M3×8 mm socket-head bolt | 2× | Platform → carriage (side-wing pilot holes at x=±16.5 mm) |
| M3×6 mm **button-head** bolt (ISO 7380) | 1× | Carriage lock (self-taps into -X wall; **use 6 mm button-head only** — gives 3.3 mm engagement; longer or socket-head bolts damage rail) |
| Standard rubber band | 1–2× | Cross-hook over 4 pegs (2 front + 2 back lip) — 1 band looped or 2 bands in X-pattern for firm phone retention |
| Stick-on rubber feet (8–10 mm dia, ~1 mm thick) | 8× | Press into tray bottom recesses (4 per half) — prevent stand sliding on desk |
| Stick-on rubber pads (4–6 mm dia, ~1 mm thick) | 4× | **Optional:** press into foot base dimples (x=±33 mm) — improves foot-to-tray grip; can substitute hot glue or leave empty |

### Step 1 — Fit test (print before anything else)

Print `rs2_fit_test.stl` **and** `rs2_pinion_knob.stl` together (~40 min total, 15%/25% infill). Test each feature:

| Feature | How to test | Pass | Fail → fix |
|---------|-------------|------|------------|
| **Rail bore pocket** (top, 12 mm deep) | Slide rack section into pocket from top | Moves freely with ~0.3 mm play | Adjust `CAR_CL` ±0.1 mm |
| **D-peg socket** (bottom) | Press stand foot D-peg upward into socket | Snug, needs thumb pressure | Adjust `PEG_CL` ±0.1 mm |
| **Tray peg socket** (+X face, 6 mm deep) | Insert tray_front horizontal peg | Snug fit, pulls out with effort | Adjust `TRAY_PEG_CL` ±0.1 mm |
| **Lock bolt pocket** (-X face, z=4 mm) | Thread M3×6 mm button-head (ISO 7380) from -X face | Head sits flush in recess; shank threads in smoothly | If splits PLA: bore too small (M3 self-tap limit); try slow insertion |
| **Rack stub** (+Y face, 3 teeth) | Press printed pinion_knob hub tangentially; rotate | Teeth slip into gaps freely, no binding | Adjust `GAP_W` from 2.4 → 2.6 mm, reprint knob only |

After adjusting a constant: re-run AgentCAD (or `uvx --from build123d --with bd_warehouse python design/rack_stand_v2.py` — see **Rebuild v2 STLs** below), reprint **only the fit_test** until it passes, then print the full set.

### Step 2 — Assembly sequence (v2)

1. **Join tray halves** — insert tray_front horizontal pegs into tray_back sockets at the y=44 mm join face. Press together. The **tray_back** piece has the user-entry funnel (wider opening, 68 mm); this end faces toward you when scanning.
2. **Set tray on table** — card channel (64 mm wide, centered) faces up. The **wider funnel opening** on tray_back faces toward you; the card stop tab inside tray_front faces away (toward the stand).
3. **Place stand foot** — center foot (70×50 mm base) over back of tray (y=88 mm). Foot bridges the card channel, resting on both tray wall tops (3 mm contact each side).
4. **Stack rack sections** — lower section 1 D-socket (bottom) onto foot D-peg (top). Lower section 2 D-socket onto section 1 D-peg. Lower section 3 D-socket onto section 2 D-peg. Each section's **D-socket is at the bottom**; each section's **D-peg is at the top** for the next. Column is 240 mm tall with teeth on +Y (card) face.
5. **Slide carriage** — lower phone carriage over column from the top. The 4 mm bore lead-in at the carriage top helps align the rail; guide the teeth (+Y face) into the bore slot and lower until the pinion zone passes the rack top.
6. **Insert pinion knob** — slide hub into carriage +X pinion bore; rotate to mesh with rack teeth. Knob disc sits flush with carriage +X face.
7. **Adjust height** — turn pinion knob to move carriage up/down. Target lens range: 260–290 mm above card. Read the rack tick mark nearest the carriage-top notch on the +X face — **the four useful ticks on the top (section 3) segment correspond to: 50 mm → 260 mm lens, 60 mm → 270 mm, 70 mm → 280 mm, 80 mm → 290 mm** (ticks are 10 mm apart; 260 mm is the minimum focus-safe height). Tighten M3×6 **button-head** lock bolt (self-tap into -X carriage wall) finger-tight.
8. **Mount platform** — lower phone platform onto carriage top; align M3 clearance holes (x=±16.5 mm, y=0) over carriage side-wing pilot holes. Thread 2× M3×8 bolts from above.
9. **Place phone** — lay iPhone 16 Pro **camera-side down** (back of phone on platform, screen faces up), camera-cluster end toward -Y (card). Camera opening (36×30 mm) exposes the camera cluster through the platform floor. Front lip retains camera end, rear lip retains back.
10. **Insert card** — slide card (unsleeved, 63 mm wide) into the tray funnel short-edge first, camera-side up. Push until you feel resistance from the card stop. **Fully seated: ~2 mm of the card's trailing edge protrudes from the entry funnel** — this is expected and makes removal easy.
11. **Secure phone** — cross-hook rubber band: front-left peg → diagonally to back-right peg; second band front-right → back-left. Or loop single band front-peg to front-peg over phone back.

> **Break-in tip:** apply a thin smear of white lithium grease or petroleum jelly to the rack teeth (+Y face of the column) before first use. FDM PLA rack-and-pinion benefits from lubrication; friction drops noticeably after 10–20 adjustments.

> **Holo/foil glare tip:** Most scanning apps (ManaBox, Delver Lens, Collectr) use ambient light — they do not fire the torch. Scan in bright room light with no overhead point source directly above the card. For stubborn holos: (1) slightly tilt the whole stand 5–10° forward, or (2) rotate the card 15–30° in the tray before re-scanning. No cross-polarizer is needed for the v2 face-down configuration.

### Clearance reference (v2)

| Interface | Constant | Value | Notes |
|-----------|----------|-------|-------|
| Rail bore → carriage | `CAR_CL` | 0.6 mm | 0.3 mm/face; generous for Toybox FDM |
| D-peg → socket | `PEG_CL` | 0.35 mm | Radius clearance |
| Tray peg → socket | `TRAY_PEG_CL` | 0.25 mm | Radius clearance |
| Rack tooth → gap | `GAP_W - TOOTH_W` | 0.4 mm | 0.2 mm/side; FDM rack best practice |
| Pinion hub → bore | `CAR_CL` | 0.6 mm | Same as rail |
| Card channel width | `CARD_CL` | 0.5 mm/side | 64 mm channel (63 mm card + 0.5 mm/side); unsleeved card slides freely |
| Tray entry funnel | `FUNNEL_EXTRA` | 2 mm/side | 68 mm wide at y=0 → 64 mm over 10 mm depth; ≈11° per side; self-centering guide at both tray entry faces |

### Rebuild v2 STLs

```bash
# Run with AgentCAD (Claude Code / Cursor with .mcp.json):
mcp__agentcad__run("design/rack_stand_v2.py", "rebuild", render="iso")

# Or run directly with uvx (no venv install needed):
uvx --from build123d --with bd_warehouse python design/rack_stand_v2.py
# STLs land in: design/output/rs2_*.stl
```

Verify: all 8 STLs export, console prints `Lens height range: 260..290 mm  (target >= 260 mm at min)` and `Section H: 84.0 mm`.

---

## Photo Box (pb_*) — diffuse lighting accessory

A white-walled side-lit enclosure for scanning difficult cards — holos, foils, shimmer patterns — where ambient-light scanning produces specular hotspots. The phone looks straight down through the open top. Four 5V LED strip segments (one per wall half) seated in wall channels at z=33.6–44mm provide 44° side illumination that bounces off the white interior to eliminate most glare without a cross-polarizer. The 6mm-deep LED channel gives a 3.2mm diffuser air gap — above the 3mm photography minimum for even illumination. Eight adhesive bumpon feet (3M SJ5302) press into recesses on the platen underside for anti-slide grip. End caps include a 5×8mm LED cable exit slot at the top-inner corner for clean wire routing.

Requires an overhead phone mount at 263mm above the desk. See `docs/photo_box_assembly.md` for the full step-by-step assembly manual. All structural parts: white/coconut matte PLA. Diffuser strip: clear or natural white PLA.

> **Note:** `rack_stand_v2` is **not compatible** — the end caps (x=±43mm wide) physically collide with its foot (x=±35mm) at y=88mm, and moving the foot clear of the end caps shifts the camera 47mm off the card centre.

### Parts list (v24)

| STL | Qty | Bed dims | Notes |
|-----|-----|----------|-------|
| `pb_platen_back.stl` | 1 | 68×49×6mm | Entry half; 2 near registration nubs; 4 Ø8.5mm bumpon recesses on underside; 0.8mm centreline alignment groove |
| `pb_platen_front.stl` | 1 | 68×44×6mm | Far half; 1 left-far nub + 2mm finger-lift notch; 4 bumpon recesses on underside; 0.8mm centreline alignment groove |
| `pb_wall_half.stl` | **4** | 13.5×44×44mm | 2 per side; LED channel at top (z=33.6..44mm, 6mm deep, 3.2mm diffuser air gap); retention pegs on inner face; end cap sockets at both y-end faces |
| `pb_endcap_half.stl` | **4** | 46×5×44mm | 2 per y-face; chamfered 3mm peg for retention; 5×8mm LED cable exit slot at top-inner corner |
| `pb_led_diffuser.stl` | **4** | 43.6×10.0×0.8mm | Optional — slides in front of LED strip; softens hotspots |
| `pb_fit_test.stl` | **2** | 44×25×4mm | **Print before full set** — validates TAB_CL, PEG_CL, EC_SOCK_CL (~8 min each) |
| `pb_led_channel_test.stl` | **1** | 8×20×14.4mm | Print before wall_half — validates LED strip + diffuser channel fit (~3 min) |
| `pb_card_tray.stl` | 1 | 68×27×37mm | Optional deck holder for batch scanning; holds ~80 unsleeved cards; 15° gravity-assist ramp self-presents cards (6.7mm wedge floor at back) |

**10 structural pieces + 4 optional diffuser strips. Print fit_test × 2 and led_channel_test × 1 first.**

**Hardware:** 3M SJ5302 clear bumpons Ø7.9mm (8 required); 5V 10mm LED strip cut to 4 × 44mm segments; 5V USB power supply ≥1A.

### Print settings

| Part | Profile | Orientation | Infill | Brim |
|------|---------|-------------|--------|------|
| `pb_fit_test` | Recommended | **Flat (4mm tall)** — print 2× first | 15% gyroid | None |
| `pb_platen_back` | Recommended | **68mm in slicer Y** (not X) — flat (6mm tall); 68+3+3=74mm fits Y=78mm | 15% gyroid | 3mm |
| `pb_platen_front` | Recommended | **68mm in slicer Y** (not X) — flat (6mm tall); same orientation as back | 15% gyroid | 3mm |
| `pb_wall_half` | Recommended | **Standing** — outer face (stability foot) **down**, 13.5×44mm base, 44mm tall | 15% gyroid | ON |
| `pb_endcap_half` | Recommended | Flat on 46×44mm XZ face → **5mm tall** (body 3mm + peg 2mm) | 15% gyroid | None |
| `pb_led_diffuser` | Recommended | **Flat** (0.8mm tall = 4 layers); clear/natural PLA | 100% rectilinear | None |
| `pb_led_channel_test` | Any colour | Flat on 8×20mm face, 14.4mm tall — print before wall_half | 15% gyroid | None |
| `pb_card_tray` | Any colour | **68mm in slicer Y** — flat (37mm tall), no brim needed | 15% gyroid | None |

3 perimeter walls, 0.2mm layers. No supports.

### Assembly

See `docs/photo_box_assembly.md` for the full illustrated step-by-step manual with fit-test procedure, orientation guide, tolerance diagnosis, and disassembly.

**Quick sequence:**

1. **Join platen halves** — back half (2 nubs) toward you; press tabs into slots at y=44mm seam.
2. **Install bumpons** — flip platen over; press one 3M SJ5302 bumpon into each of the 8 Ø8.5mm recesses (4 per half). Flip right-side-up.
3. **Seat walls** — hold each wall half inner-face toward platen long edge, foot outward; slide straight **down** so pegs enter platen side-face slots. Repeat for all 4 halves (2 per side).
4. **Attach end caps** — **back end caps** (nub end): install with chamfered peg facing +Y into wall socket. **Front end caps** (notch end): flip each cap 180° around Z, then install peg facing −Y into wall socket. Rule: peg always faces INTO the box.
5. **Insert LED strips** — press a 44mm segment of 10mm-wide 5V adhesive strip into each wall's inner-face channel (10.4mm wide × 6mm deep, 0.2mm/side clearance). Route connector wire through the end cap cable exit slot. Optional: slide `pb_led_diffuser` strip in front to soften hotspots — the 3.2mm air gap provides photography-grade diffusion.

### LED strip spec

| Spec | Value |
|------|-------|
| Width | 10mm (standard 5V USB cut-to-length) |
| Colour | Warm white 3000–4000K for accurate card colour |
| Qty | **4 segments × 44mm** (one per wall half); ~176mm total strip length |
| Power | USB 5V **≥1A** minimum; ~40–60mA/segment × 4 = 160–240mA typical; wire in **parallel** only |
| Wire routing | Through end cap cable exit slot (5×8mm, top-inner corner) |

### Phone mount

The photo box requires an **overhead phone mount** at **263mm above the desk** (259mm above card face at z=4mm). At that distance the iPhone 16 Pro 24mm camera covers ~106×79mm — the 63×88mm card fits in frame in both portrait and landscape phone orientations. Recommended options:

| Type | Notes |
|------|-------|
| Desk gooseneck clamp (Tryone, Lamicall, SAIJI) | ~$15–25, 85cm arm, desk-edge clamp — most versatile |
| Arkon RoadVise 12" rigid gooseneck | 305mm reach, C-clamp — good for fixed setups |
| Overhead copy stand boom arm | Most stable for high-volume scanning |

Setup: clamp arm to desk edge; bend gooseneck to put phone face-down at 263mm, centred over the box. The box can sit 50–100mm from the desk edge; an 85cm arm reaches easily.

> **Why not rack_stand_v2?** The foot (70mm wide, x=±35mm) collides with the end caps (88mm wide, x=±44mm) when placed at y=88mm. Sliding the foot back clears the collision but shifts the camera off-axis beyond acceptable parallax. Use a separate mount for the photo box.

### Usage

1. Place photo box on desk, open top up.
2. Mount phone overhead at **263mm** lens height. With no card in the box, use the **0.8mm centreline groove** (visible as a dark hairline on the white platen) to centre the viewfinder left/right, then lock the arm.
3. Place card **face-up** on platen. Push near edge against the two near nubs (Y-stop), then push left edge against the left nubs (X-stop).
4. Right-far corner is open; a **2.5mm deep finger-lift notch** (2.2mm gap under card corner) helps slide a finger under the card for removal.
5. Power on LED strips. Scan.

**Card registration — 3-corner kinematic:**

```
  left-near nub ──┐     right-near nub ──┐
  (Y + X stop)    │     (Y stop)          │
  ┌───────────────┼───────────────────────┤
  │  card 63×88mm                         │
  │                                       │
  └───────────────────────────────── open ┘
  left-far nub (X stop)    right-far: OPEN + finger-lift notch
```

Push card into the near-left corner → 3 nubs constrain x, y, and rotation. Right-far corner stays open for lift-out.

### Rebuild photo box STLs

```bash
uvx --from build123d --with bd_warehouse python design/photo_box.py
# STLs land in design/output/pb_*.stl
# Individual part: AgentCAD params="PART=N"
#   1=platen_back  2=platen_front  3=wall_half  4=endcap_half  5=led_diffuser  6=fit_test  7=led_channel_test
```

---

## iPhone 16 Pro — focus distance (read this first)

These numbers drive **how tall the stand must be**. Getting this wrong produces blur or lens switching jitter.

| Distance (lens → card) | What happens |
|------------------------|--------------|
| **< ~14 cm** | iOS switches to **ultra-wide macro**; viewfinder can jitter between wide and macro. Works in Apple Camera / Magnifier; **some third-party scanners stay on wide and blur**. |
| **~14–25 cm** | **Dead zone** — main wide camera often **cannot lock focus**. Avoid this range. |
| **≥ ~26 cm** | **Main Fusion camera focuses reliably** in essentially any scanning app. Card occupies ~30% of frame height; use **2×** in Camera or in-app zoom for tighter framing without moving closer. |

**Design choice for this repo:** lens-to-card ≥ **260 mm**. With **3 segments**, lowest clamp ≈ **296 mm**; highest ≈ **331 mm** (nested joint stack accounted). `SEGMENT_COUNT` is the coarse knob.

### Compact alternative (not the default)

If you only scan in apps that honor ultra-wide macro (Apple Camera, Magnifier), you can build a **~10–11 cm** stand. Shorter and more stable, but **not reliable for all scanner apps**. Document any compact variant separately before regenerating geometry.

---

## Glare and torch lighting (holo / foil cards)

The phone torch sits **on-axis beside the lens** — the worst geometry for holo specular hotspots. This build uses three layers:

| Layer | What it does | Part |
|-------|----------------|------|
| **Off-axis + diffuse torch** | Baffle blocks direct torch→card ray; angled face + diffuser slot skim light ≥30° off-axis | `torch_deflector` |
| **Cross-polarization** | Linear film over torch (fixed) + over lens (**rotate dial** until glare nulls ~90° crossed) | `polarizer_base` + `polarizer_dial` |
| **Matte black in light path** | Absorbs stray scatter (white/glossy baffles reintroduce flare) | Print deflector + base in **black** |

**Workflow:**

1. Start with **`torch_deflector`** only; medium torch brightness.
2. If holos still clip, swap to **`polarizer_base`** + insert film; snap on **`polarizer_dial`**.
3. **Rotate the dial** while watching the preview until the holo hotspot disappears (expect ~1–3 stops less light — raise torch slightly).
4. Under **diffuse room light** (no torch), the dial still helps; deflector is optional.

**Also helps:** lens mask (black ring around window), plain white scan surfaces, card flat on lane.

### Drop-in cartridges (same seat on `phone_shelf`)

Both cartridges share one **3 mm rabbet** around the camera opening. Swap without reprinting the shelf.

1. **`torch_deflector`** — default; taller baffle, angled torch face, diffuser pocket for translucent insert.
2. **`polarizer_base` + `polarizer_dial`** — best glare kill; needs ~$10 linear polarizer film (two small squares: torch + lens).

---

## Set the height / zoom

Fine-tune lens-to-card distance with the **head clamp** on the post scale (coarse height = segment count).

| Scale tick (mm) | Lens → card (mm) |
|-----------------|------------------|
| 0 | ~296 |
| 5 | ~301 |
| 10 | ~306 |
| 15 | ~311 |
| 20 | ~316 |
| 25 | ~321 |
| 30 | ~326 |
| 35 | ~331 |

**How to set:** slide `head_clamp` to the tick that gives the framing you want → flip **`cam_lever`** down to lock → drop shelf on pins.

Re-run `py build_woodstand.py` after changing `SEGMENT_COUNT`; the script prints an updated table.

> **Print-and-tune:** The script verifies geometry only. Cam clamp force and dial friction depend on `POST_CL`, `CAM_ECC`, and `DIAL_CL` — expect one test print and light sanding per the slide-fit convention.

---

## Hardware reference

### Toybox Alpha 3 printer

| Spec | Value |
|------|-------|
| Build volume | **70 × 80 × 90 mm** (script usable **68 × 78 × 88**) |
| Filament | **1.75 mm PLA** — Toybox "Printer Food" **or third-party PLA** (both allowed) |
| Heated bed | **No** — use **brim** on large flat parts (mandatory) |
| Nozzle | 0.4 mm; quality **profile** sets layer height + speed |
| Slicer | Creator Space — **infill density**, **infill pattern**, adhesion (**none / skirt / brim**), supports (**none / basic / tree**) |

**Your spools:** **coconut** = official Toybox white; black/yellow/red/blue/teal/purple are likely third-party matte PLA — all fine.

**Two-color split:** coconut/white scan surfaces; **black** torch deflector + polarizer base.

**Profiles available in Creator Space:** Draft (skip) → **Recommended** (~0.2 mm) → **Better Quality** (~0.15 mm) → **Best Quality** (~0.1 mm). You can also set **infill density**, **infill pattern**, **adhesion**, and **support type** per print — see `output/PRINT-MANIFEST.md` for every STL.

---

### Print process (follow for every part)

Every STL must pass all seven steps before it is considered done. Do not skip steps on reprints.

1. **Generate** — run `py build_woodstand.py`; confirm the part prints `[OK]` + `watertight=True` and `verify_assembly()` passes.
2. **Preview** — run `py scripts/preview_stl.py output/<part>.stl`; confirm shape and bbox look right (AI iteration step — see [3DPrintedDecor guide](https://3dprinteddecor.com/how-to-use-claude-for-3d-printing/)).
3. **Import** — open Creator Space → *Create → Import STL* → select the file from `output/`.
4. **Orient** — rotate to the orientation in the table below. Do not let Creator Space auto-orient.
5. **Configure** — set Profile, **infill density**, **infill pattern**, **adhesion**, and **supports** from `output/PRINT-MANIFEST.md`. Check the slicer preview for overhangs before accepting.
6. **Print** — send to printer. Do not change filament mid-print.
7. **Tune and record** — test fit the part in assembly. If a slide fit is tight, sand and record the confirmed clearance (e.g. `POST_CL`, `DIAL_CL`, `CAM_ECC`) in the **Tuning log** below. Update `build_woodstand.py` and this README immediately.

> **Maintenance rule:** any time a parameter in `build_woodstand.py` is physically confirmed or corrected after a test print, update both the parameter value in the script *and* the tuning log in this section. The README is the living manual — it must stay in sync with what actually prints.

---

### Per-part settings

| Part | Profile | Brim | Supports | Filament | Orientation |
|------|---------|------|----------|----------|-------------|
| `base_left` / `base_right` | **Recommended** | **ON** | None | Coconut/white | Flat (Z-up) |
| `column_segment` ×3 | **Recommended** | **ON** | None | Any matte | **Vertical, boss down** |
| `head_post` | **Better Quality** | **ON** | None | Any matte | **Vertical, boss down** |
| `head_clamp` | **Better Quality** | **ON** | Basic (ears only if slicer flags) | Any matte | Bore vertical, collar flat |
| `cam_lever` | **Better Quality** | None | None | Any matte | Flat, handle extending |
| `clamp_pin` | **Better Quality** | None | None | Any matte | Upright, head down |
| `phone_shelf_left` / `phone_shelf_right` | **Recommended** | **ON** | None | Coconut/white | Flat |
| `torch_deflector` | **Better Quality** | **ON** | None | **Black** | Flat, baffles up |
| `polarizer_base` | **Better Quality** | **ON** | None | **Black** | Flat |
| `polarizer_dial` | **Best Quality** | **ON (wide brim)** | None | Black | Flat, disc face up |
| `card_lane_left` / `card_lane_right` | **Recommended** | **ON** | Check ramp in preview | Coconut/white | Flat, ramp up |
| `card_magazine_left` / `card_magazine_right` | **Recommended** | **ON** | None (vertical walls self-support) | Coconut/white | Join face down, open top up |
| `card_magazine_lid` | **Recommended** | None | None | Any | Flat (lid face down) |
| `nest_frame` | **Recommended** | **ON** | None | Coconut/white | Flat, channels up |
| `nest_tray_ramp` / `nest_tray_bin` | **Recommended** | **ON** | None | Coconut/white | Flat, deck face up |
| `nest_stop` | **Recommended** | None | None | Coconut/white | Flat |

**Infill density, infill pattern, adhesion (none/skirt/brim), and support type (none/basic/tree)** for every STL: [`output/PRINT-MANIFEST.md`](output/PRINT-MANIFEST.md) (includes Pokémon color column).

**Slicer notes:**
- Set **infill density and pattern explicitly** in Creator Space — profile alone is not enough.
- `polarizer_dial` (2.2 mm disc): use the widest brim Creator Space allows; print solo.
- `head_clamp` axle holes bridge ~8 mm — check preview; Basic supports only if slicer flags drooping (not Tree — too hard to remove from a small bore).
- `card_lane_*` ramp is a stepped staircase (self-supporting); Tree supports only if Creator Space flags the ramp underside.
- `clamp_pin` alternative: cut a 26 mm section of the 8 mm dowel — stronger, zero fit issue.

---

### Tuning log

Record confirmed clearance values here after physical test prints. These feed back into `build_woodstand.py`.

| Parameter | Script default | Confirmed value | Part | Notes |
|-----------|---------------|-----------------|------|-------|
| `POST_CL` | 0.4 mm | — | `head_clamp` bore on `head_post` | Sand runway −x face if clamp binds |
| `CAM_ECC` | 2.5 mm | — | `cam_lever` | Increase if lever doesn't lock over-center |
| `DIAL_CL` | 0.1 mm | — | `polarizer_dial` in `polarizer_base` race | Increase if dial won't snap in; decrease if it rattles |
| `JOIN_CLEAR` | 0.25 mm | — | All dovetail / T&G joints | Sand dovetail if halves won't slide |

_Last tuned: not yet printed._

### iPhone 16 Pro (rear)

| Spec | Approx. value |
|------|----------------|
| Body | 149.6 × 71.5 × 8.25 mm, ~199 g |
| Main camera | 48 MP Fusion, 24 mm equiv., f/1.78 |
| Macro | Ultra-wide auto-macro below ~14 cm |
| Torch | Dual LED, adjacent to camera cluster (top-left on back) |

Phone sits **screen-up** on the shelf; **camera bump over the opening**; body lies **back over the column** so only the lens end cantilevers forward (~30–40 mm) over the card.

### Standard trading card

**63 × 88 mm** raw **unsleeved** (Pokémon / MTG / most TCG). Sleeves add glare and bow — lane and future feeder are sized for raw cards. Adjust in `build_woodstand.py` only if you deliberately scan sleeved cards.

---

## Phase-2 card magazine (implemented)

A **gun-magazine style** preloaded cartridge that snaps onto the left face of `card_lane_left`. Load a stack of cards off the scanner, snap the magazine on, scan until empty, pop it off and swap the next — ~3 seconds to reload.

### How it works

```
  Load cards (top open)
       ↓
  [card_magazine_left + card_magazine_right assembled]
       |  cards stacked face-to-face in Z (up to ~128 cards)
       |  bottom card rests at Z = 22 mm (hopper floor)
       ↓
  Dock gesture: hold magazine above lane left face → push DOWN →
                spring tab cams over ledge → CLICK — seated
  Release:      thumb presses spring tab → lift straight UP
```

### Magazine dock features on `card_lane_left`

- **Guide rails** — two 3×6 mm rectangular protrusions on the left face (front and back of lane), spanning full hopper height. Magazine guide slots slide over them.
- **Latch notch** — 4 mm deep × 6 mm wide pocket centred in Y; the magazine spring tab snaps in.

### Magazine cartridge parts

| Part | Qty to print | Notes |
|------|-------------|-------|
| `card_magazine_left.stl` | 3 | Outer wall + dovetail join face |
| `card_magazine_right.stl` | 3 | Guide slots + spring latch tab on lane-mating face |
| `card_magazine_lid.stl` | 6 | One per half; optional snap-on lid for transport |

Assemble two halves with the dovetail join (same `JOIN_CLEAR = 0.25 mm` slide fit as base and shelf). Lid snaps onto the open top via 2 mm inner lip.

**Tune:** if the spring tab is too stiff/loose, adjust `MAG_TAB_THK` (thinner = less force) and reprint `card_magazine_right`. Aim for ≈3–5 N thumb force.

### Card lane zones (`LANE_RAMP_END_GX = 48` — authoritative)

| Zone | Lane-local X | Height | Role |
|------|--------------|--------|------|
| Hopper / magazine throat | 0–12 | **22 mm** | Magazine exit; servo horn slot (Phase-3a) |
| Curved ramp | 12–~50 | 22 → 0 mm | Gravity feed |
| Scan nest | ~50–88 | **z0** | Imaging |
| Bin exit | 86–92 | −5 mm step | Card drop into bin or tray |

**Manual use (single card):** place one card directly on ramp or nest; optional stop pin in right segment socket. Long edge **+X**, short edge across **Y** (63 mm rails).

## Phase-2a scan deck / nest tray (implemented)

Full-width **88 mm** flat scan surface with slide-out bin tray. Split at `NEST_TRAY_JOIN_X = 68 mm` for Toybox bed.

| Part | Role |
|------|------|
| `nest_frame.stl` | U-channel frame; sits over lane scan zone; two anchor sockets |
| `nest_tray_ramp.stl` | Ramp-side tray half; join peg |
| `nest_tray_bin.stl` | Bin-side tray half; finger cutout for pull-out |
| `nest_stop.stl` | Hard return stop; drops into anchor socket |

Print nest parts in **coconut/white** (scan surface). Frame fits over lane; tray slides in from the bin end and is held by the stop tab.

**`verify_assembly()`:** lens XY over scan nest only (≤2 mm); height from `report_height()`.

---

## Wood part (the only one)

| Part | Stock | Notes |
|------|-------|-------|
| **Spine dowel** | **8 mm** hardwood/birch dowel, cut to **~252 mm** | Through split base → 3 segments → `head_post` socket |

**Assembly order:**

1. Join **base_left** + **base_right** (dovetail + bottom T&G); fill ballast cavity.
2. Stack **column_segment** ×3; seat **head_post**; drop **dowel**.
3. Slide **head_clamp** (match D-index flat); install **cam_lever** + **clamp_pin**; lock.
4. Join **phone_shelf_left** + **phone_shelf_right**; drop onto clamp pins.
5. Join **card_lane_*** halves; registration tab to base front anchors.
6. Insert glare cartridge; confirm `verify_assembly()` passes in build report.
7. **Phase-2:** Load cards into a **card_magazine** cartridge; hold above lane left face, push DOWN until spring tab clicks. To remove: press tab, lift UP.
8. **Phase-2a:** Seat **nest_frame** over scan zone; slide in **nest_tray** halves from the bin end; drop **nest_stop** into anchor socket.

To break down: unlock cam → pull dowel → separate joinery halves. Sand slide fits if tight.

---

## Printed parts

Generate STLs from the parametric script:

```bash
pip install -r requirements.txt
py build_woodstand.py
# Output: output/*.stl + ASSEMBLY CHECK + height report
```

**Phase 1 — stand (always print these):**

| File | Qty | Purpose |
|------|-----|---------|
| `base_left.stl` / `base_right.stl` | 1 each | Split ballast (120×72 assembled); dovetail + T&G |
| `column_segment.stl` | **3** | Slide-nest posts (print vertical) |
| `head_post.stl` | 1 | Scaled runway + D-index flat |
| `head_clamp.stl` | 1 | Bilateral split collar + shelf pins |
| `cam_lever.stl` / `clamp_pin.stl` | 1 each | Cam lock |
| `phone_shelf_left.stl` / `phone_shelf_right.stl` | 1 each | Split shelf; camera toward front |
| `torch_deflector.stl` | 1 | Off-axis baffle (**black**) |
| `polarizer_base.stl` / `polarizer_dial.stl` | 1 each | Cross-pol dial (**black** base) |
| `card_lane_left.stl` / `card_lane_right.stl` | 1 each | Gravity ramp chute + magazine dock rails (**coconut/white**) |

**Phase 2 — card magazine (print per magazine set wanted):**

| File | Qty | Purpose |
|------|-----|---------|
| `card_magazine_left.stl` | **3** (one per cartridge) | Outer wall + dovetail join |
| `card_magazine_right.stl` | **3** | Guide slots + spring latch tab; mates to lane |
| `card_magazine_lid.stl` | **6** (two per cartridge) | Snap-on lid for transport |

**Phase 2a — nest tray (optional scan-deck upgrade):**

| File | Qty | Purpose |
|------|-----|---------|
| `nest_frame.stl` | 1 | Scan deck frame with U-channels |
| `nest_tray_ramp.stl` / `nest_tray_bin.stl` | 1 each | Slide-out tray halves |
| `nest_stop.stl` | 1 | Hard return stop tab |

Script checks: bbox ≤ 68×78×88, watertight, **`verify_assembly()`** lens over scan nest.

**Print settings:** see [`output/PRINT-MANIFEST.md`](output/PRINT-MANIFEST.md) — infill density, pattern, orientation, and brim for all 21 stand STLs. CS2 hopper/rack STL print notes are in [`HANDOFF.md`](HANDOFF.md) Printable parts table.

### Joinery

- **Base + shelf:** sliding dovetail on vertical join face; tongue-and-groove on bottom
- **Column / head:** 28 mm boss → 28.4 mm recess; 8 mm dowel
- **Lane:** butt-join + registration tab; lane position set so scan nest aligns under lens

---

## Scanning workflow

1. Tape or clamp the **base**; assemble lane segments in front of the column.
2. Set clamp height on the post scale; lock with **cam_lever**.
3. Drop in **`torch_deflector`** or **polarizer** cartridge; rotate dial to null holo glare if using polarizer.
4. Lay phone on shelf; centre main lens over the left window; enable **2×** if the card looks small.
5. Torch **medium** brightness (or use diffuse room light only).
6. Slide **unsleeved** card into lane; use centre stop pin for repeat positioning.
7. Scan; repeat.

**Glossy holo still clipping?** Cross-polarize with the dial; check deflector is **black** matte PLA.

---

## Repository layout

```
card-scanner/
├── README.md                 ← this file (human build guide)
├── CLAUDE.md                 ← AI agent instructions (MCP + skills)
├── .cursor/
│   ├── hooks.json            ← sessionStart → MCPmarket skill sync
│   ├── hooks/
│   │   └── sync-mcpmarket-skills.sh
├── build_woodstand.py        ← parametric CAD → STL (current design)
├── requirements.txt          ← numpy, trimesh, manifold3d, scipy
├── output/                   ← generated STLs (gitignored)
└── docs/
    ├── photo_box_assembly.md   ← full photo box assembly manual (v17)
    ├── mcp-skills-research.md  ← MCPmarket + skillfish install guide
    └── legacy-full-print.md
```

---

## AI assistant tooling

Full agent routing lives in [`CLAUDE.md`](CLAUDE.md). Two separate mechanisms:

### MCP servers (external tools — Cursor)

| Server | Config source | Use on this project |
|--------|---------------|---------------------|
| **chrome-devtools** | `~/.cursor/mcp.json` | Browser research: iPhone specs, glare techniques, reference stand designs |
| **chrome-devtools-ext** | `~/.cursor/mcp.json` | Extension testing only (optional) |
| **mcpmarket-my-toolkit** | **Plugin MCP Servers** (Cursor UI, OAuth) | MCPmarket login. Shows **“No tools”** — expected. Skills sync to disk instead. |

### MCPmarket skills (filesystem — not MCP tools)

Mirrors Claude Code: baseline skills sync on session start.

| Piece | Location |
|-------|----------|
| Hook | `.cursor/hooks.json` |
| Sync script | `.cursor/hooks/sync-mcpmarket-skills.sh` |
| Skills output | `~/.cursor/skills/mcpmarket/` |

Manual sync: `"C:\Program Files\Git\bin\bash.exe" .cursor/hooks/sync-mcpmarket-skills.sh`

### Agent skills (install via skillfish — not vendored here)

Full research: [`docs/mcp-skills-research.md`](docs/mcp-skills-research.md)

Use [skillfish](https://github.com/knoxgraeme/skillfish) (MCPmarket ecosystem). `--project` installs to **`.claude/skills/`** (Claude Code) and **`.cursor/skills/`** (Cursor):

```powershell
npx skillfish add mitsuhiko/agent-stuff openscad --project --yes
npx skillfish add chriscantey/skill-3d-printing --project --yes
npx skillfish add addyosmani/agent-skills spec-driven-development --project --yes
npx skillfish add addyosmani/agent-skills incremental-implementation --project --yes
npx skillfish add addyosmani/agent-skills planning-and-task-breakdown --project --yes
```

| Skill (project) | Claude Code | Cursor |
|-----------------|-------------|--------|
| openscad | `.claude/skills/openscad/` | `.cursor/skills/openscad/` |
| 3DPrinting | `.claude/skills/3DPrinting/` | `.cursor/skills/3DPrinting/` |
| spec-driven-development | `.claude/skills/spec-driven-development/` | `.cursor/skills/spec-driven-development/` |
| incremental-implementation | `.claude/skills/incremental-implementation/` | `.cursor/skills/incremental-implementation/` |
| planning-and-task-breakdown | `.claude/skills/planning-and-task-breakdown/` | `.cursor/skills/planning-and-task-breakdown/` |

After install, reload Cursor and **restart Claude Code** in this repo so both agents pick up project skills.

MCPmarket baseline skills sync to `~/.cursor/skills/mcpmarket/` on session start.

**Global** (still useful):

| Skill | When |
|-------|------|
| **grinding-until-pass** | Loop `python build_woodstand.py` until every STL passes |
| **canvas** | Assembly diagrams, light-path visuals |
| **create-rule** | Persist conventions in `.cursor/rules/` |
| **deep-bug-hunt** | Audit geometry commits for bed overflow |

---

## Design history (why two scripts)

| Phase | Approach | Outcome |
|-------|----------|---------|
| 1 | All-print modular stand | Focus dead zone at ~13.5 cm |
| 2 | Taller all-print tower | Optically OK but tippy on Toybox |
| 3 | Plastic column + fixed arm | Stable; ~279 mm lens; no height tune / fixed pol |
| 4 | **Adjustable head + cross-pol dial + card lane** (current) | 296–331 mm tune range; rotatable null; Phase-2a feeder spec |

Reference inspirations (not sized for Toybox bed): Ultimate Card Scanner Stand (MakerWorld), Card Slinger, various MTG/Pokémon Thingiverse copy stands — same **phone above card, camera down** principle.

---

## Tuning parameters (`build_woodstand.py`)

Edit constants at the top of the script, then re-run:

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `SEGMENT_COUNT` | 3 | Coarse lens height (≥3 for focus) |
| `POST`, `POST_CL`, `CAM_ECC` | 22, 0.4, 2.5 | Clamp slide + cam lock (sand to tune) |
| `SCALE_STEP`, `SCALE_MAJOR` | 5, 20 | Post engraving interval (mm) |
| `DIAL_CL`, `RACE_LIP` | 0.1, 1.5 | Polarizer dial fit |
| Camera opening (OX0…OY1) | 4–38 × 6–34 mm | iPhone 16 Pro cluster + torch |
| `LANE_RAMP_TOP`, `LANE_RAMP_END_GX` | 22, **48** | Hopper height + ramp/flat reference |
| `PUSHER_SLOT_W` | 20 | Horn slot — servo linkage (Phase-3a), not card pusher |
| `MAG_TAB_THK` | 2.0 mm | Magazine spring tab thickness — thinner = less snap force |
| `MAG_RAIL_D` | 6.0 mm | Dock rail protrusion depth — increase if magazine rattles |
| `MAG_STACK_Z` | 45.0 mm | Magazine internal stack height (~128 cards max) |

**Case users:** measure cased phone footprint; widen `SX`/`SY` and opening if needed (stay ≤ 74 mm bed width or split shelf — open an issue before splitting).

---

## Next steps / open work

- [ ] Print **head_clamp** + **cam_lever** first; tune slide/clamp feel (`POST_CL`, `CAM_ECC`)
- [ ] Print **polarizer_dial** + base; tune `DIAL_CL` rotation friction
- [ ] Print **card_lane_left/right** in coconut/white; verify 63×88 card registers under lens
- [ ] Order linear polarizer film; test rotate-to-null workflow on holo cards
- [ ] Fill ballast; confirm stability at max cantilever
- [ ] Print **card_magazine_right** test piece; verify spring tab snap force — tune `MAG_TAB_THK` if needed
- [ ] Print 3× full magazine sets in coconut/white; test load/unload cycle
- [ ] Print **nest_frame** + tray halves; verify slide-in and scan position
- [ ] Phase-3a: SG90 servo drives card push via existing `PUSHER_SLOT` horn slot

---

## Bill of materials (summary)

| Item | Qty |
|------|-----|
| Matte PLA 1.75 mm — coconut/white + black (Toybox spools) | partial spools |
| 8 mm wood dowel | ~260 mm |
| Linear polarizer film sheet | optional |
| M3 screws / inserts | Phase-2 feeder only |
| Sand for ballast | fill base cavity |

---

## License / attribution

Parametric models in this repo are original work for the Toybox + iPhone 16 Pro constraints. Reference stand concepts credited above. Use and modify for personal scanning; regenerate STLs from the Python source when retuning.
