# Respuestas del notebook — Clase 20

Nombre: [Aristeo]

## Pregunta inicial

### Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?

Hay que entender el objetivo del problema, debemos checar si necesitamos encontrar un camino, conectar todos los nodos o establecer un orden entre tareas.

## Respuestas por sección

### 1. Recuperación: primero aparecen las estructuras
- Cola: Se usa en BFS para recorrer los nodos en el mismo orden en que se descubren, explorando el grafo por niveles.
- Deque: Se usa en 0-1 BFS porque permite agregar nodos al inicio cuando el costo es 0 y al final cuando el costo es 1.
- Heap: Se usa en Dijkstra para obtener rápidamente el nodo con la menor distancia conocida.
- Union-Find: Se usa en Kruskal para comprobar si dos nodos ya pertenecen al mismo grupo y así evitar ciclos.
- Grados de entrada + cola: Se usa en Kahn para encontrar las tareas que ya no tienen dependencias y pueden procesars

### 2. Del enunciado a una decisión
No es buena idea elegir un algoritmo solo por palabras clave, ya que una misma palabra puede tener distintos significados según el problema.

### 3. Identificar el objetivo
- Camino mínimo: Encuentra la mejor ruta entre un origen y un destino.
- MST (Árbol de Expansión Mínimo): Conecta todos los nodos con el menor costo total posible.
- Orden topológico: Organiza los nodos respetando las dependencias entre ellos.

### 4. Dirección y significado de las aristas
Si una dependencia dirigida se trata como si fuera bidireccional, se pierde el orden correcto entre las tareas. Esto puede permitir que una tarea se haga antes de cumplir sus requisitos o incluso generar ciclos.

### 5. Clasificar el dominio de pesos
El dato "hay pesos" es insuficiente porque no especifica las restricciones del dominio. Si los pesos son exclusivamente `0 y 1`, podemos explotar la estructura de un *deque* para resolver el problema en tiempo lineal $O(V + E)$ con **0-1 BFS**. Si los pesos son `no negativos generales` (como valores continuos o mayores a 1), el invariante de 0-1 BFS se rompe y estamos obligados a utilizar un *heap* con **Dijkstra**, lo que eleva el costo a $O((V + E) \log V)$.

### 6. Matriz de decisión integradora
La columna **"Operación dominante"**. Es la que conecta directamente la necesidad algorítmica con la ventaja mecánica de la estructura (por ejemplo, "extraer menor distancia" apunta inequívocamente al uso de un Heap).

### 7. Laboratorio de decisión interactivo
Antes de revelar el algoritmo, se debe predecir: el **objetivo real**, el **tipo de grafo (pesos/dirección)** y la **operación dominante**. Utilizaré como evidencia las precondiciones del contrato del algoritmo y los contraejemplos de las pruebas distintivas para corregir cualquier supuesto erróneo.

### 8. Caso de camino sin pesos: BFS
El invariante de que **la cola procesa los nodos estrictamente en orden creciente de sus distancias (por capas)**. Dado que las aristas no tienen peso (costo uniforme = 1), cuando un nodo es descubierto por primera vez, es imposible que exista un camino posterior con menos aristas que pueda alcanzarlo.

### 9. Caso de pesos 0/1: 0-1 BFS
Una mejora con peso 0 significa que el nodo vecino se encuentra a la misma distancia de la capa actual, por lo que debe ser procesado de inmediato (va al **frente** del deque). Una mejora con peso 1 significa que pertenece a la siguiente capa de distancia absoluta, por lo que se envía al **final** del deque para esperar su turno correspondiente, manteniendo la propiedad de orden sin recurrir a un heap.

### 10. Caso de pesos generales: Dijkstra
La operación de **extraer el mínimo valor de un conjunto dinámico de distancias tentativas**. El heap permite consultar y remover este mínimo de forma eficiente en tiempo logarítmico, asegurando que el nodo extraído ya posee su distancia mínima definitiva.

### 11. BFS, 0-1 BFS y Dijkstra no forman una competencia
Dijkstra sobre un dominio de pesos 0/1 es técnicamente correcto porque cumple con la precondición de no-negatividad, pero **no es la elección más adecuada** porque introduce un costo extra de ordenamiento logarítmico $O((V+E) \log V)$ mediante el heap, desperdiciando la oportunidad de resolverlo en tiempo lineal $O(V+E)$ usando un deque con 0-1 BFS.

### 12. Pesos negativos: rechazar con precisión
Técnicamente se justifica porque la presencia de aristas negativas **viola la precondición fundamental (contrato) de Dijkstra**. Al haber pesos negativos, el invariante de codicia se rompe: un nodo extraído del heap como "definitivo" podría mejorar su distancia más adelante a través de una trayectoria con un peso negativo. Al no haberse estudiado algoritmos para el caso general con pesos negativos (como Bellman-Ford), la respuesta honesta y rigurosa es "ninguno de los estudiados".

### 13. Conexión global: Kruskal y Union-Find
La consulta de alcanzabilidad/conectividad entre componentes: `find(u) == find(v)`. Esta operación se repite para cada arista candidata (ordenadas de menor a mayor peso) para verificar si su unión formaría un ciclo en el árbol.

### 14. Árbol de caminos mínimos no es MST
Porque Dijkstra toma decisiones locales **minimizando de forma acumulativa la distancia desde un único nodo raíz**. Esto puede provocar que elija aristas individuales muy costosas si estas ofrecen un "atrás directo" más corto a la raíz. En cambio, un MST busca minimizar globalmente la **suma total del peso de la red de cables**, sin importar si las rutas individuales internas entre nodos se vuelven más largas o indirectas.

### 15. Dependencias: Kahn y grados de entrada
Significa que el nodo **no tiene ningún prerrequisito o tarea pendiente** en ese momento del ordenamiento, por lo que está completamente libre y disponible para ser colocado inmediatamente en la secuencia de salida.

### 16. BFS y Kahn comparten cola, no invariante
La información adicional es el **estado auxiliar** y las operaciones sobre los vecinos: BFS utiliza un conjunto/arreglo de `visitados` o `distancias` para evitar ciclos, mientras que Kahn utiliza un arreglo dinámico de `grados de entrada` que se decrementa progresivamente a medida que los requisitos de los nodos sucesores se van liberando.

### 17. Contratos antes de ejecutar
Conserva la responsabilidad de **validar y adaptar la representación de los datos de entrada** (verificar que cumplan las precondiciones del contrato), así como de **interpretar correctamente los valores de retorno especiales** (como infinitos, listas vacías o indicadores de ciclos) para traducirlos en respuestas accionables para el dominio del problema.

### 18. Reutilización en lugar de recopia
Copiar el código duplica la lógica propiciando la aparición de bugs divergentes, dificulta el mantenimiento y ensucia el repositorio. Importar y usar un **adaptador estrecho** promueve la modularidad, permite centralizar las optimizaciones o correcciones en una única implementación base ya probada y aísla la lógica de conversión de datos.

### 19. Diseñar pruebas que distinguen decisiones
Una prueba es distintiva porque presenta una **estructura de control/datos mínima diseñada específicamente para forzar a dos algoritmos plausibles a tomar caminos u objetivos diferentes**, demostrando empíricamente por qué uno es correcto y el otro falla (ej. un grafo donde el camino con menos aristas es el más costoso en peso). Un caso feliz común no aporta información porque ambos algoritmos podrían coincidir en el resultado por mero azar del diseño del grafo.

### 20. Clínica de selecciones incorrectas
*   **Propuesta 1 (“Usaré BFS porque hay que llegar de A a B, pero las calles tienen tiempos 2 y 9”):**
    *   *Objetivo real:* Camino mínimo optimizando la suma de pesos.
    *   *Contrato violado:* Costo uniforme/sin pesos (BFS exige que todas las aristas valgan lo mismo).
    *   *Operación dominante:* Extraer de forma continua la menor distancia tentativa.
    *   *Corrección:* Utilizar un **Heap** junto con el algoritmo de **Dijkstra**.
*   **Propuesta 2 (“Usaré Dijkstra para conectar todas las sedes, pero se minimiza el costo total de la red”):**
    *   *Objetivo real:* Conexión mínima global (unir todos los componentes al menor costo).
    *   *Contrato violado:* Dijkstra optimiza rutas desde un único origen individual, no el peso de la red completa.
    *   *Operación dominante:* Validar si dos nodos ya están conectados en el mismo componente y fusionarlos.
    *   *Corrección:* Utilizar la estructura **Union-Find** junto con el algoritmo de **Kruskal**.

### 21. Trabajo en equipo A: movilidad urbana
A pesar de que el fin general es el costo mínimo, la naturaleza del dominio de pesos altera la operación dominante:
*   En **A1** (sin pesos) la operación dominante es avanzar por capas puras de llegada $\rightarrow$ **Cola + BFS**.
*   En **A2** (pesos 0 y 1) la operación es priorizar de manera inmediata los costos nulos frente a los unitarios $\rightarrow$ **Deque + 0-1 BFS**.
*   En **A3** (pesos generales no negativos) la operación dominante es la extracción del mínimo absoluto de un conjunto variable $\rightarrow$ **Heap + Dijkstra**.

### 22. Trabajo en equipo B: construir y planificar
Porque los nodos representan entidades físicas idénticas (los edificios), pero las **aristas poseen semánticas radicalmente distintas**. En la primera necesidad las aristas son enlaces simétricos bidireccionales (no dirigidos) con costo monetario; en la segunda, representan flechas de precedencia temporal estricta (dirigidas) sin pesos asociados. Los algoritmos dependen del significado y restricciones de las aristas, no de la identidad de los nodos.

### 23. Comunicación técnica de una decisión
Debe contener obligatoriamente: el **objetivo del problema**, el **tipo de grafo (dirección y pesos)**, la **operación dominante**, la **estructura de datos seleccionada**, el **algoritmo compatible**, las **precondiciones del contrato**, la **prueba distintiva** aplicada, la **complejidad asintótica** (explicada en variables del problema $V$ y $E$) y la **interpretación del resultado**.

### 24. Reflexión final del curso
1. Antes elegía una estructura por *familiaridad o intuición superficial*; ahora primero identifico *la operación dominante dictada por el objetivo y las restricciones del problema*.
2. El contrato que más me ayudó a detectar un error fue *la restricción de pesos no negativos en Dijkstra* porque *me forzó a detener la ejecución y rechazar formalmente modelos con bonificaciones negativas en lugar de intentar parchar el algoritmo*.
3. Ante un algoritmo que no aplica, ahora puedo *declarar con precisión técnica que el problema está fuera del alcance de las soluciones estudiadas, argumentando qué invariante se rompe*.

### 25. Síntesis y cierre

**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**

Identificamos la operación dominante desglosando minuciosamente el problema a través de una ruta metodológica clara: primero determinamos el **objetivo de la salida** (camino, MST o precedencia), luego clasificamos el **tipo de grafo** (dirección de aristas y dominio exacto de pesos). La intersección de estas restricciones revela cuál es la acción crítica y repetitiva que gobierna el costo computacional. 

Con esto en mente, seleccionamos la **estructura de datos** diseñada específicamente para optimizar dicha operación (Cola, Deque, Heap, Union-Find o Grados de entrada) y finalmente adoptamos el **algoritmo** que construya sus invariantes sobre esa estructura, asegurándonos de validar estrictamente sus precondiciones mediante un contrato robusto y pruebas distintivas.

---
## Corrección final de mi respuesta inicial

*(Al finalizar el laboratorio, compara esta sección con tu intuición original de la materia).*