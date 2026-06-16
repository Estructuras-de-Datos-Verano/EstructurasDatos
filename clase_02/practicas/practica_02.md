# Práctica 02: Listas, conjuntos, diccionarios y eficiencia

## Objetivos

Al terminar esta práctica podrás:

- Medir tiempos con `time.perf_counter`.
- Comparar búsqueda en `list` y `set`.
- Contar frecuencias con `dict` y `Counter`.
- Interpretar de forma informal `O(1)`, `O(n)` y `O(n²)`.
- Usar GitHub para trabajar con issues, ramas, commits, pull requests y revisiones.

## Instrucciones generales

Trabaja en tu rama personal del repositorio del curso. Puedes discutir ideas con tus compañeros, pero tus mediciones, respuestas y conclusiones deben ser tuyas.

Tiempo sugerido fuera de clase: 90 a 120 minutos.

## Ejercicio 1: Medir búsqueda en lista y conjunto

1. Abre el notebook `notebooks/clase_02_listas_sets_dicts.ipynb`.
2. Ejecuta las celdas de importación.
3. Genera datos con varios tamaños.
4. Mide la búsqueda de un valor ausente en una lista.
5. Construye un conjunto una vez y mide la búsqueda del mismo valor.
6. Genera una gráfica comparando los tiempos.

Responde:

1. ¿Cuál fue más rápido?
2. ¿La diferencia crece con el tamaño?
3. ¿Qué estructura usarías si necesitas hacer muchas búsquedas?

## Ejercicio 2: Contar frecuencias

1. Usa una lista con datos repetidos.
2. Cuenta frecuencias con un diccionario.
3. Cuenta frecuencias con `Counter`.
4. Verifica que ambos resultados representen las mismas frecuencias.

Responde:

1. ¿Qué estructura usarías si necesitas contar frecuencias?
2. ¿Qué hace más claro `Counter`?
3. ¿Qué ventaja tiene entender el diccionario manual antes de usar `Counter`?

## Ejercicio 3: Complejidad intuitiva

Clasifica cada fragmento como `O(1)`, `O(n)` u `O(n²)` y explica por qué.

```python
primero = datos[0]
```

```python
for dato in datos:
    if dato == objetivo:
        aparece = True
```

```python
for a in datos:
    for b in datos:
        pares.append((a, b))
```

## Ejercicio 4: Sacrificios de representación

Escribe una reflexión breve:

1. ¿Qué sacrificios tiene usar un `set` en lugar de una `list`?
2. ¿Cuándo sí preferirías una lista?
3. ¿Cuándo sí preferirías un conjunto?
4. ¿Qué cambia si necesitas conservar repeticiones?

## Actividad de proyecto / GitHub

Elige o crea uno de estos issues:

- `[DOC] Escribir guía de estilo`
- `[DOC] Documentar flujo básico de GitHub`
- `[TEST] Crear primera prueba de ejemplo`
- `[PROY] Definir estructura inicial de src/`

Trabajo esperado:

1. Crea una rama con el formato `clase-02-tu-nombre`.
2. Haz un cambio pequeño y claro.
3. Guarda el cambio con un commit descriptivo.
4. Abre un pull request.
5. Pide revisión.
6. Revisa al menos un pull request de otra persona.

No modifiques directamente `main`.

## Entregables

Entrega mediante pull request:

- Notebook ejecutado o guardado con tus resultados.
- Respuestas a las preguntas de reflexión.
- Cambio de proyecto asociado a un issue.
- Evidencia de una revisión realizada.

## Checklist de entrega

- [ ] Ejecuté el notebook en orden.
- [ ] Incluí tiempos para `list`, `set`, `dict` y `Counter`.
- [ ] Incluí al menos una gráfica.
- [ ] Respondí las preguntas de reflexión.
- [ ] Creé o tomé un issue.
- [ ] Trabajé en una rama propia.
- [ ] Abrí pull request.
- [ ] Revisé un pull request de otra persona.
- [ ] No trabajé directamente sobre `main`.

## Criterios de evaluación

| Criterio | Puntos |
| --- | ---: |
| Mediciones y gráfica | 30 |
| Interpretación de resultados | 25 |
| Uso correcto de `dict` y `Counter` | 15 |
| Reflexión sobre complejidad y sacrificios | 15 |
| Flujo de GitHub y revisión | 15 |

Total: 100 puntos.
