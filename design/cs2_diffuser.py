# design/cs2_diffuser.py -- v1: CS2 torch diffuser plate
# ASCII-only comments (Windows cp1252 safe).
# Sits on platform top face between platform and phone.
# iPhone 16 Pro torch fires sideways/obliquely; this white plate catches that light
# and scatters it back into the hopper, producing soft diffuse fill for the card.
#
# How it works:
#   Phone torch fires at white PLA surface -> scatters in all directions
#   Scattered light enters hopper through the slot opening -> illuminates card evenly
#   Camera sees through the 36x30mm aperture (hole cuts through plate at same position
#   as platform aperture, so diffuser is invisible in the frame)
#   Result: replaces harsh single-point torch with large-area soft-box equivalent
#
# Use with or without the cross-pol accessories:
#   Standard cards: diffuser alone, no pol clip needed
#   Holo/foil cards: diffuser + cs2_pol_clip + cs2_phone_pol for maximum glare kill
#
# Assembly: set diffuser flat on platform top; phone rests on diffuser.
# Adds 1.5mm to phone height -> negligible focus shift (<1.2% at 125mm distance).
# Aperture position matches platform exactly (APT_Y=37mm from back edge).
#
# Bed check: 68x75x1.5mm -- X is at Toybox 68mm usable limit; use brim to prevent warp.
# Print flat (1.5mm Z = 7-8 layers at 0.2mm). 0.15mm layers for smoother scatter surface.
# Material: WHITE PLA ONLY -- any colour kills diffusion. Glossy white works too.
# No supports needed. Brim strongly recommended (large flat thin part prone to warping).

PLAT_W   = 68.0    # plate width (X) -- exactly matches cs2_platform.py PLAT_W
PLAT_D   = 75.0    # plate depth (Y) -- matches cs2_platform.py PLAT_D
DIFF_T   = 1.5     # plate thickness (Z); 1.5mm = ~7 layers; enough for light scatter

APT_W    = 36.0    # camera aperture width (X) -- matches cs2_platform.py APT_W
APT_D    = 30.0    # camera aperture depth (Y)
APT_Y    = 37.0    # aperture centre distance from plate back edge -- matches platform

# Aperture centre in plate-centred coordinates:
#   plate back edge = +PLAT_D/2 = +37.5mm from centre
#   aperture centre = 37.5 - APT_Y = +0.5mm (nearly at plate centre, slightly toward back)
APT_CY   = PLAT_D / 2 - APT_Y    # = +0.5mm

# -- Diffuser plate (X/Y centred, Z from zero up) --
plate = Box(PLAT_W, PLAT_D, DIFF_T,
            align=(Align.CENTER, Align.CENTER, Align.MIN))

# -- Camera aperture: same geometry as cs2_platform.py to align when stacked --
apt = Box(APT_W, APT_D, DIFF_T + 2,
          align=(Align.CENTER, Align.CENTER, Align.MIN))
apt = apt.translate((0, APT_CY, -1))
plate = plate - apt

result = plate
show_object(result)
