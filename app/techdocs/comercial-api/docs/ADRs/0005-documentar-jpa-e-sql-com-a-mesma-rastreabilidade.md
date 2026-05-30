# ADR 0005 - Documentar JPA/repository e SQL nativo na mesma trilha

- Status: Aceita
- Decisão: Queries derivadas, native queries e operações CRUD devem aparecer junto do endpoint e do fluxo.

## Contexto

Parte do acesso a dados está em SQL versionado e parte em repositories/services herdados.

## Consequências

- Call graph manual é aceito para resolver herança/abstrações.
- Shape de SELECT só existe para SQL consultável.
- Operações CRUD precisam mapear entidade/tabela quando possível.
