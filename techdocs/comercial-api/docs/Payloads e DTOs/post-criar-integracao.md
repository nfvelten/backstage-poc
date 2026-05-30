# Payload - post-criar-integracao

- Rota: `POST /contrato/criar-integracao`
- Collection: `air-api-collection/comercial/post-criar-integracao.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Content-Type`

## Contexto da collection

Cria contrato pelo fluxo de integracao comercial.

  Codigo: ContratoController.criarIntegracao.
  Uso: simular ou reproduzir payload vindo de integracoes/Sydle/Novo CRM para criacao de contrato, lead, endereco e OS.
  Efeitos: pode criar/alterar cliente, contrato, venda, endereco, ordem de servico e dados de integracao. Executar apenas em ambiente correto.

## Campos do body

| Campo | Tipo inferido | Sensibilidade |
|---|---|---|
| `idProcessoVendaSydle` | `string/template` | - |
| `fechamento` | `integer` | - |
| `fechamentoDia` | `integer` | - |
| `vencimento` | `integer` | - |
| `vencimentoDia` | `integer` | - |
| `pacoteCodigo` | `string/template` | - |
| `pacoteNome` | `string/template` | - |
| `statusCidadeConnectMaster` | `string` | endereco |
| `pontoReservaConnectMaster` | `string/template` | - |
| `workzone` | `string/template` | - |
| `usuario` | `string` | - |
| `classificacao` | `string` | - |
| `origemVenda` | `string` | - |
| `codigoVendedor` | `string/template` | - |
| `codigoTipoCobranca` | `string/template` | financeiro |
| `contratoId` | `null` | - |
| `portabilidadeNumero` | `null` | endereco |
| `pacoteCodigoAnterior` | `null` | - |
| `observacao` | `string` | - |
| `ftta2` | `string/template` | - |
| `adhesionFeeValue` | `number` | - |
| `adhesionFeePaymentOption` | `string` | - |
| `adhesionFeePaymentMethod` | `string` | - |
| `valorTaxaAdesao` | `integer` | financeiro |
| `formaPagamentoTaxa` | `string` | financeiro |
| `opcaoPagamentoTaxa` | `string` | financeiro |
| `lead` | `object` | - |
| `lead.tipo` | `string` | - |
| `lead.nome` | `string/template` | - |
| `lead.telefone` | `string/template` | contato |
| `lead.email` | `string/template` | contato |
| `lead.cpfCnpj` | `string/template` | documento |
| `lead.telefoneAdicional` | `null` | contato |
| `lead.emailAdicional` | `null` | contato |
| `lead.fonte` | `string` | - |
| `lead.grupo` | `string` | - |
| `lead.ftta` | `boolean` | - |
| `lead.tratamento` | `string` | - |
| `lead.dataNascimento` | `string/template` | - |
| `lead.estadoCivil` | `string` | endereco |
| `lead.rgNumero` | `string/template` | endereco |
| `lead.rgOrgao` | `string` | - |
| `lead.nomeMae` | `string/template` | - |
| `lead.nomePai` | `string/template` | - |
| `lead.nomeFantasia` | `null` | - |
| `lead.inscricaoEstadual` | `string` | - |
| `lead.inscricaoMunicipal` | `string` | - |
| `lead.atividadePrincipal` | `string` | - |
| `lead.bairroNome` | `string/template` | endereco |
| `lead.cep` | `string/template` | endereco |
| `lead.unidade` | `string/template` | - |
| `lead.complemento` | `string/template` | endereco |
| `lead.tipoLogradouro` | `string` | endereco |
| `lead.logradouroNome` | `string/template` | endereco |
| `lead.latitude` | `null` | endereco |
| `lead.longitude` | `null` | endereco |
| `lead.numero` | `string/template` | endereco |
| `lead.referencia` | `string/template` | endereco |
| `lead.tipoResidencia` | `string` | - |
| `lead.justificativa` | `null` | - |
| `lead.autorizada` | `boolean` | - |
| `lead.endereco` | `object` | endereco |
| `lead.endereco.estado` | `string/template` | endereco |
| `lead.endereco.tipo` | `string` | endereco |
| `lead.endereco.numero` | `string/template` | endereco |
| `lead.endereco.bairro` | `string/template` | endereco |
| `lead.endereco.latitude` | `null` | endereco |
| `lead.endereco.codigoIbge` | `string/template` | endereco |
| `lead.endereco.tipoResidencia` | `string` | endereco |
| `lead.endereco.unidade` | `string/template` | endereco |
| `lead.endereco.ftta` | `boolean` | endereco |
| `lead.endereco.cep` | `string/template` | endereco |
| `lead.endereco.complemento` | `string/template` | endereco |
| `lead.endereco.logradouro` | `string/template` | endereco |
| `lead.endereco.cidadeNome` | `string/template` | endereco |
| `lead.endereco.referencia` | `string/template` | endereco |
| `lead.endereco.longitude` | `null` | endereco |
| `novoTitular` | `null` | - |
| `ordemServico` | `object` | - |
| `ordemServico.id` | `null` | - |
| `ordemServico.equipe` | `string` | - |
| `ordemServico.dataAgendamento` | `string/template` | - |
| `ordemServico.turno` | `string` | - |
| `ordemServico.servico` | `string` | - |
| `ordemServico.chamadoId` | `null` | - |
| `ordemServico.observacao` | `string` | - |
| `ordemServico.agendaId` | `null` | - |
| `ordemServico.idReservaOfficeTrack` | `string/template` | - |
| `ordemServico.pontoReservaConnectMaster` | `string/template` | - |
| `endereco` | `object` | endereco |
| `endereco.bairro` | `string/template` | endereco |
| `endereco.cep` | `string/template` | endereco |
| `endereco.unidade` | `string/template` | endereco |
| `endereco.complemento` | `string/template` | endereco |
| `endereco.logradouro` | `string/template` | endereco |
| `endereco.latitude` | `null` | endereco |
| `endereco.longitude` | `null` | endereco |
| `endereco.numero` | `string/template` | endereco |
| `endereco.referencia` | `string/template` | endereco |
| `endereco.tipo` | `string` | endereco |
| `endereco.codigoIbge` | `string/template` | endereco |
| `endereco.estado` | `string/template` | endereco |
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
