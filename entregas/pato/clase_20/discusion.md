# Clase 20: Discusión
#### Nombre: Patricio Navarro

## Escenario 1

- Problema y objetivo: Tender enlaces de comunicación entre los edificios de la universidad para que todos queden conectados entre sí al menor costo total posible.
- Dirección y pesos: Grafo no dirigido y pesos no negativos que representan el costo de construcción de cada enlace.
- Operación dominante: Encontrar y fusionar componentes conexas de forma rápida utilizando la arista más barata disponible.
- Estructura y algoritmo: Union-Find y Algoritmo de Kruskal.
- Contrato: Devolver el conjunto exacto de conexiones que forman el árbol de expansión mínima (MST) sin ciclos[cite: 3]. Si el grafo está desconectado, lanzar una señal de advertencia.
- Alternativa descartada: Dijkstra. Se descarta porque Dijkstra minimiza distancias individuales desde un único punto de origen, lo cual suele inflar el costo total si lo que se busca es unir a toda la red en conjunto.
- Módulo previo reutilizado: `entregas.clase_18.Pato.kruskal` .
- Adaptación de entrada/salida: La entrada se adapta ordenando la lista de aristas originales por peso en formato de tuplas `(u, v, peso)`. La salida transforma el conjunto de aristas del MST devuelto en una lista plana de enlaces a construir.
- Prueba distintiva: Un triángulo de tres edificios (A, B, C) donde las conexiones directas desde un edificio central son costosas, pero los enlaces periféricos son baratos. Kruskal conecta los tres usando dos aristas baratas, mientras que Dijkstra elegiría las rutas radiales directas encareciendo el total.
- Complejidad e interpretación: Complejidad `O(E log E)`. La salida representa el plano de cableado ideal para comunicar todo el campus gastando lo mínimo posible.

## Escenario 2

- Problema y objetivo: Encontrar la ruta que tome menos tiempo entre la estación de la ambulancia y el lugar del accidente.
- Dirección y pesos: Grafo dirigido y pesos no negativos que representan el tiempo en minutos para recorrer cada tramo.
- Operación dominante: Consultar y extraer constantemente el nodo que tenga la menor distancia tentativa acumulada.
- Estructura y algoritmo: Heap y Algoritmo de Dijkstra.
- Contrato: Devolver la secuencia ordenada de esquinas que garantizan el menor tiempo acumulado desde el origen. Si el destino no es alcanzable, devolver infinito o None.
- Alternativa descartada: BFS. Se descarta porque BFS solo cuenta la cantidad de calles recorridas e ignoraría si una ruta con más tramos es en realidad mucho más rápida por estar libre de tráfico.
- Módulo previo reutilizado: `entregas.clase_16.Pato.dijkstra`.
- Adaptación de entrada/salida: La entrada adapta el mapa urbano a un diccionario de adjacencia de Python. La salida toma el mapa de predecesores devuelto por el algoritmo y reconstruye al revés la lista ordenada de calles (`["Base", "Calle A", "Destino"]`).
- Prueba distintiva: Una avenida directa que tarda 15 minutos (1 sola arista) contra un desvío residencial de dos calles que tarda 3 y 5 minutos (2 aristas). BFS elegiría la avenida por tener menos tramos, pero Dijkstra elige el desvío por tardar menos tiempo total (8 minutos).
- Complejidad e interpretación: Complejidad `O((V+E) log V)`. La salida es la ruta de navegación exacta para que la ambulancia esquive los embotellamientos y llegue en el menor tiempo posible.

## Caso fuera del alcance

1. Intentar calcular un camino mínimo en un grafo que contiene costos o pesos negativos viola el contrato de los algoritmos estudiados. En este escenario, el invariante de Dijkstra se rompe porque asume que una vez que extraes un nodo como "mínimo", su distancia ya es definitiva. Si hay pesos negativos, una ruta futura podría restar costo y mejorar un nodo ya cerrado, atrapando al algoritmo o dando un resultado erróneo. 

2. No se debe inventar una solución artificial  porque eso altera la naturaleza real del problema y escondería fallos graves de lógica.

## Reflexión final
- Al inicio del curso, mi proceso se limitaba a elegir una estructura o un algoritmo basándome en la intuición o en qué nombre "sonaba bien" con el enunciado del problema, más que nada por la solución.
- Ahora, lo que hago es realmente hacer preguntas guiadas como las de los notebooks y tratar de ponerlo en papel de manera que entienda el comportamiento y así poder elegir la estructura correcta.