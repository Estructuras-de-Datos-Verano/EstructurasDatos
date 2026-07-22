# Discusión técnica — Clase 20

Nombre: José Daniel Molina Carrillo

## Escenario 1

- Problema y objetivo: Optimización de rutas en redes de transporte para encontrar el camino mínimo entre puntos específicos.
- Dirección y pesos: Red dirigida con costos variables no negativos en cada tramo.
- Operación dominante: Extraer repetidamente la menor distancia tentativa acumulada.
- Estructura y algoritmo: Algoritmo de Dijkstra implementado con un heap binario.
- Contrato: Exige un nodo origen válido y que todas las aristas tengan pesos no negativos.
- Alternativa descartada: BFS, ya que cuenta únicamente el número de aristas e ignora los costos variables.
- Módulo previo reutilizado: `clase_10.dijkstra` o similar del módulo de caminos mínimos ponderados.
- Adaptación de entrada/salida: Transformamos el mapa de calles a una lista de adyacencia con tuplas `(vecino, peso)`.
- Prueba distintiva: Grafo con una ruta de pocas aristas costosas y otra larga pero barata.
- Complejidad e interpretación: O(E log V), ideal para procesar mapas urbanos de forma eficiente.

## Escenario 2

- Problema y objetivo: Planificación de tareas secuenciales para determinar un orden de dependencias válido.
- Dirección y pesos: Relaciones dirigidas sin pesos, representando precedencias puras entre actividades.
- Operación dominante: Identificar y liberar nodos que tengan grado de entrada cero.
- Estructura y algoritmo: Algoritmo de Kahn asistido por una cola de procesamiento.
- Contrato: Requiere obligatoriamente un grafo dirigido acíclico (DAG) para evitar bloqueos mutuos.
- Alternativa descartada: BFS estándar, ya que su invariante por capas ignora si quedan prerrequisitos pendientes.
- Módulo previo reutilizado: `clase_14.orden_topologico` del módulo de ordenamiento en grafos.
- Adaptación de entrada/salida: Convertimos las restricciones a un vector de grados de entrada iniciales.
- Prueba distintiva: Un grafo con un ciclo cerrado que debe ser detectado para lanzar un error.
- Complejidad e interpretación: $O(V+E)$, lo que permite secuenciar proyectos masivos en tiempo lineal.

## Caso fuera del alcance

Afrontar caminos mínimos con pesos negativos viola el contrato fundamental de Dijkstra, ya que la presencia de valores negativos destruye el invariante de codicia al reabrir nodos ya procesados; para esto evitamos inventar soluciones caseras porque introducirían loops infinitos o degradaciones exponenciales incorrectas.

## Reflexión final

Antes elegía las herramientas por mera familiaridad con el código. Ahora analizo primero la operación dominante y el dominio de los pesos, ya que esto me permite seleccionar la estructura exacta que abarata el problema de forma matemática.