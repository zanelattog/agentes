# Usar sem decorar nomes

[English](usage.en.md) · [Voltar](../README.md)

Os nomes ajudam a pedir uma função específica, mas você pode explicar o objetivo em linguagem comum. Para delegar a especialistas, peça ao Codex explicitamente que use agentes e escolha os papéis necessários.

## Três jeitos

- **Direto:** “Use `cora` para revisar a segurança deste login. Não altere o código.”
- **Pelo objetivo:** “Use os agentes necessários para implementar e verificar este formulário. Evite trabalho duplicado.”
- **Com sugestão antes:** “Primeiro diga se esta tarefa precisa de especialistas. Se precisar, sugira quais e aguarde minha decisão.”

Pedir agentes não exige abrir seis conversas manualmente. O Codex coordena a delegação quando o recurso está disponível e habilitado. Os perfis precisam estar instalados no ambiente que atende à conversa; uma instalação no Mac não os instala automaticamente no Codex Cloud ou em outra máquina.

## Um combinado para a conversa

> Quando eu pedir algo simples, resolva direto. Para tarefas maiores, explique se vale a pena dividir o trabalho, sugira somente os especialistas necessários e me pergunte antes de chamá-los. Não use todos por padrão.

Você pode usar esse combinado uma vez no início do chat. Para persistir entre chats, ele precisa ser salvo nas instruções adequadas do projeto ou do cliente. Este pacote não altera essas instruções automaticamente.

Os nomes exatos são `atlas`, `luna`, `nexo`, `iris`, `cora` e `vero`. Se o Codex disser que não encontra um perfil, abra uma nova conversa e confira a instalação. Não peça que ele finja ter chamado um agente indisponível.

No Habblaud, personagens representam sessões reais. Eles não ficam todos na sala só porque os arquivos foram instalados; aparecem conforme a atividade e a integração disponível.

[Documentação oficial sobre delegação](https://learn.chatgpt.com/docs/agent-configuration/subagents).
