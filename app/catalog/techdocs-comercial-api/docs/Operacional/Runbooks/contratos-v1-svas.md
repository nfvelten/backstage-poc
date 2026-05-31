# Runbook - Contratos V1 e SVAs

- Risco: `medio`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/contratos-v1-svas.md)
- Endpoints: 4
- Queries/operações: 2

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/get-contracts-detail](../../Endpoints%20da%20Collection/get-contracts-detail.md)
- Endpoint: [/get-contracts-customer-basic-info](../../Endpoints%20da%20Collection/get-contracts-customer-basic-info.md)
- Endpoint: [/get-contrato-svas-v1](../../Endpoints%20da%20Collection/get-contrato-svas-v1.md)
- Endpoint: [/get-elegibilidade-confianca](../../Endpoints%20da%20Collection/get-elegibilidade-confianca.md)

Queries/operações principais:
- `ContratoRepository.findContractProductsAndItems` (`repository-jpql-query`)
- `ContratoRepository.findPacoteById` (`repository-jpql-query`)

Integrações prováveis:
- Sydle

## Cuidados antes de reprocessar

- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
