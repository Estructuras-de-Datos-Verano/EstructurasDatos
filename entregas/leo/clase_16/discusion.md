# Discusión clase 16 - Leonardo Daniel Arenas Serafín

## 1. Diferencia entre algoritmo correcto y función robusta.
Un algoritmo correcto es un algoritmo que no tiene errores cuando se aplica correctamente, una función robusta es una función que tiene mayor libertad en sus fronteras de entradas y que en cada caso sabe completar y detetctar errores para funcionar correctamente

## 2. Razón de separar normalización.
Para que la función principal siempre coma el mismo tipo de entrada y que esa entrada se pueda dar para una frontera amplia de distintas entradas que se normalizan en una función auxiliar

## 3. Mapping/Sequence frente a dict/list.
Mapping permite que entren estructuras de tipo key:value y no solamente diccionarios. Sequence permite que entren estructuras de tipo index y no solamente listas

## 4. TypeError frente a ValueError.
TypeError se lanza cuando la entrada no es el tipo de objeto esprado; mientras que ValueError se lanza cuando sí es el tipo correcto, pero no está dentro del dominio esperado.

## 5. Bool, NaN e infinito.
Bool es una instancia de int, por lo que es necesario hacer la disntinció. NaN es no comparable con floats, por lo que es necesario hacer la distinción. Infinito representa que todavía no hay distancia y no que sea una arista de distancia infinita.

## 6. Copia defensiva.
Antes de normalizar se admiten errores silenciosos como pesos negativos u origen no perteneciente al grafo. Lo que no solamente puede provocar que el algoritmo no funcione correctamente, sino que también provoca que haya dobles revisiones. 

## 7. Vecino implícito.
Hay veces en el que en el grafo se ve como dos vértices están conectados por una arista, pero de un lado de la arista, pero el vértice de llegada no se encuentra en el grafo. Esto saltaría un error pues no se reconoce explícitamente el vértice aunque implícitamete está. Este error se corrige al implementar el vértice faltante en la normalización

## 8. Invariante de entradas obsoletas.
Las entradas obsoletas tienen predecesor None para evitar que se pueda reconstruir un camino a partir de ellas y se reconozca el error

## 9. Responsabilidades de reconstrucción.
Se debe de diferenciar cuando hay un destino inalcanzable o un destino no existente. Esto es porque en un destino inalcanzable siempre hay camino, pero se encuentra dentro de un bucle, lo que provocaría que el algoritmo nunca termine y no detecte que no es posible; por lo que se debe de detectar para evitar esto. En un destino no existente es cuando éste no se encuentra dentro del mapa y se debe de reconocer para evitar operaciones innecesarias.

## 10. Matriz contrato–riesgo–prueba.
En el algoritmo hay ciertos parámetros que son necesarios verificar para que se pueda normalizar y que la funcion Dijkstra funcione correctamente, como por ejemplo que los pesos sean no negativos o que el origen se encuentre en el grafo.

## 11. Complejidad de normalización y Dijkstra.
Sea k el número de revisiones, la normalización tiene complejidad O(k), mientras que Dijkstra tiene complejidad O((V + E)log(V)) donde V es el número de vértices y E de aristas. Al hacer la noramlización la complejidad se vuelve simplemente O(V+E), pues la normalización detecta revisiones dobles y las evita.

## 12. Operación dominante en BFS, Dijkstra, Kruskal y topológico.
- BFS: comparación de valores por orden de entrada
- Dijkstra: comparación de valores por mínimos
- Kruskal: ordenamiento y conjunos ajenos
- Topológico: grados y colas