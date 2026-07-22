## 1. Presentación de la clase

¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?
  - la secuencia tiene un orden y es sistemática, muentras que la relación puede variar demasiado pero va mas en desorden

## 2. Problemas motivadores CSES


- [Building Roads](https://cses.fi/problemset/task/1666/)

1. ¿Qué representa un nodo?
  - una ciudad
2. ¿Qué representa una arista?
  - una carretera
3. ¿Es dirigido?
  - si, se dirije de una ciudad a a una b 
4. ¿Es ponderado?
  - no por que una condición es a lo mas una carretera entre 2 ciudades
5. ¿Qué pregunta algorítmica aparece?
  - cuantas posibles combinaciones de carreteras hay?
- [Counting Rooms](https://cses.fi/problemset/task/1192/)
1. ¿Qué representa un nodo?
  - cada cuadrito que representa suelo o pared
2. ¿Qué representa una arista?
  - los juegadores
3. ¿Es dirigido?
  - si, el jugador decide si va arriba, izq, derecha, abajo.
4. ¿Es ponderado?
  - si, el jugador decide a donde moverse
5. ¿Qué pregunta algorítmica aparece?
  - de que forma puedo ponderar entre a donde ir?
- [Labyrinth](https://cses.fi/problemset/task/1193/)
1. ¿Qué representa un nodo?
  - las partes del laberinto
2. ¿Qué representa una arista?
  - la trayectoria que hace el jugador cunado se mueve
3. ¿Es dirigido?
  - si, el jugador se mueve en una dirección
4. ¿Es ponderado?
  - si, el jugador tiene a donde darle dirección
5. ¿Qué pregunta algorítmica aparece?
  - de cuantas formas puedo resolver el laberinto
- [Message Route](https://cses.fi/problemset/task/1667/)

1. ¿Qué representa un nodo?
  - el emisor y receptor del msj
2. ¿Qué representa una arista?
  - los mensajes que se mandan
3. ¿Es dirigido?
  - si 
4. ¿Es ponderado?
  - no, el mensaje es uno
5. ¿Qué pregunta algorítmica aparece?
  - la longitud del mensaje?

## 3. Lectura de modelado

| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads |una ciudad  | una carretera | si, se dirije de una ciudad a a una b  | no por que una condición es a lo mas una carretera entre 2 ciudades | cuantas posibles combinaciones de carreteras hay?  |
| Counting Rooms | cada cuadrito que representa suelo o pared |los juegadores  | si, el jugador decide si va arriba, izq, derecha, abajo. |si, el jugador decide a donde moverse  |de que forma puedo ponderar entre a donde ir  |
| Labyrinth |las partes del laberinto  |la trayectoria que hace el jugador cunado se mueve  |si, el jugador se mueve en una dirección  |si, el jugador tiene a donde darle dirección  | de cuantas formas puedo resolver el laberinto |
| Message Route |el emisor y receptor del msj  |los mensajes que se mandan  |si  | no, el mensaje es uno |la longitud del mensaje?  |


## 4. Conceptos básicos de grafos


 Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.

  - en el grafo dirigido puede ser un laberinto
  - el grafo no dirigido se puede ejemplificar como una funcion de R -> N

## 5. Representaciones de grafos

Tres formas comunes:

1. lista de aristas;
2. lista de adyacencia;
3. matriz de adyacencia.



**Pregunta.** ¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?

  - lista de adyacencia, porque los vecinos estan presentes


## 6. Interfaz común

Queremos una interfaz que permita usar varias implementaciones con los mismos métodos.

 ¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?

  - justamente por que queremos varia implementaciónes y usaremos los 2 metodos .


## 7. Implementación 1: `GrafoListaAdyacencia`



¿Por qué un `set` ayuda a evitar aristas duplicadas?
por que el set a los elementos duplicados los hace uno es definición de conjunto

## 8. Implementación 2: `GrafoMatrizAdyacencia`

¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?
   - indica si hay una arista entre ese y otro vertice

## 9. Comparación


| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | menor | mayor |
| Facilidad de implementación | mas facil |menis facil  |
| Consultar vecinos |igual  |igual  |
| Consultar si existe arista | mas facil | mas dificil  |
| Grafos dispersos | 0 | 1 |
| Grafos densos | 1 | 0 |

## 11. Convertir implementación propia a NetworkX

I

**Pregunta.** ¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?
  - porque en la biblio externa tienes ya una interfaz



## 12. Diseño de pruebas

Las pruebas deben verificar comportamiento público, no detalles internos.

Ejemplos de comportamientos:

- crear grafo vacío;
- agregar vértice;
- agregar arista;
- verificar vecinos;
- verificar arista no dirigida en ambos sentidos;
- evitar aristas duplicadas;
- comparar ambas implementaciones.

Diseña al menos dos pruebas propias y explica qué comportamiento verifican.
  - un laberinto que evita regresar y con eso cuplimos con el punto de evitar aristas duplicadas
  - encontrar la cantidad de diagonales en un poligono regular

## 13. Patrón descubierto

Patrón: **modelado de relaciones**.

Pregunta que lo activa:

> ¿El problema habla de conexiones entre objetos?

Herramientas:

- grafo;
- lista de adyacencia;
- matriz de adyacencia;
- NetworkX para visualización.

Explica con tus palabras el patrón de modelado de relaciones.
  - es un conjunto de relaciones ordenado

Responde esta pregunta en `notebook.md`.

# 14. Cierre

### 1. ¿Qué ganamos al modelar relaciones como grafo?
  - Ganamos la capacidad de ver el "mapa completo" de cómo se conectan las cosas. En lugar de mirar datos sueltos en una tabla, un grafo nos deja ver de forma natural quién    se relaciona con quién, qué tan conectados están y descubrir caminos o intermediarios que a simple vista no notaríamos.

---

### 2. ¿Cuándo usarías lista de adyacencia?
  - La usarías cuando el grafo es **grande pero tiene pocas conexiones** (como una red social donde no todos son amigos de todos). Es ideal para ahorrar espacio en la computadora, porque solo anotas las conexiones que de verdad existen.

---

### 3. ¿Cuándo usarías matriz de adyacencia?
  - La usarías cuando **casi todos están conectados con todos** o cuando necesitas saber de inmediato (y a cada rato) si dos nodos específicos son amigos o no. Imagínalo como un cuadro de doble entrada; es rápido para buscar con la mirada, pero gasta más papel (memoria).

---

### 4. ¿Qué puede ocultar una visualización?
* **El desorden:** Si hay demasiados nodos, el dibujo se convierte en un "enredo de cables" indescifrable.
* **Falsas apariencias:** El algoritmo que dibuja el grafo puede poner dos nodos juntos solo para que se vea bonito, aunque en la realidad no tengan nada que ver.
* **Detalles importantes:** A veces no se nota a simple vista cuál conexión es más fuerte que otra o en qué dirección va la relación (quién sigue a quién).

---

### 5. ¿Qué algoritmo necesitaremos para recorrer el grafo?
Depende de lo que busques, pero usamos dos principalmente:
* **BFS (Búsqueda en anchura):** Explora primero a los vecinos más cercanos, como cuando tiras una piedra al agua y la onda se expande en círculos. Sirve para encontrar el camino más corto.
* **DFS (Búsqueda en profundidad):** Elige un camino y lo sigue hasta el fondo antes de regresar y probar otro, como cuando intentas salir de un laberinto.













