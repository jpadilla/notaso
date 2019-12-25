#!/bin/bash

set +e
echo "Checking if Docker is running..."
docker ps > /dev/null 2>&1
if [ $? != "0" ]; then
  echo "Docker needs to be running."
  exit 1
fi
set -e

echo "Running tests..."

docker-compose run \
  --rm \
  -e DATABASE_URL=postgres://postgres:password@database/postgres \
  web \
  tests