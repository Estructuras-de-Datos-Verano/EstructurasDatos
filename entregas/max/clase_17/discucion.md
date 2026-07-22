# Discusión técnica — Clase 17

## 1. Nodo y lista ligada
El nodo es nomas la celda individual que guarda un valor y las referencias, y la lista ligada es toda la estructura con reglas que va organizando a esos nodos.

## 2. Cola ligada
Para poder meter elementos al final en tiempo O(1) y sacar del principio en O(1) sin tener que chutarte el recorrido de toda la cadena cada vez.

## 3. Invariantes
Si esta vacia el frente es None, el final es None y el tamaño a fuerza es 0.

## 4. Lista simple y lista doble
La gran ventaja es que puedes ir para atras o meter/sacar cosas de ambos lados rapidisimo, el costo obvio es que gastas más memoria en referencias y tienes que tener mucho cuidado de que el anterior y el siguiente siempre concuerden.

## 5. Deque
Porque como la lista doble tiene referencias por los dos lados, es perfecta para agregar o quitar tanto por el inicio como por el final en tiempo constante (O(1)).

## 6. Complejidad
Porque en la lista de python normal (arreglos de memoria continua) si sacas el primero tienes que recorrer tooodos los demas elementos un lugar a la izquierda, por lo que te sale en O(n) y repites trabajo.

## 7. BFS
Para no duplicar trabajo, si los marcas hasta que salen se pueden volver a encolar varias veces por diferentes vecinos y se hace un despapaye en grafos grandes.

## 8. Predecesores
Ocupa nomas registrar el primer predecesor por el que se descubrio el vertice, para asi poder reconstruir todo el camino de reversa sin guardar las rutas completas en memoria.

## 9. Reutilización
Porque la forma de guardar los predecesores en el diccionario y de irse para atras hasta que llegas al origen es exactamente la misma logica, sin importar si usaste cola o heap para llenar el diccionario.

## 10. 0-1 BFS
Porque como no cuestan nada extra, se tienen que procesar al mismo nivel de prioridad actual sin tener que formarse hasta el final con los que si cuestan 1.

## 11. Comparación
En la estructura que ocupan segun los pesos. BFS normal usa Cola (pesos iguales), 0-1 BFS usa Deque (pesos de cero y uno), y Dijkstra usa Heap (pesos diferentes en general).

## 12. Elección de estructura
BFS (orden de llegada) lleva a cola, 0-1 BFS (costo 0 vs 1) lleva a deque, y Dijkstra (extraer el más barato de muchos pesos) lleva a heap.

## 13. Producción
Porque collections.deque esta hecha en C y esta optimizadisima para no tener errores en invariantes que nosotros podriamos regar haciendolo a mano.

## 14. Riesgos
Que rompas la estructura en un solo sentido, tipo que de izquierda a derecha la lista se lea bien pero de regreso no, porque no actualizaste los dos enlaces (anterior y siguiente) al mismo tiempo.

## 15. Cierre
Para pesos 0, 1 y 2 ocupariamos Dijkstra con heap, porque el truco de la deque nomas jala cuando son puros extremos (inicio y final = 0 y 1). Ya con un 2 se nos rompe el truquito binario.