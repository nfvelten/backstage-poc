---
tags:
  - trabalho
  - air
  - comercial-api
  - testes-manuais
---
# Teste Manual - Ativação de serviços

## Pré-condições

- Ambiente autorizado para teste.
- Identificadores de cliente/venda/contrato mascarados na anotação.
- Nenhum payload real copiado para Markdown.

## Execução

1. Abrir o fluxo [[../Fluxos de Negocio/ativacao-servicos]].
2. Abrir o runbook [[../Operacional/Runbooks/ativacao-servicos]].
3. Validar pré-estado nas tabelas/estados abaixo.
4. Executar a request da collection ou chamada segura equivalente.
5. Conferir pós-estado, integração externa e ausência de duplicidade.

## Estados para conferir

- `id da venda`
- `status/fase da venda`
- `status do contrato`
- `campanha vigente`
- `recorrenciaDescontoAplicado`
- `notificação enviada`

## Tabelas/efeitos esperados

- `tbl_venda`
- `tbl_contrato`
- `tbl_contrato_campanha`

## Critérios de aceite

- Reprocessamento respeita regra: Somente após checar estado da venda/contrato.
- Risco principal validado: Duplicar desconto, notificação ou ativação técnica.
- Nenhum dado real foi colado em issue, commit, print ou Markdown.
