# design/cs2_height_preview.py -- v1: CS2 platform height comparison scene
# ASCII-only comments (Windows cp1252 safe).
# NOT printable -- visualization only.
# Shows 3 CS2 assemblies side by side at PLAT_Z=100/125/150mm.
# Use to choose a print height before cutting wall sections.
#
# Wall sections available: 87mm bot + 87mm top = 174mm total.
# Valid bolt hole heights: 104, 129, 154, 169mm (platform bottom Z).
# Camera-to-card = PLAT_Z + PLAT_T - FLOOR_T = PLAT_Z + 4mm.
#   100mm -> 104mm  (ultra-close; use ultra-wide macro mode)
#   125mm -> 129mm  (standard recommended)
#   150mm -> 154mm  (wide field; good for full-card + context)
#   165mm -> 169mm  (near wall-top; maximum height)

OUTER_L = 97.0;  OUTER_W = 72.0;  OUTER_H = 50.0
SLOT_L  = 90.0;  SLOT_W  = 65.0;  FLOOR_T = 4.0
WALL_T  = 14.0;  WALL_H  = 174.0
PLAT_W  = 68.0;  PLAT_D  = 75.0;  PLAT_T  = 8.0
APT_W   = 36.0;  APT_D   = 30.0;  APT_Y   = 37.0
PHONE_W = 71.5;  PHONE_T = 8.25

WALL_CY = OUTER_W / 2 + WALL_T / 2 + 0.1
PLAT_CY = OUTER_W / 2 - PLAT_D / 2
APT_CY  = OUTER_W / 2 - APT_Y
SP = 140.0  # X spacing between assemblies

# -- Hopper shells (centred before X-offset) --
hop_outer = Box(OUTER_L, OUTER_W, OUTER_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
hop_inner = Box(SLOT_L, SLOT_W, OUTER_H - FLOOR_T + 1,
                align=(Align.CENTER, Align.CENTER, Align.MIN))
hop_inner = hop_inner.translate((0, 0, FLOOR_T))
hop_shell = hop_outer - hop_inner

hopper1 = hop_shell.translate((-SP, 0, 0))
hopper2 = hop_shell.translate((0,   0, 0))
hopper3 = hop_shell.translate(( SP, 0, 0))

# -- Wall columns --
wall_col = Box(OUTER_L, WALL_T, WALL_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
wall1 = wall_col.translate((-SP, WALL_CY, 0))
wall2 = wall_col.translate((0,   WALL_CY, 0))
wall3 = wall_col.translate(( SP, WALL_CY, 0))

# -- Platform at Z=100 (left) --
pz1 = 100.0
plat1 = Box(PLAT_W, PLAT_D, PLAT_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
plat1 = plat1.translate((-SP, PLAT_CY, pz1))
apt1 = Box(APT_W, APT_D, PLAT_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
apt1 = apt1.translate((-SP, APT_CY, pz1 - 1))
plat1 = plat1 - apt1
phone1 = Box(PHONE_W, PLAT_D, PHONE_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
phone1 = phone1.translate((-SP, PLAT_CY, pz1 + PLAT_T + 0.1))

# -- Platform at Z=125 (centre) --
pz2 = 125.0
plat2 = Box(PLAT_W, PLAT_D, PLAT_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
plat2 = plat2.translate((0, PLAT_CY, pz2))
apt2 = Box(APT_W, APT_D, PLAT_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
apt2 = apt2.translate((0, APT_CY, pz2 - 1))
plat2 = plat2 - apt2
phone2 = Box(PHONE_W, PLAT_D, PHONE_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
phone2 = phone2.translate((0, PLAT_CY, pz2 + PLAT_T + 0.1))

# -- Platform at Z=150 (right) --
pz3 = 150.0
plat3 = Box(PLAT_W, PLAT_D, PLAT_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
plat3 = plat3.translate((SP, PLAT_CY, pz3))
apt3 = Box(APT_W, APT_D, PLAT_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
apt3 = apt3.translate((SP, APT_CY, pz3 - 1))
plat3 = plat3 - apt3
phone3 = Box(PHONE_W, PLAT_D, PHONE_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
phone3 = phone3.translate((SP, PLAT_CY, pz3 + PLAT_T + 0.1))

result = (hopper1 + wall1 + plat1 + phone1 +
          hopper2 + wall2 + plat2 + phone2 +
          hopper3 + wall3 + plat3 + phone3)
show_object(result)
