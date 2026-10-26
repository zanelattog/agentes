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
profile_names=(atlas luna nexo iris cora vero pixel frame nilo maia otto)
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
updates=()
known_versions="$package_dir/releases/known-profile-hashes.txt"
for source in "${files[@]}"; do
  target="$destination/$(basename "$source")"
  if [ -L "$target" ] || { [ -e "$target" ] && [ ! -f "$target" ]; }; then
    printf 'Preserved unsafe destination: %s\n' "$target" >&2; conflict=1
  elif [ -f "$target" ] && ! cmp -s "$source" "$target"; then
    digest="$(shasum -a 256 "$target" | awk '{print $1}')"
    if [ "$mode" = install ] && [ -f "$known_versions" ] && \
       awk -v name="$(basename "$source")" -v hash="$digest" '$1 == name && $2 == hash { found=1 } END { exit !found }' "$known_versions"; then
      updates+=("$target")
    else
      printf 'Preserved conflicting/modified file: %s\n' "$target" >&2; conflict=1
    fi
  fi
done
if [ "$conflict" -eq 1 ]; then
  printf 'Stopped. No agent files changed. Resolve personal edits before retrying.\n' >&2
  exit 1
fi
backup_dir=""
if [ "${#updates[@]}" -gt 0 ] && [ "$dry_run" -eq 0 ]; then
  backup_dir="$destination/.agentes-backups/$(date +%Y%m%d-%H%M%S)-$$"
  [ ! -L "$destination/.agentes-backups" ] || { printf 'Unsafe backup directory.\n' >&2; exit 1; }
  mkdir -p "$backup_dir"
  for target in "${updates[@]}"; do cp -p "$target" "$backup_dir/$(basename "$target")"; done
  printf 'Backup: %s\n' "$backup_dir"
fi
for source in "${files[@]}"; do
  target="$destination/$(basename "$source")"
  if [ "$dry_run" -eq 1 ]; then
    printf 'Preview %s: %s\n' "$mode" "$target"
  elif [ "$mode" = uninstall ]; then
    if [ -f "$target" ]; then rm -- "$target"; printf 'Removed: %s\n' "$target"; fi
  elif [ -f "$target" ] && cmp -s "$source" "$target"; then
    printf 'Already installed: %s\n' "$target"
  elif [ -f "$target" ]; then
    # Only byte-identical known versions reach here; reject concurrent edits.
    [ -n "$backup_dir" ] && cmp -s "$target" "$backup_dir/$(basename "$target")" || { printf 'Concurrent edit; stopped.\n' >&2; exit 1; }
    staged="$lock_dir/$(basename "$source")"
    cp "$source" "$staged"; chmod 644 "$staged"
    mv "$staged" "$target"
    printf 'Updated: %s\n' "$target"
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
