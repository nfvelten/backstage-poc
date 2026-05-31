---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integração - SPC / Serasa

- Finalidade: Consulta de crédito/restrição e persistência da análise financeira.
- Política de documentação: Não registrar XML, documento, score individual ou restrição real.

## Chamadores conhecidos

- `AnaliseCreditoService`
- `spc/soap`
- `RotinaConsultaSPC`

## Fluxos relacionados

- [[../Fluxos de Negocio/analise-credito]]

## Payload lógico

- documento
- dados cadastrais
- retorno de restrição
- atributos de análise

## Falhas esperadas

- indisponibilidade do bureau
- retorno parcial
- resultado divergente por reconsulta

## Revisar em mudança

- [[../Mapa de Reprocessamento]]
- [[../Dependencias e Integracoes]]
- [[../Operacional/Runbooks/Index]]
- [[../Operacional/Dados Sensiveis]] se houver cliente, documento, telefone, token ou crédito.
