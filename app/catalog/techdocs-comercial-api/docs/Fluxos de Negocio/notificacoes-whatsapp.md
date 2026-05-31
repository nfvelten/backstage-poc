# Notificações WhatsApp

Gerado em: 2026-05-30 10:11:02

- Objetivo: Lista notificações WhatsApp por cliente.
- Risco operacional: `baixo`
- Endpoints: 1
- Queries/operações mapeadas: 0
- Tabelas SQL identificadas: 0

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-wpp-notificacoes-listar.md](../Endpoints da Collection/get-wpp-notificacoes-listar.md) | `GET /wpp-notificacoes/listar/{{customerId}}` | `NotificationController.listar` | `-` | `List<ContatoCompletoDTO>` |

## Contrato HTTP observado

### `GET /wpp-notificacoes/listar/{{customerId}}`

- Assinatura: `public List<ContatoCompletoDTO> listar(@PathVariable("customerId") String customerId)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|

## Tabelas tocadas por SQL nativo

- Nenhuma tabela extraida de SQL nativo neste fluxo.

## Efeitos colaterais e integrações

Integrações/sistemas citados no caminho ou SQL:
- Notification
- WhatsApp

## Dados sensíveis

- Nenhum sinal forte identificado automaticamente.

## Pendências de mapeamento

- Nenhuma chamada pendente neste fluxo.

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
