# Task management system built with Django
This is a simple, very basic task manager that I created in 2014, programmed in Python with Django. I haven't maintained it since then.

# Useful Links:
Video on how set the environment and demo (spanish) [https://www.youtube.com/watch?v=m6dmyg21Us8].
Mini installation guide with screenshots (spanish): [https://www.elgeneralfailure.com/2014/11/sistema-de-gestion-de-tareas-realizado.html].

# Prerequisites:
Download and install Django (pip install Django==1.7.1).

# Starting a Django instance:
- Create a deployment (django-admin.py startproject testing).
- Create admin users (python manage.py createsuperuser).
- Start a deployment (python manage.py runserver 0.0.0.0:8000).

# Setting up:
- Deploy the up (python manage.py startapp todo_list)
- Add the application's URL in the urls.py file of the deployment.
- Include the todo_list application in the INSTALLED_APPS list within the deployment's settings.py.
- Define PROJECT_PATH, STATIC_ROOT, TEMPLATE_DIRS, and STATICFILES_DIRS in the deployment's settings.py.
- Synchronize the list of static files: bash python manage.py collectstatic (respond with "yes")
- Create the project's tables in the deployment's database (bash python manage.py makemigrations todo_list python manage.py migrate).

# License :
Copyright (c) 2014 Sebastián José Moncho Maquet (aka Le Hamster ruso).
All rights reserved. Permission to use, copy, modify, and distribute this software and its documentation for any purpose is not granted without explicit prior permission from the copyright holder (comandantecobra@gmail.com). If you're a developer, I don't mind if you copy and paste parts of my code, just make sure to include me in the acknowledgments of your credits.
