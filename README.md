<p align="center"><b>Português</b> · <a href="README.en.md">English</a></p>

# Agentes de IA

Onze agentes para desenvolver, criar conteúdo, prospectar e organizar entregas. Organizei esta seleção para planejar, construir e revisar projetos no Codex, com procedimentos específicos e instalação simples.

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
| **[Pixel](agents/pixel.toml)** | Planeja e produz imagens com as ferramentas disponíveis. |
| **[Frame](agents/frame.toml)** | Prepara roteiros, cortes e edição de vídeos. |
| **[Nilo](agents/nilo.toml)** | Pesquisa e qualifica leads e prepara abordagens comerciais. |
| **[Maia](agents/maia.toml)** | Cria conteúdo, textos de campanha e apresentações. |
| **[Otto](agents/otto.toml)** | Organiza prioridades, dependências e entregas. |

![Exemplo editado do Habblaud com Atlas, Luna, Nexo, Iris, Cora e Vero e suas funções](assets/habblaud-equipe.png)

<sub>Ilustração da equipe técnica original de seis agentes, anterior à ampliação para onze. Montagem sobre uma captura oficial do <a href="https://github.com/marmottajr/habblaud">Habblaud, de Márcio Junior</a>. Nomes e funções foram editados para apresentar esta equipe. Não é uma captura de agentes nossos em execução. <a href="docs/imagens.md">Origem e edição</a>.</sub>

## Como chamar os agentes

**Não precisa decorar os nomes nem chamar todos a cada pedido.** Você pode escolher um especialista ou pedir ao Codex para escolher:

| Você quer… | Pode escrever… |
| --- | --- |
| Deixar o Codex escolher | “Use os agentes necessários para esta tarefa e explique como dividiu o trabalho.” |
| Revisar uma alteração | “Peça à Iris para revisar este código, sem alterar os arquivos.” |
| Construir e conferir uma tela | “Peça à Luna para implementar a tela e, depois, ao Vero para testar.” |

Se preferir decidir antes de gastar com outros agentes, combine no início do chat:

> Se a tarefa for simples, resolva direto. Se valer a pena usar especialistas, sugira quais e me pergunte antes de chamar.

Esse combinado vale para a conversa; em um novo chat, repita-o ou salve nas instruções do projeto. Instalar os perfis só os disponibiliza: não inicia os onze automaticamente. [Mais exemplos](docs/uso.md).

## Cinco novos especialistas na prática

- **Pixel:** “Prepare uma capa para este projeto. Gere a imagem se houver ferramenta disponível e confira o resultado.”
- **Frame:** “Monte um roteiro de 30 segundos para demonstrar meu app, com cortes e legendas.”
- **Nilo:** “Defina o cliente ideal desta oferta e pesquise empresas compatíveis, com fontes. Não envie mensagens.”
- **Maia:** “Transforme esta demonstração em um post de LinkedIn, sem inventar números.”
- **Otto:** “Organize estas pendências por prioridade, dependência e critério de conclusão.”

Imagem e vídeo exigem ferramentas de mídia acessíveis. Sem elas, os agentes entregam planejamento e informam a limitação. Pesquisa de leads depende de fontes disponíveis; rascunhar não autoriza enviar.

## O que aproveitei do Vibe Coding Toolkit

Conferir o estado real antes de agir, investigar falhas com evidência, preservar alterações locais e retomar trabalho sem confiar cegamente em resumos antigos. Essas práticas estão nos **onze perfis**. Mantive os créditos de Matheus Gomes. [Detalhes da adaptação](docs/toolkit.md).

## Comece em poucos passos

1. Clique em **Baixar os agentes** e extraia o ZIP.
2. Abra a pasta e dê dois cliques em **Instalar.command**.
3. Aguarde **Concluído** e abra uma nova conversa no Codex. Versões anteriores reconhecidas são atualizadas com backup; edições pessoais são preservadas.
4. Peça um agente pelo nome:

> Use `iris` para revisar esta alteração. Mostre os problemas com evidências e não altere os arquivos.

O mesmo instalador atende Mac Intel e Apple Silicon. O download não executa nada sozinho. [Passo a passo completo e solução de problemas](docs/instalacao.md).

## A salinha no Habblaud

O Habblaud ajuda a acompanhar quem está trabalhando ou esperando sua atenção. Ele tem seus próprios personagens: **os nomes desta imagem não são aplicados automaticamente** ao instalar os perfis. [Como personalizar os nomes e conectar o Codex](docs/habblaud.md).

Observar o painel não exige uma nova resposta de IA. Os agentes continuam consumindo tokens enquanto trabalham.

## O que esperar

Cada perfil define procedimentos, verificações e limites. A versão anterior dos seis agentes técnicos empatou na comparação e consumiu 4,04% mais tokens; esse resultado **não mede a versão 2.0 com onze agentes**. [Resultados históricos](docs/avaliacao.md) · [Verificação da versão atual](docs/validacao-v2.md).

[Entenda o consumo](docs/tokens.md) · [Veja o que foi testado](docs/avaliacao.md) · [Instalador visual do catálogo original](docs/instalacao.md#catálogo-original-pelo-agency-agents-app)

---

Curadoria e adaptação de **Gabriel (@zanelattog)**, com apoio do Codex. Bases: **Agency Agents, de Michael Sitarzewski e colaboradores**, e práticas do **Vibe Coding Toolkit, de Matheus Gomes**. [Créditos](CREDITOS.md) · [MIT](LICENSE).
