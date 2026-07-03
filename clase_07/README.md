# Clase 07: Laboratorio de información útil y estructuras monótonas

Esta clase continúa el enfoque iniciado en Clase 06:

```text
Problema -> lectura estratégica -> modelado -> elección de estructura
         -> pseudocódigo -> implementación -> pruebas -> discusión técnica
```

El objetivo no es memorizar una pila monótona. El objetivo es descubrir el patrón:

> Conservar únicamente la información que sigue siendo útil.

## Problema principal

[Nearest Smaller Values - CSES Problem Set](https://cses.fi/problemset/task/1645/)

Para cada posición de un arreglo, debemos encontrar la posición más cercana a la izquierda con un valor menor. Si no existe, se reporta `0`.

## Problemas de contraste

- Variante: Nearest Greater Values.
- Contraejemplo: [Maximum Subarray Sum - CSES Problem Set](https://cses.fi/problemset/task/1643/).
- Vista al futuro: [Sliding Window Median - CSES Problem Set](https://cses.fi/problemset/task/1076/).

## Objetivos

Al terminar la clase podrás:

- Leer estratégicamente un problema de CSES.
- Proponer una solución ingenua.
- Detectar trabajo repetido.
- Explicar qué información se vuelve inútil.
- Descubrir la idea de pila monótona.
- Implementar `valores_menores_cercanos`.
- Diseñar algunas pruebas propias.
- Ejecutar pruebas públicas con `pytest -v`.
- Escribir `notebook.md`, `discusion.md` y `reporte_pytest.md`.

## Estructura

```text
clase_07/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_07_laboratorio_informacion_util.ipynb
├── practicas/
│   └── practica_07.md
├── src/
│   ├── init.py
│   └── nearest_smaller.py
├── tests/
│   └── test_publico_nearest_smaller.py
├── pytest.ini
└── README.md
```

## Cómo abrir la presentación

Abre directamente:

```text
presentacion/index.html
```

Atajos:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

## Cómo ejecutar el notebook

```bash
jupyter notebook notebooks/clase_07_laboratorio_informacion_util.ipynb
```

No respondas dentro del `.ipynb`. Cada pregunta indica que debes responder en `notebook.md`.

## Cómo ejecutar pruebas públicas

Desde `clase_07/`:

```bash
pytest -v
```

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si esto ocurre, utiliza:

```bash
python3 -m pytest -v
```

Este comando ejecuta `pytest` usando explícitamente el intérprete de Python y suele resolver problemas relacionados con múltiples instalaciones de Python o con el `PATH`.

Para probar una entrega dentro de `entregas/clase_07/nombre/`, puedes ejecutar:

```bash
PYTHONPATH=entregas/clase_07/nombre pytest -v
```

## Entrega

No entregues el notebook `.ipynb` como evidencia principal.

Entrega:

```text
entregas/
└── clase_07/
    └── nombre/
        ├── implementacion.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

`notebook.md` contiene respuestas del notebook y no debe contener código completo.

`discusion.md` es un documento técnico: argumenta decisiones, invariantes, pruebas, complejidad y contrastes.

`reporte_pytest.md` debe incluir la salida completa de `pytest -v` o `python3 -m pytest -v`.

