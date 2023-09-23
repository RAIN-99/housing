#!/bin/sh
python3 model.py
python3 manage.py makemigrations  
python3 manage.py migrate

exec "$@"