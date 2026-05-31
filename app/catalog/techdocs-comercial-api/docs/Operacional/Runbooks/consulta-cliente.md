# Runbook - Consulta de cliente

- Risco: `medio`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/consulta-cliente.md)
- Endpoints: 5
- Queries/operações: 17

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/get-cliente-por-id](../../Endpoints%20da%20Collection/get-cliente-por-id.md)
- Endpoint: [/get-cliente-por-cpf](../../Endpoints%20da%20Collection/get-cliente-por-cpf.md)
- Endpoint: [/get-cliente-contrato](../../Endpoints%20da%20Collection/get-cliente-contrato.md)
- Endpoint: [/get-cliente-contato](../../Endpoints%20da%20Collection/get-cliente-contato.md)
- Endpoint: [/get-cliente-endereco](../../Endpoints%20da%20Collection/get-cliente-endereco.md)

Queries/operações principais:
- `ContratoRepository.findAllByCliente` (`repository-derived-query`)
- `sql.aviso-telefonia` (`native-properties`)
- `sql.aviso.rede.backbone` (`native-properties`)
- `sql.aviso.rede.manual` (`native-properties`)
- `sql.aviso.rede.monitorado` (`native-properties`)
- `sql.aviso.rede.nao-monitorado` (`native-properties`)
- `sql.contratoAvisoMigracao` (`native-properties`)
- `sql.contratoAvisoMigracaoCompulsoria` (`native-properties`)
- `sql.pacotesByClienteId` (`native-properties`)
- `sql.verifica.cliente-monitorado` (`native-properties`)
- `sql.buscarClienteContrato` (`native-properties`)
- `sql.buscarClienteOSProtocoloUra` (`native-properties`)

Integrações prováveis:
- Chamado
- Internet
- Telefonia

Pendências de mapeamento que podem exigir leitura manual:
- `ContratoService.findAll`
- `MySqlRepository.consultarMap`

## Cuidados antes de reprocessar

- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
