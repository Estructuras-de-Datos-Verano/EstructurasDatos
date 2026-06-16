# Clase 02: Listas, conjuntos, diccionarios y eficiencia

En esta clase observaremos que no existe una estructura de datos mejor en absoluto: existe una estructura más adecuada para ciertas operaciones.

Pregunta guía:

> ¿Cómo podemos observar que una estructura de datos es mejor que otra para cierta operación?

## Objetivos

Al terminar la clase podrás:

- Medir tiempos de ejecución en Python.
- Comparar búsqueda en `list` y `set`.
- Usar `dict` para contar frecuencias.
- Usar `collections.Counter`.
- Entender informalmente `O(1)`, `O(n)` y `O(n²)`.
- Explicar qué operación quieres hacer eficiente al elegir una estructura de datos.

## Estructura de archivos

```text
clase_02/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_02_listas_sets_dicts.ipynb
├── src/
│   ├── __init__.py
│   └── mediciones.py
├── practicas/
│   └── practica_02.md
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

La presentación incluye navegación, contador de diapositivas, barra de progreso, notas del profesor, MathJax, Plotly y temporizador.

Atajos útiles:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

## Cómo ejecutar el notebook

Con el entorno activado:

```bash
jupyter notebook notebooks/clase_02_listas_sets_dicts.ipynb
```

Ejecuta las celdas en orden. El notebook usa el módulo `src/mediciones.py`.

## Archivos que usarás

- `presentacion/index.html`: guía visual de la clase.
- `notebooks/clase_02_listas_sets_dicts.ipynb`: experimentos y ejercicios.
- `src/mediciones.py`: funciones reutilizables para medición.
- `practicas/practica_02.md`: instrucciones de entrega.

## Qué debes entregar

- Notebook ejecutado con tus mediciones y respuestas.
- Reflexión individual sobre `list`, `set`, `dict` y `Counter`.
- Un pull request relacionado con un issue de documentación o estructura inicial del proyecto.
- Al menos una revisión a un pull request de otra persona.
