# ADRs - comercial-api

Decisões sobre arquitetura de documentação e rastreabilidade da `comercial-api`.

| ADR | Status | Decisão |
|---|---|---|
| [0001](0001-documentacao-como-catalogo-operacional.md) | Aceita | Tratar a documentação como catálogo operacional, não só inventário de endpoints. |
| [0002](0002-nao-documentar-dados-reais-de-producao.md) | Aceita | Usar produção apenas para metadados/shape, sem registrar linhas reais. |
| [0003](0003-mapear-endpoint-query-por-analise-estatica.md) | Aceita | Começar por análise estática + collection e complementar com logs/APM depois. |
| [0004](0004-collection-como-contrato-operacional.md) | Aceita | Usar collection recente como contrato operacional documentado. |
| [0005](0005-documentar-jpa-e-sql-com-a-mesma-rastreabilidade.md) | Aceita | Documentar JPA/repository e SQL nativo na mesma trilha. |
| [0006](0006-telemetria-fora-do-escopo-atual.md) | Aceita | Manter telemetria fora do escopo atual da documentação. |
| [0007](0007-documentar-ciclos-de-vida-e-risco-por-dado.md) | Aceita | Documentar ciclos de vida e risco por dado central. |
| [0008](0008-nao-versionar-payload-real-de-integracao.md) | Aceita | Não versionar payload real de integração externa. |
