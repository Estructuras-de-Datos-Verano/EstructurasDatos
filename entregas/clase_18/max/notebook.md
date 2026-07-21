# Notebook clase 18 Max

## Sección 0 (Pregunta inicial)

¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?

La manera indicada de conectar todos los nodos sin crear ciclos con el menor costo posible es teniendo el árbol previamente ordenado de alguna anera, ya que así podremos ver que si queremos terminar en algún lado no necesitamos recorrerlo todo, y de cierta manera ya vamos a a saber más o menos a donde ir sin la necesidad de andar buscando.

## Sección 1 (Presentación de la clase)

¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?

Esperamos obtener un nuevo algoritmo que sea lo mejor de ambos mundos, que por un lado pueda hacer todo lo que hace un heap de manera correcta, pero por otra que tenga cierta restricción o algo por el estilo que nos permita generar ciclos de manera accidental, ahora por lo que me he espoileado se me hace que va a se el kruskal.

## Sección 2 (Recuperación de estructuras anteriores)

¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?

Lo que la distinque de las demas es que principalmente a diferencia de los otros tipos de colas y heaps, tenemos que kruskal no empieza en un nodo en especifico, si no que los recorre todos de manera global, de esta manera podemos ver el mejor camino antes de tan siquiera empezar.

## Sección 3 (Nueva pregunta: conectar toda la red)

¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?

Porque puede que el camino sea más largo, entonces a pesar que la primera sección sea más barata, ya la unión de todos los segmentos de carrtera terminara siendo bastante más costoso, por un lado, por el otro puede que sea bastante más llarga la ruta.

## Sección 4 (Dijkstra frente a Kruskal)

¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?

Dijkstra optimiza el camino optimo para ir de nodo en nodo de manera individual mientras que kruskal lo que hace es que optimiza la red completa, entonces cada uno funciona para cosas diferentes y cada una es buena en sus secciones respectivamente.

## Sección 5 (Árboles de expansión)

¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?

Necesitamos exactamente, no más no al menos, no distinto, igual a V -1 porque de esta manera nos podemos asegurar que todos los vertices estan conectados, ahora que necesitemos V -1 aristas no quiere decir que no haya más aristas conectadas

## Sección 6 (Por qué evitar ciclos)

¿Qué información mínima necesitamos antes de aceptar una arista u–v?

Necesitamos saber si las aristas ya estan conectadas de manera previa o si estan flotando en el vacio, además de que tenemos que asegurarnos que el ciclo ya etse cerrado.

## Sección 7 (Componentes conexas)

¿Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?

Cuando aceptamos una arista lo que estamos haciendo es que lo estamos metiendo a la participación correspondiente para poder tener el caminito hecho.

## Sección 8 (Necesidad de Union-Find)

¿Por qué conviene que union(a, b) devuelva un booleano?

Devuele el boolanea porque el True quiere decir que te acepta la arista nueva que se esta implementado correctamente, y el False quiere decir que se rechazado por ciclo.

## Sección 9 (Representación mediante padres)

¿Qué condición permite reconocer una raíz en el arreglo padre?

El paso cero.

## Sección 10 (Operación find)

¿Por qué debemos validar explícitamente los índices negativos?

Poruqe no es realista que una carretera tenga valor negativo, ya que esto quisiera decir ue te estan pagando por pasar por ahí en lugar de  haber pagado.

## Sección 11 (Operación union)

¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?

Debería de regresarnos un IndexError, ya que las cosas no estan bien implementadas.

## Sección 12 (Invariantes)

¿Qué invariantes viola padre = [1, 0, 2]?

El invariante del 1,0 ya que estos dos van a formar un ciclo, ya que esta preestablecido que 0 va a 1, entoces aquí no jalaria el kruskal.

## Sección 13 (Compresión de caminos)

¿Qué cambia y qué permanece igual durante la compresión de caminos?

Lo que se va actualizando es el padre pero lo que se queda igual es el camino que ya hemos ido recorriendo.

## Sección 14 (Unión por tamaño)

¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?

Porque de cierta manera se limitan las cosas para que se puedan hacer los arboles correctamente sin que se creen los ciclos.

## Sección 15 (Ejecución manual de Union-Find)

| Operación | raíces | efectiva | padres | tamaños en raíces | componentes |
| --- | --- | --- | --- | --- | ---: |
| inicio | — | — | `[0,1,2,3,4,5]` | seis unos | 6 |
| union(0,1) | 0 / 1 | sí | `[0,0,2,3,4,5]` | raíz 0:2 | 5 |
| union(2,3) | 2 / 3 | sí | `[0,0,2,2,4,5]` | raíz 2:2 | 4 |
| union(1,3) | 1 / 2 / 3 | sí | `[0,0,2,2,3,4]` | no se | 2 |
| union(0,3) | 1 / 2 / 3 / 4 | sí | `[0,0,2,2,4,4]` | no se | 1 |

¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?

Devuelve un camino mucho más corto que los demas.

## Sección 16 (Algoritmo de Kruskal)

¿Cómo usa Kruskal el booleano devuelto por union?

Se usa para poder ver bien todas las cuestiones que se nos pideny resolverlas de manera bastante clara.

## Sección 17 (Ejecución manual de Kruskal)

¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?

El  resultado final de esto va a ser un árbol bastante bueno.

## Sección 18 (Grafo desconectado)

¿Qué condición permite distinguir un MST completo de un bosque desconectado?

Lo que permite esto es la revisión correcta del árbol para la realización del mismo.

## Sección 19 (Pesos negativos, empates y casos especiales)

¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?

Porque los pesos negativos representan cosas que no nos sirven para la epresentación del código.

## Sección 20 (Complejidad)

¿Qué parte domina la complejidad total de Kruskal?

El orden es lo que domina, y esto hace bastante sentido, ya que cambiando el orden de las cosas se cambian los posibles caminos y por lo tanto se cambia el resultado final.

## Sección 21 (CSES Road Reparation)

¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?

La adaptación de hacer las cosas correctamente conectadas, y la de porder tener los nodos con la cantidad preestablecida de V-1

## Sección 22 (LeetCode Redundant Connection)

¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?

Por lo que entiendo lo que cambia principalmente es la facilidad de poder agregar nodos y conectarlos ya que en el kruskal no se termina de poder.

## Sección 23 (Implementación)

¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?

## Sección 24 (Pruebas)

¿Qué invariante protege una prueba de unión repetida?

Una vez más lo que lo proteje es el invariante del orden.

## Sección 25 (Cierre hacia ordenamiento topológico)

¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?

Se necitara la estructura de Redundant connection para poder implementar el código correctamente.

