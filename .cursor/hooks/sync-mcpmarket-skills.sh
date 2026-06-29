#!/usr/bin/env bash
# Sync MCPmarket baseline skills into Cursor's skills directory.
# Mirrors Claude Code plugin SessionStart hook behavior.
set -euo pipefail

PLUGIN_ROOT="${MCPMARKET_PLUGIN_ROOT:-$HOME/.claude/plugins/mcpmarket-my-toolkit}"
SKILLS_DIR="${MCPMARKET_SKILLS_DIR:-$HOME/.cursor/skills/mcpmarket}"

if [ ! -f "$PLUGIN_ROOT/shared/sync.sh" ]; then
  echo "MCPmarket sync: plugin not found at $PLUGIN_ROOT" >&2
  exit 0
fi

export MCPMARKET_PLUGIN_ROOT="$PLUGIN_ROOT"
export MCPMARKET_SKILLS_DIR="$SKILLS_DIR"
mkdir -p "$SKILLS_DIR"

bash "$PLUGIN_ROOT/shared/sync.sh"
