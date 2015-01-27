#!/bin/bash

case "$1" in
    start)
        echo "Running server..."
        gunicorn -b "0.0.0.0:$PORT" -w 3 notaso.wsgi
        ;;
    setup)
        echo "Running migrations..."
        python manage.py syncdb --migrate --noinput
        ;;
*)
    echo $"Usage: $0 {start}"
    exit 1
esac
exit 0
