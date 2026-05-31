---
tags:
  - trabalho
  - air
  - api
  - comercial-api
  - operacao
---
# Ownership e Operacao - comercial-api

Documento para transformar a documentação técnica em operação repetível: quem responde, quais sinais olhar, como investigar e quais lacunas precisam virar tarefa.

## Ownership

| Campo | Valor atual |
|---|---|
| Owner funcional | Pendente preencher |
| Owner técnico | Pendente preencher |
| Canal de suporte | Pendente preencher |
| Canal de incidentes | Pendente preencher |
| Repositório código | `/home/nfvelten/code/work/comercial-api` |
| Repositório collection | `/home/nfvelten/code/work/air-api-collection/comercial` |
| Repositório queries | `/home/nfvelten/code/work/air-db-queries/comercial/comercial-api/collection-endpoints` |

## Health e observabilidade

| Sinal | Onde olhar | Observação |
|---|---|---|
| Health da aplicação | Actuator `health` | Confirmar path exposto no ambiente. |
| Métricas Prometheus | Dependências Micrometer/Prometheus e `MetricsController` | Padronizar dashboard por endpoint/fluxo. |
| Logs estruturados | Dependência `logstash-gelf` | Confirmar destino e tags em produção. |
| Erros por endpoint | Gateway/APM/logs | Cruzar com [[Endpoints da Collection/Index]]. |
| Lentidão por query | Banco/APM + [[Operacional/Performance Queries]] | Priorizar queries largas/cross-schema. |
| Falha em integração externa | Logs da classe gateway + [[Dependencias e Integracoes]] | Separar indisponibilidade externa de bug interno. |

## Severidade sugerida

| Severidade | Critério |
|---|---|
| SEV1 | Criação de contrato, ativação de serviço, OAuth/Keycloak ou consulta central de cliente indisponível de forma ampla. |
| SEV2 | Fluxo comercial degradado, lentidão relevante, falha parcial de integração externa com workaround manual. |
| SEV3 | Endpoint específico ou rotina com impacto localizado, sem bloqueio geral do fluxo comercial. |
| SEV4 | Divergência documental, endpoint obsoleto, query sem shape ou melhoria de rastreabilidade. |

## Checklist de incidente

1. Identificar rota afetada no log/gateway.
2. Abrir a página correspondente em [[Endpoints da Collection/Index]].
3. Confirmar fluxo em [[Fluxos de Negocio/Index]] e risco em [[Operacional/Matriz de Cobertura e Risco]].
4. Se houver query, verificar [[Operacional/Performance Queries]] e o shape em [[Resultados SELECT/Index]].
5. Se houver escrita, consultar [[Operacional/Mapa de Escrita]] antes de reprocessar.
6. Se houver dado sensível, seguir [[Operacional/Dados Sensiveis]] e evitar colar payload real em issue/chat.
7. Se envolver dependência externa, consultar [[Dependencias e Integracoes]] para classe/propriedade e dono pendente.
8. Registrar causa, rota, endpoint, query e dependência afetada no runbook do fluxo.

## Runbooks prioritários

| Fluxo | Por que priorizar |
|---|---|
| [[Operacional/Runbooks/criacao-integracao-contrato]] | Escrita crítica, integração externa, cliente/lead/venda/contrato. |
| [[Operacional/Runbooks/ativacao-servicos]] | Efeito operacional no serviço contratado. |
| [[Operacional/Runbooks/oauth-integracao]] | Autenticação/credencial e remoção de usuário. |
| [[Operacional/Runbooks/analise-credito]] | Crédito, documento e decisão comercial. |
| [[Operacional/Runbooks/consulta-cliente]] | Fluxo de leitura muito usado e com dados sensíveis. |

## Mudanças seguras

- Mudanças em endpoints da collection devem atualizar a collection, regenerar documentação e revisar diferenças.
- Mudanças em queries de SELECT devem atualizar o arquivo SQL, regenerar shape com `LIMIT 0` e revisar impacto em endpoint/fluxo.
- Mudanças em escrita, integração externa ou OAuth devem atualizar runbook e mapa de escrita.
- Não versionar valores de tokens, senhas, URLs privadas com credencial ou payload real de cliente.
- Para produção, preferir documentar metadados e contagem/shape; linhas reais só devem aparecer em ferramenta autorizada e fora do vault.

## Backlog operacional

| Item | Resultado esperado |
|---|---|
| Preencher owner/canais | Escalação objetiva por incidente. |
| Adicionar dashboard principal | Link único para tráfego, erro e latência. |
| Adicionar dashboard por dependência | Ver rapidamente se falha é externa. |
| Criar SLO por fluxo crítico | Definir expectativa de disponibilidade/latência. |
| Gerar contratos de payload | Validar request/response sem depender só da collection. |
| Cruzar logs de uso real | Marcar endpoint usado, pouco usado ou candidato a remoção. |
