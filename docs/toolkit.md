# Adaptação do Vibe Coding Toolkit

[English](toolkit.en.md) · [Voltar](../README.md)

Base: [Matheus Gomes, revisão 790a895](https://github.com/soumatheusgomes/vibe-coding-toolkit/tree/790a895304e0c08b70a5b215c9d334f1c86b816c). A licença MIT foi preservada em [licenses](../licenses/VIBE-CODING-TOOLKIT-MIT.txt).

Adaptei os acordos de verificação, continuidade e passagem de trabalho de `templates/AGENTS.md.template` e `templates/task-handoff.md.template`. O guia `docs/07-harness-evaluation.md` orientou a distinção entre instalação, resposta do modelo e execução realmente observada.

As práticas estão dentro de cada TOML: não é necessário colar outro prompt para disponibilizá-las ao agente. A versão 2.0 contém onze perfis. Não incorpora o toolkit inteiro, plugins, MCPs, stack Next.js, hooks, mudança de modelo ou API paga.

O instalador não escreve um AGENTS.md global nem substitui instruções dos seus projetos. Ferramentas continuam dependendo do ambiente e das permissões reais. Perfil não instala editor de vídeo, gerador de imagem, navegador ou CRM.

Atualizações do toolkit são referências a revisar, não código executado automaticamente no seu computador. Registrar a versão de origem permite conferir exatamente o que foi adaptado. Nenhuma melhoria de inteligência, economia de tokens ou taxa de conversão é garantida.
