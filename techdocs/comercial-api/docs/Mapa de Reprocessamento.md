---
tags:
  - trabalho
  - air
  - comercial-api
  - reprocessamento
---
# Mapa de Reprocessamento - comercial-api

Guia para decidir se um fluxo pode ser reexecutado e quais estados verificar antes. Não substitui análise de incidente nem validação em produção.

| Fluxo | Pode reprocessar? | Idempotência | Escritas | Integrações | Risco principal |
|---|---|---|---|---|---|
| [[Fluxos de Negocio/criacao-integracao-contrato|Criação de contrato / integração]] | Com cautela | Correlação por processo de venda Sydle e buscas de cliente/lead/venda reduzem duplicidade, mas integrações externas podem reenviar payload. | `tbl_lead`, `tbl_cliente`, `tbl_endereco`, `tbl_venda`, `tbl_contrato`, `tbl_venda_adicional`, `tbl_venda_origem` | Sydle, Chamado, ConnectMaster | Duplicar venda/contrato, criar OS/chamado em duplicidade ou aplicar regra comercial errada. |
| [[Fluxos de Negocio/oauth-integracao|OAuth / Keycloak]] | Sim, com controle por cliente | POST manual marca cliente como ATUALIZAR; rotinas/integrações processam por status. DELETE remove por brands. | `tbl_cliente` | Keycloak/OAuth, eCare | Reativar/remover usuário indevidamente ou mascarar falha externa como sucesso interno. |
| [[Fluxos de Negocio/ativacao-servicos|Ativação de serviços]] | Somente após checar estado da venda/contrato | A campanha marca recorrenciaDescontoAplicado para evitar reaplicar desconto, mas ativação técnica/notificação podem ter efeitos externos. | `tbl_venda`, `tbl_contrato`, `tbl_contrato_campanha` | Notification, Keycloak/OAuth | Duplicar desconto, notificação ou ativação técnica. |
| [[Fluxos de Negocio/analise-credito|Análise de crédito]] | Com restrição | Depende de consulta externa e persistência de resultado por lead/análise. Reprocessar pode alterar decisão/status. | `tbl_analise_credito`, `tbl_analise_credito_atributo`, `tbl_analise_credito_restricao`, `tbl_lead` | SPC/Serasa | Alterar decisão de crédito, sobrescrever retorno de bureau ou expor dado sensível. |

## Checklists por fluxo

### Criação de contrato / integração

- Fluxo: [[Fluxos de Negocio/criacao-integracao-contrato]]
- Runbook: [[Operacional/Runbooks/criacao-integracao-contrato]]
- Pode reprocessar: Com cautela
- Verificar antes:
  - `idProcessoVendaSydle`
  - `cliente/lead por CPF/CNPJ`
  - `venda por processo Sydle`
  - `contrato gerado`
  - `chamado/OS externa`
- Tabelas/estados de escrita:
  - `tbl_lead`
  - `tbl_cliente`
  - `tbl_endereco`
  - `tbl_venda`
  - `tbl_contrato`
  - `tbl_venda_adicional`
  - `tbl_venda_origem`

### OAuth / Keycloak

- Fluxo: [[Fluxos de Negocio/oauth-integracao]]
- Runbook: [[Operacional/Runbooks/oauth-integracao]]
- Pode reprocessar: Sim, com controle por cliente
- Verificar antes:
  - `id do cliente`
  - `status de integração do cliente`
  - `brands do contrato`
  - `resposta anterior Keycloak/OAuth`
- Tabelas/estados de escrita:
  - `tbl_cliente`

### Ativação de serviços

- Fluxo: [[Fluxos de Negocio/ativacao-servicos]]
- Runbook: [[Operacional/Runbooks/ativacao-servicos]]
- Pode reprocessar: Somente após checar estado da venda/contrato
- Verificar antes:
  - `id da venda`
  - `status/fase da venda`
  - `status do contrato`
  - `campanha vigente`
  - `recorrenciaDescontoAplicado`
  - `notificação enviada`
- Tabelas/estados de escrita:
  - `tbl_venda`
  - `tbl_contrato`
  - `tbl_contrato_campanha`

### Análise de crédito

- Fluxo: [[Fluxos de Negocio/analise-credito]]
- Runbook: [[Operacional/Runbooks/analise-credito]]
- Pode reprocessar: Com restrição
- Verificar antes:
  - `id do cliente/lead`
  - `última análise`
  - `status integração SPC/Serasa`
  - `autorização manual`
  - `restrições existentes`
- Tabelas/estados de escrita:
  - `tbl_analise_credito`
  - `tbl_analise_credito_atributo`
  - `tbl_analise_credito_restricao`
  - `tbl_lead`

## Regras gerais

- Não reprocessar fluxo de escrita apenas porque a chamada HTTP falhou; confirme se houve efeito parcial no banco ou integração externa.
- Para integrações externas, conferir logs da dependência antes de reenviar.
- Para dados sensíveis, não copiar payload real para este vault.
- Se um novo fluxo de escrita entrar na collection, adicionar aqui antes de considerar a documentação completa.
