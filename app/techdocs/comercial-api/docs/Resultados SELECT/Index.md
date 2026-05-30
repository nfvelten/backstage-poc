# Resultado das Queries SELECT - comercial-api

Gerado em: 2026-05-29 22:13:44

Fonte: arquivos `.sql` em `air-db-queries/comercial/comercial-api/collection-endpoints`.

Metodo: cada query foi executada no prod main como `SELECT * FROM (<query>) codex_shape LIMIT 0`, com parametros trocados por valores neutros. Isso captura apenas os nomes das colunas, sem retornar linhas de dados.

Observacao: o tipo SQL exato nao foi inferido porque a conexao nao tem permissao para criar tabela temporaria de introspeccao. Para queries JPA derivadas, consulte `JPA e Repositories.md`.

## Resumo

- SELECTs analisados: 22
- Nao SELECTs ignorados: 0

## Indice por query

| Query | Colunas | Status |
|---|---:|---|
| [analisecreditoatributorepository-findallbyanalisecredito_id.sql](Resultados SELECT/analisecreditoatributorepository-findallbyanalisecredito_id.md) | 4 | ok |
| [analisecreditorepository-findallbyleadclienteid.sql](Resultados SELECT/analisecreditorepository-findallbyleadclienteid.md) | 90 | ok |
| [analisecreditorestricaorepository-findallbyanalisecredito_id.sql](Resultados SELECT/analisecreditorestricaorepository-findallbyanalisecredito_id.md) | 8 | ok |
| [carteirarepository-findcarteirabyid.sql](Resultados SELECT/carteirarepository-findcarteirabyid.md) | 28 | ok |
| [clienterepository-findclientebyid.sql](Resultados SELECT/clienterepository-findclientebyid.md) | 42 | ok |
| [enderecocidaderepository-findcidadebysigla.sql](Resultados SELECT/enderecocidaderepository-findcidadebysigla.md) | 13 | ok |
| [enderecorepository-findallenderecosbycliente.sql](Resultados SELECT/enderecorepository-findallenderecosbycliente.md) | 96 | ok |
| [sql-aviso-rede-backbone.sql](Resultados SELECT/sql-aviso-rede-backbone.md) | 12 | ok |
| [sql-aviso-rede-manual.sql](Resultados SELECT/sql-aviso-rede-manual.md) | 12 | ok |
| [sql-aviso-rede-monitorado.sql](Resultados SELECT/sql-aviso-rede-monitorado.md) | 14 | ok |
| [sql-aviso-rede-nao-monitorado.sql](Resultados SELECT/sql-aviso-rede-nao-monitorado.md) | 12 | ok |
| [sql-aviso-telefonia.sql](Resultados SELECT/sql-aviso-telefonia.md) | 12 | ok |
| [sql-buscarclientecontrato.sql](Resultados SELECT/sql-buscarclientecontrato.md) | 1 | ok |
| [sql-buscarclienteosprotocoloura.sql](Resultados SELECT/sql-buscarclienteosprotocoloura.md) | 1 | ok |
| [sql-buscarclienteprotocoloura.sql](Resultados SELECT/sql-buscarclienteprotocoloura.md) | 1 | ok |
| [sql-contract-brands.sql](Resultados SELECT/sql-contract-brands.md) | 2 | ok |
| [sql-contratoavisomigracao.sql](Resultados SELECT/sql-contratoavisomigracao.md) | 8 | ok |
| [sql-contratoavisomigracaocompulsoria.sql](Resultados SELECT/sql-contratoavisomigracaocompulsoria.md) | 6 | ok |
| [sql-customer-brands.sql](Resultados SELECT/sql-customer-brands.md) | 2 | ok |
| [sql-pacotesbyclienteid.sql](Resultados SELECT/sql-pacotesbyclienteid.md) | 1 | ok |
| [sql-verifica-cliente-monitorado.sql](Resultados SELECT/sql-verifica-cliente-monitorado.md) | 1 | ok |
| [vendarepository-buscarvendanoair.sql](Resultados SELECT/vendarepository-buscarvendanoair.md) | 3 | ok |

## Colunas por query

### [analisecreditoatributorepository-findallbyanalisecredito_id.sql](Resultados SELECT/analisecreditoatributorepository-findallbyanalisecredito_id.md)

- Colunas: 4

| Ordem | Coluna |
|---:|---|
| 1 | `id` |
| 2 | `codigo` |
| 3 | `nome` |
| 4 | `valor` |

### [analisecreditorepository-findallbyleadclienteid.sql](Resultados SELECT/analisecreditorepository-findallbyleadclienteid.md)

- Colunas: 90

| Ordem | Coluna |
|---:|---|
| 1 | `id` |
| 2 | `id_lead` |
| 3 | `aprovado_serasa` |
| 4 | `aprovado_spc` |
| 5 | `autorizado` |
| 6 | `cpf_cnpj_consulta` |
| 7 | `data_analise` |
| 8 | `data_autorizacao` |
| 9 | `justificativa_autorizacao` |
| 10 | `nota_serasa` |
| 11 | `status_serasa` |
| 12 | `numero_restricoes` |
| 13 | `situacao_documento` |
| 14 | `usuario_autorizador` |
| 15 | `validacao_nome` |
| 16 | `validacao_nome_mae` |
| 17 | `validacao_data_nascimento` |
| 18 | `xml` |
| 19 | `valor_total` |
| 20 | `integracao_codigo` |
| 21 | `integracao_mensagem` |
| 22 | `integracao_status` |
| 23 | `integracao_transacao` |
| 24 | `lead_criacao` |
| 25 | `lead_criador` |
| 26 | `lead_alteracao` |
| 27 | `lead_alterador` |
| 28 | `lead_excluido` |
| 29 | `lead_tipo` |
| 30 | `lead_nome` |
| 31 | `lead_qualificacao` |
| 32 | `lead_telefone` |
| 33 | `lead_email` |
| 34 | `lead_email_status` |
| 35 | `lead_fonte` |
| 36 | `lead_grupo` |
| 37 | `lead_nivel_interesse` |
| 38 | `lead_legado_id` |
| 39 | `lead_legado_sistema` |
| 40 | `lead_data_validade_carteira` |
| 41 | `lead_cpf_cnpj` |
| 42 | `lead_telefone_adicional` |
| 43 | `lead_email_adicional` |
| 44 | `lead_email_adicional_status` |
| 45 | `lead_senha_sac` |
| 46 | `lead_site` |
| 47 | `lead_twitter` |
| 48 | `lead_facebook` |
| 49 | `lead_concorrentes` |
| 50 | `lead_interesses` |
| 51 | `lead_tratamento` |
| 52 | `lead_data_nascimento` |
| 53 | `lead_estado_civil` |
| 54 | `lead_rg_numero` |
| 55 | `lead_rg_orgao` |
| 56 | `lead_nome_mae` |
| 57 | `lead_nome_pai` |
| 58 | `lead_nome_fantasia` |
| 59 | `lead_inscricao_estadual` |
| 60 | `lead_inscricao_municipal` |
| 61 | `lead_atividade_principal` |
| 62 | `lead_endereco_completo` |
| 63 | `lead_unidade` |
| 64 | `lead_cidade_id` |
| 65 | `lead_cidade_nome` |
| 66 | `lead_codigo_ibge` |
| 67 | `lead_bairro_id` |
| 68 | `lead_bairro_nome` |
| 69 | `lead_cep` |
| 70 | `lead_complemento` |
| 71 | `lead_logradouro_id` |
| 72 | `lead_tipo_logradouro` |
| 73 | `lead_logradouro_nome` |
| 74 | `lead_latitude` |
| 75 | `lead_longitude` |
| 76 | `lead_numero` |
| 77 | `lead_referencia` |
| 78 | `lead_credito_autorizado` |
| 79 | `lead_tipo_residencia` |
| 80 | `lead_condominio_id` |
| 81 | `lead_bloco` |
| 82 | `lead_apartamento` |
| 83 | `lead_endereco_certificado` |
| 84 | `lead_endereco_verificado` |
| 85 | `lead_uuid_lead_rd_station` |
| 86 | `lead_viabilidade_autorizada` |
| 87 | `lead_viabilidade_usuario` |
| 88 | `lead_viabilidade_data` |
| 89 | `lead_viabilidade_justificativa` |
| 90 | `lead_carteira_id` |

### [analisecreditorestricaorepository-findallbyanalisecredito_id.sql](Resultados SELECT/analisecreditorestricaorepository-findallbyanalisecredito_id.md)

- Colunas: 8

| Ordem | Coluna |
|---:|---|
| 1 | `cidade_associado` |
| 2 | `nome_associado` |
| 3 | `codigo_entidade` |
| 4 | `nome_entidade` |
| 5 | `contrato` |
| 6 | `data_vencimento` |
| 7 | `data_inclusao` |
| 8 | `valor` |

### [carteirarepository-findcarteirabyid.sql](Resultados SELECT/carteirarepository-findcarteirabyid.md)

- Colunas: 28

| Ordem | Coluna |
|---:|---|
| 1 | `carteiraId` |
| 2 | `carteiraCriacao` |
| 3 | `carteiraCriador` |
| 4 | `carteiraAlteracao` |
| 5 | `carteiraAlterador` |
| 6 | `carteiraExcluido` |
| 7 | `carteiraTipo` |
| 8 | `carteiraAtivo` |
| 9 | `vendedorId` |
| 10 | `vendedorCriacao` |
| 11 | `vendedorCriador` |
| 12 | `vendedorAlteracao` |
| 13 | `vendedorAlterador` |
| 14 | `vendedorExcluido` |
| 15 | `vendedorUsuario` |
| 16 | `vendedorEquipe` |
| 17 | `vendedorTerceirizada` |
| 18 | `vendedorAtivo` |
| 19 | `vendedorSupervisorId` |
| 20 | `vendedorSupervisorCriacao` |
| 21 | `vendedorSupervisorCriador` |
| 22 | `vendedorSupervisorAlteracao` |
| 23 | `vendedorSupervisorAlterador` |
| 24 | `vendedorSupervisorExcluido` |
| 25 | `vendedorSupervisorUsuario` |
| 26 | `vendedorSupervisorEquipe` |
| 27 | `vendedorSupervisorTerceirizada` |
| 28 | `vendedorSupervisorAtivo` |

### [clienterepository-findclientebyid.sql](Resultados SELECT/clienterepository-findclientebyid.md)

- Colunas: 42

| Ordem | Coluna |
|---:|---|
| 1 | `id` |
| 2 | `criacao` |
| 3 | `criador` |
| 4 | `alteracao` |
| 5 | `alterador` |
| 6 | `excluido` |
| 7 | `avaliacao` |
| 8 | `clienteB2b` |
| 9 | `codigo` |
| 10 | `fonte` |
| 11 | `grupo` |
| 12 | `idOauth` |
| 13 | `idSuporteSumicityVirtualDois` |
| 14 | `idSuporteSumicityVirtualUm` |
| 15 | `integracaoCodigo` |
| 16 | `integracaoMensagem` |
| 17 | `integracaoStatus` |
| 18 | `integracaoTransacao` |
| 19 | `integracaoSydleCodigo` |
| 20 | `integracaoSydleMensagem` |
| 21 | `integracaoSydleStatus` |
| 22 | `integracaoSydleTransacao` |
| 23 | `legadoId` |
| 24 | `legadoSistema` |
| 25 | `marcador` |
| 26 | `nome` |
| 27 | `senhaSac` |
| 28 | `tipo` |
| 29 | `tratamento` |
| 30 | `cpf` |
| 31 | `dataNascimento` |
| 32 | `estadoCivil` |
| 33 | `nomeMae` |
| 34 | `nomePai` |
| 35 | `rgNumero` |
| 36 | `rgOrgao` |
| 37 | `atividadePrincipal` |
| 38 | `cnpj` |
| 39 | `inscricaoEstadual` |
| 40 | `inscricaoMunicipal` |
| 41 | `nomeFantasia` |
| 42 | `carteiraId` |

### [enderecocidaderepository-findcidadebysigla.sql](Resultados SELECT/enderecocidaderepository-findcidadebysigla.md)

- Colunas: 13

| Ordem | Coluna |
|---:|---|
| 1 | `id` |
| 2 | `data_criacao` |
| 3 | `usuario_criacao` |
| 4 | `data_alteracao` |
| 5 | `usuario_alteracao` |
| 6 | `excluido` |
| 7 | `nome` |
| 8 | `estado` |
| 9 | `codigo_ibge` |
| 10 | `ddd` |
| 11 | `atendida` |
| 12 | `id_cidade` |
| 13 | `unidades` |

### [enderecorepository-findallenderecosbycliente.sql](Resultados SELECT/enderecorepository-findallenderecosbycliente.md)

- Colunas: 96

| Ordem | Coluna |
|---:|---|
| 1 | `id` |
| 2 | `criacao` |
| 3 | `criador` |
| 4 | `alteracao` |
| 5 | `alterador` |
| 6 | `excluido` |
| 7 | `logradouroTipo` |
| 8 | `logradouro` |
| 9 | `bairro` |
| 10 | `cep` |
| 11 | `numero` |
| 12 | `complemento` |
| 13 | `referencia` |
| 14 | `latitude` |
| 15 | `longitude` |
| 16 | `ativo` |
| 17 | `legadoId` |
| 18 | `legadoSistema` |
| 19 | `codigoSap` |
| 20 | `unidade` |
| 21 | `certificado` |
| 22 | `verificado` |
| 23 | `ftta` |
| 24 | `viabiliadadeAutorizada` |
| 25 | `ViabilidadeUsuario` |
| 26 | `viabiliadadeData` |
| 27 | `viabilidadeJustificativa` |
| 28 | `cidadeId` |
| 29 | `cidadeCriacao` |
| 30 | `cidadeCriador` |
| 31 | `cidadeAlteracao` |
| 32 | `cidadeAlterador` |
| 33 | `cidadeExcluido` |
| 34 | `cidadeNome` |
| 35 | `cidadeEstado` |
| 36 | `cidadeCodigoIbge` |
| 37 | `ddd` |
| 38 | `atendida` |
| 39 | `condominioId` |
| 40 | `condominioCriacao` |
| 41 | `CondominioCriador` |
| 42 | `CondominioAlteracao` |
| 43 | `CondominioAlterador` |
| 44 | `CondominioExcluido` |
| 45 | `condominioNome` |
| 46 | `condominioTipoCondominio` |
| 47 | `condominioEnderecoCompleto` |
| 48 | `condominioTipoLogradouro` |
| 49 | `condominioLogradouro` |
| 50 | `condominioBairro` |
| 51 | `condominioCep` |
| 52 | `condominioNumero` |
| 53 | `condominioComplemento` |
| 54 | `condominioLatitude` |
| 55 | `condominioLongitude` |
| 56 | `condominioUnidade` |
| 57 | `condominioReferencia` |
| 58 | `condominioNomeSindico` |
| 59 | `condominioTelefoneSindico` |
| 60 | `condominioEmailSindico` |
| 61 | `condominioNomeZelador` |
| 62 | `condominioTelefoneZelador` |
| 63 | `condominioEmailZelador` |
| 64 | `condominioStatusAtual` |
| 65 | `condominioStatusVisita` |
| 66 | `condominioDataVistoriaPrevista` |
| 67 | `condominioDataVistoriaExecutada` |
| 68 | `condominioDataConstrucaoPrevista` |
| 69 | `condominioDataConstrucaoRealizada` |
| 70 | `condominioEnderecoCertificado` |
| 71 | `condominioEnderecoVerificado` |
| 72 | `condominioPrioridade` |
| 73 | `condominioQuantidadeBlocos` |
| 74 | `condominioQuantidadePrumadasBloco` |
| 75 | `condominioQuantidadeApartamentosBloco` |
| 76 | `condominioQuantidadeAndares` |
| 77 | `condominioCenario` |
| 78 | `condominioLinkMapa` |
| 79 | `condominioLinkDiagrama` |
| 80 | `condominioEnderecoEntroncamento` |
| 81 | `condominioFibraFacilidadeArea` |
| 82 | `condominioMaterialGasto` |
| 83 | `condominioTipoServico` |
| 84 | `condominioPerfil` |
| 85 | `condominioMetragemLancamento` |
| 86 | `condominioDataSolicitacao` |
| 87 | `condominioDataInicio` |
| 88 | `condominioRegistroPlanilha` |
| 89 | `condominioAndaresUteis` |
| 90 | `condominioQuantidadeApartamentosAndar` |
| 91 | `condominioHpsBloco` |
| 92 | `condominioDescricaoTubulacao` |
| 93 | `condominioConcorrentes` |
| 94 | `condominioTecnologiaConcorrente` |
| 95 | `condominioServicoOferecido` |
| 96 | `condominioAvaliacaoBreve` |

### [sql-aviso-rede-backbone.sql](Resultados SELECT/sql-aviso-rede-backbone.md)

- Colunas: 12

| Ordem | Coluna |
|---:|---|
| 1 | `inicio` |
| 2 | `nivel` |
| 3 | `ocorrencia` |
| 4 | `afetaInternet` |
| 5 | `afetaTelefonia` |
| 6 | `afetaTv` |
| 7 | `impacto` |
| 8 | `tempoSolucao` |
| 9 | `idProblema` |
| 10 | `descricao` |
| 11 | `abertura` |
| 12 | `protocolo` |

### [sql-aviso-rede-manual.sql](Resultados SELECT/sql-aviso-rede-manual.md)

- Colunas: 12

| Ordem | Coluna |
|---:|---|
| 1 | `inicio` |
| 2 | `nivel` |
| 3 | `ocorrencia` |
| 4 | `afetaInternet` |
| 5 | `afetaTelefonia` |
| 6 | `afetaTv` |
| 7 | `impacto` |
| 8 | `tempoSolucao` |
| 9 | `idProblema` |
| 10 | `descricao` |
| 11 | `abertura` |
| 12 | `protocolo` |

### [sql-aviso-rede-monitorado.sql](Resultados SELECT/sql-aviso-rede-monitorado.md)

- Colunas: 14

| Ordem | Coluna |
|---:|---|
| 1 | `id` |
| 2 | `inicio` |
| 3 | `nivel` |
| 4 | `ocorrencia` |
| 5 | `afetaInternet` |
| 6 | `afetaTelefonia` |
| 7 | `afetaTv` |
| 8 | `impacto` |
| 9 | `idProblema` |
| 10 | `descricao` |
| 11 | `abertura` |
| 12 | `protocolo` |
| 13 | `tempoSolucao` |
| 14 | `estimativa` |

### [sql-aviso-rede-nao-monitorado.sql](Resultados SELECT/sql-aviso-rede-nao-monitorado.md)

- Colunas: 12

| Ordem | Coluna |
|---:|---|
| 1 | `inicio` |
| 2 | `nivel` |
| 3 | `ocorrencia` |
| 4 | `afetaInternet` |
| 5 | `afetaTelefonia` |
| 6 | `afetaTv` |
| 7 | `impacto` |
| 8 | `tempoSolucao` |
| 9 | `idProblema` |
| 10 | `descricao` |
| 11 | `abertura` |
| 12 | `protocolo` |

### [sql-aviso-telefonia.sql](Resultados SELECT/sql-aviso-telefonia.md)

- Colunas: 12

| Ordem | Coluna |
|---:|---|
| 1 | `inicio` |
| 2 | `nivel` |
| 3 | `ocorrencia` |
| 4 | `afetaInternet` |
| 5 | `afetaTelefonia` |
| 6 | `afetaTv` |
| 7 | `impacto` |
| 8 | `tempoSolucao` |
| 9 | `idProblema` |
| 10 | `descricao` |
| 11 | `abertura` |
| 12 | `protocolo` |

### [sql-buscarclientecontrato.sql](Resultados SELECT/sql-buscarclientecontrato.md)

- Colunas: 1

| Ordem | Coluna |
|---:|---|
| 1 | `id_cliente` |

### [sql-buscarclienteosprotocoloura.sql](Resultados SELECT/sql-buscarclienteosprotocoloura.md)

- Colunas: 1

| Ordem | Coluna |
|---:|---|
| 1 | `codigo_cliente` |

### [sql-buscarclienteprotocoloura.sql](Resultados SELECT/sql-buscarclienteprotocoloura.md)

- Colunas: 1

| Ordem | Coluna |
|---:|---|
| 1 | `codigo_cliente` |

### [sql-contract-brands.sql](Resultados SELECT/sql-contract-brands.md)

- Colunas: 2

| Ordem | Coluna |
|---:|---|
| 1 | `marca` |
| 2 | `regional` |

### [sql-contratoavisomigracao.sql](Resultados SELECT/sql-contratoavisomigracao.md)

- Colunas: 8

| Ordem | Coluna |
|---:|---|
| 1 | `cliente_id` |
| 2 | `contrato_codigo` |
| 3 | `pacote_atual` |
| 4 | `pacote_ofertado_1` |
| 5 | `pacote_ofertado_valor_1` |
| 6 | `pacote_ofertado_2` |
| 7 | `pacote_ofertado_valor_2` |
| 8 | `validade_promocao` |

### [sql-contratoavisomigracaocompulsoria.sql](Resultados SELECT/sql-contratoavisomigracaocompulsoria.md)

- Colunas: 6

| Ordem | Coluna |
|---:|---|
| 1 | `cliente_id` |
| 2 | `contrato_codigo` |
| 3 | `pacote_atual` |
| 4 | `pacote_ofertado_1` |
| 5 | `reajuste` |
| 6 | `migracao_compulsoria` |

### [sql-customer-brands.sql](Resultados SELECT/sql-customer-brands.md)

- Colunas: 2

| Ordem | Coluna |
|---:|---|
| 1 | `marca` |
| 2 | `regional` |

### [sql-pacotesbyclienteid.sql](Resultados SELECT/sql-pacotesbyclienteid.md)

- Colunas: 1

| Ordem | Coluna |
|---:|---|
| 1 | `pacote_codigo` |

### [sql-verifica-cliente-monitorado.sql](Resultados SELECT/sql-verifica-cliente-monitorado.md)

- Colunas: 1

| Ordem | Coluna |
|---:|---|
| 1 | `contrato_id` |

### [vendarepository-buscarvendanoair.sql](Resultados SELECT/vendarepository-buscarvendanoair.md)

- Colunas: 3

| Ordem | Coluna |
|---:|---|
| 1 | `codigoContratoAir` |
| 2 | `codigoChamadoAir` |
| 3 | `codigoOrdemServicoAir` |
