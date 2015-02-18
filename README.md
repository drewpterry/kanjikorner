kanjikorner
===========
This is a new project.

```pip install virtualenv```

Create virtual environment where venv is the directory
```virtualenv venv ```

```cd venv/bin/activate ```

```pip install -r requirements.tx ```

make sure to change your database settings in settings.py 

``` python manage.py syncdb ```

``` python manage.py migrate```


Run the server and check localhost:8000 to make sure the app is running
``` python manage.py runserver ```

close the server

```python manage.py shell```

inside shell run to populate database
``` execfile('xmltodict/jsonupload.py') ```



