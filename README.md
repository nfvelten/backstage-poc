# Backstage PoC - Portal de Engenharia Air

PoC para apresentar um portal interno de engenharia usando Backstage, simulando o ambiente real com GitLab self-hosted, Kubernetes/Rancher, Grafana self-hosted e TechDocs.

## Objetivo

Criar uma demo navegável que responda rapidamente:

- Onde está o repositório de um serviço?
- Quem é o owner?
- Onde vejo logs/workload no Kubernetes/Rancher?
- Onde está o dashboard Grafana?
- Quais dependências esse serviço usa?
- Onde está a documentação operacional?
- Como investigar incidente ou alterar endpoint/query/fluxo?

## Escopo da PoC

| Área | O que entra na PoC | Integração real agora? |
|---|---|---|
| Catálogo | `comercial-api`, sistemas, recursos e dependências | Sim, via YAML |
| Aplicação demo | `air-comercial` rodando em Kubernetes e emitindo logs fake | Sim, via manifest |
| TechDocs | Documentação da `comercial-api` em Markdown/MkDocs | Sim, com docs exportadas |
| GitLab | Links para repo, pipelines e MRs | Começar com links; plugin depois |
| Azure Boards | Link para board/work items da demo | Começar com links; plugin depois |
| Kubernetes/Rancher | Links para workload/logs e entidade cluster | Começar com links; plugin depois |
| Grafana | Links para dashboards | Começar com links; plugin depois |
| Scorecard | Checklist de maturidade por serviço | Sim, como documentação inicial |
| SSO | OAuth/OIDC com provedor interno | Fase seguinte |

## Arquitetura

```text
Usuários internos
    |
VPN / Cloudflare Access / SSO
    |
Backstage no Kubernetes Contabo
    |
PostgreSQL
    |
Catalog YAML + TechDocs
    |
Links para GitLab / Rancher / Grafana
```

## Estrutura deste pacote

| Caminho | Uso |
|---|---|
| `catalog/` | Entidades iniciais do catálogo Backstage. |
| `kubernetes/` | Manifests de referência para subir Backstage no cluster Contabo. |
| `kubernetes/air-comercial-demo.yaml` | Serviço fake para emular a comercial-api em Kubernetes. |
| `techdocs/comercial-api/` | Fonte TechDocs da `comercial-api`. |
| `config/gitlab-ci.demo.yml` | Pipeline GitLab demo para a aplicação fake. |
| `app-config.poc.yaml` | Configuração exemplo do Backstage para a PoC. |
| `Aplicacao Demo Air Comercial.md` | Explica a simulação da aplicação, logs e relações com Backstage. |
| `Integracoes da PoC.md` | Mapa das integrações simuladas/planejadas. |
| `Roteiro de Demo.md` | Sequência para apresentar ao time. |
| `Roadmap.md` | Fases para evoluir PoC para portal interno. |

## Decisão recomendada

Começar simples:

1. Subir Backstage no Contabo.
2. Cadastrar `comercial-api` e `air-comercial` no catálogo.
3. Subir `air-comercial` fake no Kubernetes e mostrar pod/logs.
4. Abrir TechDocs da documentação já criada.
5. Mostrar links de operação para GitLab, Azure Boards, Rancher e Grafana.
6. Depois integrar plugins e SSO.

Não começar tentando integrar tudo profundamente no primeiro dia. A primeira demo precisa provar valor de navegação e centralização.
