

# Discusión Teórica — Algoritmo de Dijkstra

### 1. Diferencia entre distancia por aristas y por pesos
En escencia al pasra por arisatas cuantas cuantas fueron y no tomas en cuenta el peso de cada una por eso aveces te puede pesar mael programa

### 2. Significado de distancia tentativa
Una distancia tentativa es la mejor estimación de costo encontrada hasta un momento determinado de la ejecución. No se considera un valor definitivo debido a que existe la posibilidad de descubrir una ruta alternativa indirecta que reduzca el costo actual.

### 3. Relajación con un ejemplo numérico
Relajar una arista consiste en comprobar si es posible llegar a v pasando por u de manera más económica que la mejor forma registrada hasta el momento.


### 4. Razón para usar un min-heap (Cola de prioridad)
El algoritmo requiere seleccionar reiteradamente el nodo con la menor distancia tentativa pendiente. 
*   Si utilizáramos una cola FIFO** convencional, procesaríamos por orden de descubrimiento (nivel), lo cual es ineficiente en grafos ponderados.
*   Si buscáramos linealmente sobre una lista, la complejidad de extracción de este mínimo sería de O(V) por paso. 
*   El mini-heap reduce el costo de obtener y extraer el elemento de menor valor a un tiempo logarítmico de O(log V), garantizando la eficiencia del algoritmo en grafos de gran escala.

### 5. Entrada obsoleta y eliminación perezosa
Cuando relajamos una arista y encontramos una distancia menor a un nodo que ya se encuentra dentro de la cola de prioridad, se inserta una nueva tupla con la menor distancia. 

### 6. Reconstrucción mediante predecesores
Debido a que el algoritmo mantiene un mapa donde la clave es el nodo actual y el valor es su predecesor directo, la ruta se recorre desde el nodo destino hacia atrás hasta alcanzar el origen.
### 7. Complejidad temporal y espacial
*   **Complejidad Temporal:** Usando una lista de adyacencia y un min-heap, el costo asintótico se expresa como:
    O((V + E) log V)
    
*   Complejidad Espacial:
    O(V + E)
    Necesaria para almacenar la lista de adyacencia del grafo, las distancias mínimas en un diccionario, los predecesores y el heap de elementos candidatos.

### 8. Restricción de pesos no negativos
Dijkstra es un algoritmo ávido . Se basa en la premisa de que una vez extraído un nodo del min-heap, su costo actual es definitivo ya que cualquier camino alternativo futuro solo sumará costos positivos 


### 9. Caso donde BFS falla
Considera el siguiente escenario básico:
*   A a B con peso 10
*   A a C con peso 1
*   C a B con peso 2


### 10. Evidencia de tus pruebas
Las pruebas unitarias implementadas en `test_estudiante.py` validan y protegen el software contra los siguientes escenarios:


### 11. Hallazgo de la revisión técnica
Durante el análisis técnico de las implementaciones se identificó que omitir la condición de validación perezosa `if distancia_actual > distancias[nodo_actual]: continue` no provoca fallos lógicos en grafos pequeños, pero impacta la complejidad temporal en grafos de alto volumen debido a que se terminan relajando de forma redundante las aristas de candidaturas obsoletas. La adición estricta de esta comparación mitiga por completo el sobreprocesamiento.