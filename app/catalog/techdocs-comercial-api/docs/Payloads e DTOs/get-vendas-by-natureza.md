# Payload - get-vendas-by-natureza

- Rota: `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC`
- Collection: `air-api-collection/comercial/get-vendas-by-natureza.bru`
- Auth na collection: `none`
- Headers documentados: `token`, `Accept`, `Content-Type`

## Contexto da collection

Lista vendas filtrando por natureza.
  Naturezas disponíveis: VN_NOVO_CONTRATO, VN_MIGRACAO_UP, VN_MIGRACAO_DOWN,
  VN_MIGRACAO_COMPULSORIA, VN_ADICIONAL, VN_TROCA_TITULARIDADE.

  Nota: o filtro por natureza via body pode não funcionar dependendo do endpoint.
  Endpoint força faseAtual=FASE_CONFIRMADA server-side.

## Campos do body

| Campo | Tipo inferido | Sensibilidade |
|---|---|---|
| `natureza` | `string` | - |

## Observacoes

- Tipos inferidos a partir do exemplo da collection, nao de validacao runtime.
- Valores da collection nao sao reproduzidos aqui; somente estrutura/campos.
- Campos marcados como sensiveis exigem cuidado em logs, exemplos, prints e issues.
