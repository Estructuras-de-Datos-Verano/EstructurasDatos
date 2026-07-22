# Clase 15: Caminos mínimos y Dijkstra

## Pregunta inicial

¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?

Eligiendo las de menor costo.

## 1. Por qué BFS ya no basta
**Pregunta adicional:** ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?
Una que solo compare niveles, sólo contará aristas. Si optimizamos costo total, elegirá la ruta cuyas aristas sumen menos. 

**Pregunta:** ¿Por qué contar aristas ya no es suficiente en un grafo ponderado?
Porque las aristas no son iguales: algunas pesan más.

## 2. Recordatorio de BFS
**Pregunta:** ¿En qué condición BFS sí garantiza caminos de costo mínimo?
Si las aristas pesan lo mismo.

## 3. Red de ciudades conductora
**Actividad manual:** enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.
A - B - D - E
8

A - C - D - E
9

### Comprueba tu comprensión

**Pregunta:** ¿Qué representan nodos, aristas y pesos en esta red?
Los nodos son ciudades. Las arsitas, carreteras. Los pesos, tiempo de viaje.

## 4. Distancias tentativas
**Pregunta:** ¿Qué significa infinito en la tabla de distancias?
Que aún no conocemos un camino.

## 5. Relajación
**Pregunta:** ¿Qué tres valores comparamos al relajar una arista?
El peso de la arista, la distancia actual, y la distancia candidata.

## 6. Mejoras sucesivas
**Pregunta:** ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
Porque la ruta final podría ser óptima tomando la entrada anterior.

## 7. Descubrimiento de la cola de prioridad
**Pregunta:** ¿Qué componente del par funciona como prioridad y cuál como elemento?
El peso se toma para la prioridad. El elemento es el Nodo.

## 8. Algoritmo de Dijkstra
**Pregunta:** ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
El de encontrar rutas óptimas entre nodos. Lo restringe a pesos no negativos, porque estos restarían al total, lo que no tiene sentido en este caso.

## 9. Pseudocódigo y entradas obsoletas
**Actividad:** subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.
No sé cómo subrayar en md, así que lo pondré en negritas.

para cada nodo:
    distancia[nodo] = infinito
    predecesor[nodo] = ninguno

distancia[origen] = 0
*** insertar (0, origen) en la cola de prioridad ***

mientras la cola no esté vacía:
    *** extraer (distancia_extraida, actual) ***

    si distancia_extraida no coincide con distancia[actual]:
        ignorar esta entrada y continuar

    para cada (vecino, peso) de actual:
        candidata = distancia[actual] + peso
        si candidata < distancia[vecino]:
            distancia[vecino] = candidata
            predecesor[vecino] = actual
            *** insertar (candidata, vecino) ***

**Pregunta:** ¿En qué momento se ignora una entrada obsoleta?
Cuando las nuevas candidatas son mejores.

## 10. Recorrido manual mínimo
**Pregunta:** ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
(0,A), (1,B), (3,C), (4,C)

## 11. Recorrido manual intermedio

Completa la tabla antes de usar el visualizador:

| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` | B=3 | A0 B3 C1 D6 E∞ | - |
| `(4,D)` | D=4 | A0 B3 C1 D4 E∞ | D←C |
| `(7,E)` | E=7 | A0 B3 C1 D4 E7 | E←D |

**Pregunta:** ¿Cuáles son las distancias finales desde A en la red conductora?
A0 B3 C1 D4 E7
15

## 12. Reconstrucción del camino
**Pregunta:** ¿Por qué recorremos predecesores desde el destino y después invertimos?
Porque buscamos la mejor forma de llegar a un lugar, entonces empezamos de ahí y reconstruimos. Esto nos ayuda a garantizar que llegamos al destino.

## 13. Visualización interactiva
**Actividad:** en “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.
Lo descarta.

**Pregunta:** ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
BFS no basta, recorrido manual mínimo, Entradas obsoletas, porque son muy parecidas.

## 14. Implementación
**Pregunta:** ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
Dijkstra revisa pesos y predecesores. Recosntruir camino simplmente sigue las rutas. Camino mínimo usa las dos para dar el camino mínimo.

## 15. Complejidad
**Pregunta:** ¿De dónde proviene el factor logarítmico de Dijkstra con heap?
De las extracciones.

## 16. Problema guiado: entrega urgente

**Pregunta:** ¿Cuál es el costo y camino mínimo de A a E en la red conductora?
8

## 17. Limitaciones y pesos negativos
**Pregunta:** ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
Porque el peso acumulado poría bajar. Dijkstra sólo espera que suba.

## 18. Pruebas y revisión técnica
**Pregunta adicional:** ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?
Que las entradas y salidas funcionen como se sepera.

## 19. Práctica adicional
**Pregunta:** ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
La búsqueda de rutas o caminos mínimos.

## 20. Cierre
**Pregunta:** ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
La de decidir entre aristas según su peso.