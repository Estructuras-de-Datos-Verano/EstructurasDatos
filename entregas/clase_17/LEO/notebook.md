# Notebook clase 17 - Leonardo Daniel Arenas Serafín

## Pregunta inicial

#### ¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?
Cuando se tiene la misma prioridad podemos usar un solo criterio para poder decidir cuál elemento tiene prioridad como puede ser orden de entrada (FIFO, LIFO) o los propios valores de los elementos (BST, heaps), pero al tener dos niveles de prioridad podríamos intentar establece cuál nivel es má crucial que el otro y así poder discernir entre elementos.

## 1. Presentación de la clase

#### ¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades?
Que para poder saber qué elementos tienen la prioridad, ahora debemos de utilizar dos estructuras, una por cada prioridad, en donde en una se discierne sobre un criterio principal más crucial y después en la segunda, la cual contendrá a las prioridades del primer criterii¿o, se le pueda aplicar un nuevo orden de prioridad para saber cuál es el más importante.

## 2. Problema inicial con pop(0)

#### ¿Qué trabajo repetido introduce pop(0) y por qué una referencia al frente lo evita?
Que cada vez que retiramos el elemento del frente se debe de volver a organizar toda la lista ya que hay que recorrer todos los elementos. Una referencia al frente lo evita en el sentido de que el "frente" es también un final y simplemente se está operando con los últimos elementos, lo que evita que se tengan recorrer los demás.

## 3. Nodo y referencias

#### ¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos?
Un nodo es un elemento de nuestra nueva estructura administradora, es como en una lista, la estructura que administra es la bolsa y los nodos son los elementos que están organizados. Dentro de los nodos están los valores guardados que dan información del nodo.

## 4. Lista ligada simple

#### ¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?
Que si queremos desencolar el último elemento de la lista, deberíamos de recorrer toda la lista para poder llegar al final.

## 5. Cola ligada

#### ¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean O(1)?
Porque si no tuvieramos alguna, al agregar o retirar un nodo tendríamos que recorrer todos los nodos para mantener el orden lo cual tendría O(n).

## 6. Invariantes de cola

#### ¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento?
final == inicio. siguiente is None. Retirado.siguiente is None.

## 7. Operaciones manuales

| Paso | Operación | frente | final | cadena | tamaño | valor devuelto |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear cola | `None` | `None` | vacía | 0 | — |
| 1 | `encolar("A")` | A | A | A | 1 | — |
| 2 | `encolar("B")` | A | B | A → B | 2 | — |
| 3 | `encolar("C")` | A | C | A → B → C | 3 | — |
| 4 | `desencolar()` | B | C | B → C | 2 | A |
| 5 | vaciar | `None` | `None` | vacía | 0 | ? |
| 6 | `encolar("Z")` | Z | Z | Z | 1 | — |

#### Antes de pulsar **Siguiente**, predice qué enlace o extremo cambiará. 
Cambiará el final porque se encolará C

#### En la secuencia manual, ¿qué referencias cambian al desencolar A de la cadena A → B → C?
El frente se vuelve B y el tamaño 2.

## 8. Complejidad

#### ¿Por qué buscar un valor sigue siendo O(n) aunque encolar y desencolar sean O(1)?
Porque ene sta estructura lo que se facilita es tener acceso al inicio y al final, pero a final de cuentas sigue siendo una secuencia, por lo que buscar sigue requiriendo O(n)

## 9. BFS y cola

#### ¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS?
Que en el BFS se procesa por capas, capas que están organizadas por orden de entrada, de esta forma se procesan las que primero fueron encoladas, es decir, lleva un comportamiento FIFO.

## 10. Visitados al encolar

#### ¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse?
Que se puede llegar a un mismo vértice desde varios otros, por lo que si se marca solo al desencolarse, se estaría descubriendo ese mismo vértice el número de vértices conectados a éste. 

## 11. Predecesores

#### ¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido?
Mappear cada vecino y asignarle el nodo actual como su predecesor, para así poder ir consultando el predecesor por cada nodo e ir reconstruyendo el camino.

## 12. Reconstrucción del camino

#### Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta?
El destino inalcanzable se distingue porque existe un nodo el cual se predecesor es None. En cambio en una tabla de predecesores corrupta siempre hay predecesores, pero se repiten en un bucle.

## 13. Práctica guiada de BFS

| paso | sale | cola después | nuevos predecesores |
| ---: | --- | --- | --- |
| 0 | — | A | A: `None` |
| 1 | A | B, C | B: A; C: A |
| 2 | B | C, D, E | D: B; E: B |
| 3 | C | D, E | - |
| 4 | D | E, F | F: D |

####  ¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos?
Porque los vecinos pueden estar conectados entre ellos, por lo que su longitud puede permanecer igual.

## 14. Lista doblemente ligada

#### ¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece?
Obtenemos la capacidad de poder tomar los extremos de la lista por igual con un costo mínimo. La obligación de consistencia es que para todo el predecesor de su sucesor debe ser él mismo y viceversa, además que en cada inserción/eliminación sea frontal o final, debe de llevarse esta información.

## 15. Invariantes de lista doble

#### ¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentes?
(nodo_actual.siguiente).anterior = nodo_actual

## 16. Deque ligada

#### ¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO?
Porque en el deque puedes insertar y retirar por delante y por detrás, por lo que puede tener cualquier comportamiento. El comportamiento FIFO o LIFO se determina por el agloritmo en el que está siendo usado según la necesidad de éste.

## 17. Operaciones manuales de deque

| paso | operación | inicio | cadena | final | tamaño | devuelve |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear | `None` | vacía | `None` | 0 | — |
| 1 | `agregar_inicio("B")` | B | B | B | 1 | — |
| 2 | `agregar_inicio("A")` | A | A ⇄ B | B | 2 | — |
| 3 | `agregar_final("C")` | A | A ⇄ B ⇄ C | C | 3 | — |
| 4 | `agregar_final("D")` | A | A ⇄ B ⇄ C ⇄ D | D | 4 | — |
| 5 | `quitar_inicio()` | B | B ⇄ C ⇄ D  | D | 3 | A |
| 6 | `quitar_final()` | B | B ⇄ C | C | 2 | D |

#### Después de quitar el inicio A de A ⇄ B ⇄ C ⇄ D, ¿qué cuatro hechos deben comprobarse?
Que B.predecesor is None. Que tamaño == 3. Que A.sucesor is None. Que incio es B

## 18. Qué problema resuelve 0-1 BFS

#### ¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0?
Porque BFS se basa en número de aristas, por lo que si en un camino tenemos más aristas que en otro, aunque el otro cueste más y el primero tenga costo 0, se elegirá  el otro.

## 19. Deque como estructura de prioridad

#### ¿Qué información del peso decide el extremo de inserción y por qué?
EL costo cero decide insertarse al inicio y el costo uno decide insertarse al final para así poder llevar una prioridad no solo de llegada sino de costo.

## 20. Ejecución manual de 0-1 BFS

| paso | sale | arista | decisión | deque inicio→final | cambio de distancia |
| ---: | --- | --- | --- | --- | --- |
| 0 | — | — | agregar origen | A | d(A)=0 |
| 1 | A | A→B (0) | inicio | B | d(B)=0 |
| 2 | A | A→C (1) | final | B,C | d(C)=1 |
| 3 | B | B→D (0) | inicio | D,C | d(d)=0 |
| 4 | B | B→E (1) | final | D,C,E | d(E)=1 

#### Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X?
Se agrega X al inicio por tener distancia 0 y se cambia la distancia a uno menos y se actualiza el predecesor.

## 21. Implementación

#### ¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo?
Tiene la ventaja de que podemos conocer exactamente cómo funcionan, cuáles son sus atributos y sus métodos para poder usarlos correctamente y que no existan mal entendidos o ambiguedades.

## 22. Casos límite

#### ¿Por qué True debe producir TypeError aunque isinstance(True, int) sea verdadero en Python?
Porque Python reconoce los valores booleanos como integrers

## 23. Pruebas

#### ¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura?
Que no sea el caso de que cuando se vacíe no se detecte que el tamaño == 0 y que tanto los siguientes y anteriores sean None.

## 24. Comparación BFS, 0-1 BFS y Dijkstra

#### ¿Qué operación dominante conduce respectivamente a cola, deque o heap?
Cola corresponde a FIFO. Deque corresponde a agregar al inicio costos 0 y al final costo 1. Heap corresponde a poder evaluar distintos pesos no negativos y priorizar.

## 25. Cierre hacia Union-Find y Kruskal

#### ¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos?
¿A qué hay que darle prioridad para óptimizar este proceso?