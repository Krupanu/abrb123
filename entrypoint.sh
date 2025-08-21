#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgreSQL started"

python manage.py makemigrations --no-input

python manage.py migrate --no-input

exec "$@"