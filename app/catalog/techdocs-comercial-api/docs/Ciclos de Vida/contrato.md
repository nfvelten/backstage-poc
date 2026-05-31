---
tags:
  - trabalho
  - air
  - comercial-api
  - ciclo-de-vida
---
# Ciclo de Vida - Contrato

## Estados

- base criada
- produtos/itens associados
- campanha/desconto aplicado
- ativo ou em ativação
- com avisos/migrações/SVAs consultáveis

## Transições

| Transição | Fluxo | Tabelas/estado |
|---|---|---|
| Criar contrato | Criação de contrato / integração | `tbl_contrato` |
| Associar produtos e itens | Detalhe de contrato | `tbl_contrato_produto, tbl_contrato_item` |
| Aplicar campanha/desconto | Ativação de serviços | `tbl_contrato_campanha` |
| Adicionar aviso | Avisos cliente/contrato | `tabelas de aviso/contrato` |
| Registrar/consultar migração | Vendas e migrações | `tbl_contrato_migracao` |
| Consultar SVA | Contracts v1 SVAs | `tbl_contrato*` |

## Endpoints

- [[../Endpoints da Collection/get-contrato]]
- [[../Endpoints da Collection/get-cliente-contrato]]
- [[../Endpoints da Collection/post-contrato-adicionar-aviso]]
- [[../Endpoints da Collection/get-migracoes-contrato]]
- [[../Endpoints da Collection/get-contrato-svas-v1]]
- [[../Endpoints da Collection/ativar-servicos]]

## Riscos de mudança

- mudança de versão indevida
- produto/item inconsistente
- migração errada
- brand incorreta em OAuth

## Revisar junto

- [[../Matriz de Escrita por Tabela]]
- [[../Mapa de Reprocessamento]]
- [[../Services Criticos/Index]]
- [[../Playbooks de Mudanca]]
