# design/cs2_pol_clip.py -- v1: CS2 platform polarizer film clip
# ASCII-only comments (Windows cp1252 safe).
# Press-fit clip for the cs2_platform.py camera aperture (36x30mm).
# Holds a 30x24mm polarizing film square for cross-polarization glare control.
# Particularly useful for holographic/foil cards -- kills specular hot-spots.
#
# Assembly: insert from below platform; plug (35.6x29.6mm) press-fits into
# the 36x30mm aperture. Flange (44x38x2mm) sits on platform bottom face.
# Top of plug is flush with platform top surface (where the phone rests).
# Insert 30x24mm polarizing film into the recessed pocket at plug top.
# Mount a matching film over the phone camera lens (cut from same polarizer sheet,
# rotate 90 degrees) for cross-polarization.
#
# Bed check: 44 x 38 x 8mm -- fits Toybox 68x78x88mm usable.
# Print flat (8mm Z up). 0.15mm layers for good film-seat surface finish.
# Material: white PLA (diffuses light; keep light path clean).

PLUG_W   = 35.6    # plug width (X) -- 0.2mm clearance in 36mm platform aperture
PLUG_D   = 29.6    # plug depth (Y) -- 0.2mm clearance in 30mm platform aperture
PLUG_H   = 6.0     # plug height (Z) -- platform thickness (8mm) minus flange (2mm)

FLANGE_W = 44.0    # flange width (X) -- 4mm ledge each side beyond plug
FLANGE_D = 38.0    # flange depth (Y) -- 4mm ledge each side beyond plug
FLANGE_T = 2.0     # flange thickness (Z) -- rests on platform bottom face

FILM_W   = 30.0    # film recess width (X) -- matches standard polarizer sheet cut
FILM_D   = 24.0    # film recess depth (Y)
FILM_T   = 1.5     # film recess depth (Z) -- pocket at top of plug; film sits here

BORE_W   = 26.0    # light-path bore width (X) -- clear field of view
BORE_D   = 20.0    # light-path bore depth (Y)

# -- Flange base (rests on platform bottom face) --
flange = Box(FLANGE_W, FLANGE_D, FLANGE_T,
             align=(Align.CENTER, Align.CENTER, Align.MIN))

# -- Plug (inserts into platform aperture from below) --
plug = Box(PLUG_W, PLUG_D, PLUG_H,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
plug = plug.translate((0, 0, FLANGE_T))

clip = flange + plug

# -- Film recess pocket at top of plug (film inserted face-up, toward camera) --
film_pocket = Box(FILM_W, FILM_D, FILM_T + 1,
                  align=(Align.CENTER, Align.CENTER, Align.MAX))
film_pocket = film_pocket.translate((0, 0, FLANGE_T + PLUG_H))
clip = clip - film_pocket

# -- Light-path bore: through flange and plug up to film floor --
# Annular 2mm ledge at film floor supports the film (bore narrower than film recess)
bore_h = FLANGE_T + PLUG_H - FILM_T   # z=0 to z=6.5mm
bore = Box(BORE_W, BORE_D, bore_h + 1,
           align=(Align.CENTER, Align.CENTER, Align.MIN))
bore = bore.translate((0, 0, -1))
clip = clip - bore

result = clip
show_object(result)
