# design/cs2_phone_pol.py -- v1: CS2 phone camera polarizer film frame
# ASCII-only comments (Windows cp1252 safe).
# Holds a 30x24mm polarizing film square against the iPhone 16 Pro back,
# covering the camera module. Completes the cross-pol system started by cs2_pol_clip.py.
#
# Cross-pol setup:
#   Aperture side: 30x24mm film in cs2_pol_clip (clips into platform aperture from below)
#   Camera side:   30x24mm film in THIS frame (held over phone camera by rubber band)
#   Film MUST be rotated 90 degrees relative to aperture film for cross-polarization.
#   Effect: kills specular glare on holographic/foil cards; diffuse detail passes through.
#
# Assembly: insert 30x24mm polarizing film into recess on phone-face side.
# Loop a 2mm rubber band through the 4 corner holes and stretch over phone corners.
# Centre frame over iPhone 16 Pro camera cluster (top-left of phone back).
# Rotate 90 degrees from the orientation used in cs2_pol_clip.
#
# Film size 30x24mm matches cs2_pol_clip -- cut both from the same polarizer sheet.
# Outer footprint 44x38mm matches cs2_pol_clip flange (matched set appearance).
#
# Bed check: 44x38x3mm -- fits Toybox 68x78x88mm usable easily.
# Print flat (3mm Z). 0.2mm layers. White PLA. No supports.

OUTER_W  = 44.0   # outer width (X) -- matches cs2_pol_clip flange width
OUTER_D  = 38.0   # outer depth (Y) -- matches cs2_pol_clip flange depth
FRAME_T  = 3.0    # total frame thickness (Z)

FILM_W   = 30.0   # film recess width (X) -- same cut as cs2_pol_clip
FILM_D   = 24.0   # film recess depth (Y)
FILM_T   = 1.5    # film recess depth (Z) -- film seats on 2mm annular ledge

BORE_W   = 26.0   # camera bore width (X) -- same as cs2_pol_clip bore
BORE_D   = 20.0   # camera bore depth (Y) -- cameras see through here

HOLE_D   = 4.0    # rubber-band corner hole diameter
HOLE_OFF = 5.0    # corner hole centre inset from each outer edge

# -- Frame body --
frame = Box(OUTER_W, OUTER_D, FRAME_T,
            align=(Align.CENTER, Align.CENTER, Align.MIN))

# -- Film recess: phone-face side (z=0..FILM_T); film sits on 2mm annular ledge --
film_pocket = Box(FILM_W, FILM_D, FILM_T + 1,
                  align=(Align.CENTER, Align.CENTER, Align.MIN))
frame = frame - film_pocket

# -- Camera bore: exposes cameras through frame (z=FILM_T..FRAME_T) --
bore = Box(BORE_W, BORE_D, FRAME_T - FILM_T + 1,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
bore = bore.translate((0, 0, FILM_T))
frame = frame - bore

# -- Corner holes for rubber band (4x); 2.83mm clearance from film pocket corners --
for sx in [-1, 1]:
    for sy in [-1, 1]:
        hole = Cylinder(radius=HOLE_D / 2, height=FRAME_T + 2,
                        align=(Align.CENTER, Align.CENTER, Align.MIN))
        hole = hole.translate((sx * (OUTER_W / 2 - HOLE_OFF),
                               sy * (OUTER_D / 2 - HOLE_OFF),
                               -1))
        frame = frame - hole

result = frame
show_object(result)
