# tbl_venda

Venda representa o processo comercial que conecta lead, campanha, pacote, análise de crédito, contrato e ativação.

## Resumo

| Item | Valor |
|---|---|
| Domínio | Venda/ativação/migração |
| Origem schema | [[../Banco - air_comercial]] |
| Classe provável | `venda/model/Venda.java` |
| Repository provável | `VendaRepository` |
| Dados sensíveis | Valores comerciais, conta/agência, pacote, status de venda, vínculo com contrato/lead |
| Fluxos principais | [[../Fluxos de Negocio/vendas-e-migracoes]], [[../Fluxos de Negocio/ativacao-servicos]], [[../Fluxos de Negocio/criacao-integracao-contrato]] |

## Campos principais

| Campo | Tipo | Papel |
|---|---|---|
| `id` | `bigint` | Identificador da venda. |
| `natureza` | `varchar(255)` | Novo contrato, migração, adicional, troca etc. |
| `fase_atual` | `varchar(255)` | Fase atual do funil/processo. |
| `id_lead` | `bigint` | Lead da venda. |
| `id_contrato` | `bigint` | Contrato gerado/alterado. |
| `id_analise_credito` | `bigint` | Análise usada na venda. |
| `id_vendedor`, `id_campanha` | `bigint` | Responsabilidade/oferta comercial. |
| `pacote_*` | vários | Pacote base/up e valores. |
| `valor_total`, `valor_comissao` | `decimal` | Valores comerciais. |
| `concretizada`, `confirmada`, `cancelada` | `tinyint` | Estados principais. |
| `agencia`, `conta_corrente` | `varchar` | Dados financeiros sensíveis. |
| `id_processo_venda_sydle` | `varchar(255)` | Correlação com processo Sydle. |

## Índices e relações

| Tipo | Campos |
|---|---|
| PK | `id` |
| Índices relevantes | `id_processo_venda_sydle`, `id_analise_credito`, `id_campanha`, `id_contrato`, `id_endereco`, `equipe`, `id_lead`, `id_vendedor` |
| Relações fortes | `tbl_lead`, `tbl_contrato`, `tbl_analise_credito`, `tbl_venda_adicional`, `tbl_venda_fase`, `tbl_venda_origem` |

## Endpoints e queries relacionadas

| Uso | Referência |
|---|---|
| Ativação de serviços | [[../Endpoints da Collection/ativar-servicos]] |
| Vendas por contrato/natureza | [[../Endpoints da Collection/get-vendas-contrato]], [[../Endpoints da Collection/get-vendas-by-natureza]] |
| Criação via integração | [[../Endpoints da Collection/post-criar-integracao]] |
| Query por processo Sydle | [[../Resultados SELECT/vendarepository-buscarvendanoair]] |

## Cuidados de mudança

- Mudança em `natureza` ou `fase_atual` pode alterar fluxo comercial e ativação.
- Mudança em `id_processo_venda_sydle` impacta idempotência/correlação de integração.
- Campos de conta/agência não devem ser logados ou documentados com valores reais.
- Mudança em pacote/valor deve revisar integrações financeira/SAP/Sydle.
