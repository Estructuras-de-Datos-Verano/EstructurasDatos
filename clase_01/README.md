# Clase 01: ¿Por qué existen las estructuras de datos?

Primera clase del curso intersemestral de **Estructuras de datos** para estudiantes de Matemáticas Aplicadas.

La idea central de la clase es:

> Elegir una estructura de datos es elegir qué operaciones queremos hacer eficientes.

Durante la sesión se conectan problemas, representaciones, algoritmos y resultados mediante experimentos en Python.

## Estructura de archivos

```text
clase_01/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_01_estructuras_y_eficiencia.ipynb
├── src/
│   ├── __init__.py
│   └── mediciones.py
├── practicas/
│   └── practica_01.md
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

La presentación incluye navegación con botones, contador, barra de progreso, notas del profesor, MathJax, Plotly, temporizador y pizarrón digital.

Atajos útiles:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas del profesor.
- `T`: iniciar o pausar el temporizador.
- `I`: activar o desactivar el pizarrón.

## Cómo ejecutar el notebook

Con el entorno activado:

```bash
jupyter notebook notebooks/clase_01_estructuras_y_eficiencia.ipynb
```

Ejecuta las celdas en orden. El notebook usa el módulo `src/mediciones.py` incluido en esta carpeta.

## Qué deben entregar los estudiantes

Cada estudiante debe entregar por GitHub:

- Un pull request desde una rama propia.
- El `README.md` del proyecto del curso editado con su nombre y una reflexión breve.
- El notebook de la clase ejecutado, con respuestas en las preguntas de reflexión.
- La práctica 01 resuelta según las instrucciones de `practicas/practica_01.md`.

## Material de la clase

Esta primera clase trabaja únicamente con Python y herramientas colaborativas de GitHub.
