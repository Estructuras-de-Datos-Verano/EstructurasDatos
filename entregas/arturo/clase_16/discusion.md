## Diferencia entre algoritmo correcto y función robusta
Un algoritmo correcto asume teóricamente que el grafo está bien formado y todos los pesos son válidos[cite: 1]. Una función robusta, en cambio, define un contrato reutilizable explícito: establece las condiciones para que su razonamiento sea válido decidiendo qué acepta, qué devuelve, qué no modifica y cómo informa formalmente los errores[cite: 1].

## Razón de separar normalización
La separación cumple dos objetivos: validar las fronteras de entrada y construir una copia interna predecible[cite: 1]. Esto limpia y simplifica el núcleo del algoritmo, dejando un bucle de Dijkstra más pequeño y libre de condiciones anidadas[cite: 1].

## Mapping/Sequence frente a dict/list
Utilizar abstracciones como `Mapping` y `Sequence` amplía la flexibilidad de la interfaz sin debilitar su rigor lógico[cite: 1]. Permite que los usuarios alimenten el algoritmo con tuplas y otras estructuras iterables compatibles con pares clave-valor, sin forzarlos a usar estrictamente diccionarios y listas[cite: 1].

## TypeError frente a ValueError
Se emplea `TypeError` para datos que no coinciden con la representación esperada de los tipos (por ejemplo, proporcionar un *string* como peso en lugar de un número)[cite: 1]. Por el contrario, se emplea `ValueError` cuando el tipo de dato es admisible, pero su valor específico viola las leyes matemáticas del dominio (como un peso negativo)[cite: 1].

## Bool, NaN e infinito
En Python, el tipo `bool` hereda de `int`, por lo que `True` requiere un rechazo preventivo para no ser asimilado como el número $1$[cite: 1]. El tipo `NaN`, aunque computacionalmente es un flotante, debe validarse y rechazarse porque rompe las operaciones de comparación lógico-matemáticas en el *min-heap*[cite: 1]. Finalmente, el infinito debe rechazarse en la entrada porque pertenece estrictamente a la representación del estado interno (indicando que aún no se conoce ruta)[cite: 1].

## Copia defensiva
Es el mecanismo utilizado para evitar compartir el manejo de estructuras de memoria (como listas) entre la entrada de la función y su procesamiento[cite: 1]. Garantiza que los ajustes estructurales lógicos del algoritmo (como añadir un vecino faltante) no modifiquen colateralmente el diccionario proveído por el usuario[cite: 1].

## Vecino implícito
Aquel vértice que existe físicamente como destino de una arista pero que no posee sus propias aristas de salida, por lo que no existe como clave explícita en la estructura de entrada[cite: 1]. Se debe agregar un registro vacío para él, previniendo excepciones como un `KeyError` al momento de ser inspeccionado por el algoritmo[cite: 1].

## Invariante de entradas obsoletas
Al encontrar una ruta mejor en lugar de buscar y eliminar el dato previo del *heap*, se inserta uno nuevo[cite: 1]. El invariante se mantiene utilizando una guarda o *guard clause* inmediatamente tras la extracción: si el peso sacado del *heap* no coincide con el mejor peso registrado en la tabla, se considera obsoleto y se descarta su evaluación[cite: 1].

## Responsabilidades de reconstrucción
Esta fase está desacoplada del cálculo[cite: 1]. Su única responsabilidad es procesar un mapa de predecesores para recrear la ruta hacia un destino particular o devolver una lista vacía si la ruta lógicamente no es alcanzable[cite: 1]. También es responsable de detectar errores, como pedir destinos ajenos al registro[cite: 1].

## Matriz contrato–riesgo–prueba
Es una técnica de auditoría donde las pruebas no agrupan ejemplos al azar[cite: 1]. Cada *test* está quirúrgicamente apuntado a verificar una promesa particular del contrato mediante una entrada mínima y controlada, atada a una aserción o intercepción específica de excepción[cite: 1].

## Complejidad de normalización y Dijkstra
La fase normalizadora cuesta linealmente $\mathcal{O}(V+E)$ y recorre las aristas una vez[cite: 1]. Esta tarea no domina la complejidad matemática del algoritmo, por lo que implementar las medidas de robustez conserva íntegramente la eficiencia de Dijkstra en un orden algorítmico global de $\mathcal{O}((V+E) \log V)$[cite: 1].

## Operación dominante en BFS, Dijkstra, Kruskal y topológico
*   **BFS:** Procesar nodos bajo un estricto orden cronológico de descubrimiento, apalancado en una estructura de cola FIFO[cite: 1].
*   **Dijkstra:** Extraer secuencialmente la menor distancia no definitiva priorizando el costo global, apalancado en un *min-heap*[cite: 1].
*   **Kruskal:** Unir múltiples componentes previniendo la creación de ciclos, basado en ordenar conjuntos y utilizar *Union-Find*[cite: 1].
*   **Topológico:** Retirar de la estructura solo los vértices cuyo grado de dependencia bloqueante llegue a cero, combinando una tabla de grados y una cola[cite: 1].