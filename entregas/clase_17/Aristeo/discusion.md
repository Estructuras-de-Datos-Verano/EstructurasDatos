# Discusión Técnica - Clase 17

### 1. Nodo y lista ligada
Un nodo es una estructura de datos física e individual que almacena un valor y uno o más punteros de enlace. Una lista ligada es un concepto lógico que se forma al interconectar estos nodos secuencialmente a partir de una referencia inicial.

### 2. Cola ligada
Para garantizar que tanto la inserción (`encolar`) como la extracción (`desencolar`) ocurran en tiempo constante $O(1)$ sin necesidad de iterar o recorrer la lista entera.

### 3. Invariantes de cola vacía
- `_frente is None`
- `_final is None`
- `_tamano == 0`

### 4. Lista simple y lista doble
La referencia `anterior` permite realizar recorridos bidireccionales y retirar nodos desde el extremo final en $O(1)$. El costo es una mayor huella de memoria por nodo (un puntero extra) y mayor complejidad de sincronización al actualizar enlaces.

### 5. Deque
Porque permite insertar y remover elementos en ambos extremos en complejidad temporal $O(1)$ constante mediante la manipulación directa de los punteros de los extremos.

### 6. Complejidad
Retirar el primer elemento de una lista de Python (`pop(0)`) obliga al intérprete a copiar y desplazar en memoria todos los elementos restantes una posición a la izquierda, lo cual toma tiempo lineal $O(n)$.

### 7. BFS
Porque evita encolar múltiples veces un mismo vértice alcanzable desde varios caminos de la misma capa, controlando de manera óptima el consumo de memoria.

### 8. Predecesores
Registra de forma compacta el árbol de caminos mínimos, permitiendo reconstruir la ruta óptima en sentido inverso con un consumo mínimo de recursos.

### 9. Reutilización
Ambos algoritmos se dedican a resolver el mismo problema base: encontrar caminos más cortos. La diferencia radica en la manera de explorar y ordenar las transiciones, pero el mapa de predecesores resultante tiene el mismo formato lógico.

### 10. 0-1 BFS
Porque representan una transición de costo "gratuito" (peso 0). Al ponerlas al inicio de la deque, nos aseguramos de que se exploren y resuelvan en la iteración de la capa de distancia actual antes de pasar a explorar distancias mayores.

### 11. Comparación
- BFS: Sin pesos, usa Cola, $O(V+E)$.
- 0-1 BFS: Pesos binarios $\{0, 1\}$, usa Deque, $O(V+E)$.
- Dijkstra: Pesos no negativos generales, usa Heap, $O((V+E) log V)$.

### 12. Elección de estructura
- Cola: Operación dominante FIFO (orden de llegada estricto).
- Deque: Operación dominante en ambos extremos (dos prioridades discretas).
- Heap: Selección recurrente del elemento mínimo general.

### 13. Producción
Porque `collections.deque` está escrita y optimizada en C, lo que ofrece un rendimiento superior, seguridad en concurrencia y un manejo de memoria sumamente robusto.

### 14. Riesgos
El desajuste de punteros opuestos (por ejemplo, que `A.siguiente == B` pero `B.anterior != A`), lo cual rompe la integridad de los recorridos inversos y provoca comportamientos erráticos o bucles infinitos silenciosos.

### 15. Cierre
Para pesos 0, 1 y 2 no es posible aplicar directamente 0-1 BFS porque una inserción de costo 2 requeriría un tercer extremo de inserción en la deque que no existe. Se requeriría Dijkstra con un min-heap, o en su defecto, una cola de prioridad basada en 3 buckets.