<p align="center"><b>Português</b> · <a href="README.en.md">English</a></p>

# Agentes de IA

Seis agentes, cada um com uma função. Organizei esta seleção para planejar, construir e revisar projetos no Codex, com instruções curtas e instalação simples.

**[↓ Baixar os agentes](https://github.com/zanelattog/agentes/archive/refs/heads/main.zip)** · [Instalação](docs/instalacao.md) · [Tokens](docs/tokens.md)

## Conheça a equipe

| Agente | Em que ajuda |
| --- | --- |
| **[Atlas](agents/atlas.toml)** | Planeja a solução e organiza os próximos passos. |
| **[Luna](agents/luna.toml)** | Constrói telas, formulários e interações. |
| **[Nexo](agents/nexo.toml)** | Cuida de APIs, regras de negócio e dados. |
| **[Iris](agents/iris.toml)** | Revisa o código e procura bugs e regressões. |
| **[Cora](agents/cora.toml)** | Analisa acesso, entradas e riscos de segurança. |
| **[Vero](agents/vero.toml)** | Testa a entrega e confere o que realmente funciona. |

![Exemplo editado do Habblaud com Atlas, Luna, Nexo, Iris, Cora e Vero e suas funções](assets/habblaud-equipe.png)

<sub>Montagem sobre uma captura oficial do <a href="https://github.com/marmottajr/habblaud">Habblaud, de Márcio Junior</a>. Nomes e funções foram editados para apresentar esta equipe. Não é uma captura de agentes nossos em execução. <a href="docs/imagens.md">Origem e edição</a>.</sub>

## Como chamar os agentes

**Não precisa decorar os nomes nem chamar todos a cada pedido.** Você pode escolher um especialista ou pedir ao Codex para escolher:

| Você quer… | Pode escrever… |
| --- | --- |
| Deixar o Codex escolher | “Use os agentes necessários para esta tarefa e explique como dividiu o trabalho.” |
| Revisar uma alteração | “Peça à Iris para revisar este código, sem alterar os arquivos.” |
| Construir e conferir uma tela | “Peça à Luna para implementar a tela e, depois, ao Vero para testar.” |

Se preferir decidir antes de gastar com outros agentes, combine no início do chat:

> Se a tarefa for simples, resolva direto. Se valer a pena usar especialistas, sugira quais e me pergunte antes de chamar.

Esse combinado vale para a conversa; em um novo chat, repita-o ou salve nas instruções do projeto. Instalar os perfis só os disponibiliza: não inicia os seis automaticamente. [Mais exemplos](docs/uso.md).

## Comece em poucos passos

1. Clique em **Baixar os agentes** e extraia o ZIP.
2. Abra a pasta e dê dois cliques em **Instalar.command**.
3. Aguarde **Concluído** e abra uma nova conversa no Codex.
4. Peça um agente pelo nome:

> Use `iris` para revisar esta alteração. Mostre os problemas com evidências e não altere os arquivos.

O mesmo instalador atende Mac Intel e Apple Silicon. O download não executa nada sozinho. [Passo a passo completo e solução de problemas](docs/instalacao.md).

## A salinha no Habblaud

O Habblaud ajuda a acompanhar quem está trabalhando ou esperando sua atenção. Ele tem seus próprios personagens: **os nomes desta imagem não são aplicados automaticamente** ao instalar os perfis. [Como personalizar os nomes e conectar o Codex](docs/habblaud.md).

Observar o painel não exige uma nova resposta de IA. Os agentes continuam consumindo tokens enquanto trabalham.

## O que esperar

Papéis claros ajudam a organizar implementação e revisão. Mais agentes também podem aumentar o consumo: **não há economia garantida nem benchmark desta seleção**.

[Entenda o consumo](docs/tokens.md) · [Veja o que foi testado](docs/avaliacao.md) · [Instalador visual do catálogo original](docs/instalacao.md#catálogo-original-pelo-agency-agents-app)

---

Curadoria e adaptação de **Gabriel (@zanelattog)**, com apoio do Codex. Base: **Agency Agents, de Michael Sitarzewski e colaboradores**. [Créditos](CREDITOS.md) · [MIT](LICENSE).
