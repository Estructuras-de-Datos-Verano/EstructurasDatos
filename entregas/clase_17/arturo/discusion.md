# Discusión técnica — Clase 17

## 1. Nodo y lista ligada
¿Cuál es la diferencia entre un nodo y una lista ligada?
Un nodo es una pieza individual de memoria que guarda un valor lógico y una o más referencias hacia otros elementos Una lista ligada es la estructura macro, es decir, el conjunto organizado de todos esos nodos que son alcanzables al recorrerlos desde una referencia inicial

## 2. Cola ligada
¿Por qué una cola ligada necesita referencias al frente y al final?
Necesita la referencia al frente para poder desencolar elementos directamente en tiempo O(1) sin buscar A su vez, necesita la referencia al final para poder encolar (agregar) nuevos nodos instantáneamente, evitando el costo de recorrer toda la cadena desde el inicio

## 3. Invariantes
¿Qué invariantes deben cumplirse cuando la cola está vacía?
Deben cumplirse estrictamente tres condiciones simultáneas: la referencia al frente es `None`, la referencia al final es `None`, y el atributo de tamaño es 0

## 4. Lista simple y lista doble
¿Qué ventajas y costos agrega la referencia `anterior`?
La ventaja es una flexibilidad simétrica, permitiendo retirar o agregar nodos desde ambos extremos de la estructura en tiempo O(1) El costo principal es el requerimiento de memoria adicional por nodo y la obligación de realizar más actualizaciones por cada operación, ya que ambas direcciones de la cadena deben concordar

## 5. Deque
¿Por qué una lista doblemente ligada es adecuada para una deque?
Porque la deque (double-ended queue) requiere cuatro operaciones atómicas: agregar al inicio, agregar al final, quitar al inicio y quitar al final Una lista doblemente ligada, al tener punteros simétricos y referencias externas en ambos extremos, permite ejecutar estas cuatro operaciones en O(1) constante

## 6. Complejidad
¿Por qué retirar el frente de una lista de Python no equivale a desencolar en tiempo constante?
Porque al ejecutar `pop(0)` en una lista tradicional o arreglo contiguo, todos los elementos posteriores deben desplazarse físicamente una posición hacia atrás en la memoria para rellenar el hueco, lo que cuesta O(n) iteraciones 

## 7. BFS
¿Por qué los nodos deben marcarse como visitados al encolarse?
Si un vértice se marcara como visitado recién al salir de la cola, un mismo nodo podría ser descubierto concurrentemente por múltiples vecinos y encolado múltiples veces Marcarlo al encolar evita el crecimiento exponencial de duplicaciones y sobreescrituras en grafos densos

## 8. Predecesores
¿Qué responsabilidad tiene el mapa de predecesores?
Su responsabilidad es mantener un registro compacto de conectividad, guardando para cada nodo visitado cuál fue el primer "padre" que lo descubrió (`predecesores[vecino] = actual`) Esto permite rastrear el camino mínimo de regreso sin requerir guardar las rutas completas en memoria durante la ejecución

## 9. Reutilización
¿Por qué la reconstrucción de caminos puede compartirse entre BFS y Dijkstra?
Porque tanto BFS como Dijkstra (y 0-1 BFS) abstraen su resultado en el mismo formato estándar: una tabla o mapa relacional de predecesores Al separar la lógica de cálculo (qué candidato evaluar) de la lógica de reconstrucción (ensamblar la lista de nodos), una única función coordinadora puede procesar los resultados de cualquier algoritmo

## 10. 0-1 BFS
¿Por qué las aristas de peso cero se agregan al inicio?
Porque un peso de 0 significa que este candidato mantiene exactamente el mismo costo acumulado actual Al insertarlo al inicio, el algoritmo se asegura de explorarlo prioritariamente ("gratis") antes de procesar candidatos que sí incrementaron su distancia

## 11. Comparación
¿En qué se diferencian BFS, 0-1 BFS y Dijkstra?
Se diferencian en cómo gestionan los pesos y qué estructura seleccionan: BFS asume que todas las aristas cuestan lo mismo y usa una cola 0-1 BFS asume que los pesos son exactamente 0 o 1 y usa una deque Dijkstra acepta costos no negativos generales y requiere un min-heap para priorizar dinámicamente

## 12. Elección de estructura
¿Qué operación dominante conduce a cola, deque o heap?
- **Cola:** El orden cronológico estricto de llegada por capas
- **Deque:** La política binaria de adelantar aristas de costo cero y posponer al extremo final las de costo uno
- **Heap:** La extracción continua de la menor distancia tentativa de un conjunto variable

## 13. Producción
¿Por qué en código real usaríamos `collections.deque`?
Porque es una estructura de la biblioteca estándar que ya está implementada, optimizada (típicamente en C) y exhaustivamente probada para soportar eficientemente este patrón de operaciones bidireccionales de manera segura

## 14. Riesgos
¿Qué errores de referencias son más peligrosos en una lista doblemente ligada?
El mayor riesgo es actualizar una sola dirección lógica y generar una cadena inconsistente: que la lista parezca correcta al recorrerla de izquierda a derecha (usando `siguiente`), pero esté rota o apunte a nodos muertos al recorrerla de regreso (usando `anterior`)

## 15. Cierre
¿Qué estructura elegirías para pesos 0, 1 y 2? Justifica por qué 0-1 BFS ya no se aplica directamente.
Elegiría un min-heap, pasando al algoritmo de Dijkstra 0-1 BFS ya no aplica directamente porque su política de inserción depende de los dos extremos de la deque para representar de forma binaria los dos niveles de prioridad; con la aparición de un tercer nivel (peso 2), la inserción pierde su regla evidente de O(1) constante