#!/bin/sh

# Collect static files (if applicable)
RUN python manage.py collectstatic --noinput

# wait for db
python manage.py wait_for_db

# Create new database migration files based on model changes
python manage.py makemigrations

# Apply database migrations to the database
python manage.py migrate --noinput

#create admin if doesn't exist
python manage.py initadmin

# Start your Django application
python manage.py runserver 0.0.0.0:8000
