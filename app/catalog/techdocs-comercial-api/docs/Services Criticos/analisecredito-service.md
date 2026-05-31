# AnaliseCreditoService

- Código: `comercial-api/src/main/java/br/net/air/venda/service/AnaliseCreditoService.java`
- Responsabilidade: Consulta e persiste análise financeira/crédito para lead/cliente, incluindo integrações SPC/Serasa.

## Endpoints relacionados

- [[../Endpoints da Collection/get-cliente-analise-credito]]
- [[../Endpoints da Collection/post-criar-integracao]]

## Tabelas/entidades tocadas

- `tbl_analise_credito`
- `tbl_analise_credito_atributo`
- `tbl_analise_credito_restricao`
- `tbl_lead`

## Métodos de atenção

- `consultarAnaliseFinanceira`
- `findByCliente`
- `findTopByLead`

## Cuidados

- Dado de crédito/documento. Não registrar XML, documento ou resposta real de bureau em docs.
- Revisar [[../Matriz de Impacto]] antes de alterar contrato de método ou comportamento.
- Revisar [[../Mapa de Reprocessamento]] quando a mudança alterar idempotência, status ou efeito externo.
