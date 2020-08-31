#!/bin/bash

echo "Starting Virtual Environment"
source ./amol/bin/activate
echo "Collecting Static Files"
python3 manage.py collectstatic --noinput
echo "Checking For Database Changes"
python3 manage.py makemigrations amol_blog
python3 manage.py migrate
echo "Creating SuperUser"
python3 manage.py shell -c "from django.contrib.auth.models import User; \
                           User.objects.create_superuser('aanand',
                           'admin1@example.com', '1234')"
echo "Starting Django Server"
python3 manage.py runserver 0.0.0.0:8000

