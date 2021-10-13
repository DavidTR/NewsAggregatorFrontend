# NewsAggregator frontend

## Creción de un proyecto Django desde cero.

Se recomienda crear un entorno virtual (virtualenv) para instalar las dependencias del proyecto sin que queden ligadas al intérprete del sistema. Por ahora sólo será necesario instalar Django:

```
$ virtualenv -p python3 news_aggregator_frontend
$ pip install Django
```

### Estructura básica

* Primero, hay que crear la estructura básica del proyecto. Se supone que el directorio actual es el elegido para ubicar los archivos de la aplicación:

```
$ django-admin startproject news_aggregator
```

* Una vez creada la estructura básica, hay que crear una aplicación. En este caso, como sólo se creará una (no habrá múltiples aplicaciones), la siguiente sentencia se ejecutará sólo una vez:

    - Nota: El virtualenv deberá estar activado y el directorio deberá ser el raíz del proyecto Django, creado en el paso anterior.

```
$ python manage.py startapp frontend
```

Al ejecutar este comando, se creará otra estructura de archivos distinta a la anterior que contendrá los elementos básicos para la nueva aplicación.

**NOTA**: A partir de ahora se usará esta estructura de archivos como referencia para indicar qué cambios aplicar.

### Modificar configuración en settings.py

* Se recomienda modificar el archivo `news_aggregator/settings.py` de la siguiente manera:

    1. Modificar los valores de las constantes `TIME_ZONE`, `LANGUAGE_CODE` según sea necesario. Para esta aplicación, los valores por defecto son los adecuados.
    2. Agregar `STATIC_ROOT` para su posterior uso en los templates:
    ```
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```
    3. Agregar los dominios necesarios a #`ALLOWED_HOSTS`. Por ejemplo, si el proyecto se va a subir a `pythonanywhere.com`, agregar la cadena `"pythonanywhere.com"` a la lista `ALLOWED_HOSTS`.


* Configurar la conexión a base de datos, modificando la constante `DATABASES`. En nuestro caso, como el SGBD será MySQL, se deberá aplicar la siguiente configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_DATABASE_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

Los valores se fijarán mediante variables de entorno.

Será necesario instalar la dependencia `mysqlclient` para que Django pueda conectar con la base de datos.

### Crear base de datos Django

Cualquier aplicación Django necesita de una base de datos básica para funcionar. Los elementos de base de datos a crear dependen de las aplicaciones instaladas (ver la constante `INSTALLED_APPS` en el archivo `news_aggregator/settings.py`) El siguiente comando la creará para nuestro proyecto:

```
$ python manage.py migrate
```

### Arrancar el servidor web

Django incorpora un servidor web que es el que se emplea para lanzar la aplicación y proveer de acceso a ella través de cualquier navegador. Este servidor se puede arrancar (en el puerto 8000 por ejemplo) ejecutando la siguiente sentencia:

```
$ python manage.py runserver 127.0.0.1:8000
```

Recordar que es necesario cargar las variables de entorno para que Django pueda conectar con la base de datos previamente.

Este script también se puede ejecutar desde PyCharm, cargando las variables de entorno, fijando `manage.py` como script a ejecutar y pasando las opciones `runserver 127.0.0.1:8000` como parámteros.

### Instalar nueva aplicación

Aunque los archivos se han creado correctamente, Django no conoce de la existencia de la apliación `frontend` creada al ejecutar `python manage.py startapp frontend`. Para remediar esto, bastará con agregar la siguiente línea a la cosntante `INSTALLED_APPS` de `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend.apps.FrontendConfig' # Línea añadida
]
```

### Panel de administración

Para acceder al panel de administración antes hay que crear una cuenta de superusuario. Para ello, ejecutar: 

```
$ python manage.py createsuperuser
```

Y seguir las instrucciones.

Una vez el usuario esté creado, acceder a `127.0.0.1:8000/admin` e ingresar las credenciales.

### URLs

Las URLs en Django permiten la navegación entre las diferentes secciones de la aplicación, asociando vistas a direcciones URL únicas.

En nuestro caso, la aplicación `frontend` se encargará de gestionar toda esta lógica, por lo que habrá que modificar el archivo `news_aggregator/urls.py` para que quede como sigue:

```python
"""news_aggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls'))
]
```

Ahora debemos crear el archivo `frontend/urls.py` y agregar al menos un patrón URL. El archivo quedará, por ahora, de la siguiente manera:

```python
# -*- encoding:utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Por ahora esta vista no tiene lógica ninguna, se usa como _placeholder_:

```python
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.


def index(request: WSGIRequest):
    return render(request, 'index.html')

```

El archivo `index.html` debe existir y estar ubicado en `frontend/templates`. 

Además, de cara a un futuro cercano, se crearán los directorios `static/css` y `static/icons`, que albergarán archivos CSS e iconos, respectivamente.

La estructura de archivos (para refrescar) deberá parecerse a:

```
├── LICENSE
├── README.md
├── installation_notes.md
└── news_aggregator_frontend
    ├── news_aggregator
    │   ├── frontend
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── migrations
    │   │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── static
    │   │   │   ├── css
    │   │   │   └── icons
    │   │   ├── templates
    │   │   │   └── index.html
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── manage.py
    │   └── news_aggregator
    │       ├── __init__.py
    │       ├── asgi.py
    │       ├── settings.py
    │       ├── urls.py
    │       └── wsgi.py
    └── util
        └── load_env.sh
```


