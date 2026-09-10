# 📚 Sistema de Gestión de Biblioteca (Biblioteca Magic)

Aplicación interactiva de consola desarrollada en **Python** que permite gestionar el inventario de una biblioteca mediante un sistema completo de **CRUD** (Crear, Leer, Actualizar y Eliminar), con control de acceso por usuario/contraseña y persistencia de datos en formato **JSON**.

Este proyecto fue desarrollado como trabajo integrador para la certificación de **Programación Inicial en Python** impartida por la *Agencia de Habilidades para el Futuro - Codo a Codo 4.0*.

---

### 🚀 Funcionalidades Principales

* 🔐 **Autenticación de Usuarios:** Sistema de inicio de sesión con credenciales validadas y límite de 3 intentos fallidos de seguridad.
* 📋 **Listado de Libros:** Muestra el catálogo de obras organizadas en tablas tabuladas (`ID`, `Título`, `Autor` y `Precio`).
* 🔍 **Búsqueda Dinámica:** Búsqueda inteligente que permite consultar libros por su número de **ID** o por **Título** (con soporte para insensibilidad a mayúsculas/minúsculas).
* ➕ **Alta de Libros (Create):** Incorporación de nuevas obras asignando automáticamente un ID incremental y formateando el texto para mantener la prolijidad visual.
* ✏️ **Edición de Libros (Update):** Modificación del título, autor o precio de cualquier libro registrado.
* 🗑️ **Eliminación de Libros (Delete):** Borrado de registros del catálogo.
* 💾 **Persistencia en JSON:** Guardado y lectura automática en el archivo `biblioteca.json` para mantener la información actualizada entre ejecuciones.
* 🎨 **Interfaz de Consola:** Uso de la librería `colorama` y alineaciones de texto para brindar una experiencia de usuario clara e intuitiva en la terminal.

---

### 🛠️ Tecnologías y Conceptos Aplicados

- **Lenguaje:** Python 3.x
- **Librerías Utilizadas:** `json` (persistencia de datos) y `colorama` (estilos e interfaz visual en terminal).
- **Conceptos de Programación:** 
  - Estructuras de control de flujo (`while`, `if/else`, `match-case`).
  - Funciones modulares y manejo de variables globales/locales.
  - Estructuras de datos compuestas (Listas y Diccionarios).
  - Métodos de string (`.ljust()`, `.lower()`, `.title()`, `.isdigit()`).
  - Manejo de archivos y excepciones (`try / except FileNotFoundError`).

---

### 👥 Trabajo en Equipo y Metodología

Proyecto desarrollado de forma colaborativa durante el programa Codo a Codo 4.0, donde se ejercitaron habilidades técnicas y competencias blandas:
- Coordinación y resolución en equipo de lógica de programación.
- Adaptabilidad a roles, gestión del tiempo y buenas prácticas de legibilidad de código.

---

### ⚙️ Cómo Ejecutar el Proyecto

1. Clonar el repositorio:
   git clone [https://github.com/J-code-bit/Python_gestion_biblioteca.git](https://github.com/J-code-bit/Python_gestion_biblioteca.git)

2. Ingresar a la carpeta del proyecto:
   cd Python_gestion_biblioteca

3. Instalar la dependencia de colorama:
   pip install colorama

4. Ejecutar el programa:
   python Gestion_biblioteca.py

---

> 💡 **Datos de prueba para el login:**  
> - **Usuarios permitidos:** `jime`, `marcos`, `luciano`, `maga`, `miche`  
> - **Contraseñas:** `000` (para jime), `123` (para marcos), `456` (para luciano)
 

   
