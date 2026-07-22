# Discusión técnica — Clase 20

Nombre: Arturo Prudencio Bonilla

## Escenario 1

- **Problema y objetivo:** Movilidad urbana (versión A3), encontrar la ruta más rápida entre dos puntos en una ciudad El objetivo es un **camino mínimo**
- **Dirección y pesos:** Grafo dirigido (calles de un solo sentido) con pesos generales no negativos (tiempo en minutos)
- **Operación dominante:** Consultar y extraer continuamente la prioridad extrema (menor distancia tentativa)
- **Estructura y algoritmo:** Heap y algoritmo de Dijkstra
- **Contrato:** Requiere estrictamente pesos no negativos para garantizar que una distancia extraída no mejore en el futuro
- **Alternativa descartada:** BFS, porque minimiza el número de aristas asumiendo costo uniforme, ignorando la variabilidad de los tiempos en cada calle
- **Módulo previo reutilizado:** `camino_minimo` del módulo de la Clase 16 (Dijkstra robusto).
- **Adaptación de entrada/salida:** Se debe verificar que la entrada de calles se mapee correctamente a `Mapping[str, Sequence[tuple[str, float]]]`. La salida será interpretada devolviendo la tupla `(tiempo_total, ruta_secuencial)`. Si el destino es inalcanzable, se devolverá `(inf, [])` según el contrato reutilizado
- **Prueba distintiva:** Un grafo donde exista una ruta directa `A -> B` con un costo de 10 minutos, y una ruta indirecta `A -> C -> B` con costos de 2 y 3 minutos respectivamente. Dijkstra debe preferir la ruta indirecta (costo 5), a diferencia de BFS que elegiría la ruta de un solo salto
- **Complejidad e interpretación:** $\mathcal{O}((V+E) \log V)$ La salida interpreta el recorrido temporalmente más eficiente y su costo acumulado.

## Escenario 2

- **Problema y objetivo:** Programar la renovación de cada edificio de una universidad respetando prerrequisitos técnicos El objetivo es un **orden de dependencias**
- **Dirección y pesos:** Grafo dirigido (precedencias estrictas) y sin pesos
- **Operación dominante:** Detectar y procesar tareas sin requisitos pendientes (liberar grado de entrada cero)
- **Estructura y algoritmo:** Cola combinada con arreglo de grados de entrada; algoritmo de Kahn
- **Contrato:** Requiere precedencias dirigidas formando un Grafo Dirigido Acíclico (DAG)
- **Alternativa descartada:** BFS, porque aunque usa una cola, BFS encolaría un edificio con tan solo descubrirlo por una de sus aristas entrantes, sin esperar a que se cumplan *todos* sus prerrequisitos técnicos
- **Módulo previo reutilizado:** `orden_topologico` del módulo de la Clase 19.
- **Adaptación de entrada/salida:** Si los datos originales vienen como pares `(prerrequisito, edificio)`, se debe construir un adaptador estrecho que transforme esta lista en un diccionario de adyacencias normalizado antes de llamar a la función La salida será la lista secuencial de renovaciones o un indicador de ciclo.
- **Prueba distintiva:** Un nodo que tiene dos prerrequisitos. La prueba debe garantizar que el nodo no entra a la cola ni se libera tras completarse únicamente el primero de sus requisitos, sino solo hasta que su grado de entrada llegue exactamente a cero
- **Complejidad e interpretación:** $\mathcal{O}(V+E)$ La salida representa un plan secuencial válido de construcción que no viola ninguna restricción técnica previa.

## Caso fuera del alcance

**Pesos negativos en caminos mínimos.** 
Si el problema de movilidad urbana introdujera una arista con tiempo negativo (por ejemplo, una bonificación de tiempo `−4`) El contrato violado es la premisa central de Dijkstra: al extraer una distancia como mínima, esta es definitiva y no puede mejorar posteriormente cruzando una arista negativa No inventamos una solución (como sumar una constante a todos los pesos o ignorar el signo) porque rompería matemáticamente el algoritmo; la respuesta técnica correcta es documentar que ninguno de los algoritmos estudiados (BFS, 0-1 BFS, Dijkstra) resuelve el caso general de caminos más cortos con pesos negativos

## Reflexión final

Al principio del curso, solía elegir una estructura de datos simplemente por familiaridad o porque parecía un "contenedor" lógico para los datos Ahora, mi proceso de decisión inicia forzosamente identificando la **operación dominante** del problema: reconozco qué cálculo repetirá el algoritmo intensivamente y solo entonces selecciono la estructura que abarata esa operación específica (por ejemplo, un heap para prioridades o Union-Find para componentes) Además, aprendí que reutilizar código no significa copiar a ciegas, sino validar precondiciones, adaptar datos en los bordes y diseñar pruebas que distingan decisiones técnicas competidoras