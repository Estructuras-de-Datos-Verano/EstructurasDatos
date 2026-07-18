# Notebook.md - José Iván Reyna Blanco

## Pregunta inicial

**¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?** Un deque o un heap normal son estructuras naturales para resolver problemas de pendientes. El deque puede bastar si los pendientes tienen la misma prioridad y el heap puede ayudar cuando hay más. 

## 1. Presentación de la clase

**Pregunta:** ¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades? El nivel de urgencia para resolver tareas. También podemos hablar de costos en el mismo sentido dependiendo del problema.

## 2. Problema inicial con pop(0)

**Pregunta:** ¿Qué trabajo repetido introduce pop(0) y por qué una referencia al frente lo evita? Acceder al elemento, borrarlo y después mover de posición a cada elemento restante. En cambio desencolar ahorra la operación de borrar porque mueve la referencia del elemento al siguiente nodo. Es O(n) v.s. O(1).

## 3. Nodo y referencias

**Pregunta:** ¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos? El valor guardado es el dato real que se almacena, el nodo es el contenedor en el que se almacena y la estructura que administra nodos puede ser una cola ligada, una pila o una lista sencilla.

## 4. Lista ligada simple

**Pregunta:** ¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?  Encolar un elemento porque requeriría ir hacia adelante elemento por elemento hasta llegar a 'None' y luego insertarlo. Por eso teniendo la referencia al final es inmediato. 

## 5. Cola ligada

**Pregunta:** ¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean O(1)? Porque conociendo el frente puede moverse la referencia al siguiente elemento al desencolar y conociendo el final se hace un proceso análogo para desencolar. 

## 6. Invariantes de cola

**Pregunta:** ¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento? El frente es None, la cola es None y el tamaño es cero.

## 7. Operaciones manuales

Traza esta secuencia antes de programar. Dibuja cada nodo, las referencias externas y el tamaño. Los primeros pasos sirven de modelo; completa el resto en `notebook.md`.

| Paso | Operación | frente | final | cadena | tamaño | valor devuelto |
| ---: | --- | :---: | :---: | :--- | ---: | :---: |
| 0 | crear cola | `None` | `None` | vacía | 0 | — |
| 1 | `encolar("A")` | A | A | A | 1 | — |
| 2 | `encolar("B")` | A | B | A → B | 2 | — |
| 3 | `encolar("C")` | A | C | A → B → C | 3 | — |
| 4 | `desencolar()` | B | C | B → C | 2 | "A" |
| 5 | vaciar | `None` | `None` | vacía | 0 | — |
| 6 | `encolar("Z")` | Z | Z | Z | 1 | — |

**Pregunta:** En la secuencia manual, ¿qué referencias cambian al desencolar A de la cadena A → B → C? Cuando A se desencola, B se convierte en el frente, el siguiente para A es none y tanto el siguiente para B como el final se quedan igual.

## 8. Complejidad

**Pregunta:** ¿Por qué buscar un valor sigue siendo O(n) aunque encolar y desencolar sean O(1)? Porque cada elemento en la cola requiere de un espacio en la memoria. Entonces para buscar un elemento en el peor escencario (que éste al final), de deben checar los n lugares en la memoria.

## 9. BFS y cola

**Pregunta:** ¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS? El órden de procesamiento FIFO. En una exploración de un grafo con BFS, los nodos a los que se accederá primero serán los primeros en haberse añadido. Si vigiláramos cada paso y a cada nodo procesado lo metiéramos en una lista, tendríamos una cola lista ordenada según órden de aparición. 

## 10. Visitados al encolar

**Pregunta:** ¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse? Que se vuelva a añadir a la lista de descubiertos si el vértice es vecino del siguiente elemento. 

## 11. Predecesores 

**Pregunta:** ¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido? Siempre que sea posible usar dijkstra, resulta ideal guardar un diccionario de predecesores. Teniendo esto, dijkstra puede ejecutar el recorrido y para construirlo en órden solo hace falta acceder a las claves de cada nodo, guardarlas en una lista y devolverla invertida.

## 12. Reconstrucción del camino

**Pregunta:** ¿Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta? Cuando la cadena termina en 'None' tenemos un destino inalcanzable. Si un valor está repetido, la tabla está corrupta porque no puede tener más de un antecesor ningún nodo. 

## 13. Práctica guiada de BFS

| Paso | Sale | Cola después | Nuevos predecesores |
| ---: | :---: | :--- | :--- |
| 0 | — | A | A: `None` |
| 1 | A | B, C | B: A; C: A |
| 2 | B | C, D, E | D: B; E: B |
| 3 | C | D, E | — (ninguno) |
| 4 | D | E, F | F: D |
| 5 | E | F | — (ninguno) |
| 6 | F | vacía | — (ninguno) |

**Pregunta:** ¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos? Porque en un grafo pueden existir muchas formas de recorrerlo. 

## 14. Lista doblemente ligada

**Pregunta:** ¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece? Moverse hacia atrás, pero exige actualizar también el predecesor de cada nodo además de la actualización original de sucesor. 

## 15. Invariantes de lista doble

**Pregunta:** ¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentes? Recorrería predecesores y la lista en órden. La función que devuelve predecesores que implementamos en otra clase ya devuelve una lista invertida así que solo comprobaría que el output fuera el mismo que la lista original. No usaría un set porque eliminaría repetidos, aunque quizás como copia defensiva funcionaría bien. 

## 16. Deque ligada

**Pregunta:** ¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO? Porque una double-ended queue permite operar elementos al inicio o al final con la misma complejidad. 

## 17. Operaciones manuales con Deque

| Paso | Operación | inicio | cadena | final | tamaño | devuelve |
| ---: | --- | :---: | :--- | :---: | ---: | :---: |
| 0 | crear | `None` | vacía | `None` | 0 | — |
| 1 | `agregar_inicio("B")` | B | B | B | 1 | — |
| 2 | `agregar_inicio("A")` | A | A ⇄ B | B | 2 | — |
| 3 | `agregar_final("C")` | A | A ⇄ B ⇄ C | C | 3 | — |
| 4 | `agregar_final("D")` | A | A ⇄ B ⇄ C ⇄ D | D | 4 | — |
| 5 | `quitar_inicio()` | B | B ⇄ C ⇄ D | D | 3 | "A" |
| 6 | `quitar_final()` | B | B ⇄ C | C | 2 | "D" |

**Pregunta:** Después de quitar el inicio A de A ⇄ B ⇄ C ⇄ D, ¿qué cuatro hechos deben comprobarse? Que el sucesor de A sea 'None', que el inicio sea B, que su antecesor sea 'None' y que el sucesor de D sea 'None'. 

## 18. Qué problema resuelve 0-1 BFS

**Pregunta:** ¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0? Porque BFS siempre prefiere caminos de menos aristas, pero cuando los costos son cero o 1, va a evitar recorridos de quizás 3 nodos para llegar al destino con aristas de peso cero. En cambio 0-1 BFS mediante relajación puede modificar el antecesor.

## 19. Deque como estructura de prioridad

**Pregunta:** ¿Qué información del peso decide el extremo de inserción y por qué? Si mejora el peso con cero, se inserta al frente. Si mejora con peso 1, va al final y respeta FIFO.

## 20. Ejecución manual de 0-1 BFS

Usa el grafo conductor:

```python
{"A": [("B", 0), ("C", 1)], "B": [("D", 0), ("E", 1)],
 "C": [("D", 0)], "D": [("F", 1)],
 "E": [("F", 0)], "F": []}
```

| paso | sale | arista | decisión | deque inicio→final | cambio de distancia |
| ---: | :---: | :--- | :---: | :--- | :--- |
| 0 | — | — | agregar origen | A | d(A)=0 |
| 1 | A | A→B (0) | inicio | B | d(B)=0 |
| 2 | A | A→C (1) | final | B,C | d(C)=1 |
| 3 | B | B→D (0) | inicio | D, C | d(D)=0 |
| 4 | B | B→E (1) | final | D, C, E | d(E)=1 |

**Pregunta:** Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X? Se agrega al inicio y su distancia cambia de 1 a 0.

## 21. Implementación

**Pregunta:** ¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo? Creo que poder recordar de una vez que responsabilidades hace falta cubrir y verificar que en esa etapa los contratos se cumplen, en vez de amontonar todo al final. 

# 22. Casos límite
**Pregunta:** ¿Por qué True debe producir TypeError aunque isinstance(True, int) sea verdadero en Python? Porque 'True' lo usamos para validar comparaciones, no como una distancia. Si por alguna razón una arista tuviera distancia 'True' y no validamos, el código va a funcionar usando 'True' como 1. 

## 23. Pruebas

**Pregunta:** ¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura? Detecta el defecto de punteros residuales o "fantasmas" (Stale Pointers) y la desincronización del contador de tamaño. 

## 24. Comparación BFS, 0-1 BFS y Dijkstra

**Pregunta:** ¿Qué operación dominante conduce respectivamente a cola, deque o heap? Cuando se necesita explorar un grafo donde no hay pesos, BFS con órden de llegada por capas es idóneo. Cuando hay pesos 0 o 1 estrictos, deque con adelantar costo 0 y posponer costo 1 es idóneo. Cuando hay casos de pesos enteros no negativos generales, dijsktra extrayendo distancias mínimas candidatas y usando relajación con colas de prioridad es idóneo.

## 25. Cierre

**Pregunta:** ¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos? ¿Pertenecen los dos nodos a un mismo conjutno? Cuando deja de haber un origen claro, hay que preguntarse si ya hay aristas o si no, no solo encontrarlas y recorrer el camino. 
