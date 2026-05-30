# Payload - post-oauth-integrar

- Rota: `POST /oauth/integrar`
- Collection: `air-api-collection/comercial/post-oauth-integrar.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Content-Type`

## Contexto da collection

Dispara integracao manual de clientes no OAuth/Keycloak.

  Codigo: OauthController.integrarManual -> OauthIntegracaoService.integrarManual.
  Uso: reprocessar clientes com falha de integracao ou criar usuario SSO manualmente.
  Cuidado: para processamento massivo, o proprio codigo alerta para espacamento minimo de 1 segundo entre requisicoes para evitar DoS no Keycloak.

## Campos do body

| Campo | Tipo inferido | Sensibilidade |
|---|---|---|
| `idClientes` | `array<string/template>` | - |

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
