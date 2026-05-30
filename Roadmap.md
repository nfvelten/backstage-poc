# Roadmap - Backstage PoC

## Fase 0 - PoC local no Contabo

- Subir Backstage em Kubernetes.
- Configurar PostgreSQL.
- Cadastrar `comercial-api`.
- Publicar TechDocs da `comercial-api`.
- Adicionar links para GitLab, Rancher e Grafana.

## Fase 1 - Demo interna

- Validar navegação com 2 ou 3 pessoas do time.
- Ajustar nomes, owners e links.
- Coletar quais serviços devem entrar depois.
- Definir padrão mínimo de `catalog-info.yaml`.

## Fase 2 - Integrações reais

- GitLab: repos, pipelines e merge requests.
- Kubernetes: workloads, pods e deploys.
- Grafana: dashboards e alertas.
- Auth: SSO/OIDC.

## Fase 3 - Governança

- Scorecards por serviço:
  - tem owner;
  - tem TechDocs;
  - tem dashboard;
  - tem runbook;
  - tem dependências;
  - tem ADRs.
- Templates para novo serviço/API.
- Processo de PR exigindo documentação mínima.

## Fase 4 - Escala

- Onboard dos principais serviços.
- Catálogo de APIs.
- Catálogo de bancos/filas/integrações.
- Portal de incidentes e runbooks.

