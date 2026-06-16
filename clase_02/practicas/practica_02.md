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

# Actividad de proyecto / GitHub

El objetivo de esta actividad es practicar el flujo de trabajo que utilizaremos durante todo el curso.

1. Acepta el Issue asignado por el profesor.
2. Crea una rama con el formato:

```text
clase-02-tu-nombre
```

3. Dentro de:

```text
entregas/clase_02/
```

crea un archivo llamado:

```text
tu_nombre.md
```

4. El archivo debe contener:
   - Tu nombre.
   - Una reflexión breve sobre la clase.
   - Una pregunta relacionada con la sesión.

5. Realiza un commit con un mensaje descriptivo.

6. Publica tu rama y abre un Pull Request hacia `main`.

7. En la descripción del Pull Request incluye:

```text
Closes #XX
```

donde `XX` es el número del Issue asignado.

8. Revisa el Pull Request asignado por el script `asignar_revisiones.py` y deja al menos un comentario constructivo.

## Importante

- No trabajes directamente sobre `main`.
- No modifiques archivos de otros compañeros.
- Cada alumno debe trabajar únicamente sobre su propio archivo.

El objetivo principal es practicar el flujo:

```text
Issue → Branch → Commit → Pull Request → Review → Merge
```

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
