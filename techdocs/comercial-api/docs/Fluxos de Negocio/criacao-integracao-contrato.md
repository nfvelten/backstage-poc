# Criação de contrato / integração

Gerado em: 2026-05-30 10:11:02

- Objetivo: Cria ou reaproveita cliente/lead/venda/contrato a partir da integração, normalmente vinda do CRM/Sydle.
- Risco operacional: `alto`
- Endpoints: 2
- Queries/operações mapeadas: 10
- Tabelas SQL identificadas: 6

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [post-criar-integracao.md](../Endpoints da Collection/post-criar-integracao.md) | `POST /contrato/criar-integracao` | `ContratoController.criarContrato` | `CadastrarIntegracaoDTO` | `ResponseEntity<?>` |
| [test-criar-integracao.md](../Endpoints da Collection/test-criar-integracao.md) | `POST /contrato/criar-integracao` | `ContratoController.criarContrato` | `CadastrarIntegracaoDTO` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `POST /contrato/criar-integracao`

- Assinatura: `public ResponseEntity<?> criarContrato(@RequestBody CadastrarIntegracaoDTO dto)`
- Campos do body Bruno: `idProcessoVendaSydle`, `fechamento`, `fechamentoDia`, `vencimento`, `vencimentoDia`, `pacoteCodigo`, `pacoteNome`, `statusCidadeConnectMaster`, `pontoReservaConnectMaster`, `workzone`, `usuario`, `classificacao`, `origemVenda`, `codigoVendedor`, `codigoTipoCobranca`, `contratoId`, `portabilidadeNumero`, `pacoteCodigoAnterior`, `observacao`, `ftta2`, `adhesionFeeValue`, `adhesionFeePaymentOption`, `adhesionFeePaymentMethod`, `valorTaxaAdesao`, `formaPagamentoTaxa`, `opcaoPagamentoTaxa`, `lead`, `tipo`, `nome`, `telefone`, `email`, `cpfCnpj`, `telefoneAdicional`, `emailAdicional`, `fonte`, `grupo`, `ftta`, `tratamento`, `dataNascimento`, `estadoCivil`

### `POST /contrato/criar-integracao`

- Assinatura: `public ResponseEntity<?> criarContrato(@RequestBody CadastrarIntegracaoDTO dto)`
- Campos do body Bruno: `idProcessoVendaSydle`, `fechamento`, `fechamentoDia`, `vencimento`, `vencimentoDia`, `pacoteCodigo`, `pacoteNome`, `statusCidadeConnectMaster`, `pontoReservaConnectMaster`, `workzone`, `usuario`, `classificacao`, `origemVenda`, `codigoVendedor`, `codigoTipoCobranca`, `contratoId`, `portabilidadeNumero`, `pacoteCodigoAnterior`, `observacao`, `ftta2`, `valorTaxaAdesao`, `formaPagamentoTaxa`, `opcaoPagamentoTaxa`, `lead`, `tipo`, `nome`, `telefone`, `email`, `cpfCnpj`, `telefoneAdicional`, `emailAdicional`, `fonte`, `grupo`, `ftta`, `tratamento`, `dataNascimento`, `estadoCivil`, `rgNumero`, `rgOrgao`, `nomeMae`

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `ClienteFisicoRepository.findTopByCpf` | `repository-derived-query` | `../JPA%20e%20Repositories.md#clientefisicorepository-findtopbycpf` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteFisicoRepository.findTopByCpf` |
| `ClienteJuridicoRepository.findTopByCnpj` | `repository-derived-query` | `../JPA%20e%20Repositories.md#clientejuridicorepository-findtopbycnpj` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ClienteService.criar -> ClienteJuridicoRepository.findTopByCnpj` |
| `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` | `repository-derived-query` | `../JPA%20e%20Repositories.md#contratocampanharepository-findtopbycontratoandcanceladaisfalseorderbyiddesc` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> ContratoService.criarContratoBaseNovoCRM -> ContratoCampanhaService.criar -> ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` |
| `EnderecoCidadeRepository.findCidadeBySigla` | `repository-native-query` | [enderecocidaderepository-findcidadebysigla.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/enderecocidaderepository-findcidadebysigla.sql) | [enderecocidaderepository-findcidadebysigla.md](../Resultados SELECT/enderecocidaderepository-findcidadebysigla.md) | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> EnderecoService.criarNovoCRM -> EnderecoCidadeRepository.findCidadeBySigla` |
| `VendaAdicionalRepository.save` | `repository-crud-operation` | `../JPA%20e%20Repositories.md#vendaadicionalrepository-save` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaAdicionalRepository.save` |
| `VendaOrigemRepository.save` | `repository-crud-operation` | `../JPA%20e%20Repositories.md#vendaorigemrepository-save` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaOrigemRepository.save` |
| `VendaRepository.buscarVendaNoAIR` | `repository-native-query` | [vendarepository-buscarvendanoair.sql](../../../../../../code/work/air-db-queries/comercial/comercial-api/collection-endpoints/vendarepository-buscarvendanoair.sql) | [vendarepository-buscarvendanoair.md](../Resultados SELECT/vendarepository-buscarvendanoair.md) | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.buscarVendaNoAIR -> VendaRepository.buscarVendaNoAIR` |
| `VendaRepository.findTopByIdProcessoVendaSydle` | `repository-derived-query` | `../JPA%20e%20Repositories.md#vendarepository-findtopbyidprocessovendasydle` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaBuilder.buildVendaNovoCRMIntegracao -> VendaService.findTopByIdProcessoVendaSydle -> VendaRepository.findTopByIdProcessoVendaSydle` |
| `VendedorRepository.findAllByIdVendedorSydle` | `repository-derived-query` | `../JPA%20e%20Repositories.md#vendedorrepository-findallbyidvendedorsydle` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findAllByIdVendedorSydle` |
| `VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` | `repository-derived-query` | `../JPA%20e%20Repositories.md#vendedorrepository-findtopbyusuariostartingwithandativoistrue` | - | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendedorService.buscarVendedorAir -> VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` |

## Tabelas tocadas por SQL nativo

- `air_chamado.tbl_chd_chamado`
- `air_chamado.tbl_os`
- `air_comercial.tbl_contrato`
- `air_comercial.tbl_endereco_cidade`
- `air_comercial.tbl_endereco_cidade_unidade`
- `air_comercial.tbl_venda`

## Efeitos colaterais e integrações

Endpoints com potencial efeito colateral:
- `POST /contrato/criar-integracao`
- `POST /contrato/criar-integracao`

Operações de escrita/CRUD identificadas:
- `VendaAdicionalRepository.save` (`repository-crud-operation`)
- `VendaOrigemRepository.save` (`repository-crud-operation`)

Integrações/sistemas citados no caminho ou SQL:
- Sydle

## Dados sensíveis

Sinais de dados sensíveis encontrados em nomes de campos, queries ou caminho:
- `Cnpj`
- `Cpf`
- `Endereco`
- `endereco`

## Pendências de mapeamento

- `LeadService.save`
- `RegraSuspensaoService.findOne`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
