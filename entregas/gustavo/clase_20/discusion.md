# Discusión técnica — Clase 20

Nombre: Gustavo

## Escenario 1

- Problema y objetivo: Encontrar la ruta más rápida en un edificio donde cada pasillo cuenta como un paso. El objetivo es un camino mínimo.
- Dirección y pesos: Grafo dirigido o no dirigido, sin pesos.
- Operación dominante: Procesar por capas.
- Estructura y algoritmo: Cola y BFS.
- Contrato: Asume aristas con costo uniforme (no modelado) para garantizar la ruta con el mínimo número de aristas.
- Alternativa descartada: Dijkstra. Aunque es correcto, usar un heap para simular prioridades iguales añade un costo computacional logarítmico innecesario.
- Módulo previo reutilizado: Implementación de BFS de clases anteriores (ej. de la Clase 16).
- Adaptación de entrada/salida: Escribir un adaptador estrecho que convierta los nombres de los nodos (strings) a índices enteros si la función antigua lo requiere. La salida (un diccionario de predecesores) se reconstruye para devolver la ruta legible.
- Prueba distintiva: Diseñar un grafo con dos rutas hacia el mismo destino: una con dos aristas y otra con tres aristas. BFS debe devolver invariablemente la de dos aristas.
- Complejidad e interpretación: Costo $O(V+E)$. La salida se interpreta como la ruta que requiere la menor cantidad de movimientos o transferencias posibles.

## Escenario 2

- Problema y objetivo: Programar la renovación de edificios de una universidad respetando prerrequisitos técnicos. El objetivo es un orden de dependencias.
- Dirección y pesos: Grafo con precedencias dirigidas, sin pesos.
- Operación dominante: Liberar tareas que tienen grado de entrada cero.
- Estructura y algoritmo: Cola apoyada por un arreglo de grados de entrada, utilizando el algoritmo de Kahn.
- Contrato: Requiere precedencias dirigidas. Garantiza un orden válido o devuelve una señal si existe un ciclo.
- Alternativa descartada: BFS. Aunque usa una cola, BFS encola nodos descubiertos por nivel de distancia, mientras que Kahn encola nodos disponibles porque ya no tienen dependencias pendientes.
- Módulo previo reutilizado: Implementación de Kahn de las clases finales del curso.
- Adaptación de entrada/salida: Validar que la dirección de la arista $u \to v$ signifique estrictamente "$u$ debe completarse antes que $v$". Interpretar el retorno: si la lista devuelta tiene menos de $V$ elementos, significa que existe un bloqueo.
- Prueba distintiva: Configurar un nodo que dependa de dos tareas previas. La prueba debe verificar que el nodo no entra a la cola cuando se completa la primera tarea, sino hasta que ambas (su grado llega a cero) estén terminadas.
- Complejidad e interpretación: Costo $O(V+E)$. El resultado es una secuencia de ejecución segura donde ninguna tarea intentará iniciar antes de que sus prerrequisitos estén listos.

## Caso fuera del alcance

**Dijkstra con aristas de peso negativo:**
El contrato que se viola es la precondición matemática de Dijkstra: asume que una vez que extrae una distancia mínima vigente del heap, esta es definitiva y no existe una ruta futura que la reduzca pasando por algo más costoso. Un peso negativo rompe este invariante. La decisión técnica correcta es rechazar el problema respondiendo "ninguno de los estudiados" en lugar de inventar una solución (como cambiar los pesos a cero o usar valor absoluto), ya que alterar los datos destruye el modelo real del problema.

## Reflexión final

Durante el curso mi proceso cambió de la memorización aislada al análisis de operaciones. Antes intentaba vincular una palabra clave del enunciado ("ruta", "conectar") directamente a un algoritmo, o elegía una estructura por familiaridad. Ahora, mi proceso inicia validando el contrato (dirección y pesos) para encontrar la operación dominante del problema; con esa operación clara, es natural elegir la estructura de datos que la abarata (como un heap para extraer mínimos o Union-Find para conectar conjuntos) y el algoritmo que las combina.