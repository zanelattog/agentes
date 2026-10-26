# What was verified

[Português](avaliacao.md) · [Back](../README.en.md)

Prepared on October 26, 2026.

## Installation

The installer passed eight tests using temporary macOS directories:

- Preview without file writes.
- Exact copying of six profiles and unchanged repeated installation.
- Stopping before any profile copy when a conflict exists.
- Preserving existing symbolic links.
- Removal without deleting unrelated profiles.
- Stopping removal if any profile has been edited.
- Honoring the destination selected through `CODEX_HOME`.
- Rejecting a missing destination argument.

TOML files were parsed and checked for required fields and unique names. Bash syntax was checked too. Tests did not install into the user's real Codex configuration or call models.

The installer uses macOS commands without processor-specific binaries. There was no physical Intel Mac test or Finder launch test after download/quarantine. Actual execution of the six profiles inside Codex has not been evaluated yet.

## Agent quality

This adaptation has no performance benchmark. The original project's [evaluation discussion](https://github.com/msitarzewski/agency-agents/discussions/434) does not establish the performance of these condensed profiles.

This package provides shorter role definitions, instructions and deliverable criteria. The hypothesis is that clearer scope helps direct work; results must be checked in the project where it is used.

Compare equivalent tasks and record:

| Criterion | What to observe |
| --- | --- |
| Correctness | Does the requested behavior work? |
| Evidence | Do the reported commands and results exist? |
| Review | Are findings reproducible or false positives? |
| Cost | What is aggregate usage without double-counting? |
| Time | How long did it take, including fixes? |

Do not treat an agent-generated score as sufficient evidence. Document failures and tasks where the selection did not help.

Repeat installer tests with Python 3.9+:

```bash
python3 tests/test_installer.py
```

Python is only required for these tests, not for installing profiles.
