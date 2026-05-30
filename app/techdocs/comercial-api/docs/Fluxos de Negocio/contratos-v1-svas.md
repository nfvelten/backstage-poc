# Contratos V1 e SVAs

Gerado em: 2026-05-30 10:11:02

- Objetivo: Consulta detalhes agregados de contrato, pacote, itens, SVAs e elegibilidade.
- Risco operacional: `medio`
- Endpoints: 4
- Queries/operações mapeadas: 2
- Tabelas SQL identificadas: 0

## Endpoints

| Endpoint | Rota | Codigo | Request body | Response |
|---|---|---|---|---|
| [get-contracts-detail.md](../Endpoints da Collection/get-contracts-detail.md) | `GET /v1/contracts/detail?contract_number={{contract_number}}` | `ContractsControllerV1.findContractDetails` | `-` | `ResponseEntity<GetSvasDto>` |
| [get-contracts-customer-basic-info.md](../Endpoints da Collection/get-contracts-customer-basic-info.md) | `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}` | `ContractsControllerV1.getCustomerBasicInfoByContractNumber` | `-` | `ResponseEntity<CustomerBasicInfoDto>` |
| [get-contrato-svas-v1.md](../Endpoints da Collection/get-contrato-svas-v1.md) | `GET /v1/contracts/{{id}}/svas` | `-` | `-` | `-` |
| [get-elegibilidade-confianca.md](../Endpoints da Collection/get-elegibilidade-confianca.md) | `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}` | `ContractsControllerV1.sydleContractTrustEnablementBalance` | `-` | `ResponseEntity<CheckContractTrustEnablementBalanceResponse>` |

## Contrato HTTP observado

### `GET /v1/contracts/detail?contract_number={{contract_number}}`

- Assinatura: `public ResponseEntity<GetSvasDto> findContractDetails( @RequestParam("contract_number") Long contractId)`
- Body Bruno: sem body JSON.

### `GET /v1/contracts/customer-basic-info?contract_number={{contract_number}}`

- Assinatura: `public ResponseEntity<CustomerBasicInfoDto> getCustomerBasicInfoByContractNumber( @RequestParam(value = "contract_number", required = false) Long contractId, @RequestParam(value = "document", required = false) String document)`
- Body Bruno: sem body JSON.

### `GET /v1/contracts/{{id}}/svas`

- Body Bruno: sem body JSON.

### `GET /v1/contracts/enable-by-trust-elegibility?contract_number={{contract_number}}`

- Assinatura: `public ResponseEntity<CheckContractTrustEnablementBalanceResponse> sydleContractTrustEnablementBalance( @RequestParam("contract_number") Long contractId)`
- Body Bruno: sem body JSON.

## Queries e operações

| Query/operação | Tipo | Artefato | Shape | Caminho |
|---|---|---|---|---|
| `ContratoRepository.findContractProductsAndItems` | `repository-jpql-query` | `../JPA%20e%20Repositories.md#contratorepository-findcontractproductsanditems` | - | `ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails -> ContratoRepository.findContractProductsAndItems` |
| `ContratoRepository.findPacoteById` | `repository-jpql-query` | `../JPA%20e%20Repositories.md#contratorepository-findpacotebyid` | - | `ContractsControllerV1.findContractDetails -> ContractServiceV1.findContractDetails -> ContratoRepository.findPacoteById` |

## Tabelas tocadas por SQL nativo

- Nenhuma tabela extraida de SQL nativo neste fluxo.

## Efeitos colaterais e integrações

Integrações/sistemas citados no caminho ou SQL:
- Sydle

## Dados sensíveis

Sinais de dados sensíveis encontrados em nomes de campos, queries ou caminho:
- `document`

## Pendências de mapeamento

- Nenhuma chamada pendente neste fluxo.

## Limites

- Documento gerado por análise estática.
- Queries derivadas Spring Data são aproximações semânticas; o SQL final depende do Hibernate e dos mappings.
- Shapes de SELECT foram obtidos com `LIMIT 0`, sem dados reais de produção.
