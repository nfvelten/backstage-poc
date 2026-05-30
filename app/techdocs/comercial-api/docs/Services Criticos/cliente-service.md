# ClienteService

- Código: `comercial-api/src/main/java/br/net/air/cliente/service/ClienteService.java`
- Responsabilidade: Consulta e monta dados de cliente, avisos, contratos, documentos, marcadores, eventos e integração cadastral.

## Endpoints relacionados

- [[../Endpoints da Collection/get-cliente-por-id]]
- [[../Endpoints da Collection/get-cliente-por-cpf]]
- [[../Endpoints da Collection/get-cliente-consultar-avisos]]
- [[../Endpoints da Collection/get-cliente-contrato]]
- [[../Endpoints da Collection/post-oauth-integrar]]

## Tabelas/entidades tocadas

- `tbl_cliente`
- `tbl_cliente_fisico`
- `tbl_cliente_juridico`
- `tbl_endereco`
- `tbl_contrato`

## Métodos de atenção

- `findAll`
- `buildAvisos`
- `alterarMarcador`
- `save`

## Cuidados

- Concentra dados sensíveis de pessoa, contato, documento e endereço. Evitar expor payload real em documentação ou logs.
- Revisar [[../Matriz de Impacto]] antes de alterar contrato de método ou comportamento.
- Revisar [[../Mapa de Reprocessamento]] quando a mudança alterar idempotência, status ou efeito externo.
