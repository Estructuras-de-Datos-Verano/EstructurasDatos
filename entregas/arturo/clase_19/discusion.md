# Discusión técnica — Clase 19

## 1. Dependencias
¿Qué significa una arista \(u \to v\) en un grafo de dependencias?
Significa que la tarea $u$ debe completarse obligatoriamente antes que la tarea $v$ Es una relación asimétrica que expresa precedencia

## 2. DAG
¿Qué es un grafo dirigido acíclico y por qué es necesario?
Un DAG (Directed Acyclic Graph) es un grafo que conserva la dirección de sus aristas y no contiene ningún camino que regrese a su punto de partida Es matemáticamente necesario porque un grafo dirigido tiene un orden topológico válido si y solo si no contiene ciclos

## 3. Grado de entrada
¿Qué representa el grado de entrada de un nodo?
Representa la cantidad de aristas que llegan a él; en el contexto de dependencias, indica cuántos requisitos directos siguen pendientes antes de poder iniciar esa tarea

## 4. Nodos disponibles
¿Por qué un nodo con grado cero puede procesarse?
Porque un grado de entrada actual igual a cero significa que la tarea ya no tiene requisitos pendientes y puede ejecutarse inmediatamente sin violar ninguna dependencia

## 5. Actualización
¿Qué representa disminuir el grado de un vecino?
Representa lógicamente que una de sus dependencias previas acaba de quedar satisfecha tras procesar el nodo actual

## 6. Cola
¿Por qué Kahn utiliza una cola?
Utiliza una cola (como `collections.deque`) para almacenar y recuperar en tiempo O(1) los nodos que van alcanzando un grado de entrada cero Esto permite procesar secuencialmente las tareas disponibles sin volver a buscar en todo el grafo

## 7. BFS frente a Kahn
¿En qué se parecen y en qué se diferencian?
Ambos algoritmos utilizan una cola como estructura auxiliar principal Sin embargo, se diferencian en la regla para encolar: BFS encola cualquier vecino apenas lo descubre, mientras que Kahn exige que el vecino espere y solo lo encola cuando todas sus dependencias previas se han procesado (su grado llega a cero) Además, un ciclo no impide recorrer el grafo en BFS, pero sí impide ordenarlo en Kahn

## 8. Invariantes
¿Qué propiedad debe cumplir todo nodo que está en la cola?
El invariante central es que todo nodo que ingresa y permanece en la cola tiene un grado de entrada actual de exactamente cero

## 9. Ciclos
¿Cómo detecta Kahn que existe un ciclo?
Lo detecta comprobando al final si la cantidad de nodos procesados (`len(orden)`) es distinta a la cantidad de nodos totales en el grafo normalizado (`len(normalizado)`) Si son distintos, significa que una componente no pudo liberar sus dependencias y se quedó bloqueada por un ciclo

## 10. Órdenes múltiples
¿Por qué puede haber más de un orden topológico?
Porque si varios nodos tienen grado cero de manera simultánea, cualquiera de ellos puede procesarse primero sin violar el contrato, lo que da lugar a múltiples permutaciones o caminos válidos

## 11. Validación
¿Cómo puede verificarse un orden sin ejecutar nuevamente Kahn?
Construyendo un diccionario de posiciones para la secuencia entregada (`posicion = {nodo: indice...}`) y luego iterando sobre todas las aristas $u \to v$ del grafo para confirmar que siempre se cumpla la condición `posicion[u] < posicion[v]`

## 12. Duplicados
¿Por qué conviene eliminar dependencias repetidas?
Porque si una dependencia $A \to B$ se cuenta dos veces al calcular grados, pero solo se reduce una vez al procesar $A$, el nodo $B$ se quedará bloqueado para siempre Si se redujera de más, se generarían grados negativos Normalizar evita estas inconsistencias

## 13. Nodos aislados
¿Cómo debe aparecer un nodo aislado en el resultado?
Debe aparecer exactamente una sola vez en cualquier lugar del orden resultante, ya que al no tener dependencias, inicia automáticamente con grado cero y entra a la cola

## 14. Cola ligada
¿Podría utilizarse la ColaLigada de la Clase 17?
Sí, la misma política FIFO puede implementarse perfectamente utilizando los métodos `encolar`, `desencolar` y `esta_vacia` de la `ColaLigada` diseñada en la Clase 17

## 15. Heap
¿Cuándo convendría sustituir la cola por un heap?
Convendría cuando el contrato del problema exige devolver un desempate específico, como el orden lexicográficamente mínimo El min-heap se encargaría de extraer siempre el menor nodo disponible en lugar de cualquier nodo disponible

## 16. Complejidad
¿Por qué la complejidad es \(O(V+E)\)?
Porque las fases de Kahn son consecutivas y aditivas: normalizar recorre nodos y dependencias, y luego el bucle principal encola/procesa cada nodo como máximo una sola vez y reduce cada arista exactamente una vez No existen iteraciones globales repetidas por cada nodo, evitando una complejidad multiplicativa

## 17. Comparación
Compara BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn.
*   **BFS:** Usa una cola para procesar rutas por niveles cronológicos (sin pesos)
*   **0-1 BFS:** Usa una deque para atender aristas de costo cero al inicio y posponer al final las de costo uno
*   **Dijkstra:** Usa un min-heap para extraer iterativamente la ruta con la menor distancia (pesos generales)
*   **Kruskal:** Usa Union-Find para consultar rápidamente si la unión de componentes crea ciclos en la red
*   **Kahn:** Usa una cola combinada con una tabla de grados para organizar y ordenar jerárquicamente tareas con dependencias bloqueantes

## 18. Cierre
¿Cuál es la operación dominante del ordenamiento topológico?
La operación dominante repetida a lo largo de todo el algoritmo es elegir y procesar una tarea que ya no tiene requisitos pendientes