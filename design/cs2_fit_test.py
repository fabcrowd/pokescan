# design/cs2_fit_test.py -- v1: CS2 fit test print plate
# ASCII-only comments (Windows cp1252 safe).
# Print this before the full part set -- tests 2 critical fits in one small plate.
#
# (A) Hole test block (x=-22..-4): 18x16x20mm
#     Lower slot at z=8mm : thread M3x20mm bolt through both faces (X direction).
#     Upper slot at z=14mm: insert 3mm dowel (from cs2_peg.stl) into left face.
#     PASS: bolt threads freely; dowel slides in with light thumb pressure.
#     FAIL/ADJUST: dowel too tight -> increase PEG_D in cs2_peg.py +0.05mm; reprint.
#
# (B) Platform aperture ring (x=-2..+42): 44x38x8mm with 36x30mm opening.
#     Press cs2_pol_clip plug (35.6x29.6mm) into the 36x30mm aperture from below.
#     PASS: plug press-fits with firm thumb pressure and stays without glue.
#     FAIL too tight -> increase PLUG_W/PLUG_D in cs2_pol_clip.py +0.1mm each; reprint.
#     FAIL too loose -> decrease PLUG_W/PLUG_D in cs2_pol_clip.py -0.1mm each; reprint.
#
# Bed check: 64x38x20mm -- fits Toybox 68x78x88mm usable OK.
# Print flat (20mm Z). 0.2mm layers. Same PLA colour as the target parts -- PLA shrink
# varies by pigment. No supports. 3 walls, 20% infill.

# --- (A) Hole test block ---
M3_D   = 3.4     # M3 clearance hole diameter (cs2_hopper.py M3_D)
PEG_D  = 3.0     # peg hole diameter (cs2_hopper.py PEG_D; accepts 2.95mm peg)
PEG_L  = 8.0     # peg blind hole depth -- deeper than 5mm half-pocket for full test
BLK_W  = 18.0    # block width (X)
BLK_D  = 16.0    # block depth (Y)
BLK_H  = 20.0    # block height (Z)
BLK_CX = -13.0   # block centre X; block spans x=-22..-4

block = Box(BLK_W, BLK_D, BLK_H,
            align=(Align.CENTER, Align.CENTER, Align.MIN))
block = block.translate((BLK_CX, 0, 0))

# M3 through-bolt hole in X at z=8mm (matches hopper join bolt height OUTER_H/2=25mm scaling)
bolt_hole = Cylinder(radius=M3_D / 2, height=BLK_W + 2,
                     align=(Align.CENTER, Align.CENTER, Align.CENTER))
bolt_hole = bolt_hole.rotate(Axis.Y, 90)
bolt_hole = bolt_hole.translate((BLK_CX, 0, 8.0))
block = block - bolt_hole

# 3mm blind peg hole from left face (x=-22) at z=14mm; 8mm deep
peg_hole = Cylinder(radius=PEG_D / 2, height=PEG_L,
                    align=(Align.CENTER, Align.CENTER, Align.MIN))
peg_hole = peg_hole.rotate(Axis.Y, 90)
peg_hole = peg_hole.translate((-22.0, 0, 14.0))
block = block - peg_hole

# --- (B) Platform aperture ring ---
APT_W  = 36.0    # platform aperture width (cs2_platform.py APT_W)
APT_D  = 30.0    # platform aperture depth (cs2_platform.py APT_D)
FLG_W  = 44.0    # ring outer width (cs2_pol_clip.py FLANGE_W)
FLG_D  = 38.0    # ring outer depth (cs2_pol_clip.py FLANGE_D)
RING_T = 8.0     # ring thickness = platform thickness (cs2_platform.py PLAT_T)
RNG_CX = 20.0    # ring centre X; ring spans x=-2..+42

ring = Box(FLG_W, FLG_D, RING_T,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
ring = ring.translate((RNG_CX, 0, 0))

aperture = Box(APT_W, APT_D, RING_T + 2,
               align=(Align.CENTER, Align.CENTER, Align.MIN))
aperture = aperture.translate((RNG_CX, 0, -1))
ring = ring - aperture

result = block + ring
show_object(result)
