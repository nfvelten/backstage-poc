# Vendas e migrações

Gerado em: 2026-05-30 10:11:02

- Objetivo: Consulta vendas de contrato, vendas não confirmadas e migrações de contrato.
- Risco operacional: `medio`
- Endpoints: 3
- Queries/operações mapeadas: 0
- Tabelas SQL identificadas: 0

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-vendas-contrato.md](../Endpoints da Collection/get-vendas-contrato.md) | `GET /contrato/{{id}}/venda` | `ContratoController.vendas` | `-` | `ResponseEntity<?>` |
| [get-vendas-by-natureza.md](../Endpoints da Collection/get-vendas-by-natureza.md) | `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC` | `VendaController.naoConfirmadas` | `Map` | `ResponseEntity<Page<Venda>>` |
| [get-migracoes-contrato.md](../Endpoints da Collection/get-migracoes-contrato.md) | `GET /contrato/{{id}}/migracao` | `ContratoController.migracoes` | `-` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `GET /contrato/{{id}}/venda`

- Assinatura: `public ResponseEntity<?> vendas(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

### `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC`

- Assinatura: `public ResponseEntity<Page<Venda>> naoConfirmadas( @RequestBody Map filtro, @RequestParam(value = "size", defaultValue = "30") int size, @RequestParam(value = "page", defaultValue = "0") int page, @RequestParam(value = "order", defaultValue = "id") String order, @RequestParam(value = "direction", defaultValue = "DESC") String direction)`
- Campos do body Bruno: `natureza`

### `GET /contrato/{{id}}/migracao`

- Assinatura: `public ResponseEntity<?> migracoes(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|

## Tabelas tocadas por SQL nativo

- Nenhuma tabela extraida de SQL nativo neste fluxo.

## Efeitos colaterais e integrações

Endpoints com potencial efeito colateral:
- `PUT /venda/nao_confirmadas?size={{size}}&page={{page}}&order=id&direction=DESC`

- Nenhuma integração externa forte identificada automaticamente.

## Dados sensíveis

- Nenhum sinal forte identificado automaticamente.

## Pendências de mapeamento

- `ContratoMigracaoService.findAll`
- `VendaAdicionalService.findAll`
- `VendaService.findAll`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
