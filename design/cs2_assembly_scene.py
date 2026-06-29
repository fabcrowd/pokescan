# design/cs2_assembly_scene.py -- v1: CS2 full assembly scene (NOT printable)
# ASCII-only comments (Windows cp1252 safe).
# Visual validation of CS2 spatial relationships: hopper, wall, platform, phone, card.
# Shows assembly at PLAT_Z=125mm (mid-range; valid heights: 100/125/150/165mm).
#
# Key clearances verified by this scene:
#   aperture centre at y=-1mm vs card centre at y=0 (1mm offset -- within 30mm aperture OK)
#   phone (71.5mm wide) overhangs platform (68mm) by 1.75mm each side -- OK
#   camera to card distance at PLAT_Z=125mm: 125+8-4 = 129mm (within macro range OK)
#   wall front face at y=36.1mm (0.1mm gap to hopper/platform back face -- no coplanar face)
#
# Run: py design/cs2_assembly_scene.py (or via AgentCAD for preview)
# Do NOT export as STL -- assembly scene only.

OUTER_L  = 97.0     # hopper assembled length (X) -- cs2_hopper.py OUTER_L
OUTER_W  = 72.0     # hopper assembled width (Y) -- cs2_hopper.py OUTER_W
OUTER_H  = 50.0     # hopper height (Z)
SLOT_L   = 90.0     # inner card slot length (X)
SLOT_W   = 65.0     # inner card slot width (Y)
FLOOR_T  = 4.0      # card face Z in hopper (floor thickness)

WALL_T   = 14.0     # wall depth (Y) -- cs2_wall.py WALL_T
WALL_H   = 174.0    # wall total height (Z, 2 sections of 87mm each)

PLAT_W   = 68.0     # platform width (X) -- cs2_platform.py PLAT_W
PLAT_D   = 75.0     # platform depth (Y) -- cs2_platform.py PLAT_D
PLAT_T   = 8.0      # platform thickness (Z)
APT_W    = 36.0     # camera aperture width (X)
APT_D    = 30.0     # camera aperture depth (Y)
APT_Y    = 37.0     # aperture centre Y from platform back edge

PLAT_Z   = 125.0    # platform bottom Z (preview height; adjust to 100/150/165 to taste)

PHONE_W  = 71.5     # iPhone 16 Pro width (X)
PHONE_T  = 8.25     # iPhone 16 Pro thickness (Z; sits face-down on platform)

CARD_L   = 88.0     # card long axis (X)
CARD_W   = 63.0     # card short axis (Y)
CARD_T   = 0.8      # card thickness

# -- Assembly positions (world coords, card centre = origin at z=0) --
# Wall front face: y = OUTER_W/2 + 0.1 = 36.1mm (0.1mm gap prevents coplanar boolean)
WALL_CY  = OUTER_W / 2 + WALL_T / 2 + 0.1   # = 43.1mm wall body centre Y
# Platform centre Y: back edge at y=36mm, extends PLAT_D toward camera
PLAT_CY  = OUTER_W / 2 - PLAT_D / 2          # = -1.5mm (platform straddles card centre)
# Aperture centre Y: 37mm from platform back edge
APT_CY   = OUTER_W / 2 - APT_Y               # = -1.0mm (1mm in front of card centre)

# -- Card at hopper floor (0.1mm clearance above floor for clean boolean) --
card = Box(CARD_L, CARD_W, CARD_T,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
card = card.translate((0, 0, FLOOR_T + 0.1))

# -- Hopper open-top shell --
hopper = Box(OUTER_L, OUTER_W, OUTER_H,
             align=(Align.CENTER, Align.CENTER, Align.MIN))
inner = Box(SLOT_L, SLOT_W, OUTER_H - FLOOR_T + 1,
            align=(Align.CENTER, Align.CENTER, Align.MIN))
inner = inner.translate((0, 0, FLOOR_T))
hopper = hopper - inner

# -- Wall column (back of hopper, 0.1mm gap to hopper back face) --
wall = Box(OUTER_L, WALL_T, WALL_H,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
wall = wall.translate((0, WALL_CY, 0))

# -- Platform at PLAT_Z with camera aperture --
plat = Box(PLAT_W, PLAT_D, PLAT_T,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
plat = plat.translate((0, PLAT_CY, PLAT_Z))
apt_cut = Box(APT_W, APT_D, PLAT_T + 2,
              align=(Align.CENTER, Align.CENTER, Align.MIN))
apt_cut = apt_cut.translate((0, APT_CY, PLAT_Z - 1))
plat = plat - apt_cut

# -- Phone body (simplified to platform depth; face-down, 0.1mm above platform top) --
# Phone shown truncated to PLAT_D=75mm in Y for clarity; avoids wall overlap.
# Full iPhone 16 Pro length is 149.6mm; phone overhangs platform in both Y directions.
phone = Box(PHONE_W, PLAT_D, PHONE_T,
            align=(Align.CENTER, Align.CENTER, Align.MIN))
phone = phone.translate((0, PLAT_CY, PLAT_Z + PLAT_T + 0.1))

result = hopper + wall + plat + card + phone
show_object(result)
