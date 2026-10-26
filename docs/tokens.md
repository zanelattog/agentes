# Tokens sem promessa de economia

[English](tokens.en.md) · [Voltar](../README.md)

Não existe um percentual confiável de consumo para esta seleção antes de medir tarefas reais. Um perfil menor tem menos texto, mas isso não determina o consumo total da execução.

| Situação | O que acontece |
| --- | --- |
| Baixar ou copiar os perfis pelo instalador local | Nenhuma chamada ao modelo. |
| Disponibilizar perfis no Codex | Pode acrescentar metadados ao contexto, conforme a implementação do cliente. Não inicia seis trabalhos sozinho. |
| Pedir uma tarefa a um agente | Instruções, contexto e respostas participam do uso. |
| Executar vários agentes | Acrescenta processamento individual e coordenação. |
| Acompanhar animações locais do Habblaud | A visualização não precisa de uma nova resposta do modelo. |
| Enviar trabalho ou mensagens pelo Habblaud | O agente acionado pode consumir mais tokens. |

## Exemplos de conta, não previsões

Os números abaixo são inventados apenas para explicar a comparação. Não são medições deste pacote, médias do mercado nem uma faixa esperada.

| Cenário hipotético | Sem a seleção | Com a seleção | Variação |
| --- | ---: | ---: | ---: |
| Uma revisão adicional aumenta o trabalho | 10.000 tokens | 13.000 tokens | +30% |
| Uma revisão evita tentativas que seriam repetidas | 10.000 tokens | 8.000 tokens | −20% |

Fórmula: `(total com perfis − total sem perfis) ÷ total sem perfis × 100`.

No primeiro exemplo, um total de 13.000 pode incluir 8.000 do agente principal, 3.000 do revisor e 2.000 de coordenação. Essa divisão também é fictícia. Na medição real, confira se o contador do agente principal já inclui os filhos, para não somá-los duas vezes.

Tokens não se convertem em dinheiro por uma taxa única: modelo, entrada, cache, saída, raciocínio e forma de cobrança podem ser diferentes. Não some uma coluna de raciocínio novamente se o provedor já a incluiu no total de saída. No plano por assinatura, acompanhe também os limites e o uso mostrados pelo produto.

## Como medir de verdade

1. Escolha uma tarefa pequena com critérios objetivos de sucesso.
2. Use a mesma versão do projeto, modelo, esforço de raciocínio e ferramentas.
3. Faça uma execução sem estes perfis e outra com o perfil escolhido, começando de estados equivalentes.
4. Registre o uso de todas as sessões envolvidas, tempo, problemas encontrados e testes que passaram. Anote cache e diferenças de contexto.
5. Repita com mais tarefas. Compare qualidade e custo juntos; um teste isolado não prova vantagem geral.

Para reduzir desperdício, delimite o escopo, evite que vários agentes releiam tudo e peça conclusões curtas com referências. Acrescente agentes quando houver trabalho distinto para eles. Estes cuidados são orientações, não uma garantia de economia.

## Fontes

- [OpenAI: subagentes, consumo e configuração](https://learn.chatgpt.com/docs/agent-configuration/subagents).
- [Habblaud: fontes locais, integração e mensagens](https://github.com/marmottajr/habblaud/blob/main/README.pt-BR.md).
- [Agency Agents: discussão sobre avaliação comparativa](https://github.com/msitarzewski/agency-agents/discussions/434).
