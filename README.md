# djangoDemo

- Installing Python and Django
```
conda env list
conda create -n django
conda activate django
conda install python=3.8
conda install Django=3.2.3
conda env list
```

- Creating Django
```
django-admin startproject djangoDemo
cd to the djangoDemo
python manage.py runserver
Hit in Browser
http://127.0.0.1:8000/
```

- Create a app
```
Open in PyCharm -> Using the above conda envronment
python manage.py startapp hello_app
```
