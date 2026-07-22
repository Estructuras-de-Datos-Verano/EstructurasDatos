# Notebook Aristeo

## Pregunta inicial
### ¿Cómo se convierte en una implementación confiable, reutilizable y testeable?
A través del diseño guiado por contratos, el aislamiento estricto de responsabilidades y el manejo preventivo de fallos.

## 1. De algoritmo correcto a software confiable
### ¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?
Validar los tipos y el dominio de los datos de entrada, asegurar que la función no genere efectos secundarios indeseados en las estructuras originales y asegurarse de que cualquier violación a los contratos del algoritmo sea notificada mediante excepciones claras.

## 2. Un orden profesional de lectura
### ¿Por qué conviene leer firma y docstring antes que el while principal?
Porque la firma y el docstring establecen el un contrato del componente, definen qué tipos de datos acepta, cuáles son sus precondiciones, qué promesas de salida ofrece y qué excepciones levanta.

## 3. Tipos como decisiones de diseño
### ¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?
Mapping acepta cualquier estrutura que tenga elementos relacionados de tipo llave-valor y dict solo acepta diccionarios.

## 4. Normalización y copia defensiva
### ¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?
- Resuelve el problema en que si no viene una arista explícita en el diccionario, el Dijkstra saltaría error.
- Verifica que las fronteras del los inputs estén correctas, detecta errores.

## 5. TypeError y ValueError cuentan historias distintas
### ¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?
* **TypeError:** Se lanza cuando la naturaleza o clase del dato es incorrecta para el dominio del problema. Por ejemplo, pasar una estructura que no sea un `Mapping`, usar enteros o booleanos en lugar de cadenas para los nombres de los nodos, o introducir datos no numéricos (como strings o `None`) en el lugar de los pesos.
* **ValueError:** Se lanza cuando el tipo de dato es técnicamente correcto (un `int` o `float`), pero su magnitud o propiedad aritmética viola las restricciones matemáticas del algoritmo. Por ejemplo, proveer pesos negativos, o valores no reales como `NaN` o `infinito`.


## 6. Bool, NaN e infinito
### ¿Por qué True y NaN requieren comprobaciones específicas?
* **True (y False):** En Python, la clase `bool` es históricamente una subclase de `int` (`isinstance(True, int)` evalúa como True). Si no se intercepta explícitamente, un valor booleano será aceptado erróneamente como un peso numérico válido (con valor de `1.0`).
* **NaN:** Rompe la consistencia lógica de ordenamiento del Min-Heap (`heapq`). Como cualquier operación de comparación con `math.nan` resulta siempre en `False`, su presencia corrompe el árbol de prioridades de forma silenciosa, impidiendo que el heap devuelva los elementos en el orden óptimo.

## 7. Vecinos implícitos y representación total
### ¿Qué fallo evita resultado.setdefault(vecino, [])?
Que no se detecten aristas implícitas en el grafo.

## 8. El contrato de dijkstra
### ¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?
Porque dijkstra no busca cuál es el camino mínimo para llegar de un lugar a otro, sino mappear el grafo para saber todos los caminos y que otra función pueda encontrar el camino mínimo para origen y destino. 

## 9. Estado inicial y tablas totales
### ¿Qué invariante establecen las comprensiones antes del while?
Que todos los nodos tengan una distancia infinita, entonces todavía no han sido analizadas y que todos los nodos tengas predecesores None.

## 10. El guard clause de entradas obsoletas
### ¿Qué garantiza la comparación inmediatamente posterior a heappop?
Nos garantiza el poder saber si el camino en donde estamos cambia en algo o es obsoleto.

## 11. Relajación y actualización atómica
### ¿Qué datos deben actualizarse juntos cuando una candidata mejora?
Cuando se descubre una ruta más corta hacia un vecino, se debe ejecutar una actualización en bloque e inseparable de tres elementos:
1. Reemplazar la distancia óptima en la tabla de control (distancias[vecino]).
2. Actualizar el nodo de procedencia en la tabla de rutas (predecesores[vecino]).
3. Insertar el nuevo par ordenado (candidata, vecino) en la cola de prioridad (Min-Heap).
Esta simultaneidad mantiene la coherencia absoluta entre el estado de las tablas de decisión y la cola de exploración.

## 12. Reconstruir es otro problema
### ¿Qué diferencia hay entre destino inalcanzable y destino ausente?
* **Destino Inalcanzable:** El nodo existe legítimamente dentro del grafo mapeado, pero no existe ninguna secuencia de aristas que conecte algebraicamente al origen con él. Su distancia final permanece en `math.inf` y su camino se reporta como una secuencia vacía `[]`.
* **Destino Ausente:** El nodo consultado directamente no forma parte del universo del grafo (no se encuentra en las claves ni en las aristas normalizadas). Es un fallo de frontera que viola las precondiciones y debe provocar inmediatamente un error de clave (KeyError).

## 13. Coordinación sin duplicación
### ¿Qué responsabilidades delega camino_minimo?
No tiene, creo

## 14. Del contrato a una matriz de pruebas
### ¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?
No verifica el cumplimiento de las restricciones de tipos y dominios, como rechazar strings o booleanos en pesos mediante `TypeError` o capturar valores negativos con `ValueError`.

| Contrato | Entrada mínima | Observado (en código frágil) | Esperado (en código robusto) | Test propuesto |
| --- | --- | --- | --- | --- |
| **Peso no negativo** | `grafo = {"A": [("B", -5)]}`<br>`origen = "A"` | El algoritmo procesa el peso negativo, arriesgando ciclos infinitos o distancias erróneas. | Lanza un `ValueError` con el mensaje exacto `"no negativos"`. | `test_rechaza_peso_negativo` |
| **Vecino implícito** | `grafo = {"A": [("B", 2)]}` *(B no es clave)*<br>`origen = "A"` | Lanza un `KeyError: 'B'` dentro del bucle de relajación al intentar expandir el nodo "B". | Se ejecuta con éxito. El nodo "B" se inicializa en las tablas y se calcula su distancia de `2.0`. | `test_incluye_vecino_que_no_es_clave` |
| **Origen válido** | `grafo = {"A": []}`<br>`origen = "X"` | Rompe el flujo de forma desordenada o lanza un `KeyError` tardío durante la inicialización. | Lanza un `KeyError` preventivo con un mensaje claro referente al nodo `"origen"`. | `test_rechaza_origen_inexistente` |
| **Entrada obsoleta** | `grafo = {"A": [("B", 10), ("C", 1)],`<br>`"C": [("B", 1)], "B": []}` | Extrae y procesa el nodo "B" múltiples veces del heap, desperdiciando ciclos de CPU. | La cláusula de salvaguarda intercepta la entrada obsoleta y la descarta mediante un `continue`. | `test_entrada_obsoleta_heap` |
| **Representación** | `grafo = {"A": [("B", float("nan"))]}`<br>`origen = "A"` | El heap se corrompe silenciosamente debido a que las comparaciones lógicas con `NaN` fallan. | Lanza un `ValueError` descriptivo que exige que todos los pesos sean números `"finitos"`. | `test_rechaza_peso_no_finito` |

## 15. Auditoría de una implementación frágil
### ¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?
1. **Ausencia de Normalización y Fallo de Vecinos Implícitos:** No realiza copias de seguridad de las adyacencias ni agrega los nodos sumideros como claves vacías, provocando un colapso por `KeyError` si un destino no es explícitamente una clave del diccionario.
2. **Falta de Validación de Fronteras Numéricas:** No inspecciona los pesos de las aristas, lo que permite la libre introducción de costos negativos y valores `NaN` o `infinito` que corrompen la cola de prioridad de forma silenciosa.
3. **Omisión del Filtro de Invariante de Heap:** No incluye la instrucción de control post-extracción para descartar de forma perezosa los nodos repetidos con distancias obsoletas, penalizando severamente el rendimiento asintótico del algoritmo.

## 16. Clínica de depuración
### ¿Qué información mínima debe contener un reporte de fallo útil?
Comando, entrada, esperado, observado y error.

## 17. Revisión profesional de código
### ¿Qué hace que un comentario de revisión sea accionable y verificable?
Que describa errores, fortalezas, acciones y cambios, así como el como afectan.

## 18. Complejidad sin perder robustez
### ¿La normalización cambia la complejidad asintótica de Dijkstra?
Se sigue acercando a una complejidad logaritmica.

## 19. Cuatro algoritmos, cuatro operaciones dominantes
### ¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?
* **BFS (Búsqueda en Anchura):** Exploración por niveles estrictos de vecindad -> **Cola FIFO** (`collections.deque`).
* **Dijkstra:** Extracción sistemática del nodo con la menor distancia tentativa acumulada -> **Cola de Prioridad / Min-Heap** (heapq).
* **Kruskal:** Ordenamiento global de costos e integración ágil de componentes conexas sin ciclos -> **Estructura de Conjuntos Disjuntos** (Union-Find).
* **Ordenamiento Topológico:** Identificación y remoción de nodos con grado de dependencia cero -> **Diccionario/Arreglo de grados de entrada** + **Cola de procesamiento**.

## 20. Cierre
### ¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?
Contrato -> Riesgo -> Prueba -> Implementación 
