# Use agents without memorizing names

[Português](uso.md) · [Back](../README.en.md)

Names help request a particular role, but you can describe the goal in ordinary language. To delegate to specialists, explicitly ask Codex to use agents and select the roles needed.

## Three approaches

- **Direct:** “Use `cora` to review this login's security. Do not edit the code.”
- **Goal-based:** “Use the agents needed to implement and verify this form. Avoid duplicate work.”
- **Suggest first:** “First assess whether this task needs specialists. If it does, suggest which ones and wait for my decision.”

You do not need to manually open six chats. Codex coordinates delegation when the feature is available and enabled. Profiles must be installed in the environment serving the chat; installing them on a Mac does not automatically install them in Codex Cloud or another computer.

## Set a preference for the conversation

> Handle simple requests directly. For larger tasks, explain whether dividing the work would help, suggest only the necessary specialists, and ask before calling them. Do not use everyone by default.

You can give this instruction once at the start of a chat. Persisting it between chats requires saving it in the appropriate project or client instructions. The basic installer does not change these instructions; the Maestro installer explicitly configures coordination.

Exact names are `atlas`, `luna`, `nexo`, `iris`, `cora`, `vero`, `pixel`, `frame`, `nilo`, `maia` and `otto`. If Codex cannot find a profile, start a new chat and check installation. Do not ask it to pretend it called an unavailable agent.

Habblaud characters represent real sessions. Installing files does not put all six in the office; they appear according to activity and the available integration.

[Official delegation documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Maestro on the main agent

With [Maestro](maestro.en.md) installed, the main agent coordinates directly. Describe the goal; do not spawn another Maestro. It handles small tasks alone and delegates selectively when useful and permitted. You can ask it to work alone or ask before delegating.
