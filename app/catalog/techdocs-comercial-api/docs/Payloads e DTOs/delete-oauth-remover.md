# Payload - delete-oauth-remover

- Rota: `DELETE /oauth/remover/{{id}}`
- Collection: `air-api-collection/comercial/delete-oauth-remover.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`

## Contexto da collection

Remove um cliente da integracao OAuth/Keycloak por ID do cliente AIR.

  Codigo: OauthController.remover -> OauthIntegracaoService.removerClientePorBrands.
  Uso: correcao operacional quando usuario/brand precisa ser removido do SSO.
  Cuidado: endpoint tem efeito destrutivo no vinculo OAuth; validar cliente e ambiente antes de executar.

## Campos do body

- Sem body JSON documentado na collection.

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
