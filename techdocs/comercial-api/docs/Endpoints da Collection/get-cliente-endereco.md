# get-cliente-endereco.bru

- Rota: `GET /cliente/{{id}}/endereco`
- Collection: `air-api-collection/comercial/get-cliente-endereco.bru`
- Codigo: `ClienteController.enderecos` em `comercial-api/src/main/java/br/net/air/cliente/controller/ClienteController.java:257`

## Queries e operacoes

| Query/operacao | Tipo | Artefato | Resultado SELECT | Caminho |
|---|---|---|---|---|
| `EnderecoRepository.findAllEnderecosByCliente` | `repository-native-query` | [enderecorepository-findallenderecosbycliente.sql](../enderecorepository-findallenderecosbycliente.sql) | [enderecorepository-findallenderecosbycliente.md](../Resultados SELECT/enderecorepository-findallenderecosbycliente.md) | `ClienteController.enderecos -> EnderecoService.findAllEnderecosByCliente -> EnderecoRepository.findAllEnderecosByCliente` |

## Observacoes

- Analise estatica; chamadas dinamicas e queries montadas indiretamente podem exigir revisao manual.
- Resultados SELECT mostram apenas colunas via `LIMIT 0`, sem dados reais de producao.
