1. Nodo y lista ligada

    El Nodo: Es la unidad atómica y física de almacenamiento. Su única responsabilidad es contener un dato útil (el valor) y uno o más enlaces lógicos (punteros) que apuntan hacia otros nodos de su mismo tipo. No tiene noción del tamaño de la colección ni del contexto global.

    La Lista Ligada: Es el contenedor o estructura de control abstracta que administra la secuencia de nodos. Se encarga de definir el punto de entrada (por ejemplo, el puntero al nodo inicial cabeza), mantener el tamaño total del conjunto y proveer la interfaz pública de operaciones de inserción, búsqueda y eliminación que aseguran la consistencia global de la estructura.

2. Cola ligada

    Acceso al frente: Permite retirar (desencolar) elementos en tiempo constante O(1) sin tener que buscar o desplazar elementos restantes en memoria física.

    Acceso al final: Permite añadir (encolar) nuevos elementos de forma directa y en O(1). Sin la referencia directa al último nodo, cada inserción nos obligaría a realizar un recorrido secuencial de todos los nodos de la estructura partiendo desde el frente, elevando el costo de encolar a un ineficiente O(n).

3. Invariantes de cola vacía

Cuando una cola se encuentra vacía, se deben cumplir estrictamente las siguientes condiciones de estado:

    El puntero de lectura inicial no referencia a ningún elemento en memoria: frente is None.

    El puntero de inserción final no mantiene referencias huérfanas: final is None.

    El contador interno del tamaño es exactamente cero: _tamano == 0.

    Al intentar realizar un descarte o lectura se debe levantar de inmediato una excepción de tipo IndexError.

4. Lista simple y lista doble

    Ventajas: La referencia anterior permite la navegación bidireccional por la lista. Esto hace posible la eliminación de nodos desde el extremo final en tiempo constante O(1), así como operaciones de borrado de nodos intermedios sin necesidad de rastrear de manera previa el elemento predecesor.

    Costos: Cada nodo requiere una variable adicional (anterior), incrementando el consumo de memoria en un 50% por nodo (un entero o puntero extra). Además, la lógica de inserción y remoción se vuelve más compleja y propensa a fallos, ya que cada operación requiere reasignar el doble de punteros lógicos de forma atómica.

5. Deque

    La interfaz de una deque exige inserciones y remociones eficientes (en tiempo O(1)) tanto por el inicio como por el final.

    Una lista doblemente ligada cumple perfectamente este requerimiento porque expone referencias directas a ambos extremos (inicio y final) y sus nodos permiten desenganchar elementos por atrás o por adelante de manera inmediata, eliminando la necesidad de realizar costosos barridos secuenciales.

6. Complejidad de pop(0) en listas de Python

    Las listas por defecto en Python (list) están implementadas internamente como arreglos dinámicos contiguos en memoria, no como listas ligadas.

    Al remover el primer elemento utilizando .pop(0), el espacio de memoria que este ocupaba queda libre. Para mantener la contigüidad física del arreglo, Python se ve obligado a desplazar manualmente todos los n−1 elementos restantes una posición a la izquierda en memoria. Esto hace que la remoción en el frente sea una operación de costo lineal O(n) y no O(1).

7. Marcado de visitados al encolar en BFS

    Momento de marcado: En BFS clásico, los nodos deben marcarse como visitados inmediatamente al momento de ser encolados, no al ser desencolados.

    Razón: Si se posterga el marcado hasta que el nodo es extraído de la cola, un vértice vecino común a múltiples nodos de la capa actual será añadido de manera redundante a la cola tantas veces como adyacencias tenga. En grafos densos o altamente interconectados, esto causa una explosión exponencial en el uso de memoria y procesamiento redundante.

8. Responsabilidad del mapa de predecesores

    El mapa de predecesores actúa como una estructura de "retroceso" que almacena, para cada nodo descubierto, cuál fue el vértice inmediato anterior desde el cual fue alcanzado.

    Su única responsabilidad es registrar la paternidad de los nodos durante la exploración. Esto permite desacoplar la fase de búsqueda de la fase de reconstrucción, haciendo posible trazar el camino mínimo de regreso al origen únicamente cuando el usuario lo solicita.

9. Reutilización de reconstrucción de caminos

    La reconstrucción de un camino es un proceso agnóstico a la forma en que se descubrió la ruta óptima. Ambos algoritmos, BFS (en grafos sin pesos) y Dijkstra (en grafos con pesos no negativos), guardan la estructura de caminos óptimos exactamente del mismo modo: una colección ordenada de apuntadores directos (nodo: predecesor).

    Dado que el grafo de predecesores resultante es en ambos casos un árbol de caminos mínimos, el recorrido inverso desde el destino hasta el origen sigue exactamente las mismas reglas de reconstrucción, lo que permite que una sola función utilitaria sirva para ambos.

10. Inserciones al inicio en 0-1 BFS

    En el algoritmo 0-1 BFS, cuando descubrimos una arista de costo 0, significa que podemos alcanzar este nuevo nodo sin añadir penalización de distancia al costo acumulado actual.

    Al insertarlo al inicio de la deque, garantizamos que se procesará inmediatamente en el lote de la capa actual, resolviendo de forma óptima los caminos más cortos de manera similar a como lo haría una cola de prioridad, pero sin incurrir en costos logarítmicos de ordenamiento.

11. Comparación de algoritmos de búsqueda
Característica	BFS (Clásico)	0-1 BFS	Dijkstra
Pesos permitidos	Uniformes (sin pesos o todos iguales)	Únicamente binarios: 0 y 1	Cualesquiera pesos no negativos (≥0)
Estructura clave	Cola simple (FIFO)	Deque ligada	Cola de prioridad (Min-Heap)
Complejidad	O(V+E)	O(V+E)	O((V+E)logV)
12. Elección de estructura por operación dominante

    Cola (FIFO): Elegida cuando la operación dominante es la inserción y extracción puramente secuencial y por extremos opuestos, donde el orden temporal determina la prioridad (adecuado para explorar niveles uniformes).

    Deque: Elegida cuando se requiere flexibilidad para alternar operaciones de entrada/salida en ambos extremos. Es la estructura dominante cuando hay decisiones binarias inmediatas (prioridad máxima al inicio, prioridad regular al final).

    Heap: Elegida cuando la operación dominante es la extracción dinámica y constante del elemento con el valor mínimo absoluto en un conjunto de prioridades continuamente cambiantes.

13. collections.deque en entornos de producción

    Implementación en C: La clase nativa collections.deque de Python está escrita y optimizada directamente en C. Utiliza bloques de memoria fijos (un arreglo de punteros a bloques), lo que otorga un rendimiento de caché y de CPU órdenes de magnitud más rápido que cualquier implementación pura en Python.

    Seguridad y robustez: Cuenta con un manejo óptimo de la memoria física, está altamente probada contra condiciones de carrera, soporta un límite de tamaño máximo (maxlen) e implementa internamente optimizaciones críticas que evitan la fragmentación del montículo.

14. Riesgos de referencias en listas doblemente ligadas

Los errores más peligrosos al manipular punteros en listas doblemente ligadas ocurren durante la desconexión o inserción de nodos intermedios:

    Fugas de memoria (Memory Leaks): Olvidar limpiar el puntero anterior o siguiente de un nodo que ha sido extraído mantiene dicho nodo vivo en el recolector de basura de Python, consumiendo memoria de forma silenciosa.

    Ciclos de referencias infinitos: Conectar incorrectamente el puntero siguiente de un nodo hacia sí mismo o hacia su predecesor inmediato sin actualizar el enlace simétrico opuesto. Esto provoca bucles infinitos en cualquier función iterativa de lectura, bloqueando por completo la ejecución del programa.

15. Cierre: Pesos de arista 0, 1 y 2

    Estructura recomendada: Para pesos estrictos de valor 0, 1 y 2, la estructura ideal sigue siendo una Deque utilizando una variación del algoritmo modificada, o bien, una Cola de prioridad simplificada basada en K+1 colas simples (donde K=2 es el peso máximo, requiriendo 3 colas).

    Justificación de por qué 0-1 BFS no se aplica directamente: El algoritmo 0-1 BFS clásico asume que no puede haber un elemento en la deque que tenga una diferencia de distancia superior a 1 respecto al nodo actualmente bajo exploración. Al introducir aristas de peso 2, esta regla se rompe. Si utilizáramos una deque estándar insertando elementos al final para peso 1 y peso 2, perderíamos el orden secuencial de distancias que asegura la optimalidad, produciendo resultados incorrectos. Se requeriría al menos un sistema de colas múltiples o un Heap para garantizar el orden de distancias mayores a 1.