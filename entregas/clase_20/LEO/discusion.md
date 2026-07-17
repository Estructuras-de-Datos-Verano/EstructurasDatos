# Discusión técnica — Clase 20

Nombre: Leonardo Daniel Arenas Serafín

## Escenario 1 movilidad urbana A3

- Problema y objetivo: tenmos una aplicación gps para poder decidir cuál es el camino óptimo desde un origen hasta un destino
- Dirección y pesos: Las calles no tienen sentido fijo, y los pesos son minutos no negativos
- Operación dominante: Ir evaluando posibles caminos e ir guardando el camino óptimo en cuestión de minutos
- Estructura y algoritmo: La estructura que se usaría sería heap con el algoritmo Dijkstra
- Contrato: no hay costos negativos
- Alternativa descartada: La alternativa podría ser Kruskal porque se mapea la ciudad y te da todas las opciones, pero esto mas bien sería como la base de datos en la que trabaja la aplicación y no la solución
- Módulo previo reutilizado: Dijkstra
- Adaptación de entrada/salida: La entrada sería la misma, grafo con origen y destino. La salida también, camino a seguir y costo
- Prueba distintiva: Probar que número de calles no es proporcional a tiempo.
- Complejidad e interpretación: Complejidad de O(E log E)

## Escenario 2 movilidad urbana A1

- Problema y objetivo: tenmos una aplicación gps para poder decidir cuál es el camino óptimo desde un origen hasta un destino
- Dirección y pesos: Las calles no tienen sentido fijo, y su peso es unitario
- Operación dominante: Ir evaluando posibles caminos e ir guardando el camino óptimo en cuestión de número de calles
- Estructura y algoritmo: se usa la cola con BFS
- Contrato: el mínimo camino es el de mínimo de aristas
- Alternativa descartada: La alternativa podría ser Dijkstra porque se busca lo mismo y sería útil pues resolvería el problema, sin embargo su complejidad sería mayor
- Módulo previo reutilizado: BFS
- Adaptación de entrada/salida: Misma entrada y salida
- Prueba distintiva: Que todo camino tiene costo unitario
- Complejidad e interpretación: O(E + V)

## Caso fuera del alcance

movilidad urbana A2: ya que a pesar de que parece ser que al tener 0 y 1 se puede usar 0-1 BFS, en realidad no hay forma de decir el camino mínimo con los algoritmos que usamos, pues ninguno es como un árbol de deques.

## Reflexión final

Que antes no tenía realmente un proceso de decisión, simplemente era intuición. Ahora puedo hacer un proceso de análisis y evaluación de posibles estructras aplicadas para encontrar la que resuelva el problema de manera óptima.

