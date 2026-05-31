# Análise de crédito

Gerado em: 2026-05-30 10:11:02

- Objetivo: Lista análises, atributos e restrições de crédito associadas ao cliente/lead.
- Risco operacional: `alto`
- Endpoints: 1
- Queries/operações mapeadas: 5
- Tabelas SQL identificadas: 9

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-cliente-analise-credito.md](../Endpoints da Collection/get-cliente-analise-credito.md) | `GET /cliente/{{id}}/analise_credito` | `ClienteController.analisesCredito` | `-` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `GET /cliente/{{id}}/analise_credito`

- Assinatura: `public ResponseEntity<?> analisesCredito(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` | `repository-native-query` | [analisecreditoatributorepository-findallbyanalisecredito_id.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/analisecreditoatributorepository-findallbyanalisecredito_id.sql) | [analisecreditoatributorepository-findallbyanalisecredito_id.md](../Resultados SELECT/analisecreditoatributorepository-findallbyanalisecredito_id.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` |
| `AnaliseCreditoRepository.findAllByLeadClienteId` | `repository-native-query` | [analisecreditorepository-findallbyleadclienteid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/analisecreditorepository-findallbyleadclienteid.sql) | [analisecreditorepository-findallbyleadclienteid.md](../Resultados SELECT/analisecreditorepository-findallbyleadclienteid.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoRepository.findAllByLeadClienteId` |
| `AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` | `repository-native-query` | [analisecreditorestricaorepository-findallbyanalisecredito_id.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/analisecreditorestricaorepository-findallbyanalisecredito_id.sql) | [analisecreditorestricaorepository-findallbyanalisecredito_id.md](../Resultados SELECT/analisecreditorestricaorepository-findallbyanalisecredito_id.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` |
| `CarteiraRepository.findCarteiraById` | `repository-native-query` | [carteirarepository-findcarteirabyid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/carteirarepository-findcarteirabyid.sql) | [carteirarepository-findcarteirabyid.md](../Resultados SELECT/carteirarepository-findcarteirabyid.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> ClienteService.findClienteLeadByCodigo -> ClienteService.toClienteFisicoDto -> CarteiraService.findCarteiraById -> CarteiraRepository.findCarteiraById` |
| `ClienteRepository.findClienteById` | `repository-native-query` | [clienterepository-findclientebyid.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/clienterepository-findclientebyid.sql) | [clienterepository-findclientebyid.md](../Resultados SELECT/clienterepository-findclientebyid.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> ClienteService.findClienteLeadByCodigo -> ClienteRepository.findClienteById` |

## Tabelas tocadas por SQL nativo

- `tbl_analise_credito`
- `tbl_analise_credito_atributo`
- `tbl_analise_credito_restricao`
- `tbl_carteira`
- `tbl_cliente`
- `tbl_cliente_fisico`
- `tbl_cliente_juridico`
- `tbl_lead`
- `tbl_vendedor`

## Efeitos colaterais e integrações

- Nenhuma integração externa forte identificada automaticamente.

## Dados sensíveis

Sinais de dados sensíveis encontrados em nomes de campos, queries ou caminho:
- `Credito`
- `credito`

## Pendências de mapeamento

- Nenhuma chamada pendente neste fluxo.

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
