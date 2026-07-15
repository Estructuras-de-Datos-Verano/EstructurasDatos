# Discusión - Práctica 16

**1. Diferencia entre algoritmo correcto y función robusta.**
Un algoritmo correcto es la prueba matemática de que la lógica funciona (por ejemplo, demostrar que la estrategia greedy de Dijkstra minimiza el camino). Una función robusta es el software que encapsula esa idea para que sobreviva en el mundo real, manejando entradas incorrectas, protegiendo las referencias de memoria y garantizando que las fallas sean controladas.

**2. Razón de separar normalización.**
Separar la normalización me permite limpiar y establecer el dominio total de entrada antes de operar. Así, el núcleo algorítmico (el bucle de relajación) no se contamina con validaciones condicionales y asume un estado inicial lógicamente coherente, haciéndolo mucho más predecible.

**3. Mapping/Sequence frente a dict/list.**
Al usar `Mapping` y `Sequence`, amplío la interfaz de la función. Permito que el usuario me inyecte estructuras inmutables (como tuplas) u otros mapeos personalizados sin forzar la instanciación estricta de las clases base `dict` y `list` nativas de Python, ganando flexibilidad sin perder seguridad de tipos.

**4. TypeError frente a ValueError.**
El `TypeError` lo lanzo cuando el objeto recibido no pertenece a la clase o conjunto esperado (ej. recibir un string cuando esperaba un número). El `ValueError` aplica cuando el tipo es el correcto, pero el valor numérico viola las restricciones del dominio del problema (como un peso negativo o no finito).

**5. Bool, NaN e infinito.**
En Python, la clase `bool` hereda de `int`, lo que introduciría falsos positivos numéricos de $1$ o $0$. Por su parte, `NaN` es técnicamente un flotante pero rompe la relación de orden estricto (haciendo que el min-heap falle internamente). Finalmente, el infinito no es un peso válido para una arista real de entrada, sino un marcador de estado interno para indicar la ausencia temporal de una ruta.

**6. Copia defensiva.**
Si no hago una copia defensiva profunda, al agregar vecinos implícitos o mutar los datos en mi entorno, estaría alterando las listas en la memoria del programa de quien me llamó. La copia defensiva aísla mi función y evita efectos secundarios no deseados.

**7. Vecino implícito.**
Es un vértice que pertenece al grafo por ser destino de una arista dirigida, pero que no fue explícitamente declarado como una clave en el mapeo inicial. Si no garantizo su existencia en mi diccionario normalizado, el algoritmo lanzará un `KeyError` al intentar consultarlo.

**8. Invariante de entradas obsoletas.**
En un heap, buscar y borrar un elemento que ha mejorado su costo tomaría tiempo lineal. En su lugar, lo dejamos coexistir. Al hacer `heappop`, comparo si la distancia de la tupla coincide con la menor registrada; si es mayor, la descarto como entrada obsoleta en $O(1)$.

**9. Responsabilidades de reconstrucción.**
Su única responsabilidad es mapear la cadena hacia atrás utilizando el diccionario de predecesores ya calculado. No resuelve caminos mínimos ni evalúa pesos; solo gestiona la detección de ciclos corruptos y determina si un destino es inalcanzable.

**10. Matriz contrato–riesgo–prueba.**
Es un marco de confiabilidad. Para cada promesa de la función (el contrato), defino la vulnerabilidad que lo rompería (el riesgo) y diseño una ejecución automatizada mínima y reproducible (la prueba) que asegure el comportamiento deseado, como lanzar una excepción específica.

**11. Complejidad de normalización y Dijkstra.**
Normalizar exige recorrer todos los vértices y aristas una sola vez, lo que toma $O(V+E)$. Dado que la complejidad del núcleo de Dijkstra usando un min-heap domina con $O((V+E) \log V)$, la validación lineal de la normalización es absorbida asintóticamente y no degrada el rendimiento.

**12. Operación dominante en BFS, Dijkstra, Kruskal y topológico.**
* **BFS:** Procesar nodos en estricto orden de descubrimiento (utiliza una Cola FIFO).
* **Dijkstra:** Extraer iterativamente la distancia tentativa más corta (utiliza un Min-Heap).
* **Kruskal:** Evaluar aristas y unir conjuntos disjuntos sin crear ciclos (utiliza ordenamiento y Union-Find).
* **Topológico:** Retirar vértices cuyo grado de dependencias de entrada sea exactamente cero (utiliza tabla de grados y una Cola).