# tbl_endereco

Endereço do cliente usado por venda, contrato, viabilidade, integração de estoque e atendimento.

## Resumo

| Item | Valor |
|---|---|
| Domínio | Endereço/viabilidade |
| Origem schema | [[../Banco - air_comercial]] |
| Classe provável | `configuracoes/model/Endereco` ou serviço de endereço |
| Repository provável | `EnderecoRepository` |
| Dados sensíveis | Endereço completo, coordenadas, referência, CEP |
| Fluxos principais | [[../Fluxos de Negocio/consulta-cliente]], [[../Fluxos de Negocio/criacao-integracao-contrato]] |

## Campos principais

| Campo | Tipo | Papel |
|---|---|---|
| `id` | `bigint` | Identificador interno. |
| `id_cliente` | `bigint` | Dono do endereço. |
| `id_logradouro` | `bigint` | Logradouro normalizado. |
| `id_cidade` | `bigint` | Cidade associada. |
| `codigo` | `varchar(40)` | Código externo/interno para busca. |
| `numero`, `complemento`, `referencia` | `varchar` | Componentes sensíveis do endereço. |
| `latitude`, `longitude` | `decimal` | Geolocalização sensível. |
| `unidade` | `varchar(10)` | Unidade de atendimento. |
| `ativo`, `excluido` | `tinyint` | Estado operacional. |
| `viabilidade_*` | vários | Decisão e auditoria de viabilidade. |
| `integracao_*_estoque` | vários | Estado de integração de estoque. |
| `certificado`, `verificado`, `completo` | vários | Qualidade/certificação do endereço. |
| `google_maps_*` | vários | Resultado/status de geocoding. |

## Índices e relações

| Tipo | Campos |
|---|---|
| PK | `id` |
| Índices relevantes | `codigo`, `id_cliente`, `id_logradouro`, `excluido`, `data_criacao`, `id_cidade` |
| FKs | `id_cliente -> tbl_cliente.id`, `id_logradouro -> tbl_endereco_logradouro.id`, `id_cidade -> tbl_endereco_cidade.id` |

## Endpoints e queries relacionadas

| Uso | Referência |
|---|---|
| Consulta de endereço do cliente | [[../Endpoints da Collection/get-cliente-endereco]] |
| Criação de contrato/integração com endereço | [[../Fluxos de Negocio/criacao-integracao-contrato]] |
| Shape da query de endereços | [[../Resultados SELECT/enderecorepository-findallenderecosbycliente]] |
| Cidade por sigla/unidade | [[../Resultados SELECT/enderecocidaderepository-findcidadebysigla]] |

## Cuidados de mudança

- Não usar dados reais de endereço em exemplos.
- Mudança em `id_cidade`, `unidade` ou viabilidade pode impactar ativação/instalação.
- Mudança nos campos `google_maps_*` ou coordenadas deve revisar privacidade e logs.
