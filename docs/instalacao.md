# Instalação detalhada

[English](installation.en.md) · [Voltar](../README.md)

Para instalar também o Maestro como comportamento do agente principal, abra **Instalar Maestro.command**. Requer Python 3.9+ e acrescenta instruções identificadas ao AGENTS.md pessoal, preservando o restante. [Detalhes](maestro.md).

### Esta seleção: Mac Intel ou Apple Silicon

1. Clique em [**Baixar os agentes**](https://github.com/zanelattog/agentes/archive/refs/heads/main.zip). Também pode usar **Code → Download ZIP** no GitHub.
2. No Finder, abra **Downloads** e extraia o ZIP.
3. Abra a pasta extraída e dê dois cliques em **Instalar.command**.
4. O Terminal mostrará o destino e o resultado. Aguarde **Concluído**.
5. Abra uma nova conversa no Codex, dentro do projeto em que quer trabalhar.
6. Peça um agente pelo nome, usando um dos exemplos abaixo.

O botão baixa os arquivos; a instalação acontece ao abrir o instalador no computador. O macOS pode pedir confirmação para abrir um arquivo baixado. Não é um aplicativo assinado. Se não abrir com dois cliques, abra o Terminal, digite `bash `, arraste `Instalar.command` para a janela e pressione Enter.

O instalador usa o Bash do macOS, sem bibliotecas adicionais. Copia somente os onze perfis para `~/.codex/agents` (ou `$CODEX_HOME/agents`, quando configurado). Não chama modelos, não instala o Codex ou o Habblaud e não altera permissões, modelos ou `config.toml`. Versões anteriores conhecidas, identificadas por SHA-256, são atualizadas com backup em `~/.codex/agents/.agentes-backups/`. Arquivos com edições pessoais ou origem desconhecida interrompem a instalação antes de alterar qualquer perfil.

Precisa de uma versão do Codex com suporte a agentes personalizados e uma conta configurada. Se o perfil não aparecer, reinicie o aplicativo e confira se agentes estão habilitados na sua configuração. [Referência oficial](https://learn.chatgpt.com/docs/agent-configuration/subagents).

<details>
<summary>Terminal, instalação por projeto e remoção</summary>

Na pasta extraída:

```bash
# Ver o que seria instalado, sem alterar nada
bash scripts/install.sh --dry-run

# Instalar apenas para um projeto: substitua o caminho
bash scripts/install.sh --dest "/caminho/do/projeto/.codex/agents"

# Remover os perfis desta seleção da instalação pessoal
bash scripts/install.sh --uninstall
```

Para remover de um projeto, use também `--dest` com o mesmo destino. A remoção para se encontrar um perfil modificado, preservando seus ajustes. Para atualizar, baixe novamente o ZIP do repositório e execute o instalador novo. Ele instala a versão contida nesse download; não busca atualizações em segundo plano, nem sincroniza automaticamente com os projetos originais. O backup preserva o conteúdo anterior; confira os arquivos antes de restaurá-los.

No Linux, use `bash scripts/install.sh`. No Windows, copie os onze arquivos de `agents/` para a pasta de agentes da instalação do Codex que você usa; o instalador de dois cliques deste pacote é para macOS.

</details>

### Catálogo original: pelo Agency Agents App

**O aplicativo original também atende ao Codex.** Pastas ou exemplos de Claude Code não significam que ele seja exclusivo do Claude.

1. Abra [Agency Agents App → Releases](https://github.com/msitarzewski/agency-agents-app/releases/latest).
2. Em **Assets**, escolha o `.dmg` `aarch64` para Mac Apple Silicon ou `x64` para Intel.
3. Abra o arquivo, instale o aplicativo e abra **Agency Agents**.
4. Em **Agents**, escolha os especialistas; em **Teams**, você pode explorar equipes prontas.
5. Abra a ação de instalação/deploy da seleção e escolha **Codex** como ferramenta de destino.
6. Confira o resultado e inicie uma nova conversa no Codex. Consulte o **Playbook** do aplicativo para exemplos de uso.

Os nomes dos controles podem mudar entre versões. Esse caminho instala perfis do **catálogo original**, não as onze adaptações deste repositório. A instalação disponibiliza instruções; a execução acontece no Codex. [Documentação do aplicativo](https://github.com/msitarzewski/agency-agents-app).
