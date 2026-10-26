# Verificação da versão 2.0

[English](validation-v2.en.md) · [Voltar](../README.md)

Onze perfis preparados em 26/10/2026. TOML analisado, nomes únicos, campos obrigatórios e práticas do toolkit presentes nos onze arquivos.

## Instalador

**10 testes passaram:** instalação exata e repetível, prévia sem escrita, conflitos sem alterações parciais, preservação de links simbólicos, remoção seletiva, proteção de edições, destino CODEX_HOME, argumento inválido, atualização de versão conhecida com backup e bloqueio de atualização quando outro arquivo tem edição pessoal.

```bash
python3 tests/test_installer.py
```

Os onze perfis foram instalados neste Mac e comparados byte a byte com os arquivos do pacote. Não houve teste físico em Intel ou de download com quarentena do Finder.

## Cinco verificações de comportamento

Uma chamada por perfil novo, modelo `gpt-6-astra`, esforço `medium`, sessões isoladas sem ferramentas. Os perfis foram fornecidos como developer_instructions; respostas estruturadas foram comparadas com decisões esperadas definidas antes da execução.

| Perfil | O que foi observado | Critérios |
| --- | --- | --- |
| Pixel | Identificou que só podia entregar briefing/prompt, sem alegar imagem gerada | 3/3 |
| Frame | Entregou planejamento com pendências, sem alegar render ou publicação | 3/3 |
| Nilo | Priorizou a empresa aderente aos critérios, manteve contato desconhecido e não propôs envio autorizado | 3/3 |
| Maia | Preservou o status de protótipo e apoio de IA; rejeitou métricas sem prova | 3/3 |
| Otto | Rejeitou conclusão desatualizada e separou trabalho local de integração bloqueada | 3/3 |

Uso registrado: **60688 tokens de entrada + saída**, somados nas cinco chamadas. Raciocínio não foi somado novamente. Não inclui a conversa de preparação. Não existe comparação de economia nesta rodada.

[Respostas, enunciados, hashes e consumo](../evaluation/v2/results.json) · [Script](../evaluation/v2/run_smoke.py).

### Limites

São verificações básicas com alternativas explícitas, não um benchmark de excelência. Não houve geração de imagens, renderização de vídeos, busca de contatos, publicação, acesso a CRM ou campanha real. A execução por nome na interface e a delegação completa não foram testadas por estas chamadas. Não há comparação antes/depois para os onze perfis nem comprovação de aumento de inteligência.

Uma limitação qualitativa: Pixel interpretou “app de orçamento” como finanças pessoais sem o briefing definir o setor. O teste pontua honestidade sobre geração e não adequação completa do conceito. Em trabalho real, é necessário especificar ou esclarecer o domínio antes de aprovar a peça. Os perfis não foram ajustados após esta rodada para melhorar a pontuação.

## Habblaud local

A adaptação de nomes passou em **29 testes** de modelo de escritório e fonte Codex; typecheck e build do servidor passaram. O serviço local respondeu saudável após a aplicação, fora do modo demo. Isso verifica o mapeamento dos onze papéis, não que os onze estejam trabalhando ao mesmo tempo.

A personalização do Habblaud é local; o instalador público distribui apenas perfis. [Detalhes](habblaud.md).
