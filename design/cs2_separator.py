# design/cs2_separator.py -- v1: CS2 adjustable card separator
# ASCII-only comments (Windows cp1252 safe).
#
# Mounts to hopper front face using the two lower M3 boss holes
# (bx=+-15mm, bz=18mm). Centers over the 15x4mm exit slot.
#
# Mechanism: gap plate (PART=2) slides into back-face slot of body (PART=1)
# from below. M3 setscrew from body top face presses down on plate top edge,
# setting how high the plate can rise. The plate's bottom edge defines the
# separator gap above the card floor.
#   Gap = plate bottom Z above FLOOR_T. Range: 0.5-1.5mm. Target: 0.9mm.
#
# Setup: loosen setscrew, slide plate up until one card fits under bottom
# edge, tighten setscrew. Plate is held between setscrew tip (from above)
# and card-stack pressure (from below).
#
# PART=0  assembly view (body + gap plate shown together)
# PART=1  separator body    35x5x22mm  -- PLA, print flat (5mm tall on bed)
# PART=2  gap plate         14.8x3x12mm -- PLA, print flat (3mm tall on bed)
#
# Hardware (per separator):
#   M3x30 bolts x2     -- body-to-hopper mounting (into front face boss holes)
#   M3 nuts x2         -- nut receivers for mounting bolts
#   M3x12 setscrew x1  -- gap adjustment from body top face (self-taps into PLA)

# --- Constants mirroring cs2_hopper.py ---
FLOOR_T   =  4.0   # card floor Z in hopper (mm)
EXIT_W    = 15.0   # exit slot width (X)
BOSS_BX   = 15.0   # boss hole X offset (+-BOSS_BX mm)
BOSS_BZ   = 18.0   # boss hole Z in hopper coords from hopper bottom

# --- Body geometry ---
BODY_W    = 35.0   # width (X): spans boss holes at +-15mm with 2.5mm margin
BODY_T    =  5.0   # thickness (Y): protrudes from hopper front face
BODY_H    = 22.0   # height (Z): body bottom = FLOOR_T in hopper
M3_D      =  3.4   # M3 clearance hole (mounting bolts)
M3_TAP    =  2.5   # M3 tapped/self-tap hole (setscrew in body top)

# --- Slot dimensions (back face, open at -Y and at bottom z=0) ---
PLATE_W   = EXIT_W - 0.2    # 14.8mm -- 0.1mm/side clearance in X
PLATE_T   =  3.0            # gap plate thickness (Y)
PLATE_H   = 12.0            # gap plate height (Z)
SLOT_W    = PLATE_W + 0.2   # 15.0mm slot in body (X)
SLOT_T    = PLATE_T + 0.1   # 3.1mm slot depth from back face (Y)
SLOT_H    = 15.0            # slot height (Z): from z=0 up; 3mm above plate top

# --- Setscrew hole (Z direction, from body top) ---
# Engages 7mm of body material (z=15..22) + 4mm tip in slot (z=11..15)
# M3x12 setscrew threads in, tip contacts gap plate top edge at z~12-13mm
SCREW_Y   =  1.0   # Y offset from body centre (front half, clears slot back wall)
SCREW_BOT = SLOT_H - 4.0   # z=11mm -- tip reaches plate top at gap 0.5-1.5mm
SCREW_DEP = BODY_H - SCREW_BOT   # 11mm total hole depth from body top

PART = 0

# ================================================================== #
# Body (PART=1)                                                       #
# ================================================================== #
body = Box(BODY_W, BODY_T, BODY_H,
           align=(Align.CENTER, Align.CENTER, Align.MIN))

# M3 mounting holes (Y direction) matching hopper boss holes
z_boss = BOSS_BZ - FLOOR_T   # 14.0mm from body bottom
for bx in [-BOSS_BX, BOSS_BX]:
    h = Cylinder(radius=M3_D / 2, height=BODY_T + 2,
                 align=(Align.CENTER, Align.CENTER, Align.CENTER))
    h = h.rotate(Axis.X, 90)
    h = h.translate((bx, 0, z_boss))
    body = body - h

# Gap plate slot (open at back face -Y and at bottom z=0)
# Back face at y = -BODY_T/2 = -2.5mm; slot goes +SLOT_T into body
slot = Box(SLOT_W, SLOT_T, SLOT_H + 0.1,
           align=(Align.CENTER, Align.MIN, Align.MIN))
slot = slot.translate((0, -BODY_T / 2, -0.1))
body = body - slot

# Setscrew hole (Z direction, from top face downward)
# Centred at y=SCREW_Y (front half of body); hole extends SCREW_DEP mm down
screw_h = Cylinder(radius=M3_TAP / 2, height=SCREW_DEP + 0.1,
                   align=(Align.CENTER, Align.CENTER, Align.MIN))
screw_h = screw_h.translate((0, SCREW_Y, BODY_H - SCREW_DEP))
body = body - screw_h

# ================================================================== #
# Gap plate (PART=2)                                                  #
# ================================================================== #
plate = Box(PLATE_W, PLATE_T, PLATE_H,
            align=(Align.CENTER, Align.CENTER, Align.MIN))

# ================================================================== #
# PART selector                                                       #
# ================================================================== #
if PART == 0:
    # Assembly view: body + gap plate side by side (offset X for clarity)
    result = body + plate.translate((BODY_W / 2 + PLATE_W / 2 + 5, 0, 0))

elif PART == 1:
    result = body

elif PART == 2:
    result = plate

show_object(result)
