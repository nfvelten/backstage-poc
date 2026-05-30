# post-criar-integracao.bru

- Rota: `POST /contrato/criar-integracao`
- Collection: `air-api-collection/comercial/post-criar-integracao.bru`
- Codigo: `ContratoController.criarContrato` em `comercial-api/src/main/java/br/net/air/cliente/controller/ContratoController.java:591`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ClienteFisicoRepository.findTopByCpf` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#clientefisicorepository-findtopbycpf) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteFisicoRepository.findTopByCpf` |
| `ClienteJuridicoRepository.findTopByCnpj` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#clientejuridicorepository-findtopbycnpj) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteJuridicoRepository.findTopByCnpj` |
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ContratoService.criarContratoBaseNovoCRM -> ContratoCampanhaService.criar -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `EnderecoCidadeRepository.findCidadeBySigla` | `repository-native-query` | [enderecocidaderepository-findcidadebysigla.sql](../enderecocidaderepository-findcidadebysigla.sql) | [enderecocidaderepository-findcidadebysigla.md](../Resultados SELECT/enderecocidaderepository-findcidadebysigla.md) | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> EnderecoService.criarNovoCRM -> EnderecoCidadeRepository.findCidadeBySigla` |
| `VendaAdicionalRepository.save` | `repository-crud-operation` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendaadicionalrepository-save) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaAdicionalRepository.save` |
| `VendaOrigemRepository.save` | `repository-crud-operation` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendaorigemrepository-save) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaOrigemRepository.save` |
| `VendaRepository.buscarVendaNoAIR` | `repository-native-query` | [vendarepository-buscarvendanoair.sql](../vendarepository-buscarvendanoair.sql) | [vendarepository-buscarvendanoair.md](../Resultados SELECT/vendarepository-buscarvendanoair.md) | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.buscarVendaNoAIR -> VendaRepository.buscarVendaNoAIR` |
| `VendaRepository.findTopByIdProcessoVendaSydle` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendarepository-findtopbyidprocessovendasydle) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaBuilder.buildVendaNovoCRMIntegracao -> VendaService.findTopByIdProcessoVendaSydle -> VendaRepository.findTopByIdProcessoVendaSydle` |
| `VendedorRepository.findAllByIdVendedorSydle` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendedorrepository-findallbyidvendedorsydle) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findAllByIdVendedorSydle` |
| `VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` | `repository-derived-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#vendedorrepository-findtopbyusuariostartingwithandativoistrue) | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` |

## Chamadas ainda nao resolvidas

- `LeadService.save`
- `RegraSuspensaoService.findOne`

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
