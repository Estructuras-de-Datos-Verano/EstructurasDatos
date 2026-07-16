# Arturo Prudencio Bonilla

## seccion 1

¿Qué cambia entre representar un grafo y recorrerlo?
    El uso de memoria y la utilidad de cada cosa

## seccion 2

### Counting rooms
1. ¿Qué representa un nodo?
    un suelo 
2. ¿Qué representa una arista?
    que dos suelos esten juntos, que no hay una pared en medio
3. ¿Qué significa visitar un nodo?
    "caminar" hacia otro piso vecino
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
    el camino que cruce 

### Labyrinth
1. ¿Qué representa un nodo?
    un suelo, la entrada o la salida
2. ¿Qué representa una arista?
    que dos nodos esten inmediatamente juntos
3. ¿Qué significa visitar un nodo?
    caminar o moverte hacia un nodo vecino
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
    Que caminos ya visite 

### Message route
1. ¿Qué representa un nodo?
    Cada una de las computadoras de la red, numeradas del 1 al n.
2. ¿Qué representa una arista?
    una linea de comunicacion entre las computadoras
3. ¿Qué significa visitar un nodo?
    mandar un mensaje a un nodo 
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
    un registro de computadoras ya contactadas

## seccion 4

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | C, D, E | A, B | B |
| 3 | D, E, F | A, B, C | C |
| 4 | E, F | A, B, C, D | D |

    ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?
    la cola

## seccion 5

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | B, F | A, C | C |
| 3 | B | A, C, F | F |
| 4 | B | A, C, F | C |

    ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?
    La pila

## seccion 6

Explica con tus palabras por qué BFS usa cola y DFS usa pila.

    En BFS necesitamos abarcar lo mas posible por lo que necesitamos quitarnos los pentientes cuanto antes, para visitar muchos nodos, por lo que la cola es lo mejor pues el mas antiguo en haber entrado sera el primero en ser antendido 

    EN DFS queremos agotar nuestro camino hasta topar con pared, por lo que si queremos avanzar lo mas posible necesitamos si o si antender a los ultimos que entraron 

## seccion 7
¿Qué pasaría si en BFS cambiamos la cola por una pila?

    Para empezar no tendriamos una froma de extraer el dato del frente de manera nativa, ademas no cumpliriamos el obhjetivo de BFS

## seccion 8

¿Por qué necesitamos un conjunto de descubiertos o visitados?

    Con esa infromacion podremos ahorrar memoria posteriormente para visitar algun lugar y no tener que adivinar por donde ir


## seccion 9

¿Qué ventaja tiene registrar la ejecución paso a paso?

    Asi podemos acceder a la infromacionn previa desde la interfaz (o al menos podriamos) de manera mas facil y sin repetir todo de nuevo


## seccion 11

pruebas:

```python
def test_pruebas_extras():
    grafo = {
    "A": ["C"],
    "C": ["A"],
    "X": ["Y"],
    "Y": ["X"]
    }
    bfs_recorrido = modulo.bfs(grafo, "A")
    assert modulo.bfs(grafo, "X") == ["X", "Y"]
    assert modulo.bfs(grafo, "A") == ["A", "C"]
```


Mis pruebas extras comprueban que vecinos lejanos y no conexos no rompen el codigo

## seccion 12
1. ¿Cuál algoritmo usarías para Message Route y por qué?
    BFS, pues creo que seria el que mejor abarca el grafo y el terrono
2. ¿Cuál usarías para Counting Rooms?
    BFS pues hay que agotar los suelos hasta topar con pared 
3. ¿Cómo aparecería un recorrido en Labyrinth?


## seccion 13
Explica con tus palabras el patrón de recorrido de grafos.
    Bajo las dos fromas que lo vimos hoy, hay de dos:
    1. Explorar todos los vecinos hasta agotar un camino y regresar
    2. Ir por capas, agotar todos los vecinos de una capa e ir a la siguiente

## seccion 14
1. ¿Qué ganamos al recorrer un grafo?
    Infromacion sobre las aritas existentes y como llegar de un nodo a otro
2. ¿Qué relación hay entre cola y BFS?
    BFS funciona como una cola pues primeor atendemos a los que ya estaban
3. ¿Qué relación hay entre pila y DFS?
    DFS funciona como pila pues atendemos primero a los que llegan inmediantamente 
4. ¿Qué caso te parece más fácil de visualizar?
    DfS por su funcionamiento en capas
5. ¿Qué pregunta técnica te queda abierta?  
    ¿Cual es la mas optima forma de recorrer grafos poderados? 


