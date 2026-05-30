#!/usr/bin/env sh
set -eu

kubectl apply -f kubernetes/air-comercial-demo.yaml
kubectl -n air-demo rollout status deploy/air-comercial
kubectl -n air-demo get deploy,svc,ingress,pods -l backstage.io/kubernetes-id=air-comercial

