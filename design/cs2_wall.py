# design/cs2_wall.py -- v2: CS2 back wall (height-adjustable phone stand column)
# ASCII-only comments (Windows cp1252 safe).
# Vertical back panel that supports the cs2_platform at adjustable heights.
# Matches CS30 Card Slinger C-stand form factor.
#
# 4 printable sections: 2 halves x 2 vertical sections.
# PART=0 assembly  PART=1 bot-L  PART=2 bot-R  PART=3 top-L  PART=4 top-R
#
# Assembled: 97 x 14 x 174mm (matches hopper OUTER_L=97mm width)
# Each section: 48.5 x 14 x 87mm -- fits Toybox 68x78x88mm usable (1mm Z margin)
#
# Platform height positions (4x): 100, 125, 150, 165mm above hopper floor (z=0)
# All positions are in the top sections (z=87..174mm).
# 2x M3 holes at x=+-22mm at each height -- platform bolts from front, nut on back.
#
# Section joints: 3x M3 holes in Z at z=87mm boundary (M3x20mm bolts, recessed head).
# Halves join: 3x M3 holes through wall thickness (Y direction) at left/right seam.
# Bottom flange: 5mm thick flange at z=0..5mm with 3x M3 holes to bolt to hopper back face.

WALL_W    = 97.0     # assembled width (X) -- matches hopper OUTER_L
WALL_T    = 14.0     # wall thickness (Y, front to back)
SECTION_H = 87.0     # each section height (Z); 2 sections = 174mm total

# Platform bolt positions (all in top section; z offsets from hopper floor)
# PLAT_Z is the platform BOTTOM face height; holes are at PLAT_Z + PLAT_T/2 (mid-platform)
PLAT_Z    = [100.0, 125.0, 150.0, 165.0]   # platform bottom face heights
PLAT_T    = 8.0      # platform thickness (must match cs2_platform.py PLAT_T)
PLAT_X    = 22.0     # bolt hole X offset from wall centre (each side)
PLAT_HOLE = 3.4      # M3 clearance hole through wall

# Section-join holes (3x M3 in Z at section boundary)
JOIN_Z_D  = 3.4      # M3 hole diameter for section joins
JOIN_X    = [-30.0, 0.0, 30.0]   # X positions for join holes

# Halves join (M3 in Y through wall at seam)
HALF_D    = 3.4      # M3 clearance

# Bottom flange (bolts to hopper back face)
FLANGE_T  = 5.0      # flange thickness (Z)
FLANGE_D  = 6.0      # flange depth extension in +Y (toward hopper)
FLANGE_HOLE = 3.4    # M3 clearance

PART = 0

half_w = WALL_W / 2   # 48.5mm per half

# Build full assembled wall (2 sections stacked, both halves)
wall = Box(WALL_W, WALL_T, SECTION_H * 2,
           align=(Align.CENTER, Align.MIN, Align.MIN))

# Platform attachment holes (M3, through full Y thickness, at mid-platform Z)
# Hole centre at pz + PLAT_T/2 so it aligns with the Y-direction bolt hole in cs2_platform
for pz in PLAT_Z:
    for sx in [-1, 1]:
        ph = Cylinder(radius=PLAT_HOLE / 2, height=WALL_T + 2,
                      align=(Align.CENTER, Align.CENTER, Align.CENTER))
        ph = ph.rotate(Axis.X, 90)
        ph = ph.translate((sx * PLAT_X, WALL_T / 2, pz + PLAT_T / 2))
        wall = wall - ph

# Section join holes (M3 in Z at z=SECTION_H boundary, recessed 5mm deep each side)
for jx in JOIN_X:
    jh = Cylinder(radius=JOIN_Z_D / 2, height=10.0,
                  align=(Align.CENTER, Align.CENTER, Align.MIN))
    # Hole from top of bottom section going up: z=SECTION_H-5 to SECTION_H+5
    jh_top = jh.translate((jx, WALL_T / 2, SECTION_H - 5))
    wall = wall - jh_top
    # Matching hole from bottom of top section going down: z=SECTION_H-5 to SECTION_H+5
    # (same subtraction covers both, since it spans the boundary)

# Halves join: 3x M3 holes in Y direction at x=0 seam (front/mid/back of wall)
for hz in [SECTION_H * 0.25, SECTION_H * 0.75, SECTION_H * 1.25, SECTION_H * 1.75]:
    hh = Cylinder(radius=HALF_D / 2, height=WALL_T + 2,
                  align=(Align.CENTER, Align.CENTER, Align.CENTER))
    hh = hh.rotate(Axis.X, 90)
    hh = hh.translate((0, WALL_T / 2, hz))
    wall = wall - hh

# Bottom flange: extends in +Y to bolt against hopper back face
flange = Box(WALL_W, WALL_T + FLANGE_D, FLANGE_T,
             align=(Align.CENTER, Align.MIN, Align.MIN))
wall = wall + flange

# Flange holes (3x M3 in Y for hopper attachment)
for fx in [-25.0, 0.0, 25.0]:
    fh = Cylinder(radius=FLANGE_HOLE / 2, height=WALL_T + FLANGE_D + 2,
                  align=(Align.CENTER, Align.CENTER, Align.CENTER))
    fh = fh.rotate(Axis.X, 90)
    fh = fh.translate((fx, (WALL_T + FLANGE_D) / 2, FLANGE_T / 2))
    wall = wall - fh

# PART selector
if PART == 0:
    result = wall

else:
    # Determine which section (top/bottom) and which half (left/right)
    top    = PART in [3, 4]
    is_right = PART in [2, 4]

    z_min = SECTION_H if top else 0.0
    z_max = SECTION_H * 2 if top else SECTION_H

    x_min = 0.0 if is_right else -WALL_W / 2
    x_max = WALL_W / 2 if is_right else 0.0

    z_size = z_max - z_min
    x_size = x_max - x_min
    x_ctr  = (x_min + x_max) / 2
    z_ctr  = (z_min + z_max) / 2

    mask = Box(x_size + 2, WALL_T * 4, z_size + 2,
               align=(Align.CENTER, Align.CENTER, Align.CENTER))
    mask = mask.translate((x_ctr, WALL_T / 2, z_ctr))
    result = wall & mask

show_object(result)
