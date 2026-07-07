# Discusión Técnica - Práctica 09: Grafos y Representaciones

## 1. De secuencias a relaciones
El cambio de paradigma desde estructuras de datos secuenciales (como listas, arreglos, pilas y colas) hacia los grafos es importante. Mientras que una secuencia establece un orden lineal implícito o explícito dominado por índices discretos o por el orden temporal de inserción, un grafo se desvincula de la linealidad para capturar conexiones multidireccionales arbitrarias entre objetos.

## 2. Problemas CSES
A partir del análisis de la suite de problemas de CSES, podemos categorizar el modelado de relaciones según la naturaleza de sus nodos y aristas:
* **Building Roads**: Los nodos representan ciudades y las aristas representan carreteras no dirigidas ni ponderadas. La meta algorítmica implícita consiste en identificar las componentes conexas del grafo y determinar el número mínimo de aristas requeridas para unificarlas todas en una sola componente.
* **Counting Rooms**: Los nodos representan celdas transitables  en una cuadrícula bidimensional, y las aristas representan la adyacencia espacial (norte, sur, este, oeste) entre celdas vacías. Es un grafo no dirigido y no ponderado cuyo objetivo es contabilizar el número de componentes "contiguos independientes.
* **Labyrinth**: Similar a *Counting Rooms*, los nodos son celdas de una cuadrícula, pero el foco cambia hacia la buscar el camino más corto entre un nodo de inicio 'A' y uno de destino 'B'.
* **Message Route**: Los nodos modelan computadoras de una red y las aristas representan cables de comunicación biunívocos.El problema resulta de encontrar la ruta más corta que conecte computadora de inicio-fin (queda claro que es dirigido).
## 3. Elección de representación
La selección de la estructura de datos interna impacta de manera crítica el rendimiento espacio-temporal del sistema:
* **GrafoListaAdyacencia**: Implementado mediante un diccionario de conjuntos , almacenando exclusivamente la información de las conexiones existentes. Operaciones como listar los vecinos de un nodo se ejecutan en tiempo constante O(1) para acceder a la clave del diccionario, lo que la convierte en la opción ideal para **grafos dispersos**.
* **GrafoMatrizAdyacencia**: Estructurado mediante una tabla bidimensional de booleanos tipo matriz, independientemente de si existen o no aristas. Su mayor virtud radica en que la verificación de existencia de una arista se reduce a un acceso indexado de O(1). Es la mejor opción para **grafos densos** o cuando la operación predominante sea consultar existencia de aristas específicas.

## 4. Polimorfismo
El diseño implementado se apoya firmemente en la programación orientada a objetos mediante la clase abstracta `GrafoAbstracto`. Al definir un contrato polimórfico unificado con métodos públicos comunes logramos olvidarnos de detalles internos de bajo nivel. Esto significa que un algoritmo de recorrido (como BFS o DFS) o una función de infraestructura (como `convertir_a_networkx` o `guardar_visualizacion_grafo`) pueden consumir cualquier instancia que herede de `GrafoAbstracto` sin importar si por debajo se gestiona un diccionario dinámico o una matriz booleana.

## 5. NetworkX
La integración de la biblioteca externa NetworkX ilustra la diferencia conceptual entre la **estructura de datos abstracta** y su **representación gráfica**. 

## 6. Pruebas
El aseguramiento de calidad mediante pruebas unitarias (`pytest`) debe validar de forma exclusiva el comportamiento del contrato público y no los estados internos protegidos. Esto asegura que si la lógica interna de `GrafoMatrizAdyacencia` sufre una refactorización de optimización en el crecimiento de sus listas internas, los casos de prueba sigan siendo válidos. Las pruebas clave deben garantizar escenarios límite como: el comportamiento ante grafos vacíos, la conmutatividad de las aristas no dirigidas (asegurar que si existe la arista $A-B$, automáticamente se refleje la vecindad bidireccional), el bloqueo de duplicados, y la consistencia en el cálculo de las métricas agregadas (`cantidad_vertices` y `cantidad_aristas`).

## 7. Patrón descubierto
El patrón que hemos identificado es el **Modelado de Relaciones**. Este patrón se activa en el momento en que la naturaleza de una entidad no viene dada por un valor intrínseco aislado, sino por vínculos que sostienen su entorno.
## 8. Pregunta abierta
¿Qué tipo de algoritmo puede recorrer, en el mejor caso promedio, de forma MÁS óptima en términos de tiempo y memoria el grafo y consultar datos?