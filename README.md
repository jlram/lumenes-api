# lumenes-api


## 1. Primeros pasos y requisitos para el desarrollo

### Versión de Python: 3.7.1

- (Una vez dentro de la carpeta del proyecto lo suyo es) crear un virtualenv. Por qué? 
<a href="https://yasoob.me/2013/07/30/what-is-virtualenv/">Por esto</a>.

Básicamente tenemos que hacer

```
pip install virtualenv

python -m venv env

source env/bin/activate

# o en algunos casos si en vez de carpeta 'bin' teneis 'Scripts'

source env/Scripts/activate
```

Ya está, recordad iniciar el entorno virtual siempre antes de poneros a currar para evitar llenar el pc de librerias y frameworks.

- Con el venv ya ready, para instalar todas las librerias necesarias para arrancar el proyecto tan solo tendremos que volver a la carpeta raiz y hacer:

```
pip install -r requirements.txt
```

Este comando leerá los requisitos que he escrito en el archivo y os los instalará en el venv que tengáis activado.

- Aplicar los cambios de los modelos de Django a la Base de Datos:

Este punto es importante ya que es algo que se tendrá que hacer siempre que querramos pasar los cambios de las migraciones a la bases de datos.

```
python manage.py migrate
```

Las migraciones, por asi decirlo son los archivos en los que se reflejan que cambios se han hecho en la base de datos. Se generan haciendo `python manage.py makemigrations`.
Esto es muy importante ya que cada vez que querramos aplicar nuestros cambios en la base de datos tendremos que crear un archivo de migraciones con `makemigrations` y luego migrar con `migrate`. De lo contrario no veremos ningún cambio. De todas maneras esto es un poco introductorio, ya llegaremos a eso.

- Usuario administrador

Una vez aplicados los cambios con `migrate` a la base de datos, ya tendremos, por ejemplo, lista la tabla de Usuarios, asi que es momento de crear vuestro SuperUser, con `python manage.py createsuperser`. Saldrán unos cuando diálogos para que rellenéis la info y ready.

- Arrancar el servidor

Una vez hecho todo esto, ejecutando `python manage.py runserver` arrancaréis el servidor e introduciendo 127.0.0.1:8000 en vuestro navegador tendriais que ver la página principal del proyecto :) Si quereis jugar a ser dios un rato podéis probar a poner detras de la url /admin y trasteais el panel de administración. salu2.




