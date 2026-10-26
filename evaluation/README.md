# Avaliação / Evaluation

As respostas salvas são sintéticas. Não contêm código ou contatos de clientes.
Saved responses are synthetic, with no customer source code or contacts.

- `baseline/`: perfis anteriores / previous profiles.
- `outputs/`: 12 respostas, hashes e tokens / 12 responses, hashes and tokens.
- `tasks.json`: enunciados / tasks.
- `scores.json`: resultados / results.

## Reavaliar os artefatos / Recheck saved artifacts

Revise os códigos gerados antes de executá-los. Estes scripts executam Python e HTML das respostas. Rode em ambiente isolado. Não use com respostas não revisadas.
Inspect generated code first. These scripts execute the responses' Python and HTML. Use an isolated environment; do not run unreviewed responses.

Python 3.9+, Node.js, Playwright and Chromium:

```bash
npm install --no-save playwright
npx playwright install chromium
node evaluation/grade_luna.mjs
python3 evaluation/grade.py
python3 tests/test_installer.py
```

`PLAYWRIGHT_MODULE` e `CHROMIUM_EXECUTABLE` permitem usar uma instalação existente.
These environment variables support existing installations.

## Gerar novas respostas / Generate fresh responses

Exige Codex CLI autenticado e acesso ao modelo configurado no script. **Consome sua cota/tokens e substitui os resultados locais.** Faça uma cópia antes. Os resultados podem variar. `tomllib` (Python 3.11+) ou `pip._vendor.tomli` é necessário para ler TOML.
Requires authenticated Codex CLI and access to the configured model. **Uses your quota/tokens and overwrites local results.** Back up first; results can vary. TOML parsing requires Python 3.11+ or pip's vendored tomli.

```bash
python3 evaluation/make_tasks.py
python3 evaluation/run_comparison.py
node evaluation/grade_luna.mjs
python3 evaluation/grade.py
```

[Limites da comparação](../docs/avaliacao.md) · [Limitations](../docs/evaluation.en.md).
