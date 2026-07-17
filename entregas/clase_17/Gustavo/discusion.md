# Discusión técnica — Clase 17

## 1. Nodo y lista ligada
¿Cuál es la diferencia entre un nodo y una lista ligada?
Un nodo es la pieza individual básica que almacena un valor y una o más referencias a otros nodos. En cambio, una lista ligada es el conjunto organizado de esos nodos que son alcanzables a partir de una referencia inicial, la cual es administrada por una estructura contenedora.

## 2. Cola ligada
¿Por qué una cola ligada necesita referencias al frente y al final?
Se necesitan ambas referencias para que las operaciones principales tengan una complejidad constante, O(1). El frente permite desencolar directamente sin recorrer la estructura, y el final permite encolar o enlazar un nuevo nodo en la última posición sin tener que buscar a través de toda la cadena desde el inicio.

## 3. Invariantes
¿Qué invariantes deben cumplirse cuando la cola está vacía?
Cuando la cola está vacía, deben cumplirse tres condiciones obligatorias de forma simultánea: la referencia al frente debe ser nula (`frente is None`), la referencia al final también debe ser nula (`final is None`), y el contador de tamaño debe ser exactamente 0.

## 4. Lista simple y lista doble
¿Qué ventajas y costos agrega la referencia `anterior`?
La ventaja principal es la simetría operativa, lo que permite agregar y retirar nodos desde ambos extremos de la lista en tiempo constante, O(1). El costo que esto añade es un mayor consumo de memoria por almacenar la referencia adicional en cada nodo y la obligación de realizar más actualizaciones en los enlaces para mantener la consistencia bidireccional por operación.

## 5. Deque
¿Por qué una lista doblemente ligada es adecuada para una deque?
Una lista doblemente ligada es adecuada porque una deque requiere la capacidad de insertar y eliminar elementos operando tanto por el inicio como por el final. La lista doble garantiza que estas cuatro operaciones de los extremos se realicen de manera eficiente en tiempo constante, O(1).

## 6. Complejidad
¿Por qué retirar el frente de una lista de Python no equivale a desencolar en tiempo constante?
Porque utilizar la función `pop(0)` en una lista tradicional de Python obliga a compactar internamente el arreglo, desplazando todos los elementos restantes una posición hacia la izquierda en la memoria. Este desplazamiento forzado eleva el costo de retirar el frente a O(n), perdiendo el tiempo constante O(1) que sí ofrece desencolar en una estructura ligada.

## 7. BFS
¿Por qué los nodos deben marcarse como visitados al encolarse?
Se deben marcar en el momento exacto en que se encolan para evitar que un vértice, que podría ser vecino de múltiples nodos simultáneamente, sea descubierto y agregado a la cola varias veces antes de que llegue su turno de ser desencolado. Hacerlo muy tarde genera duplicaciones masivas, especialmente en grafos densos.

## 8. Predecesores
¿Qué responsabilidad tiene el mapa de predecesores?
Su responsabilidad es mantener un registro compacto de cómo se exploró el grafo, almacenando únicamente el primer vértice predecesor desde el cual se descubrió a cada nodo. Esto permite construir el árbol BFS y reconstruir la ruta mínima sin necesidad de estar guardando caminos completos durante el recorrido.

## 9. Reutilización
¿Por qué la reconstrucción de caminos puede compartirse entre BFS y Dijkstra?
Se puede compartir porque la tarea de calcular los predecesores está completamente separada de la tarea de interpretar y reconstruir el camino. Tanto BFS, 0-1 BFS y Dijkstra calculan costos mediante lógicas diferentes, pero todos generan la misma tabla estructurada de predecesores; por ende, una única función puede rastrear e invertir esa tabla sin importar qué algoritmo la produjo.

## 10. 0-1 BFS
¿Por qué las aristas de peso cero se agregan al inicio?
Las aristas de costo cero se agregan al inicio de la deque porque representan candidatos de mejora que conservan el costo acumulado actual. Por lo tanto, tienen máxima prioridad y deben procesarse rápidamente antes de revisar los caminos que sí incrementan el costo total.

## 11. Comparación
¿En qué se diferencian BFS, 0-1 BFS y Dijkstra?
Se diferencian fundamentalmente en el tipo de pesos que soportan y la estructura auxiliar que requieren. BFS sirve para grafos donde los pesos son iguales o inexistentes y usa una cola. 0-1 BFS opera exclusivamente sobre grafos donde los pesos son de 0 o 1 exactos y requiere una deque. Dijkstra se usa para pesos generales no negativos y demanda un min-heap para la extracción del menor candidato.

## 12. Elección de estructura
¿Qué operación dominante conduce a cola, deque o heap?
El procesamiento estrictamente por orden de llegada por capas es la operación dominante que conduce a la cola simple. La necesidad de adelantar los candidatos de costo cero y posponer los de costo unitario conduce a la deque. Por último, la extracción constante de la menor distancia absoluta candidata conduce al heap.

## 13. Producción
¿Por qué en código real usaríamos `collections.deque`?
En un entorno de producción real, utilizaríamos `collections.deque` porque es una estructura madura implementada a nivel base en Python. Ya está completamente probada, asegurada para este patrón y optimizada para ocultarnos el mantenimiento de invariantes y evitar enlaces rotos accidentales.

## 14. Riesgos
¿Qué errores de referencias son más peligrosos en una lista doblemente ligada?
El error más peligroso es actualizar una sola dirección del enlace bidireccional, es decir, desincronizar el puntero `.siguiente` del `.anterior`. Esto produce una estructura engañosa que parecerá correcta y funcional al leerla de izquierda a derecha, pero que revelará enlaces rotos o bucles ocultos al intentar recorrerla de regreso.

## 15. Cierre
¿Qué estructura elegirías para pesos 0, 1 y 2? Justifica por qué 0-1 BFS ya no se aplica directamente.
Elegiría un min-heap junto con el algoritmo de Dijkstra completo. El algoritmo 0-1 BFS no se aplica directamente porque la regla de separación binaria en los extremos de la deque solo permite gestionar dos niveles lógicos de prioridad (costos de 0 o 1). La inclusión de un peso 2 crea un tercer incremento de prioridad que la deque no puede organizar internamente sin perder el orden.