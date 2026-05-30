---
tags:
  - trabalho
  - air
  - comercial-api
  - revisao
---
# Trilhas de Revisao - comercial-api

Caminhos curtos para revisar mudança, incidente ou remoção sem depender de memória tribal.

## Alterar endpoint

1. [[Endpoints da Collection/Index]]
2. [[Payloads e DTOs/Index]]
3. [[Matriz de Impacto]]
4. [[Mapa Endpoint Service Repository Tabela]]
5. [[Fluxos de Negocio/Index]]
6. [[Operacional/Runbooks/Index]] se houver escrita ou risco alto.

## Alterar query SQL/JPA

1. [[Queries por Endpoint da Collection]]
2. [[Resultados SELECT/Index]]
3. [[Operacional/Performance Queries]]
4. [[Matriz de Escrita por Tabela]]
5. [[Matriz de Impacto]]
6. [[Contratos de Dados/Index]] se tocar tabela central.

## Alterar tabela central

1. [[Contratos de Dados/Index]]
2. [[Banco - air_comercial]]
3. [[Migrations]]
4. [[Diagramas/modelo-dominio]]
5. [[Matriz de Escrita por Tabela]]
6. [[Mapa de Risco]]
7. [[Operacional/Dados Sensiveis]] se houver PII/crédito/credencial.

## Incidente

1. Identificar rota e abrir [[Matriz de Impacto]].
2. Abrir fluxo em [[Fluxos de Negocio/Index]].
3. Verificar runbook em [[Operacional/Runbooks/Index]].
4. Se envolver banco, abrir [[Matriz de Escrita por Tabela]] e [[Operacional/Performance Queries]].
5. Se envolver integração, abrir [[Integracoes Externas/Index]] e [[Dependencias e Integracoes]].
6. Se houver reprocessamento, abrir [[Mapa de Reprocessamento]] e [[Testes Manuais/Index]].

## Remover ou depreciar endpoint

1. [[Consumers por Endpoint]] para busca estática.
2. Logs/APM/gateway para uso real.
3. [[Matriz de Impacto]] para fluxo/query/tabela afetados.
4. [[Score de Maturidade Documental]] para lacunas antes de decidir.
5. Registrar decisão em [[ADRs/Index]] se a remoção for relevante.

## Alterar regra de domínio

1. [[Glossario Comercial]] para confirmar termo e agregado.
2. [[Ciclos de Vida/Index]] para estado/transição afetados.
3. [[Ownership por Dominio]] para owner documental e escalação.
4. [[Playbooks de Mudanca]] para checklist específico.
5. [[Mapa de Risco]] para sensibilidade e risco de duplicidade.
