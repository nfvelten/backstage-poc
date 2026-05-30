# ADR 0008 - Não versionar payload real de integração externa

- Status: Aceita
- Decisão: Contratos externos documentam payload lógico, falhas e campos, mas não payload real.

## Contexto

Integrações carregam PII, credenciais, telefone, documento, crédito e dados operacionais.

## Consequências

- Exemplos devem ser mascarados ou estruturais.
- Retornos de bureau/Keycloak/notification não entram no vault.
- Debug real deve ficar em ferramenta autorizada, com retenção adequada.
