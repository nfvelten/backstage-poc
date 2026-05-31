---
tags:
  - trabalho
  - air
  - comercial-api
  - ciclo-de-vida
---
# Ciclo de Vida - Lead

## Estados

- novo
- em negociação
- em ativação
- convertido em venda/contrato
- não viável ou não qualificado

## Transições

| Transição | Fluxo | Tabelas/estado |
|---|---|---|
| Receber dados de integração | Criação de contrato / integração | `tbl_lead` |
| Consultar análise de crédito | Análise de crédito | `tbl_analise_credito*` |
| Converter em venda | Criação de contrato / integração | `tbl_venda` |
| Associar cliente | Criação de contrato / integração | `tbl_cliente` |

## Endpoints

- [[../Endpoints da Collection/post-criar-integracao]]
- [[../Endpoints da Collection/test-criar-integracao]]
- [[../Endpoints da Collection/get-cliente-analise-credito]]

## Riscos de mudança

- dados pessoais no payload
- decisão de crédito sobrescrita
- lead duplicado por integração repetida

## Revisar junto

- [[../Matriz de Escrita por Tabela]]
- [[../Mapa de Reprocessamento]]
- [[../Services Criticos/Index]]
- [[../Playbooks de Mudanca]]
