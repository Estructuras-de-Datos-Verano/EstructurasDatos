# Respuestas del notebook — Clase 17 - Aristeo
## Pregunta inicial
### ¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?
Una cola debería de jalar porque el orden de llegada determina el orden de atención; cuando se introducen dos niveles de prioridad, se necesita una deque.

### 1. Presentación de la clase
Cuando pasamos de una a dos prioridades, el orden de llegada FIFO estricto ya no es suficiente para garantizar la ruta mínima. Necesitamos un mecanismo que permita "adelantar" tareas gratuitas (costo 0) para que se resuelvan antes de avanzar en costo.

### 2. Problema inicial con pop(0)
`pop(0)` en una lista tradicional de Python cuesta $O(n)$ porque obliga a desplazar hacia la izquierda todos los elementos restantes en la memoria contigua. Una referencia al frente de una lista ligada evita esto porque desencolar es simplemente avanzar un puntero: `frente = frente.siguiente`, lo cual se ejecuta en $O(1)$.

### 3. Nodo y referencias
- Valor: El dato real que se desea almacenar (ej. un string `"A"`).
- Nodo: El contenedor que envuelve al valor y contiene las direcciones físicas (referencias) a los nodos adyacentes.
- Estructura Contenedora: El objeto (como `ColaLigada`) que impone las reglas de acceso, mantiene las referencias a los extremos (`frente`, `final`) y el tamaño.

### 4. Lista ligada simple
Si solo guardáramos la referencia al `inicio`, la operación de encolar (añadir al final) sería costosa ($O(n)$) porque tendríamos que recorrer toda la lista desde el inicio para poder ubicar el nodo final y enlazar el nuevo elemento.

### 5. Cola ligada
Necesitamos ambas referencias porque el comportamiento de una cola requiere agregar en un extremo y retirar en el otro. El `frente` nos permite retirar en $O(1)$ y el `final` nos permite insertar en $O(1)$ de manera directa.

### 6. Invariantes de cola
Después de desencolar el único elemento, las tres condiciones que deben cumplirse simultáneamente son:
1. `_frente is None`
2. `_final is None`
3. `_tamano == 0`

### 7. Operaciones manuales
A continuación se muestra la tabla manual completa basada en la secuencia de operaciones:

| Paso | Operación | frente | final | cadena | tamaño | valor devuelto |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear cola | `None` | `None` | vacía | 0 | — |
| 1 | `encolar("A")` | A | A | A | 1 | — |
| 2 | `encolar("B")` | A | B | A → B | 2 | — |
| 3 | `encolar("C")` | A | C | A → B → C | 3 | — |
| 4 | `desencolar()` | B | C | B → C | 2 | "A" |
| 5 | vaciar | `None` | `None` | vacía | 0 | "B", "C" |
| 6 | `encolar("Z")` | Z | Z | Z | 1 | — |

Predicción de referencias al desencolar A de la cadena A → B → C:
- El `frente` cambia de apuntar a `A` para apuntar al nodo `B`.
- El enlace `siguiente` del nodo `A` (retirado) se limpia poniéndose en `None` para evitar fugas de memoria.
- El puntero `final` permanece apuntando al nodo `C`.

### 8. Complejidad
Buscar un valor requiere recorrer secuencialmente la lista desde el nodo inicial hasta el final si el elemento no se encuentra, inspeccionando cada puntero, lo que toma $O(n)$. Las operaciones de inserción/borrado directo ocurren exclusivamente en los extremos apuntados por referencias directas, permitiendo tiempo $O(1)$.

### 9. BFS y cola
El orden FIFO procesa los nodos en el orden exacto en que son descubiertos. Dado que los vecinos más cercanos se descubren primero, FIFO garantiza que se procesen por completo todos los nodos a distancia $d$ antes de procesar cualquier nodo a distancia $d+1$.

### 10. Visitados al encolar
Si marcamos un vértice como visitado solo al desencolarlo, un mismo nodo que tiene múltiples predecesores en la misma capa puede ser encolado múltiples veces antes de ser procesado por primera vez, lo que causa una explosión de duplicados innecesarios en memoria y tiempo de ejecución.

### 11. Predecesores
Un mapa o diccionario de predecesores (`predecesores[nodo] = padre`) almacena la relación inversa del camino mínimo. Con esta información se puede reconstruir cualquier camino yendo hacia atrás desde el destino hasta el origen.

### 12. Reconstrucción del camino
- Destino inalcanzable: Al iterar hacia atrás a través de los predecesores, nos topamos con un valor `None` antes de llegar al origen (y el nodo actual no es el origen).
- Tabla corrupta/Cíclica: Un nodo vuelve a aparecer en la secuencia de recorrido hacia atrás, indicando la presencia de un ciclo de referencias que nunca terminaría.

### 13. Práctica guiada de BFS
Tabla de traza manual para el grafo conductor:

| paso | sale | cola después | nuevos predecesores |
| ---: | --- | --- | --- |
| 0 | — | A | A: `None` |
| 1 | A | B, C | B: A; C: A |
| 2 | B | C, D, E | D: B; E: B |
| 3 | C | D, E | (Ninguno nuevo, todos descubiertos) |
| 4 | D | E, F | F: D |

Por qué puede cambiar el camino: Diferentes representaciones o recorridos en el orden de los vecinos (ej. `["C", "B"]` en lugar de `["B", "C"]`) alteran el primer predecesor que registra cada nodo, aunque la longitud de la ruta siga siendo la misma óptima.

### 14. Lista doblemente ligada
- Nueva capacidad: Podemos añadir o remover del final en $O(1)$ sin perder la capacidad de hacer lo mismo en el inicio.
- Obligación: Consistencia bidireccional estricta; siempre que `A.siguiente is B`, se debe garantizar que `B.anterior is A`.

### 15. Invariantes de lista doble
Se puede validar recorriendo la lista desde `inicio` hasta `final`, acumulando los nodos en una lista de ida, y luego repetir el recorrido en sentido inverso desde `final` hasta `inicio`. Ambas secuencias invertidas deben concordar idénticamente y la cuenta de nodos coincidir con `_tamano`.

### 16. Deque
No impone FIFO ni LIFO por sí sola porque proporciona acceso libre e inmediato a ambos extremos del contenedor. Es la lógica del algoritmo cliente la que determina su comportamiento.

### 17. Operaciones manuales de deque
Tabla de traza para la Deque:

| paso | operación | inicio | cadena | final | tamaño | devuelve |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear | `None` | vacía | `None` | 0 | — |
| 1 | `agregar_inicio("B")` | B | B | B | 1 | — |
| 2 | `agregar_inicio("A")` | A | A ⇄ B | B | 2 | — |
| 3 | `agregar_final("C")` | A | A ⇄ B ⇄ C | C | 3 | — |
| 4 | `agregar_final("D")` | A | A ⇄ B ⇄ C ⇄ D | D | 4 | — |
| 5 | `quitar_inicio()` | B | B ⇄ C ⇄ D | D | 3 | "A" |
| 6 | `quitar_final()` | B | B ⇄ C | C | 2 | "D" |

**Hechos tras quitar el inicio A de A ⇄ B ⇄ C ⇄ D:**
1. El valor devuelto es `"A"`.
2. El nuevo `_inicio` apunta al nodo `B`.
3. `B.anterior` ahora es `None`.
4. Los enlaces `anterior` y `siguiente` del nodo `A` retirado apuntan a `None`.

### 18. Qué problema resuelve 0-1 BFS
BFS común asume costos de transición uniformes. Cuando hay aristas de costo 0, una ruta con más aristas pero de costo cero puede ser globalmente más barata que una ruta directa de costo uno. BFS común se equivocaría al enfocarse en el número de pasos.

### 19. Deque como estructura de prioridad
El peso de la arista determina el extremo de inserción:
- Peso 0: Al inicio (se procesa inmediatamente en la capa de costo actual).
- Peso 1: Al final (se pospone hasta resolver todos los candidatos de costo actual).

### 20. Ejecución manual de 0-1 BFS

| paso | sale | arista | decisión | deque inicio→final | cambio de distancia |
| ---: | --- | --- | --- | --- | --- |
| 0 | — | — | agregar origen | A | d(A)=0 |
| 1 | A | A→B (0) | inicio | B | d(B)=0 |
| 2 | A | A→C (1) | final | B, C | d(C)=1 |
| 3 | B | B→D (0) | inicio | D, C | d(D)=0 |
| 4 | B | B→E (1) | final | D, C, E | d(E)=1 |

Mejora de X de 1 a 0: Su predecesor cambia al nodo que le ofrece la arista de costo 0, se actualiza `distancia[X] = 0` y el nodo `X` se vuelve a agregar al inicio de la deque.

### 21. Implementación
Implementar y probar las estructuras de forma independiente simplifica la depuración al aislar la lógica de manipulación de punteros de los problemas algorítmicos de los grafos.

### 22. Casos límite
`True` es una subclase de `int` en Python. Sin embargo, en el contexto de grafos ponderados, un valor booleano no representa una magnitud numérica de costo válida para transiciones y debe disparar un error de tipo (`TypeError`) de forma defensiva.

### 23. Pruebas
Detecta fugas de memoria, referencias muertas o la permanencia de punteros antiguos que contaminan futuras operaciones al reutilizar un objeto que se supone vacío.

### 24. Comparación BFS, 0-1 BFS y Dijkstra
- Cola (FIFO): No requiere ordenar, asume peso idéntico.
- Deque: Permite dos prioridades fijas y extremas (0 y 1).
- Heap (Cola de Prioridad): Permite prioridades ordenadas de valores arbitrarios arbitrariamente distribuidos.

### 25. Cierre hacia Union-Find y Kruskal
¿Cómo podemos unir componentes dispersas al menor costo posible sin formar ciclos?