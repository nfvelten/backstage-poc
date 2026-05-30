# Runbook - Criação de contrato / integração

- Risco: `alto`
- Fluxo: [documentação](../../Fluxos%20de%20Negocio/criacao-integracao-contrato.md)
- Endpoints: 2
- Queries/operações: 10

## Checklist inicial

1. Confirmar endpoint/rota e parâmetros usados na chamada.
2. Conferir se houve alteração recente no controller/service/repository do caminho.
3. Verificar se a falha envolve dados sensíveis antes de copiar payload/log.
4. Consultar queries SQL e shape de retorno vinculados ao endpoint.
5. Se houver integração externa, checar logs da integração antes de reprocessar.

## Onde olhar

- Endpoint: [/post-criar-integracao](../../Endpoints%20da%20Collection/post-criar-integracao.md)
- Endpoint: [/test-criar-integracao](../../Endpoints%20da%20Collection/test-criar-integracao.md)

Queries/operações principais:
- `ClienteFisicoRepository.findTopByCpf` (`repository-derived-query`)
- `ClienteJuridicoRepository.findTopByCnpj` (`repository-derived-query`)
- `ContratoCampanhaRepository.findTopByContratoAndCanceladaIsFalseOrderByIdDesc` (`repository-derived-query`)
- `EnderecoCidadeRepository.findCidadeBySigla` (`repository-native-query`)
- `VendaAdicionalRepository.save` (`repository-crud-operation`)
- `VendaOrigemRepository.save` (`repository-crud-operation`)
- `VendaRepository.buscarVendaNoAIR` (`repository-native-query`)
- `VendaRepository.findTopByIdProcessoVendaSydle` (`repository-derived-query`)
- `VendedorRepository.findAllByIdVendedorSydle` (`repository-derived-query`)
- `VendedorRepository.findTopByUsuarioStartingWithAndAtivoIsTrue` (`repository-derived-query`)

Integrações prováveis:
- Chamado
- ConnectMaster
- Sydle

Pendências de mapeamento que podem exigir leitura manual:
- `LeadService.save`
- `RegraSuspensaoService.findOne`

## Cuidados antes de reprocessar

- Fluxo de alto risco: validar cliente/contrato/venda em banco antes de repetir chamada.
- Não usar payload real em documentação ou chat sem mascarar campos sensíveis.
- Para endpoints `POST`, `PUT` ou `DELETE`, confirmar idempotência no service antes de repetir.
