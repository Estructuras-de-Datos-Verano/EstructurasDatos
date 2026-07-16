# Notebook - Clase 10 - josé Iván Reyna Blanco

## 1. Problemas CSES
**Pregunta.** ¿Qué cambia entre representar un grafo y recorrerlo? Representarlo requiere de una implementación que elija usar una estructura de datos adecuada y que permita darle sus atributos y operaciones naturales. Por otro lado, recorrerlo requiere usar un algoritmo de búsqueda en la estructura, lo cuál puede resultar desafiante si queremos evitar problemas como resizings de estructuras dinámicas o tener un tiempo de órden <= O(n). 
## 2. Recorridos manuales sin nombres
### Counting Rooms
1. ¿Qué representa un nodo? Un cuarto
2. ¿Qué representa una arista? Cuartos contiguos
3. ¿Qué significa visitar un nodo? Visitar un cuarto
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces? Si ya visité contiguos o si ya hice una vez un recorrido considerando que en el recorrido guardé los cuartos.
### Labyrinth
1. ¿Qué representa un nodo? Un piso
2. ¿Qué representa una arista? Un camino entre pisos
3. ¿Qué significa visitar un nodo? Avanzar en el laberinto
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces? Si ya hice o no un recorrido y también si fue o no exitoso.
### Message Route
1. ¿Qué representa un nodo? Una computadora
2. ¿Qué representa una arista? Una conexión biunívoca y dirigida entre ambas
3. ¿Qué significa visitar un nodo? Enviar un mensaje de una a otra
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces? Si ya hice o no un recorrido y también si fue o no exitoso.
## 3. Estrategia por niveles
| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B,C | A | A |
| 2 | C,D,E | A,B | B |
| 3 | D,E,F | A,B,C | C |
| 4 | E,F |  A,B,C,D| D |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo? FIFO

## 4. Estrategia por profundidad
| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B,C | A | A |
| 2 | B,F | A,C | C |
| 3 | B | A,C,F | F |
| 4 | D,E | A,C,F,B | B |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más reciente? LIFO
## 5. Nacen BFS y DFS
**Pregunta.** Explica con tus palabras por qué BFS usa cola y DFS usa pila. Porque Breadth First Search explora al primero en entrar. Si metemos en una pila a los nodos y vamos accediendo en órden pop(), vamos en realidad a acceder al último. Con Depth First Search es lo mismo a la inversa si usamos un queue. Por eso es que se corresponden de forma natural al revés. 
## 6. Pseudocódigo
**Pregunta.** ¿Qué pasaría si en BFS cambiamos la cola por una pila? Lo que expliqué arriba. Tendríamos que usar pop(0) y ya hemos visto que no es conveniente por el resizing. 
**Pregunta.** ¿Por qué necesitamos un conjunto de descubiertos o visitados? Porque es lo que nos deja acceder en órden a los nodos que procesamos.
## 7. Registro paso a paso
**Pregunta.** ¿Qué ventaja tiene registrar la ejecución paso a paso? Creo que poder visualizar la construcción del recorrido, como tener subgrafos y esperar a que cada paso constituya un nuevo bloque/rama.
## 8. Visualización
**Pregunta.** ¿Qué puede mostrar una animación que una lista de nodos no muestra? Directamente las aristas
## 9. Diseño de pruebas
**Pregunta.** Diseña dos pruebas propias y explica qué comportamiento verifican.
```
text
def test_llave_no_existe_bfs():
    g = {
        "A" : ["B", "C"]
    }
    res = bfs(g, "A")
    assert "B" in resultado
def test_vecinos_dfs():
    g = {
        "A" : ["B", "C"],
        "B" : ["E"]
    }
    res = dfs(g, "A")
    assert ["A", "B", "E", "C"] == res
```
1. ¿Cuál algoritmo usarías para Message Route y por qué? DFS porque necesito que vaya de INICIO-FIN sin entrar a computadoras que no se relacionan de forma dirigida.
2. ¿Cuál usarías para Counting Rooms? BFS porque si me intersa que recorra cualquier dirección y cuente cuartos.
3. ¿Cómo aparecería un recorrido en Labyrinth? Pues aparecería como una lista de movimientos correspondientes a los nodos como ["inicio", "left", "right", "fin"]
## 10. Patrón descubierto
**Pregunta.** Explica con tus palabras el patrón de recorrido de grafos. Es como preguntarte si te interesan rutas o cualquier información contenida en los nodos y así decides si quieres explorar todo lo posible a lo ancho o todo lo posible a lo profundo del grafo. 
## 11. Cierre
1. ¿Qué ganamos al recorrer un grafo? Información de los nodos y rutas posibles.
2. ¿Qué relación hay entre cola y BFS? La cola es la estructura óptima para un algoritmo BFS que sigue FIFO. 
3. ¿Qué relación hay entre pila y DFS? La pila es la estructura óptima para un algoritmo DFS que sigue LIFO.
4. ¿Qué caso te parece más fácil de visualizar? Ambos.
5. ¿Qué pregunta técnica te queda abierta? ¿La complejidad temporal de estos algoritmos se calcula solo sumando el costo de acceder a los valores o si depende diretamente del tamaño?