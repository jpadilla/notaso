import os

from fabric.api import *
from fabric.contrib.project import rsync_project


env.user = 'ubuntu'
env.hosts = ['notaso.com']
env.use_ssh_config = True

BACKEND_DIR = '/home/ubuntu/backend/'


@task
def deploy():
    sync()

    install_requirements()

    manage('migrate')
    manage('collectstatic --noinput')

    service('gunicorn', 'restart')


@task()
def sync():
    RSYNC_EXCLUDES = [
        '.git',
    ]

    RSYNC_OPTS = [
        '-f', '":- .gitignore"'
    ]

    rsync_project(
        local_dir='./',
        remote_dir=BACKEND_DIR,
        exclude=RSYNC_EXCLUDES,
        extra_opts=' '.join(RSYNC_OPTS)
    )

    with lcd('static/react'):
        local('npm install')
        local('webpack')

        # Upload bundle.js
        key_name = 'build/bundle.js'
        remote_key_path = os.path.join('static/react', key_name)
        remote_path = os.path.join(BACKEND_DIR, remote_key_path)
        put(key_name, remote_path)


@task()
def install_requirements():
    with cd(BACKEND_DIR):
        run('venv/bin/pip install -r requirements.txt')


@task
def manage(command):
    with cd(BACKEND_DIR):
        run('venv/bin/python manage.py {}'.format(command))


@task()
def service(service, command):
    sudo('service {} {}'.format(service, command), shell=False)
