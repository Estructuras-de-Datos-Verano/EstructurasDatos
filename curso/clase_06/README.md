# Clase 06: Resolución de problemas usando estructuras de datos

En esta clase cambia el enfoque del curso.

Antes partíamos de una estructura de datos y la implementábamos. Ahora partimos de un problema, lo leemos estratégicamente, lo modelamos, elegimos una estructura, diseñamos un algoritmo, lo implementamos y lo probamos.

Problema principal:

[Josephus Problem I - CSES Problem Set](https://cses.fi/problemset/task/2162)

Problema secundario solo como motivación:

[Nearest Smaller Values - CSES Problem Set](https://cses.fi/problemset/task/1645)

## Objetivos

Al terminar la clase podrás:

- Leer estratégicamente un problema.
- Identificar entrada, salida y restricciones.
- Decidir qué información debe mantenerse.
- Elegir una estructura de datos adecuada.
- Escribir pseudocódigo antes de implementar.
- Implementar una solución en Python.
- Ejecutar pruebas públicas.
- Escribir una discusión técnica argumentada.

## Estructura de archivos

```text
clase_06/
├── notebooks/
│   └── clase_06_josephus.ipynb
├── presentacion/
│   └── index.html
├── practicas/
│   └── practica_06.md
├── src/
│   └── josephus.py
├── tests/
│   └── test_publico_josephus.py
├── pytest.ini
└── README.md
```

## Cómo abrir la presentación

Abre directamente en el navegador:

```text
presentacion/index.html
```

Atajos:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

## Cómo ejecutar el notebook

Desde esta carpeta:

```bash
jupyter notebook notebooks/clase_06_josephus.ipynb
```

El notebook está guiado y contiene espacios `TODO`. No se entrega como producto final.

## Cómo ejecutar las pruebas públicas

Desde `clase_06/`:

```bash
pytest -v
```

Observación.

En algunos sistemas operativos o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto.

Si esto ocurre, utiliza:

```bash
python3 -m pytest -v
```

Este comando ejecuta `pytest` utilizando explícitamente el intérprete de Python y suele resolver problemas relacionados con múltiples instalaciones de Python o con el `PATH`.

Al inicio algunas pruebas fallarán porque `src/josephus.py` contiene una función pendiente. Eso es esperado: las pruebas son retroalimentación para tu implementación.

## Qué debes entregar

No entregues el archivo `.ipynb`.

Sí entrega `notebook.md`: un documento de trabajo con tus respuestas a las preguntas del notebook, en el mismo orden. No debe contener código completo.

Entrega:

```text
entregas/
└── clase_06/
    └── nombre/
        ├── implementacion.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

`implementacion.py` debe contener únicamente la solución del problema y debe ser importable por `pytest`.

`notebook.md` evidencia el razonamiento seguido durante la clase.

`discusion.md` es un documento técnico: argumenta decisiones de diseño, contraste, complejidad y pruebas. No debe repetir literalmente las respuestas de `notebook.md`.

`reporte_pytest.md` debe usar la salida de `pytest -v` o `python3 -m pytest -v` e incluir: comando utilizado, salida completa, interpretación, número de pruebas, cuántas pasaron, qué comportamiento verifican y qué caso importante falta probar.

## Flujo de GitHub

Trabaja con:

```text
Issue -> Branch -> Commit -> Pull Request -> Review
```

No trabajes directamente sobre `main`.
