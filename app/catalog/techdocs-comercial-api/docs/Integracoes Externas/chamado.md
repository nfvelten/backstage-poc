---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integração - Chamado / OS

- Finalidade: Criação e consulta de chamados/ordens ligados a venda, contrato e atendimento.
- Política de documentação: Não registrar protocolo real de cliente nem descrição real de atendimento.

## Chamadores conhecidos

- `ChamadoService`
- `queries air_chamado`

## Fluxos relacionados

- [[../Fluxos de Negocio/criacao-integracao-contrato]]
- [[../Fluxos de Negocio/avisos-cliente-contrato]]

## Payload lógico

- cliente
- contrato
- tipo de chamado
- protocolo
- status

## Falhas esperadas

- chamado duplicado
- protocolo ausente
- consulta cross-schema divergente

## Revisar em mudança

- [[../Mapa de Reprocessamento]]
- [[../Dependencias e Integracoes]]
- [[../Operacional/Runbooks/Index]]
- [[../Operacional/Dados Sensiveis]] se houver cliente, documento, telefone, token ou crédito.
