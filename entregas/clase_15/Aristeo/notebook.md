# Notebook Aristeo
## 1. Por qué BFS ya no basta
### ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?
Iría directo de A a D.
### ¿Por qué contar aristas ya no es suficiente en un grafo ponderado?
Porque una ruta con mayor cantidad de aristas individuales puede tener un peso menor que una ruta directa masiva.
## 2. Recordatorio de BFS
### ¿En qué condición BFS sí garantiza caminos de costo mínimo?
Cuando todas las aristas poseen exactamente el mismo peso.
## 3. Red de ciudades conductora
## enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.
1. A → B → E = 4 + 7 = 11
2. A → C → B → D → E = 1 + 2 + 1 + 3 = 7
### ¿Qué representan nodos, aristas y pesos en esta red?
Los nodos representan ciudades, las aristas representan carreteras dirigidas disponibles entre ellas, y los pesos simbolizan el tiempo de viaje en minutos.
## 4. Distancias tentativas
### ¿Qué significa infinito en la tabla de distancias?
Una distancia tentativa inicial que indica que el nodo aún no ha sido alcanzado o descubierto por ningún camino desde el origen.
## 5. Relajación
### ¿Qué tres valores comparamos al relajar una arista?
La distancia acumulada actual del nodo origen, el peso de la arista que los conecta, y la distancia acumulada actualmente registrada en el nodo destino.
## 6. Mejoras sucesivas
### ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
Porque borrar un elemento en una posición arbitraria dentro de un min-heap es una operación costosa.
## 7. Descubrimiento de la cola de prioridad
### ¿Qué componente del par funciona como prioridad y cuál como elemento?
La distancia funcniona como prioridad y el identificador del nodo como el elemento.
## 8. Algoritmo de Dijkstra
### ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
Resuelve el problema de caminos mínimos desde un único origen en grafos ponderados, y exige de forma estricta que los pesos sean no negativos.
## 9. Pseudocódigo y entradas obsoletas
### ¿En qué momento se ignora una entrada obsoleta?
Después de ser extraída de la cola de prioridad.
## 10. Recorrido manual mínimo
### ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
(0, A),(1, B),(3, C)
## 11. Recorrido manual intermedio
### La distancia de D mejora de 6 a 4 cuando se procesa B. E se descubre con 10 desde B y mejora a 7 desde D. Esta secuencia muestra que “descubierto” no significa “terminado”.
| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` |D=4, E=10 |A:0, B:3, C:1, D:4, E:10 |D←B, E←B |
| `(4,D)` |E=7|A:0, B:3, C:1, D:4, E:7 |E←D |
| `(7,E)` | Ninguna | A:0, B:3, C:1, D:4, E:7| Ninguno|
### ¿Cuáles son las distancias finales desde A en la red conductora?
A: 0, B: 3, C: 1, D: 4, E: 7.
## 12. Reconstrucción del camino
### ¿Por qué recorremos predecesores desde el destino y después invertimos?
Porque la estructura natural apunta de hijo a padre
## 13. Visualización interactiva
### ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
El grafo visual (nodos/aristas), la tabla de distancias y el estado interno del min-heap.
## 14. Implementación
### ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
- dijkstra: Realiza el algoritmo principal calculando distancias mínimas y el mapa de predecesores.
- reconstruir_camino: Sigue el rastro hacia atrás del mapa de predecesores para devolver la lista limpia del camino.
- camino_minimo: Orquesta a las dos anteriores devolviendo tanto el costo final como el camino ordenado.
## 15. Complejidad
### ¿De dónde proviene el factor logarítmico de Dijkstra con heap?
De las operaciones de inserción y extracción del elemento mínimo de prioridad balanceada, de ahí sale lo del factor logaritmico como en los AVL
## 16. Problema guiado: entrega urgente.
### ¿Cuál es el costo y camino mínimo de A a E en la red conductora?
7 y ['A', 'C', 'B', 'D', 'E']
## 17. Limitaciones y pesos negativos
### ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
Porque Dijkstra asume que una vez que un nodo es extraído del heap con la menor distancia acumulada, entonces la distancia es definitiva.
## 18. Pruebas y revisión técnica
### ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?
Que el primer elemento de la lista sea estrictamente el origen, el último sea el destino, que todos los pasos intermedios correspondan a aristas reales existentes en el grafo y que no existan duplicados ni ciclos.
### ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?
Un caso donde un nodo reciba una actualización de distancia óptima indirecta y se verifique que la tupla vieja sea ignorada sin alterar ni volver a relajar a los vecinos cuando sea extraída.
## 19. Práctica adicional
### ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
Extraer y procesar de forma iterativa el mínimo costo acumulado actual desde un nodo origen sobre pesos no negativos.
## 20. Cierre
### ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
Optimizar el costo acumulado total -> Mantener estimaciones tentativas -> Aplicar relajación de aristas -> Procesar ordenado mediante un Min-Heap.