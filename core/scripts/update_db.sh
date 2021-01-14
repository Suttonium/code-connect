#!/bin/bash

cd /home/$USER/django/codeconnect_project/

./manage.py makemigrations

if [ $? -eq 0 ]; then
  ./manage.py migrate
else
  echo "Skipping migrate command call because an error occurred."
fi

