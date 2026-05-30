# tbl_lead

Lead comercial usado para prospecção, análise de crédito, venda e integração com canais externos.

## Resumo

| Item | Valor |
|---|---|
| Domínio | Lead/prospecção |
| Origem schema | [[../Banco - air_comercial]] |
| Classe provável | `venda/model/Lead.java` |
| Repository provável | `LeadRepository` |
| Dados sensíveis | Nome, telefone, e-mail, documento, endereço, data de nascimento, RG, filiação, senha SAC |
| Fluxos principais | [[../Fluxos de Negocio/criacao-integracao-contrato]], [[../Fluxos de Negocio/analise-credito]], [[../Fluxos de Negocio/vendas-e-migracoes]] |

## Campos principais

| Campo | Tipo | Papel |
|---|---|---|
| `id` | `bigint` | Identificador do lead. |
| `id_cliente` | `bigint` | Cliente associado quando já existe. |
| `tipo` | `varchar(20)` | Tipo de lead/pessoa. |
| `nome`, `telefone`, `email` | vários | Contato principal. |
| `cpf_cnpj` | `varchar(18)` | Documento; único e sensível. |
| `end_*` | vários | Endereço capturado no lead. |
| `pf_*`, `pj_*` | vários | Dados específicos PF/PJ. |
| `senha_sac` | `varchar(255)` | Campo sensível; não expor. |
| `qualificacao` | `varchar(255)` | Estado comercial do lead. |
| `credito_autorizado`, `viabilidade_autorizada` | `tinyint` | Decisões comerciais/operacionais. |
| `uuid_lead_rd_station` | `varchar(255)` | Vínculo com RD Station. |

## Índices e relações

| Tipo | Campos |
|---|---|
| PK | `id` |
| Únicos | `id_cliente`, `cpf_cnpj` |
| Índices relevantes | `id_carteira`, `end_id_cidade`, `end_id_bairro`, `end_id_logradouro`, `id_condominio` |
| FKs declaradas | Não listadas no dump para esta tabela, apesar de existirem campos relacionais. |

## Endpoints e queries relacionadas

| Uso | Referência |
|---|---|
| Criação de contrato via integração | [[../Endpoints da Collection/post-criar-integracao]], [[../Endpoints da Collection/test-criar-integracao]] |
| Análise de crédito por cliente/lead | [[../Endpoints da Collection/get-cliente-analise-credito]] |
| Query de análise por lead/cliente | [[../Resultados SELECT/analisecreditorepository-findallbyleadclienteid]] |
| Venda por natureza/contrato | [[../Fluxos de Negocio/vendas-e-migracoes]] |

## Cuidados de mudança

- `cpf_cnpj`, contato, endereço, filiação e `senha_sac` são sensíveis.
- Mudança em `qualificacao` deve revisar funil comercial e integrações.
- Mudança em campos RD Station/fonte deve revisar tracking de origem.
- Mudança em autorização de crédito/viabilidade deve revisar os fluxos de aprovação.
