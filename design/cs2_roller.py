# design/cs2_roller.py -- v2: CS2 rubber-gasket drive roller
# ASCII-only comments (Windows cp1252 safe).
#
# Rides on 6mm shaft through cs2_hopper.py shaft holes.
# Two 16mm ID plumbing O-rings (standard sink gaskets) stretch over the
# 17mm OD drum and seat in the grooves, providing a grippy rubber nip
# for single-card eject.  Much cheaper and more replaceable than PETG
# press-fit (v1); no press-fit tooling required.
#
# Hardware: 16mm ID x 2mm cross-section rubber O-rings (x2 per roller).
#   Standard plumbing sink gaskets; widely available at hardware stores.
#
# SHAFT HEIGHT NOTE (BREAKING CHANGE vs v1):
#   OD=17mm drum requires shaft centre at z=12.5mm so drum bottom is at
#   z = 12.5 - 8.5 = 4.0mm = card floor (FLOOR_T).
#   cs2_hopper.py currently has SHAFT_Z=8mm (v2 STLs).
#   Update SHAFT_Z=12.5 in cs2_hopper.py and reprint hopper halves before
#   assembling this roller.
#
# Gasket groove geometry:
#   Groove at z=3mm from left end: seats O-ring closest to exit slot.
#   Groove at z=12mm from left end: seats second O-ring for parallel drive.
#   Groove: 3mm wide x 1.5mm deep.  O-ring protrudes 1.5mm above drum surface
#   (16mm ID O-ring on 17mm drum: protrudes (17-16)/2 = 0.5mm radially,
#    cross-section 2mm so protrusion ~1.5mm above groove lip).
#
# Bore: 6.2mm slip fit on 6mm shaft (0.1mm/side clearance).
#   Held in place with CA glue or M3 setscrew from end face.
#
# PART=0  single roller (assembly / reference)   20x17x17mm
# PART=1  print plate: 4 rollers, 2x2 grid      ~39x43x17mm (fits Toybox bed)
#
# Print: PETG preferred (better flex/grip than PLA).
#   PART=1: no supports needed (round surface on bed).

ROLLER_OD = 17.0    # drum outer diameter; stretches 16mm ID O-ring
ROLLER_L  = 20.0    # drum length (X axis in PART=0)
BORE_D    = 6.2     # bore diameter; 0.1mm/side clearance on 6mm shaft

GASKET_GROOVE_W = 3.0    # groove width in mm (seats 2mm cross-section O-ring)
GASKET_GROOVE_D = 1.5    # groove depth in mm from drum surface
GASKET_Z = [3.0, 12.0]   # groove centres, measured from left end of drum

PART = 0


def make_drum():
    """Single drum with bore and gasket grooves; long axis in X, centred at origin."""
    # Outer drum cylinder
    d = Cylinder(radius=ROLLER_OD / 2, height=ROLLER_L,
                 align=(Align.CENTER, Align.CENTER, Align.CENTER))
    d = d.rotate(Axis.Y, 90)

    # Bore
    bore = Cylinder(radius=BORE_D / 2, height=ROLLER_L + 2,
                    align=(Align.CENTER, Align.CENTER, Align.CENTER))
    bore = bore.rotate(Axis.Y, 90)
    d = d - bore

    # Gasket grooves -- each is an annular channel cut into the drum surface.
    # Annular ring = outer cyl - inner cyl, rotated so axis is in X.
    for gz in GASKET_Z:
        x_ctr = -ROLLER_L / 2 + gz   # groove centre along drum axis
        go = Cylinder(radius=ROLLER_OD / 2 + 0.1, height=GASKET_GROOVE_W,
                      align=(Align.CENTER, Align.CENTER, Align.CENTER)).rotate(Axis.Y, 90)
        gi = Cylinder(radius=ROLLER_OD / 2 - GASKET_GROOVE_D,
                      height=GASKET_GROOVE_W + 0.2,
                      align=(Align.CENTER, Align.CENTER, Align.CENTER)).rotate(Axis.Y, 90)
        groove_void = (go - gi).translate((x_ctr, 0, 0))
        d = d - groove_void

    return d


if PART == 0:
    result = make_drum()

elif PART == 1:
    # Plate of 4 rollers, each lying flat (long axis in Y for bed stability).
    # Drum lies on its round surface: Z height = ROLLER_OD/2 from bed to axis.
    # Grid spacing: 22mm in X (17 OD + 5 gap), 23mm in Y (20 length + 3 gap).
    # Plate footprint: ~39 x 43mm -- fits Toybox 68x78mm easily.
    dx = ROLLER_OD + 5.0     # 22mm between drum centres in X
    dy = ROLLER_L  + 3.0     # 23mm between drum centres in Y

    def make_flat_roller():
        # Drum (axis in X) rotated 90 deg around Z so axis is in Y (flat on bed).
        return make_drum().rotate(Axis.Z, 90)

    r1 = make_flat_roller().translate((-dx / 2, -dy / 2, ROLLER_OD / 2))
    r2 = make_flat_roller().translate(( dx / 2, -dy / 2, ROLLER_OD / 2))
    r3 = make_flat_roller().translate((-dx / 2,  dy / 2, ROLLER_OD / 2))
    r4 = make_flat_roller().translate(( dx / 2,  dy / 2, ROLLER_OD / 2))

    result = r1 + r2 + r3 + r4

show_object(result)
