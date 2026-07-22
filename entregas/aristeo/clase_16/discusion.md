# Disusion
## 1. Diferencia entre algoritmo correcto y función robusta

Un algoritmo correcto garantiza devolver el resultado óptimo bajo condiciones ideales y con entradas perfectas, una función robusta inspecciona activamente sus fronteras, tolera variaciones estructurales de los tipos de datos y gestiona las violaciones a sus condiciones con excepciones.

## 2. Razón de separar la normalización

1. **Mantenibilidad:** El código del algoritmo principal permanece limpio, legible y enfocado puramente en la optimización de caminos mínimos.
2. **Modularidad y Testeabilidad:** Permite auditar y verificar la robustez de las fronteras del grafo de forma independiente mediante pruebas unitarias dirigidas, sin necesidad de ejecutar el algoritmo completo.
3. **Optimización:** Garantiza que el grafo se procese y valide una sola vez antes de ingresar a las operaciones de prioridad del heap.

## 3. Mapping/Sequence frente a dict/list

La mayor ventaja es que al hacer cosas abstractas, ya que si se hace con diccionarios y listas se tienen que especificar màs cosas en el còdigo, y con mapping no.

## 4. TypeError frente a ValueError

ValueError es cuando usamos datos numericos que no corresponden al tipo de dato numerico que pide el còdigo, el Type es cuando nos equivocamos de tipo de dato.

## 5. Bool, NaN e infinito

Estos tres valores constituyen casos límite críticos en Python que requieren intercepción explícita debido a sus propiedades colaterales:
* **Bool:** Al ser una subclase nativa de `int`, valores como `True` burlan los filtros comunes de tipo numérico y se evalúan silenciosamente como `1.0`, corrompiendo la semántica del grafo.
* **NaN:** Carece de la propiedad de orden total; cualquier comparación lógica con `nan` (como `<` o `>`) retorna invariablemente `False`. De no filtrarse en la normalización, corrompe el orden interno del Min-Heap, rompiendo la correctitud de Dijkstra de forma silenciosa.
* **Infinito:** Es utilizado internamente por Dijkstra como la cota superior para denotar nodos temporalmente inalcanzables. Permitir que el usuario introduzca un peso infinito en la entrada genera ambigüedad semántica entre un camino costoso y la absoluta desconexión topológica.

## 6. Copia defensiva

Datos que agregados inicialmente sin necesidad de normalizarlos

## 7. Vecino implícito
Los vecinos implicitos son aquellos que están conectados con los demás de cierta forma pero que no se declara explicitamente.

## 8. Invariante de entradas obsoletas

El invariante de control frente a entradas obsoletas es  punto de partida desde el cual se va a hacer todo lo demás.

## 9. Responsabilidades de reconstrucción

La función de reconstrucción de caminos es normalizar los datos que se ingresan.

## 10. Matriz contrato–riesgo–prueba

Esta matriz es una herramienta que verifica que todo jale bien, buenas implementacioness, que normaliza y asì.

## 11. Complejidad de normalización y Dijkstra

La fase de normalización ocupa inspeccionar individualmente cada vértice y cada arista del grafo de entrada, creo que tiene una complejidad logaritmica

## 12. Operación dominante en BFS, Dijkstra, Kruskal y topológico

No existe un algoritmo que domine a los demás; en su lugar, cada arquitectura se define por la **operación dominante** que gobierna su estructura auxiliar de datos para resolver un problema específico del cierre topológico:
* **BFS:** Su operación dominante es la exploración estricta por niveles de vecindad inmediata, gobernada por una **Cola FIFO**.
* **Dijkstra:** Su operación dominante es la extracción sistemática del nodo con la menor distancia tentativa acumulada, gobernada por un **Min-Heap (Cola de Prioridad)**.
* **Kruskal:** Su operación dominante es el ordenamiento global de aristas y la fusión ágil de componentes conexas acíclicas, gobernada por una estructura **Union-Find (Conjuntos Disjuntos)**.
* **Ordenamiento Topológico:** Su operación dominante es la resolución secuencial de dependencias en Grafos Dirigidos Acíclicos (DAGs), gobernada por el control del **grado de entrada** de los vértices.