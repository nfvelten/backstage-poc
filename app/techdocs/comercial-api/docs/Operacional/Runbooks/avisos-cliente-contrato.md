# Runbook - Avisos de cliente e contrato

- Risco: `medio`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/avisos-cliente-contrato.md)
- Endpoints: 3
- Queries/operações: 13

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/get-cliente-consultar-avisos](../../Endpoints%20da%20Collection/get-cliente-consultar-avisos.md)
- Endpoint: [/get-contrato-aviso](../../Endpoints%20da%20Collection/get-contrato-aviso.md)
- Endpoint: [/post-contrato-adicionar-aviso](../../Endpoints%20da%20Collection/post-contrato-adicionar-aviso.md)

Queries/operações principais:
- `ClienteRepository.findClienteResumoAvisoById` (`repository-jpql-query`)
- `ContratoRepository.findAllIdByClienteId` (`repository-jpql-query`)
- `sql.aviso-telefonia` (`native-properties`)
- `sql.aviso.rede.backbone` (`native-properties`)
- `sql.aviso.rede.manual` (`native-properties`)
- `sql.aviso.rede.monitorado` (`native-properties`)
- `sql.aviso.rede.nao-monitorado` (`native-properties`)
- `sql.contratoAvisoMigracao` (`native-properties`)
- `sql.contratoAvisoMigracaoCompulsoria` (`native-properties`)
- `sql.pacotesByClienteId` (`native-properties`)
- `sql.verifica.cliente-monitorado` (`native-properties`)
- `ContratoAvisoOnuRepository.findOneByIdContrato` (`repository-derived-query`)

Integrações prováveis:
- Internet
- Telefonia

Pendências de mapeamento que podem exigir leitura manual:
- `MySqlRepository.carregar`
- `MySqlRepository.consultar`

## Cuidados antes de reprocessar

- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
