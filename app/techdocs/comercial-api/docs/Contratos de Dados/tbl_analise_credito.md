# tbl_analise_credito

Resultado da avaliação de crédito/restrição associada a um lead.

## Resumo

| Item | Valor |
|---|---|
| Domínio | Crédito/restrição |
| Origem schema | [[../Banco - air_comercial]] |
| Classe provável | `venda/model/AnaliseCredito.java` |
| Repository provável | `AnaliseCreditoRepository` |
| Dados sensíveis | Documento consultado, XML de retorno, validação cadastral, score/status SPC/Serasa |
| Fluxos principais | [[../Fluxos de Negocio/analise-credito]], [[../Fluxos de Negocio/vendas-e-migracoes]] |

## Campos principais

| Campo | Tipo | Papel |
|---|---|---|
| `id` | `bigint` | Identificador da análise. |
| `id_lead` | `bigint` | Lead avaliado. |
| `cpf_cnpj_consulta` | `varchar(18)` | Documento consultado; sensível. |
| `data_analise` | `datetime` | Momento da consulta/análise. |
| `numero_restricoes`, `valor_total` | vários | Resultado financeiro/restritivo. |
| `autorizado` | `tinyint` | Decisão de autorização. |
| `usuario_autorizador`, `data_autorizacao`, `justificativa_autorizacao` | vários | Auditoria da autorização. |
| `xml` | `longtext` | Retorno bruto/sensível de integração; evitar expor. |
| `integracao_*` | vários | Status/correlação da integração. |
| `validacao_*`, `situacao_documento` | vários | Dados de validação cadastral. |
| `nota_serasa`, `aprovado_serasa`, `status_serasa`, `aprovado_spc` | vários | Resultado de bureaus. |

## Índices e relações

| Tipo | Campos |
|---|---|
| PK | `id` |
| Índices relevantes | `id_lead`, `integracao_status`, `cpf_cnpj_consulta` |
| FK | `id_lead -> tbl_lead.id` |
| Tabelas filhas | `tbl_analise_credito_atributo`, `tbl_analise_credito_restricao` |

## Endpoints e queries relacionadas

| Uso | Referência |
|---|---|
| Consulta de análise por cliente | [[../Endpoints da Collection/get-cliente-analise-credito]] |
| Shape da análise | [[../Resultados SELECT/analisecreditorepository-findallbyleadclienteid]] |
| Atributos da análise | [[../Resultados SELECT/analisecreditoatributorepository-findallbyanalisecredito_id]] |
| Restrições da análise | [[../Resultados SELECT/analisecreditorestricaorepository-findallbyanalisecredito_id]] |

## Cuidados de mudança

- Não expor `xml`, documento ou resultado de bureau em exemplos.
- Mudança em status de integração afeta reprocessamento e diagnóstico.
- Mudança em campos de autorização exige auditoria clara.
- Revisar runbook de análise de crédito antes de alterar persistência ou retorno.
