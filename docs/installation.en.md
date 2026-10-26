# Detailed installation

[Português](instalacao.md) · [Back](../README.en.md)

### This selection: Intel or Apple Silicon Mac

1. Click [**Download the agents**](https://github.com/zanelattog/agentes/archive/refs/heads/main.zip), or **Code → Download ZIP** on GitHub.
2. Open **Downloads** in Finder and extract the ZIP.
3. Open the extracted folder and double-click **Instalar.command**.
4. Terminal shows the destination and results. Wait for **Done**.
5. Start a new Codex chat inside the project you want to work on.
6. Request an agent by name, using the examples below.

The button downloads files; installation happens on your computer when you open the installer. macOS may require confirmation for a downloaded file. This is not a signed application. If double-clicking does not work, open Terminal, type `bash `, drag `Instalar.command` into the window and press Enter.

The installer uses macOS Bash with no additional libraries. It copies only the eleven profiles to `~/.codex/agents` (or `$CODEX_HOME/agents` if configured). It makes no model calls, installs neither Codex nor Habblaud, and does not modify permissions, model settings or `config.toml`. Known previous versions are identified by SHA-256 and upgraded with backups under `~/.codex/agents/.agentes-backups/`. Personal edits or unknown files stop installation before any profile changes.

You need a configured Codex account and a client supporting custom agents. If profiles are unavailable, restart the app and check whether agents are enabled in your configuration. [Official reference](https://learn.chatgpt.com/docs/agent-configuration/subagents).

<details>
<summary>Terminal, project installation and removal</summary>

From the extracted folder:

```bash
# Preview without changing anything
bash scripts/install.sh --dry-run

# Install for a single project: replace this path
bash scripts/install.sh --dest "/path/to/project/.codex/agents"

# Remove this selection from your personal agents folder
bash scripts/install.sh --uninstall
```

For project removal, also pass the same `--dest`. Removal stops if it encounters a modified profile, preserving your changes. Known older package versions are updated with backups; personal changes require reconciliation.

On Linux, run `bash scripts/install.sh`. On Windows, copy the eleven files from `agents/` into the agents folder of the Codex installation you use; this package's double-click installer targets macOS.

</details>

### Original catalog: Agency Agents App

**The original application supports Codex too.** Claude Code folders or examples do not mean it is Claude-only.

1. Open [Agency Agents App → Releases](https://github.com/msitarzewski/agency-agents-app/releases/latest).
2. Under **Assets**, choose the `aarch64` `.dmg` for Apple Silicon or `x64` for Intel.
3. Install and open **Agency Agents**.
4. Browse specialists in **Agents**, or ready-made groups in **Teams**.
5. Open the selection's install/deploy action and select **Codex** as the destination tool.
6. Check the results and start a new Codex chat. The app's **Playbook** includes usage examples.

Control labels may change between versions. This route installs the **original catalog**, not this repository's eleven adapted profiles. Installation makes instructions available; execution happens in Codex. [Application documentation](https://github.com/msitarzewski/agency-agents-app).

## Updating

Download a fresh ZIP and run its installer. It installs the version bundled in that download, not a background update service or automatic upstream synchronization. Known unmodified older profiles receive backups; personal edits require reconciliation.
