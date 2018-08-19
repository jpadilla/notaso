#!/bin/ash

set -e

if [ "$1" = 'start' ]; then
  echo "==> Running migrations..."
  python manage.py collectstatic --noinput
  python manage.py makemigrations comments departments professors universities users
  python manage.py migrate

  echo "==> Running dev server..."
  python manage.py runserver 0.0.0.0:8000
else
  exec "$@"
fi
