# Sistema de Gestión de Vehículos

## Descripción del Proyecto

Este proyecto es un sistema de gestión de vehículos desarrollado como parte del curso de Ingeniería de Sistemas en la Facultad de Ingeniería, Diseño y Ciencias Aplicadas. El objetivo principal es gestionar información relevante de una flota de vehículos, incluyendo datos técnicos, historial de mantenimiento y otras características específicas.

El proyecto está diseñado para ser colaborativo, utilizando Git y GitHub para el control de versiones. Cada miembro del equipo es responsable de desarrollar y agregar funcionalidades específicas al sistema, lo que incluye la creación de clases y métodos para manejar la información de los vehículos y sus mantenimientos.

## Integrantes del Equipo

- **Usuario A:** Juan pablo Ordoñez
- **Usuario B:** Juan Camilo Muñoz Barco
- **Usuario C:** Juan David Acevedo
- **Usuario D:** Jose Manuel Cardona
- **Usuario E:** Alejandro Quiñones

## Funcionalidades Principales

- **Usuario A**

- **Añadir implementacion de la clase Vehicle:** se implemento la clase Vehicle incluyendo los atributos "brand", "model", "year", "mileage", "current_status", "fuel_type" junto con sus respectivos métodos getter y setter.

- **filtro por rango de años:** se añadio la funcion "search_by_year_range" para que el sistema pueda buscar vehículos dentro de un rango de años. Ejemplo: `search_by_year_range: " main.search_by_year_range(2010, 2016)`

- **Usuario B**

  - **Historial de Mantenimiento:** Almacena la información sobre las reparaciones y mantenimientos realizados, como la fecha, descripción del servicio, kilometraje, costo, y nombre del mecánico.

  - **Filtrar Vehículos por Año en Orden:** Implementa un método para filtrar los vehículos por año, permitiendo obtener una lista de vehículos que cumplan con un año específico. Además, se ordena la lista de vehículos por año de forma ascendente o descendente. Ejemplo: `main.search_by_year(2015, "mayor")`

- **Usuario C**

  - **Lista de vehiculos:** : Implementará la clase "Main", que será el punto central de interacción del sistema, permitiendo gestionar una lista de vehículos. A través de esta clase, se podrán añadir vehículos a la lista y buscar vehículos por año

  - **Cambios Adicionales en la Clase Vehiculo**: Modifica la clase “Vehiculo”, para agregar un nuevo atributo “color”. Agrega los getter y setter pertinentes

- **Usuario D**

  - **Validaciones Adicionales para el Tipo de Combustible en la Clase Vehiculo**: Implementa validaciones adicionales en la clase Vehiculo, asegurando que el tipo de combustible solo pueda ser de una lista predefinida (por ejemplo, “Gasolina”, “Diesel”, “Eléctrico”).

  - **Agregar un nuevo atributo “potencia”**: Implementa un nuevo atributo llamado "potencia" en la clase Vehicle.py con sus getters y setters pertinentes.

- **Usuario E**

  - **Imprimir Vehiculos con sus caracteristicas:** Implementa método para la impresión de los vehículos registrados en el sistema, mostrando información relevante de cada uno de ellos, incluyendo la marca, el modelo, el año, el tipo de combustible, potencia y color.

## Instrucciones de Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <URL-del-repositorio>
   ```
2. **Navegar al directorio del proyecto:**
   ```bash
   cd nombre-del-proyecto
   ```

## Estructura del Proyecto

- **code/**: Contiene el código fuente del proyecto, incluyendo las clases y métodos desarrollados.
- **README.md**: Este archivo, que incluye la descripción del proyecto y las instrucciones necesarias.
- **CODESTYLE.md**: Documento que especifica las reglas de estilo de codificación acordadas por el equipo y el estandar de commits.
- **Informe.pdf**: Documento que detalla el proceso de desarrollo, incluyendo evidencia de commits, merges y resolución de conflictos.

## Requisitos del Sistema

- **Lenguaje de Programación:** Python
