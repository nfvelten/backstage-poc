---
tags:
  - trabalho
  - air
  - comercial-api
  - playbook
---
# Playbooks de Mudanca - comercial-api

Checklists para mudanças comuns. A ideia é transformar revisão em caminho repetível, não depender de lembrança do código.

## Alterar análise de crédito

- Identificador: `alterar-analise-credito`

### Passos

1. Abrir [[Fluxos de Negocio/analise-credito]].
2. Abrir [[Integracoes Externas/spc-serasa]].
3. Revisar [[Contratos de Dados/tbl_analise_credito]].
4. Checar política de dados sensíveis.

### Pronto quando

- Sem XML/retorno real em docs
- Reprocessamento restrito
- Campos sensíveis classificados

## Alterar criação de contrato

- Identificador: `alterar-criacao-contrato`

### Passos

1. Abrir [[Fluxos de Negocio/criacao-integracao-contrato]].
2. Abrir [[Ciclos de Vida/contrato]], [[Ciclos de Vida/venda]] e [[Ciclos de Vida/lead]].
3. Revisar [[Services Criticos/contrato-service]] e [[Services Criticos/venda-service]].
4. Checar tabelas em [[Matriz de Escrita por Tabela]].

### Pronto quando

- Idempotência revisada
- Tabelas de escrita conhecidas
- Integrações externas revisadas

## Alterar integração OAuth/Keycloak

- Identificador: `alterar-oauth`

### Passos

1. Abrir [[Integracoes Externas/oauth-keycloak-ecare]].
2. Revisar [[Services Criticos/oauthintegracao-service]].
3. Conferir status em [[Mapa de Reprocessamento]].
4. Validar que nenhum token/senha entrou em docs/logs.

### Pronto quando

- Falha/retry documentados
- Status de cliente conhecido
- Rollback/reprocessamento descrito

## Alterar payload de endpoint

- Identificador: `alterar-payload`

### Passos

1. Atualizar collection Bruno.
2. Regenerar [[Payloads e DTOs/Index]].
3. Revisar sensibilidade dos novos campos.
4. Atualizar fluxo e teste manual se alterar regra de negócio.

### Pronto quando

- Campo novo com tipo inferido
- PII/credencial marcada
- Endpoint e fluxo linkados

## Alterar query SQL/JPA

- Identificador: `alterar-query`

### Passos

1. Localizar endpoint em [[Queries por Endpoint da Collection]].
2. Abrir shape em [[Resultados SELECT/Index]].
3. Revisar impacto em [[Matriz de Escrita por Tabela]].
4. Checar performance em [[Operacional/Performance Queries]].
5. Atualizar contrato de dados se a query tocar tabela central.

### Pronto quando

- Shape SELECT atualizado
- Endpoints impactados conhecidos
- Campos sensíveis classificados
- Nenhum valor real copiado

## Alterar status/fase de venda

- Identificador: `alterar-status-venda`

### Passos

1. Abrir [[Ciclos de Vida/venda]].
2. Revisar [[Services Criticos/venda-service]].
3. Conferir [[Mapa de Reprocessamento]].
4. Checar impacto em contrato, campanha e notificação.

### Pronto quando

- Transição documentada
- Risco de reprocessamento avaliado
- Testes manuais atualizados
