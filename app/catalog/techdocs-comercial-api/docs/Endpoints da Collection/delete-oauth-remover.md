# delete-oauth-remover.bru

- Rota: `DELETE /oauth/remover/{{id}}`
- Collection: `air-api-collection/comercial/delete-oauth-remover.bru`
- Codigo: `OauthController.remover` em `comercial-api/src/main/java/br/net/air/oauth/Controller/OauthController.java:41`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ClienteFisicoRepository.findOne` | `repository-crud-operation` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#clientefisicorepository-findone) | - | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> ClienteService.getDocumentoPorCliente -> ClienteFisicoRepository.findOne` |
| `ClienteJuridicoRepository.findOne` | `repository-crud-operation` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#clientejuridicorepository-findone) | - | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> ClienteService.getDocumentoPorCliente -> ClienteJuridicoRepository.findOne` |
| `sql.customer-brands` | `native-properties` | [sql-customer-brands.sql](../sql-customer-brands.sql) | [sql-customer-brands.md](../Resultados SELECT/sql-customer-brands.md) | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> OauthIntegracaoService.getBrands` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
