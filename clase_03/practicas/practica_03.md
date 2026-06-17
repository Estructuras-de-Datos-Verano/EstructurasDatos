# Práctica 03: Diseñar antes de implementar

## Objetivos

Al terminar esta práctica podrás:

- Explicar con tus palabras qué es un Tipo de Dato Abstracto.
- Distinguir entre interfaz e implementación.
- Reconocer situaciones donde una pila ayuda a resolver un problema.
- Proponer una interfaz básica para una pila.
- Escribir pruebas mínimas en lenguaje natural antes de implementar código.
- Usar GitHub para entregar un cambio pequeño mediante pull request y revisión.

## Instrucciones generales

Trabaja en tu rama personal del repositorio del curso. Puedes discutir ideas con tus compañeros, pero tu definición, ejemplos y pruebas deben estar escritos con tus propias palabras.

Tiempo sugerido fuera de clase: 60 a 90 minutos.

## Ejercicio 1: Definir un TDA

Escribe una definición propia de Tipo de Dato Abstracto.

Tu respuesta debe mencionar:

1. Qué operaciones ofrece.
2. Qué comportamiento promete.
3. Por qué no depende de una implementación específica.

## Ejercicio 2: Interfaz contra implementación

Explica la diferencia entre interfaz e implementación usando este ejemplo:

```python
estructura.agregar(x)
estructura.quitar()
estructura.esta_vacia()
```

Responde:

1. ¿Cuál es la interfaz?
2. ¿Qué sabemos sobre el comportamiento esperado?
3. ¿Qué no sabemos sobre cómo está implementada?
4. ¿Por qué eso puede ser una ventaja?

## Ejercicio 3: Pila como herramienta

Elige uno de estos casos:

- Historial de navegación.
- Deshacer acciones.
- Paréntesis balanceados.
- Llamadas a funciones.
- Recursión.
- DFS en grafos.

Describe:

1. Qué elementos se guardarían en la pila.
2. Por qué el último elemento en entrar debe ser el primero en salir.
3. Qué operación sería más importante: `push`, `pop`, `peek`, `esta_vacia` o `tamano`.

## Ejercicio 4: Propuesta de interfaz

Propón una interfaz para una clase `Pila`.

Incluye al menos estos métodos:

```python
push(elemento)
pop()
peek()
esta_vacia()
tamano()
```

Responde:

1. ¿Qué debería regresar `pop()`?
2. ¿Qué debería pasar si hacemos `pop()` sobre una pila vacía?
3. ¿`peek()` debería eliminar el elemento?
4. ¿Conviene usar nombres en inglés o español para este proyecto?

## Ejercicio 5: Pruebas mínimas en lenguaje natural

Antes de implementar la pila, escribe al menos cinco pruebas en lenguaje natural.

Ejemplo:

> Si apilo `1` y luego `2`, entonces `pop()` debe regresar `2`.

Incluye pruebas para:

- Apilar un elemento.
- Apilar varios elementos.
- Consultar el tope sin eliminarlo.
- Preguntar si la pila está vacía.
- Intentar sacar un elemento de una pila vacía.

# Actividad de proyecto / GitHub

Cada alumno debe crear:

```text
entregas/clase_03/tu_nombre.md
```

El archivo debe contener:

- Tu nombre.
- Definición propia de TDA.
- Diferencia entre interfaz e implementación.
- Un problema donde usarías una pila.
- Propuesta de interfaz para `Pila`.
- Una prueba mínima en lenguaje natural.

Flujo esperado:

```text
Issue → Branch → Commit → Pull Request → Review
```

## Pasos

1. Acepta o toma el issue asignado por el profesor.
2. Crea una rama con el formato:

```text
clase-03-tu-nombre
```

3. Crea tu archivo dentro de:

```text
entregas/clase_03/
```

4. Realiza un commit con un mensaje descriptivo.
5. Publica tu rama y abre un Pull Request hacia `main`.
6. En la descripción del Pull Request incluye:

```text
Closes #XX
```

donde `XX` es el número del issue asignado.

7. Revisa el Pull Request asignado con `asignar_revisiones.py`.
8. Deja al menos un comentario constructivo.

## Importante

- No trabajes directamente sobre `main`.
- No modifiques archivos de otros compañeros.
- No implementes todavía una clase `Pila` completa.
- No adelantes listas ligadas ni C++.
- Cada alumno debe trabajar únicamente sobre su propio archivo.

## Entregables

Entrega mediante Pull Request:

- Notebook ejecutado o guardado con tus respuestas.
- Archivo `entregas/clase_03/tu_nombre.md`.
- Propuesta de interfaz para `Pila`.
- Pruebas mínimas escritas en lenguaje natural.
- Evidencia de una revisión realizada.

## Reflexión

Responde:

1. ¿Qué diferencia ves entre usar una pila y diseñar una pila?
2. ¿Qué parte de la interfaz te parece más importante?
3. ¿Qué decisión dejarías abierta para la implementación de la Clase 04?
4. ¿Qué aprendiste al revisar el Pull Request de otra persona?

## Checklist de entrega

- [ ] Ejecuté el notebook en orden.
- [ ] Escribí mi definición propia de TDA.
- [ ] Expliqué interfaz contra implementación.
- [ ] Describí un problema donde usaría una pila.
- [ ] Propuse una interfaz para `Pila`.
- [ ] Escribí al menos cinco pruebas mínimas en lenguaje natural.
- [ ] Creé o tomé un issue.
- [ ] Trabajé en una rama propia.
- [ ] Abrí Pull Request.
- [ ] Revisé un Pull Request de otra persona.
- [ ] No trabajé directamente sobre `main`.

## Criterios de evaluación

| Criterio | Puntos |
| --- | ---: |
| Definición de TDA e interfaz | 25 |
| Explicación de interfaz contra implementación | 20 |
| Motivación correcta de pila como herramienta | 20 |
| Pruebas mínimas en lenguaje natural | 20 |
| Flujo de GitHub y revisión | 15 |

Total: 100 puntos.
