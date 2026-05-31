---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integração - ConnectMaster

- Finalidade: Integrações e rotina de cancelamento/serviços técnicos.
- Política de documentação: Documentar estados, não payload real enviado ao fornecedor.

## Chamadores conhecidos

- `ConnectMasterIntegracaoService`
- `RotinaCancelamento`

## Fluxos relacionados

- [[../Fluxos de Negocio/criacao-integracao-contrato]]
- [[../Fluxos de Negocio/ativacao-servicos]]

## Payload lógico

- contrato
- serviço técnico
- status/cancelamento

## Falhas esperadas

- efeito externo parcial
- cancelamento repetido
- timeout

## Revisar em mudança

- [[../Mapa de Reprocessamento]]
- [[../Dependencias e Integracoes]]
- [[../Operacional/Runbooks/Index]]
- [[../Operacional/Dados Sensiveis]] se houver cliente, documento, telefone, token ou crédito.
