# Integrações da PoC

Mapa das integrações planejadas para a apresentação do Backstage.

## Kubernetes / Rancher

Usar o plugin Kubernetes do Backstage com labels no manifesto demo.

Pontos de configuração:

- Entity annotation: `backstage.io/kubernetes-id`
- Entity annotation opcional: `backstage.io/kubernetes-namespace`
- Entity annotation opcional: `backstage.io/kubernetes-label-selector`
- Resource label: `backstage.io/kubernetes-id`

Referência oficial: https://backstage.io/docs/next/features/kubernetes/configuration/

## GitLab

Para a PoC:

- link para repositório;
- link para pipelines;
- arquivo de pipeline demo em `config/gitlab-ci.demo.yml`;
- annotation `gitlab.com/project-slug` no componente.

Depois da demo, avaliar plugin GitLab para mostrar pipelines, merge requests e releases dentro da página do componente.

## Azure Boards

Para a PoC:

- link direto para board;
- annotation `dev.azure.com/project-repo` como metadado demonstrativo;
- cards nativos podem entrar depois via plugin Azure DevOps/community plugin.

Referência de integração Azure no Backstage: https://backstage.io/docs/integrations/azure/discovery/

## Grafana

Para a PoC:

- link direto para dashboard demo;
- o dashboard pode filtrar por `service=air-comercial` se existir Loki/Prometheus no Contabo.

Depois da demo:

- adicionar plugin Grafana;
- padronizar dashboard por serviço;
- guardar link no `catalog-info.yaml`.

## Logs

Para a PoC:

- logs via stdout do pod;
- visualização via `kubectl logs` ou Rancher.

Depois da demo:

- se houver Loki/Promtail no Contabo, mandar os logs demo para Grafana;
- manter `service=air-comercial` e `env=poc-contabo` como labels/campos.

