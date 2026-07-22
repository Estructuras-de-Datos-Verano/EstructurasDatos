## Discusión técnica — Clase 20

Nombre: [Aristeo]

## Escenario 1: Movilidad Urbana con Costos Generales (A3)

- Problema y objetivo: Encontrar la ruta óptima en tiempo entre dos estaciones.
- Dirección y pesos: Grafo dirigido con pesos no negativos.
- Operación dominante: Extraer el nodo con el menor coste en tiempo acumulado.
- Estructura y algoritmo: Heap junto con Dijkstra.
- Contrato: Todas las aristas del grafo deben tener pesos no negativos.
- Alternativa descartada: BFS regular
- Módulo previo reutilizado: `clase_18.dijkstra`
- Adaptación de entrada/salida: Se mapea la lista de calles con sus coordenadas e índices numéricos a la lista ponderada exigida por el módulo, cuando recibe el vector de distancias se reconstruye la secuencia ordenada de estaciones desde el destino hacia atrás.
- Prueba distintiva: Un triángulo de nodos A, B, C, ruta directa A -> B con peso 10, ruta alternativa A -> C -> B con pesos A -> C (2) y C -> B, el BFS elegirá la directa de costo 10 (1 salto) y Dijkstra optará por el camino indirecto de coste 5 (2 saltos).
- Complejidad e interpretación: $O((V+E)log V)$. Devuelve la ruta exacta que minimiza la duración del viaje.

## Escenario 2: Renovación y Planificación de Edificios Académicos

- Problema y objetivo: Organizar cronológicamente las remodelaciones respetando requisitos de obra.
- Dirección y pesos: Grafo dirigido sin pesos.
- Operación dominante: Detección de vértices sin ningún requisito pendiente (grado de entrada 0).
- Estructura y algoritmo: Cola FIFO y Vector de grados de entrada.
- Contrato: El grafo debe ser un DAG. Si hay ciclos de dependencia cruzada el proceso no puede completarse.
- Alternativa descartada: Kruskal (MST).
- Módulo previo reutilizado: `clase_19.kahn`
- Adaptación de entrada/salida: Mapear los nombres de los edificios a índices enteros de 0 a V-1.
- Prueba distintiva: Tres tareas: $A, B, C$ donde A -> B y A -> C. La cola inicial recibirá el nodo A, al procesarlo el grado de B y C decae a 0. Cualquiera de los órdenes $[A, B, C]$ o $[A, C, B]$ es una salida válida de Kahn.
- Complejidad e interpretación: $O(V + E)$. El resultado representa la secuencia de obras que evita parálisis de dependencias.

## Caso fuera del alcance

Si se quiere resolver rutas con pesos negativos, el contrato de Dijkstra se viola.
## Reflexión final

Creo que con el curso pude aprender estructuras logicas para poder optimzar procesos, así como elegir la mejoir estructura para cada problema a resolver.

