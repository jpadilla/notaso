#!/bin/bash

case "$1" in
    rebuild)
        printf "Building container... "
        docker build --rm=true --tag="jpadilla/notaso" .

        printf "Done!\n"
        ;;
    setup)
        printf "Setting up notaso-web container... "
        docker run --rm=true jpadilla/notaso setup

        printf "Done!\n"
        ;;
    start)
        printf "Starting notaso-web container... "
        docker run -d -i -t -p 8000:8000 --name=notaso-web jpadilla/notaso start

        printf "Done!\n"
        ;;
    pause)
        printf "Stopping notaso-web container... "
        docker stop notaso-web

        printf "Removing notaso-web container... "
        docker rm notaso-web

        printf "Done!\n"
        ;;
    stop)
        printf "Stopping notaso-web container... "
        docker stop notaso-web

        printf "Removing notaso-web container... "
        docker rm notaso-web

        printf "Done!\n"
        ;;
*)
    echo $"Usage: $0 {start|pause|stop|setup}"
    exit 1
esac
exit 0
