# OAuth / Keycloak

Gerado em: 2026-05-30 10:11:02

- Objetivo: Integra ou remove cliente em OAuth/Keycloak e consulta marcas/regionais associadas.
- Risco operacional: `alto`
- Endpoints: 2
- Queries/operações mapeadas: 3
- Tabelas SQL identificadas: 2

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [post-oauth-integrar.md](../Endpoints da Collection/post-oauth-integrar.md) | `POST /oauth/integrar` | `OauthController.integrarManual` | `IntegracaoRequest` | `ResponseEntity<IntegracaoResponse>` |
| [delete-oauth-remover.md](../Endpoints da Collection/delete-oauth-remover.md) | `DELETE /oauth/remover/{{id}}` | `OauthController.remover` | `-` | `ResponseEntity<Void>` |

## Contrato HTTP observado

### `POST /oauth/integrar`

- Assinatura: `public ResponseEntity<IntegracaoResponse> integrarManual(@RequestBody IntegracaoRequest request)`
- Campos do body Bruno: `idClientes`

### `DELETE /oauth/remover/{{id}}`

- Assinatura: `public ResponseEntity<Void> remover(@PathVariable Cliente cliente)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `ClienteFisicoRepository.findOne` | `repository-crud-operation` | `../JPA%20e%20Repositories.md#clientefisicorepository-findone` | - | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> ClienteService.getDocumentoPorCliente -> ClienteFisicoRepository.findOne` |
| `ClienteJuridicoRepository.findOne` | `repository-crud-operation` | `../JPA%20e%20Repositories.md#clientejuridicorepository-findone` | - | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> ClienteService.getDocumentoPorCliente -> ClienteJuridicoRepository.findOne` |
| `sql.customer-brands` | `native-properties` | [sql-customer-brands.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-customer-brands.sql) | [sql-customer-brands.md](../Resultados SELECT/sql-customer-brands.md) | `OauthController.remover -> OauthIntegracaoService.removerClientePorBrands -> OauthIntegracaoService.getBrands` |

## Tabelas tocadas por SQL nativo

- `air_base.tbl_unidade`
- `air_comercial.tbl_contrato`

## Efeitos colaterais e integrações

Endpoints com potencial efeito colateral:
- `POST /oauth/integrar`
- `DELETE /oauth/remover/{{id}}`

Operações de escrita/CRUD identificadas:
- `ClienteFisicoRepository.findOne` (`repository-crud-operation`)
- `ClienteJuridicoRepository.findOne` (`repository-crud-operation`)

Integrações/sistemas citados no caminho ou SQL:
- Keycloak/OAuth

## Dados sensíveis

Sinais de dados sensíveis encontrados em nomes de campos, queries ou caminho:
- `Document`

## Pendências de mapeamento

- `ClienteService.findOne`
- `ClienteService.save`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
