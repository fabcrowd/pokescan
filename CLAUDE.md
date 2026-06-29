# Card Scanner — Agent Instructions

Project: **plastic-modular copy stand** with **adjustable cam-lever head**, **cross-polar dial**, and **flow-through card lane** (Phase-2 feeder anchors) for iPhone 16 Pro card scanning on a **Toybox** (75 × 80 × 90 mm bed). Read `README.md` and `restart.md` for build docs; this file tells agents **which MCP tools and skills to use** and **constraints that must not be violated**.

---

## MCP vs skills (don’t conflate these)

They are **different systems**:

| | **MCP servers** | **Agent skills** |
|---|-----------------|------------------|
| **What** | External tool servers (browser, APIs, databases) | Markdown playbooks (`SKILL.md`) |
| **How the agent uses them** | `CallMcpTool` → named tools (`navigate_page`, etc.) | Read `SKILL.md` from disk when the task matches |
| **Config file (Cursor)** | `~/.cursor/mcp.json` | `~/.cursor/skills-cursor/`, `~/.claude/skills/`, user rules |
| **This project** | See below — **Chrome DevTools only** | Listed in [Applicable agent skills](#applicable-agent-skills) |

**MCP does not “query skills” in Cursor.** Skills are file-based instructions injected into the agent context; the agent opens the relevant `SKILL.md` directly.

### What is actually connected in Cursor

| Source | Server | Purpose |
|--------|--------|---------|
| **Plugin MCP Servers** (Cursor UI) | **mcpmarket-my-toolkit** | OAuth login to your MCPmarket toolkit. **Auth only — this toolkit exposes 0 MCP tools** (`tools/list` → `[]`). |
| `~/.cursor/mcp.json` | **agentcad**, **chrome-devtools**, **chrome-devtools-ext** | CAD loop + browser automation |

Do **not** duplicate `mcpmarket-my-toolkit` in `mcp.json` — Cursor’s plugin integration already registers it (you’ll see it twice if both are present).

### How MCPmarket skills reach Cursor (mirrors Claude Code)

Claude Code runs `shared/sync.sh` on session start via a plugin hook. This repo does the same:

| Piece | Path |
|-------|------|
| Session hook | `.cursor/hooks.json` → `sessionStart` |
| Sync script | `.cursor/hooks/sync-mcpmarket-skills.sh` |
| Synced skills land in | `~/.cursor/skills/mcpmarket/{slug}/SKILL.md` |
| Plugin source (credentials) | `~/.claude/plugins/mcpmarket-my-toolkit/` |

Manual sync anytime:

```bash
"C:\Program Files\Git\bin\bash.exe" .cursor/hooks/sync-mcpmarket-skills.sh
```

**Why Cursor shows “No tools, prompts, or resources” for MCPmarket:** skills are **filesystem playbooks**, not MCP tools. The MCP connection is for auth/session; baseline skills are pulled via REST (`/api/v1/plugin/baseline`) and written to disk — same as Claude Code.

---

## Hard constraints (never ignore)

| Constraint | Value | Why |
|------------|-------|-----|
| Toybox build volume | **70 × 80 × 90 mm** (usable **68 × 78 × 88** in script) | Alpha 3 — split large parts |
| Target phone | **iPhone 16 Pro** | Camera opening, focus height, torch position |
| Lens → card distance | **≥ 260 mm** at lowest clamp (3 seg min ≈ **296 mm**) | Nested joint stack in `report_height()` |
| Card size | **63 × 88 mm** raw **unsleeved** | Lane + future feeder; sleeves add glare |
| Glare | Off-axis torch + **rotatable cross-pol dial** | Holo specular; fixed polarizer is insufficient |
| Print material | **Matte PLA 1.75 mm** — white/coconut scan surfaces, **black** light-path parts | Toybox spools; gloss reintroduces flare |
| Current architecture | **Split base/shelf** (dovetail + T&G) + adjustable head + gravity lane | `verify_assembly()` required; Phase-2a spec in `docs/phase-2a-manual-feeder.md` |
| Feeder future-proofing | `card_lane_left/right` open both ends; M3 bosses on base + lane | Do not fill hopper/bin/servo volumes in Phase-1 CAD |

When changing geometry, always run:

```bash
py build_woodstand.py
```

Success = every part `[OK]` on bed bbox, `watertight=True`, and **`verify_assembly()` passes**.

---

## MCP servers

### Claude Code (`.mcp.json` in project root)

| Server | Tool prefix | Use for this project |
|--------|-------------|----------------------|
| **agentcad** | `agentcad_*` | build123d run/render/inspect loop — execute Python CAD scripts and receive PNG previews + metrics |

### Cursor (`~/.cursor/mcp.json` + plugin)

| Source | Server | Purpose |
|--------|--------|---------|
| `~/.cursor/mcp.json` | **agentcad** | build123d execute/render/export loop (same as Claude Code) |
| `~/.cursor/mcp.json` | **chrome-devtools** | Web research: iPhone specs, glare techniques, reference stands |
| `~/.cursor/mcp.json` | **chrome-devtools-ext** | Default off — only for Chrome extension testing |
| Plugin (Cursor UI) | **mcpmarket-my-toolkit** | Auth only — 0 MCP tools exposed |

---

### AgentCAD — build123d visual feedback loop (Claude Code)

AgentCAD is an MCP server that lets Claude execute build123d Python scripts and receive rendered PNG previews after each run — no manual `preview_stl.py` step needed.

**Config:** already wired in `.mcp.json`. Claude Code auto-starts it via `uvx` on first use.

**When to use:** any time you are building or iterating on parts in `design/wheel_head.py` or any new build123d file. The render loop is the primary reason to use AgentCAD — you see geometry after every change without leaving the conversation.

**Workflow:**

```
agentcad_execute  ← run a Python build123d script
agentcad_render   ← get PNG preview of the resulting solid
agentcad_export   ← export STEP / STL / GLB
agentcad_diff     ← compare two design versions
```

**Key constraint:** AgentCAD scripts require **no imports** — build123d primitives are pre-injected. Scripts must return a `result` variable (a build123d `Part` or `Compound`).

**Example (screw shaft stub):**

```python
# No imports needed — build123d is pre-injected
core = Cylinder(radius=7.5, height=40, align=(Align.MIN, Align.MIN, Align.MIN))
result = core  # AgentCAD renders this
```

**Thread geometry** (`design/thread_geom.py` — single source of truth):

| Part | Method |
|------|--------|
| **Male** (shaft, stub_screw) | Core at `MALE_CORE_R` + `TrapezoidalThread(external=True)` |
| **Female** (nut, wheel, lock) | Pre-bore `NUT_BORE_R` + subtract `TrapezoidalThread(external=False, diameter=SCREW_OD+2×CL)` from ring |

```python
from bd_warehouse.thread import TrapezoidalThread, Thread
# Male shaft (in BuildPart with core cylinder):
TrapezoidalThread(diameter=18, pitch=5, thread_angle=30, length=40, external=True, interference=0.0)
# Female nut: pre-bore NUT_BORE_R, then subtract Thread(apex=NUT_BORE_R+SCREW_DEPTH, root=NUT_BORE_R, ...)
```

See `design/wheel_head_b123.py` and **build123d** skill `bd-warehouse-reference.md`.

### chrome-devtools workflow (Cursor — research)

1. `navigate_page` / `new_page` → target URL
2. `wait_for` → page ready
3. `take_snapshot` → extract facts (prefer over screenshot)
4. `take_screenshot` → when visual confirmation needed

**Before calling MCP tools:** read tool schemas under `mcps/user-chrome-devtools/tools/`.

### chrome-devtools-ext (Cursor)

Default **off**. Enable only when testing Chrome extensions or web-based scanner flows.

---

## Applicable agent skills

Use these skills when the task matches. Read the full `SKILL.md` before applying.

**Workflow reference:** [How to Use Claude AI for 3D Printing (2026)](https://3dprinteddecor.com/how-to-use-claude-for-3d-printing/) — verify before print, parameters-first, iterate in phases, paste errors back. Project rule: `.cursor/rules/card-scanner.mdc`.

### CAD tool hierarchy (this repo)

| Scope | Edit | Engine | Do **not** use |
|-------|------|--------|----------------|
| Stand parts (base, column — legacy head/lane until Phase 3 port) | `build_woodstand.py` | trimesh + manifold3d | OpenSCAD, CadQuery |
| **Wheel-head + redesign parts** (`design/wheel_head_b123.py`, future `design/photo_box.py`) | `design/*.py` | **build123d + bd_warehouse** — male `TrapezoidalThread`, female pre-bore + `Thread` groove | CadQuery helix; `TrapezoidalThread(external=False)` on solid ring |
| Legacy wheel-head (superseded) | `design/wheel_head.py` | CadQuery | Do not extend — use `wheel_head_b123.py` |
| New greenfield printable part (jig, bracket) | CadQuery via **parametric-3d-printing** | CadQuery | — |
| Simple one-off SCAD (user explicitly asks) | OpenSCAD skill | OpenSCAD | — |

**Run build123d scripts (no venv install):**

```bash
uvx --from build123d --with bd_warehouse --with trimesh python design/wheel_head_b123.py
```

**Skill:** read `build123d` skill before editing `design/*` — global: `~/.claude/plugins/cache/vibecad/build123d/*/skills/build123d/SKILL.md` (threads → `bd-warehouse-reference.md`).

**Claude Code:** AgentCAD via project `.mcp.json`. **Cursor:** AgentCAD via `~/.cursor/mcp.json` (reload MCP after config change). Fallback: `py scripts/preview_stl.py design/output/<part>.stl`.

**Audit pipeline:** `py scripts/audit_builds.py` — stand + wheel-head rebuild, mesh audit, verify_requirements. `--mesh-only` skips rebuilds.

After geometry changes: run audit → Creator Space slicer preview per README.

### Project skills (install via skillfish — do not vendor custom skills)

Research: [`docs/mcp-skills-research.md`](docs/mcp-skills-research.md)

Install upstream skills with [skillfish](https://github.com/knoxgraeme/skillfish) (MCPmarket ecosystem). `--project` writes **both** `.claude/skills/` (Claude Code) and `.cursor/skills/` (Cursor):

| Skill (upstream) | Install |
|------------------|---------|
| OpenSCAD 3D Modeler | `npx skillfish add mitsuhiko/agent-stuff openscad --project --yes` |
| 3D Printing workflow | `npx skillfish add chriscantey/skill-3d-printing --project --yes` |
| Spec-driven development | `npx skillfish add addyosmani/agent-skills spec-driven-development --project --yes` |
| Incremental implementation | `npx skillfish add addyosmani/agent-skills incremental-implementation --project --yes` |
| Planning / task breakdown | `npx skillfish add addyosmani/agent-skills planning-and-task-breakdown --project --yes` |

MCPmarket baseline sync (OAuth plugin): `~/.cursor/skills/mcpmarket/` via `.cursor/hooks/sync-mcpmarket-skills.sh`.

### Primary (global — use often)

| Skill | Path | When to use |
|-------|------|-------------|
| **grinding-until-pass** | `~/.claude/skills/grinding-until-pass/SKILL.md` | Iterate `build_woodstand.py` until all STLs pass bed check; fix `manifold3d`/trimesh/boolean errors in a fix→run loop |
| **build123d** | `~/.claude/plugins/cache/vibecad/build123d/*/skills/build123d/SKILL.md` | **All `design/*.py`** — threads via `bd_warehouse.TrapezoidalThread`; run with `uvx --from build123d --with bd_warehouse` |
| **create-rule** | `~/.cursor/skills-cursor/create-rule/SKILL.md` | Encode Toybox limits, iPhone 16 Pro optics, or Python CAD conventions in `.cursor/rules/*.mdc` |
| **canvas** | `~/.cursor/skills-cursor/canvas/SKILL.md` | Standalone deliverables: assembly exploded views, light-path diagrams, interactive cut-list / focus-distance calculators |

### Research & browser (MCP-backed)

| Skill | Path | When to use |
|-------|------|-------------|
| **chrome-devtools** | `~/.claude/skills/chrome-devtools/SKILL.md` | Live browser research via MCP: specs, photography guides, reference designs |
| **chrome-devtools-cli** | `~/.claude/skills/chrome-devtools-cli/SKILL.md` | Shell/CI scripts that call `chrome-devtools` CLI for repeatable research captures |
| **troubleshooting** | `~/.claude/skills/troubleshooting-chrome-devtools/SKILL.md` | MCP browser fails: `list_pages`, `navigate_page`, DevToolsActivePort, extension tools missing |
| **sync** (MCPmarket) | `~/.claude/plugins/mcpmarket-my-toolkit/skills/sync/SKILL.md` | Manual baseline pull (Claude Code). In Cursor, use `.cursor/hooks/sync-mcpmarket-skills.sh` instead. |

Synced MCPmarket skills for Cursor live at **`~/.cursor/skills/mcpmarket/`** (auto-sync on session start via `.cursor/hooks.json`).

### Secondary (situational)

| Skill | Path | When to use |
|-------|------|-------------|
| **create-skill** | `~/.cursor/skills-cursor/create-skill/SKILL.md` | Package a reusable **card-scanner-cad** or **toybox-export** skill after patterns stabilize |
| **create-hook** | `~/.cursor/skills-cursor/create-hook/SKILL.md` | Auto-run STL export after `build_woodstand.py` edits (optional automation) |
| **deep-bug-hunt** | `~/.claude/skills/deep-bug-hunt/SKILL.md` | Post-change audit of parametric script: silent geometry regressions, non-watertight exports, bed overflow |

---

## Skills NOT applicable (skip unless scope changes)

| Skill | Reason |
|-------|--------|
| tradingview-extract | Trading indicators — unrelated |
| proposed-changes-pnl-test | Trading PnL — unrelated |
| telegram-bot-architect | No bot in scope |
| chrome-extension-dev / extension-e2e-test | No extension unless explicitly added |
| babysit / split-to-prs | GitHub PR workflow — use only when opening PRs |
| sdk / automate / loop | Cursor SDK automations — not needed for CAD/print workflow |
| statusline / update-cursor-settings | IDE prefs — unrelated |
| parallel-exploring | Small repo; direct reads are enough |
| awesome-deep-research-agent | Survey-style research — overkill for hardware CAD |

---

## Agent task → tool mapping

| User asks for… | Use |
|----------------|-----|
| Design a **stand** part or tune assembly | **incremental-implementation** + edit `build_woodstand.py` + **grinding-until-pass** |
| Design / iterate **wheel-head** or **photo box** | Edit `design/wheel_head_b123.py` or `design/photo_box.py`; **build123d** skill + `TrapezoidalThread`; **AgentCAD MCP** (Claude Code) or `preview_stl.py` (Cursor) |
| Design a **new** printable part (not in stand / design scripts) | **spec-driven-development** → **parametric-3d-printing** (CadQuery) |
| Simple SCAD one-off (user asks OpenSCAD) | **openscad** skill |
| Split part for small bed | **3DPrinting** + `card_lane_*` pattern (butt-join segments) |
| Tune geometry / regenerate STLs | **incremental-implementation** + **grinding-until-pass** on `build_woodstand.py` |
| Full project build + audit | `py scripts/audit_builds.py` — rebuilds both scripts, repair pass, mesh audit, verify_requirements |
| Mesh status only (no rebuild) | `py scripts/audit_builds.py --mesh-only` or `py scripts/audit_meshes.py` |
| Adjustable head / scale / cam clamp | Edit `head_post`, `head_clamp`, `cam_lever`; tune `POST_CL`, `CAM_ECC` |
| Holo glare / cross-pol | `polarizer_base` + `polarizer_dial` + black `torch_deflector` |
| Phase-2 feeder | Spec: `docs/phase-2a-manual-feeder.md`; horn slot + anchors in Phase-1; **do not** model hopper/servo pocket in Phase-1 STLs |
| Research iPhone focus / glare | **chrome-devtools** MCP + web search |
| Assembly / optics diagram | **canvas** (`.canvas.tsx` in workspace canvases dir) |
| Project conventions for AI | **create-rule** → `.cursor/rules/card-scanner.mdc` |
| STL export broken after edit | **grinding-until-pass**; check `manifold3d` in `requirements.txt` |
| MCP browser won't connect | **troubleshooting-chrome-devtools** |
| Review recent geometry commits | **deep-bug-hunt** (bed fit, watertight, focus height constants) |

---

## Key files

| File | Role |
|------|------|
| `README.md` | Human-facing build guide |
| `CLAUDE.md` | This file — agent MCP/skill routing |
| `.mcp.json` | Claude Code MCP config — AgentCAD server |
| `build_woodstand.py` | Stand parts parametric CAD → `output/*.stl` (21 parts) |
| `design/wheel_head_b123.py` | Wheel-head + M3 hardware → `design/output/*.stl` (**9 parts**, build123d) |
| `design/wheel_head.py` | Legacy CadQuery — **superseded**, do not print |
| `design/photo_box.py` | White light box + platen — **Phase 2, not yet built** |
| `design/verify_requirements.py` | 40+ dimensional/optics requirement checks |
| `scripts/audit_builds.py` | Master build + audit pipeline (one command) |
| `scripts/audit_meshes.py` | Mesh status reporter — READY / SLICER-FX / BED-OVF |
| `scripts/preview_stl.py` | 4-view PNG render for a single STL |
| `docs/legacy-full-print.md` | Superseded all-print design |
| `output/` | Stand STLs — gitignored |
| `design/output/` | Wheel-head STLs — gitignored |

---

## Python conventions

- Type hints on all functions; PEP 257 docstrings  
- Dependencies: `requirements.txt` (`numpy`, `trimesh`, `manifold3d`, `scipy`)  
- Boolean engine: `manifold` (requires `manifold3d`)  
- Minimize scope: one geometry change at a time, re-export and verify bbox  

---

## Verification checklist (before claiming done)

- [ ] `python build_woodstand.py` — all parts `[OK]`, watertight  
- [ ] `verify_assembly()` passes (lens XY over scan nest ≤2 mm)  
- [ ] For changed parts: `py scripts/preview_stl.py output/<part>.stl` — proportions look right  
- [ ] Lens-to-card target still **≥ 260 mm** (document if wood mock-up differs)  
- [ ] Camera opening still covers iPhone 16 Pro lens + torch (or user-specified case)  
- [ ] README updated if user-visible behavior changed  
- [ ] No unrelated refactors in the same change
