# design/photo_box.py -- v3: CS2 Scan Hood (open-frame LED ring, two-piece)
# ASCII-only comments (Windows cp1252 safe).
#
# Sits on table around the card scan area, providing diffuse ring lighting.
# White PLA interior scatters LED light evenly across the 63x88mm card face.
#
# Interior: card 63mm (X), snug fit; card 88mm (Y) + 3mm each end = 94mm Y.
# Long walls (X-side): WALL_T=2mm (Toybox X-constrained; EXT_W=67mm < 68mm).
# End walls (Y-side): END_T=5mm, allows 10mm x 3mm LED channel on inner face.
# Exterior per half: 67mm (X) x 52mm (Y) x 40mm (Z) -- fits Toybox 68x78x88mm.
#
# LED strip: standard 5050 SMD, 10mm wide, 2.5mm thick (+ 0.5mm clearance = 3mm deep slot).
# LED channel on inner face of end wall, running full INT_W (63mm) at z=25..35mm.
# Strip faces inward/downward, light reflects off white long walls onto card.
#
# Hood is open top (camera looks in) and open bottom (card lies underneath).
# Two halves join at card Y-center (Y=0). Join face is open.
# Alignment: Ø3mm pin sockets at x=+/-22mm on join face, 5mm deep per half.
#
# PART=0  assembled view: both halves (Compound)
# PART=1  single half (print 2x, white PLA, flat on bed)
#         bed footprint: 67x52x40mm -- fits Toybox 68x78x88mm (1mm X margin) [OK]

CARD_W  = 63.0   # card width (X)
CARD_L  = 88.0   # card length (Y)
WALL_T  = 2.0    # long wall (X-side) thickness -- limited by Toybox X
END_T   = 5.0    # end wall (Y-side) thickness -- allows LED channel
HOOD_H  = 40.0   # hood height (Z); open top + open bottom

INT_W      = CARD_W              # interior X = 63mm
INT_L      = CARD_L + 6.0       # interior Y = 94mm (3mm clearance each end)
INT_HALF_L = INT_L / 2.0        # per-half interior Y = 47mm
EXT_W      = INT_W + 2 * WALL_T # exterior X = 67mm (1mm Toybox margin)
HALF_L     = INT_HALF_L + END_T # per-half exterior Y = 52mm (fits 78mm Toybox)

# LED channel cut into inner face of end wall.
# 5050 single-row strip: 10mm wide, 2.5mm thick. Channel is 10mm H x 3mm deep.
LED_H   = 10.0   # channel height in Z (matches 10mm strip width)
LED_D   = 3.0    # channel depth into end wall (5mm wall, 2mm material behind)
LED_Z0  = HOOD_H - LED_H - 5   # channel bottom Z = 25mm (top at 35mm, 5mm from top for structure)

PIN_D   = 3.0    # alignment pin diameter
PIN_X   = 22.0   # pin X offset from center

PART = 0


def hood_half():
    """One half of the scan hood. Spans Y=0..HALF_L (join face open at Y=0).
    End wall (Y=HALF_L face, END_T=5mm) has 63mm x 10mm x 3mm LED channel.
    Long walls (X-sides, WALL_T=2mm) are plain for maximum diffusion area.
    """
    with BuildPart() as p:
        # Outer shell: 67 x 52 x 40mm
        Box(EXT_W, HALF_L, HOOD_H,
            align=(Align.CENTER, Align.MIN, Align.MIN))

        # Interior cavity: open at join face (extends past y=0), closed at far end.
        # Stops at y=INT_HALF_L so the END_T=5mm end wall is preserved.
        with Locations((0, -0.5, -0.5)):
            Box(INT_W, INT_HALF_L + 0.5, HOOD_H + 1.0,
                align=(Align.CENTER, Align.MIN, Align.MIN), mode=Mode.SUBTRACT)

        # LED channel on inner face of end wall.
        # Inner face at y=INT_HALF_L=47mm; channel goes 3mm deeper to y=50mm.
        # Runs full INT_W in X; positioned at z=LED_Z0..LED_Z0+LED_H (z=25..35mm).
        # Leaves 2mm material behind (END_T - LED_D = 5 - 3 = 2mm).
        with Locations((0, INT_HALF_L, LED_Z0)):
            Box(INT_W + 0.5, LED_D, LED_H,
                align=(Align.CENTER, Align.MIN, Align.MIN), mode=Mode.SUBTRACT)

        # Alignment pin sockets at join face (Y=0), mid-height.
        # Each socket 5mm deep (into the solid end of the long walls).
        for px in [-PIN_X, PIN_X]:
            with Locations((px, 0.0, HOOD_H / 2.0)):
                Cylinder(PIN_D / 2.0, 5.0,
                         align=(Align.CENTER, Align.CENTER, Align.CENTER),
                         rotation=(90, 0, 0), mode=Mode.SUBTRACT)

    return p.part


if PART == 0:
    h1 = hood_half()
    h2 = mirror(h1, about=Plane.XZ)
    result = Compound(children=[h1, h2])

elif PART == 1:
    result = hood_half()

show_object(result)
