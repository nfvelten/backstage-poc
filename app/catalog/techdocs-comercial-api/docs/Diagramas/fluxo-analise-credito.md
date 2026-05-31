# Diagrama - fluxo de análise de crédito

```mermaid
sequenceDiagram
    participant Consumer as Consumidor
    participant API as comercial-api
    participant Controller as AnaliseCreditoController/ClienteController
    participant Service as AnaliseCreditoService
    participant Repo as Repositories
    participant DB as air_comercial
    participant SPC as SPC/Serasa

    Consumer->>API: GET /cliente/{id}/analise_credito
    API->>Controller: resolver rota
    Controller->>Service: consultar análise por cliente/lead
    Service->>Repo: buscar lead e análises
    Repo->>DB: tbl_lead / tbl_analise_credito / atributos / restrições
    alt precisa consulta externa
        Service->>SPC: consultar documento/restrição
        SPC-->>Service: status/score/restrições
        Service->>DB: persistir resultado/status
    end
    Service-->>Controller: DTO/resultado
    Controller-->>API: response
    API-->>Consumer: análise de crédito
```

## Pontos de atenção

- Fluxo de risco alto por documento, crédito e possível XML de retorno.
- O shape de SELECT é largo e contém campos sensíveis.
- Não usar payload real de cliente em documentação, issue ou teste versionado.

## Referências

- [[../Fluxos de Negocio/analise-credito]]
- [[../Operacional/Runbooks/analise-credito]]
- [[../Endpoints da Collection/get-cliente-analise-credito]]
- [[../Contratos de Dados/tbl_analise_credito]]
- [[../Resultados SELECT/analisecreditorepository-findallbyleadclienteid]]
