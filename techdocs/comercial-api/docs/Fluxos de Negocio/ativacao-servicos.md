# Ativação de serviços

Gerado em: 2026-05-30 10:11:02

- Objetivo: Habilita serviços de uma venda/contrato, atualiza serviços técnicos, campanha/desconto e emite notificação de ativação.
- Risco operacional: `alto`
- Endpoints: 1
- Queries/operações mapeadas: 3
- Tabelas SQL identificadas: 2

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [ativar-servicos.md](../Endpoints da Collection/ativar-servicos.md) | `PUT /venda/{{id_venda}}/ativar_servicos` | `VendaController.ativarServicos` | `-` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `PUT /venda/{{id_venda}}/ativar_servicos`

- Assinatura: `public ResponseEntity<?> ativarServicos(@PathVariable("id") Venda venda)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `repository-derived-query` | `../JPA%20e%20Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc` | - | `VendaController.ativarServicos -> ContratoService.salvarDescontoRecorrenteCampanha -> ContratoCampanhaService.buscarContratoCampanhaVigente -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `VendaOrigemRepository.findTopByVenda` | `repository-derived-query` | `../JPA%20e%20Repositories.md#vendaorigemrepository-findtopbyvenda` | - | `VendaController.ativarServicos -> VendaService.ativarServicos -> VendaOrigemService.getOrigemByVenda -> VendaOrigemRepository.findTopByVenda` |
| `sql.customer-brands` | `native-properties` | [sql-customer-brands.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/sql-customer-brands.sql) | [sql-customer-brands.md](../Resultados SELECT/sql-customer-brands.md) | `VendaController.ativarServicos -> VendaService.processarAtivacao -> VendaService.montarAtivacaoNotificationDTO -> OauthIntegracaoService.getBrands` |

## Tabelas tocadas por SQL nativo

- `air_base.tbl_unidade`
- `air_comercial.tbl_contrato`

## Efeitos colaterais e integrações

Endpoints com potencial efeito colateral:
- `PUT /venda/{{id_venda}}/ativar_servicos`

Integrações/sistemas citados no caminho ou SQL:
- Keycloak/OAuth
- Notification

## Dados sensíveis

- Nenhum sinal forte identificado automaticamente.

## Pendências de mapeamento

- `ContratoCampanhaService.save`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
