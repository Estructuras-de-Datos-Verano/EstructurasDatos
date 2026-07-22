# Daniel

### 1. De representar a recorrer
Representar un grafo es un proceso estático que consiste en definir las estructuras de datos (como listas de adyacencia) encargadas de modelar los vértices y sus conexiones en memoria[cite: 1, 2]. Por el contrario, recorrer un grafo es un proceso dinámico[cite: 1]. Exige diseñar una lógica iterativa o recursiva capaz de navegar por esas conexiones de forma ordenada, asegurando que se visiten los estados necesarios sin caer en redundancias ni bucles infinitos[cite: 1].

### 2. Estrategias manuales
Durante las simulaciones a mano previas a la formalización de los algoritmos, se hicieron evidentes dos comportamientos naturales de exploración humana[cite: 1, 2]:
* La exploración por "ondas de cercanía" (niveles), ideal para barrer un área circundante de manera uniforme[cite: 1].
* La exploración por "persecución de caminos" (profundidad), donde la prioridad es seguir una pista recta hasta que se agote la ruta antes de regresar a evaluar alternativas[cite: 1].

### 3. BFS (Breadth-First Search)
La búsqueda en anchura basa su estrategia en la expansión concéntrica[cite: 1]. Para lograr esto de forma ordenada, utiliza una **cola** como estructura de control (política FIFO)[cite: 1]. Al procesar siempre el nodo pendiente más antiguo, el algoritmo garantiza que revisará la totalidad de los nodos que se encuentran a una distancia $k$ antes de aventurarse a los nodos de distancia $k+1$[cite: 1]. Esta propiedad matemática lo vuelve la herramienta óptima para calcular caminos mínimos en grafos no ponderados[cite: 1].

### 4. DFS (Depth-First Search)
La búsqueda en profundidad prioriza la inmersión vertical en el grafo[cite: 1]. Se apoya en una **pila** (o en la pila de llamadas de la recursión) bajo la política LIFO[cite: 1]. Al atender siempre el elemento más recientemente descubierto, el algoritmo avanza con rapidez hacia los confines de una rama individual y solo realiza un retroceso (*backtracking*) cuando se encuentra atrapado o sin vecinos nuevos[cite: 1]. No garantiza caminos mínimos, pero es sumamente eficiente para explorar topologías completas[cite: 1].

### 5. Comparación
La diferencia crítica radica en el orden de extracción de la agenda de pendientes[cite: 1]. Modificar una sola línea de código en un BFS para sustituir la cola por una pila transforma de inmediato el comportamiento del algoritmo en un DFS[cite: 1]. Mientras que BFS requiere almacenar frentes de onda potencialmente grandes en memoria (ancho del grafo), DFS requiere memoria proporcional a la altura de la rama más profunda de la exploración.

### 6. Visualización
El uso de representaciones visuales fijas (como los layouts de NetworkX) permite capturar la dinámica temporal del recorrido[cite: 1]. Una simple lista de nodos visitados no refleja el costo de las aristas muertas evaluadas ni los momentos exactos de *backtracking*[cite: 1]. La animación ayuda a contrastar de manera intuitiva cómo el BFS "inunda" el grafo frente a cómo el DFS "serpentea" a través de él[cite: 1].

### 7. CSES
En el análisis de los problemas seleccionados de la plataforma CSES[cite: 1]:
* En **Message Route**, BFS es la opción obligatoria debido a que el problema requiere explícitamente el camino más corto en cantidad de conexiones de red[cite: 1].
* En **Counting Rooms**, tanto BFS como DFS son perfectamente válidos para etiquetar las componentes conexas (habitaciones)[cite: 1], siendo DFS el más habitual por su simplicidad de implementación recursiva.
* En **Labyrinth**, el rastro de la ruta se vuelve posible gracias al almacenamiento sistemático de un nodo predecesor durante la fase de descubrimiento[cite: 1].

### 8. Pruebas
El diseño de pruebas de caja negra y caja blanca debe ir más allá de los casos felices[cite: 2]. Es crucial evaluar el comportamiento del conjunto de visitados ante grafos cíclicos (evitando ciclos infinitos)[cite: 1], así como el comportamiento ante grafos desconectados (asegurando que el algoritmo se detenga correctamente al agotar la componente conexa inicial)[cite: 1].

### 9. Patrón descubierto
El patrón de recorrido de grafos se activa siempre que nos enfrentamos a problemas de conectividad, alcanzabilidad o búsqueda de caminos en estructuras discretas[cite: 1]. Sus componentes fundamentales son universales: un estado inicial, una colección para gestionar la frontera de exploración futura (pila/cola) y una colección de memoria para el historial pasado (visitados)[cite: 1].

### 10. Pregunta abierta
¿Bajo qué criterios de diseño o umbrales de escala de datos se vuelve estrictamente necesario abandonar las implementaciones recursivas de DFS en favor de un DFS iterativo con pila explícita para prevenir desbordamientos de pila (*Stack Overflow*) en entornos de producción reales?