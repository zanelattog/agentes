# What was tested

> **Historical record:** this comparison used the six profiles before toolkit integration. Hashes in `evaluation/outputs/` identify tested versions. Do not extrapolate to version 2.0. [Current checks](validation-v2.en.md).

[Português](avaliacao.md) · [Back](../README.en.md)

## Result: a tie, not a demonstrated improvement

On October 26, 2026, the short profiles and expanded profiles were compared on six exercises: one response per version per role, 12 calls total. Both passed all 51 evaluator checks. **No score improvement or regression was observed in this sample.** This does not establish equivalence on real projects.

| Agente / Agent | Antes / Before | Depois / After |
| --- | --- | --- |
| Atlas | 8/8 | 8/8 |
| Luna | 9/9 | 9/9 |
| Nexo | 15/15 | 15/15 |
| Iris | 6/6 | 6/6 |
| Cora | 6/6 | 6/6 |
| Vero | 7/7 | 7/7 |

### Exercises

- **Atlas:** eight structured architecture decisions covering durable webhook ingestion, deduplication, concurrency and recovery. No implementation.
- **Luna:** generated HTML executed in Chromium: label association, live region, keyboard focus, 320 px viewport, validation, duplicate submission prevention, error recovery, success and no navigation.
- **Nexo:** exact integer allocation, ties, zero values, type/value errors and amounts of 10³⁰. One check groups 100 additional seeded cases; these are not 100 independent proofs.
- **Iris:** distinguish three actual bugs from three unsupported allegations in synthetic code.
- **Cora:** distinguish three demonstrable security risks from three unsupported claims in a synthetic endpoint.
- **Vero:** generated tests pass against a reference implementation and detect six deliberately broken implementations: exponent, cap, zero handling, negatives and booleans.

### Method and limitations

Same model (`gpt-6-astra`), `medium` reasoning, task and output schema per pair. Fresh sessions, alternating baseline/candidate order across roles; no tools, plugins, memories or user files available to the model. Profile instructions were supplied through `developer_instructions`. The evaluator subsequently executed the artifacts; scores are not just another AI's opinion.

This tests profile-guided responses, **not multi-agent delegation in a real project**. One execution per combination, small tasks, some with explicit options, no statistical repetition or long-task evaluation. The baseline already passed everything, creating a ceiling effect. Executable checks were written after inspecting responses, based on task contracts; this is not a blind or preregistered benchmark. Profiles were not tuned after seeing the scores.

Expanded profiles add role-specific procedures, boundaries and evidence requirements. That describes their content, not proof that longer instructions improve quality. These results do not justify calling the agents “the best”.

### Observed usage

| | Input | Output | Input + output |
| --- | ---: | ---: | ---: |
| Baseline | 69525 | 3542 | 73067 |
| Candidate | 72155 | 3867 | 76022 |

Combined input + output was **4.04% higher** with expanded profiles, without a score improvement. Input includes Codex's base context, profile and task; it is not just the TOML. Reported cached input was zero. Reasoning tokens are part of output and were not counted twice. This is one measured run, not a price estimate or promised percentage for other work. It excludes the preparation conversation and icon generation.

### Evidence and reproduction

[Responses and metadata](../evaluation/outputs) · [Scores](../evaluation/scores.json) · [Mutation results](../evaluation/mutation-results.json) · [Reproduction](../evaluation/README.md).

## Installation

Eight installer tests passed in temporary directories: dry run, exact copy and repeat, conflict without partial copying, preserved symlinks, selective uninstall, protection of modified profiles, `CODEX_HOME`, and incomplete destination argument. TOML and Bash were also validated.

The six expanded profiles were installed locally with backups. The performance test above does not validate named-profile loading or the complete Habblaud integration. The installer has no processor-specific binaries; no physical Intel Mac or Finder quarantine test was performed.

```bash
python3 tests/test_installer.py
```
