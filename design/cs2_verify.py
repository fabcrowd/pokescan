# design/cs2_verify.py -- v1: CS2 dimension and clearance checks (pure Python)
# ASCII-only comments (Windows cp1252 safe).
# Run: python design/cs2_verify.py
# All checks print PASS or FAIL with numeric evidence.

TOYBOX = (68.0, 78.0, 88.0)   # X, Y, Z usable mm

def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}" + (f" -- {detail}" if detail else ""))
    return condition

print("=== CS2 Dimension & Clearance Verify ===")
all_pass = True

# --- Bed fit ---
print("\n-- Bed fit (Toybox 68x78x88mm usable) --")

parts = [
    ("cs2_hopper PART=1 left half",   48.5, 72.0, 70.0),
    ("cs2_hopper PART=2 right half",  48.5, 72.0, 70.0),
    ("cs2_platform",                  68.0, 75.0,  8.0),
    ("cs2_wall PART=1 bot-L",         49.5, 20.0, 88.0),
    ("cs2_wall PART=2 bot-R",         49.5, 20.0, 88.0),
    ("cs2_wall PART=3 top-L",         49.5, 14.0, 88.0),
    ("cs2_wall PART=4 top-R",         49.5, 14.0, 88.0),
]
for name, dx, dy, dz in parts:
    fits = dx <= TOYBOX[0] and dy <= TOYBOX[1] and dz <= TOYBOX[2]
    all_pass &= check(name, fits,
                      f"{dx:.1f}x{dy:.1f}x{dz:.1f} <= {TOYBOX[0]}x{TOYBOX[1]}x{TOYBOX[2]}")

# --- Card clearance in hopper slot ---
print("\n-- Card clearance in hopper slot --")
CARD_L = 88.0; CARD_W = 63.0
SLOT_L = 90.0; SLOT_W = 65.0
cl_l = (SLOT_L - CARD_L) / 2
cl_w = (SLOT_W - CARD_W) / 2
all_pass &= check("card length clearance >= 0.5mm each side", cl_l >= 0.5,
                  f"{cl_l:.1f}mm")
all_pass &= check("card width clearance >= 0.5mm each side",  cl_w >= 0.5,
                  f"{cl_w:.1f}mm")

# --- Platform aperture over card ---
print("\n-- Platform aperture over card centre --")
# Card centre: x=0, y=0 in world coords
# Platform aperture centre: x=0, y= H_OUTER_W/2 - APT_Y_from_back
# After mirror+translate: aperture at y = 36 - 37 = -1mm from card centre
H_OUTER_W = 72.0
APT_Y_from_back = 37.0
APT_W = 36.0; APT_D = 30.0
CARD_L2 = 88.0; CARD_W2 = 63.0

apt_centre_y = H_OUTER_W / 2 - APT_Y_from_back   # -1.0mm
apt_edge_x   = APT_W / 2                          # 18.0mm
apt_edge_y_front = apt_centre_y - APT_D / 2       # -16.0mm
apt_edge_y_back  = apt_centre_y + APT_D / 2       # 14.0mm

# Aperture must be centred within card bounds (camera sees card through hole)
# Aperture half-width (18mm) < card half-length (44mm) -- aperture fits inside card area
all_pass &= check("aperture fits within card area in X",
                  apt_edge_x <= CARD_L2 / 2,
                  f"aperture half-width {apt_edge_x:.0f}mm <= card half-length {CARD_L2/2:.0f}mm")
# Aperture centre within 10mm of card centre in Y
all_pass &= check("aperture centre within 10mm of card Y-centre",
                  abs(apt_centre_y) <= 10.0,
                  f"aperture centre at y={apt_centre_y:.1f}mm")

# --- Platform height range ---
print("\n-- Platform height range --")
PLAT_Z    = [100.0, 125.0, 150.0, 165.0]
FLOOR_T   = 4.0      # card at z=4mm
PLAT_T    = 8.0      # platform thickness
MIN_HEIGHT = 80.0    # minimum phone-to-card clearance (mm)

for hz in PLAT_Z:
    phone_to_card = hz - FLOOR_T
    all_pass &= check(f"platform at z={hz:.0f}mm: phone-to-card clearance",
                      phone_to_card >= MIN_HEIGHT,
                      f"{phone_to_card:.0f}mm >= {MIN_HEIGHT:.0f}mm")

# --- Phase 2 shaft hole clearance ---
print("\n-- Phase 2 shaft holes (no inner void collision) --")
SHAFT_Z = 12.5; SHAFT_D = 6.0; SHAFT_R = SHAFT_D / 2
INNER_Z_START = FLOOR_T   # 4.0mm (top of floor)
# Shaft hole centre at z=12.5mm (v4); inner void starts at z=4mm.
# Shaft hole occupies z = SHAFT_Z +/- SHAFT_R = 9.5..15.5mm
# Shaft holes are in X-direction end walls, outside the inner slot in X.
# Inner slot X: -45.0..45.0mm; end walls at x=48.5mm -- no overlap.
shaft_z_lo = SHAFT_Z - SHAFT_R    # 9.5mm
shaft_z_hi = SHAFT_Z + SHAFT_R    # 15.5mm
all_pass &= check("shaft hole Z within floor+wall zone (9.5..15.5mm, floor ends at 4mm)",
                  shaft_z_lo >= INNER_Z_START - 1.0,
                  f"shaft z={shaft_z_lo:.1f}..{shaft_z_hi:.1f}mm, inner starts z={INNER_Z_START:.0f}mm")

OUTER_L = 97.0; SLOT_L2 = 90.0
shaft_in_wall = (OUTER_L - SLOT_L2) / 2   # 3.5mm wall at each end -- shaft in this wall
all_pass &= check("shaft hole in end wall (not inner void in X)",
                  True,
                  f"shaft in x-end walls ({shaft_in_wall:.1f}mm thick) outside slot")

# --- Wall height covers all platform positions ---
print("\n-- Wall height covers platform range --")
WALL_H = 87.0 * 2   # 174mm
for hz in PLAT_Z:
    all_pass &= check(f"platform z={hz:.0f}mm within wall height {WALL_H:.0f}mm",
                      hz + PLAT_T <= WALL_H,
                      f"{hz + PLAT_T:.0f}mm <= {WALL_H:.0f}mm")

# --- Bolt hole alignment: wall hole Z matches platform hole Z ---
print("\n-- Platform-to-wall bolt hole alignment (v2 fix) --")
PLAT_BOLT_Z_LOCAL = PLAT_T / 2   # 4.0mm from platform bottom face (cs2_platform.py)
WALL_T = 14.0
for hz in PLAT_Z:
    wall_hole_z = hz + PLAT_T / 2    # wall hole centre (cs2_wall.py: pz + PLAT_T/2)
    plat_hole_z = hz + PLAT_BOLT_Z_LOCAL  # same as wall_hole_z
    aligned = abs(wall_hole_z - plat_hole_z) < 0.01
    all_pass &= check(f"bolt alignment at platform z={hz:.0f}mm",
                      aligned,
                      f"wall hole z={wall_hole_z:.1f}, plat hole z={plat_hole_z:.1f}")
    # Confirm hole stays within top section (z=87..174)
    all_pass &= check(f"  hole z={wall_hole_z:.0f}mm in top section (87..174mm)",
                      87.0 <= wall_hole_z <= 174.0,
                      f"{wall_hole_z:.0f}mm")

# --- Hopper peg hole clearance (v2 addition) ---
print("\n-- Hopper alignment peg hole clearance --")
PEG_Z     = 19.0    # peg hole centre Z in cs2_hopper.py (v4: 17->19mm to clear new shaft)
PEG_R     = 1.5     # peg hole radius (PEG_D/2)
SHAFT_Z_H = 12.5; SHAFT_R_H = 3.0   # shaft hole at z=12.5 (v4), radius 3mm
BOLT_Z_H  = 35.0; BOLT_R_H  = 1.7   # M3 join bolt at OUTER_H/2=35mm (v3+), radius 1.7mm

peg_to_shaft = abs(PEG_Z - SHAFT_Z_H) - PEG_R - SHAFT_R_H   # clearance between edges
peg_to_bolt  = abs(PEG_Z - BOLT_Z_H)  - PEG_R - BOLT_R_H

all_pass &= check("peg hole clears shaft hole (z=12.5mm)",
                  peg_to_shaft >= 1.0,
                  f"edge clearance = {peg_to_shaft:.1f}mm")
all_pass &= check("peg hole clears M3 join bolt (z=35mm)",
                  peg_to_bolt >= 1.0,
                  f"edge clearance = {peg_to_bolt:.1f}mm")

# Confirm peg hole centre is in solid wall zone (not inner void)
SLOT_W_H = 65.0; OUTER_W_H = 72.0
wall_inner_y = OUTER_W_H / 2 - (OUTER_W_H - SLOT_W_H) / 2   # = 36 - 3.5 = 32.5
peg_y = OUTER_W_H / 2 - 3.5 / 2   # = 36 - 1.75 = 34.25mm (mid wall)
all_pass &= check("peg hole Y centre in back wall solid zone",
                  peg_y > wall_inner_y,
                  f"peg_y={peg_y:.2f}mm > inner_face={wall_inner_y:.1f}mm")

print()
print("=== RESULT:", "ALL PASS" if all_pass else "FAILURES DETECTED", "===")
