#!/bin/bash
set -euo pipefail
package_dir="$(cd "$(dirname "$0")" && pwd)"
status=0
/bin/bash "$package_dir/scripts/install.sh" "$@" || status=$?
if [ -t 0 ]; then
  printf '\nPressione Enter para fechar. / Press Enter to close. '
  read -r _ || true
fi
exit "$status"
