# ADR 0004 - Usar collection recente como contrato operacional documentado

- Status: Aceita
- Decisão: A collection Bruno recente é tratada como recorte de endpoints usados/documentados, enquanto uso real continua dependendo de telemetria.

## Contexto

A `comercial-api` tem muitas rotas históricas. Documentar tudo de uma vez gera ruído; a collection concentra o recorte operacional atual.

## Consequências

- Endpoints fora da collection podem existir e seguir usados.
- Remoção exige validação externa de uso real.
- Mudanças na collection devem disparar regeneração documental.
