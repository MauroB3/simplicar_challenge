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
Como no tenemos un sistema de login, necesitamos crear algun tipo de usuario para usar mas adelante en los endpoints protegidos con JWT. Vamos a crear un superusuario con el comando que nos proporciona django:
```
$ python manage.py createsuperuser
```

Finalmente iniciamos la app con:
```
$ python manage.py runserver
```

# Envio de email

Para que se realize el envio de email al momento de crear un lead es necesario configurar los parametros **EMAIL_HOST_USER** y **EMAIL_HOST_PASSWORD** en el archivo settings.py.

# Endpoints de la API
### Click para expandir

<details>
<summary> Library  </summary>

| Path | Method | Body example |
| --- | --- | --- |
| /domaind/api/library/**{id}** | GET | - |
| /domain/api/library/**{id}** | POST | ```{ "name": "William Mendez" } ``` |
| /domain/api/library/ | PUT | ```{ "name": "William Mendez" } ``` |

</details>

<details>
<summary> Book  </summary>

| Path | Method | Body example |
| --- | --- | --- |
| /domaind/api/book/**{id}** | GET | - |
| /domain/api/book/**{id}** | POST | ```{ "title": "Libro modificado", "author": 61, "libraries": [1, 2] } ``` |
| /domain/api/book/ | PUT | ```{ "title": "Nuevo libro", "author": 61, "libraries": [1, 2] } ``` |
| /domain/api/book/search?text=**{texto}** | GET | - |
</details>

<details>
<summary> Author </summary>

| Path | Method | Body example |
| --- | --- | --- |
| /domaind/api/author/**{id}** | GET | - |
| /domain/api/author/**{id}** | POST | ```{ "first_name": "Lisa", "last_name": "Rivera" } ``` |
| /domain/api/author/ | PUT | ```{ "first_name": "Nuevo", "last_name": "Autor" } ``` |
</details>

<details>
<summary> Leads  </summary>

| Path | Method | Body example |
| --- | --- | --- |
| /domaind/api/leads/ | POST | ``` { "email": "reekremag@gmail.com", "fullname": "Mauro", "phone": "1115161718", "library": 1 } ``` |


Esta ruta esta protegida con JWT. Para poder utilizarla es necesario incluir en el head un token de acceso. Para obtener el token es necesario hacer un POST al path **/domain/api/token/** con el usuario y contraseña generado al principio (ya que no hay implementado un login), como se ve en la imagen:

![Imagen 1](/images/imagen_1.jpg)

Generado el token, podemos hacer el POST a **/domaind/api/leads/** tal como esta en la tabla de arriba, incluyendo el token en el header:

![Imagen 2](/images/imagen_2.jpg)

Este token expira cada 5 minutos, para obtener un nuevo token hay que hacer un POST al path **/domain/api/token/refresh/** indicando el token refresh que obtuvimos en el primer paso:

![Imagen 3](/images/imagen_3.jpg)

</details>


