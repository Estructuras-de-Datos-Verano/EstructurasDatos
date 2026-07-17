# Respuestas del notebook — Clase 20

Nombre: Gustavo

## Pregunta inicial

Analizando primero qué queremos lograr y si el problema tiene pesos o direcciones, para luego ver qué operación se repetirá más veces.

## Respuestas por sección

**1. Recuperación: primero aparecen las estructuras**
* Cola: sacar al primero que llegó.
* Deque: meter y sacar cosas rápido por ambos extremos.
* Heap: encontrar y sacar la prioridad máxima o mínima de inmediato.
* Union-Find: saber rápido si dos cosas ya están en el mismo grupo y poder juntarlas.
* Grados de entrada: detectar qué tareas ya no tienen cosas pendientes por hacer antes.

**2. Del enunciado a una decisión**
Porque las palabras pueden engañar; "conectar" puede ser simplemente ir de un punto a otro (una ruta) o puede ser unir toda una red sin importar de dónde empieces, lo que requiere herramientas matemáticas totalmente distintas.

**3. Identificar el objetivo**
* Un camino mínimo te da una ruta directa (una secuencia de nodos).
* Un MST te da un conjunto de conexiones globales (una red completa).
* Un orden topológico te da una lista secuencial de cosas por hacer una tras otra.

**4. Dirección y significado de las aristas**
Si tratamos un prerrequisito (que es dirigido) como algo de doble sentido, podríamos bloquear tareas pensando que "A depende de B" cuando en realidad la regla original era que "B depende de A".

**5. Clasificar el dominio de pesos**
Porque necesitamos saber exactamente el *tipo* de pesos. Si los pesos son exclusivamente 0 y 1, nos conviene usar 0-1 BFS, pero si son números positivos variables como 2 o 7, necesitamos forzosamente Dijkstra.

**6. Matriz de decisión integradora**
La columna de "Operación dominante", ya que la estructura se elige específicamente para hacer que esa operación repetitiva sea lo más barata y rápida posible.

**7. Laboratorio de decisión interactivo**
Debes predecir el objetivo, la estructura de datos y el algoritmo. Usarás el contrato, la prueba distintiva y la complejidad para ver si le atinaste o si debes corregir tu suposición inicial.

**8. Caso de camino sin pesos: BFS**
BFS funciona revisando por "capas" concéntricas. Esto asegura que todo lo que está a distancia 0 se revisa antes que todo lo de distancia 1, garantizando que cuando llegas a un nodo por primera vez, es por la ruta con menos aristas.

**9. Caso de pesos 0/1: 0-1 BFS**
Porque si nos cuesta 0, funciona como un "atajo" que mejora nuestro camino y debemos tomarlo de inmediato poniéndolo al frente. Si nos cuesta 1, es un movimiento normal y debe formarse al final a esperar su turno.

**10. Caso de pesos generales: Dijkstra**
La operación de extraer continuamente la menor distancia tentativa de entre todas las opciones posibles.

**11. BFS, 0-1 BFS y Dijkstra no forman una competencia**
Dijkstra es matemáticamente correcto porque funciona con números positivos, pero hace trabajo extra y procesamientos innecesarios. 0-1 BFS es mucho más adecuado porque aprovecha que solo hay dos opciones posibles para resolver el problema más rápido en $O(V+E)$.

**12. Pesos negativos: rechazar con precisión**
El algoritmo de Dijkstra asume que, una vez que sacas una distancia mínima, no habrá un camino en el futuro con un peso tan negativo que logre mejorar ese resultado. Un peso negativo rompe este invariante por completo y viola el contrato.

**13. Conexión global: Kruskal y Union-Find**
Estar preguntando constantemente "si dos nodos ya pertenecen al mismo componente o grupo" para unirlos si no lo están, evitando crear ciclos cerrados inútiles.

**14. Árbol de caminos mínimos no es MST**
Porque Dijkstra busca obsesivamente que cada ruta individual desde el punto "A" sea la más rápida. Por el contrario, Kruskal (MST) busca que el total del cableado para conectar todo sea el más barato, incluso si viajar de "A" a "D" implica dar más vueltas.

**15. Dependencias: Kahn y grados de entrada**
Significa que esa tarea ya está "libre" y se puede comenzar a trabajar en ella porque todos sus requisitos previos ya se completaron exitosamente.

**16. BFS y Kahn comparten cola, no invariante**
* En BFS la cola guarda los nodos descubiertos que nos falta explorar y su estado auxiliar son las distancias o los visitados.
* En Kahn la cola guarda los nodos que ya no tienen prerrequisitos y su estado auxiliar son los grados de entrada.

**17. Contratos antes de ejecutar**
El código debe validar que se cumplan las "precondiciones" antes de usar la función. Por ejemplo, asegurarse de que no le estemos pasando un grafo con pesos negativos a Dijkstra o verificar que la dirección de las aristas sea la correcta.

**18. Reutilización en lugar de recopia**
Porque copiar el código hace que existan muchas versiones de lo mismo, lo que puede causar confusiones. Reutilizar permite usar algo que ya está súper probado y validado; solo necesitas adaptar la forma en que entran los datos.

**19. Diseñar pruebas que distinguen decisiones**
Que debe fallar obligatoriamente si intentas usar una herramienta que parece lógica pero no lo es. Por ejemplo, crear un grafo tramposo donde BFS te dé una ruta con menos nodos pero más cara, demostrando que ahí se ocupaba Dijkstra.

**20. Clínica de selecciones incorrectas**
* **Error 1 ("Usaré BFS para ir de A a B con tiempos de 2 y 9"):** El objetivo real es el camino mínimo. Contrato violado: BFS solo sirve sin pesos. Operación dominante: Extraer la menor distancia. Corrección: Usar Dijkstra con un heap.
* **Error 4 ("Usaré Kruskal para prerrequisitos"):** El objetivo real es un orden de dependencias. Contrato violado: Kruskal pide grafos no dirigidos y los requisitos tienen flechas. Operación dominante: Liberar nodos con grado cero. Corrección: Usar Kahn con una cola.

**21. Trabajo en equipo A: movilidad urbana**
Aunque el objetivo siempre es llegar barato, la estructura cambia drásticamente: en A1 (sin pesos) usas una cola y BFS. En A2 (pesos 0 y 1) usas un deque y 0-1 BFS. En A3 (pesos generales positivos) usas un heap y Dijkstra.

**22. Trabajo en equipo B: construir y planificar**
Porque los enlaces entre edificios son conexiones físicas que funcionan en ambos sentidos (no dirigidas para Kruskal), mientras que las renovaciones son pasos lógicos obligatorios que tienen una dirección estricta de un lado a otro (dirigidas para Kahn).

**23. Comunicación técnica de una decisión**
Para que sea auditable debe mencionar: el objetivo, las restricciones (pesos y direcciones), cuál es la operación dominante, la estructura y el algoritmo seleccionado, el contrato, y también por qué descartaste la otra alternativa lógica.

**24. Reflexión final del curso**
1. Antes elegía una estructura por familiaridad; ahora primero identifico la operación dominante que abarata el costo.
2. El contrato que más me ayudó a detectar un error fue el de Dijkstra porque comprender que no admite pesos negativos evita que entregue distancias falsas.
3. Ante un algoritmo que no aplica, ahora puedo indicar explícitamente qué regla se rompió y rechazarlo con precisión en lugar de inventar una solución.
Mi proceso cambió en que ahora justifico mis decisiones con pruebas distintivas y contratos matemáticos.

## Corrección final de mi respuesta inicial

Empezamos definiendo el objetivo final y viendo las restricciones exactas del problema (si hay dirección y qué tipo de pesos tiene). Con esa información, determinamos cuál será la operación que se va a repetir más veces; al saber eso, simplemente escogemos la estructura de datos que haga que esa operación sea rápida y el algoritmo que haga match.