# CHR Test

## Summary

Se realizaron extraciones de datos desde una api y  una pagina web las cuales se almacenaron en modelos con una base de datos postgresql, y finalmente se desplegaron en vistas con bootstrap 5.

## Installation

### Dependencies

Instala las dependencias en tu entorno virtual

```bash
$ pip install -r requirements.txt
```

### Migrate and Migrations

Crear la estructura de los `models`

```bash
$ python manage.py makemigrations
```

Migrela a su `BBDD`

```bash
$ python manage.py migrate
```

### Population Data

#### Utilize el siguientes comandos para insertar datos dentro de sus tablas:
 
Datos para tarea 1 

```bash
$ python manage.py load_test1
```
 
Datos para tarea 2

```bash
$ python manage.py load_test2
```

### Create Super User

Crea tu superusuario para ver los modelos en el admin

```bash
$ python manage.py createsuperuser
```

### Extra

Se deben remplazar las credenciales de su base de datos postgresql en el archivo 'settings.py'
