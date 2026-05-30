---
tags:
  - trabalho
  - air
  - comercial-api
  - ciclo-de-vida
---
# Ciclo de Vida - Venda

## Estados

- criada
- em fase comercial
- em ativação
- confirmada
- cancelada
- não confirmada para operação

## Transições

| Transição | Fluxo | Tabelas/estado |
|---|---|---|
| Criar venda por integração | Criação de contrato / integração | `tbl_venda, tbl_venda_origem` |
| Adicionar itens/adicionais | Criação de contrato / integração | `tbl_venda_adicional` |
| Ativar serviços | Ativação de serviços | `tbl_venda, tbl_contrato, tbl_contrato_campanha` |
| Listar por natureza/fase | Vendas e migrações | `tbl_venda` |
| Consultar vendas do contrato | Vendas e migrações | `tbl_venda, tbl_venda_adicional` |

## Endpoints

- [[../Endpoints da Collection/post-criar-integracao]]
- [[../Endpoints da Collection/ativar-servicos]]
- [[../Endpoints da Collection/get-vendas-by-natureza]]
- [[../Endpoints da Collection/get-vendas-contrato]]

## Riscos de mudança

- ativação duplicada
- desconto recorrente duplicado
- fase incorreta
- notificação externa repetida

## Revisar junto

- [[../Matriz de Escrita por Tabela]]
- [[../Mapa de Reprocessamento]]
- [[../Services Criticos/Index]]
- [[../Playbooks de Mudanca]]
