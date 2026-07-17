# Notebook Clase 15 -José Iván Reyna Blanco
## Parte 1 - Recorrido Manual
**Pregunta inicial:** ¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo? Probablemente explorando todos los recorridos posibles, sumando costos (que es el peso de cada arista) y eligiendo la menor suma.
**Pregunta adicional:** ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total? Me es completamente imposible saber eso considerando que llevo 10 líneas del tema leídas hasta este momento de la práctica. De hecho ni siquiera entiendo la pregunta. 
**Pregunta:** ¿Por qué contar aristas ya no es suficiente en un grafo ponderado? Porque en uno ponderado se busca considerar los pesos, deja de tener sentido solo explorar los nodos a lo ancho porque ahora importa cómo recorrerlo en cualquier otro camino posible. 
**Pregunta:** ¿En qué condición BFS sí garantiza caminos de costo mínimo? Que el nodo buscado sea el siguiente en el mismo nivel y además ese camino tenga el menor peso. 
grafo = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1), ("E", 7)],
    "C": [("B", 2), ("D", 5)],
    "D": [("E", 3)],
    "E": []
}
| Extracción | Arista | Candidata | Comparación | Decisión | Heap después |
| --- | --- | ---: | --- | --- | --- |
| `(0,A)` | `A→B` | (4, B) |4 < inf | Meter | [(4, B)] |
| `(0,A)` | `A→C` | |(1, C) |1 < inf | meter | [(1, C), (4, B)]
| `(1,C)` | `C→B` |(3, B) ## Sumas el costo de llegar a C | 3 < 4 | Meter | [ (3, B), (4, B)] |
| `(1,C)` | `C→D` |(6, D) |6 < inf | Meter |[(3, B), (4, B), (6, D)] |
| (3, B) | B a D |(4, D) | 4 < 6  |Meter |[(4, B), (4, D), (6, D) ] |
| (3, B) | B a E |(10, E) | 8 < inf  |Meter |[(4, B), (4, D), (6, D), (10, E)] |
| (4, B) | - |- | 4 > 3  |Obsoleto |[(4, D), (6, D), (10, E)] |
| (4, D) | D a E |(7, E) | 7 < 10  | Meter |[(6, D), (7, E), (10, E)] |
| (6, D) | - | - | 6 > 4  | Obsoleto |[(7, E), (10, E) ] |
| (7, E) | - | - | - | Procesar por vacuidad |[(10, E) ] |
| (10, E) | - | - | - | Procesar por vacuidad |[] |
**Actividad:**
Usaremos la misma red durante la tabla manual, la relajación, el heap, el visualizador y la reconstrucción:

```text
        4           1
   A ------> B ----------> D
    \        |             |
   1\       7|            3|
      ▼      ▼             ▼
       C ----+-----------> E
        \ 2  ▲      5
         └──>B   C ------> D
```

Lista de adyacencia:

```python
{
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1), ("E", 7)],
    "C": [("B", 2), ("D", 5)],
    "D": [("E", 3)],
    "E": [],
}
```

Cada nodo representa una ciudad; una arista dirigida, una carretera disponible; el peso, tiempo de viaje. Buscamos desde A el costo mínimo a todas las ciudades. La dirección importa: que exista `C → B` no implica `B → C`.

**Actividad manual:** enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.
1er camino - A - C - D - E con peso 9
2ndo camino - A - B - E con peso 4
**Actividad:** subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14. 
Esto no lo puedo llenar porque hasta el momento, dado que salí de viaje, no he hecho dicha práctica. Pero una vez la termine vuelvo a llenarlo. 
**Actividad:** en “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.
Pues obviamente va a ser mejor ir a C y luego a B con costo 3 que ir de A a B con costo 10.
### Comprueba tu comprensión
**Pregunta:** ¿Qué representan nodos, aristas y pesos en esta red? Nodo - Ciudad, Arista - Carretera (dirigida), Peso - Tiempo.  
**Pregunta:** ¿Qué significa infinito en la tabla de distancias? Es la comparación natural cuando no hay nadie mayor.
**Pregunta:** ¿Qué tres valores comparamos al relajar una arista? Peso de haber llegado a el nodo inicio, peso de llegar al deseado y el peso anterior que se tenía para llegar. 
**Pregunta:** ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap? Porque en vez de borrarla solo la vuelves a comparar con el camino de menor peso que se procesa antes y queda obsoleta. En vez de buscarla en el heap para borarla, la borras cuando toca procesarla. 
**Pregunta:** ¿Qué componente del par funciona como prioridad y cuál como elemento? Prioridad : Valor, Elemento : Nodo.
**Pregunta:** ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos? Calcular caminos mínimos desde un origen en un grafo con pesos no negativos.
**Pregunta:** ¿En qué momento se ignora una entrada obsoleta? En el pseudocódigo hay una comparación, dónde si la distancia extraida de la tupla evaluada no coincide ignoramos porque significa que es de mayor peso por el óren FIFO de las queues. 
**Pregunta:** ¿Cuál es el orden de extracción vigente en el ejemplo mínimo? ABC.
``` text
// Recorrido manual
| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` | D=4, E=10 | A0 B3 C1 D4 E10 | D←B, E←B |
| `(4,D)` | E=7 | A0 B3 C1 D4 E7 | E←D |
| `(7,E)` | - | A0 B3 C1 D4 E7 | - |
```
**Pregunta:** ¿Cuáles son las distancias finales desde A en la red conductora? 15 total. (0,A), (3,B), (1,C), (4, D), (7, E).
**Pregunta:** ¿Por qué recorremos predecesores desde el destino y después invertimos? Porque eso nos da el órden origen-destino que buscamos. 
**Pregunta:** ¿Qué tres representaciones deben permanecer sincronizadas en cada paso? Nodo Actual - Arista - Destino
## Parte 2
### Comprueba tu comprensión
**Pregunta:** ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega? `dijkstra` valida pesos, calcula distancias y registra predecesores. `reconstruir_camino` sigue el mapa. `camino_minimo` devuelve costo/camino para un destino.
**Pregunta:** ¿De dónde proviene el factor logarítmico de Dijkstra con heap? De cada extracción usando heappop.
**Pregunta:** ¿Cuál es el costo y camino mínimo de A a E en la red conductora? ACBDE
**Pregunta:** ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra? Porque el uso de heap con pesos positivos garantiza el órden usando heappop. Tendríamos que ir cambiando de lugar en el heap cada vez que un valor negativo produzca que una ruta obsleta sea candidata para evitar que se ignore. 
**Pregunta:** ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente? El test de entradas obsoletas. 
**Pregunta:** ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra? Relajación. En un problema modelable a partir de grafos (una relación biunívoca, dirigida, etc) dónde se busca recorrerlo total/parcialmente y además saber el costo va a ser dominante explorar los caminos registrando el costo hasta ese momento. Esa circunstancia vuelve a Dijkstra trivialmente útil.
**Pregunta:** ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra? Minimización -> Información a preservar -> Objetivo a mejorar -> Cómo -> Qué se procesa al final -> Qué algoritmo surge <-> Restricciones 
### Problema guiado
``` text
| Concepto | Resultado que debes completar |
| --- | --- |
| Orden de extracciones vigentes | `(0,A) -> (1,C) -> (3,B) -> (4,D) -> (7,E)` |
| Mejoras de B | `B = 4` (vía A), luego `B = 3` (vía C) |
| Mejoras de D | `D = 6` (vía C), luego `D = 4` (vía B) |
| Mejoras de E | `E = 10` (vía B), luego `E = 7` (vía D) |
| Predecesores finales | `B←C, C←A, D←B, E←D` |
| Camino A→E | `A → C → B → D → E` |
| Costo total | `7 minutos` |
```
**Pregunta adicional:** ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción? Comprobaría que el costo de recorrer un grafo con destino y origen iguales sea cero y que no hayan vecinos.