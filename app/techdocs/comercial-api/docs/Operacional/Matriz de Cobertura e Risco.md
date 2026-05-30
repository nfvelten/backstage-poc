# Matriz de Cobertura e Risco - comercial-api

Gerado em: 2026-05-30 10:20:55

| Fluxo | Risco | Endpoints | Queries/operações | Escrita | Sensível | Integrações | Pendências |
|---|---|---:|---:|---|---|---|---:|
| [Análise de crédito](../Fluxos%20de%20Negocio/analise-credito.md) | `alto` | 1 | 5 | não | credito, documento, pessoa | - | 0 |
| [Ativação de serviços](../Fluxos%20de%20Negocio/ativacao-servicos.md) | `alto` | 1 | 3 | não | credencial, documento | Keycloak/OAuth, Notification | 1 |
| [Avisos de cliente e contrato](../Fluxos%20de%20Negocio/avisos-cliente-contrato.md) | `medio` | 3 | 13 | sim | documento | Internet, Telefonia | 2 |
| [Blacklist](../Fluxos%20de%20Negocio/blacklist.md) | `medio` | 1 | 0 | não | documento | - | 1 |
| [Consulta de cliente](../Fluxos%20de%20Negocio/consulta-cliente.md) | `medio` | 5 | 17 | não | contato, documento, endereco, pessoa | Chamado, Internet, Telefonia | 2 |
| [Contratos V1 e SVAs](../Fluxos%20de%20Negocio/contratos-v1-svas.md) | `medio` | 4 | 2 | não | documento, pessoa | Sydle | 0 |
| [Criação de contrato / integração](../Fluxos%20de%20Negocio/criacao-integracao-contrato.md) | `alto` | 2 | 10 | sim | contato, documento, endereco, pessoa | Chamado, ConnectMaster, Sydle | 2 |
| [Notificações WhatsApp](../Fluxos%20de%20Negocio/notificacoes-whatsapp.md) | `baixo` | 1 | 0 | não | contato, documento | Notification, WhatsApp | 0 |
| [OAuth / Keycloak](../Fluxos%20de%20Negocio/oauth-integracao.md) | `alto` | 2 | 3 | sim | credencial, documento, pessoa | Keycloak/OAuth | 2 |
| [Vendas e migrações](../Fluxos%20de%20Negocio/vendas-e-migracoes.md) | `medio` | 3 | 0 | não | documento | - | 3 |

## Leitura

- `alto`: fluxo com escrita crítica, dados sensíveis fortes, crédito/autenticação ou integração externa relevante.
- `pendências`: chamadas ainda não resolvidas automaticamente no call graph.
