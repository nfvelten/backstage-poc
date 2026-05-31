---
tags:
  - trabalho
  - air
  - comercial-api
  - dados
---
# Matriz de Escrita por Tabela - comercial-api

Visão invertida por dado: quais endpoints leem, quais escrevem, quais services concentram regra e qual risco revisar antes de mudança.

| Tabela | Domínio | Lê | Escreve | Services | Risco |
|---|---|---|---|---|---|
| `tbl_analise_credito` | Crédito | [[Endpoints da Collection/get-cliente-analise-credito|get-cliente-analise-credito]], [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `AnaliseCreditoService` | Dado financeiro/crédito; não expor retorno real de bureau. |
| `tbl_analise_credito_atributo` | Crédito | [[Endpoints da Collection/get-cliente-analise-credito|get-cliente-analise-credito]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `AnaliseCreditoService` | Atributos de análise podem conter indicadores sensíveis. |
| `tbl_analise_credito_restricao` | Crédito | [[Endpoints da Collection/get-cliente-analise-credito|get-cliente-analise-credito]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `AnaliseCreditoService` | Restrições financeiras; alto cuidado em logs/docs. |
| `tbl_blacklist` | Cliente/Restrição | [[Endpoints da Collection/get-cliente-blacklist|get-cliente-blacklist]] | rotas administrativas fora da collection atual | `BlacklistService` | Restrição de cliente; dado sensível operacional/comercial. |
| `tbl_cliente` | Cliente/OAuth | [[Endpoints da Collection/get-cliente-por-id|get-cliente-por-id]], [[Endpoints da Collection/get-cliente-por-cpf|get-cliente-por-cpf]], [[Endpoints da Collection/get-cliente-contrato|get-cliente-contrato]], [[Endpoints da Collection/post-oauth-integrar|post-oauth-integrar]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]], [[Endpoints da Collection/post-oauth-integrar|post-oauth-integrar]] | `ClienteService`, `OauthIntegracaoService` | PII, integração OAuth/eCare e vínculo com contrato. |
| `tbl_contrato` | Contrato | [[Endpoints da Collection/get-contrato|get-contrato]], [[Endpoints da Collection/get-cliente-contrato|get-cliente-contrato]], [[Endpoints da Collection/get-contracts-detail|get-contracts-detail]], [[Endpoints da Collection/get-contracts-customer-basic-info|get-contracts-customer-basic-info]], [[Endpoints da Collection/get-contrato-svas-v1|get-contrato-svas-v1]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]], [[Endpoints da Collection/ativar-servicos|ativar-servicos]] | `ContratoService`, `VendaService` | Entidade central; mudança afeta atendimento, ativação, OAuth, migração e SVA. |
| `tbl_contrato_campanha` | Contrato/Campanha | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]], [[Endpoints da Collection/ativar-servicos|ativar-servicos]] | [[Endpoints da Collection/ativar-servicos|ativar-servicos]] | `ContratoService`, `ContratoCampanhaService` | Desconto recorrente; reprocessamento pode reaplicar benefício. |
| `tbl_contrato_item` | Contrato/Produto | [[Endpoints da Collection/get-contrato|get-contrato]], [[Endpoints da Collection/get-contrato-svas-v1|get-contrato-svas-v1]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `ContratoService`, `ContratoItemService` | Detalhe de item/produto; pode afetar SVA e exibição de contrato. |
| `tbl_contrato_migracao` | Migração | [[Endpoints da Collection/get-migracoes-contrato|get-migracoes-contrato]] | fluxos de migração fora da collection atual | `ContratoMigracaoService` | Histórico e pendência de migração; risco de versão de contrato indevida. |
| `tbl_contrato_produto` | Contrato/Produto | [[Endpoints da Collection/get-contrato|get-contrato]], [[Endpoints da Collection/get-contrato-svas-v1|get-contrato-svas-v1]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `ContratoService`, `ContratoProdutoService` | Composição comercial/técnica do contrato. |
| `tbl_endereco` | Cliente/Endereço | [[Endpoints da Collection/get-cliente-endereco|get-cliente-endereco]], [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `EnderecoService`, `ClienteService` | Endereço completo e georreferência; evitar exemplos reais. |
| `tbl_lead` | Lead/Venda | [[Endpoints da Collection/get-cliente-analise-credito|get-cliente-analise-credito]], [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `LeadService`, `AnaliseCreditoService` | PII, contato, endereço e senha SAC em shape/tabela. |
| `tbl_venda` | Venda | [[Endpoints da Collection/get-vendas-by-natureza|get-vendas-by-natureza]], [[Endpoints da Collection/get-vendas-contrato|get-vendas-contrato]], [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]], [[Endpoints da Collection/ativar-servicos|ativar-servicos]] | `VendaService` | Estado comercial, ativação, confirmação/cancelamento e integração externa. |
| `tbl_venda_adicional` | Venda | [[Endpoints da Collection/get-vendas-contrato|get-vendas-contrato]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `VendaService`, `VendaAdicionalService` | Adicionais comerciais podem ser duplicados se integração for reprocessada sem checagem. |
| `tbl_venda_origem` | Venda/Integração | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | [[Endpoints da Collection/post-criar-integracao|post-criar-integracao]] | `VendaService` | Correlação com origem externa; chave para idempotência com Sydle. |

## Como usar

- Comece por esta matriz quando a mudança for em migration, entidade JPA, query ou índice.
- Para tabelas com escrita, abrir também [[Mapa de Reprocessamento]] e [[Playbooks de Mudanca]].
- Para tabelas com PII/crédito/credencial, abrir [[Operacional/Dados Sensiveis]].
