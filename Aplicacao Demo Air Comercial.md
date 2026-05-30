# Aplicação Demo - air-comercial

Esta aplicação demo existe para apresentar o Backstage sem depender da infraestrutura real do trabalho.

## O que ela emula

| Peça real | Emulação na PoC |
|---|---|
| `comercial-api` | Serviço `air-comercial` no catálogo Backstage |
| Pod Kubernetes | Deployment `air-comercial` no namespace `air-demo` |
| Logs via Rancher/Kubernetes | Sidecar `log-generator` emitindo JSON em stdout |
| GitLab self-hosted | Links e pipeline demo em `config/gitlab-ci.demo.yml` |
| Azure Boards | Link de board/work items no catálogo |
| Grafana | Link de dashboard demo |
| API docs | TechDocs exportado da documentação real da `comercial-api` |

## Demo de logs

Depois de aplicar o manifest no cluster:

```bash
kubectl -n air-demo get pods
kubectl -n air-demo logs deploy/air-comercial -c log-generator -f
```

Exemplo de linha gerada:

```json
{"service":"air-comercial","env":"poc-contabo","level":"INFO","event":"contract.detail.request","route":"/v1/contracts/detail","status":200,"duration_ms":41,"trace_id":"demo-1"}
```

## Relação com Backstage

O componente `air-comercial` usa as annotations:

```yaml
backstage.io/kubernetes-id: air-comercial
backstage.io/kubernetes-namespace: air-demo
backstage.io/kubernetes-label-selector: app=air-comercial,backstage.io/kubernetes-id=air-comercial
```

Os manifests Kubernetes usam os mesmos labels, permitindo que o plugin Kubernetes do Backstage encontre Deployment, Pod, Service e Ingress.

## Como apresentar

1. Abrir o componente `air-comercial` no Backstage.
2. Mostrar links para GitLab, Azure Boards, Rancher e Grafana.
3. Abrir a aba Kubernetes e mostrar pod/deployment.
4. Abrir logs do pod no Rancher ou via `kubectl`.
5. Abrir TechDocs e mostrar a documentação operacional da `comercial-api`.
6. Mostrar o pipeline demo no GitLab.

## Limites da simulação

- Não usa banco real.
- Não chama Sydle, Keycloak, Grafana ou Azure Boards de verdade.
- Não publica métricas reais.
- Não depende de VPN do trabalho.
- Não carrega credenciais internas.

