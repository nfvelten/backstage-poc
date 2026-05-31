---
tags:
  - trabalho
  - air
  - comercial-api
  - ownership
---
# Ownership por Dominio - comercial-api

Mapa operacional de responsabilidade documental por domínio. Use como ponto de partida para revisão e escalação; não representa organograma formal.

| Domínio | Owner documental sugerido | Docs principais | Quando escalar |
|---|---|---|---|
| `avisos` | Atendimento/Operação | [[Fluxos de Negocio/avisos-cliente-contrato]], [[Integracoes Externas/notification]] | Avisos de rede/telefonia/migração, WhatsApp, URA ou notificação. |
| `cliente` | Comercial/Atendimento | [[Ciclos de Vida/cliente]], [[Contratos de Dados/tbl_cliente]] | Falha de dados cadastrais, contato, endereço, contrato do cliente ou OAuth. |
| `contrato` | Comercial/Operação | [[Ciclos de Vida/contrato]], [[Services Criticos/contrato-service]] | Criação, detalhe, produto, campanha, migração, aviso ou SVA. |
| `credito` | Comercial/Crédito | [[Integracoes Externas/spc-serasa]], [[Services Criticos/analisecredito-service]] | Consulta/restrição de crédito, retorno de bureau ou reanálise. |
| `lead` | Comercial/Vendas | [[Ciclos de Vida/lead]], [[Contratos de Dados/tbl_lead]] | Falha de integração de oportunidade, qualificação ou conversão. |
| `oauth` | Identidade/Integrações | [[Integracoes Externas/oauth-keycloak-ecare]], [[Services Criticos/oauthintegracao-service]] | Acesso do cliente, status de integração, Keycloak/eCare. |
| `svas` | Produtos/Contrato | [[Fluxos de Negocio/contratos-v1-svas]], [[Ciclos de Vida/contrato]] | Serviços de valor agregado e detalhe de contrato v1. |
| `venda` | Comercial/Vendas | [[Ciclos de Vida/venda]], [[Services Criticos/venda-service]] | Fase/status, ativação, adicional, confirmação ou cancelamento. |

## Regra prática

- Se a mudança tocar mais de um domínio, revisar pelo domínio de escrita e pelo domínio de integração externa.
- Se não houver dono formal, registrar o domínio aqui mesmo assim para evitar documentação órfã.
