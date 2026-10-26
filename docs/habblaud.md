# Nomes no Habblaud

[English](habblaud.en.md) · [Voltar](../README.md)

Atlas, Luna, Nexo, Iris, Cora, Vero, Pixel, Frame, Nilo, Maia e Otto são os nomes dos perfis deste pacote no Codex. O Habblaud atribui nomes e aparências próprios às sessões. Essas duas coisas não são sincronizadas automaticamente por este instalador.

## Editar um personagem

Segundo a documentação do Habblaud:

1. Abra o Habblaud localmente no computador.
2. Clique no agente principal para abrir os detalhes.
3. Clique no lápis ao lado do nome, em **Editar personagem**.
4. Escolha o nome e a aparência e clique em **Salvar**.

A personalização vale para o personagem do projeto, não para uma regra que renomeia qualquer subagente. Uma segunda sessão simultânea no mesmo projeto pode receber outro personagem. O editor exige acesso local e o terminal habilitado. Não há neste pacote uma integração que force todos os nomes da imagem no Habblaud.

## Ver o Codex

O Habblaud oferece leitura dos registros locais do Codex. Para atualizações mais imediatas, o projeto documenta a instalação de hooks com `npm run codex:install` e aprovação em `/hooks` no Codex. Siga esses comandos **na instalação do Habblaud**, não neste repositório.

O Habblaud é opcional e não vem incluído no instalador dos onze perfis. O painel acompanha a atividade; não elimina o consumo do modelo. Mandar mensagens ou iniciar trabalho pelo painel pode provocar novo processamento.

[Documentação oficial do Habblaud](https://github.com/marmottajr/habblaud/blob/main/README.pt-BR.md#editar-o-personagem).

## Personalização local deste ambiente

No computador usado para preparar esta versão, o Habblaud 0.7.0 recebeu uma adaptação local que mapeia os onze perfis para nomes e funções, quando uma sessão real informa o papel correspondente. O teste do modelo de escritório cobre os onze nomes. Essa alteração não faz parte do instalador público e pode precisar ser reaplicada após atualizar o Habblaud. Não cria personagens trabalhando sem sessões reais.
