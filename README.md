# Lab 27

## Django Models: Snacks

### Author

- Ella Svete
- I worked on this with Eden Brekke

### Setup

- python3 -m venv .venv
- source .venv/bin/activate
- pip install django
- django-admin startproject snack_tracker_project
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp snacks
- Make TUV and add to settings
- python manage.py makemigrations snacks
- python manaage.py createsuperuser
- python manage.py runserver

### Tests

- to run tests import the class Snacks
- import django.test import TestCase
- python manage.py test to run tests

- I referenced the tests provided in today's demo
