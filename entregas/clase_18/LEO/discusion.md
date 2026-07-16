# Discusión técnica — Clase 18 - Leonardo Daniel Arenas Serfín

## 1. Problema
#### ¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?
Los caminos mínimos evaluan los caminos posibles entre un nodo origen y uno destino mientras que el de expansión mínima solo evalúa costos mínimos de aristas entre dos nodos

## 2. Árbol de expansión
#### ¿Por qué una solución tiene \(V-1\) aristas?
Porque solo puede existir un camino entre dos nodos, por lo que en V nodos solo puede haver V-1 aristas

## 3. Ciclos
#### ¿Por qué se rechaza una arista cuyos extremos ya están conectados?
Porque así se caería en un ciclo, lo cual debemos evitar

## 4. Componentes
#### ¿Qué representa una componente en Union-Find?
Representa un conjunto de nodo(s) que deben de ser conectados con los demás

## 5. Representantes
#### ¿Qué significa la raíz de un elemento?
Es el índice de dicho elemento

## 6. `find`
#### ¿Qué operación realiza `find`?
Busca qué nodos están conectados con el que se busca

## 7. `union`
#### ¿Por qué conviene que `union` devuelva un booleano?
Para saber si es posible pasar con la construcción del camino si es True, no si es False

## 8. Compresión
#### ¿Qué cambia y qué no cambia con la compresión de caminos?
No cambia nada sobre la lógica externa y los contadores del algoritmo, pero cambia la lógica interna en sentido que se detectan que nodos están conectados por transitividad

## 9. Unión por tamaño
#### ¿Por qué se coloca el árbol pequeño debajo del grande?
Para así evitar que el árbol grande llegue a una profundidad extrema y desequilibre la búsqueda

## 10. Invariantes
#### ¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?
Los padres son los índices de las raíces, los tamaños van en orden de los índices de los padres, una raíz es su propio padre

## 11. Kruskal
#### ¿Cuál es la operación dominante de Kruskal?
Verificar si existe una conexión entre nodos

## 12. Grafo desconectado
#### ¿Por qué Kruskal puede terminar con un bosque?
Porque puede llegar a ser el caso en que los nodos no se concten y no se pueda encontrar la red global

## 13. Pesos negativos
#### ¿Por qué Kruskal acepta pesos negativos y Dijkstra no?
Porqu Dijkstra lleva orden de prioridad de mínimos, que al tener neativos puede llevar a errores silencioso. Como Kruskal no lleva un orden, pues no construye caminos de origen a destino, sino que construye redes globales, los negativos no provocan error alguno.

## 14. Empates
#### ¿Por qué puede haber varios árboles de expansión mínima?
Porque puede ser que existe más de una sola red

## 15. Complejidad
#### ¿Qué parte domina la complejidad de Kruskal?
La parte de ordenar los nodos

## 16. Comparación
#### Compara cola, deque, heap y Union-Find según la operación que optimizan.
Cola sigue comportamiento FIFO. Deque sigue el comportamiento deseado por extremos. Heap ordena con base en un criterio de prioridad. Union-Find comprueba mínimos y busca conexión entre la totalidad de nodos.

## 17. Producción
#### ¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?
Que podría empezarse a tomar las raíces a la mitad, provocando que nunca se llegue a una red global.

## 18. Cierre
#### ¿Qué estructura se necesitaría para procesar tareas según dependencias?
Un árbol en donde solo se puede acceder a los hijos a partir de la raíz de la totalidad del árbol.