# OauthIntegracaoService

- Código: `comercial-api/src/main/java/br/net/air/oauth/service/OauthIntegracaoService.java`
- Responsabilidade: Integra, remove e reprocessa clientes no OAuth/Keycloak/eCare por marca/brand.

## Endpoints relacionados

- [[../Endpoints da Collection/post-oauth-integrar]]
- [[../Endpoints da Collection/delete-oauth-remover]]
- [[../Endpoints da Collection/ativar-servicos]]

## Tabelas/entidades tocadas

- `tbl_cliente`
- `tbl_contrato`
- `air_base.tbl_unidade`

## Métodos de atenção

- `integrarManual`
- `removerClientePorBrands`
- `cancelarClienteKeycloak`
- `integrarClientesComFalha`

## Cuidados

- Fluxo sensível por credencial/autenticação. Reprocessamento deve considerar status de integração e respostas externas.
- Revisar [[../Matriz de Impacto]] antes de alterar contrato de método ou comportamento.
- Revisar [[../Mapa de Reprocessamento]] quando a mudança alterar idempotência, status ou efeito externo.
