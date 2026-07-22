## 1. Presentación de la clase

**Pregunta.** ¿Qué cambia entre representar un grafo y recorrerlo?

Representar un gráfico es ver sus elementos y sus relaciones, recorrerlo sería acceder a esos elementos.

## 2. Problemas CSES

## Counting Rooms

1. ¿Qué representa un nodo?
Piso y muro.
2. ¿Qué representa una arista?
Adyacencia.
3. ¿Qué significa visitar un nodo?
Conocer si es muro o piso.
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Si es piso o muro.

## Labyrinth

1. ¿Qué representa un nodo?
Piso, muro, inicio o final.
2. ¿Qué representa una arista?
Adyacencia.
3. ¿Qué significa visitar un nodo?
Conocer si es muro, piso, inicio o final.
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Si es piso, muro, inicio o fin.

## Message Route

1. ¿Qué representa un nodo?
Una computadora.
2. ¿Qué representa una arista?
Una conexión.
3. ¿Qué significa visitar un nodo?
Conocer sus conexiones.
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Las conexiones de los nodos.

## 4. Estrategia por niveles

Estrategia: visitar primero todos los vecinos cercanos, luego los vecinos de esos vecinos.

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | C,D,E,F | B,A | A |
| 1 | C,D,E,F | A,B | B |
| 2 | D,E,F | A,B,C | C |
| 3 | D,F | A,B,C,E | E |
| 4 | F | A,B,C,D,E | D |
| 5 | F | A,B,C,D,E | C |
| 6 | - | A,B,C,D,E | F |


**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?
Una cola.

## 5. Estrategia por profundidad

Estrategia: avanzar todo lo posible por una rama y regresar cuando no se pueda continuar.

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | C,D,E,F | A,B | A |
| 1 | C,D,E,F | A,B | B |
| 2 | C,D,F | A,B,E | E |
| 3 | C,F | A,B,E, | D |
| 4 | C,F | A,B,E,D | B |
| 5 | C,F | A,B,E,D | A |
| 6 | F | A,B,E,D,C | C |
| 7 | - | A,B,E,D,C | F |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?
Una pila.

## 6. Nacen BFS y DFS

**Pregunta.** Explica con tus palabras por qué BFS usa cola y DFS usa pila.
Porque con BFS queremos conocer todos los vecinos y después profundizar en cada uno, así que necesitamos volver al más antiguo. En DFS queremos avanzar y volver donde vinimos, entonces sirve el más reciente.

## 7. Pseudocódigo

**Pregunta.** ¿Qué pasaría si en BFS cambiamos la cola por una pila?
Sería un DFS

## 8. Implementación
**Pregunta.** ¿Por qué necesitamos un conjunto de descubiertos o visitados?
Para saber qué nodos ya recorrimos.

## 9. Registro paso a paso
**Pregunta.** ¿Qué ventaja tiene registrar la ejecución paso a paso?
Que conocemos cómo se recorre el grafo y entendemos mejor las relaciones entre nodos.

## 10. Visualización

**Pregunta.** ¿Qué puede mostrar una animación que una lista de nodos no muestra?
Cómo se ve el recorrido entre nodos de manera fácilmente comprensible.

## 11. Diseño de pruebas
OJO

## 12. CSES aplicado

1. ¿Cuál algoritmo usarías para Message Route y por qué?
DFS, porque me premite entender cada ruta, que es lo más útil para casos así.
2. ¿Cuál usarías para Counting Rooms?
BFS, porque necesito entender cómo se relacionan todos los nodos con sus vecinos.
3. ¿Cómo aparecería un recorrido en Labyrinth?
Como intentar salir revisando las conexiones entre nodos con un DFS.

## 13. Patrón descubierto
**Pregunta.** Explica con tus palabras el patrón de recorrido de grafos.
Recorrer grafos significa visitar cada nodo a través de sus conexiones, para conocer las rutas más eficientes entre ellos, o entender mejor qué representan.

## 14. Cierre

1. ¿Qué ganamos al recorrer un grafo?

Información sobre sus conexiones.

2. ¿Qué relación hay entre cola y BFS?
El BFS va visitando los vecinos de cada nodo que se ecnuentra, entonces los organiza en una cola para visitar sus vecinos en el orden en que encontró los nodos.
3. ¿Qué relación hay entre pila y DFS?
Que el DFS profundiza cada ruta que encuentra, entonces tiene que poder regresar.
4. ¿Qué caso te parece más fácil de visualizar?
El DFS, porque a veces confunde visitar todos los vecinos en el BFS.
5. ¿Qué pregunta técnica te queda abierta?
¿Cuál es más eficiente en general?
