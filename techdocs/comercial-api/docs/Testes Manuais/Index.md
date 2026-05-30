---
tags:
  - trabalho
  - air
  - comercial-api
  - testes-manuais
---
# Testes Manuais - comercial-api

Roteiros seguros para validar fluxo sem registrar dados reais no vault. Use IDs mascarados e execute somente em ambiente autorizado.

| Fluxo | Documento | Validação principal |
|---|---|---|
| Criação de contrato / integração | [[criacao-integracao-contrato]] | Conferir efeitos em tbl_lead, tbl_cliente, tbl_endereco |
| OAuth / Keycloak | [[oauth-integracao]] | Conferir efeitos em tbl_cliente |
| Ativação de serviços | [[ativacao-servicos]] | Conferir efeitos em tbl_venda, tbl_contrato, tbl_contrato_campanha |
| Análise de crédito | [[analise-credito]] | Conferir efeitos em tbl_analise_credito, tbl_analise_credito_atributo, tbl_analise_credito_restricao |
