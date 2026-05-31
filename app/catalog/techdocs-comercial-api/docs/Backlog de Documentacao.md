---
tags:
  - trabalho
  - air
  - comercial-api
  - backlog
---
# Backlog de Documentacao - comercial-api

Backlog gerado a partir de score, pendências de call graph, escrita, fluxo e busca estática de consumers.

| Prioridade | Escopo | Endpoint | Item | Contexto |
|---|---|---|---|---|
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/ativar-servicos|PUT /venda/{{id_venda}}/ativar_servicos]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/delete-oauth-remover|DELETE /oauth/remover/{{id}}]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-cliente-analise-credito|GET /cliente/{{id}}/analise_credito]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-cliente-blacklist|GET /cliente/{{id}}/blacklist]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-cliente-consultar-avisos|GET /cliente/{{id}}/consultar_avisos]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-cliente-endereco|GET /cliente/{{id}}/endereco]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-cliente-por-id|GET /cliente/{{id}}]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-contracts-customer-basic-info|GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-contracts-detail|GET /v1/contracts/detail?contract_number={{contract_number}}]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-contrato-svas-v1|GET /v1/contracts/{{id}}/svas]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-contrato|GET /contrato/{{id}}]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-elegibilidade-confianca|GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-migracoes-contrato|GET /contrato/{{id}}/migracao]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-vendas-by-natureza|PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/get-vendas-contrato|GET /contrato/{{id}}/venda]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/post-contrato-adicionar-aviso|POST /contrato/{{id}}/adicionar_aviso]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |
| `P2` | `fora do escopo atual` | `[[Endpoints da Collection/post-oauth-integrar|POST /oauth/integrar]]` | Validar uso real com telemetria | Busca estática não encontrou consumer; confirmar antes de marcar como candidato a remoção. |

## Critério

- `P0`: risco alto, escrita crítica ou pendência que atrapalha operação.
- `P1`: lacuna relevante em fluxo médio/baixo ou call graph incompleto.
- `P2`: validação complementar, principalmente telemetria/uso real.
- Itens marcados como `fora do escopo atual` dependem de logs/APM/gateway e não foram executados nesta rodada.
