# Notebook clase 15 - Leonardo Daniel Arenas Serafín

#### ¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?
Debemos de recorrer todos los caminos posibles e ir llevando la cuenta de las aristas para al final compararlas y encontrar el mínimo con un heap

## 1. Por qué BFS ya no basta

#### ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?
En el primer caso se elegiría A -> D pues es una sola arista a diferencia de A -> B -> D que son 2. En el segundo caso se elegiría A -> B -> D pues tiene un costo de 2, a diferencia de A -> D que cuesta 10.
#### ¿Por qué contar aristas ya no es suficiente en un grafo ponderado?
Porque el costo no es algo proporcional al número de aristas, sino que cada arista tiene su propio peso.

## 2. Recordatorio de BFS

#### ¿En qué condición BFS sí garantiza caminos de costo mínimo?
Cuando las aristas tienen un costo unitario o bien cuando el costo es el mismo para todas las aristas

## 3. Red de ciudades conductora

#### Enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.
1. A -> B -> D -> E. Tiene un costo de 4 + 1 + 3 = 8 respectivamente
2. A -> C -> B -> E. Tiene un costo de 1 + 2 + 5 = 8 respectivamente

#### ¿Qué representan nodos, aristas y pesos en esta red?
Los nodos son los lugares a los que llegas, las aristas son los caminos que los conectan y los pesos son el costo de tomar un camino de un lugar a otro.

## 4. Distancias tentativas

#### ¿Qué significa infinito en la tabla de distancias?
Puede significar dos cosas. La primera y la principal es que todavía no conocemos ningún camino. La segunda es que el costo de ese camino es demasiado grande, tan grande que cualquier otro camino costará menos, lo que significa que no es una opción.

## 5. Relajación

#### ¿Qué tres valores comparamos al relajar una arista?
Comparamos el valor que tenemos ya establecido, comparamos el peso del nuevo camino y comparamos la cuenta que ya se tenía antes de tomar el nuevo camino

## 6. Mejoras sucesivas

#### ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
Porque eliminarla podría llevar a errores y complicaciones en la estructura, es mejor simplemente ignorarla y que quede en el pasado para seguir con el proceso y evitar estos errores.

## 7. Descubrimiento de la cola de prioridad

#### ¿Qué componente del par funciona como prioridad y cuál como elemento?
La prioridad es el costo de llegar a tal lugar (valor entero), el cual es el elemento.

## 8. Algoritmo de Dijkstra

#### ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
Resuelve el problema de encontrar el camino más óptimo (con menos costo) para llegar de un punto a otro. Tiene la restricción de que no puede haber costos negativos, ya que el algoritmo le da prioridad a los caminos encontrados como más óptimos, el problema con pesos negaivos es que un camino que al inicio pueda ser costoso, con pesos negativos se puede volver mucho más óptimos que los demás, pero como al inicio no tiene prioridad por ser costoso, no se descubriría este camino.

## 9. Pseudocódigo y entradas obsoletas

```text
para cada nodo:
    distancia[nodo] = infinito
    predecesor[nodo] = ninguno

distancia[origen] = 0
insertar (0, origen) en la cola de prioridad <---- Depende

mientras la cola no esté vacía:
    extraer (distancia_extraida, actual) <---- Depende

    si distancia_extraida no coincide con distancia[actual]:
        ignorar esta entrada y continuar

    para cada (vecino, peso) de actual:
        candidata = distancia[actual] + peso
        si candidata < distancia[vecino]: 
            distancia[vecino] = candidata
            predecesor[vecino] = actual
            insertar (candidata, vecino) <---- Depende
```
#### ¿En qué momento se ignora una entrada obsoleta?
Cuando no está conectada mediante una arista con más vecinos, por lo que no llega a ningún lado y se ignora. Esto pasa cuando la distancia del elemento extraido no coincide con la distancia del actual.


## 10. Recorrido manual mínimo

#### ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
El orden de extracción se define a partir de cuál es el costo mínimo.

## 11. Recorrido manual intermedio

| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` | D=4, E=10 | A0 B3 C1 D4 E10 | D←B E←D |
| `(4,D)` | E=7 | A0 B3 C1 D4 E10 | E←D |
| `(7,E)` | - | - | - |


#### ¿Cuáles son las distancias finales desde A en la red conductora? 
13 y 17

## 12. Reconstrucción del camino

#### ¿Por qué recorremos predecesores desde el destino y después invertimos?
 Porque los predecesores devuelven de dónde vino, por lo debemos ir para atrás. Lo invertimos para poder visualizar el camino seguido.

 ## 13. Visualización interactiva

 #### “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.
Se ignorará `(10,B)` ya que es un camino que resultó ser mucho más costoso que el otro, por lo que no es eficiente.
 #### ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
 El heap, la comparación y los costos.

 ## 14. Implementación

 #### ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
 - `dijkstra` solamente debe de mapear los caminos
 - `reconstruir_camino` debe de tomar el mapa y decir cuáles son los caminos
 - `camino_minimo` trabaja en conjunto con las otras dos funciones para que después de mapear y analizar los caminos, decida cuál es el mínimo.

 ## 15. Complejidad

 #### ¿De dónde proviene el factor logarítmico de Dijkstra con heap?
 Proviene de que en este problema debemos de utilizar el MinHeap para poder hacer las extracciones, como esta estructura tiene una complejidad logarítmica, provoca que Dijkstra tenga un factor logarítmico en su solución. Ya que debemos usar el mínimo para ir mappeando los caminos y decidir cuál es el óptimo.

 ## 16. Problema guiado: entrega urgente


 | Concepto | Resultado que debes completar |
| --- | --- |
| Orden de extracciones vigentes | (0,A) |
| Mejoras de B | B=2, C=4 |
| Mejoras de D | D=1 |
| Mejoras de E | B->E=7, D->E=1 |
| Predecesores finales | A→B→E, A→C→D→E |
| Camino A→E | A→2→B→7→E, A→4→C→1→D→1→E |
| Costo total | 9, 6 |

#### ¿Cuál es el costo y camino mínimo de A a E en la red conductora?
El camino mínimo es A→C→D→E y cuesta 6. 
#### Explica por qué una ruta con más aristas puede ser mejor.
Porque aquí el costo de un camino no es cuántas aristas se toman sino cuál es el costo de tomar dichas aristas. Uno puede tomar dos aristas que cuesten 9 o puede tomar 3 que cuesten 6.


## 17. Limitaciones y pesos negativos

#### ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
Porque como el algoritmo le da prioridad a los caminos encontrados como más óptimos, el problema con pesos negaivos es que un camino que al inicio pueda ser costoso, con pesos negativos se puede volver mucho más óptimos que los demás, pero como al inicio no tiene prioridad por ser costoso, no se descubriría este camino. Evita errores silenciosos.

## 18. Pruebas y revisión técnica

#### ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?
Que si hay un destino inalcanzable no se tome en cuenta o que las rutas costosas no se eliminen, sino que simplemente se ignoren
#### ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?
test_nodo_inalcanzable_conserva_infinito(), ya que verifique que se tome como infinito.

## 19. Práctica adicional

#### ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
Suma de costos positivos

## 20. Cierre

#### ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
La cadena de tomar el camino provisional mínimo, pues no solamente buscamos caminos, sino que buscamos el mínimo. Así usamos heaps.

## Parte 1 — Recorrido manual

```python
grafo = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1), ("E", 7)],
    "C": [("B", 2), ("D", 5)],
    "D": [("E", 3)],
    "E": [],
}
```

| Extracción | Arista | Candidata | Comparación | Decisión | Heap después |
| --- | --- | ---: | --- | --- | --- |
| `(0,A)` | `A→B` | (4, B) | 0<4 | (0,A) | [(0,A), (4,B)] |
| `(0,A)` | `A→C` | (1, C) | 0<1 | (1,C) | [(1,C), (4,B)] |
| `(1,C)` | `C→B` | (2,B) | 1<2 | (1,C) | [(1,C), (2,B), (4,B)] |
| `(1,C)` | `C→D` | (5,D) | 1<5 | (1,C) | [(2,B), (4,B), (5,D)] |
| `(2,B)` | `B→D` | (1,D) | 1<2 | (1,D) | [(1,D), (2,B), (4,B), (5,D)] |
| `(1,D)` | `D→E` | (3,E) | 1<3 | (1,D) | [(2,B), (3,E), (4,B), (5,D)] |
| `(2,B)` | `B→E` | (7,E) | 2<7 | (2,B) | [(3,E), (4,B), (5,D), (7,E)] |
| `(3,E)` | - | - | - | (INFINITO,E) | [(4,B), (5,D), (7,E)] |  <--- Obsoleta
| `(4,B)` | `B→D` | (1,D) | 1<4 | (1,D) | [(1,D), (4,B), (5,D), (7,E)] |
| `(1,D)` | `D→E` | (3,E) | 1<3 | (1,D) | [(4,B), (5,D), (7,E)] |
| `(4,B)` | `B→E` | (7,E) | 4<7 | (4,B) | [(5,D), (7,E)] |
| `(5,D)` | `D→E` | (3,E) | 3<5 | (3,E) | [(7,E)] |
| `(7,E)` | - | - | - | (INFINITO,E) | [] |  <--- Obsoleta

### Camino`A→E`
A->C->B->D->E. Costo: 7