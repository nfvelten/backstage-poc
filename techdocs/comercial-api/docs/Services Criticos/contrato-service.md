# ContratoService

- Código: `comercial-api/src/main/java/br/net/air/cliente/service/ContratoService.java`
- Responsabilidade: Orquestra contrato, ativação, migração, avisos, marca/brand, desconto recorrente, serviços técnicos e integrações associadas.

## Endpoints relacionados

- [[../Endpoints da Collection/get-contrato]]
- [[../Endpoints da Collection/get-cliente-contrato]]
- [[../Endpoints da Collection/get-contrato-aviso]]
- [[../Endpoints da Collection/post-contrato-adicionar-aviso]]
- [[../Endpoints da Collection/post-criar-integracao]]
- [[../Endpoints da Collection/ativar-servicos]]

## Tabelas/entidades tocadas

- `tbl_contrato`
- `tbl_contrato_campanha`
- `tbl_contrato_produto`
- `tbl_contrato_item`
- `tbl_contrato_migracao`
- `tbl_endereco`

## Métodos de atenção

- `salvarDescontoRecorrenteCampanha`
- `ativarServicos`
- `migrar`
- `cadastrarIntegracao`
- `atualizarServicosTecnicos`

## Cuidados

- Mudanças aqui costumam ter efeito em contrato, venda, desconto, ativação e integrações. Revisar mapa de reprocessamento antes de repetir operação.
- Revisar [[../Matriz de Impacto]] antes de alterar contrato de método ou comportamento.
- Revisar [[../Mapa de Reprocessamento]] quando a mudança alterar idempotência, status ou efeito externo.
