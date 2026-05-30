---
tags:
  - trabalho
  - air
  - comercial-api
  - risco
---
# Mapa de Risco - comercial-api

Classificação qualitativa para orientar revisão. Não substitui análise de produção; usa documentação estática, dados sensíveis e efeito de escrita.

| Área/tabela | Domínio | Dado sensível | Escrita crítica | Integração externa provável | Duplicidade/reprocessamento | Impacto |
|---|---|---|---|---|---|---|
| `tbl_cliente` | Cliente/OAuth | `alto` | `alto` | `sim` | `medio` | `alto` |
| `tbl_endereco` | Cliente/Endereço | `medio` | `alto` | `nao` | `medio` | `alto` |
| `tbl_lead` | Lead/Venda | `alto` | `alto` | `nao` | `medio` | `alto` |
| `tbl_venda` | Venda | `medio` | `alto` | `sim` | `alto` | `alto` |
| `tbl_venda_adicional` | Venda | `medio` | `alto` | `sim` | `alto` | `alto` |
| `tbl_venda_origem` | Venda/Integração | `medio` | `alto` | `sim` | `medio` | `alto` |
| `tbl_contrato` | Contrato | `medio` | `alto` | `sim` | `alto` | `alto` |
| `tbl_contrato_campanha` | Contrato/Campanha | `medio` | `alto` | `sim` | `alto` | `alto` |
| `tbl_contrato_produto` | Contrato/Produto | `medio` | `alto` | `sim` | `medio` | `alto` |
| `tbl_contrato_item` | Contrato/Produto | `medio` | `alto` | `sim` | `medio` | `alto` |
| `tbl_contrato_migracao` | Migração | `medio` | `alto` | `sim` | `medio` | `alto` |
| `tbl_analise_credito` | Crédito | `alto` | `alto` | `sim` | `medio` | `alto` |
| `tbl_analise_credito_atributo` | Crédito | `medio` | `alto` | `sim` | `medio` | `alto` |
| `tbl_analise_credito_restricao` | Crédito | `medio` | `alto` | `sim` | `medio` | `alto` |
| `tbl_blacklist` | Cliente/Restrição | `medio` | `alto` | `nao` | `medio` | `alto` |

## Regras de leitura

- `alto` em escrita crítica exige consultar [[Mapa de Reprocessamento]].
- `alto` em dado sensível exige consultar [[Operacional/Dados Sensiveis]] e [[ADRs/0002-nao-documentar-dados-reais-de-producao]].
- Integração externa provável exige consultar [[Integracoes Externas/Index]] antes de alterar payload, retry ou status.
