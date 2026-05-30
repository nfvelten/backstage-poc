# get-contracts-detail.bru

- Rota: `GET /v1/contracts/detail?contract_number={{contract_number}}`
- Collection: `air-api-collection/comercial/get-contracts-detail.bru`
- Codigo: `ContractsControllerV1.findContractDetails` em `comercial-api/src/main/java/br/net/air/clean_arch/application/controllers/ContractsControllerV1.java:32`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `ContratoRepository.findContractProductsAndItems` | `repository-jpql-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratorepository-findcontractproductsanditems) | - | `ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails -> ContratoRepository.findContractProductsAndItems` |
| `ContratoRepository.findPacoteById` | `repository-jpql-query` | [JPA e Repositories.md](../JPA%20e%20Repositories.md#contratorepository-findpacotebyid) | - | `ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails -> ContratoRepository.findPacoteById` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
