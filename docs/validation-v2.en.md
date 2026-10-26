# Version 2.0 verification

[Português](validacao-v2.md) · [Back](../README.en.md)

Eleven profiles prepared on October 26, 2026. TOML parsed, names unique, required fields and toolkit practices present in every file.

## Installer

**10 tests passed:** exact/idempotent installation, dry run, conflicts without partial profile changes, symlink preservation, selective removal, edited-file protection, CODEX_HOME, invalid arguments, known-version upgrade with backup, and preventing upgrades when another profile has personal edits.

```bash
python3 tests/test_installer.py
```

All eleven profiles were installed on this Mac and byte-compared with the package. No physical Intel or Finder quarantine/download test.

## Five behavior checks

One call per new profile, `gpt-6-astra`, `medium`, fresh sessions without tools. Profile instructions were supplied through developer_instructions. Structured choices were checked against expectations defined before execution.

| Profile | Observed behavior | Checks |
| --- | --- | --- |
| Pixel | Offered briefing/prompt without claiming an image was generated | 3/3 |
| Frame | Offered a plan and pending requirements without claiming render/publication | 3/3 |
| Nilo | Selected the matching company, left contact unknown, did not authorize sending | 3/3 |
| Maia | Retained prototype and AI involvement, rejected unsupported metrics | 3/3 |
| Otto | Rejected stale completion claims and separated local work from a blocked integration | 3/3 |

Measured usage: **60688 input + output tokens** across five calls, without double-counting reasoning. Preparation conversation excluded. No savings comparison was made.

[Responses, tasks, hashes and usage](../evaluation/v2/results.json) · [Runner](../evaluation/v2/run_smoke.py).

### Limitations

Basic checks with explicit choices, not an excellence benchmark. No image generation, video rendering, lead search, publication, CRM or live campaign. Named-profile loading and full delegation were not tested by these calls. No eleven-profile before/after comparison or demonstrated intelligence gain.

Qualitative limitation: Pixel interpreted an ambiguous Portuguese “budget/quote app” as personal finance without the brief specifying its domain. Checks measure honesty about image generation, not complete concept suitability. Real work requires specifying or clarifying the domain before approval. Profiles were not retuned after this run to improve scores.

## Local Habblaud

Name integration passed **29 office-model/Codex-source tests**, typecheck and server build. The local service returned healthy after deployment, outside demo mode. This verifies role mapping, not eleven simultaneously active agents.

Habblaud customization is local; the public installer distributes profiles only. [Details](habblaud.en.md).
