# Notebook_clase_09_Max

## Sección 1 (Presentación de la clase)

¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?

Ya que ya hemos avanzado un poco más en el tema, ya puedo responder mejor a esta pregunta, y la respuesta es que la resolución principal es la forma más eficiente en la que se analizan los datos, ya que no se necesita analizar todos los datos para poder encontrar el dato que necesitamos para la actividad o tarea en cuestión.

## Sección 2 (Problemas motivadores CSES)

**Building Roads**

```text
1. ¿Qué representa un nodo?

    En este ejercicio un nodo representa una ciudad.

2. ¿Qué representa una arista?

    Representan las diferentes calles por las cuales se conectan las ciudades.

3. ¿Es dirigido?

    No, las calles no tienen ningun tipo de dirección.

4. ¿Es ponderado?

    No, las calles no representan ningun tipo de ponderación

5. ¿Qué pregunta algorítmica aparece?

    Aparece que ¿Cúal es el menor número de calles para que este algoritmo sea eficiente?

```

**Counting Rooms**

```text
1. ¿Qué representa un nodo?

    Si mal no entendí los nodos representan las paredes que son las que forman los cuartos.

2. ¿Qué representa una arista?

    Las aristas representan el suelo, que vendría siendo la forma en la que estan conectadas las paredes.

3. ¿Es dirigido?

    Si, no es lo mismo que el piso te guie hacia el frente, que hacia un costado, esta es la diferencia entre hacer una habitación de 2x1 que una de 1x2.

4. ¿Es ponderado?

No, generar un "piso" no genera ningún tipo de "cuota".

5. ¿Qué pregunta algorítmica aparece?

    ¿Cúal es el número de cuartos que se creo en este edificio?

```

**Labyrinth**

```text
1. ¿Qué representa un nodo?

    Al igual que el problema anterior, aquí un nodo representa una pared.

2. ¿Qué representa una arista?

    Una arista representa el suelo en el que se van conectando las paredes.

3. ¿Es dirigido?

    Si, al igual que el anterior, no es lo mismo colocar una pared llendo hacia la izquierda, que dirigiendono hacia la derecha.

4. ¿Es ponderado?

    No, generar un suelo no determina ningún tipo de "costo"

5. ¿Qué pregunta algorítmica aparece?

    Yo diria que hay dos ¿Se puede resolver el laberinto?¿Qué tan grande es el laberinto en cuestión? 

```

**Message Route**

```text
1. ¿Qué representa un nodo?

    En este ejercicio, un nodo representa a una computadora, de la cual se van enviando los mensajes.

2. ¿Qué representa una arista?

    Representa la ruta que fueron recorriendo los mensjes de computadora en computadora, hasta llegar al final

3. ¿Es dirigido?

    Si, no es lo mismo mandar un mensaje que recibirlo, adems asi se va siguiendo la ruta.

4. ¿Es ponderado?

    No, enviar y recibir mensajes no tiene ningún tipo de costo en este ejercicio.

5. ¿Qué pregunta algorítmica aparece?

    ¿A donde fue a parar el mensaje enviado?

```

**Observación**

Ninguno de estos 4 ejemplos que se nos pusieron en esta clase cuentan con algun tipo de "costo" en las aristas en el apartado de ponderación.

## Sección 3 (Lectura modelado)



| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudades | Carreteras | No | No | ¿Cúal es el menor número de calles para que este algoritmo sea eficiente? |
| Counting Rooms | Paredes | Pisos | Si | No | ¿Cúal es el número de cuartos que se creo en este edificio? |
| Labyrinth | Pardes | Pisos | Si | No | ¿Se puede resolver el laberinto?¿Qué tan grande es el laberinto en cuestión? |
| Message Route | Computadoras | Lineas de envio de mensaje | Si | No | ¿A donde fue a parar el mensaje enviado? |



## Sección 4 (Conceptos básicos de grafos)

Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.

```text
Mi primer ejemplo de grafo dirigido es el e un paquete en una paqueteria, porque no es lo mismo que el paquete se diriga de la fabrica al almacen, que del almacen a la fabrica.

Mi segundo ejemplo, el de grafos no dirigido, sería de los diferentes caminos que hay aquí en la UP de ir de un anexo a otro, ya que da exactamente lo mismo si ocupas este camino de ida o de vuelta.

```

## Sección 5 (Representación de grafos)

¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?

Con gran diferencia, para mi la pregunta más importante es la de listar vecinos, porque si empezamos por preguntarnos si existe una arista uando la respuesta sea no, podemos llegar a ignorar nodos que no estan conectados, de esta manera, haciendonos esta primera pregunta conocemos a todos los nodos que existen y ya despues vemos si estan conectados o si no lo estan.

## Sección 6 (Interfaz común)

¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?

Nos interesa porque en el fodo tienen el mismo funcionamiento, si bien el objeto que estan analizando es diferente nos debería arrojar al final el mismo resultado, entonces si la impementación resultara ser diferente, no podriamos llegar a mutar un problema para utilizar la segunda implementación.

## Sección 7 (Iplementación 1: GrafoListaAdyacencia)

¿Por qué un `set` ayuda a evitar aristas duplicadas?

Por la naturaleza de la herrmienta, si el usuario llega a cometer algun error y por accidente llega a agregar el mismo valor en segunda ocación o en más ocaciones, por la naturaleza de los conjuntos, sta herramienta nos ayuda a que en este caso solamente se tome una vez este valor, y así nos libramos de problemas bastante innecesarios.

## Sección 8 (Implementación 2 GrafoMatrizAdyacencia)

¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?

Cuando se agregue un nuevo indice, lamatriz debería de hacerce más grande, osea crear más vecinos para que de esta manera esos indices se tomen en cuenta y sus valores tengan sentido, porque de no hacerlo, terminrian aislados.

## Sección 9 (Comparación)

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Toma poca memoria | Toma una mayor cantidad de memoria |
| Facilidad de implementación | Facil | Dificil |
| Consultar vecinos | No es tan eficiente en esto | Es muy eficiente en esto |
| Consultar si existe arista | No es tan eficiente en esto | Es muy eficiente en esto |
| Grafos dispersos | Lo maneja con facilidad | Le cuesta más manejar estos casos |
| Grafos densos | Se cvuelve ineficiente | Es donde este sistema brilla en eficiencia |

## Sección 11 (Convertir implementación propia a NetworkX)

¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?

Porque de esta manera podemos llegar a generalizar un poco toda la implementación y así utilizarla en otros archivos sin la necesidad de andar repitiendo código que ya tenemos, entnonces esto lo vuelve bastante más eficiente a la hora de correrlo.

## Sección 12 (Diseño de pruebas)

Diseña al menos dos pruebas propias y explica qué comportamiento verifican.

Las pruebas que diseñe, lo que hacen es comprobar que se detecten nodos que no estan conectados a travez de aristas, ambas prueban lo mismo con dos pruebas diferentes e hice esto porque la verdad no se me ourrio que más podia probar.

## Sección 13 (Patrón descubierto)

Explica con tus palabras el patrón de modelado de relaciones.

El patron que sigue es una ve que se agragaron las diferentes cosas, entonces se buca que tengan la misma implementación con diferentes terminos para que así se ocupe la más conveniente dependiendo de la cantidad de datos.

## Sección 14 (Cierre)

**1. ¿Qué ganamos al modelar relaciones como grafo?**

```text
Lo que ganamos es que los datos no se tienen que buscar por toda la lista hasta encontrarlos, podemos adoptar un tipo de busqueda conveniente y de esta manera ignorar lo que no nos funciona para asi poder ser más eficientes.

```

**2. ¿Cuándo usarías lista de adyacencia?**

```text
Cuando la cantidad de datos no sea muy grande.

```

**3. ¿Cuándo usarías matriz de adyacencia?**

```text
Cuando necesitemos manejar una cantidad bestial de datos.

```

**4. ¿Qué puede ocultar una visualización?**


```text
Puede ocultar toda la implementación que hay detras, así como las especificaciones.

```

**5. ¿Qué algoritmo necesitaremos para recorrer el grafo?**

```text
Ocupamos tanto BFS como DFS.

```