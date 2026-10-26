# Maestro: você conversa com quem coordena

[English](maestro.en.md) · [Voltar](../README.md)

Maestro é o modo de trabalho do **agente principal do Codex**. Não é um segundo
agente entre você e o principal, nem um novo modelo de IA.

```text
Você → Codex principal (Maestro)
          ├─ resolve sozinho tarefas simples
          └─ delega etapas delimitadas → especialistas → confere e integra
```

## Instalar

1. [Baixe o pacote](https://github.com/zanelattog/agentes/archive/refs/heads/main.zip) e extraia.
2. Abra **Instalar Maestro.command**. Ele instala os onze especialistas e acrescenta
   um bloco identificado em `~/.codex/AGENTS.md` (respeita `CODEX_HOME`). Requer Python
   3.9 ou superior, além do Bash. Não instala dependências automaticamente.
3. Abra um **novo chat** no Codex. Se necessário, reinicie o app para recarregar
   instruções. Peça: “Explique quais instruções do Maestro você carregou.”
4. Descreva o trabalho normalmente. Você não precisa decorar nomes ou pedir um
   subagente Maestro. Uma conversa antiga não comprova que o arquivo foi recarregado.

Prefere somente os especialistas? Use **Instalar.command**, que mantém o
comportamento anterior e não escreve instruções do principal. Se o Finder não abrir
o arquivo, execute `bash ` seguido do caminho do instalador no Terminal.

O bloco orienta delegação seletiva quando útil e permitida, sem pedir autorização
de novo a cada especialista. Você pode dizer “faça sozinho” ou “pergunte antes de
delegar”. Isso não altera permissões, aprovações, modelo ou limites do Codex.

O instalador preserva o restante do arquivo byte por byte, cria backup antes de
alterar arquivos existentes e recusa blocos editados ou marcadores ambíguos.
Se houver `AGENTS.override.md` não vazio, para e informa que esse arquivo tem
precedência. Não apague suas regras para resolver: reconcilie as instruções.

Para visualizar ou remover só o bloco, na pasta extraída:

```bash
python3 scripts/install_maestro.py --dry-run
python3 scripts/install_maestro.py --uninstall
```

Remover o bloco não remove especialistas nem recupera automaticamente versões de
outros arquivos. Para uso em um projeto, passe `--dest /caminho/do/projeto/AGENTS.md`
ao script e instale os especialistas no ambiente correspondente. Regras específicas
do projeto e restrições de maior prioridade continuam valendo. O instalador de
Maestro e o de especialistas são etapas separadas: uma falha de sistema entre elas
pode deixar só uma etapa concluída; verifique a saída e execute novamente.

## Para quem está começando

> Quero uma demonstração local de organização de contatos, com dados fictícios.
> Escolha as etapas e os especialistas necessários. Explique de forma simples e
> confira o resultado. Não envie mensagens nem conecte serviços reais.

Maestro deve transformar o objetivo em passos verificáveis, fazer escolhas
reversíveis e perguntar apenas o que bloquear uma decisão importante.

## Para quem já desenvolve

> Implemente esta alteração preservando o contrato da API. Delegue implementação
> e revisão quando houver escopo independente. Defina a propriedade dos arquivos,
> confira os testes relevantes e apresente o diff e as limitações.

Ele deve respeitar arquitetura e versões existentes, evitar edições concorrentes
no mesmo arquivo e resolver divergências com evidências. Atlas ajuda em arquitetura;
Otto, em prioridades; o principal continua responsável pela integração.

## Habblaud e limites

“Ícaro” ou outro nome da sala pode ser apenas o personagem visual da sessão.
Mudar o nome para Maestro não instala comportamento. O comportamento vem das
instruções carregadas pelo Codex; o Habblaud acompanha sessões reais.

O pacote não renomeia personagens do Habblaud. Sem ferramentas de delegação,
Maestro executa etapas sequencialmente e informa a limitação. Não promete atividade
contínua, economia de tokens, integrações automáticas ou superioridade a outros modelos.

[Instruções completas](../coordinator/maestro.md) · [Verificação](validacao-maestro.md)

Fontes oficiais: [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
e [subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents).
