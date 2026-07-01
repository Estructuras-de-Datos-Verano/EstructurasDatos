# Clase 05: Colas, FIFO y comparación con pilas

En esta clase estudiamos las colas como Tipos de Datos Abstractos. La idea central es que una cola no se define por estar hecha con una lista o con un `deque`, sino por su comportamiento FIFO: el primer elemento que entra es el primer elemento que sale.

Pregunta guía:

> ¿Qué estructura necesitamos cuando importa atender en orden de llegada?

## Objetivos

Al terminar la clase podrás:

- Explicar la diferencia entre LIFO y FIFO.
- Definir la interfaz básica de una cola.
- Implementar o revisar `ColaLista`.
- Implementar o revisar `ColaDeque`.
- Explicar por qué `pop(0)` puede ser costoso.
- Escribir pruebas con `assert`.
- Ejecutar pruebas con `pytest`.
- Usar `pytest.raises` y `pytest.mark.parametrize`.

## Estructura de archivos

```text
clase_05/
├── presentacion/
│   └── index.html
├── notebooks/
│   └── clase_05_colas_fifo_pytest.ipynb
├── src/
│   ├── __init__.py
│   └── colas.py
├── tests/
│   └── test_colas.py
├── practicas/
│   └── practica_05.md
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
jupyter notebook notebooks/clase_05_colas_fifo_pytest.ipynb
```

Ejecuta las celdas en orden.

## Cómo ejecutar las pruebas

Desde la carpeta `clase_05/`:

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
entregas/clase_05/nombre/
├── clase_05_colas_nombre.ipynb
├── resumen.md
└── evidencia_pytest.txt
```

La entrega se realiza mediante:

```text
Issue → Branch → Commit → Pull Request → Review
```

No trabajes directamente sobre `main`.

