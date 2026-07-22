# Arturo Prudencio Bonilla 

## seccion 1

¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?

    A -> D

    A -> B -> D


¿Por qué contar aristas ya no es suficiente en un grafo ponderado?

    Porque ahora las aristas tiene un coste por pasar por ellas, por lo que la cantidad de aristas no refleja el costo real de recorrer el grafo

## seccion 2

¿En qué condición BFS sí garantiza caminos de costo mínimo?

    CUando es un grafo no ponderdo o si lo es, que todas las aristas pesen lo mismo

## seccion 3

¿Qué representan nodos, aristas y pesos en esta red?

    Nodos, ciudades. 

    Aristas, carreteras

    Peso, tiempo de recorrido

## seccion 4

¿Qué significa infinito en la tabla de distancias?

    QUe se desconocen todos los caminos


## seccion 5

¿Qué tres valores comparamos al relajar una arista?

    la distancia actual, la candidata y la arista

## seccion 6

¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
    
    Porque borrar una entrada arbitraria dentro de un heap complicaría la implementación.

    Al extraer una entrada obsoleta, su distancia no coincidirá con la mejor distancia registrada en ese momento, por lo que simplemente se ignora y se continúa.

## seccion 7 

¿Qué componente del par funciona como prioridad y cuál como elemento?

    En el par (distancia, nodo), la distancia actúa como la prioridad y el nodo como elemento 

## seccion 8 
¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?

    El algoritmo calcula los caminos mínimos desde un nodo de origen en un grafo ponderado

    La restricción esencial es que los pesos del grafo deben ser no negativos

## seccion 9 

```text
para cada nodo:
    distancia[nodo] = infinito
    predecesor[nodo] = ninguno

distancia[origen] = 0
`insertar (0, origen) en la cola de prioridad`

mientras la cola no esté vacía:
    `extraer (distancia_extraida, actual)`

    si distancia_extraida no coincide con distancia[actual]:
        ignorar esta entrada y continuar

    para cada (vecino, peso) de actual:
        candidata = distancia[actual] + peso
        si candidata < distancia[vecino]:
            distancia[vecino] = candidata
            predecesor[vecino] = actual
            `insertar (candidata, vecino)`
```
## seccion 10

¿Cuál es el orden de extracción vigente en el ejemplo mínimo?

    El orden de las extracciones vigentes es (0,A), (1,B) y (3,C)

## seccion 11

¿Cuáles son las distancias finales desde A en la red conductora?

    Las distancias finales son: A=0, B=3, C=1, D=4 y E=7

## seccion 12

¿Por qué recorremos predecesores desde el destino y después invertimos?

    Porque el mapa de predecesores apunta hacia atrás, registrando desde qué nodo anterior se llegó al actual; al recorrer esta secuencia, se obtiene el camino desde el destino hasta el origen, por lo que es necesario invertirla para obtener la ruta correcta


## seccion 13
¿Qué tres representaciones deben permanecer sincronizadas en cada paso?

    La red ponderada
    
    La tabla de distancias y predecesores
    
    El min-heap de candidaturas. 

## seccion 14

¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?

    dijkstra: Valida los pesos, calcula las distancias y registra los predecesores
    
    reconstruir_camino: Sigue el mapa de predecesores para reconstruir la ruta sin volver a recorrer el grafo
    
    camino_minimo: Coordina a las dos funciones anteriores y devuelve el costo y el camino para un destino específico

## seccion 15

¿De dónde proviene el factor logarítmico de Dijkstra con heap?

    Proviene de las operaciones de la cola de prioridad

## seccion 16 

Actividad: Explica por qué una ruta con más aristas puede ser mejor

    Porque lo que se minimiza es la suma total de los pesos (el costo acumulado), no la cantidad de saltos o aristas. Una ruta con muchos tramos de peso pequeño puede sumar menos que un solo tramo directo muy costoso

¿Cuál es el costo y camino mínimo de A a E en la red conductora?

    El camino mínimo es A → C → B → D → E

    El costo total es 7


## seccion 17

¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?

    Porque el algoritmo confía en que avanzar por nuevas aristas no reducirá el costo acumulado por debajo de la menor distancia ya extraída

    Una arista negativa permitiría que un nodo ya procesado y considerado "terminado" pudiera mejorar su costo más adelante

## seccion 18

¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?

    Comprobaría que el camino inicie exactamente en el nodo origen y termine en el nodo destino

¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?

    Un caso de prueba de "mejora múltiple"

    Esto ocurre cuando un camino directo costoso es reemplazado por uno indirecto más barato, dejando en el heap entradas antiguas que el algoritmo debe ser capaz de ignorar correctamente

## seccion 19 

¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?

    La necesidad de procesar o buscar repetidamente la menor distancia pendiente


## seccion 20

¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?

    Para minimizar la suma de pesos, se guardan distancias y predecesores

    Se intenta mejorar las rutas mediante la relajación

    Se procesa la menor distancia pendiente utilizando un min-heap, bajo la restricción esencial de que los pesos sean no negativos


