# Blacklist

Gerado em: 2026-05-30 10:11:02

- Objetivo: Consulta bloqueios/blacklist do cliente.
- Risco operacional: `medio`
- Endpoints: 1
- Queries/operações mapeadas: 0
- Tabelas SQL identificadas: 0

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-cliente-blacklist.md](../Endpoints da Collection/get-cliente-blacklist.md) | `GET /cliente/{{id}}/blacklist` | `ClienteController.blacklist` | `-` | `ResponseEntity<?>` |

## Contrato HTTP observado

### `GET /cliente/{{id}}/blacklist`

- Assinatura: `public ResponseEntity<?> blacklist(@PathVariable("id") Long id)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|

## Tabelas tocadas por SQL nativo

- Nenhuma tabela extraida de SQL nativo neste fluxo.

## Efeitos colaterais e integrações

- Nenhuma integração externa forte identificada automaticamente.

## Dados sensíveis

- Nenhum sinal forte identificado automaticamente.

## Pendências de mapeamento

- `BlacklistService.findAll`

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
