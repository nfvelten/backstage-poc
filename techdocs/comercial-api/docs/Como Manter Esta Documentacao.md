---
tags:
  - trabalho
  - air
  - api
  - comercial-api
  - docs-as-code
---
# Como Manter Esta Documentacao

Playbook para manter a documentação da `comercial-api` próxima do código, da collection e das queries versionadas.

## Quando regenerar

| Mudança | Ação |
|---|---|
| Novo endpoint ou alteração em controller | Regenerar inventário de endpoints e revisar fluxo. |
| Novo request Bruno | Rodar mapeamento collection -> código -> query. |
| Alteração em query SQL/JPA | Regenerar queries por endpoint e shape de SELECT. |
| Alteração em escrita ou integração externa | Atualizar mapa de escrita, dependências e runbook. |
| Alteração de tabela/migration | Regenerar banco/migrations e revisar queries impactadas. |
| Alteração em tabela central | Atualizar [[Contratos de Dados/Index]] e [[Diagramas/modelo-dominio]]. |
| Alteração em fluxo crítico | Atualizar [[Diagramas/Index]] quando o caminho de negócio mudar. |
| Alteração em service crítico | Atualizar [[Services Criticos/Index]] e revisar endpoints impactados. |
| Alteração em reprocessamento/idempotência | Atualizar [[Mapa de Reprocessamento]] e runbooks relacionados. |

## Ordem recomendada

Execute a partir do vault `/home/nfvelten/amphora`.

```bash
python3 Trabalho/Air/APIs/scripts/mapear-queries-collection-comercial-api.py
python3 Trabalho/Air/APIs/scripts/documentar-resultados-select-comercial-api.py
python3 Trabalho/Air/APIs/scripts/gerar-fluxos-comercial-api.py
python3 Trabalho/Air/APIs/scripts/gerar-operacional-comercial-api.py
python3 Trabalho/Air/APIs/scripts/gerar-governanca-comercial-api.py
```

## Fontes de verdade

| Fonte | Uso |
|---|---|
| Código Spring | Endpoints, repositories, services, chamadas internas, escrita e integração. |
| Bruno collection | O que está sendo documentado como API usada/recente. |
| `air-db-queries` | SQL versionado por endpoint/fluxo. |
| Banco prod main | Metadados de schema e shape de SELECT com `LIMIT 0`. |
| Logs/APM/gateway | Uso real, endpoint morto, endpoint quente e latência. |

## Política de segurança

- Não registrar linhas reais de produção no vault.
- Para SELECT, documentar somente colunas/shape, usando `LIMIT 0`.
- Não registrar valores de propriedades sensíveis; usar apenas o nome da chave e a classe que consome.
- Não colar CPF, CNPJ, telefone, e-mail, token, senha, endereço completo ou payload real em Markdown.
- Se uma query retornar campo sensível, documentar a categoria do campo, não o valor.

## Revisão depois de regenerar

1. Abrir `git status` do vault, collection e query repo.
2. Revisar endpoints novos, removidos ou sem match com controller.
3. Revisar SQLs novos e garantir nome sem prefixo de endpoint quando a query for reutilizável.
4. Conferir se arquivos em `Resultados SELECT/` foram criados para todos os SELECTs.
5. Conferir se fluxos críticos ainda apontam para endpoint/query corretos.
6. Atualizar [[Dependencias e Integracoes]] se aparecer nova classe HTTP, propriedade ou serviço externo.
7. Atualizar [[Ownership e Operacao]] se a mudança alterar risco ou runbook.
8. Atualizar [[Contratos de Dados/Index]] se a mudança tocar `tbl_cliente`, `tbl_endereco`, `tbl_contrato`, `tbl_lead`, `tbl_venda` ou `tbl_analise_credito`.
9. Atualizar [[Diagramas/Index]] se a mudança alterar relação entre entidades, dependências externas ou fluxo crítico.
10. Atualizar [[Services Criticos/Index]] se a mudança alterar regra central, escrita ou dependência externa.
11. Atualizar [[Mapa de Reprocessamento]] se a mudança alterar retry, reversão, idempotência ou reconciliação.
12. Revisar [[Health Check da Documentacao]]; falha ali indica documentação incompleta.
13. Revisar [[Consumers por Endpoint]] antes de considerar rota candidata a remoção; busca estática não substitui telemetria real.
14. Quando o gerador marcar chamada não resolvida, documentar a resolução em [[Call Graph Manual]] ou ajustar o script de governança para reconhecê-la.
15. Lacunas que dependem de uso real ficam como validação futura; sem logs/APM/gateway não classificar endpoint como morto.

## Como documentar endpoint novo

| Item | O que registrar |
|---|---|
| Collection | Método, rota, path params, query params, body exemplo sem segredo e contexto funcional. |
| Endpoint page | Controller/método, service principal, queries, operações JPA e pendências. |
| SQL | Um arquivo por query reutilizável, com comentário de contexto no topo quando necessário. |
| SELECT shape | Colunas retornadas, origem e status da introspecção. |
| Fluxo | Objetivo, risco, integrações, escrita, dados sensíveis e runbook. |
| Contrato de dados | Significado da tabela, campos importantes, índices/FKs, endpoints/queries e cuidados de mudança. |
| Diagrama | Mermaid curto, com links para os documentos textuais que sustentam o desenho. |
| Service crítico | Responsabilidade, endpoints que passam por ele, tabelas, integrações e cuidados de mudança. |
| Reprocessamento | O que pode ser refeito, pré-checagens, risco de duplicidade e evidências para validar depois. |

## Critérios de qualidade

- Uma pessoa nova deve conseguir sair de uma rota para: controller, service, query, tabela, shape, fluxo, risco e runbook.
- Uma pessoa em incidente deve conseguir identificar se o problema é endpoint, banco, integração externa ou payload.
- Uma pessoa alterando query deve conseguir saber quais endpoints e fluxos serão impactados.
- Uma pessoa revisando segurança deve conseguir listar campos e fluxos com PII/credencial/crédito.
