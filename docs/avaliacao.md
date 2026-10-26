# O que foi testado

[English](evaluation.en.md) · [Voltar](../README.md)

## Resultado: empate, não uma melhora comprovada

Em 26/10/2026, comparei os perfis curtos com os perfis ampliados: uma resposta por versão para cada um dos seis exercícios, 12 chamadas no total. Ambos passaram nos 51 critérios definidos pelo avaliador. **Não houve ganho de pontuação nem regressão observada nesta amostra.** Isso não prova equivalência em projetos reais.

| Agente / Agent | Antes / Before | Depois / After |
| --- | --- | --- |
| Atlas | 8/8 | 8/8 |
| Luna | 9/9 | 9/9 |
| Nexo | 15/15 | 15/15 |
| Iris | 6/6 | 6/6 |
| Cora | 6/6 | 6/6 |
| Vero | 7/7 | 7/7 |

### O que os exercícios verificam

- **Atlas:** oito decisões de arquitetura para webhooks, duplicatas, concorrência, persistência e recuperação. Resposta de escolhas estruturadas, sem implementar o sistema.
- **Luna:** HTML executado em Chromium: associação do rótulo, região acessível, foco pelo teclado, largura de 320 px, validação, bloqueio de envio duplicado, recuperação de erro, sucesso e ausência de navegação.
- **Nexo:** distribuição proporcional com inteiros, empates, zeros, erros de tipo/valor e valores de 10³⁰. Um critério reúne 100 casos adicionais com semente fixa; não são 100 provas independentes.
- **Iris:** distinguir três bugs de três acusações sem fundamento em um exemplo sintético.
- **Cora:** distinguir três riscos demonstráveis de três afirmações sem evidência em um endpoint sintético.
- **Vero:** a suíte gerada passa na implementação de referência e detecta seis versões deliberadamente defeituosas. Os defeitos incluem expoente errado, ausência de teto, zeros, negativos e aceitação de booleanos.

### Método e limites

Mesmo modelo (`gpt-6-astra`), esforço `medium`, enunciado e formato de resposta em cada par. Sessões novas, ordem antiga/nova alternada entre papéis, sem ferramentas, plugins, memória ou arquivos do usuário disponíveis ao modelo. As instruções de cada perfil foram fornecidas como `developer_instructions`. Os artefatos foram depois executados pelo avaliador; a qualidade não foi julgada apenas por outra IA.

É uma avaliação de respostas orientadas por perfis, **não de delegação multiagente em um projeto real**. Apenas uma execução por combinação, tarefas pequenas e algumas questões com alternativas explícitas. O modelo já acertou tudo com as instruções antigas: existe efeito de teto. Não houve repetição estatística nem medida de ganho em tarefas longas. Os critérios executáveis foram escritos após inspecionar as respostas, com base nos contratos dos enunciados; portanto não é um benchmark cego ou pré-registrado. Não alterei os perfis para melhorar a nota depois dos resultados.

Os perfis ampliados acrescentam procedimentos específicos, limites de atuação e exigência de evidência. Isso descreve o conteúdo; não significa que mais texto seja melhor. Não há fundamento aqui para chamar estes agentes de “os melhores”.

### Consumo observado

| | Input | Output | Input + output |
| --- | ---: | ---: | ---: |
| Baseline | 69525 | 3542 | 73067 |
| Candidate | 72155 | 3867 | 76022 |

O total de entrada + saída ficou **4.04% maior** com os perfis ampliados, sem ganho de pontuação. A entrada inclui o contexto-base do Codex, além do perfil e do exercício; não é só o tamanho do TOML. Cache informado: zero. Tokens de raciocínio são um detalhamento da saída e não foram somados novamente. Este resultado é desta rodada, não uma previsão de custo ou percentual garantido para outros trabalhos. Não inclui a conversa que preparou a avaliação nem a geração do ícone.

### Evidências e reprodução

[Respostas e metadados](../evaluation/outputs) · [Pontuações](../evaluation/scores.json) · [Testes de mutação](../evaluation/mutation-results.json) · [Como reproduzir](../evaluation/README.md).

## Instalação

Oito testes do instalador passaram em pastas temporárias: prévia sem escrita, cópia exata e repetição, conflito sem cópia parcial, links simbólicos preservados, remoção seletiva, proteção a perfis editados, `CODEX_HOME` e argumento incompleto. TOML e Bash também foram validados.

Os seis perfis ampliados foram instalados localmente com backup dos anteriores. O teste de desempenho acima não valida o carregamento por nome nem toda a integração com o Habblaud. O instalador não contém binários dependentes de processador, mas não houve teste físico em Mac Intel ou após download com quarentena do Finder.

```bash
python3 tests/test_installer.py
```
