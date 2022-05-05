# Flask Mailer
## Aplicación que envía y almacena correos

Aplicación web sencilla que se encarga de enviar y almancenar correos en una Base de Datos. El servicio para enviar cada uno de los correos es gracias a SendGrid, pues no requiere de un servidor de correos.

# Preperación del Entorno
Antes de iniciar la ejecución de la aplicación es necesario dar de alta las variables del entorno.
Para que la aplicación funcione, Flask debe reconocer estas variables.
Las variables de entorno se encuentran especificadas dentro del archivo: `__init__.py`

Donde:

> `FLASK_APP` : Es el nombre de la aplicación, en este caso es el nombre que contiene toda la app, la carpeta 'to_do'.
"

> `FLASK_ENV` : En caso de solo usar al aplicación como modo desarrollo.

> `FLASK_DATABASE_HOST` : Nombre o IP para acceder a la Base de Datos.

> `FLASK_DATABASE_PASSWORD` : Contraseña para acceder a la Base de Datos.

> `FLASK_DATABASE_USER` : Usuario para acceder a la Base de Datos.

> `FLASK_DATABASE` : Nombre de la Base de Datos.

> `SENDGRID_KEY` : API Key obtenida del servicio de SendGrid.

> `FROM_EMAIL` : Email dado de alta dentro del servcio de SendGrid como un "Sender".


En caso de ser la primera vez en usar la aplicación es necesario ejecutar el comando:

> `flask init-db` : Este comando ha sido dado de alta en `db.py` y contiene los esquemas necesarios para purgar, limpiar e inicilizar la Base de Datos.

Este comando solo debe ser ejecutado la primera vez ya que de lo contrario cada que sea llamado realizará las acciones mencionadas con anterioridad.

# ¿Qué Packages son necesarios?
Todos los recursos usados para el desarrollo se encuentran en: `requirements.txt`
> `pip install -r requirements.txt`

# Screenshots
<img src="app\doc\img\index.png">

<img src="app\doc\img\create.png">

# Recursos
Flask: https://flask.palletsprojects.com/en/2.0.x/

Secrets: https://docs.python.org/3/library/secrets.html

MySQL Connector: https://dev.mysql.com/doc/connector-python/en/

Click: https://click.palletsprojects.com/en/8.0.x/

SendGrid: https://docs.sendgrid.com/for-developers/sending-email/v3-python-code-example
