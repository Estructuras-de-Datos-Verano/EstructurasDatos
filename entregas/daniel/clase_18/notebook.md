# José Daniel Molina Carrillo 

Initial Q: ¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?
- Usando el algoritmo de Kruskal: ordenamos las carreteras por costo de menor a mayor y las unimos usando, descartando las que cierran un ciclo hasta conectar todo.  
Sec 1: ¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?
- Buscamos un árbol de expansión mínima (conectar todo al menor costo total). A diferencia de un camino desde un origen, aquí no hay un punto de partida especial ni buscamos rutas individuales.
Sec 2: ¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?
- Preguntarnos constantemente si dos nodos ya están en la misma componente para evitar ciclos (union(u, v)), en lugar de buscar la menor distancia tentativa.
Sec 3: ¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?
- Porque podrías aceptar carreteras baratas que unan nodos que ya están conectados por otras vías más baratas, gastando presupuesto de forma redundante .
Sec 4: ¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?
- Dijkstra optimiza las distancias individuales desde un origen (y lo necesita). Kruskal optimiza el costo total de la red completa sin requerir un origen.
Sec 5: ¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?
- Porque empiezas con $V$ componentes aisladas y cada arista útil une exactamente dos componentes, necesitando exactamente $V-1$ uniones para fusionar todo en una sola.
Sec 6: ¿Qué información mínima necesitamos antes de aceptar una arista u–v?
- Saber si $u$ y $v$ ya pertenecen a la misma componente conexa. Si ya están conectados, agregar la arista crearía un ciclo innecesario.  
Sec 7: ¿Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?
- Las dos componentes disjuntas a las que pertenecían los nodos se fusionan en una sola, reduciendo el número total de conjuntos independientes en uno.
Sec 8: ¿Por qué conviene que union(a, b) devuelva un booleano?
- Porque nos permite tomar la decisión y actualizar la estructura a la vez: si es True aceptamos la arista y si es False la rechazamos por ciclo.
Sec 9: ¿Qué condición permite reconocer una raíz en el arreglo padre?
- Que su valor en el arreglo apunte a sí mismo
Sec 10: ¿Por qué debemos validar explícitamente los índices negativos?
- Porque en Python los índices negativos acceden al final de la lista por detrás, lo que causaría un comportamiento erróneo en lugar de lanzar un error.
Sec 11: ¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?
- Rompe la estructura de árbol y los tamaños lógicos, creando árboles incorrectamente profundos o inconsistencias al no unir las raíces reales.
Sec 12: ¿Qué invariantes viola padre = [1, 0, 2]?
- Viola el invariante de que toda cadena debe terminar en una raíz y que no debe haber ciclos cerrados, ya que el 0 apunta al 1 y el 1 al 0.
Sec 13: ¿Qué cambia y qué permanece igual durante la compresión de caminos?
- Cambia la estructura interna (conecta los nodos visitados directo a la raíz para acelerar búsquedas futuras); no cambian los tamaños, el contador ni las componentes.
Sec 14: ¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?
- Porque al colgar el árbol más pequeño del más grande, la profundidad del árbol resultante solo aumenta si ambos tenían el mismo tamaño, manteniéndolo plano.
Sec 15: ¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?
- Devuelve True (unión efectiva). Las raíces son 0 y 2, y al unirlas, la componente {2,3} se colgará de la de {0,1}, quedando 3 componentes en total.
Sec 16: ¿Cómo usa Kruskal el booleano devuelto por union?
- Si devuelve True acepta la arista para el árbol de expansión; si devuelve False, la ignora porque sus extremos ya estaban conectados (ciclo).
Sec 17: ¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?
- El costo total es 8. Se detiene al tener 4 aristas porque con 5 nodos ya alcanzamos la condición de V-1 aristas. 
Sec 18: ¿Qué condición permite distinguir un MST completo de un bosque desconectado?
- al terminar de procesar todas las aristas logramos seleccionar exactamente V-1 aristas. Si seleccionamos menos, el grafo está desconectado.
Sec 19: ¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?
- Porque ante un empate de pesos pueden existir múltiples soluciones válidas (distintos MST) con el mismo costo mínimo total.
Sec 20: ¿Qué parte domina la complejidad total de Kruskal?
- El ordenamiento inicial de las aristas por peso, que toma un tiempo de O(E log E). 
Sec 21: ¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?
- Convertir los índices de base 1 a base 0, y manejar el caso donde el resultado es None imprimiendo la palabra "IMPOSSIBLE".
Sec 22: ¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?
- En Redundant Connection las aristas se procesan en el orden en que vienen sin ordenar por peso, buscando solo el primer ciclo que se forme.
Sec 23: ¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?
- Las operaciones  con sus validaciones e invariantes antes de usarlas en Kruskal.
Sec 24: ¿Qué invariante protege una prueba de unión repetida?
- El invariante de que una unión redundante (de nodos ya conectados) no debe alterar el contador de componentes ni modificar el tamaño del conjunto.
Sec 25: ¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?
- Una estructura de grafo dirigido junto con una cola para implementar el Algoritmo de Kahn (grados de entrada) para el ordenamiento topológico.