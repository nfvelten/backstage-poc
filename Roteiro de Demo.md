# Roteiro de Demo - Backstage PoC

## Narrativa

"Hoje nossas informações estão espalhadas entre GitLab, Rancher/Kubernetes, Grafana, logs e notas. A PoC mostra um portal único onde uma pessoa consegue entrar pelo serviço e chegar em código, operação, documentação, owners e dependências."

## Fluxo da apresentação

1. Abrir a home do Backstage.
2. Buscar `air-comercial`.
3. Mostrar a página do serviço demo:
   - owner;
   - lifecycle;
   - sistema;
   - links para GitLab, Azure Boards, Rancher e Grafana;
   - dependências.
4. Mostrar Kubernetes:
   - deployment;
   - pod;
   - service;
   - ingress;
   - logs do sidecar `log-generator`.
5. Abrir TechDocs da `comercial-api`.
6. Navegar por:
   - endpoints;
   - fluxos de negócio;
   - matriz de escrita por tabela;
   - integrações externas;
   - mapa de risco;
   - runbooks/testes manuais.
7. Mostrar como uma pessoa investigaria incidente:
   - serviço -> dashboard;
   - serviço -> workload/logs;
   - serviço -> runbook;
   - serviço -> dependências.
8. Mostrar o catálogo de recursos:
   - banco `air_comercial`;
   - Grafana;
   - Kubernetes/Rancher;
   - GitLab.
9. Fechar com roadmap:
   - SSO;
   - plugins reais;
   - templates;
   - scorecards;
   - onboarding dos outros serviços.

## Frase de fechamento

"O Backstage não substitui GitLab, Grafana ou Rancher. Ele vira o índice operacional confiável que conecta tudo."
