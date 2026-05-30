---
tags:
  - trabalho
  - air
  - comercial-api
  - ciclo-de-vida
---
# Ciclo de Vida - Cliente

## Estados

- prospect/lead relacionado
- cliente criado ou localizado
- contatos e endereços associados
- contratos vinculados
- integração OAuth/eCare pendente ou processada

## Transições

| Transição | Fluxo | Tabelas/estado |
|---|---|---|
| Criar/localizar cliente | Criação de contrato / integração | `tbl_cliente, tbl_cliente_fisico, tbl_cliente_juridico` |
| Atualizar endereço/contato | Criação de contrato / integração ou manutenção cadastral | `tbl_endereco, contato` |
| Vincular contrato | Criação de contrato / integração | `tbl_contrato` |
| Marcar integração OAuth | OAuth / Keycloak | `tbl_cliente.integracao_status` |
| Consultar avisos/contratos | Consulta cliente / avisos | `queries cross-schema e tbl_contrato` |

## Endpoints

- [[../Endpoints da Collection/get-cliente-por-id]]
- [[../Endpoints da Collection/get-cliente-por-cpf]]
- [[../Endpoints da Collection/get-cliente-contrato]]
- [[../Endpoints da Collection/get-cliente-consultar-avisos]]
- [[../Endpoints da Collection/post-oauth-integrar]]

## Riscos de mudança

- exposição de PII
- estado OAuth incorreto
- duplicidade cadastral
- contrato associado ao cliente errado

## Revisar junto

- [[../Matriz de Escrita por Tabela]]
- [[../Mapa de Reprocessamento]]
- [[../Services Criticos/Index]]
- [[../Playbooks de Mudanca]]
