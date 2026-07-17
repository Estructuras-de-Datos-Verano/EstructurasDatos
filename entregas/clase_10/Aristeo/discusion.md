# Discusión — Recorridos de grafos
## 1. De representar a recorrer
Representar un grafo es definir su estructura estática: vértices, aristas y atributos. Recorrerlo es ejecutar un procedimiento que explora esa estructura en el tiempo para extraer información dinámica: componentes, rutas o distancias. La representación responde a "qué es"; el recorrido, a "qué puedo hacer con ello".
## 2. Estrategias manuales
Antes de formalizar algoritmos podemos simular manualmente: atender primero vecinos cercanos (estrategia por niveles) o avanzar hasta un tope y retroceder (estrategia por profundidad). Estas simulaciones ayudan a intuir las estructuras de datos necesarias (cola/pila) y a preparar registros para seguimiento.
## 3. BFS
BFS (Breadth-First Search) expande la frontera por capas: visita todos los vértices a distancia k antes de pasar a k+1. Es la opción natural cuando buscamos menor número de aristas entre dos nodos o cuando necesitamos la noción de nivel.
## 4. DFS
DFS (Depth-First Search) profundiza en una rama hasta que ya no puede continuar, entonces retrocede. Es útil para exploración exhaustiva, detección de ciclos y para algoritmos que requieren backtracking. El orden resultante depende del orden de los vecinos.
## 5. Comparación
BFS y DFS comparten complejidad O(V+E) en grafos representados por listas de adyacencia, pero se comportan distinto: BFS garantiza distancias mínimas en grafos no ponderados y tiene comportamiento nivelado; DFS produce recorridos profundos y es más natural para tareas de exploración recursiva.
## 6. Visualización
Mostrar la evolución de la frontera y los estados (descubiertos, visitados) hace evidente por qué cada algoritmo se comporta así. Las visualizaciones ayudan a depurar, a validar heurísticas y a enseñar el razonamiento detrás de las elecciones (cola vs pila).
## 7. CSES
Varios problemas de CSES encajan en estos patrones: rutas más cortas entre nodos (BFS), contar habitaciones/áreas conectadas (flood-fill con BFS/DFS), y modelar laberintos (BFS para rutas mínimas, DFS para explorar). Elegir el método correcto simplifica la solución y asegura propiedades requeridas.
## 8. Pruebas
Recomiendo preparar casos de prueba que incluyan: grafos con ciclos, grafos desconectados, nodos aislados, y grafos lineales. Fijar el orden de los vecinos permite resultados deterministas y facilita la comparación entre implementaciones.
## 9. Patrón descubierto
El patrón común es: identificar la necesidad (alcance, conectividad, distancia), elegir la frontera adecuada (cola para niveles, pila para profundidad), mantener `visitados` para terminar y, opcionalmente, registrar `predecesor`/`distancia` para reconstruir rutas.
## 10. Pregunta abierta
Cómo integrar eficientemente recorridos cuando las aristas tienen pesos heterogéneos y además hay restricciones dinámicas (por ejemplo, aristas que aparecen/desaparecen): ¿qué híbridos o adaptaciones (A*, Dijkstra dinámico, BFS con capas) resultan más adecuados en entornos reales?
