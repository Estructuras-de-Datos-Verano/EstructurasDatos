# Discusión técnica — Clase 19

## 1. Dependencias
¿Qué significa una arista \(u \to v\) en un grafo de dependencias?
Significa que la tarea \(u\) debe completarse de forma obligatoria antes de poder empezar la tarea \(v\)[cite: 1]. Es un paso a paso estricto, como tener que preparar la masa antes de empezar a hornear.

## 2. DAG
¿Qué es un grafo dirigido acíclico y por qué es necesario?
Es un grafo que respeta las direcciones de las flechas (dirigido) y que no forma caminos cerrados o bucles que regresen al punto de partida (acíclico)[cite: 1]. Es estrictamente necesario porque si hubiera un ciclo, las tareas se esperarían unas a otras infinitamente, lo que impide crear cualquier orden topológico[cite: 1].

## 3. Grado de entrada
¿Qué representa el grado de entrada de un nodo?
Representa cuántas flechas apuntan directamente hacia él, es decir, la cantidad exacta de requisitos previos que aún tiene pendientes por cumplir al inicio[cite: 1].

## 4. Nodos disponibles
¿Por qué un nodo con grado cero puede procesarse?
Porque tener grado cero significa que ya no tiene ningún requisito pendiente esperándolo[cite: 1]. Está totalmente liberado y puede ejecutarse sin violar ninguna regla de dependencia[cite: 1].

## 5. Actualización
¿Qué representa disminuir el grado de un vecino?
Representa que una de las dependencias de ese vecino acaba de ser satisfecha[cite: 1]. Es el equivalente a tachar un pendiente de la lista para estar un paso más cerca de liberarlo.

## 6. Cola
¿Por qué Kahn utiliza una cola?
Porque es la estructura ideal para ir guardando y sacando en tiempo \(O(1)\) las tareas que se van liberando, permitiendo procesar rápidamente los nodos disponibles sin tener que recorrer todo el grafo de nuevo buscando qué hacer[cite: 1].

## 7. BFS frente a Kahn
¿En qué se parecen y en qué se diferencian?
Ambos algoritmos se parecen en que utilizan una cola para organizar el trabajo[cite: 1]. La gran diferencia es su regla de entrada: en BFS metes un nodo a la cola con el simple hecho de "descubrirlo" una vez, mientras que Kahn es mucho más estricto y obliga al nodo a esperar afuera hasta que absolutamente todas sus dependencias hayan llegado a cero[cite: 1].

## 8. Invariantes
¿Qué propiedad debe cumplir todo nodo que está en la cola?
La regla sagrada es que todo nodo que logre entrar a la cola debe tener un grado de entrada actual de exactamente cero[cite: 1].

## 9. Ciclos
¿Cómo detecta Kahn que existe un ciclo?
Comprobando si le faltó trabajo por hacer[cite: 1]. Al finalizar el algoritmo, compara la cantidad de nodos que logró procesar y guardar en su orden contra la cantidad total de nodos en el grafo original; si los números no coinciden, es porque detectó un ciclo[cite: 1].

## 10. Órdenes múltiples
¿Por qué puede haber más de un orden topológico?
Porque en muchos momentos del proceso puedes tener varias tareas disponibles al mismo tiempo (todas con grado cero) y cualquiera que elijas primero generará un orden válido[cite: 1]. 

## 11. Validación
¿Cómo puede verificarse un orden sin ejecutar nuevamente Kahn?
Construyendo un diccionario con las posiciones de cada tarea en la lista final y revisando cada arista original \(u \to v\) para confirmar que la posición de \(u\) siempre sea menor (es decir, haya quedado antes) que la posición de \(v\)[cite: 1].

## 12. Duplicados
¿Por qué conviene eliminar dependencias repetidas?
Porque si a un nodo le cuentas la misma dependencia dos veces, su grado subirá a 2[cite: 1]. Cuando su requisito termine, el algoritmo solo le restará "1", dejándolo estancado para siempre con un grado fantasma de 1, bloqueando todo el proceso[cite: 1].

## 13. Nodos aislados
¿Cómo debe aparecer un nodo aislado en el resultado?
Debe aparecer en algún lugar del orden final[cite: 1]. Como inicia con cero aristas entrantes (y por lo tanto cero dependencias), entra rápidamente a la cola y se procesa[cite: 1].

## 14. Cola ligada
¿Podría utilizarse la ColaLigada de la Clase 17?
Sí, sin ningún problema[cite: 1]. Cualquier estructura que cumpla con la política básica de encolar, desencolar y reportar si está vacía, funcionará perfectamente para este algoritmo[cite: 1].

## 15. Heap
¿Cuándo convendría sustituir la cola por un heap?
Solo en el caso especial donde el problema nos exija que, además de cumplir las dependencias, siempre debamos elegir el nodo "menor" (por ejemplo, el de menor valor numérico o alfabético) entre todos los que estén disponibles en ese instante[cite: 1].

## 16. Complejidad
¿Por qué la complejidad es \(O(V+E)\)?
Porque las operaciones se suman, no se multiplican[cite: 1]. El bucle no reinicia búsquedas globales; simplemente inicializa y procesa cada nodo como máximo una vez, y revisa/reduce cada arista exactamente una vez[cite: 1].

## 17. Comparación
Compara BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn.
Cada uno domina un problema con una estructura clave:
* BFS usa una cola para encontrar el camino más corto sin pesos[cite: 1].
* 0-1 BFS usa una deque para manejar caminos con costos de cero[cite: 1].
* Dijkstra usa un heap para extraer siempre la distancia mínima[cite: 1].
* Kruskal usa Union-Find para conectar redes consultando componentes[cite: 1].
* Kahn usa una cola y un arreglo de grados para ordenar dependencias[cite: 1].

## 18. Cierre
¿Cuál es la operación dominante del ordenamiento topológico?
Procesar tareas sin requisitos (o elegir el nodo que ya tiene grado de entrada cero)[cite: 1].