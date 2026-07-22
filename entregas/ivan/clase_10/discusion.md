# Discusion
1. De representar a recorrer
Ya sabemos cómo guardar un grafo en código usando un diccionario (donde las llaves son los nodos y los valores sus listas de vecinos). Pero solo guardar los datos no sirve de mucho si no podemos movernos por ellos. Recorrer un grafo significa visitar cada nodo de forma ordenada, asegurándonos de revisar todo sin quedarnos atrapados en un ciclo infinito.

2. Estrategias manuales
Si te ponen un laberinto en papel, normalmente haces una de dos cosas: o intentas avanzar por todos los caminos cercanos a ti al mismo tiempo para ver cuál avanza más rápido, o te vas por un solo pasillo hasta topar con pared y luego te regresas a la última desviación. Para no dar vueltas en círculos, vas dejando una marca mental en los lugares por donde ya pasaste. 

3. BFS 
Avanzamos por niveles, como si fuera a lo ancho. Revisas primero a todos tus vecinos directos, luego a los vecinos de tus vecinos, y así te la llevas. Se usa una Cola dado que el primero que llega es el primero en salir (FIFO).
Todo se basa en sacar un nodo de la fila, checar a sus vecinos, y a los que no has visitado, meterlos a la fila.

4. DFS
Aquí te vas hasta el fondo de un camino. Exploras y avanzas hasta que ya no hay salida y una vez que topas te echas para atrás un pasito y pruebas otra ruta.
Se usa una Pila (stack). El último que entra es el primero en salir (LIFO), como los platos sucios en la cocina.
En código usamos una lista normal y sacamos el último elemento con pop().
Metemos los vecinos al revés usando reversed() para que la pila los procese en el orden natural al sacarlos.

5. Comparación
BFS te asegura encontrar el camino más corto siempre. Si usas DFS para buscar la salida de un laberinto, puede que encuentres una ruta larguísima antes de darte cuenta de que había otra salida a dos pasos de ti.Un detalle es que el BFS marca los nodos como visitados ANTES de meterlos a la fila (para no saturar la memoria con duplicados). DFS los marca DESPUÉS, justo al sacarlos de la pila, para permitir que se exploren los caminos más profundos.

6. Visualización
Ver qué está haciendo la compu ayuda muchísimo. Usamos NetworkX y Matplotlib para dibujar el grafo y le pasamos los datos de cada paso para pintar los nodos: rojo para el actual, verde para los procesados y azul para los que esperan turno.

7. CSES
Llevamos esto a la práctica con problemas típicos de programación competitiva:

Counting Rooms: Literalmente contar cuántos grupos separados de cuartos hay en un mapa. Corres un BFS o DFS desde cada casilla no visitada y cuentas cuántas veces tuviste que iniciar un recorrido.

Labyrinth: Buscar si hay camino desde el punto A hasta el B. Como piden el camino más corto, BFS era obligatorio.

Message Route: Muy parecido al laberinto. El truco fue hacer que el BFS guardara de dónde venía cada nodo (un diccionario de papás) para luego poder rastrear e imprimir la ruta exacta de regreso.

8. Pruebas
Hicimos  tests para asegurar que el código no falle con escenarios no idóneos. Comprobamos que si un nodo no tiene llaves definidas en el diccionario, usar el método .get(nodo, []) nos salva de un error. 

9. Patrón descubierto
BFS y DFS son el mismo algoritmo disfrazado. La estructura del código es casi idéntica; lo único que cambia es la estructura de datos que maneja los pendientes (una fila contra una pila) y el momento en el que decides registrar un nodo en tu lista de "visitados".

10. Pregunta abierta
¿Cómo adaptamos estos algoritmos para resolver algo como Google Maps?