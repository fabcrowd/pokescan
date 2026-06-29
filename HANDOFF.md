# HANDOFF — CS2 card scanner (updated 2026-06-28, v153)

## CS2 SYSTEM STATUS: PRINT-READY + DOCUMENTED — ALL STLs IN design/output/

### CS2 files (design/ directory)
| File | Status | AgentCAD | Parts |
|------|--------|----------|-------|
| cs2_hopper.py | VALIDATED v5 | v269-271 | PART=0 assembly 97×72×70mm, 1 left-half 48.5×72×70mm, 2 right-half; v4 Phase-2 changes + v5 thumb-push hole in back wall (25×14mm, z=2..16mm); Phase-1 manual eject without any automated parts; cs2_verify.py 31/31 PASS |
| cs2_platform.py | VALIDATED v2 | v204/214 | PART=0 single piece; bolt holes now Y-direction |
| cs2_wall.py | VALIDATED v2 | v205-208/215-218 | PART=0 assembly, 1-4 printable sections; hole Z corrected |
| cs2_peg.py | VALIDATED v1 | v219 | 4× alignment peg print plate (3mm×10mm) |
| cs2_pol_clip.py | VALIDATED v1 | v220 | Polarizer film clip for 36x30mm aperture (aperture side) |
| cs2_phone_pol.py | VALIDATED v1 | v221 | Phone camera polarizer film frame (lens side) |
| cs2_fit_test.py | VALIDATED v1 | v222 | Fit test plate: peg/bolt holes + pol_clip aperture ring |
| cs2_diffuser.py | VALIDATED v1 | v224 | White PLA torch diffuser plate (sits on platform top) |
| cs2_assembly_scene.py | VALIDATED v1 | v223 | Full assembly scene (NOT printable -- visualization only) |
| cs2_height_preview.py | VALIDATED v1 | v226 | Height comparison scene: 100/125/150mm side by side (NOT printable) |
| cs2_centering_insert.py | VALIDATED v3 | v246-248 | Funnel collar clips onto hopper top; PART=0 full collar, 1 left half, 2 right half; loft-based taper (v1/v2 wedge approach scrapped) |
| cs2_roller.py | VALIDATED v2 | v249/250 | Rubber-gasket drum roller (OD=17mm, L=20mm, bore=6.2mm slip-fit); two 3mm×1.5mm O-ring grooves at z=3/12mm; PART=0 single 20×17×17mm, PART=1 plate of 4 39×43×17mm; **SHAFT_Z must change to 12.5mm in cs2_hopper.py before printing** (current hopper v2 has SHAFT_Z=8mm) |
| cs2_separator.py | VALIDATED v1 | v251/252 | Adjustable card separator; body (35×5×22mm) + gap plate (14.8×3×12mm); M3 setscrew from body top sets gap 0.5-1.5mm; mounts to hopper front face boss holes at ±15mm |
| cs2_motor_bracket.py | VALIDATED v1 | v230 | Phase 2 SG90 servo mount; U-channel cradle + 4x M3 holes + zip-tie slots |
| **cs2_card_pusher.py** | **VALIDATED v1** | **v262/263** | **PART=1 crank_arm 29x9x6mm (D-flat hub + 22mm arm + tip pin socket), PART=2 push_rod 31x5x3mm (3mm pin sockets each end); STLs exported** |
| cs2_preview.py | VALIDATED | v203 | Full assembly scene (hopper+wall+2 platforms) |
| cs2_verify.py | ALL PASS | (pure Python) | 31/31 dimension+clearance+alignment+peg checks |
| **cs2_rack_stand.py** | **VALIDATED v2** | **v256-261** | **PART=0 assembly, 1 rack_section 26×26×84mm, 2 foot 50×40×54mm, 3 carriage 37.2×47×50mm, 4 knob 29.7×29.7×41.6mm, 5 platform 65×75×25mm, 6 fit_test 42×38×20mm; all STLs exported to design/output/** |
| **photo_box.py** | **VALIDATED v3** | **v239-240** | **PART=0 assembled (67x104x40mm), PART=1 single half (67x52x40mm, print 2x white PLA); STANDALONE -- does NOT interface with cs30_arch (which was for photo_box v25, 84mm wide); old designs/design/cs30_verify.py 19/19 PASS (old system unchanged)** |

### Phase-2 open items (before reprinting hopper)
| Item | Status |
|------|--------|
| Card exit opening in hopper wall | **DONE v4** — EXIT_W widened 15→90mm (= SLOT_L); card body exits through same opening as push-rod arm; STLs in design/output/. |
| Hopper SHAFT_Z 8mm → 12.5mm (roller v2) | **DONE v4** — SHAFT_Z updated; peg hole moved z=17→19mm to maintain 2mm clearance from shaft top. |

### Printable parts — 11 STLs in design/output/cs2_*.stl (all fit Toybox 68x78x88mm)
| STL file | Dims (mm) | Print notes |
|----------|-----------|-------------|
| **cs2_fit_test.stl** | **64x38x20** | **PRINT FIRST** -- same PLA as target parts; validates holes and pol_clip fit |
| cs2_hopper_left.stl | 48.5x72x70 | Black PLA, print upright; v5 (thumb-push hole in back wall for manual eject) |
| cs2_hopper_right.stl | 48.5x72x70 | Black PLA, print upright; v5 |
| cs2_platform.stl | 68x75x8 | Black PLA, print flat |
| cs2_wall_bot_left.stl | 49.5x20x88 | Black PLA, print upright |
| cs2_wall_bot_right.stl | 49.5x20x88 | Black PLA, print upright |
| cs2_wall_top_left.stl | 49.5x14x88 | Black PLA, print upright |
| cs2_wall_top_right.stl | 49.5x14x88 | Black PLA, print upright |
| cs2_peg.stl | 10x10x10 | PETG preferred; 4 pegs, use 2 per hopper assembly |
| cs2_pol_clip.stl | 44x38x8 | White PLA, print flat; OPTIONAL cross-pol aperture side |
| cs2_phone_pol.stl | 44x38x3 | White PLA, print flat; OPTIONAL cross-pol lens side |
| cs2_diffuser.stl | 68x75x1.5 | White PLA, print flat + BRIM; OPTIONAL torch scatter plate |
| cs2_centering_insert_left.stl | ~51.5x78x30 | White PLA, flat (30mm tall); print 1x; join with right half |
| cs2_centering_insert_right.stl | ~51.5x78x30 | White PLA, flat (30mm tall); print 1x; join with left half |
| cs2_roller.stl | 20x17x17 | PETG; single drum assembly reference; Phase 2 (requires SHAFT_Z=12.5mm hopper) |
| cs2_roller_plate.stl | 39x43x17 | PETG; plate of 4 drums; 2x assembly + 2x spare; Phase 2 — print when hopper reprinted |
| cs2_separator_body.stl | 35x5x22 | PLA, print flat (5mm tall); Phase 2 single-card gate |
| cs2_separator_gap_plate.stl | 14.8x3x12 | PLA, print flat (3mm tall); adjust gap 0.5-1.5mm via M3 setscrew |
| cs2_motor_bracket.stl | 42x15x32 | PLA or PETG, flat; Phase 2 servo mount for hopper front face |
| cs2_crank_arm.stl | 29x9x6 | PLA, print flat (hub base down); Phase 2 servo crank; see docs/phase-2-cs2-motor.md |
| cs2_push_rod.stl | 31x5x3 | PLA, print flat; Phase 2 connecting rod (3mm pins at each end) |
| **cs2_rack_stand_fit_test.stl** | **42×38×20** | **Print FIRST — 4 tolerance features (rail bore, D-socket, lock bolt, rack stub)** |
| cs2_rack_stand_rack_section.stl | 26×26×84 | Print 2×, upright; D-peg top + D-socket bottom stacks sections |
| cs2_rack_stand_foot.stl | 50×40×54 | Print flat; column base, front face flush with hopper back |
| cs2_rack_stand_carriage.stl | 37×47×50 | Print flat, bore-side up; M3 lock bolt on -X face |
| cs2_rack_stand_knob.stl | 30×30×42 | Print upright, hub down; 8-tooth pinion + 30mm thumb disc |
| cs2_rack_stand_platform.stl | 65×75×25 | Print face-down (lips up); 36×30mm camera aperture + lip clips |

### Hardware BOM (per scanner)
| Item | Qty | Spec | Use |
|------|-----|------|-----|
| M3×30 bolt | 8 | socket head | platform-to-wall (2) + section joins (6) |
| M3×20 bolt | 6 | socket head | hopper half joins (2) + spare |
| M3 nut | 14 | standard hex | all bolt receivers |
| 3mm dowel pin | 2 | from cs2_peg.stl | hopper seam alignment |
| CA glue | small | cyanoacrylate | wall flange to hopper back face (Phase 1) |
| 16mm ID O-ring | 2× per roller | 16mm ID × 2mm cross-section rubber (plumbing sink gasket) | seats in cs2_roller v2 gasket grooves; Phase 2 |
| M3x12 setscrew | 1 | hex socket or flat | cs2_separator gap adjustment from body top face |

### What loop built this iteration (v153)
- cs2_hopper.py v5: Phase-1 manual operation — thumb-push hole in back wall
  - 25mm wide × 14mm tall rectangular cutout in back wall (y=+OUTER_W/2)
  - Centred at x=0 (spans both halves; each half gets a 12.5×14mm notch at its seam face)
  - z=2..16mm: starts 2mm below card floor so thumb slips UNDER card and pushes its face/body,
    not the narrow 0.8mm card edge — avoids card damage, safe for bare and sleeved cards
  - Clears peg holes (z=19mm) by 1.5mm; no conflict with end-wall shaft holes (different walls)
  - Phase-2 parts (servo, roller, bracket) remain optional bolt-ons; manual flow works without them
  - AgentCAD v269 (PART=0): is_valid=true, 97×72×70mm, face_count=33 ✓
  - AgentCAD v270 (PART=1 left): is_valid=true, 48.5×72×70mm ✓ — STL exported
  - AgentCAD v271 (PART=2 right): is_valid=true, 48.5×72×70mm ✓ — STL exported
  - cs2_verify.py 31/31 PASS
  - Manual scan workflow: drop card top → scan → push thumb through back-wall hole → card exits front slot

### What loop built this iteration (v152)
- cs2_hopper.py v4: Phase-2 CAD — both deferred open items resolved
  - EXIT_W widened 15mm → 90mm (= SLOT_L): original 15×4mm slot was arm-port only; card body (88mm)
    could not exit. New 90×4mm opening matches inner slot width, giving card 1mm clearance each side.
  - SHAFT_Z 8.0 → 12.5mm: roller v2 has OD=17mm; shaft at 12.5mm centres roller bottom at z=4mm
    (card floor), giving correct 0.8mm nip compression on 0.8mm card.
  - Peg hole z=17 → 19mm: maintains 2.0mm clearance from new shaft top (z=15.5mm); was 0mm at z=17.
  - cs2_verify.py: SHAFT_Z_H 8→12.5, PEG_Z 17→19, BOLT_Z_H 25→35 (stale v2 value corrected)
  - AgentCAD v266 (PART=0 assembly): is_valid=true, 97×72×70mm ✓
  - AgentCAD v267 (PART=1 left): is_valid=true, 48.5×72×70mm ✓ — STL exported
  - AgentCAD v268 (PART=2 right): is_valid=true, 48.5×72×70mm ✓ — STL exported
  - cs2_verify.py 31/31 PASS
  - Both STLs copied to design/output/cs2_hopper_left.stl / cs2_hopper_right.stl
  - Phase-2 hopper reprint is now unblocked; see docs/phase-2-cs2-motor.md for assembly sequence

### What loop built this iteration (v151)
- photo_box.py v3: lighting geometry pass -- LED channel redesigned to be practical
  - v2 LED groove was 2mm wide in a 2mm wall: no real LED strip (5-10mm wide) could fit
  - Web search finding: 5050 SMD single-row strip = 10mm wide, ~2.5mm thick (source: superlightingled.com)
  - Fix: long wall thickness stays 2mm (Toybox X constraint); end walls thickened to END_T=5mm
    - End walls are in the Y direction where there is room (52mm per half vs 78mm Toybox)
    - Inner face of each end wall now has 63mm x 10mm x 3mm LED channel at z=25..35mm
    - 5mm end wall - 3mm channel = 2mm material behind LED strip (adequate for PLA/PETG)
  - Long walls (2mm white PLA): no groove, pure diffuser surface -- light from end LEDs bounces
  - Autonomous decision: LED strips at end walls facing inward/downward (not in long walls)
    - Long walls are Toybox-constrained to 2mm -- no room for any LED channel
    - End walls in Y direction are unconstrained; 5mm allows proper 3mm channel
    - End-wall strip shines across 63mm card width, reflects off white 2mm long walls
  - PART=0 assembly: AgentCAD v239, is_valid=true, 67x104x40mm ✓
  - PART=1 single half: AgentCAD v240, is_valid=true, 67x52x40mm ✓ (fits Toybox 68x78x88mm)

### What loop built this iteration (v150)
- photo_box.py v2: CS2 scan hood (open-frame LED diffuser ring, two-piece)
  - Interior: 63mm X (tight card fit) x 94mm Y (card 88mm + 3mm each end), open top + open bottom
  - Wall thickness: 2mm all sides; exterior per half: 67×49×40mm — fits Toybox 68×78×88mm (1mm margin X) ✓
  - Long walls (X walls) have 2×3mm LED strip groove at top inner edge for ring illumination
  - End wall preserved at Y=HALF_L (far end); join face at Y=0 open (split seam between halves)
  - Alignment pin sockets: Ø3mm × 5mm deep at x=±22mm on join face; push 5mm into each half
  - PART=0 (assembly Compound): AgentCAD v237, is_valid=true, 67×98×40mm ✓
  - PART=1 (single half): AgentCAD v238, is_valid=true, 67×49×40mm ✓
  - v1 bug: interior cavity spanned full Y including end wall → end walls removed → Z=37mm not 40mm
  - v2 fix: cavity limited to INT_HALF_L+0.5 = 47.5mm in Y → end wall (2mm) preserved correctly
  - Autonomous decision: LED groove on outer TOP of long wall (strip rests in groove, faces inward/downward)
    - Alternative was inner-face groove (harder to model, LED shines sideways)
    - Top groove simpler to model, LED faces card naturally, strip held by gravity + snap fit

### What loop built this iteration (v149)
- cs2_rack_stand.py v2: adjustable rack-and-pinion phone stand for CS2 hopper
  - PART selector added: 0=assembly, 1=rack_section, 2=foot, 3=carriage, 4=knob, 5=platform, 6=fit_test
  - fit_test() added: 42x38x20mm block with 4 tolerance features (rail bore, D-socket, lock bolt, rack stub)
  - Bug fix: PHONE_OFFSET_Y -38.5→-35.5 (M3 holes were 1mm outside platform body in v1)
  - Camera now at world y=3mm (vs 0mm target; 3mm off 63mm-wide card is negligible)
  - AgentCAD v233 (PART=0 assembly): is_valid=true, 97x176.6x214mm ✓
  - AgentCAD v234 (PART=6 fit_test): is_valid=true, 42x38x20mm ✓
  - AgentCAD v235 (PART=5 platform): is_valid=true, 65x75x25mm ✓ (25mm not 17mm — rubber band pegs add 8mm)
  - Foot front face at y=36mm = hopper back face — abuts flush, no gap
  - Camera-to-card range: 101..211mm (CS2 scan target 104..169mm fully covered)
  - Next: export STLs for all PART values; verify rack_section/foot/carriage/knob visually

### What loop built this iteration (v148)
- cs2_motor_bracket.py v1: SG90 servo mount for hopper front face (Phase 2)
  - Plate (42x3x32mm) with 4x M3 through-holes at boss positions (x=+/-15mm, z=18/36mm)
  - U-channel cradle (28x12x27mm outer, 23x10x23mm servo channel) extends 12mm behind plate
  - Servo body (22.5x12x22mm) slides into open +Y face; shaft faces hopper in -Y
  - 2x zip-tie slots (10x3.2mm) through plate for secondary servo retention
  - Total: 42x15x32mm -- fits Toybox 68x78x88mm usable (42x32mm footprint, 15mm tall) ✓
  - AgentCAD v230: is_valid=true, 42x15x32mm, CoM x=0.0 (symmetric), face_count=29 ✓
  - Exported to design/output/cs2_motor_bracket.stl
  - Do NOT print until cs2_card_pusher.py (crank arm + push rod) is designed
- Web search finding: N20 motor output shaft is 3mm D-flat, 9.5mm long
  - N20 motor is NOT suitable for the front-face bracket (shaft at z=28mm != roller shaft at z=8mm)
  - SG90 servo is the right actuator: servo arm drives a connecting rod in XZ plane
  - 22mm arm at z=28mm (servo shaft height) -> crank throw reaches z=6mm (exit slot) ✓
- Autonomous decision: servo shaft faces hopper (-Y) not user (+Y)
  - Shaft facing hopper means arm sweeps in XZ plane toward the exit slot region
  - If shaft faced user, arm would swing into thin air away from the mechanism
  - Back wall (1.5mm at y=3..4.5mm) anchors servo body; zip-ties hold it in place

### What loop built this iteration (v147)
- cs2_roller.py v1: Phase 2 card-eject drive roller
  - Rides on 6mm shaft through hopper end wall shaft holes (SHAFT_D=6mm at z=8mm)
  - OD=8mm: roller bottom at z=4mm = exactly card floor; compresses 0.8mm onto card top
  - Bore=5.8mm press-fit on 6mm rod (0.2mm interference = secure in PETG with CA glue)
  - L=15mm matches EXIT_W=15mm exit slot -- roller sits directly over eject opening
  - PART=0 (single): AgentCAD v227, is_valid=true, 15x8x8mm, face_count=4 ✓
  - PART=1 (print plate 4x): AgentCAD v228, is_valid=true, 18x32x8mm, face_count=16 ✓
  - Both fit Toybox 68x78x88mm with ample margin
  - Exported to design/output/cs2_roller.stl (print plate, 4 rollers)
  - Do not print until N20 motor is sourced and cs2_motor_bracket.py is designed
- Web search finding: commercial card dispensers use 0.4-0.8mm card thickness range
  - 8mm OD gives exactly 0.8mm nip compression on a standard 0.76-0.8mm card
  - This is the correct amount: positive drive friction without excessive card compression
- Autonomous decision: press-fit bore (5.8mm on 6mm rod) rather than set screw or D-flat
  - Wall thickness = (OD-bore)/2 = (8-5.8)/2 = 1.1mm; too thin for any fastener hole
  - Press-fit + CA glue is permanent but reliable; D-flat requires machining a metal shaft
  - Phase 2 roller is a consumable -- press-fit is appropriate at this scale

### What loop built this iteration (v146)
- cs2_height_preview.py v1: three-assembly height comparison scene (100/125/150mm)
  - Shows hopper + wall + platform + phone at each valid bolt-hole height
  - Validates that 174mm wall accommodates all heights (phone top at 116/141/166mm -- all clear)
  - AgentCAD v226: is_valid=true, 377x89.1x174mm, CoM x=0.0 (symmetric), face_count=99 ✓
  - NOT printable -- visualization only; use to choose platform height before printing
- docs/cs2_assembly.md v1: full step-by-step assembly guide
  - Step 0: fit test procedure (peg/bolt + pol_clip press-fit)
  - Step 1-4: hopper → wall → wall-to-hopper bond → platform mount
  - Step 5: iPhone 16 Pro placement (camera 3.9mm protrusion fits 8mm aperture tunnel)
  - Step 6: standard scanning; Step 7: diffuser; Step 8: cross-pol for holo/foil
  - Height table: 104/129/154/169mm cam-to-card at bolt-hole Z 104/129/154/169mm
  - Rebuild commands + verification
- Autonomous decision: added camera protrusion note (3.9mm from web search) to assembly guide
  - iPhone 16 Pro camera bump protrudes 3.9mm from back; platform aperture is 8mm deep
  - Camera module seats in aperture without touching phone glass to platform -- good clearance
  - This was missing from all prior documentation

### What loop built this iteration (v145)
- cs2_diffuser.py v1: white PLA torch diffuser plate (lighting geometry for CS2)
  - 68x75x1.5mm flat plate, sits on platform top between platform and phone
  - 36x30mm aperture at APT_CY=+0.5mm (matches cs2_platform.py aperture exactly)
  - Phone torch hits white PLA surface -> scatters into hopper -> soft diffuse fill light
  - Adds 1.5mm to phone height; negligible (<1.2%) at 125mm camera-to-card distance
  - AgentCAD v224: is_valid=true, 68x75x1.5mm, CoM x=0 (symmetric), face_count=10 ✓
  - Copied to design/output/cs2_diffuser.stl (1.6KB)
  - Use: standard cards (diffuser alone); holo/foil (diffuser + pol_clip + phone_pol)
  - Print notes: WHITE PLA only; brim required (thin flat part, 68mm at bed limit)
- Autonomous decision: chose 1.5mm thickness (7-8 layers) over thicker
  - Thicker diffuser (3mm) would add unnecessary height and wouldn't improve scatter
  - White PLA at 1.5mm reflects/scatters well; transmission is not the mechanism
  - Exact aperture match to platform means stacking is foolproof (one correct orientation)

### What loop built this iteration (v144)
- cs2_fit_test.py v1: fit test print plate (Feature A: peg+bolt holes, Feature B: aperture ring)
  - AgentCAD v222: is_valid=true, 64x38x20mm -- print BEFORE full parts ✓
- cs2_assembly_scene.py v1: full assembly scene (hopper + wall + platform@125mm + phone + card)
  - AgentCAD v223: is_valid=true, 97x89.1x174mm, CoM x=0.0 (symmetric) ✓
  - Validates: aperture at y=-1mm (1mm off card centre -- within 30mm aperture OK)
  - Validates: camera-to-card at PLAT_Z=125mm = 125+8-4 = 129mm (within macro range OK)
  - Validates: wall front face (y=36.1mm) clears hopper and platform back face (y=36mm) by 0.1mm ✓
  - NOT exported as STL -- visualization only; change PLAT_Z to preview other height settings
- README.md: CS2 section added (after CS30 Arch section)
  - Part list table (11 STLs + print settings)
  - Hardware BOM, fit test procedure, assembly sequence, height table
  - Cross-pol instructions for holo/foil cards
  - Rebuild and verify commands

### What loop built this iteration (v143)
- cs2_fit_test.py v1: fit test print plate (print BEFORE full parts to verify critical fits)
  - Feature A (x=-22..-4, 18x16x20mm): hole test block
    - M3 through-bolt hole (3.4mm, X direction, z=8mm) -- test M3 bolt clearance
    - 3mm blind peg hole (3.0mm, 8mm deep from left face, z=14mm) -- test peg fit
    - PASS: bolt free, peg snug with thumb push
    - FAIL/ADJUST: peg tight -> PEG_D in cs2_peg.py +0.05mm steps
  - Feature B (x=-2..+42, 44x38x8mm): platform aperture ring
    - 36x30mm aperture (matches platform aperture exactly)
    - Press cs2_pol_clip plug (35.6x29.6mm) in from below; test 0.2mm clearance press-fit
    - FAIL/ADJUST: too tight -> PLUG_W/PLUG_D in cs2_pol_clip.py +0.1mm; too loose -> -0.1mm
  - AgentCAD v222: is_valid=true, 64x38x20mm, both features in single valid solid ✓
  - Copied to design/output/cs2_fit_test.stl (52KB)

### What loop built this iteration (v142)
- cs2_phone_pol.py v1: phone camera polarizer film frame (lens-side cross-pol component)
  - Completes the cross-pol system: cs2_pol_clip (aperture side) + cs2_phone_pol (lens side)
  - Frame: 44x38mm outer (matches cs2_pol_clip flange footprint), 3mm thick
  - Film recess: 30x24mm pocket (phone-face side, z=0..1.5mm) -- same film cut as cs2_pol_clip
  - Camera bore: 26x20mm through-frame (z=1.5..3mm) -- 2mm annular ledge seats film
  - 4x corner holes (Ø4mm) for rubber band retention; 2.83mm clearance from film pocket corners
  - AgentCAD v221: is_valid=true, 44x38x3mm, CoM x=0/y=0 (symmetric) ✓
  - Copied to design/output/cs2_phone_pol.stl (104KB)
  - Usage: insert 30x24mm film, rubber band over phone corners, align over camera cluster, 90deg from aperture film

### What loop built this iteration (v141)
- cs2_pol_clip.py v1: polarizer film clip for CS2 platform's 36x30mm camera aperture
  - Press-fit plug (35.6x29.6x6mm) + 2mm flange (44x38mm) = 8mm total (matches platform thickness)
  - Film pocket: 30x24x1.5mm at plug top; light bore 26x20mm through to z=6.5mm
  - AgentCAD v220: is_valid=true, 44x38x8mm, face_count=20 ✓
  - Copied to design/output/cs2_pol_clip.stl (3.2KB)
  - Assembly: insert from below platform aperture; film sits in top pocket; cross-pol over phone camera lens

### What loop built this iteration (v140)
- Exported all 7 v2 printable STLs to design/output/ with canonical names (v212-218)
- cs2_peg.py v1: 4× alignment peg print plate (3mm dia × 10mm, 2.95mm for clearance fit)
  - AgentCAD v219: is_valid=true, 9.95×9.95×10mm, face_count=12 (4 separate cylinders) ✓
  - Copied to design/output/cs2_peg.stl (97.7KB)
- Added hardware BOM to HANDOFF: 8 M3×30, 6 M3×20, 14 nuts, 2 dowel pins, CA glue

### What loop built this iteration (v139)
- cs2_hopper.py v2: added 2× alignment peg holes (3mm dia, 5mm long) at seam (x=0)
  - Positions: front wall (y=-34.25mm) and back wall (y=+34.25mm), both at z=17mm
  - Each half gets 2.5mm blind hole; a 3mm×5mm dowel pin bridges both halves
  - Clearance verified: 4.5mm from shaft holes (z=8mm), 4.8mm from join bolts (z=25mm)
  - All 3 PART selectors pass (v209-211): PART=0 97×72×50, PART=1/2 48.5×72×50
- cs2_verify.py: 31/31 PASS (3 new peg clearance checks added)
- Hardware spec clarified: wall-to-hopper is friction fit + PLA glue in Phase 1; flange provides
  enough contact area and wall weight holds it; formal bolt-down is Phase 2

### What loop built this iteration (v138)
- Fixed structural bolt hole mismatch between cs2_platform.py and cs2_wall.py:
  - cs2_platform.py v2: replaced Z-direction bolt holes with Y-direction (x=±22mm, z=4mm from bottom)
  - cs2_wall.py v2: shifted platform hole Z from PLAT_Z to PLAT_Z+PLAT_T/2 (mid-platform alignment)
  - Bolt centres now match exactly: wall=pz+4mm, platform=pz+4mm at each of 4 height positions
- Re-validated all 5 wall selectors (v205-208): all is_valid=true, dims unchanged
- Re-validated platform (v204): is_valid=true, 68x75x8mm
- cs2_verify.py updated: 28/28 checks pass (added 8 bolt alignment checks)

### Design notes (v138)
- cs2_wall.py uses FIXED bolt holes at 4 heights (not T-slots): 104, 129, 154, 169mm (= PLAT_Z + 4)
  - Simpler/stronger for Phase 1; can upgrade to T-slots in Phase 2 if needed
- cs2_platform.py bolt holes are Y-direction at z=PLAT_T/2=4mm from bottom (v2 fix)
  - Assembly: M3x30 bolt through platform back edge (15mm), through wall (14mm), nut on back
  - All 4 hole positions confirmed in top section (z=87..174mm)
- Bolt X position: x=±22mm in both platform and wall (BOLT_X = PLAT_X = 22mm)

### Next steps (Phase 2 / future)
- Print fit test: start with hopper halves + platform (simpler parts)
- Verify card slides in and rests flat at z=4mm
- Verify iPhone 16 Pro sits level on platform with camera over aperture
- Phase 2: motorized feed/eject using existing shaft holes + boss holes

---

# HANDOFF — photo_box loop (superseded by CS2, archived below)
## Active file: `design/cs30_arch.py` v13  |  5 parts, all AgentCAD-valid (ARCHIVED)

## Active file: `design/cs30_arch.py` v13  |  5 parts, all AgentCAD-valid
## photo_box.py v25 -- unchanged, frozen; all 9 PART selectors validated (last: PART=8 AgentCAD v175)
## design/full_system_preview.py -- v3 (AgentCAD v181: is_valid, 128x216.5x164mm, CoM_x=0): all parts + iPhone 16 Pro
## design/photo_box_context.py -- v2 (AgentCAD v180: is_valid, 120x149.6x164mm): optical context view
## design/photo_box_combined_scene.py -- DEPRECATED (rack_stand_v2 era); deprecation header added v135
## design/cs30_fit_test.py -- v2, AgentCAD v163, 68x16x30mm; 4 features (A/B/C/D)
## README.md -- rack_mark upper limit tightened 90->85mm (macro boundary research)
## design/output/cs30_lock_knob.stl -- v12 (AgentCAD v168, socket on correct outer face)
## design/output/cs30_arch_leg_section.stl -- v13 (AgentCAD v169, end cap clearance notches)
## docs/cs30_print_manifest.md -- NEW (v118): full per-part print manifest with slicer notes
## design/output/cs30_arch_carriage.stl -- v10 (AgentCAD v164, slot_d=12.3mm tooth clearance)
## cs30_assembly.md -- v13: leg foot plate end cap clearance noted in Step 5
## design/output/cs30_fit_test.stl -- v2 (AgentCAD v163, 4 features, 68x16x30mm)
## docs/photo_box_assembly.md -- LED channel depth corrected 4mm->6mm (was stale v23 value)

---

## Loop status: SYSTEM COMPLETE + polarizer clip added (v136).
## design/polarizer_clip.py -- NEW v1 (AgentCAD v183: is_valid=true, 44x38x10mm, face_count=20)
## design/output/polarizer_clip.stl -- exported AgentCAD v183
## docs/cs30_print_manifest.md -- polarizer clip + film BOM added (optional anti-glare accessory)
## cs30_arch.py PART=0 assembly -- AgentCAD v182: is_valid=true, 128x158.7x169mm, CoM_x=-0.004mm

### What changed this loop (v136)

**`design/polarizer_clip.py` -- NEW v1: camera aperture polarizer clip**

Design gap identified: CLAUDE.md lists cross-pol dial as a hard design goal ("rotatable cross-pol
dial | Holo specular; fixed polarizer is insufficient") but no polarizer part existed in the system.

New printable accessory for holo/foil card scanning:
- Press-fit plug (35.6x29.6mm, 0.2mm clearance) slides into bridge aperture (36x30mm) from below
- Flange (44x38x2mm) abuts bridge bottom face; stops insertion at correct depth
- Film recess (30x24mm x 1.5mm) at plug top holds polarizing film
- 2mm annular ledge at z=8.5mm supports film over 26x20mm light-path bore
- Light path: 26x20mm bore from z=0 through flange and plug to film recess floor

Cross-pol setup:
  Camera polarizer: 30x24mm film in this clip (camera-side)
  Source polarizer: 10x80mm film strips glued over LED diffuser panels at 90deg (user assembly)
  Effect: kills specular glare on holographic/foil cards; diffuse card detail passes through

AgentCAD v183: is_valid=true, 44x38x10mm, volume=6274mm3, face_count=20, CoM x=0/y=0 (symmetric)
STL exported to design/output/polarizer_clip.stl
ISO render confirmed: flange base visible with raised plug and rectangular film recess opening

docs/cs30_print_manifest.md updated:
  - polarizer_clip.stl row added to part table (1x, 44x38x10mm, ~20 min)
  - Linear polarizing film added to Hardware BOM (optional)
  - Step 8 added to print-and-assemble order (optional, for holo card scanning)

**Autonomous decision:** Press-fit rather than continuously rotatable design.
A two-piece rotating dial would add significant design complexity (inner ring + outer ring +
retention lip + detents). The press-fit achieves the same result: remove clip, rotate 90deg,
reinsert. For cross-polarization, only 0deg and 90deg orientations are needed. The simpler
single-piece design prints without support, has no assembly steps, and is less likely to fail.

### What changed this loop (v135)

**`design/photo_box_combined_scene.py` -- deprecation header added**

Last remaining stale file. It showed rack_stand_v2 + photo_box v22 (stale constants:
PB_WALL_T=6mm vs current 8mm; PB_EC_HALF=44mm vs current 46mm; rack_stand_v2 superseded).
full_system_preview.py v3 covers the same purpose with correct current constants plus iPhone.

Added 5-line deprecation block at top of file redirecting to full_system_preview.py.
Did not delete the file -- no harm in keeping it; the header prevents accidental use.

**cs30_arch.py PART=0 assembly -- AgentCAD v182 final validation**

- is_valid=true, 128x158.7x169mm, volume=448380mm3, face_count=539
- CoM_x=-0.004mm (symmetric), CoM_y=30.8mm, CoM_z=45.3mm (unchanged from v170/v173)
- All 5 cs30_arch parts + ramp + photo_box block in full Compound -- validates cleanly

**Autonomous decision:** Deprecated rather than deleted photo_box_combined_scene.py.
Deletion would be cleaner, but the file contains no wrong geometry (it just has stale
constants and references superseded parts); a deprecation header costs nothing and avoids
any confusion if someone opens it directly from the filesystem.

### What changed this loop (v134)

**`design/full_system_preview.py` -- v3: iPhone 16 Pro body added + BRIDGE_HW corrected**

Two changes from v2:
1. BRIDGE_HW corrected: 58mm -> 60mm (AgentCAD v176 confirmed actual bridge half = 60mm;
   v2 used 58mm which was wrong by 2mm/side). Bridge block now 120mm wide (was 116mm).
   Note: bounding box x unchanged at 128mm -- carriages (x=+/-64mm) are still wider.

2. iPhone 16 Pro body added: 71.5x149.6x8.25mm box, face-down on bridge top (z=135mm),
   camera centred over bridge aperture at (x=0, y=39mm).
   Phone extends y=-35.8..+113.8mm (149.6mm total, centred at y=39mm).

AgentCAD v181: is_valid=true, 128x216.5x164mm (y grew 193.7->216.5mm from phone), CoM_x=0

Key verifications from v3 scene geometry:
- Phone (71.5mm) inside bridge (120mm): 24.25mm margin each side to leg inner faces (x=42mm)
- Phone far edge (y=113.8mm) extends 22.8mm past photo_box far end cap (y=91mm) -- expected
- Phone near edge (y=-35.8mm) clears card_tray far face (y=-75.7mm) by 39.9mm -- no conflict
- Bridge (z=125mm) clears photo_box top (z=44mm) by 81mm -- ample clearance at rack_mark=70mm

**Autonomous decision:** Kept phone centred at y=BRIDGE_D/2=39mm, not at card centre y=44mm.
The 5mm offset means the phone camera (near y=39mm hole) is 5mm from card centre, acceptable
given camera FOV covers 88mm card. Centering phone on y=44mm (card centre) would misalign
camera with the 39mm aperture -- the aperture position governs, not the card centre.

### What changed this loop (v133)

### What changed this loop (v133)

**`design/photo_box_context.py` -- rewritten v2 (was stale v21 constants, gooseneck phone at 263mm)**

Old file showed phone at PHONE_Z=263mm (gooseneck era, before cs30_arch). Running it produced
a scene with wrong camera height and wrong photo_box dimensions (v21). Replaced with cs30_arch
context visualization.

New file shows:
- photo_box (single bounding block 92x94x44mm, near face at y=0)
- Card (63x88x0.8mm at z=4mm)
- Leg columns (14x10x164mm at x=+/-49mm, both sides)
- Bridge (120x78x10mm at z=125mm, confirmed bridge half=60mm from AgentCAD v176)
- Camera aperture marker (r=3mm cylinder at x=0, y=39mm, z=124-135mm)
- iPhone 16 Pro body (71.5x149.6x8.25mm, face-down on bridge top at z=135mm)

AgentCAD v180: is_valid=true, 120x149.6x164mm, CoM_x=0 (symmetric), CoM_y=39.6mm (at camera centre)

Key verifications shown in scene:
- Phone (71.5mm wide) fits inside bridge span (120mm): 24.25mm clearance each side to leg inner face (42mm)
- Phone extends y=-35.8..+113.8mm; photo_box near cap at y=-3mm, far cap at y=91mm
  Phone overhangs far end by 22.8mm, near end by 32.8mm -- expected for 149.6mm phone on 78mm bridge
- Bridge bottom (z=125mm) to card (z=4mm) = 121mm camera-to-card (macro OK)

**Autonomous decision:** Used PHONE_L=149.6mm (actual iPhone 16 Pro spec) not PHONE_D=156.9mm
in cs30_arch.py. The 156.9mm value in the design file is ~7mm longer than spec; likely a
measurement error with a case on. Visualization uses the correct bare-phone spec.

### What changed this loop (v132)
## photo_box.py PART=6 (pb_fit_test) — AgentCAD v179: is_valid=true, 44x25x4mm, 39 faces (assembly doc correct)
## docs/photo_box_assembly.md Step 7 — stale "74-139mm (rack 30-90mm)" corrected to "81-136mm (rack 30-85mm)"

### What changed this loop (v132)

**photo_box.py PART=6 (pb_fit_test) -- validated AgentCAD v179**

- is_valid=true, 44x25x4mm, volume=3291mm3, face_count=39
- Confirms photo_box_assembly.md Step 0 "Each fit_test piece is 44x25x4mm" -- exact match

**docs/photo_box_assembly.md -- Step 7 Option A cam range corrected**

Step 7 Option A described cs30_arch as operating at "74-139mm (rack marks 30-90mm)".
Both numbers were from the old buggy height formula (bridge_z - 6mm, not bridge_z - 4mm)
and the old rack_mark=30mm typo (74mm instead of 81mm) fixed in v130 README.

Correct values: 81-136mm cam-to-card at rack marks 30-85mm.

The inconsistency: README was fixed in v130 but photo_box_assembly.md was not updated
at the same time, leaving docs with contradictory cam-to-card values.

**Autonomous decision:** Scanned all 284 lines of photo_box_assembly.md for stale values.
No other inconsistencies found. The LED channel "top 10mm" vs LED_W=10.4mm mismatch
(wall_half Step 1 description says "top 10mm" for the channel zone) is a natural-language
rounding in a description, not a dimensional error -- the LED channel HEIGHT (z-span) happens
to be exactly 10.4mm matching LED_W, and the description is correct about the approximate
location at the top 10mm of the 44mm wall.

### What changed this loop (v131)
## design/cs30_arch.py PART=2 (leg_section) — AgentCAD v178: is_valid=true, 14x24x87mm, 100 faces
## README.md — "System verification" section added: py design/cs30_verify.py documented with 6-category description
## [COMPLETE] all 5 cs30_arch PART selectors now at AgentCAD v177-178 in this session

### What changed this loop (v131)

**cs30_arch.py PART=2 (leg_section) -- revalidated AgentCAD v178**

- is_valid=true, 14x24x87mm (prints 87mm tall, 1mm within 88mm Toybox Z), volume=7537mm3
- face_count=100 (expected: body + 82/5=16 rack teeth per side + peg + notch geometry)
- CoM_x=0 (symmetric), CoM_z=38.79mm (near geometric centre of 87mm column, correct)
- Matches print manifest "14x24x87mm" -- confirmed

All 5 cs30_arch printable PART selectors now fresh in this session:
  PART=1 ramp:         v177  68x70.74x32.57mm  23 faces
  PART=2 leg_section:  v178  14x24x87mm        100 faces
  PART=3 bridge_half:  v176  60x78x10mm         26 faces
  PART=4 carriage:     v164  30x16x55mm         (prior loop)
  PART=5 lock_knob:    v168  19.2x20x8mm        (prior loop)

**README.md -- "System verification" section added**

cs30_verify.py was created in v128 but never referenced in README; users reading the
documentation had no way to know the script existed. Added "System verification" subsection
in the CS30 Arch section between "Rebuild STLs" and the next section separator.
Documents the run command, 6 check categories, exit code behaviour, and speed.

**Autonomous decision:** Added the verify section within the CS30 Arch v13 block (not a
top-level section) because it is specific to cs30_arch + photo_box v25 constants.
A top-level verification section would imply it covers the entire project (including
rack_stand_v2 superseded design).

### What changed this loop (v130)
## design/cs30_arch.py PART=1 (ramp) — AgentCAD v177: is_valid=true, 68x70.74x32.57mm, 23 faces
## README.md height table — 3 bugs fixed: formula (-6->-4mm), row-1 typo (74->81mm), removed impossible rack_mark=120mm row
## design/cs30_arch.py PART=3 (bridge_half) — AgentCAD v176: is_valid=true, 60x78x10mm, 26 faces
## docs/cs30_print_manifest.md — fit test feature D bolt spec corrected: M3x25mm -> M3x30mm
## design/cs30_verify.py — 19 system checks, pure Python, all PASS (py design/cs30_verify.py)
## design/full_system_preview.py — v2 (AgentCAD v174, 128x193.7x164mm, is_valid)
## photo_box.py PART=8 (card_tray) — AgentCAD v175: is_valid=true, 68x27x37mm, volume=17292mm3

### What changed this loop (v130)

**cs30_arch.py PART=1 (ramp) -- revalidated AgentCAD v177**

- is_valid=true, 68x70.74x32.57mm, volume=15214mm3, face_count=23, CoM_x=0 (symmetric)
- Y span -9.66..61.08mm: C-clip foot extends 9.66mm behind y=0 (into end cap region)
- Matches print manifest "68x70.7x32.6mm" within float rounding -- manifest is accurate
- full_system_preview.py RAMP_D=70.7mm matches actual 70.74mm -- confirmed

**README.md height adjustment table -- 3 bugs fixed**

Bug 1: Formula note said "bridge height - 6mm" but FLOOR_T=4mm, so correct formula is bridge_z - 4mm.
  All cam-to-card values were 2mm too low in every row.

Bug 2: rack_mark=30mm row showed cam-to-card=74mm. Correct: 30+50+5-4=81mm. Typo was -7mm off.

Bug 3: rack_mark=120mm row was physically impossible: carriage_top = 120+50 = 170mm >
  LEG_COL_H = 164mm (column height). Removed this row.

Corrected table adds rack_mark=70mm (recommended) and rack_mark=85mm (safe limit).
Formula note rewritten with explicit constants: bridge_z = rack_mark + 55mm, cam = bridge_z - 4mm.
Maximum physical rack_mark clarified as 114mm (column 164 - carriage 50).

**Autonomous decision:** All cam-to-card values in README were systematically wrong by 2mm due
to wrong formula. Fixed all rows rather than just patching the note, since users read the table
more than the formula note.

### What changed this loop (v129)

**cs30_arch.py PART=3 (bridge_half) — validated via AgentCAD v176**

- is_valid=true, dimensions 60x78x10mm, volume=23823mm3, face_count=26
- Confirms print manifest "60x78x10mm" is exact
- Confirms cs30_verify.py BRIDGE_T=10mm (aperture tunnel depth for vignetting check) is correct
- Full_system_preview.py uses BRIDGE_HW=58 (simple 116mm block) vs actual half=60mm.
  This is a 2mm/side simplification in the visualization only -- clearances are not affected
  (overall x bounding box is set by carriages at x=+/-64mm, not the bridge)

**docs/cs30_print_manifest.md -- fit test feature D bolt spec corrected**

Fit test procedure (feature D) said "Thread M3x25mm bolt" but hardware BOM says M3x30mm
with note "25mm falls 2mm short." A user following the fit test with a 25mm bolt
would buy the wrong hardware. Fixed to "M3x30mm (the assembly bolt)."

**Autonomous decision:** Did not update full_system_preview.py for 2mm bridge width correction.
The visualization shows a 116mm-wide bridge vs 120mm actual, but the overall scene bounding
box (128mm) is set by carriages, not the bridge. Re-running AgentCAD for a cosmetic fix
adds no design value.

### What changed this loop (v128)

**`design/cs30_verify.py` -- new system-level constraint verification script**

Pure Python (math + sys only), no build123d or AgentCAD required.
Run: `py design/cs30_verify.py`

19 checks across 6 categories -- all PASS:
  1. Camera-to-card distance: safe range rack 0..85mm (90mm span); 70mm = 121mm cam-to-card
  2. Geometric clearances: leg flush with wall (0mm gap); ramp 8mm clear of legs; aperture 24mm clear
  3. Optical vignetting: aperture Y=56.3deg >> card FoV=20.0deg; X=60.9deg >> 14.6deg; 36deg margin
  4. LED channel: 6mm channel vs 2.8mm stack (strip+diffuser); 3.2mm air gap for light mixing
  5. Foot plate notch: 4mm X notch = end cap foot overhang; 3mm Y notch = EC_T exactly
  6. Bridge Y alignment: aperture at y=39mm, card centre at y=44mm, 5mm offset OK

Script exits 0 on pass, 1 on failure -- CI-friendly. Can be run at any time to catch
regressions if constants in photo_box.py or cs30_arch.py are changed.

**Autonomous decision:** Two section-6 checks initially failed with wrong requirement
(testing BRIDGE_D >= CARD_L, which is not a design requirement). The bridge positions
the camera at y=39mm and does not need to physically span the full 88mm card length.
Fixed checks to test the actual requirements: bridge spans past card midpoint, and camera
aperture Y falls within bridge span. Both correct and passing.

### What changed this loop (v127)

**photo_box.py PART=8 (card_tray) — last unvalidated part confirmed**

AgentCAD v175 run on PART=8 selector:
- is_valid=true, dimensions 68x27x37mm, volume=17292mm3
- face_count=10 (correct for U-tray with internal Wedge ramp)
- center_of_mass: x=0.0 (symmetric), y=9.28, z=10.84
- Wedge(TRAY_W=64, TRAY_D=25, TRAY_RAMP_H=6.7, xmin=0, zmin=0, xmax=64, zmax=0)
  produces valid geometry inside BuildPart context

All 9 photo_box.py PART selectors (0-8) now explicitly AgentCAD-validated this session.

**HANDOFF header corrected**
- Line 5 had stale v1 data for full_system_preview.py (AgentCAD v172, 128x97.85x164mm)
- Corrected to v2 (AgentCAD v174, 128x193.7x164mm)
- photo_box.py line updated to note all 9 selectors validated

**Autonomous decision:** No new geometry this loop. All parts validated; next meaningful
work would require physical fit testing (user task). Loop entering long-period heartbeat.

### What changed this loop (v126)

**`design/full_system_preview.py` updated to v2 — ramp + card_tray added**

Added cs30_ramp (68x70.7x32.6mm box at y=-70.7..0mm) and card_tray
(68x27x37mm box at y=-102.7..-75.7mm) to complete the full workflow scene.

**AgentCAD v174: is_valid=true, 128x193.7x164mm**
- Y span: -102.7mm (tray near face) to +91mm (photo_box far end cap) = 193.7mm total
- Ramp-to-leg clearance: ramp at x=+/-34mm, legs at x=+/-42mm -> 8mm gap OK
- All components non-overlapping, CoM x=0 (symmetric) OK

**Camera aperture analysis (web search + analytic)**
- iPhone 16 Pro ultra-wide camera module: minimum focus 20mm, raised ~3.9mm
- Bridge aperture (CAM_W=36mm, CAM_D=30mm, BRIDGE_T=10mm depth):
  - Y half-angle: arctan(15/10) = 56 degrees unobstructed
  - Card Y FoV needed at 121mm: arctan(44/121)*2 = 40 degrees
  - 56 > 40: no vignetting for card scanning -- aperture is adequate OK
- No geometry change required

**Autonomous decision:** Ramp shown as full-height box (32.6mm), not tapered wedge.
The exact ramp slope (20 degrees in cs30_ramp.stl) doesn't affect interface validation;
what matters is the bounding box clearance to legs and photo_box, which is validated.

## LOOP STATUS: COMPLETE. All printable geometry and documentation finished.

User next steps:
1. Print fit tests first: pb_fit_test.stl (x2) + cs30_fit_test.stl (x1)
2. If pass: full prints per docs/photo_box_assembly.md + docs/cs30_print_manifest.md
3. Assembly: docs/photo_box_assembly.md -> docs/cs30_assembly.md (v13)
4. Rack mark 30-85mm for ultra-wide macro; 70mm recommended

Full workflow (assembled):
  card_tray -> cs30_ramp -> photo_box platen (kinematic registration) -> scan -> remove

### What changed this loop (v125)

**`docs/cs30_assembly.md` — three documentation bugs fixed**

**Bug 1: Header still said "CS30 Arch v12"**
- Fixed to "CS30 Arch v13"

**Bug 2: Step 7 referenced a removed join peg**
- Old: "Halves meet at the centreline; join peg links them."
- Join peg was removed in v12 (it self-conflicted after YZ mirror fix)
- Fixed: "The two halves meet at the centreline (x=0) with no fastener -- the 4 peg connections (2 per half) hold them in alignment."
- Also clarified inner/outer peg world-X positions (+/-41mm, +/-57mm)

**Bug 3: BOM table header had 4 columns but rows had 5**
- Missing "Print notes" column in header -- Markdown would render broken table
- Fixed: added "Print notes" column; also corrected bridge_half height "9mm"->"10mm"
  (BRIDGE_T=10mm in cs30_arch.py v13)

**Final AgentCAD validation: cs30_arch.py PART=0 v173**
- is_valid=true, 128x158.74x169mm (unchanged from v170)
- CoM x=-0.004mm (symmetric OK), y=30.8mm, z=45.3mm (low CoM -- legs are ballast)

**Autonomous decision:** Fixed bridge_half print height from "9mm tall" to "10mm tall".
BRIDGE_T=10mm in cs30_arch.py; 9mm was stale (pre-v12 value when BRIDGE_T was 4mm body+5mm
peg). The 10mm is the flat plate thickness; pegs add 5mm for a total slot depth of 15mm on
the carriage, but the printable part height is 10mm.

## LOOP STATUS: COMPLETE

All geometry and documentation verified. No further work needed.

User next steps (unchanged):
1. Print photo_box first -- docs/photo_box_assembly.md Step 0 (fit tests)
2. Print cs30_arch -- docs/cs30_print_manifest.md (print cs30_fit_test.stl first)
3. Assemble per docs/cs30_assembly.md (now v13, join-peg reference removed)
4. Rack mark 30-85mm for reliable ultra-wide macro; 70mm recommended

### What changed this loop (v124)

**`design/full_system_preview.py` — NEW — combined system scene v1**

**Purpose:** Visual validation of photo_box + cs30_arch interface — not a printable part.
Shows: photo_box (simplified solid blocks), card at z=4mm, two leg stacks, two carriages
at RACK_MARK=70mm, bridge at BRIDGE_Z=125mm, camera marker disc at y=39mm.

**AgentCAD v172: is_valid=true, 128x97.85x164mm**
- x: +/-64mm (carriage outer edge) -- symmetric, CoM x=0 OK
- y: -6.85..+91mm (leg foot near edge to photo_box far end cap)
- z: 0..164mm (table to leg stack top)

**Interface clearances validated geometrically:**
- Leg at x=+/-49mm vs end cap at x=+/-46mm: 3mm clearance per side OK
- Leg foot y_min=-6.85mm vs back end cap y=-3..0mm: clearance notches (v13) cover this OK
- Bridge (y=0..78mm, z=125..135mm) vs photo_box top (z=44mm): 81mm vertical clearance OK
- Camera at z=125mm, card at z=4mm: 121mm camera-to-card -- within 20-140mm macro OK

**Web search finding: iPhone 16 Pro ultra-wide minimum focus = 20mm**
- Source: macro focus range = 20mm minimum, ~140mm maximum
- cs30_arch at rack_mark=85mm: camera-to-card = 85+51 = 136mm -- safely in macro
- cs30_arch at rack_mark=90mm: camera-to-card = 90+51 = 141mm -- borderline, iOS may switch
- README.md updated: recommended range 30-90mm -> 30-85mm

**`docs/photo_box_assembly.md` -- documentation bug fixed**
- Step 6: "10.4mm wide x 4mm deep" -- stale v23 value
- Corrected to: "10.4mm wide x 6mm deep" (LED_D=6mm since v24)
- Air gap description corrected: 1.2mm -> 3.2mm (strip 2mm + diffuser 0.8mm = 2.8mm used, 3.2mm air gap)

**Autonomous decision:** Bridge placed at y=0..78mm (starting at photo_box near face), not
centred at y=LEG_CY=5.15mm. Camera hole at y=39mm lands 5mm off card centre (y=44mm) --
within the 30mm camera aperture width. This matches cs30_arch assembly code convention
(bridge_half.translate((0,0,bridge_z)) -- no Y offset).

## LOOP STATUS: COMPLETE

All geometry validated. No further autonomous design work required.

User next steps:
1. Print photo_box first -- see docs/photo_box_assembly.md Step 0 (fit tests)
2. Then print cs30_arch -- see docs/cs30_print_manifest.md, print cs30_fit_test.stl first
3. Assemble photo_box -- docs/photo_box_assembly.md Steps 1-6 + 8
4. Assemble cs30_arch -- docs/cs30_assembly.md Steps 1-8
5. Rack mark 30-85mm for ultra-wide macro; 70mm recommended starting point

If fit tests fail: adjust constant in appropriate .py, re-export STL, reprint fit_test only.

### What changed this loop (v123)

**Documentation-only loop — no geometry changes**

**Version string cleanup:**
- `design/cs30_fit_test.py` header: "cs30_arch v9" → "v13"; constants comment: "v10" → "v13"
- `docs/cs30_print_manifest.md` header: "CS30 Arch v10" → "CS30 Arch v13"
- `HANDOFF.md` README header: updated to reflect v13 README state

**`docs/photo_box_assembly.md` Step 7 — cs30_arch added as recommended Option A**
- Previously: Step 7 only listed flex arm / gooseneck mounts and said "rack_stand_v2 NOT compatible"
- Missing: no mention of cs30_arch, which is the purpose-built integrated arch for this photo_box
- Fix: restructured Step 7 into Option A (cs30_arch, recommended: ultra-wide macro at 74–139mm, no desk clamp needed) and Option B (flex arm fallback: main camera at 263mm)
- Centring aid / alignment groove instructions moved under Option B (gooseneck needs centering; cs30_arch bridge is self-centred at x=0)

**Final STL audit (all present in design/output/):**
- cs30: ramp, arch_leg_section, phone_bridge_half, fit_test, arch_carriage, lock_knob (6 files)
- pb: card_tray, endcap_half, fit_test, led_channel_test, led_diffuser, platen_back, platen_front, wall_half (8 files)
- Total: 14 STLs ✓

**Autonomous decision**: Added cs30_arch as Option A in photo_box_assembly.md rather than creating a separate combined-scene document. The user's assembly guide is the right place for this cross-reference; a separate combined scene (photo_box_combined_scene.py) would be redundant with the PART=0 assembly preview already in cs30_arch.py.

## LOOP STATUS: COMPLETE

**All geometry is done. No further design loops needed.**

User next steps:
1. **Print photo_box first** — see `docs/photo_box_assembly.md` Step 0 (fit tests)
2. **Then print cs30_arch** — see `docs/cs30_print_manifest.md`, print `cs30_fit_test.stl` first
3. **Assemble photo_box** — `docs/photo_box_assembly.md` Steps 1–6 + 8
4. **Assemble cs30_arch** — `docs/cs30_assembly.md` Steps 1–8
5. **Scan** — cs30_arch Option A (ultra-wide macro 74–139mm) or flex arm Option B (263mm)

If fit tests fail → adjust the relevant constant in the appropriate .py file, re-export STL, reprint.

### What changed this loop (v122)

**`design/cs30_arch.py` → v13 — leg foot plate end cap clearance notches**

**Interface conflict found: photo_box end cap extends 4mm past wall outer face**
- `EC_W = PLATEN_W/2 + WALL_T + FOOT_W = 34+8+4 = 46mm per half` in photo_box.py
- cs30_arch leg inner x-face at x=±42mm (wall outer face) — but end cap extends to x=±46mm
- Leg foot plate (y=-12..+12mm, z=0..3mm) collides with end cap body at x=42..46mm, y=-3..0mm zone (4mm × 3mm × 3mm conflict per side)

**Fix: 4mm × 3mm notches at both inner-X × near-Y corners of foot plate**
- `EC_FOOT_W=4.0`, `FOOT_PLATE_H=3.0` constants added inside function
- Subtracts `Box(4, 3, 3)` centered at `(±5mm, -1.5mm, 1.5mm)` from foot plate
- Clears the end cap extension at both x=±42..±46mm, y=-3..0mm zones
- Bounding box UNCHANGED: 14×24×87mm ✓ (notches are inside the envelope)
- Both x corners notched symmetrically so part works on either left or right leg

**AgentCAD v169: PART=2 leg_section, is_valid=true, 14×24×87mm ✓**
- face_count=100 (was ~80 before notches); volume=7536mm³
- AgentCAD v170: PART=0 assembly, is_valid=true, 128×158.7×169mm ✓ (unchanged)

**Documentation updates:**
- README.md: section header v11→v12, hardware/clearance headers updated, lock knob description corrected ("top-face socket" not "bottom-face socket")
- docs/cs30_assembly.md: header v11→v12, lock knob instruction corrected, Step 5 end cap clearance note added
- docs/cs30_print_manifest.md: lock_knob orientation note already correct ("Flat (bottom face down)" is print orientation, not socket location)

**Autonomous decision**: Used symmetric notches (both ±x corners) rather than asymmetric (inner corner only). The same leg section part is used on left and right legs without mirroring in the assembly, so the inner-x face differs by side. Symmetric notches ensure the correct corner is notched regardless of which side the leg is placed on.

### What changed this loop (v121)

**`design/cs30_arch.py` → v12 — lock knob socket face corrected**

**Bug: Socket placed on inner face (z=0) instead of outer face (z=8mm)**
- v11 had `Locations((0,0,0))` + `Align.MIN` → socket opens at z=0 (inner face, presses against carriage)
- The bolt head is at the -X exterior of the carriage. The knob slides onto it outer face (z=8mm) first.
- A socket on z=0 would require the bolt head to pass through the full 8mm knob to reach it — mechanically impossible.
- The indicator groove on z=8mm (outer face) confirmed user-visible face is z=8mm, but socket was on opposite face.

**Fix: `Locations((0,0,0)) + Align.MIN` → `Locations((0,0,KNOB_H)) + Align.MAX`**
- Socket now opens at z=8mm (outer face, user-visible); cuts inward to z=4.7mm
- Assembly: bolt head at -X carriage exterior; knob outer face (z=8mm) approaches bolt head; head seats in 6.1mm×3.3mm socket ✓
- Inner face (z=0) presses flat against carriage -X wall; no socket protrusion to interfere ✓
- Both socket and indicator groove now on same face (z=8mm outer) — consistent ✓

**AgentCAD v168: PART=5 lock_knob, is_valid=true, 19.17×20×8mm ✓**
- face_count=21, is_valid=true; dims unchanged (socket placement only, not size)
- Iso render confirmed: large counterbore visible on top face (z=8mm); bottom face flat ✓

**Autonomous decision**: The v11 socket placement was geometrically valid (builds without error) but mechanically wrong. The rendered iso view was the diagnostic: top face shows the 6.1mm counterbore with 3.4mm bore inside it; bottom face is flat. Assembly orientation unambiguous — outer face always faces user during operation.

**Autonomous decision**: Used SOCK_CL=0.3mm (0.3mm/side) for bolt head socket clearance, matching CARR_CL. Standard FDM slide fit; user presses knob onto bolt head, friction holds during use.

## Next loop priorities

### All 5 cs30_arch parts are now print-ready (v11)

The loop prompt's priority list (photo_box.py) is satisfied — photo_box.py is frozen at v25.
The lock knob was the last functional geometry bug. No further geometry issues remain.

**If loop is re-invoked**: consider checking if cs30_fit_test.py feature (D) bolt note should be updated from M3×25mm to M3×30mm (currently says "Thread M3×25mm bolt through 3.4mm hole" — the fit_test stub is only 9mm wide, so 25mm works for the test, but the note should say "M3×30mm" so users buy the right bolt before testing).

### What changed this loop (v117)

**`design/cs30_arch.py` → v10 — carriage slot depth bug fixed (rack teeth collision)**

**Bug: slot_d too shallow — rack teeth collide with carriage back wall**
- Old `slot_d = LEG_D + CARR_CL = 10.3mm`
- After CARR_Y_OFF=-5.15: slot back at world y=5.15mm
- Rack teeth extend from leg +Y face (world y=5mm) to y=7mm (tooth tip)
- Teeth at y=5.15..7mm would be INSIDE the back wall material — carriage cannot slide onto leg

**Fix: extend slot_d to clear tooth height**
- New `slot_d = LEG_D + RACK_TOOTH_H + CARR_CL = 10+2+0.3 = 12.3mm`
- After CARR_Y_OFF: slot back now at world y=7.15mm → 0.15mm clearance beyond tooth tips ✓
- Added `leg_ctr_y = (LEG_D + CARR_CL)/2 = 5.15mm` — named constant so bolt/nut/peg Y positions
  remain at 5.15mm (world y=0) regardless of slot_d; prevents accidental drift if slot_d changes again
- Volume delta: -1460mm³ = slot_w × RACK_TOOTH_H × CARR_H = 14.6 × 2 × 50 ✓

**AgentCAD v164: PART=4 carriage, is_valid=true, 30×16×55mm ✓**
**AgentCAD v165: PART=0 assembly, is_valid=true, 128×159×169mm ✓**

**cs30_fit_test.py (A) comment updated**: slot dims now 14.6×12.3mm (was 14.6×10.3mm)

**Autonomous decision**: kept CARR_D=16mm (back wall 3.7mm). Back wall transmits only
  compressive bolt load in X — not shear. At 3.7mm FDM PLA, σ ≈ 200N/(3.7×50mm²) = 1.1 MPa 
  vs PLA yield ~50 MPa. More than adequate; no need to increase CARR_D.

---

### What changed last loop (v116)

**`design/cs30_arch.py` → v9 — nut trap FDM clearance added**
- v8 had 5.5×5.5mm pocket for 5.5mm AF M3 hex nut — zero clearance, won't drop in on FDM
- Added `NUT_AF=5.5`, `NUT_TRAP_CL=0.2`, `NUT_TRAP_D=3.0` constants to carriage parameter block
- Pocket now `nt = NUT_AF + NUT_TRAP_CL = 5.7mm` → `Box(3.0, 5.7, 5.7, Align.MAX)` ✓
- AgentCAD v162: is_valid=true, 30×16×55mm; volume decreased 6.72mm³ (= 5.7²×3 − 5.5²×3) ✓

**`design/cs30_fit_test.py` → v2 — feature (D) nut trap stub added**
- Replaced "(D) NOT ADDED" note with actual 9mm-wide stub at x=30..39mm
- Total width: -29 to +39 = 68mm (exactly at Toybox usable bed limit; 1mm physical margin) ✓
- Body: Box(9, 8, 12); bolt hole: Box(11, 3.4, 3.4) through width; nut pocket: Box(3, 5.7, 5.7) Align.MAX on +X
- Test: thread M3 bolt → drop M3 hex nut; validates carriage nut trap before full print
- AgentCAD v163: is_valid=true, **68×16×30mm** ✓ (was 56×16×30mm)

**Fail/adjust table added to README for feature (D)**

**Autonomous decision**: expanded nut trap from 5.5mm (zero clearance) to 5.7mm (0.2mm total = 0.1mm/side). Standard FDM hex nut trap targets 5.6–5.8mm for M3; chose 5.7mm (midpoint) to balance drop-in ease vs nut rattle.

---

### What changed last loop (v115)

**`design/cs30_arch.py` → v8 — carriage nut trap alignment bug fixed**

**Bug: nut trap box was entirely outside the carriage solid**
- `Align.MIN` at `(CARR_W/2, slot_d/2, CARR_H/2)` = `(15, 5.15, 25)` with `Box(3.0, ...)`
- `Align.MIN` places the minimum X face at x=15; box spans x=15→18 — outside carriage (x=−15..+15)
- SUBTRACT of a box outside the solid = no-op; nut has no pocket to seat in
- Confirmed by v161 vs old v152: face_count increased 29 faces, CoM shifted to x=−0.046mm (pocket cuts +X only) ✓

**Fix: `Align.MIN` → `Align.MAX`**
- `Align.MAX` places the MAX X face at x=15 (outer face); box spans x=12→15
- Creates 3mm deep × 5.5mm × 5.5mm square pocket opening on +X face ✓
- M3 hex nut (5.5mm AF) seats flush; bolt threads in from −X through full width ✓

**AgentCAD v161: PART=4 carriage, is_valid=true, 30×16×55mm ✓**

**Slicer note added (Priority 2)**
- README + cs30_assembly.md: leg section orientation now says "foot plate down" explicitly
- 24mm Y foot plate is the bed face in the slicer (wider than 14mm body)

---

### What changed last loop (v114)

**Documentation pass — all three v113 priorities resolved**

**Priority 1 — README updated to v7**
- Section header: "CS30 Arch v5" → "CS30 Arch v7"
- Leg section bed dims: `14×12×87mm` → `14×24×87mm`
- Leg notes: added "24mm wide foot plate stands on table, inner face abuts photo_box wall; **no brim**"
- Assembly step 5: removed C-clip language; now describes foot plate abutting wall for lateral location
- `docs/cs30_assembly.md` also updated: header v5→v7, BOM note, step 5 revised

**Priority 2 — Leg section + bridge half STLs re-exported**
- Leg section: AgentCAD v159, is_valid=true, **14×24×87mm** ✓
- `design/output/cs30_arch_leg_section.stl` replaced (was old v150, 14×12×87mm)
- Bridge half: AgentCAD v160, is_valid=true, **60×78×10mm** ✓ (audit table showed stale v151 63×78×9mm)
- `design/output/cs30_phone_bridge_half.stl` replaced

**Priority 3 — cs30_fit_test.py header updated**
- (A) now clearly states: REQUIRES separately printed cs30_arch_carriage
- (D) mini carriage cross-section: documented as NOT added — 30mm carriage width + 56mm body = ~90mm total > 68mm bed limit

---

### What changed last loop (v113)

**`design/cs30_arch.py` → v7 — leg clip removed, foot plate added**

**Leg C-clip was geometrically broken:**
- `Align.MIN` in +Y caused clip to extend INTO the leg body, not outward
- The "slot" actually punched through the leg body at y=-3..+5.3mm — useless as a clip
- AgentCAD showed y=[−5,+7]=12mm total (clip geometry invisible; fins merged with body)

**Fix: replaced broken clip with wide foot plate**
- `Box(LEG_W, 24.0, 3.0)` centered at leg base (z=0..3mm, y=-12..+12mm)
- Leg inner face at local x=−7mm = absolute x=±42mm = photo_box wall outer face ✓
- Leg stands on table (z=0); foot inner edge abuts photo_box wall for lateral location
- PART=2: v157, is_valid=true, **14×24×87mm** ✓ (was 14×12×87mm)

**Assembly (PART=0) updated to v7b:**
- LEG_Z=0 (legs on table, not z=34mm clip-seating)
- Simplified photo_box block (84×88×44mm) added to Compound
- Ramp translated by −RAMP_DY to sit against photo_box near face (y=0)
- Bridge at z=145mm (CARRIAGE_Z=90mm example); leg stack top at z=169mm
- PART=0: v158, is_valid=true, **128×159×169mm** ✓
- Camera-to-card at max CARRIAGE_Z (114mm): bridge=169mm, card=6mm → **163mm** (macro range)

**Height note: camera-to-card at max setting ≈ 163mm (16.3cm)**
- iPhone 16 Pro ultra-wide macro works at <14cm; dead zone 14-26cm; reliable main cam ≥26cm
- cs30_arch is a COMPACT DESIGN targeting close-range macro scanning, same as cs30 inspiration
- Apps using manual focus or macro mode (Apple Camera, Magnifier, Delver Lens) compatible
- Users wanting main-camera distance need rack_stand_v2 (superseded) or 3-section leg variant

---

### What changed last loop (v112)

**`design/cs30_arch.py` → v6 — three assembly geometry bugs fixed**

**Bug 1: Bridge socket was through-hole (not blind)**
- BRIDGE_T was 4mm, socket depth = SEC_PEG_H = 5mm → punched through plate
- Fix: BRIDGE_T 4→6mm; socket is now blind (5mm depth, 1mm floor) ✓

**Bug 2: Bridge assembly used wrong mirror plane**
- `mirror(Plane.XZ)` flips Y only → both halves landed at x=[0,58]
- Fix: `mirror(Plane.YZ)` negates X → left half at x=[-60,0] ✓
- Assembly x=[-64,64]=128mm symmetric, confirmed by PART=0 bbox ✓

**Bug 3: Carriage Y offset missing — slot didn't centre on leg**
- Carriage slot Align.MIN at y=0, leg centred at y=0 → slot captured only back half of leg
- Fix: `CARR_Y_OFF = -(LEG_D + CARR_CL)/2 = -5.15mm` applied to both carriages
- Carriage peg world-Y: -5.15 + slot_d/2 = 0 → aligns with bridge socket at y=0 ✓

**Removed join peg from bridge half** (would self-conflict after YZ mirror)
- Two halves butt join at x=0; held by 4 carriage sockets (2 per side)

**AgentCAD results:**
- PART=3 bridge_half: v154, is_valid=true, **60×78×10mm** (was 63×78×9mm)
- PART=0 assembly: v155, is_valid=true, **128×99×169mm** ✓

---

### What changed last loop (v111)

**`design/cs30_fit_test.py` — AgentCAD v148, is_valid=true, 56×16×30mm ✓**
- Three-feature clearance validator: leg stub (A), peg base (B), end cap stub (C)
- Bed footprint 56×16mm — well within 68×78mm Toybox usable area
- No supports; ~15 min print time; ready to slice and print

**`README.md` — cs30_arch v5 section added**
- Full part list table (5 parts + fit_test)
- Fit test procedure table (A/B/C features → pass/fail/adjust)
- 8-step quick assembly sequence; height reference table
- Clearance reference; rebuild instructions
- rack_stand_v2 section header marked "(superseded by CS30 Arch v5)"

---

### What changed last loop (v110)

**`design/cs30_arch.py` → v5**

**Ramp: C-clip lead-in chamfer added**
- 0.8mm×45° chamfer on inner arm bottom-inner edge (z_local=8.6, y_local=3.6)
- Found via `filter_by_position(Axis.Z, 8.45..8.75)` + `filter_by_position(Axis.Y, 3.45..3.75)`
- face_count: 22→23 ✓, volume: 15235→15214mm³ (chamfer removed correct material)
- AgentCAD v146: is_valid=true, **68×70.7×32.6mm** ✓

**Assembly preview (PART=0): carriages + correct bridge height**
- Added carriages at CARRIAGE_Z=90mm (example mid-height setting)
- Bridge now at bridge_z = CARRIAGE_Z + CARR_H + SEC_PEG_H = 90+50+5 = **145mm** (was 175mm)
- AgentCAD v147: is_valid=true, **128×101×169mm** ✓
  - z_max=169mm = top of leg stack (2×82mm=164mm + 5mm peg) ✓
  - Bridge at z=145..154mm, carriages at z=90..140mm visible in preview

**`docs/cs30_assembly.md` — new (8 steps, BOM included)**
- BOM: 2× M3×25mm bolt, 2× M3 hex nut, 4× leg sections, 2× carriages, 2× bridge halves, 1× ramp
- Assembly order: photo_box → carriage prep → slide carriages → stack legs → clip to walls → set height + lock → place bridge → clip ramp
- Height adjustment procedure: loosen → slide to tooth mark → tighten → verify level

### Complete cs30_arch.py v7 part inventory
| PART | File | Count | Dims | Notes |
|------|------|-------|------|-------|
| 1 | cs30_ramp.stl | 1 | 68×70.7×32.6mm | 20° ramp, C-clip with lead-in chamfer |
| 2 | cs30_arch_leg_section.stl | 4 | **14×24×87mm** | Wide foot plate (24mm Y vs old 12mm); print standing |
| 3 | cs30_phone_bridge_half.stl | 2 | 60×78×10mm | Blind sockets (5mm+1mm floor); butt join at x=0 |
| 4 | cs30_arch_carriage.stl | 2 | 30×16×55mm | 1 per leg, lock bolt adjustable |
| 5 | cs30_lock_knob.stl | 2 | 19.2×20×8mm | **M3×30mm** bolt, thumb-turn; socket on outer face |

---

## STL export audit (AgentCAD v148–v159)

| PART | AgentCAD ver | Dims | is_valid | Bed OK? | Notes |
|------|-------------|------|----------|---------|-------|
| 1 ramp | v149 | 68×70.7×32.6mm | ✓ | ✓ | fits comfortably |
| 2 leg_section | **v169** | **14×24×87mm** | ✓ | ✓ tight | 87/88mm Z — **print standing, NO brim**; foot 24mm Y; end cap notches at inner corners |
| 3 bridge_half | **v160** | **60×78×10mm** | ✓ | ✓ tight | Y=78/78mm limit — **print flat, NO brim**; blind sockets |
| 4 carriage | **v164** | 30×16×55mm | ✓ | ✓ | **slot_d=12.3mm** clears rack teeth (was 10.3mm); leg_ctr_y=5.15mm ✓ |
| 5 lock_knob | **v168** | 19.2×20×8mm | ✓ | ✓ | socket on outer face (z=8mm) ✓ |

*Assembly v170: PART=0, is_valid=true, 128×158.7×169mm ✓ (v13 leg sections)*
| fit_test | **v163** | **68×16×30mm** | ✓ | ✓ | **(D) nut trap stub added**; 4 features; at 68mm bed limit |

## What changed this loop (v118)

**Documentation pass — all v117 priorities resolved**

### README.md — v10 complete
- Section header: "CS30 Arch v7" → "CS30 Arch v10"
- Part list header: "(v7)" → "(v10)" with integrated print settings columns (Profile, Infill, Brim, Notes)
- Carriage dims corrected: "30×16×50mm" → "30×16×55mm" (CARR_H=50 body + SEC_PEG_H=5 pegs)
- Added "Better Quality" profile and "25% gyroid / brim ON" for carriages
- Added "NO brim" warning for leg sections (87mm, 1mm bed margin) and bridge halves (78mm, 1mm bed margin)
- Fit test procedure: "56×16×30mm" → "68×16×30mm" (was stale; nut trap stub added in v116)
- Hardware section: "(v5)" → "(v10)"
- Clearance reference: "(v5)" → "(v10)"

### docs/cs30_print_manifest.md — NEW
- Full per-part table: qty, bed dims, orientation, profile, infill, brim, est. time
- Slicer orientation notes for each part (leg sections, bridge halves, carriage, ramp)
- Fit test procedure table (A/B/C/D) with adjust guidance
- Hardware BOM, print-and-assemble order, rebuild commands

**Autonomous decision**: chose 25% gyroid + Better Quality for carriage over 20% Recommended. The carriage is the only structural load-bearing part under clamping force; 25% adds ~3–4% more material at the nut trap and bolt bore walls without significant extra time.

## What changed this loop (v119)

**Final validation + README camera-to-card guidance**

**AgentCAD v166: PART=0 assembly final validation, is_valid=true, 128×158.7×169mm ✓**
- CoM x=−0.004mm (symmetric ✓), y=30.8mm, z=45.3mm (low CoM — legs are ballast)
- Full Compound with ramp, 4 leg sections, 2 carriages, bridge halves — all valid

**README height table expanded:**
- Added Camera→card column (= bridge_height − 6mm platen surface)
- Added Focus mode column: marks 30–90 = ultra-wide macro (<14cm); marks 95+ = dead zone
- Recommended range: rack marks 30–90mm
- Added app compatibility note (Apple Camera + Magnifier confirmed; third-party apps may blur)
- Formula: camera→card = rack_mark + 49mm

**Autonomous decision**: stopped the loop after v119. cs30_arch v10 is geometry-complete, documentation-complete, and final-validated. All assembly interfaces analytically verified. The next work item is physical printing + fit-testing by the user — not more geometry loops.

## LOOP STATUS: COMPLETE

cs30_arch v10 is **print-ready**. No further geometry loops needed.

### What the user should do next:
1. Open Creator Space; import `design/output/cs30_fit_test.stl` — print first (~18 min)
2. Test all four features (A/B/C/D) per `docs/cs30_print_manifest.md`
3. If fit_test passes, print full set per print manifest
4. Keep rack mark ≤ 90mm for ultra-wide macro focus (Apple Camera / Magnifier)

### If fit_test reveals a clearance issue:
- Adjust the appropriate constant in `cs30_arch.py`, re-run AgentCAD, reprint only fit_test
- See HANDOFF STL audit table for which constants control which feature

---

## Key parameters
```
RAMP_ANGLE=20°  RAMP_OW=68mm      ARCH_LEG_SEC_H=82mm  RACK_PITCH=5mm
LEG_W=14mm      LEG_D=10mm        CARR_W=30mm  CARR_D=16mm  CARR_H=50mm
CAM_W=36mm      CAM_D=30mm        KNOB_R=10mm  KNOB_H=8mm
PB_BOX_EXT_W=84mm  ARCH_H=175mm   EC_T=3mm  EC_SOCK_CL=0.3mm
BRIDGE_W=112mm  hw=58mm  CARR_PEG_X=41mm  CARR_PEG_OUTER_X=57mm
CARRIAGE_Z_PREVIEW=90mm  BRIDGE_Z_PREVIEW=145mm
```

## DO NOT
- Change photo_box.py geometry (frozen at v25)
- Add servo/motor geometry (Phase-2)
- Re-audit rack_stand_v2 (superseded)
