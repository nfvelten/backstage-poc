---
tags:
  - trabalho
  - air
  - api
  - comercial-api
  - dominio
---
# Mapa de Dominio - comercial-api

Mapa conceitual para orientar leitura do código e das rotas. A intenção é reduzir o tempo entre “achei uma rota” e “entendi que parte do negócio ela afeta”.

## Pacotes principais

| Pacote | Responsabilidade dominante |
|---|---|
| `cliente` | Cliente, contrato, contato, endereço, blacklist, marcadores, eventos, campanhas de contrato e serviços relacionados ao ciclo de vida do contrato. |
| `venda` | Lead, venda, fase de venda, origem, adicionais, análise de crédito, bloqueios, renegociação e ativação. |
| `integracao` | Entrada de dados de integração para cliente, endereço, contrato, desconto, contato e WhatsApp. |
| `migracao` | Migração de contrato/pacote e validações de migração. |
| `configuracoes` | Cadastros de apoio comercial: campanha, carteira, vendedor, vencimento, endereço, produto, termo e regras. |
| `composicao` | Produtos, pacotes e itens vindos/relacionados ao SAP. |
| `financeiro` | Cobrança pontual, faturamento, desconto, título e dashboard financeiro. |
| `notification` | Integração com serviço de notificações/URA. |
| `oauth` | Integração/removal OAuth e rotinas de processamento. |
| `connectmaster` | Integração e rotina com ConnectMaster. |
| `spc` | Consulta/restrição de crédito via SPC/Serasa. |
| `clean_arch` | Gateways/portas para CRM, financeiro, notification, TV e link shortener. |
| `ecare` | Clientes e autenticação eCare/Keycloak. |
| `app`, `assine`, `perfilador`, `viabilidadeTeorica` | Canais/funcionalidades auxiliares ligados a venda, assinatura, perfilação e viabilidade. |

## Conceitos centrais

| Conceito | Significado prático | Onde aparece |
|---|---|---|
| Cliente | Pessoa física/jurídica base para contrato, contato, endereço, eventos e análise. | `cliente/model`, `ClienteController`, `ClienteService` |
| Contrato | Relação comercial do cliente com produtos/serviços, avisos, entrega, campanha, SVA e status. | `ContratoController`, `ContratoService`, `tbl_contrato` |
| Lead | Oportunidade comercial anterior ou paralela à venda/contrato. | `venda/model/Lead`, `LeadController` |
| Venda | Processo comercial com natureza, fase, adicional, migração e ativação. | `venda/model/Venda`, `VendaController` |
| Análise de crédito | Avaliação/restrição ligada a lead/cliente, com atributos e restrições. | `AnaliseCredito*`, [[Fluxos de Negocio/analise-credito]] |
| Aviso | Comunicação/alerta ligado a contrato/cliente, incluindo avisos de rede/telefonia/migração. | `ContratoAvisoController`, SQLs `sql-aviso-*` |
| Migração | Mudança de pacote/contrato, incluindo migração compulsória. | `migracao/*`, `ContratoMigracaoService`, SQLs de migração |
| SVA | Serviço de valor agregado associado ao contrato. | `ContractsControllerV1`, [[Fluxos de Negocio/contratos-v1-svas]] |
| Campanha | Regra/oferta comercial aplicada a venda/contrato/pacote. | `configuracoes/Campanha*`, `ContratoCampanhaService` |
| Carteira/Vendedor | Organização comercial e atribuição de venda/cliente. | `CarteiraRepository`, `VendedorController` |
| Integração | Entrada/saída com sistemas como Sydle, CRM, Chamado, ConnectMaster e OAuth. | `integracao/*`, [[Dependencias e Integracoes]] |

## Agregados e tabelas mais relevantes

| Agregado | Tabelas frequentes | Documentos relacionados |
|---|---|---|
| Cliente | `tbl_cliente`, `tbl_cliente_fisico`, `tbl_cliente_juridico`, `tbl_cliente_contato`, `tbl_endereco` | [[Resultados SELECT/clienterepository-findclientebyid]], [[Resultados SELECT/enderecorepository-findallenderecosbycliente]] |
| Contrato | `tbl_contrato`, `tbl_contrato_item`, `tbl_contrato_entrega`, `tbl_contrato_onu_aviso` | [[Resultados SELECT/sql-buscarclientecontrato]], [[Fluxos de Negocio/contratos-v1-svas]] |
| Venda/Lead | `tbl_venda`, `tbl_lead`, `tbl_venda_fase`, `tbl_venda_origem`, `tbl_venda_adicional` | [[Resultados SELECT/vendarepository-buscarvendanoair]], [[Fluxos de Negocio/vendas-e-migracoes]] |
| Crédito | `tbl_analise_credito`, `tbl_analise_credito_atributo`, `tbl_analise_credito_restricao` | [[Fluxos de Negocio/analise-credito]] |
| Avisos | `tbl_aviso_migracao`, tabelas cross-schema `air_internet.tbl_aviso*` | [[Fluxos de Negocio/avisos-cliente-contrato]] |
| Configuração comercial | `tbl_carteira`, `tbl_vendedor`, `tbl_campanha*`, `tbl_vencimento` | [[Codigo]], [[Banco - air_comercial]] |

## Estados relevantes

| Estado/categoria | Valores observados | Uso |
|---|---|---|
| Natureza da venda | `VN_NOVO_CONTRATO`, `VN_MIGRACAO_UP`, `VN_MIGRACAO_DOWN`, `VN_TROCA_TITULARIDADE`, `VN_ADICIONAL`, `VN_MIGRACAO_COMPULSORIA` | Define tipo de venda/migração/adicional. |
| Fase da venda | `FASE_CAMPANHA`, `FASE_PACOTE`, `FASE_ADICIONAL`, `FASE_CADASTRO`, `FASE_TERMO`, `FASE_REVISAO`, `FASE_ATIVACAO`, `FASE_CONFIRMADA`, `FASE_CANCELADA`, `FASE_APROVACAO_MIGRACAO` | Controla avanço do processo comercial. |
| Qualificação do lead | `LQ_NAO_QUALIFICADO`, `LQ_EM_NEGOCIACAO`, `LQ_EM_ATIVACAO`, `LQ_NAO_VIAVEL`, `LQ_CONTA`, `LQ_NOVO` | Classificação comercial do lead. |

## Perguntas para aprofundar

| Pergunta | Caminho |
|---|---|
| Quais rotas afetam contrato? | [[Endpoints da Collection/Index]] e busca por `contrato`. |
| Quais queries retornam dados de cliente? | [[Queries por Endpoint da Collection]] e [[Operacional/Dados Sensiveis]]. |
| Onde há integração externa no fluxo? | [[Dependencias e Integracoes]] e seção de integrações em cada fluxo. |
| O que pode ser reprocessado? | Runbook do fluxo em [[Operacional/Runbooks/Index]]. |
| Onde existe escrita? | [[Operacional/Mapa de Escrita]]. |
