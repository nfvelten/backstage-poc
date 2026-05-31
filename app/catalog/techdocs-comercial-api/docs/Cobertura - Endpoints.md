---
tags:
  - trabalho
  - air
  - api
  - documentacao
  - comercial-api
  - endpoints
gerado_em: 2026-05-29 21:35:45
---
# Cobertura - Endpoints comercial-api

Relatorio para decidir quais endpoints devem virar requests Bruno com contexto.

## Leitura correta

- `git_count` indica que o arquivo mudou nos ultimos 12 meses; isso e sinal de manutencao, nao de uso real.
- Para saber endpoints mais usados ou mortos em producao, precisa cruzar com Loki/Gateway logs.
- Requests Bruno existentes com `docs` devem ser preservadas como fonte manual.

## Resumo

| Item | Quantidade |
|---|---:|
| Endpoints no codigo | 224 |
| Requests Bruno em `comercial/` | 24 |
| Cobertos por Bruno | 22 |
| Sem request Bruno | 202 |
| Requests Bruno sem correspondencia estatica no codigo | 2 |
| Requests Bruno sem bloco `docs` | 0 |
| Rotas com uso real informado | 11 |

## Rotas com sucesso no painel

Fonte: `Trabalho/Air/APIs/comercial-api/usage/top-rotas-sucesso.csv`.

| Metodo | Path | Controller | Funcao | Sucessos | Bruno | Fonte |
|---|---|---|---|---:|---|---|
| GET | `/v1/contracts/detail` | `ContractsControllerV1` | `findContractDetails` | 56671 | `get-contracts-detail.bru` | `src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:32` |
| GET | `/wpp-notificacoes/listar/{customerId}` | `NotificationController` | `listar` | 15646 | `get-wpp-notificacoes-listar.bru` | `src/main/java/br/net/air/notification/controller/NotificationController.java:49` |
| GET | `/contrato/{id}/aviso` | `ContratoAvisoController` | `buscarAviso` | 10208 | `get-contrato-aviso.bru` | `src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java:35` |
| GET | `/v1/contracts/customer-basic-info` | `ContractsControllerV1` | `getCustomerBasicInfoByContractNumber` | 6562 | `get-contracts-customer-basic-info.bru` | `src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:46` |
| POST | `/contrato/{id}/adicionar_aviso` | `ContratoAvisoController` | `adicionarAviso` | 5658 | `post-contrato-adicionar-aviso.bru` | `src/main/java/br/net/air/cliente/controller/ContratoAvisoController.java:29` |
| GET | `/cliente/{id}/contrato` | `ClienteController` | `contratos` | 2730 | `get-cliente-contrato.bru` | `src/main/java/br/net/air/cliente/controller/ClienteController.java:211` |
| GET | `/cliente/{id}/contato` | `ClienteController` | `contatos` | 2052 | `get-cliente-contato.bru` | `src/main/java/br/net/air/cliente/controller/ClienteController.java:263` |
| GET | `/cliente/{id}/endereco` | `ClienteController` | `enderecos` | 1853 | `get-cliente-endereco.bru` | `src/main/java/br/net/air/cliente/controller/ClienteController.java:257` |
| GET | `/cliente/{id}/consultar_avisos` | `ClienteController` | `consultarAvisos` | 1844 | `get-cliente-consultar-avisos.bru` | `src/main/java/br/net/air/cliente/controller/ClienteController.java:543` |
| GET | `/cliente/{id}/analise_credito` | `ClienteController` | `analisesCredito` | 1685 | `get-cliente-analise-credito.bru` | `src/main/java/br/net/air/cliente/controller/ClienteController.java:310` |
| GET | `/cliente/{id}/blacklist` | `ClienteController` | `blacklist` | 1683 | `get-cliente-blacklist.bru` | `src/main/java/br/net/air/cliente/controller/ClienteController.java:269` |

## Requests Bruno sem correspondencia estatica no codigo

Como a collection `comercial/` e recente, estes requests devem ser tratados como usados. Ausencia de match aqui significa apenas que a rota pode estar em outro servico, proxy, branch, formato nao coberto pelo parser, ou precisar de normalizacao manual.

| Metodo | Path Bruno | Arquivo | Docs |
|---|---|---|---|
| GET | `/v1/contracts/{{id}}/svas` | `get-contrato-svas-v1.bru` | sim |
| POST | `/contrato/criar-integracao` | `post-criar-integracao.bru` | sim |

## Requests Bruno sem contexto

| Metodo | Path Bruno | Arquivo |
|---|---|---|
| - | - | - |

## Prioridade para criar/atualizar requests Bruno

Top 60 endpoints sem request Bruno, ranqueados por atividade git + controller central + risco operacional.

| Metodo | Path | Controller | Funcao | Sucessos | git_count | Ultimo commit | Fonte | Motivo |
|---|---|---|---|---:|---:|---|---|---|
| PUT | `/contrato/{id}/alterar_endereco` | `ContratoController` | `alterarEndereco` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:275` | score=27; 12 mudanças no arquivo em 12m; controller central; fluxo operacional/risco alto; tem efeito colateral |
| PUT | `/contrato/{id}/habilitar_confianca` | `ContratoController` | `habilitarConfianca` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:218` | score=27; 12 mudanças no arquivo em 12m; controller central; fluxo operacional/risco alto; tem efeito colateral |
| GET | `/contrato/massivas_por_contrato/{idContrato}` | `ContratoController` | `consultarMassiva` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:596` | score=25; 12 mudanças no arquivo em 12m; controller central; fluxo operacional/risco alto |
| POST | `/v1/contracts/change-plan` | `ContractsControllerV1` | `changePlan` | 0 | 10 | 2026-03-24 | `src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:38` | score=25; 10 mudanças no arquivo em 12m; controller central; fluxo operacional/risco alto; tem efeito colateral |
| PUT | `/cliente` | `ClienteController` | `filtrar` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:124` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/anexo_visualizar` | `ClienteController` | `anexos` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:298` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/dataDeNascimentoSydle` | `ClienteController` | `alteracaoDataDeNascimentoSydle` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:437` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/evento_fatura` | `ClienteController` | `eventoFatura` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:444` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/fatuas_gi/cpf_cnpj` | `ClienteController` | `faturasGI` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:322` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/gerarCupom` | `ClienteController` | `gerarCupomCliente` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:485` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/marcadoresClientes` | `ClienteController` | `marcadoresClientes` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:465` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/marcadoresContratos` | `ClienteController` | `marcadoresClientes` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:516` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/perfilar_cobranca` | `ClienteController` | `perfilarCobranca` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:374` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/perfilar_retencao` | `ClienteController` | `perfilarRetencao` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:384` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/cliente/validarCupom` | `ClienteController` | `validarCupom` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:511` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/{id}` | `ClienteController` | `alterar` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:137` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/{id}/desmarcar` | `ClienteController` | `alterar` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:152` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/{id}/marcar` | `ClienteController` | `alterar` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:145` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/{id}/outrosMarcadores` | `ClienteController` | `outrosMarcadores` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:450` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/cliente/{id}/senha` | `ClienteController` | `alterarSenha` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:159` | score=21; 14 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| GET | `/cliente/{id}/anexo` | `ClienteController` | `anexos` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:275` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/classificar_risco` | `ClienteController` | `listarClassificarRisco` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:410` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/evento` | `ClienteController` | `eventos` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:304` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/obs` | `ClienteController` | `observacoes` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:251` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/orientacoes` | `ClienteController` | `buscarClienteOrientacoes` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:428` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/outrosMarcadores` | `ClienteController` | `listarOutrosMarcadores` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:458` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/registro_ligacao` | `ClienteController` | `buscarRegistroLigacoes` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:204` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/routethis` | `ClienteController` | `buscarRoutethis` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:416` | score=19; 14 mudanças no arquivo em 12m; controller central |
| GET | `/cliente/{id}/v2/anexo` | `ClienteController` | `anexosV2` | 0 | 14 | 2026-04-16 | `src/main/java/br/net/air/cliente/controller/ClienteController.java:291` | score=19; 14 mudanças no arquivo em 12m; controller central |
| POST | `/contrato/atualizarContatos` | `ContratoController` | `atualizarContatos` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:513` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/contrato/contratos-cancelados` | `ContratoController` | `buscarContratoCancelado` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:571` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/adicionar_saldo_habilitacao` | `ContratoController` | `adicionarSaldoHabilitacao` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:431` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/alterarEquipe` | `ContratoController` | `alterarEquipe` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:527` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/alterarStatus` | `ContratoController` | `alterarIntegracaoStatus` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:473` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/alterarValorIlustrativoB2B` | `ContratoController` | `alterarValorIlustrativoB2B` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:541` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/alterar_forma_pagamento` | `ContratoController` | `alterarFormaPagamento` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:329` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/alterar_marcador` | `ContratoController` | `alterarMarcador` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:227` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/atualizar_servicos_tecnicos` | `ContratoController` | `atualizarServicosTecnicos` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:549` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/contrato/{id}/emitir_evento/habilitacao_confianca` | `ContratoController` | `emitirEventoHabilitacaoEmConfianca` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:560` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/contrato/{id}/solicitar_cancelamento` | `ContratoController` | `cancelar` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:248` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/contrato/{id}/unidade/{unidade}` | `ContratoController` | `alterarUnidadeContrato` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:392` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/venda/adicional` | `VendaController` | `adicional` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:351` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/venda/aprovacao_migracao` | `VendaController` | `aprovacaoMigracao` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:111` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/venda/assine/clientes` | `VendaController` | `vendasByAssine` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:419` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/venda/crm/criar_contrato` | `VendaController` | `vendasNovoCRM` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:426` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/venda/crm/trocar_titularidade` | `VendaController` | `trocaDeTitularidadeNovoCRM` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:451` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/venda/retornoQtdChamadosFila` | `VendaController` | `chamadosPorFila` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:457` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/venda/{id_contrato}/alterar_vendedor` | `VendaController` | `alterarVendedor` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:406` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| PUT | `/venda/{id}/aprovar_migracao` | `VendaController` | `aprovarMigracao` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:289` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| POST | `/venda/{id}/cancelar_venda_ativacao` | `VendaController` | `cancelarVendaAtivacao` | 0 | 12 | 2026-01-29 | `src/main/java/br/net/air/venda/controller/VendaController.java:465` | score=19; 12 mudanças no arquivo em 12m; controller central; tem efeito colateral |
| GET | `/contrato/auto-isp/{idContrato}` | `ContratoController` | `linkContratoAutoISP` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:586` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/endereco-por-contrato/{idContrato}` | `ContratoController` | `consultarEnderecoPorContrato` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:601` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/eventos_onu/{id}` | `ContratoController` | `buscarEventosONU` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:566` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{idContrato}/dados_contrato_cliente` | `ContratoController` | `buscarDadosContratoById` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:444` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{id}/adicionais_disponiveis` | `ContratoController` | `adicionaisContrato` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:320` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{id}/desconto` | `ContratoController` | `descontos` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:186` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{id}/evento` | `ContratoController` | `eventos` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:165` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{id}/informacao_forma_pagamento` | `ContratoController` | `informacaoFormaPagamento` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:337` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{id}/termo` | `ContratoController` | `termo` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:355` | score=17; 12 mudanças no arquivo em 12m; controller central |
| GET | `/contrato/{id}/valorIlustrativoB2B` | `ContratoController` | `valorIlustrativoB2B` | 0 | 12 | 2026-04-10 | `src/main/java/br/net/air/cliente/controller/ContratoController.java:535` | score=17; 12 mudanças no arquivo em 12m; controller central |

## Possiveis endpoints antigos/baixo sinal

Sem request Bruno e sem alteracao no arquivo nos ultimos 12 meses. Nao significa morto; significa que precisa de log de producao para confirmar.

| Metodo | Path | Controller | Funcao | Sucessos | git_count | Ultimo commit | Fonte | Motivo |
|---|---|---|---|---:|---:|---|---|---|
| POST | `/cliente_anexo/site/{id_contrato}` | `ClienteAnexoController` | `cadastarAnexoBySite` | 0 | 0 | 2020-02-06 | `src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:87` | baixo sinal por git |
| POST | `/cliente_anexo/{id}` | `ClienteAnexoController` | `cadastar` | 0 | 0 | 2020-02-06 | `src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:36` | baixo sinal por git |
| GET | `/cliente_anexo/{id}` | `ClienteAnexoController` | `buscar` | 0 | 0 | 2020-02-06 | `src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:58` | baixo sinal por git |
| PUT | `/cliente_anexo/{id}` | `ClienteAnexoController` | `alterar` | 0 | 0 | 2020-02-06 | `src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:64` | baixo sinal por git |
| DELETE | `/cliente_anexo/{id}` | `ClienteAnexoController` | `deletar` | 0 | 0 | 2020-02-06 | `src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:70` | baixo sinal por git |
| GET | `/cliente_anexo/{id}/download` | `ClienteAnexoController` | `download` | 0 | 0 | 2020-02-06 | `src/main/java/br/net/air/cliente/controller/ClienteAnexoController.java:77` | baixo sinal por git |
| GET | `/dashboard/historico/{tipo}/{id}` | `DashboardController` | `obterHistoricoEvento` | 0 | 0 | 2020-05-12 | `src/main/java/br/net/air/financeiro/controller/DashboardController.java:31` | baixo sinal por git |
| GET | `/cobranca_pontual` | `CobrancaPontualController` | `listar` | 0 | 0 | 2020-05-14 | `src/main/java/br/net/air/financeiro/controller/CobrancaPontualController.java:26` | baixo sinal por git |
| POST | `/cobranca_pontual` | `CobrancaPontualController` | `cadastrar` | 0 | 0 | 2020-05-14 | `src/main/java/br/net/air/financeiro/controller/CobrancaPontualController.java:40` | baixo sinal por git |
| PUT | `/cobranca_pontual/{id}` | `CobrancaPontualController` | `alterar` | 0 | 0 | 2020-05-14 | `src/main/java/br/net/air/financeiro/controller/CobrancaPontualController.java:45` | baixo sinal por git |
| DELETE | `/cobranca_pontual/{id}` | `CobrancaPontualController` | `deletar` | 0 | 0 | 2020-05-14 | `src/main/java/br/net/air/financeiro/controller/CobrancaPontualController.java:54` | baixo sinal por git |
| GET | `/reajuste/contrato/{id}` | `ContratoReajusteController` | `liberar` | 0 | 0 | 2020-05-14 | `src/main/java/br/net/air/cliente/controller/ContratoReajusteController.java:25` | baixo sinal por git |
| POST | `/assine/exibir_token` | `AssineController` | `exibirToken` | 0 | 0 | 2020-11-01 | `src/main/java/br/net/air/assine/controller/AssineController.java:27` | baixo sinal por git |
| POST | `/assine/lomadee` | `AssineController` | `relatorioLomadee` | 0 | 0 | 2020-11-01 | `src/main/java/br/net/air/assine/controller/AssineController.java:22` | baixo sinal por git |
| POST | `/app/restart` | `ApplicationController` | `restart` | 0 | 0 | 2021-03-01 | `src/main/java/br/net/air/ApplicationController.java:16` | baixo sinal por git |
| GET | `/endereco_estado` | `EnderecoEstadoController` | `listar` | 0 | 0 | 2024-03-12 | `src/main/java/br/net/air/configuracoes/controller/EnderecoEstadoController.java:23` | baixo sinal por git |
| GET | `/metricas/{endpoint}` | `MetricsController` | `metrics` | 0 | 0 | 2024-06-14 | `src/main/java/br/net/air/MetricsController.java:21` | baixo sinal por git |
| GET | `/v2/vendedor/usuario_logado` | `VendedorControllerV2` | `findByUsuario` | 0 | 0 | 2024-11-13 | `src/main/java/br/net/air/configuracoes/controller/V2/VendedorControllerV2.java:22` | baixo sinal por git |
| POST | `/integracao/cliente` | `IntegracaoController` | `criarCliente` | 0 | 0 | 2025-04-03 | `src/main/java/br/net/air/integracao/controller/IntegracaoController.java:34` | baixo sinal por git |
| POST | `/integracao/contato` | `IntegracaoController` | `criaContato` | 0 | 0 | 2025-04-03 | `src/main/java/br/net/air/integracao/controller/IntegracaoController.java:61` | baixo sinal por git |
| POST | `/integracao/contrato` | `IntegracaoController` | `criarContrato` | 0 | 0 | 2025-04-03 | `src/main/java/br/net/air/integracao/controller/IntegracaoController.java:44` | baixo sinal por git |
| POST | `/integracao/desconto` | `IntegracaoController` | `cadastrarDesconto` | 0 | 0 | 2025-04-03 | `src/main/java/br/net/air/integracao/controller/IntegracaoController.java:49` | baixo sinal por git |
| POST | `/integracao/endereco` | `IntegracaoController` | `criarEndereco` | 0 | 0 | 2025-04-03 | `src/main/java/br/net/air/integracao/controller/IntegracaoController.java:39` | baixo sinal por git |
| POST | `/integracao/whatsapp` | `IntegracaoController` | `criarContatoWhatsapp` | 0 | 0 | 2025-04-03 | `src/main/java/br/net/air/integracao/controller/IntegracaoController.java:29` | baixo sinal por git |

## Arquivos mais alterados no ultimo ano

| Arquivo | Mudancas |
|---|---:|
| `src/main/java/br/net/air/venda/service/VendaService.java` | 36 |
| `src/main/java/br/net/air/cliente/service/ContratoService.java` | 24 |
| `src/main/java/br/net/air/cliente/service/ClienteService.java` | 23 |
| `src/main/java/br/net/air/clean_arch/application/services/ContractServiceV1.java` | 21 |
| `src/main/java/br/net/air/cliente/controller/ClienteController.java` | 14 |
| `src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java` | 14 |
| `src/main/java/br/net/air/venda/service/ChamadoService.java` | 12 |
| `src/main/java/br/net/air/cliente/controller/ContratoController.java` | 12 |
| `src/main/java/br/net/air/venda/controller/VendaController.java` | 12 |
| `src/main/java/br/net/air/clean_arch/application/enuns/ContractItemType.java` | 11 |
| `src/main/java/br/net/air/exception/GlobalExceptionHandler.java` | 11 |
| `src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java` | 10 |
| `src/main/java/br/net/air/cliente/service/EnderecoService.java` | 9 |
| `src/main/java/br/net/air/venda/service/NotificationService.java` | 9 |
| `src/main/java/br/net/air/configuracoes/service/OperacaoService.java` | 8 |
| `src/main/java/br/net/air/venda/dto/VendaDTO.java` | 8 |
| `src/main/java/br/net/air/clean_arch/application/controllers/ContractApiV1.java` | 7 |
| `src/main/java/br/net/air/clean_arch/domain/usecases/ContractUseCase.java` | 7 |
| `src/main/java/br/net/air/cliente/dto/CadastrarIntegracaoDTO.java` | 7 |
| `src/main/java/br/net/air/cliente/repository/ContratoRepository.java` | 7 |
| `src/main/java/br/net/air/clean_arch/application/controllers/customerController/ContactControllerV1.java` | 7 |
| `src/main/java/br/net/air/connectmaster/service/ConnectMasterIntegracaoService.java` | 6 |
| `src/main/java/br/net/air/notification/controller/NotificationController.java` | 6 |
| `src/main/java/br/net/air/configuracoes/service/VendedorService.java` | 5 |
| `src/main/java/br/net/air/venda/repository/VendaRepository.java` | 5 |
| `src/main/java/br/net/air/venda/service/LeadService.java` | 5 |
| `src/main/java/br/net/air/clean_arch/domain/models/responses/CustomerBasicInfoDto.java` | 5 |
| `src/main/java/br/net/air/cliente/repository/ClienteContatoRepository.java` | 5 |
| `src/main/java/br/net/air/clean_arch/application/services/ContactServiceV1.java` | 5 |
| `src/main/java/br/net/air/cliente/model/Contrato.java` | 4 |

## Cobertura atual

| Metodo | Path | Controller | Funcao | Bruno |
|---|---|---|---|---|
| GET | `/v1/contracts/enable-by-trust-elegibility` | `ContractsControllerV1` | `sydleContractTrustEnablementBalance` | `get-elegibilidade-confianca.bru` |
| GET | `/v1/contracts/detail` | `ContractsControllerV1` | `findContractDetails` | `get-contracts-detail.bru` |
| GET | `/v1/contracts/customer-basic-info` | `ContractsControllerV1` | `getCustomerBasicInfoByContractNumber` | `get-contracts-customer-basic-info.bru` |
| GET | `/cliente` | `ClienteController` | `listar` | `get-cliente-por-cpf.bru` |
| GET | `/cliente/{id}` | `ClienteController` | `buscar` | `get-cliente-por-id.bru` |
| GET | `/cliente/{id}/contrato` | `ClienteController` | `contratos` | `get-cliente-contrato.bru` |
| GET | `/cliente/{id}/endereco` | `ClienteController` | `enderecos` | `get-cliente-endereco.bru` |
| GET | `/cliente/{id}/contato` | `ClienteController` | `contatos` | `get-cliente-contato.bru` |
| GET | `/cliente/{id}/blacklist` | `ClienteController` | `blacklist` | `get-cliente-blacklist.bru` |
| GET | `/cliente/{id}/analise_credito` | `ClienteController` | `analisesCredito` | `get-cliente-analise-credito.bru` |
| GET | `/cliente/{id}/consultar_avisos` | `ClienteController` | `consultarAvisos` | `get-cliente-consultar-avisos.bru` |
| POST | `/contrato/{id}/adicionar_aviso` | `ContratoAvisoController` | `adicionarAviso` | `post-contrato-adicionar-aviso.bru` |
| GET | `/contrato/{id}/aviso` | `ContratoAvisoController` | `buscarAviso` | `get-contrato-aviso.bru` |
| GET | `/contrato/{id}` | `ContratoController` | `buscar` | `get-contrato.bru` |
| GET | `/contrato/{id}/migracao` | `ContratoController` | `migracoes` | `get-migracoes-contrato.bru` |
| GET | `/contrato/{id}/venda` | `ContratoController` | `vendas` | `get-vendas-contrato.bru` |
| POST | `/contrato/criar-integracao` | `ContratoController` | `criarContrato` | `test-criar-integracao.bru` |
| GET | `/wpp-notificacoes/listar/{customerId}` | `NotificationController` | `listar` | `get-wpp-notificacoes-listar.bru` |
| POST | `/oauth/integrar` | `OauthController` | `integrarManual` | `post-oauth-integrar.bru` |
| DELETE | `/oauth/remover/{cliente}` | `OauthController` | `remover` | `delete-oauth-remover.bru` |
| PUT | `/venda/nao_confirmadas` | `VendaController` | `naoConfirmadas` | `get-vendas-by-natureza.bru` |
| PUT | `/venda/{id}/ativar_servicos` | `VendaController` | `ativarServicos` | `ativar-servicos.bru` |
