# Reflexion tecnica - Clase 08

Nombre: Patricio Navarro

## Ideas recurrentes

Que ideas aparecieron en varios recursos?

- No existe la estructura "perfecta": Todos los recursos (especialmente Alpaca Tech, Chio Code y Sajjad Kadeer) enfatizan que la elección depende completamente del problema (Trade-offs). Si ganas velocidad de búsqueda (como en un Hashmap), normalmente sacrificas orden o usas más memoria; si ganas velocidad de inserción (como en una Lista Enlazada), sacrificas velocidad de acceso.
- La importancia de la Notación Big O: Casi todos evalúan la utilidad de las estructuras basándose en su complejidad temporal (`O(1)` vs `O(n)`) para las 4 operaciones clave: Buscar, Acceder, Insertar y Eliminar.
- La RAM dicta las reglas: La forma física en la que los datos se guardan en la memoria (continuos como en un Arreglo, o dispersos con flechas/apuntadores como en los Nodos) define el comportamiento de la estructura.

## Comparacion critica

Compara al menos dos recursos. (Compararemos el Recurso 6: Alpaca Tech y el Recurso 8: Python Docs)

| Aspecto | Recurso A (Alpaca Tech - Video) | Recurso B (Python Docs DS - Texto) |
| :--- | :--- | :--- |
| Claridad | Muy alta y amigable. Usa analogías de la vida diaria (platos, filas). | Alta, pero requiere vocabulario técnico y conocimiento previo del lenguaje. |
| Ejemplos | Conceptuales (El botón de Control+Z para explicar Pilas). | Prácticos y aplicados (Uso de `deque` para optimizar el rendimiento). |
| Profundidad| Básica. Excelente para entender "el qué" y "el por qué". | Intermedia/Avanzada. Te dice exactamente "el cómo" implementarlo a nivel profesional. |
| Visualizaciones| Excelentes. Muestra tablas comparativas de complejidad en pantalla. | Nulas. Es solo texto escrito en la web. |
| Codigo | Casi no muestra código, se centra en la lógica algorítmica. | Abundante. Es una guía de sintaxis pura y métodos nativos. |

## Recurso mas util

Cual fue el recurso mas util para ti y por que?

- El Recurso 8 (Documentación Oficial de Python). Aunque los videos son geniales para entender la teoría, al momento de programar los ejercicios del curso, necesitas saber cómo funcionan las herramientas nativas. Aprender que Python desaconseja usar `list` como colas y te ofrece `collections.deque` te ahorra horas de frustración al intentar optimizar algoritmos como el de las ventanas móviles o Josephus.

## Recurso menos recomendable

Cual fue el recurso menos recomendable o menos claro y por que?

- El Recurso 5 (Hacktrickz). Además de tener un audio/ritmo más denso, utiliza el lenguaje C para explicar los conceptos. Dado que este curso se enfoca en Python (que abstrae el manejo dinámico de la memoria y los punteros), ver cómo se inicializan arreglos estáticos en C puede causar más confusión que claridad en este momento específico de tu aprendizaje.

## Relacion con el curso

Como se conecta esta investigacion con Josephus, Nearest Smaller Values, pilas, colas, diccionarios o pruebas?

- Josephus: Resolver este problema matemáticamente es complejo, pero programarlo iterativamente es un ejemplo perfecto del uso de Colas circulares (o `collections.deque`). Vas sacando elementos del frente y empujándolos al final hasta que toca eliminar a uno.
- Nearest Smaller Values: Este algoritmo requiere retroceder en el historial de números para encontrar el menor más cercano. Hacerlo con dos ciclos anidados tardaría `O(n^2)`, pero al usar una Pila (Stack) para mantener una "información monótona" (guardando solo los números relevantes y sacando los que ya no sirven), el tiempo se reduce mágicamente a `O(n)`.
- Diccionarios / Pruebas: Los diccionarios (Hashmaps) son vitales cuando mides tiempos de ejecución en tus pruebas. Si necesitas verificar si un número ya fue visitado o calcular sus frecuencias, hacerlo en una lista toma `O(n)`, pero en un diccionario toma `O(1)`, haciendo que tus algoritmos aprueben los test de estrés del curso.

## Preguntas nuevas

Formula al menos tres preguntas tecnicas que quieras resolver en las siguientes clases.

1. Internamente en Python, ¿cómo maneja el lenguaje las "colisiones" en un diccionario (Hashmap) para seguir garantizando que la búsqueda sea de tiempo constante `O(1)`?
2. En el problema de Nearest Smaller Values, ¿por qué el algoritmo sigue siendo `O(n)` si dentro del ciclo `for` principal tenemos un bucle `while` que hace `.pop()` a la pila? ¿No debería ser `O(n^2)`?
3. Si la estructura `collections.deque` es tan eficiente para insertar y eliminar en ambos extremos, ¿existe algún escenario donde una lista normal (`list`) siga siendo una mejor opción de diseño?

## Que explicarias diferente

Si tuvieras que explicar uno de los temas investigados a otro estudiante, que cambiarias respecto a los recursos que consultaste?

- Al explicar la Complejidad Temporal (Big O), evitaría saltar directamente a gráficas matemáticas abstractas como hacen muchos videos. En su lugar, pondría dos fragmentos de código uno al lado del otro (uno buscando en un Array y otro en un Diccionario) y usaría un "debugger" visual para que el estudiante literalmente cuente cuántos pasos (operaciones) le toma a la computadora llegar al mismo resultado en ambos casos. Ver físicamente cómo la computadora "sufre" haciendo un bucle iterativo ancla la idea mucho mejor que una gráfica de una curva exponencial.
