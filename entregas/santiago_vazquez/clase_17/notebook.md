Pregunta inicial

Cuando todos los pendientes tienen la misma prioridad, necesitamos una cola (FIFO). Al introducir dos niveles de prioridad, necesitamos una deque para insertar elementos sin costo adicional por el frente (prioridad inmediata) o por el final (prioridad estándar).

1. Presentación de la clase

Cambia la necesidad de decidir dónde insertar cada elemento descubierto: si una mejora cuesta cero aristas, debe procesarse de inmediato (inicio); si cuesta una arista, se pospone al final del bloque actual.

2. Problema inicial con pop(0)

pop(0) obliga a desplazar los n-1 elementos restantes una posición a la izquierda en la memoria física. Una referencia directa al frente permite que la desconexión se realice reasignando un puntero en O(1).

3. Nodo y referencias

El valor es el dato en sí; el nodo es el contenedor físico que asocia el valor con sus referencias; y la estructura es la entidad encargada de controlar el acceso y mantener consistentes los punteros frente y final.

4. Lista ligada simple

La operación de encolar (insertar al final) sería extremadamente costosa (O(n)) si solo tuviéramos acceso directo al inicio de la lista, ya que obligaría a recorrer secuencialmente toda la cadena para encontrar el último nodo.

5. Cola ligada

Para asegurar que ambas operaciones sean de costo constante, el frente permite remover el primer elemento sin realizar desplazamientos, y el final permite acoplar un nuevo nodo directamente sin recorrer la lista.

6. Invariantes de colaAl desencolar el único elemento, las condiciones necesarias son: frente is None, final is None y un tamaño total igual a 0.

7. Operaciones manuales

Al desencolar A de la cadena A a B a C, la variable del frente cambia su referencia de A hacia B, mientras que la referencia final se mantiene apuntando sin cambios al nodo C.

8. Complejidad

Porque la estructura solo mantiene punteros directos al inicio y al final; buscar un valor aleatorio obliga a realizar un recorrido secuencial nodo por nodo desde el frente de la cola hasta encontrar la coincidencia.

9. BFS y cola

El orden de llegada FIFO garantiza un procesamiento nivel por nivel (capas), de modo que ningún vértice situado a una distancia d+1 pueda ser explorado antes de haber procesado todos los de distancia d.

10. Visitados al encolar

Si se marca al desencolar, un mismo nodo que es vecino de múltiples vértices en la capa actual será añadido varias veces a la cola, provocando una explosión de trabajo redundante y caminos duplicados en grafos densos.

11. Predecesores

Un simple mapa de retroceso (un diccionario de predecesores) que almacene el padre directo de cada nodo visitado es suficiente para trazar el camino inverso desde cualquier destino alcanzable hasta el origen.

12. Reconstrucción del camino

Un destino inalcanzable presentará un camino que corta su recorrido en un nodo sin predecesor antes de llegar al origen, mientras que una tabla corrupta provocará un ciclo infinito (el mismo nodo se visita dos veces en el rastreo).

13. Práctica guiada de BFS

El camino puede variar según la posición de los vecinos en la lista de adyacencia del nodo analizado, lo que altera qué vértice los descubre primero; sin embargo, todos los caminos alternativos mantendrán siempre el mismo costo mínimo.

14. Lista doblemente ligada

Obtenemos la capacidad de retirar elementos del extremo final en $O(1)$ sin recorrer la lista. La obligación es que al modificar un enlace, se actualicen concurrentemente los punteros siguiente del nodo izquierdo y anterior del nodo derecho.

15. Invariantes de lista doble

Se puede corroborar recorriendo la lista de inicio a fin acumulando las referencias de los nodos y luego haciendo el recorrido inverso comparando que para cada nodo visitado se cumpla que nodo.siguiente.anterior is nodo.

16. Deque ligada

La deque solo provee los mecanismos de entrada y salida eficientes en ambos extremos; el algoritmo es el que impone la disciplina del flujo de datos usando las inserciones y remociones convenientes.

17. Operaciones manuales de deque

Se debe verificar que el nuevo puntero de inicio de la deque sea B, que el enlace B.anterior sea reasignado a None, que el nodo A tenga sus enlaces anterior y siguiente en None, y que el tamaño se reduzca a 3.

18. Qué problema resuelve 0-1 BFS

BFS asume que todos los saltos añaden el mismo costo. Si existen aristas de peso 0, un camino con mayor número de saltos gratuitos puede ser globalmente más barato que una sola arista directa de costo 1.

19. Deque como estructura de prioridad

El peso de la arista determina el extremo: si la arista es gratuita (peso 0), el vértice se coloca al inicio para procesarse de inmediato; si cuesta 1, se pospone colocándolo al final de la deque.

20. Ejecución manual de 0-1 BFS

Cuando X mejora su distancia de 1 a 0, su valor en la tabla de distancias cambia a 0, su predecesor se actualiza al nodo que descubrió la mejora, y X se inserta en el extremo de inicio de la deque.

21. Implementación

Permite aislar por completo la lógica de punteros de las estructuras de la lógica de recorrido de grafos, haciendo que los errores de enlace sean detectados inmediatamente en pruebas unitarias unitarias y no en algoritmos complejos.

22. Casos límite

Porque los booleanos en Python heredan directamente de la clase entera, pero conceptualmente no representan un peso numérico válido de arista dentro del dominio de control del grafo y deben ser descartados.

23. Pruebas

Permite identificar fugas de referencias y enlaces antiguos mal limpiados que quedan activos cuando la estructura pasa por un estado transitorio vacío y se vuelve a poblar.

24. Comparación BFS, 0-1 BFS y Dijkstra

Un flujo de inserción secuencial e inmutable en un solo extremo (cola), una inserción bifronte dependiente de un costo binario inmediato (deque), y una extracción constante del mínimo elemento en un conjunto dinámico de costos (heap).

25. Cierre hacia Union-Find y Kruskal

¿Cómo podemos verificar de manera eficiente si la inclusión de una arista barata une dos vértices que ya pertenecen a la misma componente conexa, sin necesidad de realizar una búsqueda costosa en el grafo?