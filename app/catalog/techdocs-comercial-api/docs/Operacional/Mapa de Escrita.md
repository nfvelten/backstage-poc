# Mapa de Escrita - comercial-api

Gerado em: 2026-05-30 10:20:55

Lista fluxos/endpoints com provável efeito colateral. Operações derivadas de análise estática.

## Avisos de cliente e contrato

- Risco: `medio`
- Endpoints com verbo de escrita: `post-contrato-adicionar-aviso`

## Criação de contrato / integração

- Risco: `alto`
- Endpoints com verbo de escrita: `post-criar-integracao`

| Operação | Tipo | Caminho | Tabelas SQL associadas |
|---|---|---|---|
| `VendaAdicionalRepository.save` | `repository-crud-operation` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaAdicionalRepository.save` | - |
| `VendaOrigemRepository.save` | `repository-crud-operation` | `ContratoController.criarContrato -> ContratoService.cadastrarIntegracao -> VendaService.processarCriacaoDeContrato -> VendaService.criarContratoNovoCRMIntegracao -> VendaOrigemRepository.save` | - |

## OAuth / Keycloak

- Risco: `alto`
- Endpoints com verbo de escrita: `post-oauth-integrar`, `delete-oauth-remover`

## Cuidados

- Validar idempotência antes de reprocessar chamadas.
- Evitar executar endpoints de escrita em produção sem identificar venda/contrato/cliente alvo.
- Para `save` derivado de repository, a tabela exata depende do mapping JPA da entidade.
