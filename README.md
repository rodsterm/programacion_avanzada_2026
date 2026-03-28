# 🚀 Portafolio de Programación Avanzada - IACC

¡Bienvenido al repositorio de **Programación Avanzada**! Este repositorio contiene una serie de proyectos estudiantiles desarrollados a lo largo de las semanas correspondientes al ramo **Programación Avanzada**, impartido por el **Instituto Profesional IACC**. Los aplicativos aquí documentados abarcan de forma progresiva desde los conceptos fundamentales del lenguaje Python hasta el desarrollo de interfaces gráficas interactivas y la conexión con bases de datos relacionales.

## 📂 Estructura del Repositorio

A continuación se detalla el contenido y el propósito principal de cada uno de los proyectos y carpetas dentro de este repositorio:

### 🛠️ [Proyecto_01] - Lógica Condicional y Ciclos
Un programa de iteración y cálculo de precios (`Proyecto_01.py`) enfocado en una tienda de neumáticos "Rueda Fácil". Su propósito es definir un precio unitario dinámico mediante condicionales dependiendo de la cantidad comprada, manejando ciclos `while` y `for` para la atención de múltiples clientes y cálculo de cobros.

### 🧮 [Proyecto_02] - Funciones y Recursividad
Script interactivo (`Proyecto_02.py`) basado en menús que aplica funciones matemáticas personalizadas. Permite calcular descuentos por volumen de licencias de software y el volumen real de una esfera. Además, sirve como escenario educativo para comprender el concepto de recursividad al implementar un generador de factoriales.

### ⚠️ [Proyecto_03] - Manejo Lógico de Excepciones
Un sistema enfocado en la integridad de los datos de un inventario frutícula (`Proyecto_03.py`). Su principal valor radica en las validaciones con bloques `try - except`, gestionando errores intencionados (`ValueError`) para prevenir ingresos con cantidades negativas e inconsistencias en la sustracción del inventario diario.

### 📊 [Proyecto_04] - Estructura de Datos (Conjuntos)
Simulador analítico del registro de un Museo (`Proyecto_04.py`). Expone el comportamiento eficiente y el poder de la estructura _Sets_ en Python. Aplica la matemática de teoría de conjuntos (Uniones, Intersecciones y Diferencias) para depurar visitantes duplicados y cruzar asistencias entre distintas salas de exposición.

### 📦 [Proyecto_05] - Modularidad y Paquetes
Sistema de recursos humanos de "Orange Solutions". Este proyecto rompe el esquema monolítico dividiendo la lógica de la aplicación en múltiples módulos orquestados (`main.py`, `empleados.py`, `calculos.py`, `beneficios.py`). Enseña las mejores prácticas paramétricas, el uso de la clase nativa `datetime` y la separación de responsabilidades en la ingeniería de software.

### 💾 [Proyecto_06] - Persistencia de Datos (Archivos JSON)
Sistema administrativo bibliotecario de consola (`Proyecto_06.py`). Implementa el análisis, la conversión y manipulación de archivos y serialización JSON. Almacena en crudo toda la actividad, garantizando que el catálogo de libros o autores no se destruya al finalizar el ciclo de ejecución del programa sino que persista en `libros.json` y `autores.json`.

### 🖥️ [Proyecto_07] - Interfaces Gráficas (GUI) con Tkinter
Aplicación visual interactiva (`Proyecto_07_final.py`). Una interfaz gráfica robusta y nativa desarrollada bajo la librería Tkinter para el registro de activos de la "Biblioteca SaberX". Demuestra el uso de la mayoría de componentes (Widgets) que conforman una UI estándar: *Frames, Labels, Text Entries, Dropdowns (OptionMenu), Checkbuttons, Radiobuttons*, y diálogos en forma de ventanas emergentes (messagebox).

### 🗄️ [Proyecto_08] - Sistema CRUD con Base de Datos (MySQL)
La culminación del aprendizaje (`Proyecto_08_final.py`). En esta etapa se une el frontend de Tkinter con el backend de una base de datos relacional MySQL. Construye un sistema transaccional íntegro CRUD (Crear, Leer, Actualizar, Borrar) para gestionar un catálogo de Videojuegos, realizando *queries* SQL directos desde el código por medio del conector nativo de MySQL.


---

## ⚙️ Tecnologías y Módulos Utilizados
* **Lenguaje:** Python 3.x
* **Interfaces Gráficas:** `tkinter`
* **Conectividad a Base de Datos:** `mysql-connector-python`
* **Formatos de Transporte:** `json`
* **Módulos Incorporados:** `datetime`, `math`, `os`

## 🚀 Cómo Ejecutar cada Módulo

Al ser proyectos independientes, la forma más sencilla de ejecutarlos es iniciar una terminal, dirigirse al directorio deseado y arrancar el intérprete de Python:

```bash
cd Proyecto_02
python Proyecto_02.py
```

> **📌 Consideraciones Especiales Importantes:** Para la correcta ejecución del **Proyecto 08** es imprescindible tener montado un servidor relacional de MySQL o MariaDB (como XAMPP, WAMPP) corriendo en el puerto 3306. Se exige además la inyección de la base de datos `semana8` y la tabla *Videojuegos*. Asegúrese finalmente de instalar las dependencias con: `pip install mysql-connector-python`.

---
*Este repositorio recopila de manera profesional el avance logrado durante la ruta del curso **Programación Avanzada** de **IACC**. ¡Siéntete libre de explorar el código! 👨‍💻👩‍💻*

---
<div align="center">
  <i>Hecho con amor por yo ❤️</i>
</div>
