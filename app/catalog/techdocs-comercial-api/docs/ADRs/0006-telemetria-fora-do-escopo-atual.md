# ADR 0006 - Manter telemetria fora do escopo atual da documentação

- Status: Aceita
- Decisão: Itens que exigem logs/APM/gateway ficam marcados como fora do escopo atual.

## Contexto

A documentação atual usa código, collection, queries e metadados de banco. Uso real de produção depende de fontes externas e políticas de acesso.

## Consequências

- Sem consumer estático não significa endpoint morto.
- Backlog P2 pode permanecer apenas como validação futura.
- Decisão de remoção não deve ser tomada só por análise estática.
