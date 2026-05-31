---
tags:
  - trabalho
  - air
  - comercial-api
  - testes-manuais
---
# Teste Manual - Criação de contrato / integração

## Pré-condições

- Ambiente autorizado para teste.
- Identificadores de cliente/venda/contrato mascarados na anotação.
- Nenhum payload real copiado para Markdown.

## Execução

1. Abrir o fluxo [[../Fluxos de Negocio/criacao-integracao-contrato]].
2. Abrir o runbook [[../Operacional/Runbooks/criacao-integracao-contrato]].
3. Validar pré-estado nas tabelas/estados abaixo.
4. Executar a request da collection ou chamada segura equivalente.
5. Conferir pós-estado, integração externa e ausência de duplicidade.

## Estados para conferir

- `idProcessoVendaSydle`
- `cliente/lead por CPF/CNPJ`
- `venda por processo Sydle`
- `contrato gerado`
- `chamado/OS externa`

## Tabelas/efeitos esperados

- `tbl_lead`
- `tbl_cliente`
- `tbl_endereco`
- `tbl_venda`
- `tbl_contrato`
- `tbl_venda_adicional`
- `tbl_venda_origem`

## Critérios de aceite

- Reprocessamento respeita regra: Com cautela.
- Risco principal validado: Duplicar venda/contrato, criar OS/chamado em duplicidade ou aplicar regra comercial errada.
- Nenhum dado real foi colado em issue, commit, print ou Markdown.
