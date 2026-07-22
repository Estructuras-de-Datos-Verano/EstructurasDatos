Discusión técnica — Clase 17
1. Nodo y lista ligada
¿Cuál es la diferencia entre un nodo y una lista ligada?
Un nodo es solo una pieza
2. Cola ligada
¿Por qué una cola ligada necesita referencias al frente y al final?
Para hacerla más eficiente
3. Invariantes
¿Qué invariantes deben cumplirse cuando la cola está vacía?
Que el tamaño sea 0
4. Lista simple y lista doble
¿Qué ventajas y costos agrega la referencia anterior?
Que podemos ir en ambas direcciones
5. Deque
¿Por qué una lista doblemente ligada es adecuada para una deque?
Porque podemos sacar de cualquier punto cuando cambian prioridades
6. Complejidad
¿Por qué retirar el frente de una lista de Python no equivale a desencolar en tiempo constante?
Porque actualiza otros valores
7. BFS
¿Por qué los nodos deben marcarse como visitados al encolarse?
Para evitar ciclos
8. Predecesores
¿Qué responsabilidad tiene el mapa de predecesores?
Garantizar las conecciones
9. Reutilización
¿Por qué la reconstrucción de caminos puede compartirse entre BFS y Dijkstra?
Porque ambos buscan rutas mínimas
10. 0-1 BFS
¿Por qué las aristas de peso cero se agregan al inicio?
Porque son de mayor prioridad
11. Comparación
¿En qué se diferencian BFS, 0-1 BFS y Dijkstra?
QUe BFS contempla aristas de igual valor, en 0-1 algunas pueden valer 0, en Dijkstra pueden valer distinto
12. Elección de estructura
¿Qué operación dominante conduce a cola, deque o heap?
Desencolar
13. Producción
¿Por qué en código real usaríamos collections.deque?
Porque python ya la tiene implementado convenientemente
14. Riesgos
¿Qué errores de referencias son más peligrosos en una lista doblemente ligada?
los ciclos
15. Cierre
¿Qué estructura elegirías para pesos 0, 1 y 2? Justifica por qué 0-1 BFS ya no se aplica directamente.
Dijkstra
Porque sólo contempla valores entre 0 y 1