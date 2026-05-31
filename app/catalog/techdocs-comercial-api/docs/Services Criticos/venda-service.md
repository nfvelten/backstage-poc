# VendaService

- Código: `comercial-api/src/main/java/br/net/air/venda/service/VendaService.java`
- Responsabilidade: Orquestra venda, criação de contrato, ativação de serviços, confirmação/cancelamento, notificação e integração com origem/Sydle.

## Endpoints relacionados

- [[../Endpoints da Collection/ativar-servicos]]
- [[../Endpoints da Collection/get-vendas-by-natureza]]
- [[../Endpoints da Collection/get-vendas-contrato]]
- [[../Endpoints da Collection/post-criar-integracao]]

## Tabelas/entidades tocadas

- `tbl_venda`
- `tbl_venda_adicional`
- `tbl_venda_origem`
- `tbl_contrato`
- `tbl_lead`

## Métodos de atenção

- `ativarServicos`
- `processarAtivacao`
- `processarCriacaoDeContrato`
- `criarContratoNovoCRMIntegracao`

## Cuidados

- É ponto crítico para idempotência de integração e ativação. Reprocessar sem checar venda/contrato pode duplicar efeitos externos.
- Revisar [[../Matriz de Impacto]] antes de alterar contrato de método ou comportamento.
- Revisar [[../Mapa de Reprocessamento]] quando a mudança alterar idempotência, status ou efeito externo.
