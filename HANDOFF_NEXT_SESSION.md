# Next Session Handoff — CS2 Card Scanner

**Date:** 2026-06-29  
**Repo:** https://github.com/fabcrowd/pokescan  
**Local:** `C:\repos\card scanner`

---

## Current Status: PRINT-READY

All CS2 STLs are validated and in `design/output/`. The hopper was just updated to v5.

---

## What was done this session

### cs2_hopper.py v5 (reprint needed — v5 replaces v3 in design/output/)

Two batches of changes:

**v4 (Phase-2 CAD):**
- `SHAFT_Z` 8.0 → 12.5mm — roller v2 has OD=17mm; shaft at 12.5mm centres roller bottom at card floor z=4mm
- `EXIT_W` 15mm → 90mm — card body (88mm) can now exit through the front slot (was arm-port only)
- Peg holes z=17 → 19mm — maintains 2mm clearance from new shaft top

**v5 (Manual operation):**
- Thumb-push hole in back wall: 25mm wide × 14mm tall, z=2..16mm, centred at x=0
- Starts 2mm below card floor — thumb slips UNDER the card and pushes its face, not its narrow edge (card-safe)
- Spans the x=0 seam; each printed half gets a 12.5×14mm notch that forms the full hole when assembled
- Phase-2 parts (servo, roller, bracket, crank arm, push rod) remain optional bolt-ons

**Verify:** `py design/cs2_verify.py` → 31/31 PASS

---

## Print queue (what to print next)

| Part | File | Notes |
|------|------|-------|
| **Hopper halves (REPRINT)** | `cs2_hopper_left.stl` + `cs2_hopper_right.stl` | v5 — thumb-push hole in back wall |

All other STLs are unchanged from previous prints. Only the hopper halves need reprinting.

**Print settings for hopper:** Black PLA, upright orientation, standard quality, 20% infill.

---

## Manual scan workflow (Phase 1, no automation)

1. Drop card into top of hopper (centering insert helps funnel it in)
2. Scan with iPhone on platform above
3. Push thumb through back-wall hole → card slides forward → exits through 90mm front slot
4. Next card

---

## Phase-2 open items (deferred — reprint planned)

All Phase-2 CAD is done. Hardware still needed before Phase-2 can run:
- SG90 micro-servo (1×)
- 6mm steel shaft, 30mm long (1×)
- 3mm steel pins, 10mm long (2×)
- M3×8 SHCS bolts (4×) for motor bracket

See `docs/phase-2-cs2-motor.md` for full assembly sequence.

---

## Key files

| File | Purpose |
|------|---------|
| `design/cs2_hopper.py` | Hopper v5 — **reprint halves** |
| `design/cs2_verify.py` | 31-check verification: `py design/cs2_verify.py` |
| `design/output/*.stl` | All print-ready STLs |
| `HANDOFF.md` | Full iteration history and part table |
| `docs/cs2_assembly.md` | Assembly guide |
| `docs/phase-2-cs2-motor.md` | Phase-2 servo spec (all CAD done) |

---

## To rebuild STLs after any design change

```bash
# Run AgentCAD via MCP (Claude Code), or locally:
uvx --from build123d --with bd_warehouse python design/cs2_hopper.py
py design/cs2_verify.py
```
