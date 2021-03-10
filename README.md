# simplicar_challenge

# Descripcion

La api esta desarrollada con django-rest-framework. A su vez, utilize JWT para proteger un endpoint de la api (detallado mas abajo).
Desarrollado utilizando python 3.7.7.

# Preparando el entorno

Primero instalamos las librerias adicionales al proyecto:
```
$ pip install djangorestframework
$ pip install django-rest-framework-simplejwt
```
Luego en el archivo settings.py se deben configurar los parametros de la base de datos. Hecho esto hay que realizar las migraciones y cargar los datos iniciales:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata book/fixtures/data.json
```
Finalmente iniciamos la app con:
```
$ python manage.py runserver
```

# Endpoints de la API

<details>
<summary> Library  </summary>

  - Path: /domain/api/library/**<id>**
    Method: GET

  - Path: /domain/api/library/**<id>**
    Method: POST
    Body example:
    ```
    {
      "name": "William Mendez"
    }
    ```

</details>

