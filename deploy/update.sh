#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/bookme_api'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart bookme_api

echo "DONE! :)"