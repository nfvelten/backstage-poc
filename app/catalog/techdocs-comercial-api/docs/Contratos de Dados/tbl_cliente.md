# tbl_cliente

Tabela raiz do cliente comercial. Concentra identidade interna, status de integração, carteira, credenciais indiretas e vínculos OAuth.

## Resumo

| Item | Valor |
|---|---|
| Domínio | Cliente |
| Origem schema | [[../Banco - air_comercial]] |
| Classe provável | `cliente/model/Cliente.java` |
| Repository provável | `ClienteRepository` |
| Dados sensíveis | Nome, senha SAC, vínculos OAuth, integração, possível identificação indireta |
| Fluxos principais | [[../Fluxos de Negocio/consulta-cliente]], [[../Fluxos de Negocio/criacao-integracao-contrato]], [[../Fluxos de Negocio/analise-credito]], [[../Fluxos de Negocio/oauth-integracao]] |

## Campos principais

| Campo | Tipo | Papel |
|---|---|---|
| `id` | `bigint` | Identificador interno. |
| `excluido` | `tinyint` | Exclusão lógica/filtro operacional. |
| `id_carteira` | `bigint` | Relação com carteira/vendedor. |
| `tipo` | `varchar(20)` | Pessoa física/jurídica ou categoria de cliente. |
| `nome` | `varchar(100)` | Nome principal do cliente. |
| `codigo` | `varchar(20)` | Código único do cliente. |
| `senha_sac` | `varchar(20)` | Campo sensível usado por SAC/integrações; não expor em docs/logs. |
| `integracao_status` | `varchar(20)` | Estado de integração legado/principal. |
| `integracao_codigo` | `varchar(255)` | Código externo de integração. |
| `integracao_transacao` | `varchar(255)` | Transação externa de integração. |
| `integracao_status_sydle` | `varchar(20)` | Estado de integração Sydle. |
| `id_oauth*` | `varchar(255)` | Identificadores OAuth por marca/canal. |
| `cupom` | `varchar(50)` | Cupom associado ao cliente. |
| `nome_social` | `varchar(100)` | Nome social. |

## Índices e relações

| Tipo | Campos |
|---|---|
| PK | `id` |
| Único | `codigo` |
| Índices relevantes | `nome`, `id_carteira`, `integracao_codigo`, `integracao_transacao`, `senha_sac`, `legado_id`, `excluido + integracao_status`, `cupom` |
| FK | `id_carteira -> tbl_carteira.id` |

## Endpoints e queries relacionadas

| Uso | Referência |
|---|---|
| Consulta por ID/CPF e dados básicos | [[../Endpoints da Collection/get-cliente-por-id]], [[../Endpoints da Collection/get-cliente-por-cpf]], [[../Endpoints da Collection/get-contracts-customer-basic-info]] |
| Contrato, contato e endereço do cliente | [[../Endpoints da Collection/get-cliente-contrato]], [[../Endpoints da Collection/get-cliente-contato]], [[../Endpoints da Collection/get-cliente-endereco]] |
| Query nativa de cliente | [[../Resultados SELECT/clienterepository-findclientebyid]] |
| Query agregada por endpoint | [[../Queries por Endpoint da Collection]] |

## Cuidados de mudança

- Não retornar `senha_sac` em response nova sem justificativa explícita e tratamento de segurança.
- Mudanças em OAuth exigem revisar [[../Fluxos de Negocio/oauth-integracao]].
- Mudanças em `integracao_*` exigem revisar fluxos Sydle/CRM e reprocessamento.
- Mudanças em índices de `excluido`/`integracao_status` podem afetar rotinas e consultas operacionais.
