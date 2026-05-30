# Payload - post-contrato-adicionar-aviso

- Rota: `POST /contrato/{{id}}/adicionar_aviso`
- Collection: `air-api-collection/comercial/post-contrato-adicionar-aviso.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Rota do painel Top Rotas com Sucesso: /contrato/{id}/adicionar_aviso (5.658 sucessos no print).

  Codigo: ContratoAvisoController.adicionarAviso -> ContratoAvisoOnuService.criar.
  Uso: cria ou atualiza aviso ONU para um contrato.
  Cuidado: endpoint tem efeito de escrita. Validar contrato, dados de ONU e ambiente antes de executar.

## Campos do body

| Campo | Tipo inferido | Sensibilidade |
|---|---|---|
| `problemId` | `string/template` | - |
| `descricao` | `string/template` | - |
| `id` | `string/template` | - |
| `onu` | `object` | - |
| `onu.olt` | `string/template` | - |
| `onu.slot` | `string/template` | - |
| `onu.pon` | `string/template` | - |
| `onu.index` | `string/template` | - |
| `onu.serial` | `string/template` | - |
| `onu.descricao` | `string/template` | - |
| `onu.rx_power` | `string/template` | - |

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
