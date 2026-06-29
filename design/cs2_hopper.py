# design/cs2_hopper.py -- v5: CS2 card scanner hopper (open-top funnel box, 2 halves)
# ASCII-only comments (Windows cp1252 safe).
# Matches CS30 Card Slinger form factor: open-top box, card settles on floor for scanning.
#
# Orientation: card long axis (88mm) runs in X across the split seam at x=0.
#              card short axis (63mm) runs in Y.
#              z=0 is table surface, card face at z=FLOOR_T=4mm.
#
# PART=0 full assembly  PART=1 left half (x<=0)  PART=2 right half (x>=0)
#
# Bed check per half: 48.5 x 72 x 70mm -- fits Toybox 68x78x88mm usable OK.
#
# v4 Phase-2 changes (reprint required):
#   SHAFT_Z 8 -> 12.5mm  (roller v2: OD=17mm, so shaft at 12.5mm centres roller bottom at 4mm)
#   EXIT_W  15 -> 90mm   (card body exit: widened from arm-port-only to full slot width)
#   peg hole z=17 -> 19mm (maintains >=1mm clearance from new shaft top at z=15.5mm)
#
# v5 Phase-1 manual operation:
#   Thumb-push hole in back wall (z=2..16mm, 25mm wide, centred x=0).
#   Hole starts 2mm below card floor so thumb slips under card and pushes its face,
#   not the narrow 0.8mm card edge -- safe for sleeved and bare cards.
#
# Phase 2 provisions (geometry only -- no mechanism in Phase 1):
#   6mm shaft holes in end walls at z=SHAFT_Z (roller axle spans both halves)
#   90x4mm card exit opening in front wall at z=FLOOR_T (card body + arm port)
#   4x M3 boss holes on front face (motor bracket mount points)
#
# Join: 2x M3 through-holes (X direction) in front/back walls + 2x 3mm align pegs

CARD_L   = 88.0     # card long axis (X)
CARD_W   = 63.0     # card short axis (Y)
SCAN_TOL = 1.0      # clearance each side at inner slot
WALL_T   = 3.5      # wall thickness
FLOOR_T  = 4.0      # floor thickness (card face at z=FLOOR_T)
OUTER_H  = 70.0     # total hopper height (v3: increased from 50mm; ~160 practical cards)

SLOT_L   = CARD_L + 2 * SCAN_TOL   # 90.0mm: inner slot length (X)
SLOT_W   = CARD_W + 2 * SCAN_TOL   # 65.0mm: inner slot width (Y)
INNER_H  = OUTER_H - FLOOR_T        # 46.0mm: inner void height

OUTER_L  = SLOT_L + 2 * WALL_T     # 97.0mm: total assembled length (X)
OUTER_W  = SLOT_W + 2 * WALL_T     # 72.0mm: total assembled width (Y)

M3_D     = 3.4      # M3 clearance hole diameter
PEG_D    = 3.0      # alignment peg diameter
PEG_L    = 5.0      # alignment peg length

SHAFT_D  = 6.0      # Phase 2: roller shaft diameter
SHAFT_Z  = 12.5     # Phase 2: shaft hole centre height (v4: 8->12.5 for roller v2 OD=17mm)
EXIT_W   = 90.0     # Phase 2: card exit opening width (v4: 15->90mm = SLOT_L; card body exits)
EXIT_H   = 4.0      # Phase 2: exit opening height (Z)
BOSS_D   = 3.4      # Phase 2: motor boss hole diameter (M3)

THUMB_W  = 25.0     # Manual: thumb-push hole width (X)
THUMB_H  = 14.0     # Manual: thumb-push hole height (Z); starts 2mm below card floor
THUMB_Z0 = 2.0      # Manual: hole bottom (below card floor at z=4); thumb slips under card

PART = 0

# -- Outer shell --
outer = Box(OUTER_L, OUTER_W, OUTER_H,
            align=(Align.CENTER, Align.CENTER, Align.MIN))

# -- Inner card slot (straight-sided; card rests on floor) --
inner = Box(SLOT_L, SLOT_W, INNER_H + 2,
            align=(Align.CENTER, Align.CENTER, Align.MIN))
inner = inner.translate((0, 0, FLOOR_T))

hopper = outer - inner

# -- Phase 2: roller shaft holes through end walls (X direction) --
# One hole per end wall; roller axle spans the full 97mm when assembled.
for sx in [-1, 1]:
    shaft = Cylinder(radius=SHAFT_D / 2, height=WALL_T + 2,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER))
    shaft = shaft.rotate(Axis.Y, 90)
    shaft = shaft.translate((sx * OUTER_L / 2, 0, SHAFT_Z))
    hopper = hopper - shaft

# -- Phase 2: card exit slot in front wall (y = -OUTER_W/2) --
exit_slot = Box(EXIT_W, WALL_T + 2, EXIT_H,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
exit_slot = exit_slot.translate((0, -OUTER_W / 2 + WALL_T / 2, FLOOR_T))
hopper = hopper - exit_slot

# -- Phase 2: M3 motor bracket boss holes on front face (4x) --
for bx, bz in [(-15.0, 18.0), (15.0, 18.0), (-15.0, 36.0), (15.0, 36.0)]:
    boss = Cylinder(radius=BOSS_D / 2, height=WALL_T + 2,
                    align=(Align.CENTER, Align.CENTER, Align.CENTER))
    boss = boss.rotate(Axis.X, 90)
    boss = boss.translate((bx, -OUTER_W / 2 + WALL_T / 2, bz))
    hopper = hopper - boss

# -- Manual eject: thumb-push hole in back wall (y = +OUTER_W/2) --
# Centred at x=0 (spans both halves), z=THUMB_Z0..THUMB_Z0+THUMB_H = 2..16mm.
# Starts 2mm below card floor so user's thumb slips under the card and pushes
# the card face rather than its narrow 0.8mm edge -- avoids card damage.
# Clears peg holes (z=19mm) with 1.5mm margin.  No conflict with end-wall shaft holes.
thumb_hole = Box(THUMB_W, WALL_T + 2, THUMB_H,
                 align=(Align.CENTER, Align.CENTER, Align.MIN))
thumb_hole = thumb_hole.translate((0, OUTER_W / 2 - WALL_T / 2, THUMB_Z0))
hopper = hopper - thumb_hole

# -- Join: M3 through-holes (X direction) in front and back walls at mid-height --
for by in [-OUTER_W / 2 + WALL_T / 2, OUTER_W / 2 - WALL_T / 2]:
    bolt = Cylinder(radius=M3_D / 2, height=OUTER_L + 2,
                    align=(Align.CENTER, Align.CENTER, Align.CENTER))
    bolt = bolt.rotate(Axis.Y, 90)
    bolt = bolt.translate((0, by, OUTER_H / 2))
    hopper = hopper - bolt

# -- Alignment peg holes (2x 3mm, PEG_L=5mm) at halves seam (x=0) --
# z=17mm: clears shaft holes (z=5..11mm) and join bolts (z=25mm).
# Each half gets a 2.5mm blind hole; a 3mm x 5mm dowel pin bridges both halves.
for by in [-OUTER_W / 2 + WALL_T / 2, OUTER_W / 2 - WALL_T / 2]:
    ph = Cylinder(radius=PEG_D / 2, height=PEG_L,
                  align=(Align.CENTER, Align.CENTER, Align.CENTER))
    ph = ph.rotate(Axis.Y, 90)
    ph = ph.translate((0, by, 19.0))
    hopper = hopper - ph

# -- PART selector: split at x=0 --
if PART == 0:
    result = hopper

elif PART == 1:
    # Left half: x from -OUTER_L/2 to 0
    mask = Box(OUTER_L / 2, OUTER_W * 2, OUTER_H * 2,
               align=(Align.MAX, Align.CENTER, Align.CENTER))
    result = hopper & mask

elif PART == 2:
    # Right half: x from 0 to +OUTER_L/2
    mask = Box(OUTER_L / 2, OUTER_W * 2, OUTER_H * 2,
               align=(Align.MIN, Align.CENTER, Align.CENTER))
    result = hopper & mask

show_object(result)
