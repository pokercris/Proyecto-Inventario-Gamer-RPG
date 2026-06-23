# Sistema de Inventario Gamer RPG

Este programa es una aplicación de consola interactiva desarrollada en Python que funciona como un sistema de gestión para personajes de videojuegos RPG. Permite a los usuarios administrar su propio inventario de héroes de forma persistente durante la ejecución de la app.

## Funcionalidades (CRUD)

Este proyecto incluye las siguientes funcionalidades a través de un menú interactivo:

* **Create**: Permite agregar un nuevo personaje al sistema validando que su nombre sea único, que los campos no estén vacíos y asignando puntos de daño numéricos.
* **Read**: Muestra la lista completa de personajes registrados detallando sus atributos de forma ordenada y legible.
* **Update**: Modifica los datos de un personaje existente (clase, rareza o daño) buscando por su nombre único.
* **Delete**: Elimina un personaje del sistema de manera definitiva a través de su nombre.

## Requisitos Técnicos Aplicados

* Uso de listas para el almacenamiento global y diccionarios para la estructura de cada personaje.
* Uso de funciones independientes y debidamente comentadas para cada operación.
* Validaciones estrictas y manejo de excepciones (`try/except`) para evitar caídas del programa por datos erróneos.
* Validación de duplicados y campos vacíos.

## Autor

* **Cristian Patricio Contreras Sandoval**
* FPY1101 Fundamentos de Programación
