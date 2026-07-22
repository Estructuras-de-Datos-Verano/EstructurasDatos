# Práctica 07: Nearest Smaller Values

## Contexto

Resolverás el problema [Nearest Smaller Values](https://cses.fi/problemset/task/1645/) del CSES Problem Set.

La meta no es memorizar una pila monótona. La meta es descubrir qué información sigue siendo útil, qué información puede descartarse y cómo una estructura de datos permite evitar trabajo repetido.

## Objetivos

Al terminar esta práctica podrás:

- Leer estratégicamente un problema de CSES.
- Proponer y analizar una solución ingenua.
- Detectar trabajo repetido.
- Explicar el patrón de información útil.
- Implementar `valores_menores_cercanos`.
- Diseñar pruebas propias.
- Escribir una discusión técnica con contraste.
- Revisar el Pull Request de otro compañero.

## Instrucciones

1. Revisa el notebook.
2. Responde sus preguntas en `notebook.md`.
3. Implementa `valores_menores_cercanos` en `implementacion.py`.
4. Completa o diseña las pruebas públicas marcadas con TODO.
5. Ejecuta `pytest -v`.
6. Crea `reporte_pytest.md`.
7. Escribe `discusion.md`.
8. Abre Pull Request.
9. Revisa el PR asignado por `asignar_revisiones.py`.

No respondas preguntas dentro del notebook.

No entregues el notebook `.ipynb` como evidencia principal.

No modifiques `main`.

No modifiques tests públicos salvo los TODOs explícitos.

Trabaja en:

```text
entregas/nombre/clase_07/
```

Usa Markdown para que GitHub permita una revisión clara.

## Entrega obligatoria

```text
entregas/
└── clase_07/
    └── nombre/
        ├── implementacion.py
        ├── notebook.md
        ├── discusion.md
        └── reporte_pytest.md
```

## `implementacion.py`

Debe contener tu solución del problema principal.

Debe definir:

```python
def valores_menores_cercanos(numeros: list[int]) -> list[int]:
    ...
```

No debe ejecutar `input()` al importarse.

No debe contener código de pruebas.

Puede incluir funciones auxiliares si ayudan a la claridad.

## `notebook.md`

Contiene tus respuestas a las preguntas del notebook, en el mismo orden.

No debe contener código completo.

Estructura sugerida:

```text
# Notebook - Clase 07

## 1. Presentación del laboratorio
## 2. Lectura estratégica
## 3. Ingeniería inversa del algoritmo
## 4. Solución ingenua
## 5. Descubrimiento de la pila monótona
## 6. Pseudocódigo
## 7. Variante: Nearest Greater Values
## 8. Contraejemplo: Maximum Subarray Sum
## 9. Vista al futuro: Sliding Window
## 10. Diseño de pruebas
## 11. ¿Qué patrón descubrimos?
```

## `discusion.md`

Debe contener:

1. Problema y primera idea.
2. Por qué la solución ingenua repite trabajo.
3. Información útil e información descartable.
4. Elección de estructura.
5. Variante: Nearest Greater Values.
6. Contraejemplo: Maximum Subarray Sum.
7. Sliding Window.
8. Invariante.
9. Pruebas.
10. Complejidad.
11. Cómo descubrimos el algoritmo.
12. Pregunta abierta.

No debe repetir literalmente `notebook.md`.

## `reporte_pytest.md`

Debe contener:

- comando ejecutado;
- salida completa;
- interpretación;
- cuántas pruebas se ejecutaron;
- cuántas pasaron;
- si hubo errores;
- qué comportamiento verifican;
- qué prueba diseñaste tú;
- qué caso todavía falta probar.

Usa:

```bash
pytest -v
```

o:

```bash
python3 -m pytest -v
```

Observación.

En algunos sistemas o configuraciones de Python, el comando `pytest` puede no encontrar correctamente el entorno del proyecto. Si esto ocurre, utiliza `python3 -m pytest -v`.

## Actividad GitHub

Cada alumno debe:

- crear una rama `clase-07-tu-nombre`;
- trabajar en su carpeta;
- hacer commits claros;
- abrir Pull Request;
- revisar el PR asignado;
- comentar al menos una cosa sobre claridad, estructura, invariante, prueba diseñada, caso límite o redacción técnica.

## Checklist

- [ ] Respondí preguntas del notebook en `notebook.md`.
- [ ] `notebook.md` no contiene código completo.
- [ ] Implementé `valores_menores_cercanos`.
- [ ] No ejecuté `input()` al importar.
- [ ] Completé o diseñé pruebas en TODOs explícitos.
- [ ] Ejecuté `pytest -v` o `python3 -m pytest -v`.
- [ ] Escribí `reporte_pytest.md`.
- [ ] Escribí `discusion.md`.
- [ ] Expliqué el invariante de la pila.
- [ ] Analicé complejidad.
- [ ] Abrí PR.
- [ ] Revisé el PR asignado.
- [ ] No modifiqué `main`.

## Rúbrica

| Criterio | Puntos |
| --- | ---: |
| `notebook.md` y lectura estratégica | 15 |
| Descubrimiento del algoritmo | 20 |
| Implementación en `implementacion.py` | 25 |
| Diseño y ejecución de pruebas | 15 |
| `discusion.md` y redacción técnica | 15 |
| GitHub y revisión | 10 |

Total: 100 puntos.
