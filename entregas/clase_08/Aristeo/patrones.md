# Catalogo de patrones - Clase 08

Nombre: Aristeo

## Patron 1: Simulacion

- Problema ejemplo: El problema de Josephus, donde se elimina una posicion cada cierto paso y se sigue el proceso hasta quedar un unico elemento.
- Pregunta detonadora: ¿Que pasa si el problema pide procesar eventos en orden y modificar el estado despues de cada paso?
- Estructuras que suelen aparecer: Colas, listas, arreglos y variables de estado.
- Ejemplo en clase: Josephus visto en clase, donde cada eliminacion cambia la estructura del conjunto.
- Cuando usarlo: Cuando el problema se resuelve paso a paso y cada paso depende del estado anterior.
- Cuando no usarlo: Cuando el problema admite una formula cerrada o una estrategia mas directa que no necesita simular todo.

## Patron 2: Informacion monotonica

- Problema ejemplo: Nearest Smaller Values, donde se necesita encontrar el valor menor mas cercano a la izquierda.
- Pregunta detonadora: ¿Que informacion ya no sirve y puede descartarse cuando el recorrido avanza?
- Estructuras que suelen aparecer: Pilas, listas y arreglos.
- Ejemplo en clase: El ejercicio de Nearest Smaller Values visto en clase.
- Cuando usarlo: Cuando una solucion ingenua revisa muchas veces lo mismo y se puede conservar un conjunto ordenado de candidatos.
- Cuando no usarlo: Cuando el problema necesita comparar elementos en mas de una direccion o no existe un criterio de monotonicidad claro.

## Patron 3: Backtracking / Fuerza Bruta Estructurada

- Problema ejemplo: Generar todas las combinaciones o permutaciones posibles de un conjunto (ej. el problema de la asignación o agrupamiento).
- Pregunta detonadora: ¿Se necesita explorar un espacio completo de soluciones siguiendo un conjunto de decisiones secuenciales y restricciones?
- Estructuras que suelen aparecer: Árboles de decisión (lógicos), pilas de recursión y arreglos/listas de estado.
- Ejemplo en clase o recurso consultado: La explicacion de Abdul Bari sobre el enfoque de fuerza bruta y retroceso (Backtracking) usando diagramas de árbol para rastrear las restricciones del problema.
- Cuando usarlo: Cuando el problema requiere construir una solución paso a paso y evaluar si cumple con ciertos criterios, permitiendo "regresar" si una ruta falla.
- Cuando no usarlo: Cuando el problema posee una estructura lineal simple o una solución codiciosa (greedy) que no requiere explorar múltiples caminos.

## Patron 4: Hash maps

- Problema ejemplo: Contar frecuencias de letras, palabras o eventos en una secuencia.
- Pregunta detonadora: ¿Se necesita consultar rapidamente si un elemento ya fue visto o cuantas veces aparece?
- Estructuras que suelen aparecer: Diccionarios, conjuntos y tablas hash.
- Ejemplo en clase o recurso consultado: La explicación del canal HackerRank sobre Hash Tables orientada al mapeo mediante arreglos junto con las operaciones de la documentación oficial.
- Cuando usarlo: Cuando la consulta por clave es central y se quiere rendimiento promedio O(1).
- When no usarlo: Cuando el dominio de datos es sumamente pequeño o se requiere obligatoriamente preservar un orden secuencial estricto de los elementos.

## Patrones adicionales opcionales

- Patron 5: Two pointers o sliding window, util para problemas de subarreglos y ventanas fijas.

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

- Simulacion y Backtracking se parecen en que ambos dividen el problema en una serie de decisiones secuenciales o pasos sucesivos. Se diferencian en que la simulación sigue un único camino determinado por el estado anterior, mientras que el Backtracking explora múltiples ramificaciones en forma de árbol y retrocede cuando encuentra restricciones insalvables.

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- Me parece mas dificil reconocer informacion monotonica, porque requiere identificar con precisión matemática que valores específicos pueden descartarse sin perder la respuesta correcta, lo cual no siempre es evidente a primera vista.