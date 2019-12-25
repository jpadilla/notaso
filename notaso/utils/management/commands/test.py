import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs the application tests while connected to a DB by using docker-compose"

    def handle(self, *args, **options):
        process = subprocess.Popen(
            "./run-tests.sh",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            encoding="utf-8",
        )
        while True:
            output = process.stdout.readline()
            if process.poll() is not None and output == "":
                break
            if output:
                self.stdout.write(output, ending="\r")
