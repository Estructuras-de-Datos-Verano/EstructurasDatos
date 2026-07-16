# Clase 17: Discusión
#### Nombre: Patricio Navarro

## 1. Nodo y lista ligada
¿Cuál es la diferencia entre un nodo y una lista ligada?

- Un nodo es la pieza individual que almacena un valor y la referencia hacia el siguiente elemento. La lista ligada es el conjunto completo de esos nodos organizados, junto con la estructura contenedora que dicta las reglas.

## 2. Cola ligada
¿Por qué una cola ligada necesita referencias al frente y al final?

- Para garantizar que tanto la inserción como la extracción se realicen en tiempo constante `O(1)`. Al tener acceso directo a ambos extremos, evitas tener que recorrer todos los elementos uno por uno.

## 3. Invariantes
¿Qué invariantes deben cumplirse cuando la cola está vacía?

- Las variables `frente` y `final` deben apuntar a `None`, y el tamaño registrado debe ser exactamente `0`.

## 4. Lista simple y lista doble
¿Qué ventajas y costos agrega la referencia `anterior`?

- Ventaja: Permite operar simétricamente en ambos extremos en tiempo constante `O(1)`.
- Costo: Consume más memoria por nodo y exige actualizar el doble de punteros en cada operación, aumentando el riesgo de errores lógicos.

## 5. Deque
¿Por qué una lista doblemente ligada es adecuada para una deque?

- Porque una deque requiere insertar y retirar elementos por ambos extremos de manera eficiente. Los enlaces `anterior` y `siguiente` de la lista doble permiten hacer exactamente esto en `O(1)`.

## 6. Complejidad
¿Por qué retirar el frente de una lista de Python no equivale a desencolar en tiempo constante?

- Porque las listas estándar de Python están respaldadas por arreglos contiguos en memoria. Al usar `pop(0)`, el primer espacio queda vacío y el sistema está obligado a desplazar todos los elementos restantes una posición hacia atrás, lo que toma tiempo lineal `O(n)`.

## 7. BFS
¿Por qué los nodos deben marcarse como visitados al encolarse?

- Para evitar duplicaciones masivas.

## 8. Predecesores
¿Qué responsabilidad tiene el mapa de predecesores?

- Su única responsabilidad es registrar quién descubrió por primera vez a cada nodo. 

## 9. Reutilización
¿Por qué la reconstrucción de caminos puede compartirse entre BFS y Dijkstra?

- Porque resuelven la ruta de la misma manera: generando un mapa de `predecesores`. 

## 10. 0-1 BFS
¿Por qué las aristas de peso cero se agregan al inicio?

- Porque un peso de cero significa que avanzar hacia ese nodo no incrementa la distancia total. Es una mejora gratuita que debe explorarse inmediatamente antes que los candidatos que sí cuestan algo.

## 11. Comparación
¿En qué se diferencian BFS, 0-1 BFS y Dijkstra?

- Se diferencian en lo que asumen sobre los pesos de las aristas y la estructura que usan:
    - BFS: Asume que todos los pesos son iguales. Usa una cola.
    - 0-1 BFS: Asume que los pesos son exclusivamente 0 o 1. Usa una deque.
    - Dijkstra: Maneja cualquier peso positivo. Usa un min-heap (cola de prioridad).

## 12. Elección de estructura
¿Qué operación dominante conduce a cola, deque o heap?

- Cola: El orden de llegada puro (procesamiento por capas).
- Deque: La clasificación binaria en extremos (adelantar prioridad alta, postergar prioridad baja).
- Heap: La búsqueda constante del elemento con el valor mínimo absoluto en todo el conjunto.

## 13. Producción
¿Por qué en código real usaríamos `collections.deque`?

- Porque está implementada en C bajo el capó. Está altamente optimizada, libre de fugas de memoria, robusta ante casos frontera y es considerablemente más rápida y segura que cualquier implementación manual en Python puro.

## 14. Riesgos
¿Qué errores de referencias son más peligrosos en una lista doblemente ligada?

- Actualizar solo una dirección (por ejemplo, A apunta a B, pero olvidas hacer que B apunte a A) y no limpiar los punteros de los nodos retirados. Esto genera estructuras rotas que solo fallan al recorrerse en reversa, o crea "zombies" que impiden que el recolector de basura libere memoria.

## 15. Cierre
¿Qué estructura elegirías para pesos 0, 1 y 2? Justifica por qué 0-1 BFS ya no se aplica directamente.
- Elegiría el algoritmo de Dijkstra. 
- 0-1 BFS ya no aplica porque una deque solo tiene dos extremos. No existe un tercer lugar constante para insertar eficientemente las aristas con peso 2 manteniendo el orden estricto de prioridades.