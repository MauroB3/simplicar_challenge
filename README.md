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

| Path | Method | Body example |
| --- | --- | --- |
| /domaind/api/library/**{id}** | GET | - |
| /domain/api/library/**{id}** | POST | ```json { "name": "William Mendez" } ``` |
| /domain/api/library/ | PUT | ```json { "name": "William Mendez" } ``` |

</details>

<details>
<summary> Book  </summary>

| Path | Method | Body example |
| --- | --- | --- |
| /domaind/api/book/**{id}** | GET | - |
| /domain/api/book/**{id}** | POST | ```json     {
        "title": "Libro modificado",
        "author": 61,
        "libraries": [1, 2]
    } ``` |
| /domain/api/book/ | PUT | ```json     {
        "title": "Nuevo libro",
        "author": 61,
        "libraries": [1, 2]
    } ``` |
| /domain/api/book/search?text=**{texto}** | GET | - |
</details>


