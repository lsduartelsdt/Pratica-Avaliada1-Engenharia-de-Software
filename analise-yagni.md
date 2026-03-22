# Análise YAGNI

## Atributos desnecessários (exemplos)

- endereço
- telefone
- foto_perfil
- data_nascimento

Esses atributos não são necessários para login ou cadastro básico.

---

## Métodos desnecessários

- alterar_foto()
- enviar_email()
- gerar_relatorio()
- autenticação com múltiplos fatores

Não fazem parte dos requisitos atuais.

---

## Por que viola YAGNI?

O princípio YAGNI diz para não implementar algo que não é necessário agora. Esses itens aumentam complexidade sem gerar valor imediato.
