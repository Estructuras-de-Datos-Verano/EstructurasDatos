# Discusión técnica — Clase 18

## 1. Problema
Los caminos mínimos optimizan la distancia desde un único nodo de origen a los demás de forma individual, mientras que el árbol de expansión mínima minimiza la suma total de las aristas necesarias para mantener conectados a todos los nodos de la red.

## 2. Árbol de expansión
Porque iniciamos con V componentes disjuntas y cada arista útil reduce exactamente en uno el número de componentes. Para llegar a una única componente conexa se necesitan exactamente V-1 fusiones.

## 3. Ciclos
Porque si ambos extremos ya se encuentran conectados a través de otros caminos, añadir esa arista genera una ruta redundante (ciclo) que aumenta el costo global sin ofrecer nueva conectividad.

## 4. Componentes
Representa un conjunto disjunto de nodos en el que todos están conectados entre sí de manera directa o transitiva, compartiendo un único representante común.

## 5. Representantes
Es el nodo raíz de la componente al que apuntan directa o indirectamente todos sus miembros. Sirve de identificador único para verificar pertenencia grupal.

## 6. `find`
Recorre la cadena de padres de un elemento hacia arriba hasta encontrar la raíz de su componente y comprime el camino haciendo que los nodos intermedios apunten directamente a ella.

## 7. `union`
Permite verificar la pertenencia a la misma componente y fusionar los conjuntos en una sola operación atómica, optimizando el rendimiento al evitar llamadas duplicadas a la raíz.

## 8. Compresión
Cambia la estructura del árbol acortando las distancias de los nodos hacia la raíz, disminuyendo costos de futuras búsquedas; no altera la partición lógica de los conjuntos ni el conteo de componentes.

## 9. Unión por tamaño
Se coloca el árbol pequeño bajo la raíz del grande para controlar el crecimiento vertical de la estructura, limitando la altura de los árboles y manteniendo las operaciones de búsqueda casi constantes.
 y domina la complejidad del algoritmo.

## 12. Grafo desconectado
Porque si el grafo original no es conexo, las aristas disponibles se agotarán antes de poder seleccionar las V-1 requeridas, resultando en un bosque de múltiples componentes desconectadas.

## 13. Pesos negativos
Kruskal solo requiere ordenar las aristas globalmente, lo cual funciona con valores negativos. Dijkstra asume que acumular costos nunca reduce la distancia total, por lo que falla ante aristas negativas.

## 14. Empates
Porque si hay varias aristas con el mismo costo mínimo que previenen ciclos, elegir una u otra de forma intercambiable producirá árboles físicamente diferentes pero con idéntico costo total de expansión.

## 15. Complejidad
El proceso de ordenación de las aristas por peso, que requiere un tiempo de O(E log E).

## 16. Comparación
La cola optimiza el acceso FIFO; la deque optimiza inserción y extracción en ambos extremos; el heap optimiza la extracción del elemento mínimo o máximo; y Union-Find optimiza la comprobación y fusión de componentes.

## 17. Producción
Se podría consultar de forma accidental el final de la lista por la indexación negativa nativa de Python, generando incoherencias de datos silenciosas muy difíciles de depurar en producción.

## 18. Cierre
Se necesitaría una lista de adyacencia para representar las relaciones de dependencia, un arreglo de grados de entrada para identificar tareas libres de requisitos y una cola para procesarlas secuencialmente.