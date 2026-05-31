# Runbook - Ativação de serviços

- Risco: `alto`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/ativacao-servicos.md)
- Endpoints: 1
- Queries/operações: 3

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/ativar-servicos](../../Endpoints%20da%20Collection/ativar-servicos.md)

Queries/operações principais:
- `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` (`repository-derived-query`)
- `VendaOrigemRepository.findTopByVenda` (`repository-derived-query`)
- `sql.customer-brands` (`native-properties`)

Integrações prováveis:
- Keycloak/OAuth
- Notification

Pendências de mapeamento que podem exigir leitura manual:
- `ContratoCampanhaService.save`

## Cuidados antes de reprocessar

- Fluxo de alto risco: validar cliente/contrato/venda em banco antes de repetir chamada.
- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
