# Respuestas a la Clase 16: Implementación robusta de Dijkstra - Gustavo Torres
## Pregunta inicial
**¿Cómo se convierte en una implementación confiable, reutilizable y testeable?**
Para que una idea matemática abstracta se convierta en software confiable, necesito establecer contratos estrictos desde el inicio. Debo validar los dominios de entrada (manejando nodos desconectados o pesos inválidos), hacer copias defensivas para no mutar los datos originales y aislar las responsabilidades (cálculo vs. reconstrucción) para poder testear cada parte de forma independiente.

## 1. De algoritmo correcto a software confiable
**¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?**
Al pasar de la abstracción a una herramienta que usaré en mis scripts, adquiero la responsabilidad de validar las fronteras de los datos, manejar excepciones de manera estructurada, proteger la información original y separar la lógica de cálculo del ruteo. 

## 2. Un orden profesional de lectura
**¿Por qué conviene leer firma y docstring antes que el while principal?**
Porque me da el "contrato" de la función. Es como definir el dominio y el codominio antes de evaluar una función matemática; si no entiendo qué tipos de datos entran y qué promesas de salida hay, analizar el bucle `while` línea por línea carece de sentido lógico.

## 3. Tipos como decisiones de diseño
**¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?**
Usar `Mapping` y `Sequence` amplía la flexibilidad para quien consuma la función. Permite que me pasen estructuras inmutables (como tuplas) u otros mapeos personalizados sin forzarlos a usar estrictamente las clases concretas `dict` y `list` de Python.

## 4. Normalización y copia defensiva
**¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?**
Primero, actúa como una aduana que valida el dominio (asegurando que los pesos y nodos sean correctos). Segundo, crea una copia defensiva y uniforme, evitando que cualquier modificación interna altere las variables en el entorno de quien llamó a la función.

## 5. TypeError y ValueError cuentan historias distintas
**¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?**
Uso `TypeError` cuando la estructura o la clase del dato es incorrecta (por ejemplo, si me pasan un string `"3"` en vez de un número). Uso `ValueError` cuando el tipo de dato es numéricamente correcto, pero su valor viola el dominio lógico del problema (como un peso negativo o un valor infinito).

## 6. Bool, NaN e infinito
**¿Por qué True y NaN requieren comprobaciones específicas?**
Porque por diseño en Python, `True` hereda de `int` y vale `1`, lo que introduciría datos basura si no lo filtro antes. Por otro lado, `NaN` es técnicamente un `float`, pero rompe por completo el algoritmo porque cualquier comparación lógica con él devuelve falso, arruinando el ordenamiento del min-heap.

## 7. Vecinos implícitos y representación total
**¿Qué fallo evita resultado.setdefault(vecino, [])?**
Evita un `KeyError` inminente. Si un nodo existe únicamente como destino en una arista (un vecino implícito) y no garantizo que exista como llave en mi diccionario interno, el algoritmo fallará más adelante al intentar consultar su distancia o sus propias conexiones.

## 8. El contrato de dijkstra
**¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?**
Porque calcular y reconstruir son problemas distintos. Devolver los diccionarios de costos y predecesores me permite conservar el estado completo del cálculo, dándome la libertad de reconstruir múltiples caminos hacia distintos destinos sin repetir el costo computacional del algoritmo.

## 9. Estado inicial y tablas totales
**¿Qué invariante establecen las comprensiones antes del while?**
Garantizan que el dominio interno es total: absolutamente todos los nodos normalizados existen en los diccionarios. Además, aseguran que la distancia inicial al origen es $0$, la del resto es infinita, y que el heap arranca exclusivamente con la candidatura del origen.

## 10. El guard clause de entradas obsoletas
**¿Qué garantiza la comparación inmediatamente posterior a heappop?**
Garantiza que solo trabaje con la información más óptima vigente. Al comparar la distancia extraída con la actual en mi diccionario, detecto y descarto en $O(1)$ las candidaturas obsoletas que se quedaron atrapadas en el heap por una relajación previa.

## 11. Relajación y actualización atómica
**¿Qué datos deben actualizarse juntos cuando una candidata mejora?**
La actualización debe ser una operación atómica de tres pasos: registrar el nuevo costo mínimo en el diccionario de distancias, registrar el nodo actual en el diccionario de predecesores, y empujar (push) la nueva tupla de prioridad al heap.

## 12. Reconstruir es otro problema
**¿Qué diferencia hay entre destino inalcanzable y destino ausente?**
Un destino inalcanzable es un nodo válido dentro del grafo pero desconectado del origen, por lo que su costo es infinito y devuelve una lista vacía `[]`. Un destino ausente es un nodo que ni siquiera existe en el mapeo inicial, lo cual es una violación de contrato y levanta un `KeyError`.

## 13. Coordinación sin duplicación
**¿Qué responsabilidades delega camino_minimo?**
Funciona como un orquestador. Delega la carga computacional pesada (relajación y ruteo) a la función `dijkstra`, y delega la interpretación lógica de la ruta a `reconstruir_camino`. No duplica lógica algorítmica.

## 14. Del contrato a una matriz de pruebas
**¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?**
La corrección de la ruta en sí misma. Probar solo el número final no me asegura que la secuencia lógica de predecesores construya un camino real y sin ciclos hacia ese destino.

## 15. Auditoría de una implementación frágil
**¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?**
1. Permite cálculos con pesos negativos sin levantar un `ValueError`. 
2. Falla catastróficamente con un `KeyError` si se encuentra con un vecino implícito. 
3. Desperdicia ciclos procesando entradas obsoletas del heap porque carece de un guard clause tras el `heappop`.

## 16. Clínica de depuración
**¿Qué información mínima debe contener un reporte de fallo útil?**
Debe ser accionable: contener el contrato esperado, la entrada mínima necesaria para reproducir el fallo, el resultado observado frente al deseado, y la prueba unitaria automatizada que localiza el problema.

## 17. Revisión profesional de código
**¿Qué hace que un comentario de revisión sea accionable y verificable?**
Que aísle el comportamiento erróneo aportando evidencia. Debe indicar qué promesa del contrato se rompió, proporcionar un test que falle de manera reproducible y sugerir el cambio lógico específico.

## 18. Complejidad sin perder robustez
**¿La normalización cambia la complejidad asintótica de Dijkstra?**
No. La normalización tiene un costo lineal de $O(V+E)$, el cual es absorbido asintóticamente por la operación dominante de relajación con el heap en Dijkstra, que se mantiene en $O((V+E) \log V)$.

## 19. Cuatro algoritmos, cuatro operaciones dominantes
**¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?**
* **BFS:** Cola FIFO (para respetar el orden de descubrimiento).
* **Dijkstra:** Min-heap (para priorizar la ruta tentativa más barata).
* **Kruskal:** Ordenamiento y conjuntos disjuntos (para agrupar sin formar ciclos).
* **Topológico:** Cola combinada con conteo de grados de entrada (para respetar estrictamente las dependencias previas).

## 20. Cierre
**¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?**
El flujo va desde entender las promesas en el contrato y validar las fronteras de los tipos/dominios $\rightarrow$ establecer un estado seguro $\rightarrow$ mantener el invariante dentro del bucle manejando los riesgos algorítmicos $\rightarrow$ demostrarlo todo con un sistema de pruebas riguroso.