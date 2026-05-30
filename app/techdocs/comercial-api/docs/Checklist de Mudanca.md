---
tags:
  - trabalho
  - air
  - api
  - comercial-api
  - checklist
---
# Checklist de Mudanca - comercial-api

Checklist para PR/release quando uma mudança tocar endpoint, query, fluxo comercial, integração externa ou dado sensível.

## Antes de abrir PR

- [ ] Identifique se a mudança altera endpoint público, payload, query, tabela, integração externa, rotina ou dado sensível.
- [ ] Atualize ou crie request na collection Bruno quando houver rota nova/alterada.
- [ ] Atualize SQL em `air-db-queries` quando a query for relevante para consulta/reuso.
- [ ] Regere a documentação seguindo [[Como Manter Esta Documentacao]].
- [ ] Revise o endpoint em [[Endpoints da Collection/Index]].
- [ ] Revise o fluxo em [[Fluxos de Negocio/Index]].
- [ ] Revise escrita em [[Operacional/Mapa de Escrita]] se houver `POST`, `PUT`, `PATCH`, `DELETE`, `save`, `delete` ou update nativo.
- [ ] Revise dados sensíveis em [[Operacional/Dados Sensiveis]] se houver documento, contato, endereço, credencial ou crédito.
- [ ] Revise dependências em [[Dependencias e Integracoes]] se houver novo host, propriedade, gateway ou client HTTP.

## Perguntas de revisão

| Tema | Pergunta |
|---|---|
| Endpoint | A rota está documentada na collection e no código? |
| Payload | Campos obrigatórios/opcionais mudaram? Existe exemplo sem dado real? |
| Query | A query tem arquivo próprio, contexto e shape de SELECT? |
| Banco | A mudança depende de migration? A migration está documentada? |
| Escrita | O efeito colateral é idempotente? Pode ser reprocessado? |
| Integração | Existe timeout? Existe fallback? Qual sistema é dono da falha? |
| Segurança | Algum campo sensível novo aparece em request, response ou log? |
| Observabilidade | Erro/latência podem ser vistos por endpoint e por dependência? |
| Operação | O runbook do fluxo explica como diagnosticar a falha? |
| Compatibilidade | Algum consumidor antigo quebra com a mudança? |

## Critérios para bloquear merge

- Endpoint novo sem collection ou sem contexto mínimo.
- Query relevante sem arquivo versionado ou sem shape quando for SELECT.
- Escrita crítica sem atualização do mapa de escrita/runbook.
- Integração externa nova sem classe/propriedade documentada.
- Campo sensível novo sem registro em dados sensíveis.
- Uso de valor real de produção em documentação, teste, payload exemplo ou commit.

## Depois do deploy

- [ ] Validar health/actuator.
- [ ] Verificar taxa de erro da rota alterada.
- [ ] Verificar latência da rota e das queries envolvidas.
- [ ] Verificar logs da integração externa, se aplicável.
- [ ] Atualizar runbook se o comportamento observado diferir do documentado.
- [ ] Se houver tráfego real relevante, marcar endpoint como usado/alto uso na próxima revisão de telemetria.
