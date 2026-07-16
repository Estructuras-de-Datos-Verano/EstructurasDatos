# Discusión clase 10 - Leonardo Daniel Arenas Serafín

## 1. De representar a recorrer.
La representación de un grafo es simplemente la creación del mismo y su mera ilustración para su visualización, mientras que el recorrdio implica un análisis y el establecimiento de jerarquía. Una analogía puede ser como una ciudad: el diseñar las calles es la representación y el caminarlas es el recorrido.

## 2. Estrategias manuales.
- Estrategia por niveles: En la estrategia por niveles, debemos de primero empezar en un paso 0 para después ir recorriendo todos los vecinos cercanos a éste, para después, recorrer ahora los vecinos cercanos a estos vecinos sin repetir el origen y así en una iteración de vecinos hasta agotar el grafo
- Estrategia por profundidad: En la estrategia por profundidad debemos de primero empezar en un paso 0 para después alegir uno de los vecinos cercanos y recorrer el grafo hasta que ya no podamos llegar a otro vecino que esté más adelante, entonces regresamos a donde iniciamos y hacemos lo mismo para el siguient vecino y así continúa la iteración hasta agotar todo el grafo

## 3. BFS.
Técnica de recorrido de un grafo en donde primero se recorren los vecinos más cercanos antes de avanzar al siguiente nivel. Se usa la estructura de cola pues queremos ir descartando los primeros nodos que fueron visitados para ir avanzando

## 4. DFS.
Técnica de recorrido de un grafo en donde se recorre toda la línea de los vecinos del origen hasta que no se pueda acceder a un nivel superior, para después regresarse y hacer lo mismo con los demás caminos. Se utilza la estructura de pilas pues para poder seguir avanzando con las demás líneas de vecinos es necesario deshacerse de los últimos nodos visitados.

## 5. Comparación.
Ambas estrategias son muy buenas y su utilidad depende de la finalidad del recorrido. Considero que el BFS es muy bueno para hacer un análiss exhaustivo del grafo, para conocer todas las posibilidades. En cambio considero que el DFS es mejor para hacer un análisis intensivo del grafo, para conocer posibiliades específicas.

## 6. Visualización.
La visualización de un recorrido de un grafo es algo muy útil pues establece cierto o jerarquía en un grafo al incilizar en un origen y avanzar a sus vecinos. Cosa que en la mera representación no es posible hacer.

## 7. CSES.
### - Counting Rooms:
#### ¿Qué representa un nodo? 
Representa suelo
#### ¿Qué representa una arista?
Representa la continuidad que hay entre dos suelos, es decir, que no haya un muro en medio
#### ¿Qué significa visitar un nodo?
Signfica caminar sobre el suelo relacionado a tal nodo
#### ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Dónde ya has pisado

### - Labyrinth:
#### ¿Qué representa un nodo?
Representa suelo
#### ¿Qué representa una arista?
Representa la continuidad que hay entre dos suelos, es decir, que no haya un muro en medio
#### ¿Qué significa visitar un nodo?
Signfica caminar sobre el suelo relacionado a tal nodo
#### ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Dónde ya has pisado, y más específicamente el recorrido que llevas para poder encontrar el camino más óptimo

### - Message Route:
#### ¿Qué representa un nodo?
Representa una computadora
#### ¿Qué representa una arista?
La conexión entre dos computadoras
#### ¿Qué significa visitar un nodo?
Significa que el mensaje salte de una computadora a otra
#### ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
De dónde proviene el mensaje

## 8. Pruebas.
De las 14 pruebas realizadas, 13 fueron correctamente hechas y solamente una fallo. La que fallo fue una que yo mismo implementé y considero que el error no está en el algoritmo de la estructura sino en mi propio entendimiento de las funciones. Yo diseñé las siguientes pruebas: test_todo_bfs_y_dfs_ordenes_distintos(), test_todo_nodo_aislado(), test_todo_no_visita_repetidos(). E implementé por mi propia cuenta las siguientes pruebas: test_recorrido_paso0_LEO(), test_grafo_uniforme_bfs_y_dfs_iguales_LEO()

## 9. Patrón descubierto.
#### - BFS
BFS sigue un patrón en donde se visitan exhaustivamente todos los posibles caminos posibles a la vez. No busca específicamente saber si es posible llegar a un lugar, sino que simplemente analiza cuáles son todos los lugares posibles a los que se puede llegar. De la misma manera no busca específicamente la distancia mínima entre nodos, sino que encuentra todas las distancias que hay entre todos los nodos

#### - DFS
DFS sigue un patrón en donde se visitan intensívamente los posibles caminos, pues no para hasta llegar al final. Busca específicamente si es posible llegar a un lugar y encuentra la distancia mínima entre puntos, a diferencia del BFS.

## 10. Pregunta abierta.
Hemos visto como es posible recorrer de diferentes formas un grafo en cuestión de cuáles son los pasos a seguir. Pero ¿qué es lo que cambiaría en el recorrido de un grafo al cambiar el origen para ambas implementaciones? ¿Existe alguna diferencia crucial al hacer esto o simplemente altera el orden de salida del recorrido?