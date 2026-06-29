# design/cs2_centering_insert.py -- v2: CS2 funnel collar
# ASCII-only comments (Windows cp1252 safe).
#
# Clips onto top of the assembled CS2 hopper halves.  Adds 25mm of angled
# entry funnel above the hopper so cards tossed from above self-center into
# the 90x65mm slot without precise placement.
#
# Inspired by Card Slinger 3.0 toss-and-scan workflow; geometry is original.
#
# Orientation: matches cs2_hopper.py -- card long axis (88mm) in X.
#   z=0 = bottom of collar (sits on top of hopper outer walls at z=50mm).
#   Total collar height: 30mm.
#
# Clip section (z=0..5mm): channel slides over hopper outer walls.
#   Inner channel: OUTER_L+2*CLIP_CL x OUTER_W+2*CLIP_CL (0.3mm clearance).
#
# Funnel void (z=5..30mm): ruled loft from SLOT (90x65) at z=5 to HAT
#   footprint (103x78) at z=30.  All four walls are planar tapered faces --
#   cards dropped from above land in the 103x78 mouth and converge to the slot.
#
# v1 bug: wedge-subtract approach gave wrong taper (wedges only reached z~16).
# v2 fix: loft replaces all four wedge subtractions.
#
# PART=0  full collar (assembly / reference)   103x78x30mm
# PART=1  left half  (x<=0)  51.5x78x30mm  -- fits Toybox 68x78x88mm
# PART=2  right half (x>=0)  -- same dims
#
# Print: white/coconut PLA, flat on XY (30mm tall), no supports.
# Join halves: 2x M3 through-holes in X direction (same spacing as hopper).

# --- Hopper constants (must match cs2_hopper.py) ---
SLOT_L   = 90.0   # hopper inner slot length (X)
SLOT_W   = 65.0   # hopper inner slot width (Y)
OUTER_L  = 97.0   # hopper outer length (X)
OUTER_W  = 72.0   # hopper outer width (Y)

# --- Funnel collar constants ---
CLIP_H    =  5.0   # clip section height (slides over hopper outer walls)
FUNNEL_H  = 25.0   # funnel section height above clip
TOTAL_H   = CLIP_H + FUNNEL_H   # 30mm

CLIP_CL   =  0.3   # clearance for clip channel over hopper walls (each side)
CLIP_WALL_X = 3.0  # clip wall in X: (103 - 97) / 2
CLIP_WALL_Y = 3.0  # clip wall in Y: (78  - 72) / 2

HAT_L = OUTER_L + 2 * CLIP_WALL_X   # 103.0mm
HAT_W = OUTER_W + 2 * CLIP_WALL_Y   # 78.0mm  (exactly Toybox usable Y)

M3_D = 3.4
PART = 0

# ------------------------------------------------------------------ #
#  Outer solid                                                        #
# ------------------------------------------------------------------ #
hat = Box(HAT_L, HAT_W, TOTAL_H,
          align=(Align.CENTER, Align.CENTER, Align.MIN))

# ------------------------------------------------------------------ #
#  Clip channel (z=0..CLIP_H)                                        #
#  Slides over assembled hopper outer walls.                         #
# ------------------------------------------------------------------ #
clip_void = Box(OUTER_L + 2 * CLIP_CL,
                OUTER_W + 2 * CLIP_CL,
                CLIP_H + 0.1,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
hat = hat - clip_void

# ------------------------------------------------------------------ #
#  Tapered funnel void (z=CLIP_H..TOTAL_H)                           #
#  Ruled loft: slot rect at z=5 -> hat footprint (+2mm margin) at    #
#  z=30.  Planar faces on all four walls; correct taper guaranteed.  #
# ------------------------------------------------------------------ #
with BuildPart() as _fp:
    with BuildSketch(Plane.XY.offset(CLIP_H)):
        Rectangle(SLOT_L, SLOT_W)
    with BuildSketch(Plane.XY.offset(TOTAL_H)):
        Rectangle(HAT_L, HAT_W)            # matches hat footprint exactly -- clean open top
    loft(ruled=True)
hat = hat - _fp.part

# ------------------------------------------------------------------ #
#  M3 through-holes (X direction) for collar half join               #
#  y = +/-OUTER_W/4, z = CLIP_H/2 (centre of clip section)          #
#  Same bolt hardware as the hopper seam bolts.                      #
# ------------------------------------------------------------------ #
for by in [OUTER_W / 4, -OUTER_W / 4]:
    bolt = Cylinder(radius=M3_D / 2, height=HAT_L + 2,
                    align=(Align.CENTER, Align.CENTER, Align.CENTER))
    bolt = bolt.rotate(Axis.Y, 90)
    bolt = bolt.translate((0, by, CLIP_H / 2))
    hat = hat - bolt

# ------------------------------------------------------------------ #
#  PART selector                                                      #
# ------------------------------------------------------------------ #
if PART == 0:
    result = hat

elif PART == 1:
    mask = Box(HAT_L, HAT_W * 2, TOTAL_H * 2,
               align=(Align.MAX, Align.CENTER, Align.CENTER))
    result = hat & mask

elif PART == 2:
    mask = Box(HAT_L, HAT_W * 2, TOTAL_H * 2,
               align=(Align.MIN, Align.CENTER, Align.CENTER))
    result = hat & mask

show_object(result)
