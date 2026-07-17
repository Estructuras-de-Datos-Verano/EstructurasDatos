# Discusión técnica — Clase 18

## 1. Problema
Los caminos mínimos buscan la ruta más corta entre vértices específicos, mientras que el árbol de expansión mínima busca conectar todo el grafo al menor costo total posible.

## 2. Árbol de expansión
Porque es la cantidad exacta de aristas necesarias para conectar $V$ vértices sin formar ciclos; poner una menos desconecta el grafo y una más crea bucles.

## 3. Ciclos
Porque si ambos extremos ya están conectados por otro camino, agregar esa arista solo crearía un ciclo redundante y aumentaría el costo sin aportar conectividad.

## 4. Componentes
Representa un conjunto de elementos que ya están conectados entre sí; es decir, una "isla" aislada del resto de los nodos del grafo.

## 5. Representantes
Es el elemento líder o "jefe" de un conjunto. Sirve como la identidad única para saber si dos elementos pertenecen al mismo grupo.

## 6. `find`
Busca y devuelve el representante (la raíz) del grupo al que pertenece un elemento, recorriendo el camino de padres hacia arriba.

## 7. `union`
Porque te avisa con un `True` si realmente unió dos grupos separados, o con un `False` si ya estaban conectados, lo cual es clave para evitar ciclos en Kruskal.

## 8. Compresión
Cambia la estructura del árbol apuntando los nodos directo a la raíz para acelerar futuras búsquedas; no cambia las relaciones de conectividad ni el número de componentes.

## 9. Unión por tamaño
Para mantener el árbol lo más chato y balanceado posible, evitando que las operaciones de búsqueda se vuelvan lentas al colgar caminos largos.

## 10. Invariantes
En `padres`, que no existan ciclos y cada camino termine en una raíz propia; en `tamaños`, que el valor de la raíz refleje la suma exacta de nodos de su grupo.

## 11. Kruskal
La operación dominante es el ordenamiento inicial de todas las aristas por su peso, que toma un tiempo de O(E log E).

## 12. Grafo desconectado
Porque si hay nodos inalcanzables entre sí, Kruskal no podrá conectar todo en un solo árbol y dejará varios subárboles aislados (un bosque).

## 13. Pesos negativos
Kruskal solo decide por el orden global de las aristas, mientras que Dijkstra asume que acumular pasos siempre suma costo, fallando si encuentra "atajos" negativos después.

## 14. Empates
Porque si hay varias aristas con el mismo peso mínimo, elegir una u otra puede generar árboles de formas distintas pero con exactamente el mismo costo total.

## 15. Complejidad
Sigue siendo el ordenamiento de las aristas (O(E log E)), ya que las operaciones de Union-Find con compresión y rango son casi instantáneas.

## 16. Comparación
La cola optimiza FIFO, la deque accesos en ambos extremos, el heap extrae extremos (mínimos/máximos) en O(1), y Union-Find optimiza la fusión y consulta de conjuntos disjuntos.

## 17. Production
Python interpretaría los índices negativos como accesos desde el final del arreglo (`-1` sería el último nodo), rompiendo silenciosamente la lógica y mezclando grupos incorrectos.

## 18. Cierre
Para procesar tareas según sus dependencias necesitarías un Ordenamiento Topológico, el cual se apoya típicamente en una búsqueda en profundidad (DFS) o en el Algoritmo de Kahn.