# Operacional - comercial-api

Gerado em: 2026-05-30 10:20:55

Camada voltada a manutenção, diagnóstico, risco, dados sensíveis e performance inicial.

## Artefatos

| Documento | Conteudo |
|---|---|
| [Matriz de Cobertura e Risco](Matriz%20de%20Cobertura%20e%20Risco.md) | Cobertura por fluxo, risco, pendências e sinais operacionais. |
| [Mapa de Escrita](Mapa%20de%20Escrita.md) | Endpoints com efeito colateral, operações CRUD e tabelas impactadas. |
| [Dados Sensiveis](Dados%20Sensiveis.md) | Campos e fluxos com sinais de PII, credenciais ou crédito. |
| [Performance Queries](Performance%20Queries.md) | Joins, tabelas, filtros e largura de resultado dos SELECTs. |
| [Runbooks](Runbooks/Index.md) | Diagnóstico prático por fluxo crítico. |

## Fluxos

| Fluxo | Risco | Endpoints | Queries/operações | Pendências |
|---|---|---:|---:|---:|
| [Análise de crédito](../Fluxos%20de%20Negocio/analise-credito.md) | `alto` | 1 | 5 | 0 |
| [Ativação de serviços](../Fluxos%20de%20Negocio/ativacao-servicos.md) | `alto` | 1 | 3 | 1 |
| [Avisos de cliente e contrato](../Fluxos%20de%20Negocio/avisos-cliente-contrato.md) | `medio` | 3 | 13 | 2 |
| [Blacklist](../Fluxos%20de%20Negocio/blacklist.md) | `medio` | 1 | 0 | 1 |
| [Consulta de cliente](../Fluxos%20de%20Negocio/consulta-cliente.md) | `medio` | 5 | 17 | 2 |
| [Contratos V1 e SVAs](../Fluxos%20de%20Negocio/contratos-v1-svas.md) | `medio` | 4 | 2 | 0 |
| [Criação de contrato / integração](../Fluxos%20de%20Negocio/criacao-integracao-contrato.md) | `alto` | 2 | 10 | 2 |
| [Notificações WhatsApp](../Fluxos%20de%20Negocio/notificacoes-whatsapp.md) | `baixo` | 1 | 0 | 0 |
| [OAuth / Keycloak](../Fluxos%20de%20Negocio/oauth-integracao.md) | `alto` | 2 | 3 | 2 |
| [Vendas e migrações](../Fluxos%20de%20Negocio/vendas-e-migracoes.md) | `medio` | 3 | 0 | 3 |
