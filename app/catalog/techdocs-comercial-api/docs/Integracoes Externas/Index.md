---
tags:
  - trabalho
  - air
  - comercial-api
  - integracoes
---
# Integracoes Externas - comercial-api

Contratos operacionais das dependências externas e serviços internos chamados pelo comercial. Registra formato lógico e risco, sem valores reais.

| Integração | Finalidade | Fluxos | Documento |
|---|---|---|---|
| Chamado / OS | Criação e consulta de chamados/ordens ligados a venda, contrato e atendimento. | [[../Fluxos de Negocio/criacao-integracao-contrato|criacao-integracao-contrato]], [[../Fluxos de Negocio/avisos-cliente-contrato|avisos-cliente-contrato]] | [[chamado]] |
| ConnectMaster | Integrações e rotina de cancelamento/serviços técnicos. | [[../Fluxos de Negocio/criacao-integracao-contrato|criacao-integracao-contrato]], [[../Fluxos de Negocio/ativacao-servicos|ativacao-servicos]] | [[connectmaster]] |
| Notification API / WhatsApp / URA | Envio de comunicação operacional/comercial e consulta de notificações WhatsApp. | [[../Fluxos de Negocio/notificacoes-whatsapp|notificacoes-whatsapp]], [[../Fluxos de Negocio/ativacao-servicos|ativacao-servicos]], [[../Fluxos de Negocio/avisos-cliente-contrato|avisos-cliente-contrato]] | [[notification]] |
| OAuth / Keycloak / eCare | Criação, remoção e reprocessamento de acesso/autenticação do cliente por marca/brand. | [[../Fluxos de Negocio/oauth-integracao|oauth-integracao]], [[../Fluxos de Negocio/ativacao-servicos|ativacao-servicos]] | [[oauth-keycloak-ecare]] |
| SPC / Serasa | Consulta de crédito/restrição e persistência da análise financeira. | [[../Fluxos de Negocio/analise-credito|analise-credito]] | [[spc-serasa]] |
| Sydle | Origem/integração de processo comercial, criação de contrato, ativação e confiança. | [[../Fluxos de Negocio/criacao-integracao-contrato|criacao-integracao-contrato]], [[../Fluxos de Negocio/ativacao-servicos|ativacao-servicos]] | [[sydle]] |
