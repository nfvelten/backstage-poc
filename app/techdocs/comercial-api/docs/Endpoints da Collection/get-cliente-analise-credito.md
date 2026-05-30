# get-cliente-analise-credito.bru

- Rota: `GET /cliente/{{id}}/analise_credito`
- Collection: `air-api-collection/comercial/get-cliente-analise-credito.bru`
- Codigo: `ClienteController.analisesCredito` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:310`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` | `repository-native-query` | [analisecreditoatributorepository-findallbyanalisecredito_id.sql](../analisecreditoatributorepository-findallbyanalisecredito_id.sql) | [analisecreditoatributorepository-findallbyanalisecredito_id.md](../Resultados SELECT/analisecreditoatributorepository-findallbyanalisecredito_id.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` |
| `AnaliseCreditoRepository.findAllByLeadClienteId` | `repository-native-query` | [analisecreditorepository-findallbyleadclienteid.sql](../analisecreditorepository-findallbyleadclienteid.sql) | [analisecreditorepository-findallbyleadclienteid.md](../Resultados SELECT/analisecreditorepository-findallbyleadclienteid.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoRepository.findAllByLeadClienteId` |
| `AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` | `repository-native-query` | [analisecreditorestricaorepository-findallbyanalisecredito_id.sql](../analisecreditorestricaorepository-findallbyanalisecredito_id.sql) | [analisecreditorestricaorepository-findallbyanalisecredito_id.md](../Resultados SELECT/analisecreditorestricaorepository-findallbyanalisecredito_id.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` |
| `CarteiraRepository.findCarteiraById` | `repository-native-query` | [carteirarepository-findcarteirabyid.sql](../carteirarepository-findcarteirabyid.sql) | [carteirarepository-findcarteirabyid.md](../Resultados SELECT/carteirarepository-findcarteirabyid.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> ClienteService.findClienteLeadByCodigo -> ClienteService.toClienteFisicoDto -> CarteiraService.findCarteiraById -> CarteiraRepository.findCarteiraById` |
| `ClienteRepository.findClienteById` | `repository-native-query` | [clienterepository-findclientebyid.sql](../clienterepository-findclientebyid.sql) | [clienterepository-findclientebyid.md](../Resultados SELECT/clienterepository-findclientebyid.md) | `ClienteController.analisesCredito -> AnaliseCreditoService.findAllByLeadClienteId -> ClienteService.findClienteLeadByCodigo -> ClienteRepository.findClienteById` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
