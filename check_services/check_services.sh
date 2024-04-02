#!/bin/bash

if docker compose ps --services --filter "status=running" | grep -q -v homepage; then
  echo "Non tutti i servizi sono in esecuzione."
  exit 1
fi
curl -X POST services-discovery:5001/api/v1/homepage/refresh
