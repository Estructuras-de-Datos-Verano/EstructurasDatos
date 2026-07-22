# Discusión Técnica - Práctica 09: Grafos y Representaciones

## 1. De secuencias a relaciones
El cambio de paradigma desde estructuras de datos secuenciales (como listas, arreglos, pilas y colas) hacia los grafos es importante. Una secuencia tiene un órden explícita de operaciones mientras que el grafo tiene relaciones multidireccionales.
## 2. Problemas CSES

* **Building Roads**: Los nodos representan ciudades y las aristas representan carreteras no dirigidas ni ponderadas. La meta consiste en identificar las componentes "contiguas" del grafo y determinar el número mínimo de aristas requeridas para unificarlas todas.
* **Counting Rooms**: Los nodos representan celdas transitables  en una cuadrícula bidimensional, y las aristas representan la adyacencia espacial (norte, sur, este, oeste) entre celdas vacías. Es un grafo no dirigido y no ponderado cuyo objetivo es contabilizar el número de componentes "contiguos independientes.
* **Labyrinth**: Similar a Counting Rooms, los nodos son celdas de una cuadrícula, pero el foco cambia hacia buscar el camino más corto entre un nodo de inicio 'A' y uno de destino 'B'.
* **Message Route**: Los nodos modelan computadoras de una red y las aristas representan cables de comunicación biunívocos.El problema resulta de encontrar la ruta más corta que conecte computadora de inicio-fin (queda claro que es dirigido).
## 3. Elección de representación
* **GrafoListaAdyacencia**: Implementado mediante un diccionario de conjuntos , almacenando exclusivamente la información de las conexiones existentes. Operaciones como listar los vecinos de un nodo se ejecutan en tiempo constante O(1) para acceder a la clave del diccionario, lo que la convierte en la opción ideal para **grafos dispersos**.
* **GrafoMatrizAdyacencia**: Estructurado mediante una tabla bidimensional de booleanos tipo matriz, independientemente de si existen o no aristas. Su mayor virtud radica en que la verificación de existencia de una arista se reduce a un acceso indexado de O(1). Es la mejor opción para **grafos densos** o cuando la operación predominante sea consultar existencia de aristas específicas.

## 4. Polimorfismo
El diseño se apoya firmemente en la programación orientada a objetos mediante la clase abstracta `GrafoAbstracto`. Al definir un contrato polimórfico con métodos públicos comunes logramos olvidarnos de detalles internos. Esto significa que un algoritmo de recorrido (como BFS o DFS) o una función de infraestructura (como "convertir_a_networkx" o "guardar_visualizacion_grafo") pueden consumir cualquier instancia que herede de "GrafoAbstracto" sin importar si por debajo se gestiona un diccionario dinámico o una matriz booleana.

## 5. NetworkX
La integración de la biblioteca externa NetworkX ilustra la diferencia conceptual entre la **estructura de datos abstracta** y su **representación gráfica**. 

## 6. Pruebas
 Las pruebas garantizan un comportamiento idóneo en escenarios límite como: el comportamiento ante grafos vacíos, la conmutatividad de las aristas no dirigidas (asegurar que si existe la arista A-B, automáticamente se refleje la vecindad bidireccional), el bloqueo de duplicados, y la consistencia en el cálculo de las cantidades de aristas/vértices.

## 7. Patrón descubierto
El patrón que hemos identificado es el **Modelado de Relaciones**. Este patrón se activa en el momento en que la naturaleza de una entidad no viene dada por un valor intrínseco aislado, sino por vínculos que sostienen su entorno.
## 8. Pregunta abierta
¿Qué tipo de algoritmo puede recorrer, en el mejor caso promedio, de forma óptima en términos de tiempo y memoria el grafo y consultar datos?