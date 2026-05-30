# Payload - get-wpp-notificacoes-listar

- Rota: `GET /wpp-notificacoes/listar/{{customerId}}`
- Collection: `air-api-collection/comercial/get-wpp-notificacoes-listar.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /wpp-notificacoes/listar/{customerId} (15.646 sucessos no print).

  Codigo: NotificationController.listar -> NotificationIntegracaoService.consultarContatos.
  Uso: lista contatos WhatsApp vinculados ao cliente/customerId via integracao de notificacoes.
  Variavel: customerId = ID do cliente no AIR usado como customerId na Notification API.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
