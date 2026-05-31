---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integração - OAuth / Keycloak / eCare

- Finalidade: Criação, remoção e reprocessamento de acesso/autenticação do cliente por marca/brand.
- Política de documentação: Nunca registrar token, senha, Authorization ou resposta com credencial.

## Chamadores conhecidos

- `OauthIntegracaoService`
- `KeycloakAuthClientImpl`
- `EcareClientImpl`

## Fluxos relacionados

- [[../Fluxos de Negocio/oauth-integracao]]
- [[../Fluxos de Negocio/ativacao-servicos]]

## Payload lógico

- cliente
- brand
- status de integração
- credenciais/tokens internos

## Falhas esperadas

- usuário ausente
- 404 tratado como ausência em alguns cenários
- falha de envio
- token inválido

## Revisar em mudança

- [[../Mapa de Reprocessamento]]
- [[../Dependencias e Integracoes]]
- [[../Operacional/Runbooks/Index]]
- [[../Operacional/Dados Sensiveis]] se houver cliente, documento, telefone, token ou crédito.
