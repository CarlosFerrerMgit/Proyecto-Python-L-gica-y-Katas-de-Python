# 🐍 Proyecto Python: Lógica y Algoritmos sobre Katas de Programación

> **Módulo 5: Python**  
> **Python 3.12+ (Entorno de desarrollo en VS Code)**  
> **Fecha: Noviembre 2026** 

## 📌 1. Descripción del Proyecto

Este repositorio reúne la resolución de las **40 katas de Python** propuestas en el módulo, diseñadas para practicar desde las estructuras de datos básicas y el control de flujo hasta la programación funcional y la orientación a objetos.

El objetivo no ha sido solo que los ejercicios funcionen, sino escribir código limpio, bien tipado, documentado con *docstrings* y preparado para controlar posibles errores de entrada o casos límite.

## 🛠️ 2. Metodología y Desarrollo de las Katas

A lo largo del proyecto he dividido las soluciones tanto en un script unificado (`docs/katas_python.py`) como en un cuaderno interactivo para facilitar su lectura y prueba:

* **Programación funcional (`map`, `filter`, `reduce`, `lambda`):** Ha sido una de las partes más interesantes para dejar atrás los bucles tradicionales y escribir transformaciones en una sola línea. El mayor reto aquí fue controlar los casos límite, como evitar fallos en `reduce` cuando recibe listas vacías o filtrar correctamente enteros descartando valores booleanos (`type(x) is int`).
* **Manejo de excepciones personalizadas:** Implementación de bloques `try / except` para validar entradas de usuario (como divisiones por cero, edades fuera de rango o horas no válidas) y creación de errores propios como `ListaVaciaError`.
* **Programación Orientada a Objetos (Clases: `Arbol` y `UsuarioBanco`):** Diseño de atributos y métodos con validaciones internas para asegurar que la lógica de negocio se cumpla (por ejemplo, comprobar si un usuario tiene cuenta corriente activa y saldo suficiente antes de permitir una transferencia).
* **Manipulación de texto y lógica matemática:** Procesamiento de cadenas palabra a palabra con `split()` para evitar reemplazos parciales no deseados y cálculo de áreas geométricas apoyándome en la librería estándar `math`.

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
