# Payload - test-criar-integracao

- Rota: `POST /contrato/criar-integracao`
- Collection: `air-api-collection/comercial/test-criar-integracao.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Content-Type`

## Contexto da collection

Payload de teste fechado para /contrato/criar-integracao.

  Codigo alvo: ContratoController.criarIntegracao.
  Uso: reproduzir cenario completo de criacao de contrato com dados fixos de HML/teste.
  Cuidado: contem dados de exemplo; revisar documento, pacote, vendedor, agenda, endereco e ambiente antes de executar.

## Campos do body

| Campo | Tipo inferido | Sensibilidade |
|---|---|---|
| `idProcessoVendaSydle` | `string` | - |
| `fechamento` | `integer` | - |
| `fechamentoDia` | `integer` | - |
| `vencimento` | `integer` | - |
| `vencimentoDia` | `integer` | - |
| `pacoteCodigo` | `string` | - |
| `pacoteNome` | `string` | - |
| `statusCidadeConnectMaster` | `string` | endereco |
| `pontoReservaConnectMaster` | `null` | - |
| `workzone` | `null` | - |
| `usuario` | `string` | - |
| `classificacao` | `string` | - |
| `origemVenda` | `string` | - |
| `codigoVendedor` | `string` | - |
| `codigoTipoCobranca` | `string` | financeiro |
| `contratoId` | `null` | - |
| `portabilidadeNumero` | `null` | endereco |
| `pacoteCodigoAnterior` | `null` | - |
| `observacao` | `string` | - |
| `ftta2` | `boolean` | - |
| `valorTaxaAdesao` | `integer` | financeiro |
| `formaPagamentoTaxa` | `string` | financeiro |
| `opcaoPagamentoTaxa` | `string` | financeiro |
| `lead` | `object` | - |
| `lead.tipo` | `string` | - |
| `lead.nome` | `string` | - |
| `lead.telefone` | `string` | contato |
| `lead.email` | `string` | contato |
| `lead.cpfCnpj` | `string` | documento |
| `lead.telefoneAdicional` | `null` | contato |
| `lead.emailAdicional` | `null` | contato |
| `lead.fonte` | `string` | - |
| `lead.grupo` | `string` | - |
| `lead.ftta` | `boolean` | - |
| `lead.tratamento` | `string` | - |
| `lead.dataNascimento` | `string` | - |
| `lead.estadoCivil` | `string` | endereco |
| `lead.rgNumero` | `string` | endereco |
| `lead.rgOrgao` | `string` | - |
| `lead.nomeMae` | `string` | - |
| `lead.nomePai` | `string` | - |
| `lead.nomeFantasia` | `null` | - |
| `lead.inscricaoEstadual` | `string` | - |
| `lead.inscricaoMunicipal` | `string` | - |
| `lead.atividadePrincipal` | `string` | - |
| `lead.bairroNome` | `string` | endereco |
| `lead.cep` | `string` | endereco |
| `lead.unidade` | `string` | - |
| `lead.complemento` | `string` | endereco |
| `lead.tipoLogradouro` | `string` | endereco |
| `lead.logradouroNome` | `string` | endereco |
| `lead.latitude` | `null` | endereco |
| `lead.longitude` | `null` | endereco |
| `lead.numero` | `string` | endereco |
| `lead.referencia` | `string` | endereco |
| `lead.tipoResidencia` | `string` | - |
| `lead.justificativa` | `null` | - |
| `lead.autorizada` | `boolean` | - |
| `lead.endereco` | `object` | endereco |
| `lead.endereco.estado` | `string` | endereco |
| `lead.endereco.tipo` | `string` | endereco |
| `lead.endereco.numero` | `string` | endereco |
| `lead.endereco.bairro` | `string` | endereco |
| `lead.endereco.latitude` | `null` | endereco |
| `lead.endereco.codigoIbge` | `integer` | endereco |
| `lead.endereco.tipoResidencia` | `string` | endereco |
| `lead.endereco.unidade` | `string` | endereco |
| `lead.endereco.ftta` | `boolean` | endereco |
| `lead.endereco.cep` | `string` | endereco |
| `lead.endereco.complemento` | `string` | endereco |
| `lead.endereco.logradouro` | `string` | endereco |
| `lead.endereco.cidadeNome` | `string` | endereco |
| `lead.endereco.referencia` | `string` | endereco |
| `lead.endereco.longitude` | `null` | endereco |
| `novoTitular` | `null` | - |
| `ordemServico` | `object` | - |
| `ordemServico.id` | `null` | - |
| `ordemServico.equipe` | `string` | - |
| `ordemServico.dataAgendamento` | `string` | - |
| `ordemServico.turno` | `string` | - |
| `ordemServico.servico` | `string` | - |
| `ordemServico.chamadoId` | `null` | - |
| `ordemServico.observacao` | `string` | - |
| `ordemServico.agendaId` | `null` | - |
| `ordemServico.idReservaOfficeTrack` | `null` | - |
| `ordemServico.pontoReservaConnectMaster` | `null` | - |
| `endereco` | `object` | endereco |
| `endereco.bairro` | `string` | endereco |
| `endereco.cep` | `string` | endereco |
| `endereco.unidade` | `string` | endereco |
| `endereco.complemento` | `string` | endereco |
| `endereco.logradouro` | `string` | endereco |
| `endereco.latitude` | `null` | endereco |
| `endereco.longitude` | `null` | endereco |
| `endereco.numero` | `string` | endereco |
| `endereco.referencia` | `string` | endereco |
| `endereco.tipo` | `string` | endereco |
| `endereco.codigoIbge` | `integer` | endereco |
| `endereco.estado` | `string` | endereco |
| `produtosPacote` | `array<object>` | - |
| `produtosPacote[].codigo` | `string` | - |
| `produtosPacote[].valor` | `number` | financeiro |
| `produtosPacote[].nome` | `string` | - |
| `produtosPacote[].itemGrupo` | `string` | - |
| `produtosAdicionais` | `array` | - |
| `descontos` | `array` | financeiro |
| `codigoChamadoAir` | `null` | - |
| `codigoOrdemServicoAir` | `null` | - |
| `codigoContratoAir` | `null` | - |

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
