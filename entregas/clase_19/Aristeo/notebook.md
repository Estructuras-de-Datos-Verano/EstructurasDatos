# Notebook - clase_10 - Aristeo

## Seccion 1 (Presentación de clase)

¿Qué cambia entre representar un grafo y recorrerlo?

Por lo que entiendo con una analogía representar un grafo es como hacer el mapa de una ciudad y recorrerlo es como caminar sobre sus calles.

## Sección 2 (Problemas Cses)

1. ¿Qué representa un nodo?

Un nodo rpresenta una entidad discreta, osea un punto dentro de una red uqe sirve como un tipo de vertice para esta misma red.

2. ¿Qué representa una arista?

Una arista representaría el camino por donde se conectan los nodos, que en este caso, serian los procedimientos o metodos a seguir para llegar de nodo a nodo

3. ¿Qué significa visitar un nodo?

Consultar su información

4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?

Necesitaria conocer la forma en las que se conectas los nodos, porque si es de manera circular podemos llegarlos a repetir

## Sección 4 (Estrategia por niveles)

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | B, C, D, E, F | A | A |
| 1 | D, E, F, C | A, B | B |
| 2 | D, E, F, C | A, B, C | A |
| 3 | D, E, F | A, B, C | C |
| 4 | E, D | A, B, C, F | F |
| 5 | E, D | A, B, C, F | C |
| 6 | E, D | A, B, C, F | A |
| 7 | E, D | A, B, C, F | B |
| 8 | E | A, B, C, D, F | D |
| 9 | No hay | A, B, C, D, F, E | E |


¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?

Si simpre atendemos al pendiente más antiguo, la estructura que estamos utilizando es la de las colas, ya que estamos agarrando los elementos más antiguos o mejor dicho los que estan hasta abajo de la pila.

## Seccion 5 (Estrategia por profundidad)

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | B, C | A | A |
| 1 | D, E | A, B | B |
| 2 | No hay | A, B, D | D |
| 3 | E | A, B, D | B |
| 4 | No hay | A, B, D, E | E |
| 5 | No hay | A, B, D, E | B |
| 6 | C | A, B, D, E | A |
| 7 | F | A, B, C, D, E | C |
| 8 | No hay | A, B, C, D, E, F | F |


¿Qué estructura aparece si siempre atendemos el pendiente más reciente?

En este caso, la estructura que parece que estamos ocupando es la de la pila, porque debemos quitar el elemanto superior para poder manipular el que tenemos debajo de el.

## Sección 6 (BFS y DFS)

Viendo las tablas anteriores y las respuestas a las preguntas ya hechas, se ve claramente por que una ocupa colas y la otra ocupa pilas, en la primera las colas se usan para poder visitar más de un vecino a la vez, mientras en la segunda se necesitan pilas para justamente evitar esto ultimo e ir de nodo en nodo de manera individual.

## Sección 7 (Pseudocódigo)

Lo que pasaria es que no tendriamos un BFS, tendriamos un DFS, ya que su estructura es practicamente la misma, unicamente cambia la estructura de pilas y colas, por lo que no se va a poder modificar como queriamos.

## Sección 8 (Implementación)

¿Por qué necesitamos un conjunto de descubiertos o visitados?

Para que no se vayan a repetir varias veces los nodos que ya visitamos.

## Sección 9 (Regristro paso a paso)

¿Qué ventaja tiene registrar la ejecución paso a paso?

La ventaja principal es que como despues de muchas iteraciones tenemos muchos pasos realizados, ya llendo de tras para adelante y de adelante para atras en el código cuando cometemos un error puede llegar a ser confunso donde sucedio, así si registramos todo el procedimiento, cuando cometamos un error sabremos exactamente donde fue y si sabemos donde fue, vamos a saber que tipo de error se cometio, y lo podemos solucionar más facilmente.

## Sección 10 (Visualización)

¿Qué puede mostrar una animación que una lista de nodos no muestra?

Además del apoyo visual para entender el problema que se esta resolviendo, sirve para ver todo el recorrido para poder ver nodos en concreto para ver la información que tengamos en el y como modificarlo y así.

## SecciÓn 11 (Diseño de pruebas)

Diseño BFS
```text

Para esta prueba, el nodo de inicio sera el A, que esta conectado a B y A C, y C esta conectado a D.

Lo que tiene que suceder es que de A se tiene que ir a B o C, luego tiene que regresar a A e irse al otro (Suponiendo que al primero que se va es a B, entonces se iria a C), luego de C se va a D y termina el código.

```

Diseño DFS
```text

Para esta prueba la iniciaremos igual que la pasada, el nodo de inicio sera el A, que esta conectado a B y A C, y C esta conectado a D.

Lo que tiene que suceder es que de A se tiene que ir a B o C, luego si se va a B, como B no esta conectado a nada se regresa a A, si se va a C se tiene que ir a D y termina el código.

```

## SecciÓn 12 (CSES aplicado)

1. ¿Cuál algoritmo usarías para Message Route y por qué?

Para este problema siento que utilizar DFS es más que suficiente, poruqe no hay que ir llendo y regresando tanto en los nodos, por lo que siento que es más eficiente para resolver este problema en especifico.

2. ¿Cuál usarías para Counting Rooms?

Ocuparía el BFS, porque siento que las colas son bastante util para l a hora de crear los cuartos.


3. ¿Cómo aparecería un recorrido en Labyrinth?

Como la implementación de los muros del laberinto es similar a la del ejercicio anterior, siento que lo más eficiente para la implementación es de tipo BFS.

## SecciÓn 13 (Patrón descubiertob)

- ¿Tengo que visitar nodos conectados?

Si, los que no lo estan no los puedo visitar

- ¿Quiero saber si puedo llegar?

Si, para poder saber si estan conectados y como hacerlos

- ¿Quiero distancia mínima en número de aristas?

Tiene que ser de al menos uno necesariamente, porque si no no esta conectado.

El patron de recorrido va a cambiar segun la estructura, pero lo que tienen en comun todas es que tienes que regresar al ultimo nucleo para ir al siguiente.

## SecciÓn 14 (Cierre)

1. ¿Qué ganamos al recorrer un grafo?

Ganamos información y ganamos el tener un metodo conveniente para hacerlo.

2. ¿Qué relación hay entre cola y BFS?

Que BFS es un tipo de grafo que forsosamente neceita de una cola para poder ser modificado, por la manera en la que funciona, que ya hemos visto a lo largo del notebook.

3. ¿Qué relación hay entre pila y DFS?

Asi como con el BFS para el DFS es elemental la implementación de una pila, de nuevo, por la manera en la que funciona.

4. ¿Qué caso te parece más fácil de visualizar?

Ambos son bastante facil, peor yo diria que el más facil es el de BFS, se me hace el más natural e intuitivo para visualizar el problema.

5. ¿Qué pregunta técnica te queda abierta?

¿Qué otro tipo de grafos existe?
