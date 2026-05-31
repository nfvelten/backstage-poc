---
tags:
  - trabalho
  - air
  - api
  - comercial-api
  - dependencias
---
# Dependencias e Integracoes - comercial-api

Mapa das dependências observadas por análise estática do código, `pom.xml`, propriedades de configuração e documentação gerada. Este documento registra nomes de propriedades e classes, nunca valores sensíveis.

## Bancos e dados

| Dependência | Uso observado | Evidência |
|---|---|---|
| MySQL `air_comercial` | Banco primário do domínio comercial, JPA, native queries e Flyway. | `spring.datasource.*`, [[Banco - air_comercial]], [[Migrations]] |
| Schemas MySQL adjacentes | Consultas cross-schema para chamado, internet, base e telefonia. | [[Operacional/Performance Queries]] |
| SQL Server / SAP | Integrações de composição/produto/pacote e dados SAP. | Propriedades `datasource.sqlserver.*`, controllers/services `*Sap*` |
| EhCache | Cache local via dependência. | `pom.xml` |
| Flyway | Versionamento de schema. | `flyway.enabled`, [[Migrations]] |

## APIs externas e serviços internos

| Dependência | Finalidade inferida | Classes/pacotes de origem | Propriedades/chaves |
|---|---|---|---|
| Sydle | Integração de contrato, cliente, venda e fluxos de ativação. | `SydleConnection`, `IntegracaoService`, `ContratoService`, `HabilitarConfiancaService` | `sydle.*`, `air-sydle.*` |
| Chamado | Criação/consulta de chamados e OS ligadas a venda/contrato. | `ChamadoService`, queries cross-schema `air_chamado.*` | `chamado.*` |
| ConnectMaster | Integração e rotina de cancelamento. | `ConnectMasterIntegracaoService`, `RotinaCancelamento` | `connectmaster.*` |
| OAuth / Keycloak | Integrar/remover usuário e autenticação eCare. | `OauthIntegracaoService`, `KeycloakAuthClientImpl`, `EcareClientImpl` | `oauth.*`, `keycloak.*`, `ecare.*` |
| Notification API | Notificações, WhatsApp/URA e envio de mensagens. | `NotificationIntegracaoService`, `NotificationApiProvider`, `NotificationService` | `notification.*`, `wpp.*` |
| Link shortener | Encurtamento de links enviados por notificação. | `LinkShortenerProvider` | `link-shortener.*` |
| CRM service / barramento CRM | Integrações de cliente/contrato com CRM. | `CrmServiceProvider` | `crm.*`, `barramento.*` |
| Financial service | Consultas/integrações financeiras. | `FinancialServiceProvider`, `financeiro/*` | `financial.*`, `financeiro.*` |
| TV API | Integrações ligadas a TV/serviços. | `AirTvProvider` | `tv.*` |
| Internet/Telefonia | Avisos, reservas, contratos e consultas cross-schema. | `ContratoService`, SQLs de aviso | `internet.*`, `telefonia.*` |
| SPC/Serasa | Consulta de crédito/restrição. | `spc/soap/*`, `RotinaConsultaSPC`, `AnaliseCreditoService` | `spc.*`, `serasa.*` |
| RD Station | Origem/integração de marketing/venda. | Pacotes de venda/lead e propriedades de integração | `rdstation.*` |

## Gateways e clientes HTTP

| Classe | Tipo | Observação |
|---|---|---|
| `AppConfiguration` | `RestTemplate` bean | Configura templates padrão e Sydle com timeout. |
| `restPattern/Rest` | Helper HTTP | Wrapper próprio para chamadas REST com timeout opcional. |
| `SydleConnection` | Cliente HTTP | Comunicação com Sydle. |
| `ConnectionTokenManager` | Cliente HTTP/token | Monta `RestTemplate` com autenticação por API key. |
| `EcareClientImpl` | Cliente HTTP | Cliente eCare. |
| `KeycloakAuthClientImpl` | Cliente HTTP | Autenticação Keycloak/eCare. |
| `ConnectMasterIntegracaoService` | Cliente HTTP | Integração ConnectMaster. |
| `OauthIntegracaoService` | Cliente HTTP | Integração/removal OAuth. |
| `NotificationIntegracaoService` | Cliente HTTP | Notification API e URA. |
| `CrmServiceProvider` | Gateway clean arch | CRM service. |
| `FinancialServiceProvider` | Gateway clean arch | Financial service. |
| `NotificationApiProvider` | Gateway clean arch | Notification API. |
| `LinkShortenerProvider` | Gateway clean arch | Link shortener. |
| `AirTvProvider` | Gateway clean arch | TV API. |

## Rotinas agendadas

| Rotina | Agenda | Responsabilidade inferida | Risco |
|---|---|---|---|
| `connectmaster/rotina/RotinaCancelamento` | `fixedRate = 3_600_000` | Processar cancelamentos/integrações ConnectMaster periodicamente. | Médio: integração externa e possível efeito colateral. |
| `oauth/rotina/RotinaIntegracao` | `fixedDelay = 1_000` | Processamento frequente de integrações OAuth pendentes. | Alto: autenticação/credencial e fila com alta frequência. |
| `oauth/rotina/RotinaIntegracao` | `cron = "0 * 1-5 * * *"` | Rotina programada em janela de madrugada. | Alto: autenticação e alteração de estado. |
| `cliente/rotinas/RotinaRemocaoMarcadoresExpirados` | `cron = "0 1 0 * * ?"` | Remover marcadores expirados de clientes. | Médio: alteração em cliente. |
| `spc/rotina/RotinaConsultaSPC` | Sem agenda ativa observada no trecho buscado | Consulta/rotina SPC parece existir, mas annotations podem estar comentadas ou condicionais. | Revisar antes de operar. |

## Eventos internos

| Evento/listener | Origem | Uso provável |
|---|---|---|
| `ClienteEvent` / `ClienteListener` | Pacote `cliente/event` | Reações assíncronas/síncronas a mudanças de cliente. |
| `AvisoEvent` | Pacote `cliente/event` | Propagação de avisos relacionados a cliente/contrato. |
| `CondominioEvent` / `CondominioEventListener` | Pacote `configuracoes/event` | Reações a mudanças de condomínio/configuração. |
| `LeadEvent` / `LeadListener` | Pacote `venda/event` | Reações a mudanças de lead/venda. |

## Consumidores conhecidos ou prováveis

| Consumidor | Evidência | Status |
|---|---|---|
| Collection comercial Bruno | Requests versionadas e documentadas. | Confirmado para a documentação atual. |
| CRM / barramento | Nomes de propriedades, fluxos de integração e histórico de memória do projeto. | Provável; confirmar por logs/gateway. |
| Customer support / atendimento | Rotas de cliente, contrato, aviso, URA e consulta. | Provável; confirmar por logs/gateway. |
| Financial service | Gateways financeiros e controllers financeiros. | Provável; confirmar por logs/gateway. |
| Chamado API | Integrações e queries `air_chamado`. | Provável; confirmar por logs/gateway. |
| TV/Internet/Telefonia | Gateways e SQLs cross-schema. | Provável; confirmar por logs/gateway. |

## Lacunas de confiabilidade por dependência

| Lacuna | Impacto | Próximo passo |
|---|---|---|
| Timeouts/retries não documentados por chamada | Incidente externo pode degradar endpoint comercial. | Levantar timeout/retry por classe HTTP e registrar nesta página. |
| Ownership das dependências ausente | Escalação fica tribal. | Preencher owner/canal por dependência. |
| Contrato de payload externo ausente | Mudança em serviço externo pode quebrar fluxo crítico. | Adicionar exemplos/schema por integração de alto risco. |
| Métricas por dependência ausentes | Difícil separar lentidão interna de falha externa. | Criar painel por host/cliente HTTP ou tag de integração. |
