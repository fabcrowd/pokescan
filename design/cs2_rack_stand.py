# design/cs2_rack_stand.py -- v2: CS2 Rack-and-Pinion Adjustable Phone Stand
# Sits behind the CS2 hopper (foot front face flush with hopper back face at y=36mm).
# Carriage slides on 2x rack sections; phone platform cantilevers forward so camera
# sits at y≈3mm (card center is y=0mm; 3mm off is negligible on a 63mm-wide card).
# Cam lock: M3x6 button-head bolt on carriage -X face; tighten to fix height.
#
# Mechanism from rack_stand_v2.py (unchanged): RACK_PITCH=4mm, 8-tooth pinion, 30mm knob.
# Only foot proportions, PHONE_OFFSET_Y, and phone_platform aperture changed for CS2.
#
# CHANGES v1→v2:
#   - Fixed PHONE_OFFSET_Y: -38.5→-35.5  (M3 bolt holes were 1mm outside platform body)
#   - Added PART selector: 0=assembly, 1=rack_section, 2=foot, 3=carriage, 4=knob,
#                          5=platform, 6=fit_test
#   - Added fit_test(): 4 tolerance features in a 42x36x20mm block, print FIRST
#
# Camera-to-card height range (card floor at z=4mm):
#   Minimum: FOOT_H + CAR_H + PHONE_T - 4 = 50+50+5-4 = 101mm
#   Maximum: FOOT_H + 2*BODY_H + PHONE_T - 4 = 50+160+5-4 = 211mm
#   CS2 target scan range 104..169mm is fully covered.
#
# Bed check (all parts fit Toybox 68x78x88mm usable):
#   fit_test:       42 x 36 x 20mm (flat)    -- print FIRST ✓
#   rack_section:   26 x 24 x 84mm (upright) -- 26x24 footprint ✓
#   stand_foot:     50 x 40 x 50mm (flat)    -- 50x40 footprint ✓
#   phone_carriage: 37 x 47 x 50mm (flat)    -- 37x47 footprint ✓
#   pinion_knob:    30 x 30 x 42mm (upright) -- 30x30 footprint ✓
#   phone_platform: 65 x 75 x 17mm (flat)    -- 65x75 footprint (tight: 1.5mm/side in X) ✓

import math

# =============================================================================
# CONSTANTS
# =============================================================================

PART = 0   # 0=assembly  1=rack_section  2=foot  3=carriage  4=knob  5=platform  6=fit_test

# -- Rack geometry (unchanged from rack_stand_v2) --
RACK_PITCH  = 4.0
TOOTH_W     = 2.0
GAP_W       = 2.4    # tooth gap 0.4mm wider than tooth for FDM clearance
TOOTH_DEPTH = 2.0
BODY_H      = 80.0   # section body; 80/4=20 teeth, integer multiple of RACK_PITCH
PEG_H       = 4.0    # D-peg height;  4/4=1 pitch, integer multiple of RACK_PITCH
SECTION_H   = BODY_H + PEG_H   # 84mm <= 88mm Toybox Z ✓
N_TEETH     = int(BODY_H / RACK_PITCH)
RAIL_W      = 26.0
RAIL_D      = 24.0

# -- D-peg / socket --
PEG_D    = 10.0
PEG_FLAT = 3.0    # flat on +Y side: anti-rotation key, rack-face indicator
PEG_CL   = 0.35  # clearance radius added to socket

# -- Carriage --
CAR_H    = 50.0
CAR_WALL = 5.0
CAR_CL   = 0.6   # 0.3mm/side clearance on rail faces
CAR_BORE_W = RAIL_W + 2 * CAR_CL
CAR_BORE_D = RAIL_D + TOOTH_DEPTH + CAR_CL

# -- Pinion / knob --
PINION_N    = 8
PINION_PD   = PINION_N * RACK_PITCH / math.pi   # ~10.19mm pitch diameter
PINION_R    = PINION_PD / 2
PINION_LEN  = RAIL_W - 4     # 22mm; hub spans carriage interior
KNOB_D      = 30.0
KNOB_H      = 12.0
KNOB_AXLE_D = 5.0
KNOB_STUB_L = (CAR_BORE_W + 2 * CAR_WALL) / 2 - PINION_LEN / 2   # ~7.6mm

# -- Lock bolt (M3x6 button-head ISO 7380 -- DO NOT use M3x8, shank punches through rail) --
LOCK_BORE_R   = 1.4   # 2.8mm pilot for M3 self-tapping
LOCK_CK_R     = 3.0   # 6.0mm countersink = M3 button-head body diameter
LOCK_CK_DEPTH = 1.7   # M3 button-head head height; bolt engagement = 5-1.7=3.3mm (6.6 threads)
LOCK_Z_FRAC   = 0.75

# -- M3 platform bolts (M3x8 socket-head) --
M3_PILOT_R = 1.25   # 2.5mm self-tapping pilot into PLA
M3_CLEAR_R = 1.7    # 3.4mm clearance through platform floor

# -- Stand foot (CS2: taller than rs2 so rack starts at hopper-top level z=50mm) --
FOOT_W = 50.0   # X: narrower than hopper (97mm); independent column, not a bracket
FOOT_D = 40.0   # Y depth
FOOT_H = 50.0   # Z: matches CS2 hopper height

# -- CS2 hopper geometry (reference only) --
HOPPER_L    = 97.0
HOPPER_W    = 72.0
HOPPER_H    = 50.0
HOPPER_BACK = HOPPER_W / 2   # 36mm

# -- Column Y: foot center immediately behind hopper back face --
STAND_Y = HOPPER_BACK + FOOT_D / 2   # 56mm

# -- Phone platform --
APT_W     = 36.0    # camera aperture width (CS2 spec from cs2_platform.py)
APT_D     = 30.0    # camera aperture depth
PHONE_W   = 65.0    # platform X; iPhone 16 Pro (71.5mm) gets 3.25mm margin/side
PHONE_D   = 75.0    # platform Y depth
PHONE_LIP = 12.0
PHONE_T   = 5.0

# PHONE_OFFSET_Y: platform Y offset from STAND_Y (in platform local frame).
# v1 was -38.5 which put M3 holes at y=0 just 1mm outside the back edge (y=-1mm).
# Fixed to -35.5: back edge now at y=+2mm, M3 holes 2mm inside material.
# Camera at y = STAND_Y + (-35.5) - PHONE_D/2 + 20 = 56-35.5-37.5+20 = 3mm (≈0 ✓)
PHONE_OFFSET_Y = -35.5


# =============================================================================
# D-PEG / SOCKET HELPERS  (must be called inside an active BuildPart context)
# =============================================================================

def _d_peg(z_base):
    r = PEG_D / 2
    with Locations((0, 0, z_base)):
        Cylinder(r, PEG_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    flat_y0   = r - PEG_FLAT
    box_ysize = PEG_FLAT + 2.0
    box_yc    = flat_y0 + box_ysize / 2
    with Locations((0, box_yc, z_base + PEG_H / 2)):
        Box(PEG_D + 2, box_ysize, PEG_H + 2, mode=Mode.SUBTRACT)


def _d_socket(z_base):
    sr = PEG_D / 2 + PEG_CL
    with Locations((0, 0, z_base)):
        Cylinder(sr, PEG_H, align=(Align.CENTER, Align.CENTER, Align.MIN),
                 mode=Mode.SUBTRACT)
    flat_y0   = PEG_D / 2 - PEG_FLAT + PEG_CL
    box_ysize = PEG_FLAT - PEG_CL + 2.0
    box_yc    = flat_y0 + box_ysize / 2
    with Locations((0, box_yc, z_base + PEG_H / 2)):
        Box(PEG_D + 4, box_ysize, PEG_H + 2, mode=Mode.SUBTRACT)


# =============================================================================
# PARTS
# =============================================================================

def rack_section():
    """Identical section x2. Rack teeth on +Y face. Print upright. 26x24x84mm."""
    EMBED = 0.5
    with BuildPart() as p:
        Box(RAIL_W, RAIL_D, BODY_H,
            align=(Align.CENTER, Align.CENTER, Align.MIN))
        for i in range(N_TEETH):
            z_c = i * RACK_PITCH + TOOTH_W / 2
            with Locations((0, RAIL_D / 2 + (TOOTH_DEPTH - EMBED) / 2, z_c)):
                Box(RAIL_W, TOOTH_DEPTH + EMBED, TOOTH_W)
        _d_peg(BODY_H)
        _d_socket(0.0)
        for _tz in [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]:
            with Locations((RAIL_W / 2 - 0.25, 0, _tz)):
                Box(0.5, RAIL_D + 2, 1.0,
                    align=(Align.CENTER, Align.CENTER, Align.CENTER),
                    mode=Mode.SUBTRACT)
    return p.part


def stand_foot():
    """Column base. Front face (y=-FOOT_D/2) abuts hopper back face (y=36mm).
    D-peg on top receives rack section 1. Print flat. 50x40x50mm."""
    with BuildPart() as p:
        Box(FOOT_W, FOOT_D, FOOT_H,
            align=(Align.CENTER, Align.CENTER, Align.MIN))
        _d_peg(FOOT_H)
        for _fx, _fy in [(-18.0, -12.0), (18.0, -12.0), (-18.0, 12.0), (18.0, 12.0)]:
            with Locations((_fx, _fy, 0.5)):
                Cylinder(2.0, 1.0,
                         align=(Align.CENTER, Align.CENTER, Align.CENTER),
                         mode=Mode.SUBTRACT)
    return p.part


def phone_carriage():
    """Slides on rack. Pinion bore overlaps rail bore creating tooth engagement zone.
    M3 lock on -X face. Print flat. ~37x47x50mm."""
    hub_r         = PINION_R + TOOTH_DEPTH
    outer_W       = CAR_BORE_W + 2 * CAR_WALL
    bore_cy       = TOOTH_DEPTH / 2
    bore_half_D   = (RAIL_D + TOOTH_DEPTH + CAR_CL) / 2
    pinion_cy     = RAIL_D / 2 + PINION_R
    pinion_bore_r = hub_r + CAR_CL
    pinion_z      = CAR_H / 2
    bore_bot      = bore_cy - bore_half_D
    car_y_plus    = pinion_cy + pinion_bore_r + CAR_WALL
    car_y_minus   = abs(bore_bot) + CAR_WALL
    outer_D       = car_y_plus + car_y_minus
    box_cy        = (car_y_plus - car_y_minus) / 2
    lock_x_face   = -outer_W / 2
    lock_y_val    = bore_cy
    lock_z_val    = CAR_H * LOCK_Z_FRAC
    lock_depth    = CAR_WALL + 1.0
    lock_cx       = lock_x_face + lock_depth / 2
    ck_cx         = lock_x_face + LOCK_CK_DEPTH / 2

    with BuildPart() as p:
        with Locations((0, box_cy, 0)):
            Box(outer_W, outer_D, CAR_H,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
        with Locations((0, bore_cy, CAR_H / 2)):
            Box(CAR_BORE_W, bore_half_D * 2, CAR_H + 2, mode=Mode.SUBTRACT)
        with Locations((0, bore_cy, CAR_H - 2)):
            Box(CAR_BORE_W + 3, bore_half_D * 2 + 3, 4, mode=Mode.SUBTRACT)
        with Locations((0, pinion_cy, pinion_z)):
            Cylinder(pinion_bore_r, outer_W + 2,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER),
                     rotation=(0, 90, 0), mode=Mode.SUBTRACT)
        with Locations((lock_cx, lock_y_val, lock_z_val)):
            Cylinder(LOCK_BORE_R, lock_depth,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER),
                     rotation=(0, 90, 0), mode=Mode.SUBTRACT)
        with Locations((ck_cx, lock_y_val, lock_z_val)):
            Cylinder(LOCK_CK_R, LOCK_CK_DEPTH,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER),
                     rotation=(0, 90, 0), mode=Mode.SUBTRACT)
        for _mx in [outer_W / 2 - 2.1, -(outer_W / 2 - 2.1)]:
            with Locations((_mx, 0.0, CAR_H)):
                Cylinder(M3_PILOT_R, 5.0,
                         align=(Align.CENTER, Align.CENTER, Align.MAX),
                         mode=Mode.SUBTRACT)
        with Locations((outer_W / 2, bore_cy, CAR_H)):
            Box(1.5, 5.0, 3.0,
                align=(Align.MAX, Align.CENTER, Align.MAX),
                mode=Mode.SUBTRACT)
        with Locations((0, -car_y_minus + 1.0, CAR_H / 2)):
            Box(20.0, 2.0, 15.0,
                align=(Align.CENTER, Align.CENTER, Align.CENTER),
                mode=Mode.SUBTRACT)
    return p.part


def pinion_knob():
    """8-tooth pinion hub + axle stub + 30mm thumb disc. Print upright. ~30x30x42mm."""
    hub_r   = PINION_R + TOOTH_DEPTH
    disc_z0 = PINION_LEN + KNOB_STUB_L

    with BuildPart() as p:
        Cylinder(hub_r, PINION_LEN,
                 align=(Align.CENTER, Align.CENTER, Align.MIN))
        for i in range(PINION_N):
            angle = i * 360.0 / PINION_N
            cx = PINION_R * math.cos(math.radians(angle))
            cy = PINION_R * math.sin(math.radians(angle))
            with Locations((cx, cy, PINION_LEN / 2)):
                Box(GAP_W, hub_r * 2 + 2, PINION_LEN + 2,
                    rotation=(0, 0, angle), mode=Mode.SUBTRACT)
        with Locations((0, 0, PINION_LEN)):
            Cylinder(KNOB_AXLE_D / 2 + 0.25, KNOB_STUB_L,
                     align=(Align.CENTER, Align.CENTER, Align.MIN))
        Cylinder(KNOB_AXLE_D / 2, PINION_LEN - 1,
                 align=(Align.CENTER, Align.CENTER, Align.MIN),
                 mode=Mode.SUBTRACT)
        with Locations((0, 0, disc_z0)):
            Cylinder(KNOB_D / 2, KNOB_H,
                     align=(Align.CENTER, Align.CENTER, Align.MIN))
        for i in range(12):
            angle = i * 30.0
            gx = (KNOB_D / 2 - 1.5) * math.cos(math.radians(angle))
            gy = (KNOB_D / 2 - 1.5) * math.sin(math.radians(angle))
            with Locations((gx, gy, disc_z0 + KNOB_H / 2)):
                Cylinder(2.5, KNOB_H + 2,
                         align=(Align.CENTER, Align.CENTER, Align.CENTER),
                         mode=Mode.SUBTRACT)
    return p.part


def phone_platform():
    """Phone mounting plate. Bolts to carriage top with 2x M3x8 socket-head.
    Camera aperture 36x30mm at front. Print face-down (lips point up). 65x75x17mm.
    M3 holes at y=0 (local frame) = 2mm inside back edge at y=+2mm. ✓"""
    po = PHONE_OFFSET_Y
    _car_outer_half = (CAR_BORE_W + 2 * CAR_WALL) / 2 - 2.1

    with BuildPart() as p:
        with Locations((0, po, 0)):
            Box(PHONE_W, PHONE_D, PHONE_T,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
        with Locations((0, po - PHONE_D / 2 + PHONE_LIP / 2, PHONE_T)):
            Box(PHONE_W, PHONE_LIP, PHONE_LIP,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
        with Locations((0, po + PHONE_D / 2 - PHONE_LIP / 2, PHONE_T)):
            Box(PHONE_W, PHONE_LIP, PHONE_LIP,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
        with Locations((0, po + PHONE_D / 2 - PHONE_LIP / 2, PHONE_T + PHONE_LIP / 2)):
            Box(10.0, PHONE_LIP + 2, 8.0,
                align=(Align.CENTER, Align.CENTER, Align.CENTER),
                mode=Mode.SUBTRACT)
        with Locations((0, po - PHONE_D / 2 + APT_D / 2, PHONE_T / 2)):
            Box(APT_W, APT_D, PHONE_T + 2, mode=Mode.SUBTRACT)
        for px in [-PHONE_W / 2 + 8, PHONE_W / 2 - 8]:
            with Locations((px, po - PHONE_D / 2 + PHONE_LIP / 2, PHONE_T + PHONE_LIP)):
                Cylinder(2.5, 8.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
        for px in [-PHONE_W / 2 + 8, PHONE_W / 2 - 8]:
            with Locations((px, po + PHONE_D / 2 - PHONE_LIP / 2, PHONE_T + PHONE_LIP)):
                Cylinder(2.5, 8.0, align=(Align.CENTER, Align.CENTER, Align.MIN))
        for _mx in [_car_outer_half, -_car_outer_half]:
            with Locations((_mx, 0.0, PHONE_T / 2)):
                Cylinder(M3_CLEAR_R, PHONE_T + 2,
                         align=(Align.CENTER, Align.CENTER, Align.CENTER),
                         mode=Mode.SUBTRACT)
            with Locations((_mx, 0.0, PHONE_T)):
                Cylinder(3.0, 3.5,
                         align=(Align.CENTER, Align.CENTER, Align.MAX),
                         mode=Mode.SUBTRACT)
    return p.part


def fit_test():
    """Tolerance block -- print FIRST before committing to full parts.
    4 features in one 42x36x20mm block (fits Toybox 68x78x88mm flat).

    Feature 1 -- Rail bore pocket (top face, 12mm deep):
      Slide a rack_section in from above. Should move freely, ~0.3mm play per face.
      Too tight: increase CAR_CL from 0.6 to 0.7mm and reprint carriage.

    Feature 2 -- D-peg socket (bottom face):
      Press stand_foot D-peg up from below. Should click snug with thumb pressure.
      Too tight: increase PEG_CL from 0.35 to 0.45mm.

    Feature 3 -- Lock bolt pocket (-X face, z=4mm):
      Thread M3x6mm button-head (ISO 7380) from -X. Head must sit flush in 6mm CK
      recess; shank self-taps 4.3mm without splitting PLA.
      Strips: heat-set M3 insert instead, or reduce LOCK_BORE_R by 0.05mm.

    Feature 4 -- Mini rack stub (+Y face, 3 teeth at z=5/9/13mm):
      Press pinion_knob hub tangentially and rotate. Teeth must slip into gaps freely.
      Binds: increase GAP_W from 2.4 to 2.6mm and reprint knob only.
    """
    W, D_b, H = 42.0, 36.0, 20.0
    bore_cy = TOOTH_DEPTH / 2
    bore_hD = (RAIL_D + TOOTH_DEPTH + CAR_CL) / 2

    with BuildPart() as p:
        Box(W, D_b, H, align=(Align.CENTER, Align.CENTER, Align.MIN))

        with Locations((0, bore_cy, H)):
            Box(CAR_BORE_W, bore_hD * 2, 12,
                align=(Align.CENTER, Align.CENTER, Align.MAX),
                mode=Mode.SUBTRACT)

        _d_socket(0.0)

        _lck = CAR_WALL + 1.0
        with Locations((-W / 2 + LOCK_CK_DEPTH / 2, 0.0, 4.0)):
            Cylinder(LOCK_CK_R, LOCK_CK_DEPTH,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER),
                     rotation=(0, 90, 0), mode=Mode.SUBTRACT)
        with Locations((-W / 2 + _lck / 2, 0.0, 4.0)):
            Cylinder(LOCK_BORE_R, _lck,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER),
                     rotation=(0, 90, 0), mode=Mode.SUBTRACT)

        _EMBED = 0.5
        for _tz in [5.0, 9.0, 13.0]:
            with Locations((0, D_b / 2 + (TOOTH_DEPTH - _EMBED) / 2, _tz)):
                Box(RAIL_W, TOOTH_DEPTH + _EMBED, TOOTH_W)

    return p.part


# =============================================================================
# PART SELECTION
# =============================================================================

if PART == 0:
    # -- Assembly scene --
    sec      = rack_section()
    foot     = stand_foot()
    carriage = phone_carriage()
    knob     = pinion_knob()
    platform = phone_platform()

    foot_placed = foot.translate((0, STAND_Y, 0))
    sec1 = sec.translate((0, STAND_Y, FOOT_H))
    sec2 = sec.translate((0, STAND_Y, FOOT_H + BODY_H))

    car_z = FOOT_H + 30
    carriage_placed = carriage.translate((0, STAND_Y, car_z))
    platform_placed = platform.translate((0, STAND_Y, car_z + CAR_H))

    pinion_cy_val = RAIL_D / 2 + PINION_R
    knob_placed = (knob
        .rotate(Axis.Y, 90)
        .translate((-PINION_LEN / 2, STAND_Y + pinion_cy_val, car_z + CAR_H / 2))
    )

    hopper_rep = Box(HOPPER_L, HOPPER_W, HOPPER_H,
                     align=(Align.CENTER, Align.CENTER, Align.MIN))

    IPHONE_L = 149.6; IPHONE_W = 71.5; IPHONE_T = 8.25
    platform_floor_z = car_z + CAR_H + PHONE_T
    phone_front_y    = STAND_Y + PHONE_OFFSET_Y - PHONE_D / 2
    phone_cy         = phone_front_y + IPHONE_L / 2
    phone_body = Box(IPHONE_W, IPHONE_L, IPHONE_T,
                     align=(Align.CENTER, Align.CENTER, Align.MIN)).translate(
        (0, phone_cy, platform_floor_z))

    card_rep = Box(63.0, 88.0, 0.8,
                   align=(Align.CENTER, Align.CENTER, Align.MIN)).translate(
        (0, 0, 4.0))

    result = Compound(children=[
        hopper_rep,
        foot_placed, sec1, sec2,
        carriage_placed, platform_placed, knob_placed,
        phone_body, card_rep,
    ])

    print(f"STAND_Y: {STAND_Y}mm  (foot front face at Y={STAND_Y - FOOT_D/2}mm = hopper back ✓)")
    print(f"Camera world Y: {phone_front_y + 20:.1f}mm  (card centre = 0mm)")
    print(f"Camera-to-card range: {FOOT_H + CAR_H + PHONE_T - 4:.0f}..{FOOT_H + 2*BODY_H + PHONE_T - 4:.0f}mm")

elif PART == 1:
    result = rack_section()
    print("rack_section: 26x24x84mm, print upright (2x required)")

elif PART == 2:
    result = stand_foot()
    print("stand_foot: 50x40x50mm, print flat")

elif PART == 3:
    result = phone_carriage()
    print("phone_carriage: ~37x47x50mm, print flat (bore-side up)")

elif PART == 4:
    result = pinion_knob()
    print("pinion_knob: ~30x30x42mm, print upright (hub down)")

elif PART == 5:
    # Centre platform in Y for printing (shift by -PHONE_OFFSET_Y)
    result = phone_platform().translate((0, -PHONE_OFFSET_Y, 0))
    print("phone_platform: 65x75x17mm, print face-down (lips and pegs point up)")
    print(f"  Camera aperture 36x30mm at front; M3 bolt holes at y={-PHONE_OFFSET_Y:.1f}mm (centred print)")

elif PART == 6:
    result = fit_test()
    print("fit_test: 42x36x20mm, print flat -- do this FIRST")
    print("  F1 rail bore (top), F2 D-socket (bottom), F3 lock bolt (-X), F4 rack stub (+Y)")

show_object(result)
