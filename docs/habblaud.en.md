# Names in Habblaud

[Português](habblaud.md) · [Back](../README.en.md)

Atlas, Luna, Nexo, Iris, Cora, Vero, Pixel, Frame, Nilo, Maia and Otto are the names of this package's Codex profiles. Habblaud assigns its own session names and appearances. This installer does not synchronize the two.

## Edit a character

According to Habblaud's documentation:

1. Open Habblaud locally on your computer.
2. Click the main agent to open its details.
3. Click the pencil beside its name to open the character editor.
4. Choose a name and appearance, then save.

This customization applies to a project's character, not to a rule renaming every subagent. A second concurrent session in the same project may get another character. The editor requires local access and the terminal feature enabled. This package does not force the image's six names into Habblaud.

## Display Codex activity

Habblaud can read Codex's local session records. For more immediate updates, its documentation describes installing hooks with `npm run codex:install` and approving them through `/hooks` in Codex. Run those commands **inside your Habblaud installation**, not this repository.

Habblaud is optional and is not bundled with the eleven profiles. Watching the dashboard does not eliminate model usage. Sending messages or starting work through it may trigger additional processing.

[Official Habblaud documentation](https://github.com/marmottajr/habblaud).

## Local customization in this environment

On the Mac used to prepare this version, Habblaud 0.7.0 was locally adapted to map all eleven profile roles to names and labels when actual sessions report those roles. Office-model tests cover all eleven names. This patch is not bundled in the public installer and may require reapplication after a Habblaud upgrade. It does not create working characters without real sessions.
