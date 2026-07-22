# Notebook - Clase 09 - Leonardo Daniel Arenas Serafín

#### ¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?
Para modelar una secuencia solamente es necesario mantener un orden de entrada y salida, es una estructura lineal. En cambio una relación requiere de un criterio, requiere de una regla específica para poder establecer el lazo y s necesita otro tipo de estructura para almacenar los datos de cuáles relacions hay.

## 1. Problemas motivadores CSES

#### ¿Qué representa un nodo?
- Building Roads: representa una ciudad
- Counting Rooms: representa suelo
- Labrynth: representa suelo
- Message Route: representa una computadora

#### ¿Qué representa una arista?
- Building Roads: representa un camino
- Counting Rooms: representa que no hay un muro en medio
- Labrynth: representa que no hay un muro en medio
- Message Route: representa una conexión entre computadora

#### ¿Es dirigido?
- Building Roads: No
- Counting Rooms: No
- Labrynth: Sí
- Message Route: No

#### ¿Es ponderado?
- Building Roads: No
- Counting Rooms: No
- Labrynth: No
- Message Route: No

#### ¿Qué pregunta algorítmica aparece?
- Building Roads: ¿Cómo podemos saber qué caminos son necesarios construir para que todas las ciudades estén conectadas sin que haya más de un camino entre dos ciudades?
- Counting Rooms: ¿Cómo podemos saber cuando hay un muro de por medio o no?
- Labrynth: ¿Cómo podemos minimizar el camino?
- Message Route: ¿Cómo podemos saber cuál relación existe entre dos computadoras?


## 2. Modelado de relaciones

| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | representa una ciudad | representa un camino | No | No | ¿Cómo podemos saber qué caminos son necesarios construir para que todas las ciudades estén conectadas sin que haya más de un camino entre dos ciudades? |
| Counting Rooms | representa suelo | representa que no hay un muro en medio | No | No | ¿Cómo podemos saber cuando hay un muro de por medio o no? |
| Labyrinth | representa suelo | representa que no hay un muro en medio | Sí | No | ¿Cómo podemos minimizar el camino? |
| Message Route | representa una computadora | representa una conexión entre computadora | No | No | ¿Cómo podemos saber cuál relación existe entre dos computadoras? |


## 3. Conceptos básicos de grafos

####  Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.
- Grafo dirigido: Un grafo que represente los estados de amistad en una red social, las aristas tienen orientación ya que una persona puede seguir a otra, pero la otra puede no seguir de vuelta a la una. 
- Grafo no dirigido: Un grafo que represente películas con plataformas de streaming. No tienen orientación las aristas porque la relación que existe entre una película y en dónde es streammeada no implica direccionalidad. 

## 4. Representaciones

#### ¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?
Ambas operaciones son igual de importantes, porque al preguntar si existe una arista estás preguntando simplemente si existe una relación entre dos elementos, lo cual es básico pero crucial. En el caso de listar vecinos, es muy importante porque esta operación permite que haya un análisis más profundo del grafo.

## 5. Interfaz común

#### ¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?
Porque una lista es una matriz de tamaño 1xn. De esta forma peds hacer que ambas estructuras mantengan un mismo comportamiento para ahorrar código y complejidad.

## 6. Implementaciones

#### ¿Por qué un `set` ayuda a evitar aristas duplicadas?
Porque en un conjunto no hay repetidos, si "aparece" una arista dos veces en el conjunto, el conjuno solo identificará que la arista pertenece mas no cuántas veces.

#### ¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?
Se debe de agregar una dimensión más a cada una de las dimensiones. Es decir, si teníamos una matriz de nxn, entonces al agregar un nuevo vértice la matriz nueva será de (n+1)x(n+1) ya que la última fila representará el estatus del nuevo vértice en relación con todos los demás vértices y la última columna representará el estatus de todos los demás vértices con el nuevo.


| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Utiliza poca memoria al solo tener un diccionario | Utiliza más memoria al tener un diccionario y una lista de listas |
| Facilidad de implementación | Difícil de implementar pero posible | Bastante más difícil de implementar al tener dos dimensiones |
| Consultar vecinos | Bastante fácil pues esa información está guardada en el diccionario | Es bastante difícil pues para hacerlo tuve que implementar 4 iteraciones distintas |
| Consultar si existe arista | Muy fácil | Muy fácil |
| Grafos dispersos | Se visualizaría al tener conjuntos pequeños en el diccionario | Se visualizaría al ver que hay muchos False |
| Grafos densos | Se visualizaría al tener conjuntos grandes en el diccionario | Se visualizaría al ver que hay muchos True |

## 7. Visualización con NetworkX

#### ¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?
Para que los demás usuarios que quieran consultar tu implementación tengan la facilidad de trabajar con una biblioteca externa conocida.

## 8. Diseño de pruebas

#### Diseña al menos dos pruebas propias y explica qué comportamiento verifican.
- test_consistencia_vecinos_y_aristas_LEO(): este test verifica que existe consistencia entre las aristas que hay y los vecinos que se marcan
- test_vertices_funciona_LEO(): este test verifica que el método que yo mismo agregué para saber cuáles son los vértices del grafo funcione bien

## 9. Patrón descubierto

#### Explica con tus palabras el patrón de modelado de relaciones.
El patrón que se observa es que uno tiene que guardar la información de relaciones en estructuras que permitan la almacenación de datos sin tener que guardar el orden necesariamente. Por ejemplo, en esta clase utilizamos los diccionarios para llevar el conteo de aristas y usamos matrices para guardar información sobre la existencia de relaciones.

## 10. Cierre

#### ¿Qué ganamos al modelar relaciones como grafo?
Ganamos más noción sobre diferentes tipos de estructuras de datos

#### ¿Cuándo usarías lista de adyacencia?
Cuando tenga pocos vértices pues no es necesario darle mayor estructura para que sea legible

#### ¿Cuándo usarías matriz de adyacencia?
Cuando tenemos tantos vértices que el verlo en una lista es muy exhaustivo y engorroso, por lo que sería mejor ordenar las relaciones en dos dimensiones

#### ¿Qué puede ocultar una visualización?
Si no tenemos agregada la orientación de la relación, se puede ocultar la información de si es dirigido o no el grafo.

#### ¿Qué algoritmo necesitaremos para recorrer el grafo?
for, pues al tener listas y diccionarios debemos iterar sobre estos.
