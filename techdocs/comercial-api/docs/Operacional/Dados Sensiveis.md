# Dados Sensiveis - comercial-api

Gerado em: 2026-05-30 10:20:55

Sinais de dados sensíveis encontrados em body Bruno, nomes de colunas, queries e caminhos de chamada.

## Por fluxo

| Fluxo | Categorias | Integrações |
|---|---|---|
| [Análise de crédito](../Fluxos%20de%20Negocio/analise-credito.md) | credito, documento, pessoa | - |
| [Ativação de serviços](../Fluxos%20de%20Negocio/ativacao-servicos.md) | credencial, documento | Keycloak/OAuth, Notification |
| [Avisos de cliente e contrato](../Fluxos%20de%20Negocio/avisos-cliente-contrato.md) | documento | Internet, Telefonia |
| [Blacklist](../Fluxos%20de%20Negocio/blacklist.md) | documento | - |
| [Consulta de cliente](../Fluxos%20de%20Negocio/consulta-cliente.md) | contato, documento, endereco, pessoa | Chamado, Internet, Telefonia |
| [Contratos V1 e SVAs](../Fluxos%20de%20Negocio/contratos-v1-svas.md) | documento, pessoa | Sydle |
| [Criação de contrato / integração](../Fluxos%20de%20Negocio/criacao-integracao-contrato.md) | contato, documento, endereco, pessoa | Chamado, ConnectMaster, Sydle |
| [Notificações WhatsApp](../Fluxos%20de%20Negocio/notificacoes-whatsapp.md) | contato, documento | Notification, WhatsApp |
| [OAuth / Keycloak](../Fluxos%20de%20Negocio/oauth-integracao.md) | credencial, documento, pessoa | Keycloak/OAuth |
| [Vendas e migrações](../Fluxos%20de%20Negocio/vendas-e-migracoes.md) | documento | - |

## Por endpoint

| Endpoint | Rota | Campos sensíveis no body/queries |
|---|---|---|
| [ativar-servicos](../Endpoints%20da%20Collection/ativar-servicos.md) | `PUT /venda/{{id_venda}}/ativar_servicos` | `credencial` |
| [delete-oauth-remover](../Endpoints%20da%20Collection/delete-oauth-remover.md) | `DELETE /oauth/remover/{{id}}` | `credencial`, `documento` |
| [get-cliente-analise-credito](../Endpoints%20da%20Collection/get-cliente-analise-credito.md) | `GET /cliente/{{id}}/analise_credito` | `credito` |
| [get-cliente-endereco](../Endpoints%20da%20Collection/get-cliente-endereco.md) | `GET /cliente/{{id}}/endereco` | `endereco` |
| [post-criar-integracao](../Endpoints%20da%20Collection/post-criar-integracao.md) | `POST /contrato/criar-integracao` | `documento`, `endereco` |
| [test-criar-integracao](../Endpoints%20da%20Collection/test-criar-integracao.md) | `POST /contrato/criar-integracao` | `documento`, `endereco` |

## Política prática

- Não incluir exemplos reais de produção para campos listados aqui.
- Mascarar CPF/CNPJ, telefone, email, endereço e campos de crédito em logs compartilhados.
- Tratar `senha_sac`, tokens e XML de bureaus como sensíveis mesmo quando aparecem apenas em shape de SELECT.
