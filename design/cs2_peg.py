# design/cs2_peg.py -- v1: CS2 hopper alignment peg print plate
# ASCII-only comments (Windows cp1252 safe).
# 4x cylindrical alignment pegs for the cs2_hopper halves join.
# Each peg: 3mm dia x 10mm long (5mm into each half seam hole).
# Hole diameter in hopper is 3.0mm -- peg is 2.95mm for reliable fit.
# Print 4 pegs per plate; use 2 per hopper assembly (front + back wall).
#
# Bed check: 22 x 22 x 10mm -- fits Toybox 68x78x88mm usable easily.
# Print upright (10mm Z). No supports. 4 walls + 60% infill for strength.
# Material: PETG or PLA; PETG preferred for slight flex (better snap fit).

PEG_D   = 2.95   # slightly under 3.0mm hole for clearance fit; adjust +/-0.05 as needed
PEG_L   = 10.0   # total length: 5mm into each half (matches PEG_L=5 in cs2_hopper.py x2)
SPACING = 7.0    # centre-to-centre spacing in X and Y

# -- 4 pegs in 2x2 grid --
pegs = []
for ix in range(2):
    for iy in range(2):
        p = Cylinder(radius=PEG_D / 2, height=PEG_L,
                     align=(Align.CENTER, Align.CENTER, Align.MIN))
        p = p.translate((ix * SPACING - SPACING / 2,
                         iy * SPACING - SPACING / 2,
                         0))
        pegs.append(p)

result = pegs[0] + pegs[1] + pegs[2] + pegs[3]
show_object(result)
