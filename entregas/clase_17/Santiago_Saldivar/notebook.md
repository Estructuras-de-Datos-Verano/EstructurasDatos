# Clase 17 asíncrona: listas ligadas, BFS y 0-1 BFS
**Pregunta:** ¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades?
Que tenemos que comparar según dos criterios.

## 2. Problema inicial con pop(0)
**Pregunta:** ¿Qué trabajo repetido introduce pop(0) y por qué una referencia al frente lo evita?
Desencolar

## 3. Nodo y referencias
**Pregunta:** ¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos?
El nodo es una pieza que guarda el valor. La estructura es la lista.

## 4. Lista ligada simple
**Pregunta:** ¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?
Desencolar

## 5. Cola ligada
**Pregunta:** ¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean O(1)?
Porque si no tendríamos que recorrer de más.

## 6. Invariantes de cola
**Pregunta:** ¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento?
Si es vacía, frente y final es None
Si hay un nodo, el frente es el final
Frente alcanza exactamente tamaño nodos, final es el último.

## 7. Operaciones manuales
| Paso | Operación | frente | final | cadena | tamaño | valor devuelto |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear cola | `None` | `None` | vacía | 0 | — |
| 1 | `encolar("A")` | A | A | A | 1 | — |
| 2 | `encolar("B")` | A | B | A → B | 2 | — |
| 3 | `encolar("C")` | A | B | A - B -C | 3 | — |
| 4 | `desencolar()` | B | C | B-C | 2 | a |
| 5 | vaciar | none | none | - | 0 | - |
| 6 | `encolar("Z")` | Z | Z | Z | 1 | Z |

**Pregunta:** En la secuencia manual, ¿qué referencias cambian al desencolar A de la cadena A → B → C?
inicio

# 8 Complejidad
**Pregunta:** ¿Por qué buscar un valor sigue siendo O(n) aunque encolar y desencolar sean O(1)?porque revisa todo

## 9. BFS y cola
**Pregunta:** ¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS?
Que en BFS va revisando los primeros niveles, como en FIFO

## 10. Visitados al encolar
**Pregunta:** ¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse?
Que se vuelva a visitar redundantemente.

## 11. Predecesores
**Pregunta:** ¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido?
Los predecesores

## 12. Reconstrucción del camino
**Pregunta:** ¿Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta?
Si no está en las claves de ningún nodo

## 13. Práctica guiada de BFS
**Pregunta:** ¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos?
Porque sigue habiendo la misma cantidad

## 14. Lista doblemente ligada
**Pregunta:** ¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece?
Podemos ir en ambas direcciones
Cada antecesor y predecesor deben conectarse bilateralmente

## 15. Invariantes de lista doble
**Pregunta:** ¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentes?
Revisando las claves

## 16. Deque ligada
**Pregunta:** ¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO?
Porque podría aceptar funciones de ambas

## 17. Operaciones manuales de deque

| paso | operación | inicio | cadena | final | tamaño | devuelve |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear | `None` | vacía | `None` | 0 | — |
| 1 | `agregar_inicio("B")` | B | B | B | 1 | — |
| 2 | `agregar_inicio("A")` | A | A ⇄ B | B | 2 | — |
| 3 | `agregar_final("C")` | A | A-B-C | C | 3 | — |
| 4 | `agregar_final("D")` | D | A-B-C-D | D | 4 | — |
| 5 | `quitar_inicio()` | A | B-C-D | D | 3 | A |
| 6 | `quitar_final()` | D | C | B-C | 2 | D |

**Pregunta:** Después de quitar el inicio A de A ⇄ B ⇄ C ⇄ D, ¿qué cuatro hechos deben comprobarse?
que b sea inicio
que d sea final
que todos estén conectados
que a no esté

## 18. Qué problema resuelve 0-1 BFS
**Pregunta:** ¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0?
Porque espera que siempre aumente

## 19. Deque como estructura de prioridad
**Pregunta:** ¿Qué información del peso decide el extremo de inserción y por qué?
Si mejora, para elegir la mejor ruta

## 20. Ejecución manual de 0-1 BFS
**Pregunta:** Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X?
Cambia el peso total. Se agrega al grafo

## 21. Implementación
**Pregunta:** ¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo?
Que detectamos errores antes que nada

## 22. Casos límite
**Pregunta:** ¿Por qué True debe producir TypeError aunque isinstance(True, int) sea verdadero en Python?
Porque queremos números

## 23. Pruebas
**Pregunta:** ¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura?
El vaciado y llenado correcto

## 24. Comparación BFS, 0-1 BFS y Dijkstra
**Pregunta:** ¿Qué operación dominante conduce respectivamente a cola, deque o heap?
Desencolar

## 25. Cierre hacia Union-Find y Kruskal
**Pregunta:** ¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos?
Cómo elegirlas y formar la mejor ruta
