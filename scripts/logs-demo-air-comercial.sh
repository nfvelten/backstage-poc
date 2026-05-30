#!/usr/bin/env sh
set -eu

kubectl -n air-demo logs deploy/air-comercial -c log-generator -f

