# ADR 0001 - Documentacao como catalogo operacional

## Status

Aceita.

## Contexto

A `comercial-api` tem muitos endpoints, queries, integrações e rotinas espalhadas entre código, collection, query repo e banco. Um inventário bruto ajuda pouco em incidente ou evolução, porque não mostra fluxo, risco, dono, dependência e efeito colateral.

## Decisão

Organizar a documentação como catálogo operacional:

- `Service Catalog` para identidade e fronteiras do serviço.
- `Dependencias e Integracoes` para bancos, APIs, rotinas e eventos.
- `Fluxos de Negocio` para agrupar endpoints por jornada.
- `Operacional` para risco, escrita, dados sensíveis, performance e runbooks.
- `ADRs` para registrar decisões de documentação.

## Consequências

- A entrada principal deixa de ser só “lista de endpoint” e passa a responder perguntas de operação e mudança.
- A documentação precisa ser regenerável e revisada quando código, collection ou query mudar.
- Lacunas ficam explícitas em vez de escondidas, como owner, SLO e consumers reais.
