#!/bin/sh
set -o errexit
set -o nounset

python /app/manage.py collectstatic --noinput
python /app/manage.py migrate
/usr/local/bin/gunicorn {{cookiecutter.project_slug}}.wsgi --bind 0.0.0.0:8000 --chdir=/app
