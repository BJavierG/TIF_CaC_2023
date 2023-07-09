# TIF_CaC_2023
Repo del Trabajo Integrador Final del curso de FullStack Python de Codo a Codo 2023

# Trabajo Práctico - Aplicación de CRUD de Productos

Este proyecto consiste en el desarrollo de una pagina informativa de una feria urbana con su respectivo canal de ventas online (en desarrollo)
y una aplicación web para la gestión de productos utilizando el framework Django y una API REST.
El objetivo principal es permitir realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los productos almacenados en la base de datos.

## Características principales

- La aplicación CRUD cuenta con las siguientes funcionalidades:
  - Listar todos los productos existentes.
  - Crear nuevos productos con información como código, nombre, descripción, precio y una imagen.
  - Ver los detalles de un producto específico.
  - Actualizar la información de un producto existente.
  - Eliminar un producto de la base de datos.


- La interfaz de usuario ha sido desarrollada utilizando HTML, CSS y templates de Django para lograr una experiencia amigable y fácil de usar.

## Configuración y ejecución

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

1. Clona este repositorio en tu máquina.

2. Crea un entorno virtual e instala las dependencias necesarias utilizando el comando `pip install -r requirements.txt`.

3. Configura la base de datos en el archivo `settings.py`. Asegúrate de tener una base de datos configurada y actualiza las credenciales de conexión según sea necesario.

4. Ejecuta las migraciones para crear las tablas en la base de datos utilizando el comando `python manage.py migrate`.

5. Inicia el servidor de desarrollo con el comando `python manage.py runserver`.

6. Abre tu navegador web y visita `http://localhost:8000` para acceder a la aplicación.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. 
Si encuentras algún problema, tienes alguna sugerencia de mejora o te gustaría agregar nuevas funcionalidades,
por favor, siéntete libre de crear un issue o enviar un pull request.

