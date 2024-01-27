#!/usr/bin/env bash

python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 crowdfunding.wsgi

fly volumes create -a crowdfunding_back_end1990 -r syd --size 1 dbvol
