# Deploy no Contabo - Backstage PoC

Guia operacional para transformar este pacote em uma demo no Kubernetes do Contabo.

## Pré-requisitos

- Cluster Kubernetes acessível por `kubectl`.
- Ingress Controller instalado.
- DNS apontando para o Ingress, por exemplo `backstage.poc.seudominio.com`.
- Imagem Docker do Backstage publicada em registry acessível pelo cluster.
- Secrets reais criados fora do Git/vault.

## Valores que precisam ser trocados

| Placeholder | Substituir por |
|---|---|
| `backstage.poc.example.com` | Domínio real da PoC |
| `gitlab.example.internal` | Host do GitLab self-hosted |
| `grafana.example.internal` | Host do Grafana |
| `rancher.example.internal` | Host do Rancher |
| `logs.example.internal` | URL da ferramenta de logs |
| `change-me` | Secret real criado via Kubernetes Secret |
| `backstage-poc:latest` | Imagem real publicada em registry |

## Sequência de deploy

```bash
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/postgres.yaml
kubectl apply -f kubernetes/backstage-rbac.yaml
kubectl apply -f kubernetes/backstage.yaml
kubectl apply -f kubernetes/ingress.yaml
kubectl apply -f kubernetes/air-comercial-demo.yaml
```

## Sobre o ConfigMap

O arquivo `kubernetes/backstage.yaml` contém um `ConfigMap` mínimo. Para o deploy real, copiar o conteúdo de `app-config.poc.yaml` para o campo `app-config.poc.yaml` do ConfigMap ou gerar o ConfigMap via pipeline.

## Sobre o catálogo

Os arquivos em `catalog/` precisam estar disponíveis dentro do container em `/app/catalog/`, porque o `app-config.poc.yaml` aponta para:

- `/app/catalog/domains-systems.yaml`
- `/app/catalog/resources.yaml`
- `/app/catalog/comercial-api.yaml`
- `/app/catalog/air-comercial-demo.yaml`

Para uma PoC rápida, a imagem Docker pode copiar a pasta `catalog/` para `/app/catalog/`.

## Aplicação demo

O manifest `kubernetes/air-comercial-demo.yaml` cria:

- namespace `air-demo`;
- deployment `air-comercial`;
- container `nginx` para workload HTTP simples;
- sidecar `log-generator` emitindo logs JSON;
- service e ingress;
- labels `backstage.io/kubernetes-id=air-comercial` para o plugin Kubernetes.

## Plugin Kubernetes

O `app-config.poc.yaml` já inclui um bloco `kubernetes` apontando para o cluster local via `https://kubernetes.default.svc`.
O manifesto `kubernetes/backstage-rbac.yaml` cria uma ServiceAccount `backstage` com permissão somente leitura para pods, logs, services, deployments e ingresses.

Comandos úteis:

```bash
kubectl -n air-demo get deploy,svc,ingress,pods
kubectl -n air-demo logs deploy/air-comercial -c log-generator -f
```

## Sobre o TechDocs

A documentação da `comercial-api` fica em:

```text
techdocs/comercial-api/
  mkdocs.yml
  docs/
```

O `catalog/comercial-api.yaml` usa:

```yaml
backstage.io/techdocs-ref: dir:../techdocs/comercial-api
```

Se o catálogo for movido para outro repo ou path dentro da imagem, ajustar essa annotation.

## Segurança

- Não colocar tokens reais nos YAML versionados.
- Começar atrás de VPN, Cloudflare Access ou SSO.
- Evitar abrir a PoC publicamente, porque ela documenta endpoints, banco, riscos e integrações internas.
