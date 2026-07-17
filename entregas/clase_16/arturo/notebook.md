# Arturo Prudencio Bonilla

## Pregunta inicial
**Ya entendemos la idea de Dijkstra. ¿Cómo se convierte en una implementación confiable, reutilizable y testeable?**
Se convierte en una implementación confiable, reutilizable y testeable cuando se basa en un sistema de promesas y contratos claros que definen qué acepta, qué devuelve, qué no modifica, cómo informa los errores y qué invariante sostiene su ciclo principal[cite: 1]. Esto requiere validar tipos, aplicar normalización, separar la reconstrucción del cálculo y crear pruebas que falsifiquen y protejan específicamente cada promesa[cite: 1].



## seccion 1
**¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?**
Aparecen las responsabilidades de decidir explícitamente cómo manejar las entradas (si se normalizan o rechazan anomalías), definir qué se acepta y qué se devuelve, asegurar que la función no modifique objetos recibidos, establecer cómo se informan los errores y proteger matemáticamente el invariante del ciclo algorítmico[cite: 1].



## seccion 2
**¿Por qué conviene leer firma y docstring antes que el while principal?**
Porque la firma y el docstring establecen el contrato (los tipos, retornos y excepciones)[cite: 1]. Leer esto antes nos permite entender qué promesas intenta proteger el código, en lugar de perdernos simulando variables y detalles línea por línea sin contexto[cite: 1].



## seccion 3
**¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?**
Aceptar `Mapping` y `Sequence` amplía la interfaz sin debilitarla, permitiendo al usuario pasar otras estructuras (como tuplas en lugar de listas) siempre que contengan pares clave-valor y mantengan la estructura de nodos `str` y aristas de dos elementos[cite: 1]. Exigir `dict` y `list` de forma estricta limitaría innecesariamente la flexibilidad de entrada de la función[cite: 1].



## seccion 4
**¿Qué dos problemas resuelve `_normalizar_grafo` antes de ejecutar Dijkstra?**
Resuelve la validación de la frontera (asegurándose de que los tipos y dominios sean correctos, ej. pesos finitos no negativos y nodos `str`) y construye una representación interna predecible mediante una copia defensiva[cite: 1]. Esto evita compartir listas mutables con la entrada original y reduce las condiciones a manejar dentro del bucle de relajación[cite: 1].



## seccion 5
**¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?**
Corresponde `TypeError` cuando el dato recibido no tiene la clase de representación esperada (por ejemplo, si el grafo no es un mapeo, o si el peso no es un valor numérico)[cite: 1]. Se usa `ValueError` cuando el tipo de dato es admisible, pero su valor viola las reglas lógicas del dominio (por ejemplo, un peso numérico pero negativo, o un valor `NaN`)[cite: 1].



## seccion 6
**¿Por qué True y NaN requieren comprobaciones específicas?**
`True` requiere comprobación específica porque en Python hereda de `int` y podría aceptarse erróneamente como un peso de 1, aunque lógicamente no sea una medida del dominio[cite: 1]. `NaN` requiere comprobación (mediante `math.isfinite`) porque, aunque es un `float`, rompe la intuición de las operaciones de comparación, haciendo que un heap pierda su capacidad de representar un orden válido de prioridades[cite: 1].



## seccion 7
**¿Qué fallo evita `resultado.setdefault(vecino, [])`?**
Evita un `KeyError` que ocurriría si un nodo que solo existe como destino dentro de una arista (pero que no es clave explícita del diccionario principal) se extrae del heap y el algoritmo intenta consultar su lista de adyacencia[cite: 1].



## seccion 8 
**¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?**
Devuelve un mapa de costos y un mapa de predecesores para separar el cálculo del algoritmo de la reconstrucción de un camino particular[cite: 1]. Esta separación conserva toda la información, evitando tener que repetir el algoritmo entero si el código llamador decide consultar destinos distintos[cite: 1].



## seccion 9
**¿Qué invariante establecen las comprensiones antes del while?**
Establecen que cada clave interna (nodo) existe en ambos mapas (distancias y predecesores), que `distancias[n]` contiene el menor costo descubierto hasta el momento (inicializado en infinito para todos menos el origen que inicia en 0.0), y que cada par insertado en el heap es una candidatura histórica[cite: 1].



## seccion 10
**¿Qué garantiza la comparación inmediatamente posterior a heappop?**
Garantiza que el ciclo procese exclusivamente candidaturas vigentes[cite: 1]. Si la distancia extraída del heap difiere de la registrada en la tabla de `distancias` para ese nodo, la tupla se considera una entrada obsoleta y se descarta con un `continue`, evitando procesarla sin tener que eliminarla del heap arbitrariamente[cite: 1].



## seccion 11
**¿Qué datos deben actualizarse juntos cuando una candidata mejora?**
Deben actualizarse de manera atómica tres componentes: registrar el nuevo costo en la tabla de distancias, registrar al nodo actual como el nuevo padre en la tabla de predecesores, e insertar la nueva prioridad (distancia y vecino) en el heap[cite: 1].



## seccion 12
**¿Qué diferencia hay entre destino inalcanzable y destino ausente?**
Un destino inalcanzable es un nodo válido que sí pertenece al grafo, pero cuya cadena de recorrido llega a `None` sin encontrar el origen (devuelve distancia infinita y una lista `[]`)[cite: 1]. Un destino ausente es aquel cuya clave no existe en el mapa de resultados (ni como nodo explícito ni implícito), lo que es un uso inválido que lanza un `KeyError`[cite: 1].



## seccion 13
**¿Qué responsabilidades delega camino_minimo?**
Delega la responsabilidad del cálculo de distancias y predecesores a la función `dijkstra`, y delega la secuencia lógica de formación de la ruta a la función `reconstruir_camino`[cite: 1]. De este modo actúa solo como coordinador sin duplicar código de relajación ni recorridos propios[cite: 1].



## seccion 14
**¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?**
Al probar únicamente el costo final, no se verifican promesas vitales como la no mutación de la entrada original, la inclusión adecuada de vecinos implícitos, el rechazo a violaciones del dominio o tipo (errores tipo ValueError o TypeError), la representación correcta de inalcanzables (`inf` y `[]`) ni la defensa efectiva frente a ciclos[cite: 1].



## seccion 15
**¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?**
De acuerdo con el texto de la auditoría, la implementación frágil:
1. No valida la estructura de grafo (acepta pesos negativos y tipos inválidos como booleanos)[cite: 1].
2. No incluye a los vecinos implícitos en las tablas de estado[cite: 1].
3. Procesa entradas obsoletas en el heap al omitir la condición de validación post-extracción y no rechaza orígenes ausentes[cite: 1].



## seccion 16
**¿Qué información mínima debe contener un reporte de fallo útil?**
Debe contener el comando que se utilizó, la entrada mínima reproducible, el resultado esperado según el contrato, el resultado observado al ejecutarse y la ubicación probable del fallo (la primera línea donde el estado deja de cumplir el contrato)[cite: 1].



## seccion 17
**¿Qué hace que un comentario de revisión sea accionable y verificable?**
Se vuelve accionable y verificable cuando el revisor separa comprensión, evidencia y recomendación estructurada[cite: 1]. Es decir, cuando identifica explícitamente el contrato roto, proporciona una entrada o prueba de evidencia, describe el impacto y propone el cambio más pequeño posible que restaura la corrección[cite: 1].



## seccion 18
**¿La normalización cambia la complejidad asintótica de Dijkstra?**
No, no la cambia[cite: 1]. La normalización es una fase de procesamiento lineal que recorre nodos y aristas tomando un tiempo `O(V+E)`, lo cual no logra dominar asintóticamente al término logarítmico principal de Dijkstra que es `O((V+E) log V)`[cite: 1].



## seccion 19
**¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?**
- **BFS:** Cola FIFO (para procesar nodos estrictamente por orden de descubrimiento)[cite: 1].
- **Dijkstra:** Min-heap (para extraer siempre el nodo con la menor distancia tentativa)[cite: 1].
- **Kruskal:** Ordenamiento de listas + Conjuntos disjuntos / Union-Find (para unir componentes asegurando que no se creen ciclos)[cite: 1].
- **Orden Topológico:** Arreglo de grados + Cola (para ir retirando los nodos en cuanto su grado de entrada llega a cero)[cite: 1].



## seccion 20
**¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?**
La cadena sistemática de: Contrato → Invariante → Riesgo → Prueba[cite: 1]. Esta secuencia obliga a pensar qué se promete (contrato), qué debe ser cierto siempre (invariante), qué ejemplo lo rompería (riesgo) y finalmente cómo se automatiza esa comprobación (prueba), convirtiendo el código en software que puede falsarse y mantenerse de forma predecible[cite: 1].

> **Ticket de salida:**
> - **Contrato:** Los pesos del grafo deben ser finitos.
> - **Riesgo:** Un peso `math.nan` rompería la capacidad de comparación en el min-heap y generaría falsos caminos de costo menor.
> - **Prueba mínima:** Pasar `{"A": [("B", math.nan)]}` y asertar que levanta un `ValueError` específico.