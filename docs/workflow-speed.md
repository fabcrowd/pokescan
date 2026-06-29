# CS2 Card Scanner — Workflow Speed & Capacity

## Card Capacity

### Current hopper (OUTER_H = 50mm)

| Parameter | Value |
|-----------|-------|
| Total hopper height | 50mm |
| Floor thickness (FLOOR_T) | 4mm |
| Interior stack height | 46mm |
| Card thickness (unsleeved) | 0.32mm |
| Theoretical max | 46 / 0.32 = **144 cards** |
| Practical capacity (~85%) | **~120 cards** |
| Toybox Z margin remaining | 88 − 50 = **38mm spare** |

### Recommended hopper v3 (OUTER_H = 70mm)

Increasing OUTER_H from 50 to 70mm in `cs2_hopper.py` is safe:

| Parameter | Value |
|-----------|-------|
| Total hopper height | 70mm |
| Interior stack height | 66mm |
| Theoretical max | 66 / 0.32 = **206 cards** |
| Practical capacity (~80%) | **~160 cards** |
| Toybox Z check | 70mm < 88mm usable ✓ |
| Half-piece dims | 48.5 × 72 × 70mm — fits 68×78×88mm bed ✓ |
| Wall interface | unchanged — wall starts at z=0 (table), unaffected |

Card Slinger 3.0 benchmarks 150+ cards. At OUTER_H=70 the CS2 system hits ~160 cards practical, clearing the benchmark with margin.

## Toss-and-Scan Workflow (with cs2_centering_insert)

The centering insert (req 1) enables a high-speed toss-and-scan loop that eliminates careful card placement:

1. **Load**: drop a stack of cards (up to ~120 or ~160 cards with v3 hopper) into the funnel mouth (103×78mm opening). Cards self-center into the 90×65mm slot and settle onto the card floor at z=4mm.
2. **Scan**: trigger the iPhone 16 Pro camera — scanner app captures the top card (or bottom card via mirror, depending on setup).
3. **Eject** (Phase 2): motor drives the Phase-2 rubber-gasket roller. The separator (cs2_separator.py) gates the exit to one card at a time. Card exits through the 15×4mm slot into a collection tray.
4. **Repeat**: next card is now at the scan position. Repeat scan + eject.

Without Phase-2 motor: remove the top card by hand after each scan. Still faster than hand-placing each card due to the bulk-load step.

## Cards-Per-Hour Estimate

| Mode | Assumption | Rate |
|------|------------|------|
| Phase 1 (manual eject) | 4s per card (scan + hand remove) | **~900 cards/hour** |
| Phase 2 (motorised) | 2s per card (scan + auto eject) | **~1800 cards/hour theoretical** |
| Phase 2 realistic | occasional mismatch, rescan, jam | **~600–900 cards/hour** |
| Card Slinger 3.0 (reference) | claimed ~150 cards in under 5 min | **~1800 cards/hour** |

At Phase 2 realistic rates (~750 cards/hour), a 160-card load empties in ~13 minutes. A typical MTG collection of 3000 cards scans in ~4 hours.

## Recommendation: implement OUTER_H=70 (req 5)

All safety checks pass:
- Fits Toybox bed (70mm < 88mm Z usable)
- Half-piece within bed limits (48.5×72×70mm)
- Wall column interface unchanged (starts at z=0 table, not attached to hopper top)
- cs2_verify.py height check uses `OUTER_H` variable, not a literal — should update cleanly

Implement as `cs2_hopper.py` v3. Re-export and reprint hopper halves.
