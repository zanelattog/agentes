# Maestro: talk directly to the coordinator

[Português](maestro.md) · [Back](../README.en.md)

Maestro configures the **main Codex agent**, rather than spawning another coordinator.
It handles small requests directly and delegates bounded work to the existing eleven
specialists when useful and permitted, then verifies and integrates their results.

## Installation

1. [Download](https://github.com/zanelattog/agentes/archive/refs/heads/main.zip) and extract.
2. Open **Instalar Maestro.command**. This requires Python 3.9+ and Bash. It installs
   the specialists and adds a marked block to `~/.codex/AGENTS.md`, respecting
   `CODEX_HOME`. It does not install dependencies, change models or weaken approvals.
3. Start a new Codex chat; restart the app if needed. Ask which Maestro instructions
   were loaded. Existing conversations may not reload the file.
4. Describe your goal normally; do not request a separate Maestro subagent.

To install only specialist profiles, use **Instalar.command** instead. If Finder
does not open a downloaded script, run `bash ` followed by its path in Terminal.

Unrelated instructions are preserved byte for byte and existing files are backed up.
Edited blocks, ambiguous markers and nonempty `AGENTS.override.md` files stop the
installation for manual reconciliation. Project rules and higher-priority restrictions
still apply. The two installers are separate steps; a system failure between steps
may leave a partial installation. Check output and rerun if needed.

```bash
python3 scripts/install_maestro.py --dry-run
python3 scripts/install_maestro.py --uninstall
```

Removal affects only the managed block, not specialists. Use `--dest /path/AGENTS.md`
for project instructions, and ensure specialist profiles are available in that environment.

## Usage

Beginner: “Build a local demo using synthetic contacts. Choose the necessary steps
and specialists, explain simply and verify the result. Do not send messages or
connect real services.”

Experienced: “Implement this change without breaking the API contract. Delegate
independent implementation and review, assign file ownership, run relevant checks
and report the diff and remaining limitations.”

Selective delegation is requested by the installed instructions; you can override
it with “work alone” or “ask before delegating.” Unavailable tools are disclosed,
not simulated. Without delegation tools the main agent can work sequentially.

Habblaud character names are visual labels, not evidence of agent configuration.
The package does not rename those characters. No token savings, autonomous background
monitoring or model superiority is promised.

[Instructions](../coordinator/maestro.md) · [Validation](validacao-maestro.md)
· [Official AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
· [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).
