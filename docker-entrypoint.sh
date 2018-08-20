#!/bin/ash

set -e

postgres_ready(){
python manage.py shell << END
import sys
import psycopg2
from django.db import connections
try:
    connections['default'].cursor()
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

if [ "$1" = 'start' ]; then
  until postgres_ready; do
    >&2 echo "==> Waiting for Postgres..."
    sleep 1
  done

  echo "==> Running migrations..."
  python manage.py collectstatic --noinput
  python manage.py migrate
  python manage.py loaddata notaso/universities/fixtures/initial.json
  python manage.py loaddata notaso/departments/fixtures/initial.json
  python manage.py loaddata notaso/users/fixtures/dummy.json
  python manage.py loaddata notaso/professors/fixtures/dummy.json
  python manage.py loaddata notaso/comments/fixtures/dummy.json

  echo "==> Running dev server..."
  python manage.py runserver 0.0.0.0:8000
else
  exec "$@"
fi
