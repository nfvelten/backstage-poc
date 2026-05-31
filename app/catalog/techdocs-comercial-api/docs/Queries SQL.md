---
tags: [trabalho, air, api, documentacao, sql]
gerado_em: 2026-05-29 21:07:41
---
# Queries SQL

Inventario dos arquivos `.sql` em `air-db-queries`.

| Area | Arquivo | Operacoes | Tabelas citadas | Contexto no topo |
|---|---|---|---|---|
| chamado | `air-db-queries/chamado/protocolos-ura-fechar.sql` | SELECT:3, UPDATE:2 | tbl_chd_chamado, tbl_os | Card 22948: Fechar protocolos URA abertos em massa / DB: air_chamado (prod main 10.99.1.155) / Mesma lógica da RotinaProtocolos (cron 03h) /  / ATENÇÃO: usar NOT EXISTS, não NOT IN / tbl_os tem registros com id_chamado = NULL → NOT IN retorna 0 rows / Verificação antes de rodar: |
