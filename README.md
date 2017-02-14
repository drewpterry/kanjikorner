kanjikorner
===========
A spaced-repitition based web application for learning Japanese vocabulary using django and vue.js . View at [kanjisama.com](kanjisama.com) .

```pip install virtualenv```

Create virtual environment where venv is the directory
```virtualenv venv ```

```cd venv/bin/activate ```

inside venv directory run:
``` git clone https://github.com/drewpterry/kanjikorner.git kanjisite ```


inside kanjisite run:
```pip install -r requirements.tx ```

make sure to change your database settings in settings.py 

``` python manage.py makemigrations```

``` python manage.py migrate```


Run the server and check localhost:8000 to make sure the app is running
``` python manage.py runserver ```
