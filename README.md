# budget_app
<br>
The purpose of this project is to demonstrate an understanding of working with an SQL database as well as object-oriented programming and design patterns.  All development was done on Ubuntu 20.04 using the Django framework along with Postgres for the database.
<br>

## Setup
Environment Setup

    sudo apt install -y python3-pip
    sudo apt install build-essential libssl-dev libffi-dev python-dev
    sudo apt install -y python3-venv

Postgres Installation
    
    sudo apt install postgresql postgresql-contrib
    sudo apt install libpq-dev
    sudo su - postgres
    psql

Postgres Configuration

    CREATE DATABASE budget_appdb;
    CREATE USER dbuser WITH PASSWORD 'password';
    ALTER ROLE dbuser SET client_encoding TO 'utf8';
    ALTER ROLE dbuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE dbuser SET timezone TO 'UTC';
    GRANT ALL PRIVELAGES ON DATABASE budget_appdb TO dbuser;
    ALTER USER dbuser CREATEDB;
    \q
    exit
    
Create a virtual environment

    mkdir budget_project
    cd budget_project
    python3 -m venv testenv
    source testenv/bin/activate

Install Django and some other packages that we'll need

    pip3 install wheel
    pip3 install django psycopg2
    pip3 install python-dateutil
    pip3 install yfinance
    
## Create a Django Project

    django-admin.py startproject budget_site .

The directory structure will look like this currently:

    .
    ├── manage.py
    └── budget_site
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
