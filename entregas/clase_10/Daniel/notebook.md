## 1. Presentación de la clase



¿Qué cambia entre representar un grafo y recorrerlo?
  - Recorrer un grafo significa visitar nodos siguiendo aristas y mantener memoria de lo que ya vimos para no repetirnos ni perdernos, mientras que recorrerlo significa
    unicamente interfzearlo si esa palabra existe


## 2. Problemas CSES

Usaremos estos problemas como motivación:

- [Counting Rooms](https://cses.fi/problemset/task/1192/)
  

1. ¿Qué representa un nodo?
  - los cuartos
2. ¿Qué representa una arista?
  - las conexiones entre cuartos
3. ¿Qué significa visitar un nodo?
  - estar en un cuarto
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
  - marcar el cuarto donde ya estuviste

- [Labyrinth](https://cses.fi/problemset/task/1193/)



1. ¿Qué representa un nodo?
  - las posiciones del laberinto
2. ¿Qué representa una arista?
  - moverse a traves del laberinto
3. ¿Qué significa visitar un nodo?
  - estar en una perte del lavberinto
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
  - no dar vueltas en circulos 


- [Message Route](https://cses.fi/problemset/task/1667/)


1. ¿Qué representa un nodo?
  - las letras
2. ¿Qué representa una arista?
  - los espacios entre letras
3. ¿Qué significa visitar un nodo?
  - hacer una palabra
4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
  - no hacer la misma palabra o palabras que rimen


## 3. Recorridos manuales sin nombres

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | B , C | C |
| 1 | C  | A, F | F  |
| 2 | F |C  | A |
| 3 | A |B,C  |B  |
| 4 | B | A,E,D |D  |

 ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?

  - una cola

## 5. Estrategia por profundidad

Estrategia: avanzar todo lo posible por una rama y regresar cuando no se pueda continuar.

Completa en `notebook.md`:

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A |B,C | B |
| 1 | B |A,E,D  |D  |
| 2 | D |B  |B  |
| 3 |B  |A,E,D  |D  |
| 4 | D |B  |B  |

 ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?
 - uan pila


## 6. Nacen BFS y DFS

Explica con tus palabras por qué BFS usa cola y DFS usa pila.
  - DFS usa pila por que es mas facil, en los ejemplos vimos un buscador y eso claro que te recomendará cosas mas recienes, 
    mientras que el BFS usa una cola por que como va explorando por niveles necesitta un orden de prioridad


## 7. Pseudocódigo


¿Qué pasaría si en BFS cambiamos la cola por una pila?
  - no  sería tan facil la funcion de sacar del frente y aparte el elemento que nos da no sería el correcto 

## 8. Implementación



 ¿Por qué necesitamos un conjunto de descubiertos o visitados?
   - por que de esa forma nos queda evidencia de todo lo que ejecutó el codigo

## 9. Registro paso a paso


¿Qué ventaja tiene registrar la ejecución paso a paso?
  - que se lleva un registro completo de todos los pasos a seguir desde la ejecición del programa
  
## 10. Visualización



¿Qué puede mostrar una animación que una lista de nodos no muestra?
extra

## 11. Diseño de pruebas

Diseña dos pruebas propias y explica qué comportamiento verifican.
 - 

## 12. CSES aplicado


1. ¿Cuál algoritmo usarías para Message Route y por qué?
2. ¿Cuál usarías para Counting Rooms?
3. ¿Cómo aparecería un recorrido en Labyrinth?

## 13. Patrón descubierto


Preguntas que lo activan:

- ¿Tengo que visitar nodos conectados?
- ¿Quiero saber si puedo llegar?
- ¿Quiero distancia mínima en número de aristas?

Herramientas:

- BFS;
- DFS;
- cola;
- pila.

**Pregunta.** Explica con tus palabras el patrón de recorrido de grafos.

Responde esta pregunta en `notebook.md`.

## 14. Cierre

Responde en `notebook.md`:

1. ¿Qué ganamos al recorrer un grafo?
 - ganamos una visión mas amplia y concreta y mas sencilla de el algoritmo que quieres explicar
2. ¿Qué relación hay entre cola y BFS?
 - 
3. ¿Qué relación hay entre pila y DFS?
4. ¿Qué caso te parece más fácil de visualizar?
5. ¿Qué pregunta técnica te queda abierta?

No respondas aquí. Responde en `notebook.md`.



