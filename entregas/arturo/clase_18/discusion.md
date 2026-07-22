# Discusión técnica — Clase 18

## 1. Problema
¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?


Caminos mínimos (ej. Dijkstra) optimiza la distancia total desde un nodo origen hacia los demás, minimizando el costo individual de cada ruta específica. El Árbol de Expansión Mínima (MST), por el contrario, busca minimizar el peso global requerido para mantener conectados todos los vértices de la red, sin importar si la ruta resultante entre dos nodos individuales no es la más corta o directa.

## 2. Árbol de expansión
¿Por qué una solución tiene \(V-1\) aristas?


para conectar un conjunto de $V$ vértices de forma continua sin formar ningún ciclo, necesitas matemáticamente exactamente $V-1$ aristas. Una arista de menos deja componentes aisladas (desconexión); una arista de más inevitablemente cerrará un ciclo.

## 3. Ciclos
¿Por qué se rechaza una arista cuyos extremos ya están conectados?


Porque aceptarla violaría la propiedad acíclica de un árbol. Si los dos extremos de la arista ya pertenecen a la misma componente conexa (es decir, tienen el mismo representante en Union-Find), significa que ya existe un camino que los comunica. Añadir esta arista solo crearía un ciclo redundante, aumentando el costo total del árbol innecesariamente.

## 4. Componentes
¿Qué representa una componente en Union-Find?


Representa un conjunto disjunto de vértices que ya han sido interconectados entre sí mediante las aristas que el algoritmo ha aceptado hasta ese momento. A nivel de estructura de datos, es un árbol n-ario lógico en memoria donde todos los nodos terminan apuntando (directa o indirectamente) a un único nodo raíz.

## 5. Representantes
¿Qué significa la raíz de un elemento?


Es el "identificador canónico" de su componente conexa. Si ejecutamos la operación de búsqueda sobre dos nodos diferentes y ambos devuelven la misma raíz, sabemos con certeza ($\mathcal{O}(1)$ amortizado) que pertenecen a la misma red. Se identifica fácilmente porque es el único nodo que se apunta a sí mismo (padre[i] == i).

## 6. `find`
¿Qué operación realiza `find`?


Escala recursivamente (o iterativamente) por la cadena de punteros padre desde el nodo consultado hasta encontrar a su representante supremo. En una implementación optimizada para producción, esta operación también realiza la mutación estructural conocida como "compresión de caminos" durante su ejecución.

## 7. `union`
¿Por qué conviene que `union` devuelva un booleano?


Porque actúa como un elegante predicado de control de flujo para el algoritmo de Kruskal. Si union devuelve True, la fusión ocurrió con éxito y la arista es válida para el MST. Si devuelve False, los nodos ya compartían raíz (detectando un ciclo inminente) y la arista puede ser descartada en la misma línea de código, sin necesidad de comprobaciones redundantes.

## 8. Compresión
¿Qué cambia y qué no cambia con la compresión de caminos?


ni idea

## 9. Unión por tamaño
¿Por qué se coloca el árbol pequeño debajo del grande?


Para mantener el árbol balanceado y evitar el peor caso donde degenere en una lista enlazada (lo que daría tiempos de consulta $\mathcal{O}(N)$). Al anexar el árbol con menor cantidad de nodos bajo la raíz del que tiene mayor volumen, garantizamos que la profundidad máxima de la estructura crezca de forma estrictamente logarítmica.

## 10. Invariantes
¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?


Identidad de raíz: Un nodo $i$ es raíz si y solo si padre[i] == i


Precisión de volumen: En el arreglo de tamaños, el valor almacenado en el índice correspondiente a una raíz debe reflejar con exactitud la suma de todos los nodos de ese conjunto disjunto


Persistencia de pertenencia: Ninguna heurística de optimización (como la compresión) puede mover a un nodo hacia un conjunto diferente al que fue asignado.
## 11. Kruskal
¿Cuál es la operación dominante de Kruskal?


El ordenamiento inicial de las aristas según su peso. Mientras que las comprobaciones de conectividad con Union-Find son casi instantáneas, ordenar la lista requiere un esfuerzo algorítmico mucho mayor.

## 12. Grafo desconectado
¿Por qué Kruskal puede terminar con un bosque?


Si el grafo original carece de puentes suficientes para unir a todos los nodos (es decir, viene pre-dividido en múltiples islas), Kruskal procesará y agotará ordenadamente todas las aristas válidas sin lograr conectarlos a una única raíz. El algoritmo termina su ejecución normalmente, pero entrega un "bosque de expansión mínima" con un conteo de aristas aceptadas estrictamente menor a $V - 1$.


## 13. Pesos negativos
¿Por qué Kruskal acepta pesos negativos y Dijkstra no?


Dijkstra depende del invariante de monotonicidad: asume que al avanzar por las aristas, el costo acumulado siempre aumenta, garantizando que la primera vez que visita un nodo, encontró su ruta óptima. Kruskal usa una estrategia greedy global; simplemente ordena todas las aristas de menor a mayor. Los pesos negativos no rompen nada, sencillamente quedan al principio del arreglo, se evalúan primero y se integran al árbol si no forman ciclo.

## 14. Empates
¿Por qué puede haber varios árboles de expansión mínima?


Cuando en la red existen múltiples aristas que tienen exactamente el mismo costo, el algoritmo de ordenamiento (sort) determina de forma más o menos arbitraria cuál procesar primero. Si ambas conectan distintos segmentos válidos sin crear ciclos, elegirlas en distinto orden producirá topologías (dibujos de árbol) diferentes, aunque todas tendrán matemáticamente idéntico costo total.

## 15. Complejidad
¿Qué parte domina la complejidad de Kruskal?


El sorting inicial. Evaluar $E$ aristas con Union-Find toma un tiempo amortizado de $\mathcal{O}(E \cdot \alpha(V))$, donde $\alpha$ (la función inversa de Ackermann) es virtualmente una constante $\le 4$. En cambio, ordenar el arreglo de aristas exige invariablemente $\mathcal{O}(E \log E)$. El peso asintótico recae en la ordenación.

## 16. Comparación
Compara cola, deque, heap y Union-Find según la operación que optimizan.


Cola (Queue): Optimiza el procesamiento secuencial (FIFO) en $\mathcal{O}(1)$, ideal para enrutamiento por niveles o BFS


Deque: Optimiza inserciones y extracciones constantes por ambos extremos, crucial en ventanas deslizantes o BFS 0-1


Heap (Priority Queue): Optimiza el acceso y la extracción continua del valor mínimo (o máximo) dinámico en $\mathcal{O}(\log N)$, esencial para Dijkstra o Prim


Union-Find: Optimiza exclusivamente consultas dinámicas de conectividad ("¿A y B están conectados?") y la fusión segura de conjuntos disjuntos en tiempo casi lineal.
## 17. Producción
¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?


En lenguajes de bajo nivel como C/C++, causaría un acceso fuera de los límites de memoria (Out-of-Bounds), resultando en vulnerabilidades de seguridad, corrupción de datos o un segmentation fault. En lenguajes de alto nivel como Python, un índice negativo accedería silenciosamente a los elementos desde el final del arreglo (padre[-1]), corrompiendo por completo la lógica matemática de las uniones sin emitir errores de ejecución, creando bugs muy difíciles de rastrear


## 18. Cierre
¿Qué estructura se necesitaría para procesar tareas según dependencias?


Se requeriría modelar las tareas como un Grafo Dirigido Acíclico (DAG) y aplicar un Ordenamiento Topológico. A nivel de estructuras de datos específicas, la implementación estándar (como el algoritmo de Kahn) utiliza un Arreglo de grados de entrada (in-degrees) para rastrear cuántas dependencias bloquean cada tarea, combinado con una Cola (Queue) para ir procesando e iterando sobre las tareas cuyo grado de entrada llega a cero
