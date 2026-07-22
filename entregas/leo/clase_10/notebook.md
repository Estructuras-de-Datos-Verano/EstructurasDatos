# Notebook - Clase 10 - Leonardo Daniel Arenas Serafín

#### ¿Qué cambia entre representar un grafo y recorrerlo?
Representar un grafo solamente es almacenar la información del grafo en un objeto. Recorrerlo es más como analizar esta información de manera óptima para sacar conclusiones.

## 1. Problemas CSES

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

## 2. Recorridos manuales sin nombres



## 3. Estrategia por niveles

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | B, C | A | A |
| 1 | C | A, B | B |
| 2 | C | A, B | A |
| 3 | D, E, F | A, B, C | C |
| 4 | D, E | A, B, C, F | F |
| 5 | D, E | A, B, C, F | C |
| 6 | D, E | A, B, C, F | A |
| 7 | D, E | A, B, C, F | B |
| 8 | D | A, B, C, D, E, F | E |
| 9 | D | A, B, C, E, F | B |
| 19 | - | A, B, C, D, E, F | D |


#### ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?
Aparece una estructura como de una cola, pues ésta sigue el comportamiento FIFO

## 4. Estrategia por profundidad

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | B, C, D, E, F | A | A |
| 1 | B, D, E, F | A, C | C |
| 2 | B, D, E | A, C, F | F |
| 3 | B, D, E | A, C, F | C |
| 4 | B, D, E | A, C, F | A |
| 5 | D, E | A, B, C, F | B |
| 6 | E | A, B, C, D, F | D |
| 7 | E | A, B, C, D, F | B |
| 8 | - | A, B, C, D, E, F | E |

#### ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?
Aparece una estructura como de una pila, pues ésta sigue el comportamiento LIFO

## 5. Nacen BFS y DFS

#### Explica con tus palabras por qué BFS usa cola y DFS usa pila.
BFS usa cola porque al avanzar de un nivel al otro, lo primero que hiciste fue revisar los nodos de todo el primer nivel para después ir con el siguiente, de tal forma que los primeros nodos que revisaste son los descartables porque ya fueron recorridos. DFS usa pila pues como vamos avanzando en una misma rama hasta no poder más, al querer regresar debemos de descartar el último nodo visitado para seguir avanzando.

## 6. Pseudocódigo

#### ¿Qué pasaría si en BFS cambiamos la cola por una pila?
Lo que pasaría sería que en la primera iteración sacaríamos uno de los extremos finales del grafo para recorrerlo, y después si no lo encolamos, seguimos recorriendo de adelante hacia atrás, pero si se decide encolar, cosa que en algun caso pasará, se creará un bucle y revisará y encolará el mismo elemento sin fin.
#### ¿Por qué necesitamos un conjunto de descubiertos o visitados?
Porque parte de lo que se pide en un recorrido de un grafo es no visitar ni revisar un mismo nodo dos veces o más, por lo que al meterlo a un conjunto evitar regresarlo a la cola/pila y evitas repeticiones en el arreglo.

## 7. Registro paso a paso

#### ¿Qué ventaja tiene registrar la ejecución paso a paso?
Tiene la ventaja de que podemos analizar cuál implementación es más compleja y podemos saber exactamente cómo es que funcionan estas implementaciones al llevar la cuenta de cuáles son su operaciones. Igualmente es algo bastante ilustrativo para poder posteriormente definir la implementación de la visualización del recorrido

## 8. Visualización

#### ¿Qué puede mostrar una animación que una lista de nodos no muestra?
La animación muestra cómo es que se puede establecer cierta jerarquía u orden en las relaciones al especificar el origen del grafo, mientras que la lista, a pesar de llevar un orden, a la hora de la visualización no es posible apreciarse este detalle.

## 9. Diseño de pruebas

### Diseña dos pruebas propias y explica qué comportamiento verifican.
#### - def test_recorrido_paso0_LEO():
Este test verifica que cuando en un grafo solo tenemos un nodo, se regresa la lista con el paso 0 determinado por default para ambas implemenaciones bfs y dfs
#### - def test_grafo_uniforme_bfs_y_dfs_iguales_LEO():
Este test verifica que cuando tenemos un grafo uniforme (entiéndase uniforme por un grafo que solo tiene dos niveles, el origen y el final o en línea recta), el bfs el dfs realizan el mismo recorrido.

## 10. Patrón descubierto

#### ¿Cuál algoritmo usarías para Message Route y por qué?
- Caso 1: Si Message Route buscara estrictamente el camino más óptimo para llevar el mensaje de computadora A a computadora B usaría DFS, pues primero revisaría todos los caminos directos posibles y después compararía para saber cuál es el camino más corto
- Caso 2: Si Message Route no buscara el camino más óptimo, usaría BFS pues de esta forma puedo revisar más exhaustivamente si el mensaje llega o no

#### ¿Cuál usarías para Counting Rooms?
Usaría BFS pues solo me interesa ver cuáles son todas las habitaciones que hay.

#### ¿Cómo aparecería un recorrido en Labyrinth?
Sería DFS, pues así podemos encontrar cuáles son las opciones para encontrar un camino directo para posterioirmente comparar estos caminos para encontrar el más corto.

### Explica con tus palabras el patrón de recorrido de grafos.
#### - BFS
BFS sigue un patrón en donde se visitan exhaustivamente todos los posibles caminos posibles a la vez. No busca específicamente saber si es posible llegar a un lugar, sino que simplemente analiza cuáles son todos los lugares posibles a los que se puede llegar. De la misma manera no busca específicamente la distancia mínima entre nodos, sino que encuentra todas las distancias que hay entre todos los nodos

#### - DFS
DFS sigue un patrón en donde se visitan intensívamente los posibles caminos, pues no para hasta llegar al final. Busca específicamente si es posible llegar a un lugar y encuentra la distancia mínima entre puntos, a diferencia del BFS.


## 11. Cierre


#### ¿Qué ganamos al recorrer un grafo?
Podemos analizar el grafo establecieno una jerarquía de origen y final.

#### ¿Qué relación hay entre cola y BFS?
En el BFS debemos acceder a los primeros nodos que revisamos. La cola sigue el comportamiento de poder acceder a los primeros elementos ingresados. Por eso es que la relación que existe es que la cola es una estructura necesaria para codificar el algoritmo de BFS

#### ¿Qué relación hay entre pila y DFS?
En el DFS debemos descartar los últimos nodos que revisamos para regresar a revisar las ramas aledañas. La pila sigue el comportamiento de poder acceder a los últimos elementos ingresados. Por eso es que la relación que existe es que la pila es una estructura necesaria para codificar el algoritmo de DFS

#### ¿Qué pregunta técnica te queda abierta?
Hemos visto como es posible recorrer de diferentes formas un grafo en cuestión de cuáles son los pasos a seguir. Pero ¿qué es lo que cambiaría en el recorrido de un grafo al cambiar el origen para ambas implementaciones? ¿Existe alguna diferencia crucial al hacer esto o simplemente altera el orden de salida del recorrido?

## Ejemplo BFS
            A
         /     \
        B       C
       / \       \
      D   E       F


      cola = [A]
      descubiertos = {A}
      lista = []
    while cola it 1
    actual = A
    lista.append(actual)
    b y c
    si b y c están en descubiertos. nada
    si no, descubiertos = {A, B, C}
    cola = [B, C]
    while cola it 2
    actual = B


    ## Ejemplo DFS
            A
         /     \
        B       C
       / \       \
      D   E       F

      pila = [A]
      descubiertos = {A}
      lista = []
    while pila it 1
    actual = A
    lista.append(actual)
    b y c
    si b y c no estan en descubiertos 
    pila = [B, C], descubiertos = {A, B, C}
    while pila it 2
    actual = C
    lista.append(actual)
    F
    si F no esta en descubiertos
    pila 0 [B, F]. descubiertos = {A, B, C}

