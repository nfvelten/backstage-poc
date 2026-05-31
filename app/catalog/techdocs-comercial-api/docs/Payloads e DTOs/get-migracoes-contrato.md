# Payload - get-migracoes-contrato

- Rota: `GET /contrato/{{id}}/migracao`
- Collection: `air-api-collection/comercial/get-migracoes-contrato.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Lista migracoes vinculadas ao contrato.

  Codigo: ContratoController.migracoes.
  Filtro: contrato.id e venda.excluido=false.
  Uso comum: investigar troca de plano, migracao adicional, migracao compulsoria e historico de versoes do contrato.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
