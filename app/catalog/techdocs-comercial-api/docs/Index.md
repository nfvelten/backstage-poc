---
tags:
  - trabalho
  - air
  - api
  - documentacao
  - comercial-api
gerado_em: 2026-05-29 21:07:41
---
# comercial-api - documentacao gerada

Documentacao regeneravel da `comercial-api`, cruzando codigo, banco prod main, queries versionadas e Bruno collection.

## Fontes

| Fonte | Caminho |
|---|---|
| Codigo | `/home/nfvelten/code/work/comercial-api` |
| Bruno collection | `/home/nfvelten/code/work/air-api-collection` |
| Queries SQL | `/home/nfvelten/code/work/air-db-queries` |
| Banco | `airdb-prod-main / air_comercial` |

## Artefatos

| Nota | Conteudo |
|---|---|
| [[Health Check da Documentacao]] | Checks de cobertura documental: endpoint, SQL, SELECT shape, runbook, contrato de dados e docs base. |
| [[Score de Maturidade Documental]] | Score heurístico por endpoint para priorizar lacunas de documentação. |
| [[Backlog de Documentacao]] | Lista priorizada de melhorias documentais gerada a partir de risco, score e pendências. |
| [[Trilhas de Revisao]] | Caminhos de consulta para mudança, incidente, query, tabela e remoção de endpoint. |
| [[Call Graph Manual]] | Resoluções manuais de chamadas que a análise estática inicial não fechou. |
| [[Mapa de Reprocessamento]] | Guia de reprocessamento/idempotência para fluxos críticos de escrita e integração. |
| [[Services Criticos/Index]] | Documentação por classe service crítica, com endpoints, tabelas e métodos de atenção. |
| [[Glossario Comercial]] | Termos de domínio, tabelas, docs relacionados e cuidados de segurança/operação. |
| [[Ciclos de Vida/Index]] | Estados e transições de cliente, lead, venda e contrato. |
| [[Matriz de Escrita por Tabela]] | Visão invertida por dado: quem lê, quem escreve, services e risco. |
| [[Integracoes Externas/Index]] | Contratos operacionais de integrações externas sem payload real. |
| [[Playbooks de Mudanca]] | Checklists de revisão para alterações comuns em query, payload, status, OAuth, contrato e crédito. |
| [[Mapa de Risco]] | Classificação qualitativa por dado/domínio: sensibilidade, escrita, integração e duplicidade. |
| [[Testes Manuais/Index]] | Roteiros seguros de validação manual por fluxo crítico. |
| [[Ownership por Dominio]] | Responsabilidade documental sugerida por domínio e caminho de escalação. |
| [[Mapa Endpoint Service Repository Tabela]] | Visão única rota -> código -> query/operação -> tabela resolvida manualmente. |
| [[Matriz de Impacto]] | Mapa endpoint -> fluxo -> código -> queries -> SELECTs -> pendências para review e mudança. |
| [[Payloads e DTOs/Index]] | Estrutura de body/headers da collection, tipos inferidos e sensibilidade por campo. |
| [[Consumers por Endpoint]] | Busca estática em repositórios consumidores conhecidos para cada rota da collection. |
| [[Service Catalog]] | Identidade do serviço, stack, runtime, fronteiras, owners pendentes e links principais. |
| [[Mapa de Dominio]] | Glossário dos conceitos comerciais, pacotes do código e entidades centrais. |
| [[Contratos de Dados/Index]] | Contratos das tabelas centrais: significado, campos, índices, FKs, endpoints, queries e riscos. |
| [[Diagramas/Index]] | Diagramas Mermaid de contexto, dependências, domínio e fluxos críticos. |
| [[Dependencias e Integracoes]] | Mapa de bancos, APIs externas, gateways, rotinas agendadas, eventos e consumidores conhecidos. |
| [[Codigo]] | Inventario de classes, pacotes, annotations e SQL nativo no codigo. |
| [[Endpoints - Codigo]] | Endpoints extraidos dos controllers Spring. |
| [[Endpoints - Bruno]] | Requests documentadas na collection Bruno. |
| [[Fluxos de Negocio/Index]] | Fluxos de negócio com endpoints, DTOs, queries, tabelas, integrações, efeitos colaterais e riscos. |
| [[Operacional/Index]] | Matriz de risco, mapa de escrita, dados sensíveis, performance e runbooks. |
| [[Ownership e Operacao]] | Responsabilidade, sinais de saúde, rotina de incidentes e lacunas operacionais. |
| [[Como Manter Esta Documentacao]] | Playbook para regenerar, revisar e ampliar a documentação sem expor dados sensíveis. |
| [[Checklist de Mudanca]] | Checklist de PR/release para manter endpoint, query, fluxo, segurança e operação alinhados. |
| [[ADRs/Index]] | Decisões arquiteturais/documentais tomadas para este pacote de documentação. |
| [[Endpoints da Collection/Index]] | Entrada principal por endpoint da collection comercial, com queries, SQL, JPA/repository e shape de retorno. |
| [[Queries por Endpoint da Collection]] | Relatorio agregado endpoint -> queries/operações. |
| [[Resultados SELECT/Index]] | Shape modularizado dos SELECTs introspectado no prod main com `LIMIT 0`. |
| [[Banco - air_comercial]] | Tabelas, colunas, indices e FKs do schema em prod main. |
| [[Migrations]] | Historico de migrations Flyway do projeto. |
| [[Queries SQL]] | Queries versionadas em `air-db-queries`. |

## Resumo

| Item | Quantidade |
|---|---:|
| Classes Java | 825 |
| Endpoints no codigo | 224 |
| Requests Bruno | 49 |
| Migrations Flyway | 190 |
| Tabelas em prod main | 134 |
| Colunas em prod main | 1551 |

## Resumo da documentacao operacional

| Item | Quantidade |
|---|---:|
| Endpoints da collection comercial documentados | 24 |
| Queries/operacoes mapeadas a endpoints | 41 |
| Arquivos SQL da collection em `air-db-queries` | 22 |
| Shapes de SELECT introspectados | 22 |
| Fluxos de negocio documentados | 10 |
| Runbooks gerados | 10 |
| Contratos de dados centrais | 6 |
| Diagramas Mermaid | 5 |
| Payload docs da collection | 24 |
| Health checks documentais | gerado |
| Scores de maturidade | gerado |
| Backlog documental | gerado |
| Chamadas resolvidas manualmente | 18 |
| Services criticos documentados | 5 |
| Fluxos com mapa de reprocessamento | 4 |
| Termos no glossario comercial | 11 |
| Ciclos de vida documentados | 4 |
| Tabelas na matriz de escrita | 15 |
| Integracoes externas documentadas | 6 |
| Playbooks de mudanca | 6 |
| Consumers por endpoint | gerado |
| ADRs de documentacao | 8 |

## Maiores controllers por endpoints

| Controller | Endpoints |
|---|---:|
| ClienteController | 33 |
| ContratoController | 30 |
| VendaController | 12 |
| LeadController | 11 |
| ContratoRetencaoController | 10 |
| NotificationController | 10 |
| CampanhaController | 7 |
| EnderecoCidadeController | 7 |
| VendedorController | 7 |
| ClienteAnexoController | 6 |
| IntegracaoController | 6 |
| ContractsControllerV1 | 5 |
| ContactControllerV1 | 5 |
| BlacklistController | 5 |
| ClienteContatoController | 5 |
| ItemSapController | 5 |
| PacoteSapController | 5 |
| ProdutoSapController | 5 |
| VencimentoController | 5 |
| NotificationControllerV1 | 4 |

## Collections Bruno

| Collection | Requests |
|---|---:|
| chamado | 17 |
| comercial | 13 |
| cyclopay | 7 |
| barramento | 3 |
| crm | 3 |
| internet | 3 |
| loki | 2 |
| sumicity | 1 |
