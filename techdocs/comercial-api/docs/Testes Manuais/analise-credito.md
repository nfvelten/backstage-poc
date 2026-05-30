---
tags:
  - trabalho
  - air
  - comercial-api
  - testes-manuais
---
# Teste Manual - Análise de crédito

## Pré-condições

- Ambiente autorizado para teste.
- Identificadores de cliente/venda/contrato mascarados na anotação.
- Nenhum payload real copiado para Markdown.

## Execução

1. Abrir o fluxo [[../Fluxos de Negocio/analise-credito]].
2. Abrir o runbook [[../Operacional/Runbooks/analise-credito]].
3. Validar pré-estado nas tabelas/estados abaixo.
4. Executar a request da collection ou chamada segura equivalente.
5. Conferir pós-estado, integração externa e ausência de duplicidade.

## Estados para conferir

- `id do cliente/lead`
- `última análise`
- `status integração SPC/Serasa`
- `autorização manual`
- `restrições existentes`

## Tabelas/efeitos esperados

- `tbl_analise_credito`
- `tbl_analise_credito_atributo`
- `tbl_analise_credito_restricao`
- `tbl_lead`

## Critérios de aceite

- Reprocessamento respeita regra: Com restrição.
- Risco principal validado: Alterar decisão de crédito, sobrescrever retorno de bureau ou expor dado sensível.
- Nenhum dado real foi colado em issue, commit, print ou Markdown.
