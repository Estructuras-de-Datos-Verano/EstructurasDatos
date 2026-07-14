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
...
## 8. Algoritmo de Dijkstra
### ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
...
## 9. Pseudocódigo y entradas obsoletas
### **Actividad:** subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.
...
### ¿En qué momento se ignora una entrada obsoleta?

...
## 10. Recorrido manual mínimo
### ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
...
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
...
## 12. Reconstrucción del camino
### ¿Por qué recorremos predecesores desde el destino y después invertimos?
...
## 13. Visualización interactiva
### ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
...
## 14. Implementación
### ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
...
## 15. Complejidad
### ¿De dónde proviene el factor logarítmico de Dijkstra con heap?
...
## 16. Problema guiado: entrega urgente
### Compara al final con dos alternativas: A→B→E y A→C→D→E. Explica por qué una ruta con más aristas puede ser mejor.
...
### ¿Cuál es el costo y camino mínimo de A a E en la red conductora?
...
## 17. Limitaciones y pesos negativos
### ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
...
## 18. Pruebas y revisión técnica
### ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?
...
### ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?
...
## 19. Práctica adicional
### ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
...
## 20. Cierre
### ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
...