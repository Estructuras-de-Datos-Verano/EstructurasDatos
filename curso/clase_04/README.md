# Clase 04: Múltiples implementaciones de un TDA y pytest

En esta clase convertimos la interfaz conceptual de una pila en un contrato formal con una clase abstracta. Después implementamos el mismo TDA usando herramientas internas distintas y validamos el comportamiento con pruebas.

Pregunta guía:

> Si todas son pilas, ¿por qué podríamos implementarlas de distintas formas?

Idea central:

> Una pila es un Tipo de Dato Abstracto definido por su comportamiento LIFO. La interfaz debe mantenerse estable, pero la implementación puede cambiar.

## Objetivos

Al terminar la clase podrás:

- Explicar la relación entre TDA, interfaz y clase abstracta.
- Usar `ABC` y `abstractmethod`.
- Implementar pilas con `list`, `deque` y `tuple`.
- Explicar polimorfismo usando pilas.
- Escribir pruebas con `assert`.
- Ejecutar pruebas con `pytest`.
- Usar `pytest.raises` y `pytest.mark.parametrize`.

## Estructura de archivos

```text
clase_04/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_04_pilas_abstractas_pytest.ipynb
├── src/
│   ├── __init__.py
│   └── pilas.py
├── tests/
│   └── test_pilas.py
├── practicas/
│   └── practica_04.md
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

Atajos útiles:

- Flecha derecha o espacio: siguiente diapositiva.
- Flecha izquierda: diapositiva anterior.
- `N`: mostrar u ocultar notas.
- `T`: iniciar o pausar el temporizador.

## Cómo ejecutar el notebook

Con el entorno activado:

```bash
jupyter notebook notebooks/clase_04_pilas_abstractas_pytest.ipynb
```

Ejecuta las celdas en orden.

## Cómo ejecutar las pruebas

Desde la carpeta `clase_04/`:

```bash
pytest
```

Para guardar evidencia:

```bash
pytest > evidencia_pytest.txt
```

## Qué debes entregar

Cada estudiante debe entregar:

```text
entregas/nombre/clase_04/
├── clase_04_pilas_nombre.ipynb
├── resumen.md
└── evidencia_pytest.txt
```

La entrega se realiza mediante:

```text
Issue → Branch → Commit → Pull Request → Review
```

No trabajes directamente sobre `main`.
