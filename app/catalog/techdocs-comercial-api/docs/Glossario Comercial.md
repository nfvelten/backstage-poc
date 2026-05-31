---
tags:
  - trabalho
  - air
  - comercial-api
  - glossario
---
# Glossario Comercial - comercial-api

Vocabulário de domínio para reduzir ambiguidade entre código, banco, collection e operação.

| Termo | Significado prático | Tabelas | Docs | Cuidados |
|---|---|---|---|---|
| Análise de crédito | Consulta e persistência de resultado financeiro/crédito, com atributos e restrições. | `tbl_analise_credito`, `tbl_analise_credito_atributo`, `tbl_analise_credito_restricao` | [[Contratos de Dados/tbl_analise_credito]], [[Fluxos de Negocio/analise-credito]] | Não versionar retorno real de bureau, XML, documento ou score individual. |
| Aviso | Mensagem/alerta relacionado a cliente ou contrato, incluindo rede, telefonia, migração e avisos manuais. | `tbl_contrato`, `air_internet.tbl_aviso*`, `air_telefonia.tbl_reserva` | [[Fluxos de Negocio/avisos-cliente-contrato]], [[Resultados SELECT/sql-aviso-rede-monitorado]] | Consultas são cross-schema; alteração pode afetar atendimento, URA e comunicação com cliente. |
| Blacklist | Restrição operacional/comercial associada ao cliente. | `tbl_blacklist` | [[Fluxos de Negocio/blacklist]], [[Endpoints da Collection/get-cliente-blacklist]] | Dado sensível de decisão/atendimento; evite expor motivo ou registro real fora do sistema. |
| Campanha | Oferta/regra comercial aplicada a venda ou contrato, incluindo desconto recorrente. | `tbl_contrato_campanha`, `tbl_campanha` | [[Mapa de Reprocessamento]], [[Services Criticos/contrato-service]] | Na ativação, conferir `recorrenciaDescontoAplicado` antes de reprocessar desconto. |
| Cliente | Pessoa física ou jurídica usada como base para contrato, contato, endereço, autenticação e atendimento. | `tbl_cliente`, `tbl_cliente_fisico`, `tbl_cliente_juridico`, `tbl_endereco` | [[Contratos de Dados/tbl_cliente]], [[Fluxos de Negocio/consulta-cliente]] | Contém documento, contato, endereço e credenciais indiretas; não usar payload real em documentação. |
| Contrato | Relação comercial do cliente com produtos, serviços, campanha, migração, aviso e status operacional. | `tbl_contrato`, `tbl_contrato_produto`, `tbl_contrato_item`, `tbl_contrato_campanha`, `tbl_contrato_migracao` | [[Contratos de Dados/tbl_contrato]], [[Fluxos de Negocio/criacao-integracao-contrato]] | É entidade central; mudanças afetam atendimento, ativação, OAuth, avisos, migração e faturamento. |
| Lead | Oportunidade comercial que antecede ou acompanha venda/contrato. | `tbl_lead` | [[Contratos de Dados/tbl_lead]], [[Fluxos de Negocio/criacao-integracao-contrato]] | Pode carregar dados pessoais, endereço, contato e análise de crédito. |
| Migração | Mudança de pacote/plano/contrato, incluindo migração compulsória e histórico de alterações. | `tbl_contrato_migracao`, `tbl_venda`, `tbl_contrato` | [[Fluxos de Negocio/vendas-e-migracoes]], [[Endpoints da Collection/get-migracoes-contrato]] | Já houve histórico de risco em versionamento indevido de contrato; revisar ciclo de vida antes de mudar. |
| Origem Sydle | Origem externa de venda/processo usada para correlacionar integração, cliente, venda e contrato. | `tbl_venda`, `tbl_venda_origem` | [[Fluxos de Negocio/criacao-integracao-contrato]], [[Services Criticos/venda-service]] | Chamadas podem chegar duplicadas; usar id de processo e buscas existentes para reduzir duplicidade. |
| SVA | Serviço de valor agregado associado a contrato, exposto em rotas v1 de contracts. | `tbl_contrato`, `tbl_contrato_produto`, `tbl_contrato_item` | [[Fluxos de Negocio/contratos-v1-svas]], [[Endpoints da Collection/get-contrato-svas-v1]] | Rota `/svas` é distinta de `/v1/contracts/detail`; manter separação no mapeamento. |
| Venda | Processo comercial com natureza, fase, origem, adicionais, ativação e possível contrato associado. | `tbl_venda`, `tbl_venda_adicional`, `tbl_venda_origem` | [[Contratos de Dados/tbl_venda]], [[Fluxos de Negocio/vendas-e-migracoes]] | Estado incorreto pode duplicar ativação, confirmar venda errada ou travar reprocessamento. |

## Como usar

- Ao revisar endpoint, use este glossário para alinhar nome de rota, entidade JPA, tabela e termo de negócio.
- Quando um termo novo aparecer em controller, service, query ou collection, adicionar aqui antes de espalhar em páginas específicas.
