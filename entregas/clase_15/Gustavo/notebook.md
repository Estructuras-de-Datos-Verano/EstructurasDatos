# Respuestas y recorrido manual (Clase 15: Dijkstra)
# Gustavo Torres 

## Parte 1 — Recorrido manual de la Práctica 15

A continuación, la traza completa del algoritmo Dijkstra para la red conductora desde el origen A hasta E.

| Extracción | Arista | Candidata | Comparación | Decisión | Heap después |
| --- | --- | ---: | --- | --- | --- |
| `(0,A)` | `A→B` | 4 | 4 < ∞ | actualizar | `(4,B)` |
| `(0,A)` | `A→C` | 1 | 1 < ∞ | actualizar | `(1,C), (4,B)` |
| `(1,C)` | `C→B` | 3 | 3 < 4 | actualizar | `(3,B), (4,B)` |
| `(1,C)` | `C→D` | 6 | 6 < ∞ | actualizar | `(3,B), (4,B), (6,D)` |
| `(3,B)` | `B→D` | 4 | 4 < 6 | actualizar | `(4,D), (4,B), (6,D)` |
| `(3,B)` | `B→E` | 10 | 10 < ∞ | actualizar | `(4,D), (4,B), (6,D), (10,E)` |
| `(4,D)` | `D→E` | 7 | 7 < 10 | actualizar | `(4,B), (6,D), (7,E), (10,E)` |
| `(4,B)` | — | — | 4 ≠ 3 | ignorar (obsoleta)| `(6,D), (7,E), (10,E)` |
| `(6,D)` | — | — | 6 ≠ 4 | ignorar (obsoleta)| `(7,E), (10,E)` |
| `(7,E)` | — | — | — | sin vecinos | `(10,E)` |
| `(10,E)`| — | — | 10 ≠ 7 | ignorar (obsoleta)| `vacío` |

* **Entradas obsoletas detectadas:** `(4,B)`, `(6,D)` y `(10,E)`.
* **Reconstrucción del camino hacia E:** E ← D ← B ← C ← A. Invertido es **A → C → B → D → E** con un costo total de **7**.

---

## Respuestas a las preguntas del notebook

**Pregunta inicial:** ¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?
**R:** Evaluando el costo total acumulado de cada ruta y procesando siempre la candidatura que tenga la menor distancia pendiente usando una cola de prioridad.

**Sección 1:**
* ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?
  **R:** La que compara niveles (BFS) elegiría A → D (costo 10, nivel 1). Si optimizamos costo total, deberíamos elegir A → B → D (costo 2, nivel 2).
* ¿Por qué contar aristas ya no es suficiente en un grafo ponderado?
  **R:** Porque una ruta con más aristas puede sumar un costo total inferior a una ruta directa o con menos aristas que tenga pesos muy altos.

**Sección 2:**
* ¿En qué condición BFS sí garantiza caminos de costo mínimo?
  **R:** Solamente cuando el grafo no es ponderado, o cuando todas sus aristas tienen exactamente el mismo costo.

**Sección 3:**
* Enumera al menos dos caminos de A a E y suma sus pesos.
  **R:** 1) A → B → E (costo: 4 + 7 = 11). 2) A → C → D → E (costo: 1 + 5 + 3 = 9).
* ¿Qué representan nodos, aristas y pesos en esta red?
  **R:** Los nodos representan ciudades, las aristas representan carreteras disponibles y los pesos representan el tiempo de viaje.

**Sección 4:**
* ¿Qué significa infinito en la tabla de distancias?
  **R:** Significa que, hasta ese momento, el algoritmo aún no ha descubierto ningún camino válido para llegar a ese nodo desde el origen.

**Sección 5:**
* ¿Qué tres valores comparamos al relajar una arista?
  **R:** Comparamos la "candidata" (calculada sumando la **distancia actual del nodo de origen** + el **peso de la arista**) contra la **distancia que ya conocíamos del nodo destino**.

**Sección 6:**
* ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
  **R:** Porque eliminar un elemento arbitrario del medio de un Heap es una operación ineficiente y compleja. Es mejor aplicar "eliminación perezosa" e ignorarla cuando sea extraída si la distancia no coincide.

**Sección 7:**
* ¿Qué componente del par funciona como prioridad y cuál como elemento?
  **R:** En el par `(distancia, nodo)`, la `distancia` funciona como la prioridad (ordenando el Heap) y el `nodo` es el elemento almacenado.

**Sección 8:**
* ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
  **R:** Encuentra los caminos mínimos desde un nodo origen hacia todos los demás nodos alcanzables. La restricción vital es que los pesos deben ser **no negativos**.

**Sección 9:**
* Subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.
  **R:** 1) *insertar (0, origen) en la cola de prioridad*, 2) *extraer (distancia_extraida, actual)*, 3) *insertar (candidata, vecino)*.
* ¿En qué momento se ignora una entrada obsoleta?
  **R:** Inmediatamente después de extraerla del heap, comprobando si su valor extraído no coincide con el guardado en la tabla de distancias actual.

**Sección 10:**
* ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
  **R:** Primero se extrae `(0,A)`, luego `(1,B)` y finalmente `(3,C)`.

**Sección 11:**
* ¿Cuáles son las distancias finales desde A en la red conductora?
  **R:** A = 0, B = 3, C = 1, D = 4, E = 7.

**Sección 12:**
* ¿Por qué recorremos predecesores desde el destino y después invertimos?
  **R:** Porque los predecesores registran de dónde "llegamos" (hacia atrás). Al leerlos armamos el camino desde el destino al origen, y la inversión corrige el orden cronológico del viaje.

**Sección 13:**
* En “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.
  **R:** Será descartada/ignorada, ya que en ese punto la distancia real y optimizada hacia B será menor a 10.
* ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
  **R:** La red ponderada gráfica, la tabla de distancias/predecesores y el min-heap de candidaturas.

**Sección 14:**
* ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
  **R:** `dijkstra` calcula las distancias mínimas y registra predecesores. `reconstruir_camino` genera la lista ordenada del camino leyendo el mapa anterior. `camino_minimo` coordina a ambas para devolver costo y ruta en un solo paso.

**Sección 15:**
* ¿De dónde proviene el factor logarítmico de Dijkstra con heap?
  **R:** Proviene de las operaciones de inserción y extracción del mínimo (`heappush` y `heappop`) en la estructura del min-heap.

**Sección 16:**
* ¿Cuál es el costo y camino mínimo de A a E en la red conductora?
  **R:** El costo mínimo es **7**, y el camino es **A → C → B → D → E**. Las alternativas (como A→C→D→E con costo 9 o A→B→E con costo 11) demuestran que pasar por más nodos puede ser globalmente más barato.

**Sección 17:**
* ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
  **R:** Porque Dijkstra asume que una vez procesada la distancia menor vigente de la cola, es definitiva ya que sumar costos siempre incrementará o mantendrá el total. Una arista negativa invalidaría rutas que ya se consideraban terminadas.

**Sección 18:**
* ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?
  **R:** Verificaría que la lista inicia en el origen correcto, termina en el destino solicitado, que los tramos existen en el grafo y que la lista devuelta está vacía si el destino es inalcanzable.
* ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?
  **R:** Un caso donde una misma ciudad reciba una ruta más cara en aristas pero más barata en costo después de ya haber encolado una candidata previa.

**Sección 19:**
* ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
  **R:** La necesidad de procesar continuamente la "menor distancia o costo acumulado pendiente" priorizando nodos basados en su costo desde un origen.

**Sección 20:**
* ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
  **R:** Queremos suma mínima → usamos distancias tentativas → relajamos aristas para mejorar → necesitamos procesar el menor pendiente → lo resolvemos con un Min-Heap.