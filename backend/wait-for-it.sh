#!/usr/bin/env bash

# wait-for-it.sh
# Licence: MIT
# Source: https://github.com/vishnubob/wait-for-it

set -e

host="$1"
shift
port="$1"
shift

timeout=30

echo "⏳ Attente que $host:$port soit prêt..."

for i in $(seq $timeout); do
  if nc -z "$host" "$port"; then
    echo "✅ $host:$port est prêt !"
    exec "$@"
    exit
  fi
  sleep 1
done

echo "❌ Timeout après $timeout secondes en attendant $host:$port"
exit 1
