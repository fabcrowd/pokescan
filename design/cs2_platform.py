# design/cs2_platform.py -- v2: CS2 phone platform (camera shelf)
# ASCII-only comments (Windows cp1252 safe).
# Flat shelf the phone rests on face-down. Camera looks through aperture at card below.
# Attaches to cs2_wall.py back wall via 2x M3 bolts in T-slots (height adjustable).
#
# iPhone 16 Pro (71.5mm wide) overhangs 1.75mm each side -- acceptable.
# Camera aperture 36x30mm centred at x=0, y=37mm from back edge.
#
# Bed check: 68 x 75 x 8mm -- fits Toybox 68x78x88mm usable exactly (X at limit).
# Print flat (8mm Z up). No supports needed.

PLAT_W   = 68.0     # platform width (X) -- matches Toybox X limit
PLAT_D   = 75.0     # platform depth (Y, front-to-back)
PLAT_T   = 8.0      # platform thickness (Z)

# Camera aperture (sized for iPhone 16 Pro ultra-wide + main lens coverage)
APT_W    = 36.0     # aperture width (X)
APT_D    = 30.0     # aperture depth (Y)
APT_Y    = 37.0     # aperture centre Y from back edge (phone camera position)

# Back edge M3 bolt holes -- Y-direction, mate with cs2_wall.py Y-direction holes
BOLT_X   = 22.0     # bolt hole X offset from centre (each side) -- matches PLAT_X in wall
BOLT_D   = 3.4      # M3 clearance hole diameter

# Front chamfer to register phone (prevents phone from sliding forward)
CHAM     = 2.0      # chamfer height on front top edge

PART = 0

# -- Platform body --
plat = Box(PLAT_W, PLAT_D, PLAT_T,
           align=(Align.CENTER, Align.MIN, Align.MIN))

# -- Camera aperture: centred at x=0, y=APT_Y from back edge --
apt = Box(APT_W, APT_D, PLAT_T + 2,
          align=(Align.CENTER, Align.CENTER, Align.MIN))
apt = apt.translate((0, APT_Y, -1))
plat = plat - apt

# -- M3 bolt holes through platform back edge in Y direction --
# Bolt goes horizontally from back face (y=0) 15mm into platform body.
# Hole centre at z=PLAT_T/2 so it aligns with the corresponding wall hole.
# Assembly: bolt enters platform from y=0, passes through wall (14mm), nut on back.
for sx in [-1, 1]:
    bh = Cylinder(radius=BOLT_D / 2, height=15.0,
                  align=(Align.CENTER, Align.CENTER, Align.MIN))
    bh = bh.rotate(Axis.X, 90)   # now in Y direction
    bh = bh.translate((sx * BOLT_X, 0, PLAT_T / 2))
    plat = plat - bh

# -- Front edge lip (2mm tall, 3mm deep) to register phone and stop forward slide --
lip = Box(PLAT_W, 3.0, CHAM, align=(Align.CENTER, Align.MAX, Align.MAX))
lip = lip.translate((0, PLAT_D, PLAT_T))
plat = plat + lip

result = plat
show_object(result)
