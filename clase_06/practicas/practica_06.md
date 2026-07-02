# Práctica 06: Josephus Problem I

## Contexto

En esta práctica resolverás el problema [Josephus Problem I](https://cses.fi/problemset/task/2162) del CSES Problem Set.

El objetivo no es solo programar. El objetivo es argumentar cómo pasaste del enunciado a una estructura de datos, de la estructura a un algoritmo, y del algoritmo a pruebas.

## Objetivos

Al terminar esta práctica podrás:

- Leer estratégicamente un problema.
- Identificar entrada, salida y restricciones.
- Modelar la información que debe mantenerse.
- Elegir una estructura de datos y justificarla.
- Implementar una solución importable.
- Ejecutar pruebas públicas.
- Escribir una discusión técnica.

## Instrucciones

1. Lee el enunciado original de CSES.
2. Completa el notebook como guía de trabajo.
3. Implementa tu solución en `implementacion.py`.
4. Ejecuta las pruebas públicas.
5. Escribe `notebook.md` con las respuestas guiadas del notebook.
6. Escribe `discusion.md`.
7. Escribe `reporte_pytest.md`.
8. Abre Pull Request desde una rama propia.
9. Revisa el PR asignado.

No modifiques directamente `main`.

## Entrega

Estructura obligatoria:

```text
entregas/
└── clase_06/
    └── nombre/
        ├── implementacion.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

## `implementacion.py`

Debe contener únicamente la solución del problema.

Requisitos:

- Debe definir `orden_eliminacion(n)`.
- Debe ser importable por `pytest`.
- No debe contener código de pruebas.
- No debe leer de `input()` al importar.
- Puede incluir funciones auxiliares si ayudan a la claridad.

Interfaz esperada:

```python
def orden_eliminacion(n: int) -> list[int]:
    ...
```

## `notebook.md`

Este archivo no es una copia del notebook.

Es un documento de trabajo. Su objetivo es evidenciar el razonamiento seguido durante la clase.

Debe contener únicamente tus respuestas a las preguntas que aparecen durante el notebook, en el mismo orden. No debe contener código completo.

Estructura sugerida:

```text
# Notebook - Clase 06

## Lectura estratégica

### ¿Qué está pidiendo el problema?

...

### ¿Qué información debemos recordar?

...

---

## Ingeniería inversa del algoritmo

...

---

## Modelado

...

---

## Pseudocódigo

...
```

## `discusion.md`

No lo llames resumen. Debe llamarse exactamente:

```text
discusion.md
```

Este archivo es un documento técnico. Su objetivo es argumentar decisiones de diseño.

No debe repetir literalmente las respuestas de `notebook.md`. Debe usar esas respuestas como base para construir contraste, análisis y reflexión técnica.

Incluye estas secciones:

### 1. Lectura estratégica

Explica qué pide el problema.

### 2. Elección de estructura

¿Por qué una cola?

¿Qué otra estructura consideraste?

¿Por qué la descartaste?

### 3. Diseño del algoritmo

Explica el algoritmo antes del código.

### 4. Pruebas

Escoge una prueba pública.

Explica qué propiedad verifica.

Propón una prueba adicional.

### 5. Complejidad

Analiza tiempo y memoria.

### 6. Contraste

Si el problema cambiara ligeramente, ¿seguirías usando una cola?

¿Por qué?

### 7. Pregunta abierta

Formula una pregunta técnica interesante relacionada con el problema.

## `reporte_pytest.md`

Debe contener:

- comando utilizado;
- salida completa obtenida con `pytest -v` o `python3 -m pytest -v`;
- interpretación;
- número de pruebas;
- cuántas pasaron;
- qué comportamiento verifican;
- qué caso importante todavía no está siendo probado.

## Pruebas públicas

Ejecuta desde `clase_06/`:

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

Las pruebas públicas están en:

```text
tests/test_publico_josephus.py
```

Sirven como retroalimentación. No cubren todos los casos posibles.

## Actividad GitHub

Rama sugerida:

```text
clase-06-tu-nombre
```

Issues sugeridos:

- `[CLASE06] Implementar Josephus Problem I`
- `[TEST] Ejecutar pruebas públicas de Josephus`
- `[DOC] Escribir discusión técnica`
- `[REVIEW] Revisar argumentación y pruebas`

## Checklist de entrega

- [ ] `implementacion.py` define `orden_eliminacion`.
- [ ] `implementacion.py` no ejecuta `input()` al importar.
- [ ] Escribí `notebook.md` con respuestas en el orden del notebook.
- [ ] `notebook.md` no contiene código completo.
- [ ] Ejecuté `pytest -v` o `python3 -m pytest -v`.
- [ ] Escribí `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] `discusion.md` no repite literalmente `notebook.md`.
- [ ] Analicé complejidad.
- [ ] Propuse una prueba adicional.
- [ ] Trabajé en una rama propia.
- [ ] Abrí Pull Request.
- [ ] Revisé el PR asignado.
- [ ] No trabajé directamente sobre `main`.

## Criterios de evaluación

| Criterio | Puntos |
| --- | ---: |
| `notebook.md`: lectura estratégica y modelado | 20 |
| Elección y justificación de estructura | 20 |
| Implementación importable | 25 |
| Pruebas y reporte de pytest | 20 |
| Discusión técnica y GitHub | 15 |

Total: 100 puntos.
