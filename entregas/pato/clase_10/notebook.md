# Clase 10: Notebook
#### Nombre: Patricio Navarro

## Presentación
¿Qué cambia entre representar un grafo y recorrerlo?
- Representarlo es nada más el dibujo, o la forma de mostrar como se relacionan dos objetos, mientras que recorrer un grafo es analizar nodo por nodo su información y sus relaciones con sus vecinos.

## Problemas CSES 

### Counting Rooms
1. ¿Qué representa un nodo?
    - Una pieza de piso. Es decir, `.`
2. ¿Qué representa una arista?
    - Aquellos `.` que estan únidos por un borde, por lo que se puede pasar de uno a otro.
3. ¿Qué significa visitar un nodo?
    - Pararse en esa pieza de piso.
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
    - Los nodos por los que ya estuviste, en el que estás y los vecinos que tiene cada nodo.

### Labyrinth
1. ¿Qué representa un nodo?
    - Una pieza de piso y los puntos de partida/llegada. Es decir `.`, `a` y `b`.
2. ¿Qué representa una arista?
    - Son las relaciones entre dos nodos donde puedes moverte de un nodo a otro cuando el camino está habilitado.
3. ¿Qué significa visitar un nodo?
    - Pararse en esa casilla de piso o punto.
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
    - Los nodos por los que ya estuviste, en el que estás y los vecinos que tiene cada nodo.

### Message Route
1. ¿Qué representa un nodo?
    - Una computadora.
2. ¿Qué representa una arista?
    - La conexión de red entre dos computadoras.
3. ¿Qué significa visitar un nodo?
    - Mandar un mensaje a esa computadora.
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
    - Los nodos por los que ya estuviste, en el que estás y los vecinos que tiene cada nodo.

## Estrategia por niveles

### 1. Visitar primero todos los vecinos cercanos, luego los vecinos de esos vecinos.

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | C, D, E | A, B | B |
| 3 | D, E, F | A, B, C | C |
| 4 | E, F | A, B, C, D | D |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?
- Una cola.

### 2. Avanzar todo lo posible por una rama y regresar cuando no se pueda continuar.

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | B, D, E, F | A, C | C |
| 3 | B, D, E | A, C, F | F |
| 4 | B, D, E | A, C, F | C |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?
- Una pila.

## BFS y DFS
Explica con tus palabras por qué BFS usa cola y DFS usa pila.
- BFS usa cola porque el comportamiento es secuencial o por niveles, entonces te importa ir en orden desde el primer nodo que entra al último, por lo que su comportamiento sigue justo el de FIFO. Por otro lado, DFS se puede decir que usa una pila porque se sigue por una rama completa hasta llegar al final, y ya que llega al final entonces saca ese nodo de la ecuación y se regresa hasta poder tomar la otra rama. 

## Pseudocódigo
¿Qué pasaría si en BFS cambiamos la cola por una pila?
- Pues ya no sería BFS, porque sacarías alguno de los nodos que te importan y te quedarías trabado yo creo. O cuando menos perderías la mayor ventaja de BFS que es encontra el camino más corto.

## Implementación
¿Por qué necesitamos un conjunto de descubiertos o visitados?
- Para saber a quienes ya visitamos a que nodos ya consideramos y así poder mantenerun órden en las siguientes visitas.

## Registro paso a paso
¿Qué ventaja tiene registrar la ejecución paso a paso?
- Que para debuggear es más sencillo y así podemos ir comparando con las tablas que hicimos antes para asegurar que el comportamiento es el buscado.

## Visualización
¿Qué puede mostrar una animación que una lista de nodos no muestra?
- El proceso que se lleva a cabo cuando se recorre o se crea algo. Además es mucho más ilustrativo.

## Diseño de pruebas
Diseña dos pruebas propias y explica qué comportamiento verifican.

1. Verifica que si se estén contando todos los pasos en los registros de bfs y dfs.
```python
def test_pasos_registro():
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
    }
    registro_bfs = modulo.registrar_bfs(grafo, "A")
    registro_dfs = modulo.registrar_dfs(grafo, "A")
    assert all("paso" in paso for paso in registro_bfs)
    assert all("paso" in paso for paso in registro_dfs)
```

2. Verifica que se estén contando las aristas exploradas en bfs y dfs.
```python
def test_aristas_exploradas_registro():
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
    }
    registro_bfs = modulo.registrar_bfs(grafo, "A")
    registro_dfs = modulo.registrar_dfs(grafo, "A")
    assert all("aristas_exploradas" in paso for paso in registro_bfs)
    assert all("aristas_exploradas" in paso for paso in registro_dfs)
```

## CSES aplicado

1. ¿Cuál algoritmo usarías para Message Route y por qué?
    - BFS, porque justo es el algoritmo que sí te puede dar el camino más corto para llegar de un nodo a otro.
2. ¿Cuál usarías para Counting Rooms?
    - En teoría creo que cualquiera de las dos funciona, pero me parece que es más eficiente hacerlo con BFS.
3. ¿Cómo aparecería un recorrido en Labyrinth?
    - Como un grafo cíclico yo creo, donde vas checando nodos por nodos y ves a donde te llevan, creo que lo mejor sería con BFS.

## Patrón descubierto
Explica con tus palabras el patrón de recorrido de grafos.
- Realmente ambos algoritmos hacen algo parecido, solo cambia el comportamiento, pero ambos checan nodo por nodo, guardan el actual, los que ya fueron visitados y conforme encuentran vecinos para cada nodo los añaden a la cola o a la pila para poder visitarlos después.

## Cierre
1. ¿Qué ganamos al recorrer un grafo?
    - Los vecinos de cada nodo y las rutas para poder llegar de cualquier nodo a otro.
2. ¿Qué relación hay entre cola y BFS?
    - Que ambas usan un comportamiento FIFO. De hecho, la cola se usa para registrar los nodos que se van a visitar después del actual.
3. ¿Qué relación hay entre pila y DFS?
    - Ambos usan un comportamiento LIFO, y el DFS ocupa una pila para los nodos que se visitan después de cada paso.
4. ¿Qué caso te parece más fácil de visualizar?
    - El BFS.
5. ¿Qué pregunta técnica te queda abierta?
    - ¿Qué algoritmo se usa en las competencias de micro-ratones?