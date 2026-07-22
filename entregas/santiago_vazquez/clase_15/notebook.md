## Pregunta inicial

¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?

Procesando los nodos en orden de menor distancia acumulada utilizando una cola de prioridad.

## 1. Por qué BFS ya no basta

**Pregunta adicional:** ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?

BFS elegiría la ruta directa costosa por niveles, pero la optimización por costo debe elegir la ruta indirecta con menor peso acumulado.

**Pregunta:** ¿Por qué contar aristas ya no es suficiente en un grafo ponderado?

Porque una ruta con más aristas puede acumular un costo total menor que una ruta directa pesada.

## 2. Recordatorio de BFS

**Pregunta:** ¿En qué condición BFS sí garantiza caminos de costo mínimo?

Únicamente cuando todas las aristas del grafo tienen el mismo peso o costo unitario.

## 3. Red de ciudades conductora

**Actividad manual:** enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.

Actividad manual (caminos de A a E):
- A -> B -> E (Costo: 4 + 7 = 11)
- A -> C -> B -> D -> E (Costo: 1 + 2 + 1 + 3 = 7)

**Pregunta:** ¿Qué representan nodos, aristas y pesos en esta red?

Los nodos representan ciudades, las aristas carreteras dirigidas y los pesos el tiempo o costo de viaje.

## 4. Distancias tentativas

**Pregunta:** ¿Qué significa infinito en la tabla de distancias?

Indica que un nodo es inalcanzable temporal o permanentemente desde el origen.

## 5. Relajación

**Pregunta:** ¿Qué tres valores comparamos al relajar una arista?

La distancia acumulada del nodo origen actual, el peso de la arista hacia el vecino y la mejor distancia conocida hasta el momento de ese vecino.

## 6. Mejoras sucesivas

**Pregunta:** ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?

Porque las entradas viejas del heap simplemente se ignoran al extraerlas, lo cual es más eficiente que reestructurar el heap en cada actualización.

## 7. Descubrimiento de la cola de prioridad

**Pregunta:** ¿Qué componente del par funciona como prioridad y cuál como elemento?

La distancia acumulada funciona como prioridad (menor valor, mayor prioridad) y el identificador del nodo actúa como el elemento.

## 8. Algoritmo de Dijkstra

**Pregunta:** ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?

Resuelve el problema de caminos mínimos desde un único origen y exige la restricción de que todos los pesos sean no negativos.

## 9. Pseudocódigo y entradas obsoletas

**Actividad:** subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.

```text
para cada nodo:
    distancia[nodo] = infinito
    predecesor[nodo] = ninguno

distancia[origen] = 0
**<u>insertar (0, origen) en la cola de prioridad</u>**

mientras la cola no esté vacía:
    **<u>extraer (distancia_extraida, actual)</u>** de la cola de prioridad

    si distancia_extraida no coincide con distancia[actual]:
        ignorar esta entrada y continuar

    para cada (vecino, peso) de actual:
        candidata = distancia[actual] + peso
        si candidata < distancia[vecino]:
            distancia[vecino] = candidata
            predecesor[vecino] = actual
            **<u>insertar (candidata, vecino)</u>** en la cola de prioridad

```

**Pregunta:** ¿En qué momento se ignora una entrada obsoleta?

Inmediatamente después de extraerla de la cola de prioridad, si su distancia acumulada es mayor que la distancia guardada en el registro de distancias tentativas.

**Responde esta pregunta en notebook.md.**

## 10. Recorrido manual mínimo

**Pregunta:** ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?

El orden de extracción es el nodo A con distancia 0, el nodo B con su costo mínimo y los subsiguientes vecinos óptimos.

## 11. Recorrido manual intermedio

Completa la tabla antes de usar el visualizador:

| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` | D=4, E=10 | A0 B3 C1 D4 E10 | D←B, E←B |
| `(4,D)` | E=7 | A0 B3 C1 D4 E7 | E←D |
| `(7,E)` | Ninguna (Fin) | A0 B3 C1 D4 E7 | Ninguno |


**Pregunta:** ¿Cuáles son las distancias finales desde A en la red conductora?

Las distancias finales mapeadas son: A: 0, B: 3, C: 1, D: 4, E: 7.

## 12. Reconstrucción del camino

**Pregunta:** ¿Por qué recorremos predecesores desde el destino y después invertimos?

Porque cada nodo conoce únicamente quién fue su predecesor inmediato para llegar a él, por lo que la ruta se descubre en sentido inverso (destino -> origen).

## 13. Visualización interactiva

**Actividad:** en “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.

El algoritmo extraerá la tupla (10,B) del min-heap y la **ignorará inmediatamente, continuando con la siguiente iteración sin evaluar a sus vecinos.

**Pregunta:** ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?

El grafo de la red, el diccionario de distancias/predecesores y el estado interno del min-heap.

## 14. Implementación

**Pregunta:** ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?

- `dijkstra`: Calcula distancias y predecesores sin modificar la entrada.
- `reconstruir_camino`: Rastrea la ruta inversa de destino a origen.
- `camino_minimo`: Coordina el flujo completo devolviendo costo y ruta.

## 15. Complejidad

**Pregunta:** ¿De dónde proviene el factor logarítmico de Dijkstra con heap?

Proviene de las operaciones de inserción (`push`) y extracción del elemento mínimo (`pop`) en el min-heap.

## 16. Problema guiado: entrega urgente

Tabla de evidencia:

| Concepto | Resultado que debes completar |
| --- | --- |
| Orden de extracciones vigentes | A(0), C(1), B(3), D(4), E(7) |
| Mejoras de B | De ∞ a 4 (vía A), de 4 a 3 (vía C) |
| Mejoras de D | De ∞ a 6 (vía C), de 6 a 4 (vía B) |
| Mejoras de E | De ∞ a 10 (vía B), de 10 a 7 (vía D) |
| Predecesores finales | B<-C, C<-A, D<-B, E<-D |
| Camino A→E | A -> C -> B -> D -> E |
| Costo total | 7 |

Compara al final con dos alternativas: A→B→E y A→C→D→E. Explica por qué una ruta con más aristas puede ser mejor.

Porque la suma de los costos individuales pequeños de múltiples aristas puede ser menor que el costo elevado de una única arista directa.

**Pregunta:** ¿Cuál es el costo y camino mínimo de A a E en la red conductora?

Camino mínimo: `A -> C -> B -> D -> E`
Costo total:** `7

## 17. Limitaciones y pesos negativos

**Pregunta:** ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?

Porque el algoritmo asume con un enfoque codicioso que una vez que un nodo es extraído del heap, ya se ha encontrado su costo mínimo absoluto, impidiendo reevaluarlo si surge un costo menor provocado por un peso negativo.

## 18. Pruebas y revisión técnica

**Pregunta adicional:** ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?

Comprobaría que el primer elemento sea el origen, el último sea el destino y que la secuencia corresponda a conexiones existentes en el grafo.

**Pregunta:** ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?

Un caso donde un mismo vecino reciba múltiples actualizaciones de costo decreciente, generando varios registros duplicados en el heap que deban ser descartados perezosamente.

## 19. Práctica adicional

### Comprueba tu comprensión

**Pregunta:** ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?

La necesidad de optimizar y encontrar la ruta acumulativa más económica en redes dirigidas o no dirigidas con costos positivos.

## 20. Cierre

**Pregunta:** ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?

Establecer distancias infinitas provisionales, aplicar relajaciones de aristas basadas en acumulaciones de costo y utilizar una cola de prioridad para procesar siempre el camino más prometedor.




