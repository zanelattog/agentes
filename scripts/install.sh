#!/bin/bash
# Local installer. No network, model calls, credentials, or config.toml changes.
set -euo pipefail
package_dir="$(cd "$(dirname "$0")/.." && pwd)"
destination="${CODEX_HOME:-$HOME/.codex}/agents"
mode=install
dry_run=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --dest)
      [ "$#" -ge 2 ] && [ -n "$2" ] || { printf 'Missing destination.\n' >&2; exit 2; }
      destination="$2"; shift 2 ;;
    --dry-run) dry_run=1; shift ;;
    --uninstall) mode=uninstall; shift ;;
    --help)
      printf 'Usage: bash scripts/install.sh [--dest DIRECTORY] [--dry-run] [--uninstall]\n'
      exit 0 ;;
    *) printf 'Unknown option: %s\n' "$1" >&2; exit 2 ;;
  esac
done
case "$destination" in
  /*) ;;
  *) destination="$PWD/$destination" ;;
esac
while [ "${destination%/}" != "$destination" ]; do destination="${destination%/}"; done
[ -n "$destination" ] || { printf 'Root destination is not allowed.\n' >&2; exit 2; }
[ ! -L "$destination" ] || { printf 'Refusing symbolic-link destination.\n' >&2; exit 1; }
profile_names=(atlas luna nexo iris cora vero)
files=()
for profile_name in "${profile_names[@]}"; do
  source="$package_dir/agents/$profile_name.toml"
  [ -f "$source" ] && [ ! -L "$source" ] || { printf 'Incomplete package: missing %s\n' "$profile_name" >&2; exit 1; }
  files+=("$source")
done
printf 'Agentes de IA / AI Agents\nMode: %s\nDestination: %s\n' "$mode" "$destination"
if [ "$dry_run" -eq 0 ]; then
  mkdir -p "$destination"
  lock_dir="$destination/.agentes-curadoria-install.lock"
  mkdir "$lock_dir" 2>/dev/null || { printf 'Another install may be active: %s\n' "$lock_dir" >&2; exit 1; }
  trap 'rmdir "$lock_dir"' EXIT
fi
# Validate every destination before writing any profile.
conflict=0
for source in "${files[@]}"; do
  [ -f "$source" ] && [ ! -L "$source" ] || { printf 'Invalid source: %s\n' "$source" >&2; exit 1; }
  target="$destination/$(basename "$source")"
  if [ -L "$target" ] || { [ -e "$target" ] && { [ ! -f "$target" ] || ! cmp -s "$source" "$target"; }; }; then
    printf 'Preserved conflicting/modified file: %s\n' "$target" >&2
    conflict=1
  fi
done
if [ "$conflict" -eq 1 ]; then
  printf 'Stopped. No agent files changed. Back up and resolve conflicts before retrying.\n' >&2
  exit 1
fi
for source in "${files[@]}"; do
  target="$destination/$(basename "$source")"
  if [ "$dry_run" -eq 1 ]; then
    printf 'Preview %s: %s\n' "$mode" "$target"
  elif [ "$mode" = uninstall ]; then
    if [ -f "$target" ]; then rm -- "$target"; printf 'Removed: %s\n' "$target"; fi
  elif [ -f "$target" ]; then
    printf 'Already installed: %s\n' "$target"
  else
    # Stage and hard-link without replacing an existing destination.
    staged="$lock_dir/$(basename "$source")"
    cp "$source" "$staged"
    chmod 644 "$staged"
    if ! ln "$staged" "$target"; then
      rm -f "$staged"
      printf 'Install interrupted; destination changed concurrently.\n' >&2
      exit 1
    fi
    rm "$staged"
    printf 'Installed: %s\n' "$target"
  fi
done
if [ "$dry_run" -eq 1 ]; then
  printf 'Preview only. Nothing changed.\n'
elif [ "$mode" = install ]; then
  printf '\nConcluído. Abra uma nova conversa no Codex e peça um agente pelo nome.\nDone. Open a new Codex chat and request an agent by name.\n'
fi
