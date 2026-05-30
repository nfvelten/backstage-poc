---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integração - Sydle

- Finalidade: Origem/integração de processo comercial, criação de contrato, ativação e confiança.
- Política de documentação: Registrar campos lógicos e IDs técnicos mascarados; não registrar payload real de cliente.

## Chamadores conhecidos

- `ContratoService`
- `VendaService`
- `IntegracaoService`
- `HabilitarConfiancaService`
- `SydleConnection`

## Fluxos relacionados

- [[../Fluxos de Negocio/criacao-integracao-contrato]]
- [[../Fluxos de Negocio/ativacao-servicos]]

## Payload lógico

- identificador de processo
- cliente/lead
- contrato/venda
- pacotes/serviços
- status de integração

## Falhas esperadas

- timeout ou erro HTTP
- payload duplicado
- processo inexistente
- resposta parcial

## Revisar em mudança

- [[../Mapa de Reprocessamento]]
- [[../Dependencias e Integracoes]]
- [[../Operacional/Runbooks/Index]]
- [[../Operacional/Dados Sensiveis]] se houver cliente, documento, telefone, token ou crédito.
