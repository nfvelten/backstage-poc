# ativar-servicos.bru

- Rota: `PUT /venda/{{id_venda}}/ativar_servicos`
- Collection: `air-api-collection/comercial/ativar-servicos.bru`
- Codigo: `VendaController.ativarServicos` em `comercial-api/src/main/java/br/net/air/venda/controller/VendaController.java:269`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc) | - | `VendaController.ativarServicos -> ContratoService.salvarDescontoRecorrenteCampanha -> ContratoCampanhaService.buscarContratoCampanhaVigente -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `VendaOrigemRepository.findTopByVenda` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendaorigemrepository-findtopbyvenda) | - | `VendaController.ativarServicos -> VendaService.ativarServicos -> VendaOrigemService.getOrigemByVenda -> VendaOrigemRepository.findTopByVenda` |
| `sql.customer-brands` | `native-properties` | [sql-customer-brands.sql](../sql-customer-brands.sql) | [sql-customer-brands.md](../Resultados SELECT/sql-customer-brands.md) | `VendaController.ativarServicos -> VendaService.processarAtivacao -> VendaService.montarAtivacaoNotificationDTO -> OauthIntegracaoService.getBrands` |

## Chamadas ainda nao resolvidas

- `ContratoCampanhaService.save`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
