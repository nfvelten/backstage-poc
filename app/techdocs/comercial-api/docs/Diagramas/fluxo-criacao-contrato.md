# Diagrama - fluxo de criação de contrato / integração

```mermaid
sequenceDiagram
    participant Consumer as Consumidor/CRM/Sydle
    participant API as comercial-api
    participant Integracao as IntegracaoService
    participant Cliente as Cliente/Endereco Services
    participant Venda as Venda/Contrato Services
    participant DB as air_comercial
    participant Ext as Sydle/Chamado/ConnectMaster

    Consumer->>API: POST /contrato/criar-integracao
    API->>Integracao: validar e orquestrar payload
    Integracao->>Cliente: localizar/criar cliente
    Cliente->>DB: tbl_cliente / tbl_endereco
    Integracao->>Venda: criar lead/venda/contrato
    Venda->>DB: tbl_lead / tbl_venda / tbl_contrato
    Venda->>Ext: acionar integrações quando aplicável
    Ext-->>Venda: retorno/correlação externa
    Venda-->>Integracao: resultado da criação
    Integracao-->>API: DTO de resposta
    API-->>Consumer: sucesso/erro funcional
```

## Pontos de atenção

- Fluxo de risco alto.
- Escreve cliente, endereço, lead, venda e contrato.
- Pode acionar integrações externas.
- Deve ser tolerante a duplicidade/correlação externa quando possível.

## Referências

- [[../Fluxos de Negocio/criacao-integracao-contrato]]
- [[../Operacional/Runbooks/criacao-integracao-contrato]]
- [[../Endpoints da Collection/post-criar-integracao]]
- [[../Contratos de Dados/tbl_cliente]]
- [[../Contratos de Dados/tbl_contrato]]
- [[../Contratos de Dados/tbl_venda]]
