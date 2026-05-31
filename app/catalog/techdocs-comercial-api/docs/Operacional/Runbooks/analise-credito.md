# Runbook - Análise de crédito

- Risco: `alto`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/analise-credito.md)
- Endpoints: 1
- Queries/operações: 5

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/get-cliente-analise-credito](../../Endpoints%20da%20Collection/get-cliente-analise-credito.md)

Queries/operações principais:
- `AnaliseCreditoAtributoRepository.findAllByAnaliseCredito_id` (`repository-native-query`)
- `AnaliseCreditoRepository.findAllByLeadClienteId` (`repository-native-query`)
- `AnaliseCreditoRestricaoRepository.findAllByAnaliseCredito_id` (`repository-native-query`)
- `CarteiraRepository.findCarteiraById` (`repository-native-query`)
- `ClienteRepository.findClienteById` (`repository-native-query`)

## Cuidados antes de reprocessar

- Fluxo de alto risco: validar cliente/contrato/venda em banco antes de repetir chamada.
- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
