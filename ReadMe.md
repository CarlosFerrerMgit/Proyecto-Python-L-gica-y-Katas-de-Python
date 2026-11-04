# 🐍 Proyecto Python: Lógica y Algoritmos sobre Katas de Programación

> **Módulo 5: Python**  
> **Python 3.12+ (Entorno de desarrollo en VS Code)**  
> **Fecha: Noviembre 2026** 

## 📌 1. Descripción del Proyecto

Este repositorio contiene la resolución limpia y optimizada de los 40 ejercicios prácticos (Katas 1 a 41, con salto del ejercicio 35 en el enunciado oficial de ThePower) diseñados para afianzar el razonamiento algorítmico y las capacidades técnicas del lenguaje Python.

El proyecto demuestra el dominio de la sintaxis fundamental, estructuras de datos, programación funcional con funciones de orden superior (map, filter, reduce), manejo estructurado de excepciones y programación orientada a objetos (POO), cumpliendo de forma estricta los estándares de calidad y estilo de la industria (PEP 8).

## 🛠️ 2. Metodología y Pasos Seguidos

### A. Pasos Seguidos durante el Proyecto

* **Configuración del Entorno de Trabajo en VS Code:** Configuración del intérprete de Python y verificación del gestor de paquetes (`pip`).

* **Instalación de extensiones clave:** `Python, Pylance, Jupyter, autoDocstring y Black Formatter`.

* **Diseño y Testeo Iterativo:** Desarrollo y prueba celda a celda en un entorno interactivo tipo notebook (`katas_python.ipynb`), evaluando casos límite, listas vacías, divisiones por cero y argumentos no válidos.

### B. Competencias Técnicas Demostradas en las Katas

* **Tipos de Datos y Métodos Nativos de Cadena:**
  * Uso de métodos de inspección y transformación de strings (`.lower()`, `.upper()`, `.split()`, `.replace()`, `.strip()`, `.startswith()`).
  * Indexación y rebanado avanzado (*slicing*) para el enmascaramiento de datos sensibles conservando caracteres finales (`texto[-4:]`).
* **Estructuras de Datos y Complejidad Temporal:**
  * **Diccionarios:** Manejo del método `.get(clave, 0)` para conteos y acumulación de frecuencias sin disparar errores `KeyError`.
  * **Listas y List Comprehensions:** Transformación y filtrado sintético en una sola línea con alta eficiencia y legibilidad.
  * **Conjuntos (`set`):** Eliminación de elementos duplicados y optimización de comprobaciones de pertenencia (`item in set`).
  * **Tuplas:** Agrupamiento de respuestas inmutables y retorno de múltiples salidas en funciones.
* **Programación Funcional y Funciones de Orden Superior:**
  * **`lambda`:** Funciones anónimas para operaciones directas (cálculo de potencias, restos con `%`, sumas paramétricas).
  * **`map()`:** Transformaciones diferidas elemento a elemento y mapeo sincronizado en paralelo sobre dos o más listas (`map(lambda x, y: x - y, lista1, lista2)`).
  * **`filter()`:** Extracción condicional de subconjuntos mediante evaluación de predicados booleanos.
  * **`reduce()`:** Reducción de secuencias a un único valor escalar (cálculo de factoriales posicionales, diferencias acumuladas y productos continuos).
* **Control de Excepciones y Robustez:**
  * Captura diferenciada con bloques `try / except / else` para responder ante errores de tipo (`ValueError`) y aritméticos (`ZeroDivisionError`).
  * Creación y lanzamiento de excepciones personalizadas (`class ListaVaciaError(Exception)`) para validar estructuras de entrada.
* **Programación Orientada a Objetos (POO):**
  * Modelado de entidades del mundo real mediante atributos de estado y métodos de mutación (`class Arbol`).
  * Lógica transaccional segura con validaciones cruzadas entre múltiples instancias y control de saldos (`class UsuarioBanco`).
* **Modularidad y Funciones Variádicas:**
  * Desempaquetado dinámico posicional mediante `*args` para construir funciones despachadoras u orquestadoras (`procesar_texto`).

## 📁 3. Estructura del Proyecto
```text

├── docs/
│   ├── EnunciadoDataProjectPython.pdf               # Enunciados de las katas a realizar
│   ├── katas_python.ipynb                           # Cuaderno interactivo
│   └── katas_python.py                              # Script final
└── README.md                                        # Documentación principal del repositorio
```

 ## 🤝 Contribuciones

 Las contribuciones, sugerencias y mejoras son bienvenidas. 
 
 ## 👤 Autor
 
 Carlos A. Ferrer Mendoza — Ingeniero Electrónico | MBA y Alumno del Máster en Data & Analytics (ThePower Business School).
 www.linkedin.com/in/carlos-ferrer-mendoza-835294292