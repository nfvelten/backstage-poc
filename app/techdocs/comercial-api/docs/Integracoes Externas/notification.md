---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integração - Notification API / WhatsApp / URA

- Finalidade: Envio de comunicação operacional/comercial e consulta de notificações WhatsApp.
- Política de documentação: Não registrar telefone real nem conteúdo personalizado real.

## Chamadores conhecidos

- `NotificationIntegracaoService`
- `NotificationApiProvider`
- `NotificationService`

## Fluxos relacionados

- [[../Fluxos de Negocio/notificacoes-whatsapp]]
- [[../Fluxos de Negocio/ativacao-servicos]]
- [[../Fluxos de Negocio/avisos-cliente-contrato]]

## Payload lógico

- cliente
- contrato
- telefone
- template/mensagem
- status de envio

## Falhas esperadas

- mensagem duplicada
- telefone inválido
- envio parcial
- template incorreto

## Revisar em mudança

- [[../Mapa de Reprocessamento]]
- [[../Dependencias e Integracoes]]
- [[../Operacional/Runbooks/Index]]
- [[../Operacional/Dados Sensiveis]] se houver cliente, documento, telefone, token ou crédito.
