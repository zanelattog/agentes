#!/bin/bash
# Main-agent coordination + the eleven specialists. No model or approval changes.
set -euo pipefail
package_dir="$(cd "$(dirname "$0")" && pwd)"
command -v python3 >/dev/null || { printf 'Maestro requer Python 3.9+. Veja docs/maestro.md.\n'; exit 1; }
printf 'Instala Maestro em CODEX_HOME/AGENTS.md e os onze especialistas. Preserva conteúdo existente.\n'
python3 "$package_dir/scripts/install_maestro.py" --dry-run
/bin/bash "$package_dir/scripts/install.sh" --dry-run
/bin/bash "$package_dir/scripts/install.sh"
python3 "$package_dir/scripts/install_maestro.py"
printf '\nConcluído. Abra um novo chat: o principal coordena sem criar outro Maestro.\n'
if [ -t 0 ]; then read -r -p 'Enter para fechar. / Enter to close. ' _ || true; fi
