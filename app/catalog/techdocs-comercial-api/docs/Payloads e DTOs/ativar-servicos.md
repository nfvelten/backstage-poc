# Payload - ativar-servicos

- Rota: `PUT /venda/{{id_venda}}/ativar_servicos`
- Collection: `air-api-collection/comercial/ativar-servicos.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Habilita o contrato no AIR a partir do ID da venda.

  O contrato precisa estar com vendaFase = FASE_ATIVACAO.
  A venda pode ter confirmada = true e não aparecer na interface — usar este endpoint diretamente.

  Efeitos:
  - status do contrato → ST_CONT_HABILITADO
  - dataPrimeiraAtivacao preenchida com data atual
  - Emite EVT_CONTRATO_SERVICOS_ATIVADOS
  - Notifica /notification/v1/activations

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
