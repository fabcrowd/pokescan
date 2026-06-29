# design/cs2_final_render.py -- full CS2 system with all accessories
# Not printable -- visualization only.
# Shows: hopper + wall + platform (125mm) + pol_clip + diffuser + phone + card

OUTER_L  = 97.0;  OUTER_W = 72.0;  OUTER_H = 50.0
SLOT_L   = 90.0;  SLOT_W  = 65.0;  FLOOR_T = 4.0
WALL_T   = 14.0;  WALL_H  = 174.0
PLAT_W   = 68.0;  PLAT_D  = 75.0;  PLAT_T  = 8.0
APT_W    = 36.0;  APT_D   = 30.0;  APT_Y   = 37.0
PLAT_Z   = 125.0
FLG_W    = 44.0;  FLG_D   = 38.0;  FLG_T   = 2.0
PLG_W    = 35.6;  PLG_D   = 29.6;  PLG_H   = 6.0
DIFF_T   = 1.5
PHONE_W  = 71.5;  PHONE_T = 8.25
CARD_L   = 88.0;  CARD_W  = 63.0;  CARD_T  = 0.8

WALL_CY  = OUTER_W / 2 + WALL_T / 2 + 0.1
PLAT_CY  = OUTER_W / 2 - PLAT_D / 2
APT_CY   = OUTER_W / 2 - APT_Y        # -1.0mm

# -- Card --
card = Box(CARD_L, CARD_W, CARD_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
card = card.translate((0, 0, FLOOR_T + 0.1))

# -- Hopper (open-top shell) --
hopper = Box(OUTER_L, OUTER_W, OUTER_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
inner = Box(SLOT_L, SLOT_W, OUTER_H - FLOOR_T + 1, align=(Align.CENTER, Align.CENTER, Align.MIN))
inner = inner.translate((0, 0, FLOOR_T))
hopper = hopper - inner

# -- Wall column (0.1mm gap prevents coplanar face with hopper) --
wall = Box(OUTER_L, WALL_T, WALL_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
wall = wall.translate((0, WALL_CY, 0))

# -- Platform with aperture --
plat = Box(PLAT_W, PLAT_D, PLAT_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
plat = plat.translate((0, PLAT_CY, PLAT_Z))
apt_cut = Box(APT_W, APT_D, PLAT_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
apt_cut = apt_cut.translate((0, APT_CY, PLAT_Z - 1))
plat = plat - apt_cut

# -- Pol_clip: flange below platform + plug in aperture --
pol_flange = Box(FLG_W, FLG_D, FLG_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
pol_flange = pol_flange.translate((0, APT_CY, PLAT_Z - FLG_T))
pol_plug = Box(PLG_W, PLG_D, PLG_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
pol_plug = pol_plug.translate((0, APT_CY, PLAT_Z))
pol_clip = pol_flange + pol_plug

# -- Diffuser plate on platform top (0.1mm gap) --
diff = Box(PLAT_W, PLAT_D, DIFF_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
diff = diff.translate((0, PLAT_CY, PLAT_Z + PLAT_T + 0.1))
diff_apt = Box(APT_W, APT_D, DIFF_T + 2, align=(Align.CENTER, Align.CENTER, Align.MIN))
diff_apt = diff_apt.translate((0, APT_CY, PLAT_Z + PLAT_T - 1))
diff = diff - diff_apt

# -- Phone body (on diffuser, 0.1mm gap) --
phone = Box(PHONE_W, PLAT_D, PHONE_T, align=(Align.CENTER, Align.CENTER, Align.MIN))
phone = phone.translate((0, PLAT_CY, PLAT_Z + PLAT_T + DIFF_T + 0.2))

result = hopper + wall + plat + pol_clip + diff + phone + card
show_object(result)
