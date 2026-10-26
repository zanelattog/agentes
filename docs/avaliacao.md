# O que foi verificado

[English](evaluation.en.md) · [Voltar](../README.md)

Versão preparada em 26 de outubro de 2026.

## Instalação

O instalador passou por oito testes em pastas temporárias no macOS:

- Prévia sem escrita de arquivos.
- Cópia exata dos seis perfis e repetição sem alterações.
- Interrupção antes de copiar qualquer perfil quando há conflito.
- Preservação de links simbólicos existentes.
- Remoção sem apagar perfis de outros projetos.
- Interrupção da remoção quando um perfil foi editado.
- Respeito ao destino configurado por `CODEX_HOME`.
- Rejeição de argumento de destino incompleto.

Os arquivos TOML foram analisados sintaticamente e conferidos quanto aos campos obrigatórios e nomes únicos. A sintaxe dos scripts Bash também foi verificada. Os testes não instalaram perfis no Codex real do usuário e não chamaram modelos.

O instalador usa comandos presentes no macOS, sem binários específicos de processador. Não houve teste físico em um Mac Intel nem teste de abertura pelo Finder após download/quarentena. A execução real dos seis perfis no Codex ainda não foi avaliada.

## Qualidade dos agentes

Não há benchmark desta adaptação. O projeto original tem uma [discussão de avaliação](https://github.com/msitarzewski/agency-agents/discussions/434), que não comprova o desempenho destes perfis resumidos.

O que este pacote oferece é uma organização mais curta de papéis, instruções e critérios de entrega. A hipótese é que isso ajude a direcionar o trabalho; o resultado precisa ser conferido no projeto em que for usado.

Para comparar, escolha tarefas equivalentes e registre:

| Critério | O que observar |
| --- | --- |
| Correção | O comportamento solicitado funciona? |
| Evidência | Os comandos e resultados relatados existem? |
| Revisão | Os achados são reproduzíveis ou falsos positivos? |
| Custo | Qual foi o uso agregado, sem contagem duplicada? |
| Tempo | Quanto demorou, incluindo correções? |

Nunca use apenas a nota atribuída por outro agente como prova de qualidade. Documente também falhas e tarefas em que a seleção não ajudou.

Para repetir os testes de instalação, use Python 3.9+:

```bash
python3 tests/test_installer.py
```

Python é necessário somente para esses testes, não para instalar os perfis.
