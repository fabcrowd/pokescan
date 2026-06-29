# design/cs2_card_pusher.py -- v1: CS2 Phase 2 crank arm + push rod for SG90 servo
# No imports needed -- build123d pre-injected by AgentCAD.
# ASCII-only comments (Windows cp1252 safe).
#
# SG90 servo shaft at z=28mm (cs2_motor_bracket: CHAN_Z0=17, body 22mm, shaft at body mid+).
# Crank arm: 22mm moment arm; at full 90-deg throw arm points straight down,
#   tip descends from (22, y, 28) to (0, y, 6mm) -- exactly the exit slot Z.
# Push rod: 31mm connecting rod linking crank tip to card-exit anchor; spans XZ plane.
#
# PART=0  assembly stub (arm at servo height + rod offset)
# PART=1  crank_arm  -- D-flat hub bore + 22mm arm + tip pin socket; print flat ~29x9x6mm
# PART=2  push_rod   -- 31mm rod + pin sockets at each end; print flat 31x5x3mm
#
# Bed check (Toybox 68x78x88mm usable):
#   crank_arm: 29 x 9 x 6mm  -- fits flat OK
#   push_rod:  31 x 5 x 3mm  -- fits flat OK

SHAFT_Z    = 28.0   # servo shaft Z (world coords, bracket mounted at hopper front face)
ARM_L      = 22.0   # moment arm length: shaft centre to tip; equals (SHAFT_Z - EXIT_Z)
EXIT_Z     = 6.0    # exit slot Z centre (FLOOR_T=4, EXIT_H=4)

HUB_OD     = 9.0    # hub boss outer diameter
HUB_L      = 6.0    # hub boss length (depth on shaft)

# D-flat bore (SG90: 4.7mm D-flat shaft)
BORE_R     = 2.50   # bore radius = 4.7/2 + 0.15mm clearance
FLAT_Y     = 1.55   # flat edge Y = 4.7/2 - 0.8mm chord depth (flat faces +Y)

ARM_W      = 5.0    # arm width (Y)
ARM_T      = 3.5    # arm thickness (Z when printing flat)
ARM_X0     = 2.5    # arm root X (overlaps hub by HUB_OD/2 - ARM_X0 = 2mm)

PIN_D      = 3.0    # pin socket diameter (press-fit 3mm pin)

ROD_L      = 31.0   # push rod body length (~sqrt(22^2 + 22^2) = 31.1mm)
ROD_W      = 5.0    # rod width
ROD_T      = 3.0    # rod thickness

PART = 0


def crank_arm():
    """Hub boss with D-flat bore + 22mm rectangular arm + tip pin socket."""
    # Hub boss
    hub = Cylinder(radius=HUB_OD / 2, height=HUB_L,
                   align=(Align.CENTER, Align.CENTER, Align.MIN))

    # D-flat bore: bore cylinder minus the flat-cut slab above FLAT_Y
    bore = Cylinder(radius=BORE_R, height=HUB_L + 4,
                    align=(Align.CENTER, Align.CENTER, Align.CENTER))
    bore = bore.translate((0, 0, HUB_L / 2))
    # Flat-cut slab: starts at y=FLAT_Y, extends in +Y; removes top of cylinder
    flat = Box(BORE_R * 4, BORE_R * 4, HUB_L + 6,
               align=(Align.CENTER, Align.MIN, Align.CENTER))
    flat = flat.translate((0, FLAT_Y, HUB_L / 2))
    # D-flat void = bore - flat (lower D-arc shape); subtract from hub
    hub = hub - (bore - flat)

    # Arm body: MIN-aligned in X, starts at ARM_X0, spans ARM_L
    arm = Box(ARM_L, ARM_W, ARM_T,
              align=(Align.MIN, Align.CENTER, Align.MIN))
    arm = arm.translate((ARM_X0, 0, (HUB_L - ARM_T) / 2))

    # Tip pin socket: Z-direction through arm at tip (2mm from end)
    tip_x = ARM_X0 + ARM_L - 2.0
    pin_sk = Cylinder(radius=PIN_D / 2, height=ARM_T + 2,
                      align=(Align.CENTER, Align.CENTER, Align.CENTER))
    pin_sk = pin_sk.translate((tip_x, 0, HUB_L / 2))
    arm = arm - pin_sk

    return hub + arm


def push_rod():
    """Connecting rod: 31mm body + 3mm pin sockets at each end."""
    rod = Box(ROD_L, ROD_W, ROD_T,
              align=(Align.MIN, Align.CENTER, Align.MIN))
    # Pin sockets at each end (Z-direction, 2.5mm from each end)
    for px in [2.5, ROD_L - 2.5]:
        sk = Cylinder(radius=PIN_D / 2, height=ROD_T + 2,
                      align=(Align.CENTER, Align.CENTER, Align.CENTER))
        sk = sk.translate((px, 0, ROD_T / 2))
        rod = rod - sk
    return rod


if PART == 0:
    arm = crank_arm().translate((0, 0, SHAFT_Z))
    rod = push_rod().translate((0, ARM_W + 5, EXIT_Z))
    result = arm + rod
    print(f"Assembly: arm at z={SHAFT_Z}mm (servo shaft), rod at z={EXIT_Z}mm (exit slot)")
elif PART == 1:
    result = crank_arm()
    print("crank_arm: ~29x9x6mm, print flat (hub base on bed, arm extends in +X)")
elif PART == 2:
    result = push_rod()
    print("push_rod: 31x5x3mm, print flat")

show_object(result)
