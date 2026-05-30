---
tags:
  - trabalho
  - air
  - comercial-api
  - maturidade
---
# Score de Maturidade Documental - comercial-api

Score heurístico para priorizar melhoria documental por endpoint. Não mede qualidade do código nem uso real de produção.

| Endpoint | Score | Nível | Forças | Lacunas |
|---|---:|---|---|---|
| [[Endpoints da Collection/delete-oauth-remover|DELETE /oauth/remover/{{id}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; queries/operações mapeadas | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-cliente-por-id|GET /cliente/{{id}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; queries/operações mapeadas | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-cliente-analise-credito|GET /cliente/{{id}}/analise_credito]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; queries/operações mapeadas | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-cliente-blacklist|GET /cliente/{{id}}/blacklist]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; 1 chamada(s) resolvida(s) manualmente | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-cliente-consultar-avisos|GET /cliente/{{id}}/consultar_avisos]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente; queries/operações mapeadas | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-cliente-contato|GET /cliente/{{id}}/contato]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; consumer estático encontrado | sem queries/operações detectadas |
| [[Endpoints da Collection/get-cliente-contrato|GET /cliente/{{id}}/contrato]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente; queries/operações mapeadas; consumer estático encontrado | - |
| [[Endpoints da Collection/get-cliente-endereco|GET /cliente/{{id}}/endereco]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; queries/operações mapeadas | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-cliente-por-cpf|GET /cliente?cpfcnpj={{cpf}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; queries/operações mapeadas; consumer estático encontrado | - |
| [[Endpoints da Collection/get-contrato|GET /contrato/{{id}}]] | 85 | `forte` | controller/método mapeado; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente; queries/operações mapeadas | sem fluxo de negócio associado; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-contrato-aviso|GET /contrato/{{id}}/aviso]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; queries/operações mapeadas; consumer estático encontrado | - |
| [[Endpoints da Collection/get-migracoes-contrato|GET /contrato/{{id}}/migracao]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; 1 chamada(s) resolvida(s) manualmente | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-vendas-contrato|GET /contrato/{{id}}/venda]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-contracts-customer-basic-info|GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-contracts-detail|GET /v1/contracts/detail?contract_number={{contract_number}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; queries/operações mapeadas | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-elegibilidade-confianca|GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-contrato-svas-v1|GET /v1/contracts/{{id}}/svas]] | 85 | `forte` | ligado a fluxo de negócio; call graph sem pendência local | sem código mapeado; sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-wpp-notificacoes-listar|GET /wpp-notificacoes/listar/{{customerId}}]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; call graph sem pendência local; consumer estático encontrado | sem queries/operações detectadas |
| [[Endpoints da Collection/post-criar-integracao|POST /contrato/criar-integracao]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente; queries/operações mapeadas; payload documentado; sensibilidade de payload marcada; consumer estático encontrado | - |
| [[Endpoints da Collection/test-criar-integracao|POST /contrato/criar-integracao]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente; queries/operações mapeadas; payload documentado; sensibilidade de payload marcada; consumer estático encontrado | - |
| [[Endpoints da Collection/post-contrato-adicionar-aviso|POST /contrato/{{id}}/adicionar_aviso]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; queries/operações mapeadas; payload documentado | sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/post-oauth-integrar|POST /oauth/integrar]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; 2 chamada(s) resolvida(s) manualmente; payload documentado | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/get-vendas-by-natureza|PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC]] | 100 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; 1 chamada(s) resolvida(s) manualmente; payload documentado | sem queries/operações detectadas; sem consumer estático encontrado; validar com telemetria |
| [[Endpoints da Collection/ativar-servicos|PUT /venda/{{id_venda}}/ativar_servicos]] | 95 | `forte` | ligado a fluxo de negócio; controller/método mapeado; escrita com runbook; call graph sem pendência local; 1 chamada(s) resolvida(s) manualmente; queries/operações mapeadas | método de escrita sem body JSON na collection; sem consumer estático encontrado; validar com telemetria |

## Como usar

- Priorize endpoints com score menor e fluxo de risco alto/médio.
- `sem consumer estático` não significa rota morta; confirme em logs/APM/gateway.
- Score baixo por pendência de call graph indica necessidade de revisão manual do caminho service/repository.
