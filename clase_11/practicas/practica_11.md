# Práctica 11: Árboles binarios de búsqueda

## Contexto

En las clases anteriores usamos listas, pilas, colas y grafos para modelar distintos tipos de problemas.

En esta práctica cambia la forma de organizar la información: una lista guarda datos en secuencia, mientras que un árbol organiza datos de forma jerárquica.

La pregunta central es:

> ¿Cómo podemos organizar datos para buscar más eficientemente que en una lista?

Trabajaremos con árboles binarios de búsqueda, BST, para entender cómo una propiedad estructural permite descartar una parte del espacio en cada paso.

## Objetivos

Al terminar esta práctica podrás:

- explicar qué es un árbol, un nodo, una raíz, una hoja, un subárbol y la altura;
- enunciar el invariante de un árbol binario de búsqueda;
- implementar `Nodo`;
- implementar `ArbolBinarioBusqueda`;
- insertar valores sin duplicados;
- buscar valores;
- calcular altura;
- recorrer el árbol en inorden, preorden y postorden;
- explicar por qué inorden devuelve valores ordenados en un BST;
- escribir pruebas propias en `test_estudiante.py`;
- usar `evaluar.py` para ejecutar pruebas públicas;
- escribir una discusión técnica en Markdown.

## Instrucciones

1. Revisa el notebook de la clase.
2. Responde sus preguntas en `notebook.md`.
3. Implementa `Nodo` en `implementacion.py`.
4. Implementa `ArbolBinarioBusqueda` en `implementacion.py`.
5. Implementa `insertar`.
6. Implementa `contiene`.
7. Implementa `altura`.
8. Implementa `inorden`, `preorden` y `postorden`.
9. Escribe al menos 3 pruebas propias en `test_estudiante.py`.
10. Ejecuta la evaluación con `evaluar.py`.
11. Crea `reporte_pytest.md`.
12. Escribe `discusion.md`.
13. Abre Pull Request.
14. Revisa el PR asignado por `asignar_revisiones.py`.

No respondas preguntas dentro del notebook.

No entregues el notebook `.ipynb` como evidencia principal.

No programes animaciones. Los GIFs ya están integrados como material de apoyo.

No modifiques `main`.

No modifiques tests públicos salvo los TODOs explícitos y solo si el profesor lo indica para tu rama. Tus pruebas obligatorias deben estar en `test_estudiante.py`.

Trabaja en:

```text
entregas/clase_11/nombre/
```

Puedes usar `src/arboles.py` como molde para crear tu `implementacion.py`, pero las pruebas evaluarán tu archivo de entrega.

Usa Markdown para que GitHub permita una revisión clara.

## Entrega obligatoria

```text
entregas/
└── clase_11/
    └── nombre/
        ├── implementacion.py
        ├── test_estudiante.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

## `implementacion.py`

Debe contener tu implementación.

Debe definir:

```python
class Nodo:
    ...

class ArbolBinarioBusqueda:
    ...
```

La clase `ArbolBinarioBusqueda` debe tener estos métodos:

```python
def esta_vacio(self) -> bool:
    ...

def insertar(self, valor: int) -> None:
    ...

def contiene(self, valor: int) -> bool:
    ...

def altura(self) -> int:
    ...

def inorden(self) -> list[int]:
    ...

def preorden(self) -> list[int]:
    ...

def postorden(self) -> list[int]:
    ...
```

No implementes eliminación de nodos en esta clase.

No ejecutes código al importar `implementacion.py`.

No incluyas pruebas dentro de `implementacion.py`.

Puedes incluir funciones auxiliares si ayudan a la claridad.

## `test_estudiante.py`

Debe contener al menos 3 pruebas propias.

Cada prueba debe tener nombre claro y docstring o comentario breve que explique qué comportamiento verifica.

Ejemplo de estilo:

```python
def test_inorden_de_arbol_con_varios_niveles():
    """Verifica que inorden regresa valores ordenados en un árbol con varios niveles."""
    ...
```

Tus pruebas pueden revisar:

- recorrido preorden;
- recorrido postorden;
- altura de un árbol degenerado;
- búsqueda de valores inexistentes;
- manejo de duplicados;
- árbol con valores negativos.

## `notebook.md`

Contiene tus respuestas a las preguntas del notebook, en el mismo orden.

No debe contener código completo.

Estructura sugerida:

```text
# Notebook - Clase 11

## 1. Motivación
## 2. Problemas relacionados
## 3. Conceptos básicos
## 4. Árbol binario de búsqueda
## 5. Búsqueda
## 6. Inserción
## 7. Altura
## 8. Recorridos
## 9. Animaciones
## 10. Implementación
## 11. Pruebas
## 12. Patrón descubierto
## 13. Cierre
```

`notebook.md` es un documento de trabajo. Su objetivo es evidenciar el razonamiento guiado seguido durante la clase.

## `discusion.md`

Es un documento técnico. Su objetivo es argumentar decisiones de diseño.

No debe repetir literalmente `notebook.md`.

Debe contener:

```text
# Discusión técnica

## 1. Lista vs árbol
## 2. Motivación del BST
## 3. Invariante
## 4. Inserción
## 5. Recorridos
## 6. Altura y eficiencia
## 7. Pruebas
## 8. Cambio técnico: evaluar.py
## 9. Problemas relacionados
## 10. Pregunta abierta
```

## `reporte_pytest.md`

Debe contener:

- comando ejecutado;
- salida completa;
- interpretación;
- cuántas pruebas se ejecutaron;
- cuántas pasaron;
- si hubo errores;
- qué comportamiento verifican;
- qué prueba diseñaste tú en `test_estudiante.py`;
- qué caso todavía falta probar.

Usa:

```bash
python3 evaluar.py entregas/clase_11/nombre clase_11/tests
```

Este script ejecuta internamente `pytest -v` sobre la carpeta de tests públicos y permite que los tests importen directamente desde tu `implementacion.py`.

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si necesitas ejecutar pytest directamente, utiliza:

```bash
python3 -m pytest -v
```

Este comando ejecuta `pytest` usando explícitamente el intérprete de Python y suele resolver problemas relacionados con múltiples instalaciones de Python o con el `PATH`.

## Nuevo flujo con `evaluar.py`

A partir de esta clase, los tests públicos ya no buscan varias rutas posibles ni importan desde `src`.

Los tests asumen que existe:

```text
implementacion.py
```

en tu carpeta de entrega.

Ejecuta desde la raíz de `curso-alumnos`:

```bash
python3 evaluar.py entregas/clase_11/nombre clase_11/tests
```

El script:

- verifica que exista tu carpeta de entrega;
- verifica que exista `implementacion.py`;
- agrega tu carpeta de entrega al entorno de Python;
- ejecuta las pruebas públicas con `pytest -v`;
- muestra el resultado.

Por eso los tests públicos pueden importar de forma limpia:

```python
from implementacion import ArbolBinarioBusqueda, Nodo
```

## Actividad GitHub

Cada alumno debe:

- crear una rama `clase-11-tu-nombre`;
- trabajar en su carpeta;
- hacer commits claros;
- abrir Pull Request;
- revisar el PR asignado;
- comentar al menos una cosa sobre claridad de explicación, invariante del BST, prueba diseñada, recorridos, redacción técnica o uso correcto de `evaluar.py`.

## Checklist

- [ ] Respondí preguntas del notebook en `notebook.md`.
- [ ] `notebook.md` sigue el orden del notebook.
- [ ] `notebook.md` no contiene código completo.
- [ ] Implementé `Nodo`.
- [ ] Implementé `ArbolBinarioBusqueda`.
- [ ] Implementé `insertar`.
- [ ] Implementé `contiene`.
- [ ] Implementé `altura`.
- [ ] Implementé `inorden`.
- [ ] Implementé `preorden`.
- [ ] Implementé `postorden`.
- [ ] No implementé eliminación de nodos.
- [ ] Escribí al menos 3 pruebas propias en `test_estudiante.py`.
- [ ] Ejecuté `python3 evaluar.py entregas/clase_11/nombre clase_11/tests`.
- [ ] Guardé la salida completa en `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] Expliqué el invariante del BST.
- [ ] Expliqué por qué inorden ordena los valores.
- [ ] Abrí PR.
- [ ] Revisé el PR asignado.
- [ ] No modifiqué `main`.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| `notebook.md` y conceptos de árboles | 20 |
| Implementación de BST | 25 |
| Recorridos y altura | 15 |
| Pruebas propias y evaluación con `evaluar.py` | 15 |
| `discusion.md` y redacción técnica | 15 |
| GitHub y revisión | 10 |

Total: 100 puntos.
