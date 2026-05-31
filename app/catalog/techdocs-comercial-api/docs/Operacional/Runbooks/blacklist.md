# Runbook - Blacklist

- Risco: `medio`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/blacklist.md)
- Endpoints: 1
- Queries/operações: 0

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/get-cliente-blacklist](../../Endpoints%20da%20Collection/get-cliente-blacklist.md)

Pendências de mapeamento que podem exigir leitura manual:
- `BlacklistService.findAll`

## Cuidados antes de reprocessar

- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
