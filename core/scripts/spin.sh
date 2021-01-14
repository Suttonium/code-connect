#!/bin/bash

cd /home/$USER/django/codeconnect_project/

echo "Starting PostgreSQL Database. Please enter valid credentials."
sudo service postgresql start

echo "Valid credentials received. Starting Python environment."
pipenv shell

echo "Setup complete."
