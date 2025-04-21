#!/bin/bash

# Flush Database
python3 manage.py flush --no-input

# Migrate Database
python3 manage.py makemigrations
python3 manage.py migrate

# Create Superuser
python3 manage.py createsuperuser --noinput --username admin --email admin@localhost.com

# Create more users
http POST 127.0.0.1:8000/register/  username=ali    password=8423904@aut  email=ali@yahoo.com
http POST 127.0.0.1:8000/register/  username=ahmad  password=8423904@aut  email=ahmad@yahoo.com
http POST 127.0.0.1:8000/register/  username=abdol  password=8423904@aut  email=abdol@yahoo.com

# Create Users and test
# export PGPASSWORD="842390"
# psql -h localhost -U postgres -d template1 -c "DROP DATABASE test_tms_db;"
# python3 manage.py test tms.tests.TestUsers