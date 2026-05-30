---
tags:
  - trabalho
  - air
  - comercial-api
  - services
---
# Services Criticos - comercial-api

Documentação orientada a classes de service com maior impacto em fluxos comerciais, integrações e reprocessamento.

| Service | Responsabilidade | Documento |
|---|---|---|
| `AnaliseCreditoService` | Consulta e persiste análise financeira/crédito para lead/cliente, incluindo integrações SPC/Serasa. | [[analisecredito-service]] |
| `ClienteService` | Consulta e monta dados de cliente, avisos, contratos, documentos, marcadores, eventos e integração cadastral. | [[cliente-service]] |
| `ContratoService` | Orquestra contrato, ativação, migração, avisos, marca/brand, desconto recorrente, serviços técnicos e integrações associadas. | [[contrato-service]] |
| `OauthIntegracaoService` | Integra, remove e reprocessa clientes no OAuth/Keycloak/eCare por marca/brand. | [[oauthintegracao-service]] |
| `VendaService` | Orquestra venda, criação de contrato, ativação de serviços, confirmação/cancelamento, notificação e integração com origem/Sydle. | [[venda-service]] |
