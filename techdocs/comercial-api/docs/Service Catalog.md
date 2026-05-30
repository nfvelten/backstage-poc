---
tags:
  - trabalho
  - air
  - api
  - comercial-api
  - service-catalog
---
# Service Catalog - comercial-api

Catalogo operacional do serviço `comercial-api`, inspirado em práticas de service ownership/documentação interna usadas por empresas com muitos serviços: identidade clara, fronteiras explícitas, dependências versionadas, links de operação e lacunas rastreáveis.

## Identidade

| Campo | Valor |
|---|---|
| Nome técnico | `air-comercial` / `comercial-api` |
| Descrição | API REST de apoio ao domínio comercial: cliente, contrato, venda, análise de crédito, migração, avisos, integrações e configurações comerciais. |
| Linguagem/runtime | Java 8 |
| Framework | Spring Boot `1.5.x`, Spring MVC, Spring Data JPA, Spring Security, Actuator, WebSocket |
| Build | Maven |
| Banco primário documentado | `air_comercial` em `airdb-prod-main` |
| Migrations | Flyway habilitado no projeto |
| Collection usada como fonte funcional | `/home/nfvelten/code/work/air-api-collection/comercial` |
| Query repo documentado | `/home/nfvelten/code/work/air-db-queries/comercial/comercial-api/collection-endpoints` |

## Fronteiras de domínio

| Área | Responsabilidade observada |
|---|---|
| Cliente | Cadastro, contato, endereço, blacklist, marcadores, orientação e dados cadastrais. |
| Contrato | Consulta, criação via integração, aviso, SVA, entrega, campanha, reajuste, suspensão e retenção. |
| Venda/Lead | Lead, venda, fase, origem, análise de crédito, bloqueios e renegociação. |
| Configurações comerciais | Campanhas, carteiras, vendedores, vencimentos, endereços e termos. |
| Integrações | Sydle, Chamado, ConnectMaster, OAuth/Keycloak, notification, CRM, financeiro, TV, link shortener e serviços externos. |
| Operacional interno | Rotinas agendadas, eventos Spring, métricas, health e endpoints auxiliares. |

## Links principais

| Pergunta | Onde consultar |
|---|---|
| Quais endpoints existem no código? | [[Endpoints - Codigo]] |
| Quais endpoints da collection são usados? | [[Endpoints da Collection/Index]] |
| Quais queries cada endpoint usa? | [[Queries por Endpoint da Collection]] |
| Qual o shape de retorno dos SELECTs? | [[Resultados SELECT/Index]] |
| Quais fluxos de negócio existem? | [[Fluxos de Negocio/Index]] |
| Quais fluxos escrevem dados ou têm risco alto? | [[Operacional/Matriz de Cobertura e Risco]] |
| Quais queries parecem mais pesadas? | [[Operacional/Performance Queries]] |
| Como agir em incidente por fluxo? | [[Operacional/Runbooks/Index]] |
| Quais integrações e rotinas existem? | [[Dependencias e Integracoes]] |

## Princípios de documentação

- A collection Bruno recente é tratada como fonte funcional do que está em uso.
- O código Spring é tratado como fonte de verdade para endpoints, chamadas internas, repositories e efeitos colaterais.
- O banco prod main é usado apenas para metadados e shape de SELECT, sem capturar linhas reais.
- Valores sensíveis de configuração não devem entrar na documentação; registrar somente nome de propriedade, classe e finalidade.
- Quando houver conflito entre código e collection, documentar a divergência e preferir abrir pendência em vez de esconder a diferença.

## Lacunas abertas

| Lacuna | Por que importa | Próximo passo |
|---|---|---|
| Owner formal do serviço | Incidentes e mudanças precisam de responsável claro. | Preencher time, canal e escalation em [[Ownership e Operacao]]. |
| SLO/SLI | Hoje a documentação aponta rotas e riscos, mas não define objetivo de disponibilidade/latência. | Adicionar SLO por fluxo crítico quando houver métrica confiável. |
| Consumers reais por rota | Parte dos consumidores pode estar fora da collection. | Cruzar logs/gateway/APM com endpoints do código e da collection. |
| Contratos de payload | A collection tem exemplos, mas ainda não há schema formal por DTO. | Gerar OpenAPI ou contrato Markdown por controller/DTO. |
| Dependências com criticidade | Integrações estão mapeadas, mas nem todas têm timeout, retry, dono ou impacto definidos. | Completar [[Dependencias e Integracoes]] com dono e runbook por dependência. |
