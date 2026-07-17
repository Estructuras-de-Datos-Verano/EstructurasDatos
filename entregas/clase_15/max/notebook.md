# Notebook_clase_15_Max

## Sección 0 (Pregunta inicial)

¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?

Lo que se me puede llegar a ocurrir que puede solucionar este problema, es que le podemos dar cierto peso o valor a cada camino, mientras mayor sea este costo quiere decir que menos conviene, por lo que podemos programar para elegir los más baratos. 

## Sección 1 (Por qué BFS ya no basta)

¿Por qué contar aristas ya no es suficiente en un grafo ponderado?

Porque ya no nos importa unicamente el número de aristas o e conexiones que haya entre ciertas cosas, si no que tambien que valor tienen estas aristas en cuestión.

¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?

Una estrategia que solamente compare niveles tambien compararia las cosas entre las diferentes ciudadedes pero en distancias, en cambio la estrategia para comparar costos es la de pesos

## Sección 2 (Recordatorio de BFS)

¿En qué condición BFS sí garantiza caminos de costo mínimo?

Unicamente se me ocurre que en un escenario con mucha suerte e ideal, donde agarre los caminos más cortos y estos coincidan en que sean los más baratos, unicamente así se me ocurre que se pueda.

## Sección 3 (Red de ciudades conductora)

¿Qué representan nodos, aristas y pesos en esta red?

En esta red en particular, lo que representan los nodos son las ciudades, las aristas las calles y por cada calle se le agrega el valor de cada carretera.

enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.

A a B, B a D, D a E, y costaría 8
De A a C, de C a E y costaría: 8

## Sección 4 (Distancias tentativas)

¿Qué significa infinito en la tabla de distancias?

Significa que todavia no hemos recorrido esos caminos, por lo cual el infinito no representa acá algo que no tenga fin, si no que representa algo que no se conoce.

## Sección 5 (Relajación)

¿Qué tres valores comparamos al relajar una arista?

Los costos de la carretera, la distancia entre las mismas y las decisiones que se tomaron.

## Sección 6 (Mejoras sucesivas)

¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?

Por la naturaleza del funcionamiento del heap, no es algo del tipo FIFO, entonces se pueden actualizar y reacomodar las cosas sin la necesidad de andar rehaciendo todos los pasos.

## Sección 7 (Descubrimiento de la cola de prioridad)

¿Qué componente del par funciona como prioridad y cuál como elemento?

Las arristas pasan a segundo plano, ya que no nos importa tanto cuales sean, y la información principal pasa a sel el precio de la ponderación de las mismas, ya que esta si nos interesa.

## Sección 8 (Algoritmo de Dijkstra)

¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?

El problema originalq ue resuelve es el problema de eficiencia, ya que con este algoritmo ya podemos elegir caminos más eficientes, y la restricción que tienen los pesos es que no pueden haber pesos negativos.

## Sección 9 (Pseudocódigo y entradas obsoletas)

subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.

```text
para cada nodo:
    distancia[nodo] = infinito
    predecesor[nodo] = ninguno

distancia[origen] = 0
insertar (0, origen) en la cola de prioridad

mientras la cola no esté vacía:
    extraer (distancia_extraida, actual)

    si distancia_extraida no coincide con distancia[actual]: #1
        ignorar esta entrada y continuar

    para cada (vecino, peso) de actual:
        candidata = distancia[actual] + peso #2
        si candidata < distancia[vecino]: #3
            distancia[vecino] = candidata
            predecesor[vecino] = actual
            insertar (candidata, vecino)
```

¿En qué momento se ignora una entrada obsoleta?

EN el momento que encontramos un camino más barato, ya que una vez que lo encontramos lo ignoramos por completo porque ya no nos sirve esta información

## Sección 10 (Recorrido manual mínimo)

¿Cuál es el orden de extracción vigente en el ejemplo mínimo?

El orden de extracción en este ejemplo es A, B, C y ya y ahí mismo se ve que esta eligiendo a las más baratas

## Sección 11 (Recorrido manual intermedio)

| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` | D=4 | A0 B3 C1 D3 E∞ | B←C, D←C D←B |
| `(4,D)` | E=7 | A0 B3 C1 D3 E7 | B←C, D←C D←B E←D |
| `(7,E)` | obsoleta | A0 B3 C1 D3 E7 | B←C, D←C D←B E←D |

¿Cuáles son las distancias finales desde A en la red conductora?

Las distancias finales son vienen siendo los costos de cada carretera para llegar al destino final, que en este caso es el nodo E.

## Sección 12 (Reconstrucción del camino)

¿Por qué recorremos predecesores desde el destino y después invertimos?

Para así poder comparar carreteras y así elegir la más barata, ya que de no hacerlo no podremos elegir la más barata.

## Sección 13 (Visualización interactiva)

¿Qué tres representaciones deben permanecer sincronizadas en cada paso?

Las tres entradas que deben de permanecer sincronisadas en cada paso son: Nodo actual, nodo recorrido y nodo seleccionado, llamese a nodo seleccionado como el nodo que se elgio basado en el camino más barato.

en “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.

Las entradas obsoletas se tienen porque a final de cuentas esos caminos dejan de ser rentables por los costos de los mismos.

## Sección 14 (Implementación)

¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?

Tienen tres funciones principales, las cuales vienen siendo las de analizar el camino recorrido, ver si el camino es rentable para agilizar costos y de volverlo a recorrer para poder ver si en verdad es el más rentable.

## Sección 15 (Complejidad)

¿De dónde proviene el factor logarítmico de Dijkstra con heap?

Proviene del de la manera en la que funcionan los árboles, ya que por naturaleza este tipo de arboles tiene este tipo de ventaja en la cúal se tiene que esta bastante más econonomico a la horra de elegir caminos, porque se van descartando.

## Sección 16 (Problema guiado: entrega urgente)

| Concepto | Resultado que debes completar |
| --- | --- |
| Orden de extracciones vigentes | A, B, C, D, E |
| Mejoras de B | Costos 1 |
| Mejoras de D | Costos 2 |
| Mejoras de E | Costos 3 |
| Predecesores finales | A, B, C, (D, 4) |
| Camino A→E | A, B, C, D, E |
| Costo total | 10 |

¿Cuál es el costo y camino mínimo de A a E en la red conductora?

El costo vendria viendo el más corto que hay y esto implica que sea el camino más corto

## Sección 17 (Limitaciones y pesos negativos)

¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?

Porque meter a una arista negativa nos a substraer del costo total, en lugar de sumarlo, lo cual ya sabemos que nunca sucede en la vida cotidiana.

## Sección 18 (Pruebas y revisión técnica)

¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?

El caso de ver manualmente cual es ekl costo menor y comparar si es que es verdad esto del costo menor con lo que nos arroje el programa de vuelta.

## Sección 19 (Práctica adicional)

¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?

Para empezar el problema necesita que se tenga una ponderación por cada camino disponible, luego, se necesita que cada nodo este conectado, y con esto ya se pueden hacer caminos para poder ver que tipo de camino es el más rentable.

## Sección 20 (Cierre)

¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?

La unica diferencia y la elemental sería el ver que la ponderación en la cual se esta tomando en cuenta para cada arista sea la más barata.

## Sección 21 (Tabla de la practica)

| Extracción | Arista | Candidata | Comparación | Decisión | Heap después |
| --- | --- | ---: | --- | --- | --- |
| `(0,A)` | `A→B` | B | Costosa | No tomarla | A→C |
| `(0,A)` | `A→C` | C | Barata | Tomarlo | A→C |
| `(1,C)` | `C→B` | B | Barata | Tomarlo | C→B |
| `(1,C)` | `C→D` | D | Barata | Tomarlp | C→D |
| … | A→D| No hay | No hay | No hay | No hay |