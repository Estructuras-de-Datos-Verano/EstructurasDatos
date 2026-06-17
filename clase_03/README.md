# Clase 03: Tipos de Datos Abstractos, interfaz y pilas

En esta clase pasamos de usar estructuras de datos a diseñar estructuras de datos.

Pregunta guía:

> ¿Qué diferencia hay entre usar una estructura de datos y diseñar una estructura de datos?

Idea central:

> Un Tipo de Dato Abstracto describe qué operaciones existen y qué comportamiento se espera, pero no fija una implementación.

La pila será nuestro primer ejemplo fuerte de Tipo de Dato Abstracto.

## Objetivos

Al terminar la clase podrás:

- Explicar qué es un Tipo de Dato Abstracto.
- Distinguir entre interfaz e implementación.
- Conectar TDA con clases y métodos de Programación Orientada a Objetos.
- Reconocer problemas donde una pila aparece como herramienta.
- Diseñar una interfaz básica para una pila.
- Proponer pruebas mínimas para validar una pila.

## Estructura de archivos

```text
clase_03/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_03_tda_pilas.ipynb
├── src/
│   ├── __init__.py
│   └── herramientas_pila.py
├── practicas/
│   └── practica_03.md
├── README.md
└── requirements.txt
```

## Instalación

Desde esta carpeta:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows, la activación del entorno suele ser:

```bash
.venv\Scripts\activate
```

## Cómo abrir la presentación

Abre directamente en el navegador:

```text
presentacion/index.html
```

La presentación incluye navegación, contador de diapositivas, barra de progreso, notas del profesor y temporizador.

Atajos útiles:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

## Cómo ejecutar el notebook

Con el entorno activado:

```bash
jupyter notebook notebooks/clase_03_tda_pilas.ipynb
```

Ejecuta las celdas en orden. El notebook usa el módulo `src/herramientas_pila.py`.

## Archivos que usarás

- `presentacion/index.html`: guía visual de la clase.
- `notebooks/clase_03_tda_pilas.ipynb`: ejercicios de motivación y diseño.
- `src/herramientas_pila.py`: funciones auxiliares para simular usos de pila.
- `practicas/practica_03.md`: instrucciones de entrega.

## Qué debes entregar

Cada estudiante debe crear:

```text
entregas/clase_03/tu_nombre.md
```

El archivo debe incluir:

- Definición propia de Tipo de Dato Abstracto.
- Diferencia entre interfaz e implementación.
- Un problema donde usarías una pila.
- Propuesta de interfaz para `Pila`.
- Una prueba mínima escrita en lenguaje natural.

La entrega se realiza mediante el flujo:

```text
Issue → Branch → Commit → Pull Request → Review
```
