---
tags:
  - trabalho
  - air
  - comercial-api
  - testes-manuais
---
# Teste Manual - OAuth / Keycloak

## Pré-condições

- Ambiente autorizado para teste.
- Identificadores de cliente/venda/contrato mascarados na anotação.
- Nenhum payload real copiado para Markdown.

## Execução

1. Abrir o fluxo [[../Fluxos de Negocio/oauth-integracao]].
2. Abrir o runbook [[../Operacional/Runbooks/oauth-integracao]].
3. Validar pré-estado nas tabelas/estados abaixo.
4. Executar a request da collection ou chamada segura equivalente.
5. Conferir pós-estado, integração externa e ausência de duplicidade.

## Estados para conferir

- `id do cliente`
- `status de integração do cliente`
- `brands do contrato`
- `resposta anterior Keycloak/OAuth`

## Tabelas/efeitos esperados

- `tbl_cliente`

## Critérios de aceite

- Reprocessamento respeita regra: Sim, com controle por cliente.
- Risco principal validado: Reativar/remover usuário indevidamente ou mascarar falha externa como sucesso interno.
- Nenhum dado real foi colado em issue, commit, print ou Markdown.
