# ADR 0003 - Mapear endpoint e query por analise estatica

## Status

Aceita.

## Contexto

O uso real de endpoints depende de logs, gateway ou APM. Esses dados nem sempre estão disponíveis no momento da geração da documentação. Por outro lado, a collection comercial é recente e o código contém controllers, services, repositories e SQLs suficientes para montar um mapa inicial.

## Decisão

Usar análise estática como primeira fonte de rastreabilidade:

- collection Bruno para endpoints funcionais;
- controllers Spring para rota e método;
- services/repositories para chamadas internas;
- SQL/JPA/Spring Data para queries e operações;
- banco apenas para shape de SELECT.

Logs/APM/gateway entram como camada futura para marcar endpoint quente, pouco usado ou candidato a remoção.

## Consequências

- O mapa endpoint -> query fica disponível mesmo sem acesso a telemetria.
- Chamadas dinâmicas, reflexão ou fluxo indireto podem ficar como pendência.
- A documentação deve manter uma coluna de pendências e não fingir cobertura total quando o call graph não resolver tudo.
