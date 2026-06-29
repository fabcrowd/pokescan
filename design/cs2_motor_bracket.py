# design/cs2_motor_bracket.py -- v1: CS2 Phase 2 servo motor mount bracket
# ASCII-only comments (Windows cp1252 safe).
# Mounts on hopper front face (y=-OUTER_W/2 outer face) via 4x M3 boss holes.
# Boss holes in cs2_hopper.py: x=+/-15mm, z=18mm and z=36mm (Y-direction through front wall).
#
# Holds SG90 micro servo (body 22.5x12x22mm, shaft 4.7mm above base):
#   Servo slides into cradle from the user side (+Y face, away from hopper).
#   Servo output shaft faces -Y (toward hopper); arm sweeps in XZ plane.
#   Arm drives connecting rod from z=28mm (servo shaft) down to z=6mm (exit slot level).
#   One full arm swing (90deg) ejects one card through the 15x4mm exit slot.
#
# Crank geometry: see design/cs2_card_pusher.py (PART=1 crank_arm, PART=2 push_rod).
#   Arm length: 22mm -> tip moves 22mm * sin(90) = 22mm horizontal at exit slot level
#   Exit slot is 15mm wide; pusher paddle needs 15mm stroke minimum.
#
# Print: PETG or PLA, flat on bed (XZ face down).
# Bed check: 42 x 15 x 32mm -- fits Toybox 68x78x88mm usable easily.
# No supports. Zip-tie slots allow any servo/motor body within 23mm width.

PLATE_W  = 42.0   # plate width (X); covers boss holes at +/-15mm + 6mm margin each side
PLATE_T  = 3.0    # plate thickness (Y); flush against hopper front face
PLATE_H  = 32.0   # plate height (Z); covers boss holes z=18..36mm + 7mm each side
PLATE_Z0 = 11.0   # plate bottom Z (= BOSS_Z_LO - 7mm = 18 - 7)

# Cradle: U-channel extending in +Y from plate back face; holds servo body
CRADLE_OW = 28.0  # cradle outer width (X); 23mm servo + 2.5mm wall each side
CRADLE_OD = 12.0  # cradle outer depth (Y); equals SG90 body depth (12mm)
CRADLE_OH = 27.0  # cradle outer height (Z); 23mm channel + 2mm bottom + 2mm top
CRADLE_Z0 = 15.0  # cradle bottom Z (= servo bottom z=17mm - 2mm bottom wall)

# Servo channel dimensions (open at +Y face for insertion)
CHAN_W  = 23.0    # channel width (X); SG90 22.5mm + 0.25mm clearance each side
CHAN_D  = 10.0    # channel depth (Y from cradle back wall); leaves ~2mm back wall
CHAN_H  = 23.0    # channel height (Z); SG90 22mm + 0.5mm clearance
CHAN_Z0 = 17.0    # channel bottom Z (servo body spans z=17..40mm, shaft at z=28mm)

M3_D    = 3.4     # M3 clearance hole diameter
BOSS_X  = 15.0    # boss hole X offset (matches cs2_hopper.py BOSS positions)
BOSS_Z0 = 18.0    # lower boss hole Z
BOSS_Z1 = 36.0    # upper boss hole Z

# -- Flat mounting plate (MIN in Y: plate front face at y=0, back face at y=PLATE_T) --
plate = Box(PLATE_W, PLATE_T, PLATE_H,
            align=(Align.CENTER, Align.MIN, Align.MIN))
plate = plate.translate((0, 0, PLATE_Z0))

# -- Servo cradle outer (MIN in Y: front face at y=PLATE_T, back face at y=PLATE_T+CRADLE_OD) --
cradle = Box(CRADLE_OW, CRADLE_OD, CRADLE_OH,
             align=(Align.CENTER, Align.MIN, Align.MIN))
cradle = cradle.translate((0, PLATE_T, CRADLE_Z0))

# -- Servo channel: removes interior, open at high-Y face for servo insertion --
# Box MAX-aligned in Y so its high face sits at cradle top (+Y face) + 0.5mm overcut.
# Channel: y from ~(PLATE_T + 2mm back-wall) to (PLATE_T + CRADLE_OD + 0.5mm).
chan = Box(CHAN_W, CHAN_D + 1, CHAN_H,
           align=(Align.CENTER, Align.MAX, Align.MIN))
chan = chan.translate((0, PLATE_T + CRADLE_OD + 0.5, CHAN_Z0))
# Back wall = CRADLE_OD - CHAN_D - 0.5 = 12 - 10 - 0.5 = 1.5mm (adequate for PLA/PETG)

bracket = plate + cradle - chan

# -- 4x M3 through-holes (Y-direction through full plate + cradle back wall) --
# Cylinder axis in Y; centred at y=PLATE_T/2 so it spans y=-1..PLATE_T+1.
for bx in [-BOSS_X, BOSS_X]:
    for bz in [BOSS_Z0, BOSS_Z1]:
        m3 = Cylinder(radius=M3_D / 2, height=PLATE_T + CRADLE_OD + 2,
                      align=(Align.CENTER, Align.CENTER, Align.CENTER))
        m3 = m3.rotate(Axis.X, 90)
        m3 = m3.translate((bx, (PLATE_T + CRADLE_OD) / 2, bz))
        bracket = bracket - m3

# -- 2x zip-tie slots through plate (Y-direction, at servo body centre height) --
# Slots centred at servo mid-Z (z=CHAN_Z0 + CHAN_H/2 = 28.5mm), at x=+/-5mm.
ZT_L = 10.0; ZT_H = 3.2
for sx in [-1, 1]:
    zt = Box(ZT_L, PLATE_T + 2, ZT_H,
             align=(Align.CENTER, Align.CENTER, Align.CENTER))
    zt = zt.translate((sx * 5, PLATE_T / 2, CHAN_Z0 + CHAN_H / 2))
    bracket = bracket - zt

result = bracket
show_object(result)
