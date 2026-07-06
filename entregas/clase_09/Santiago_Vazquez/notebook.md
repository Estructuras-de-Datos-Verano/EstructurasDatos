# notebook.md

## 1. Presentación de la clase

Modelar una secuencia implica un orden lineal y secuencial, donde los elementos van uno detrás de otro. En cambio, modelar relaciones nos lleva a una estructura no lineal y más compleja, donde un mismo objeto puede estar conectado con múltiples entidades en distintas direcciones de forma simultánea.

## 2. Problemas motivadores CSES y 3. Lectura de modelado

| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudades | Carreteras que unen ciudades | No | No | Conteo de componentes conexas |
| Counting Rooms | Casillas de piso | Adyacencia espacial (norte, sur, este, oeste) | No | No | Conteo de componentes conexas |
| Labyrinth | Casillas libres | Movimiento válido entre dos casillas | No | No | Encontrar el camino más corto |
| Message Route | Computadoras | Conexiones de red entre equipos | No | No | Encontrar el camino más corto |


## 4. Conceptos básicos de grafos

* **Grafo dirigido:** El mapa curricular de la carrera de matemáticas aplicadas. Si Álgebra Lineal I es requisito para Álgebra Lineal II, existe una relación estricta de orden y dirección; no puedes cursar la segunda sin la primera.

* **Grafo no dirigido:** Un tratado de libre comercio bilateral entre varios países. Si el país A tiene libre comercio con el país B, el país B naturalmente lo tiene con el A.

## 5. Representaciones de grafos

Para los algoritmos que solemos implementar en estructuras de datos, listar los vecinos es la operación más importante y frecuente. La mayoría de los algoritmos de exploración consisten en visitar un estado y expandirse sistemáticamente hacia sus nodos adyacentes para continuar la búsqueda, en lugar de consultar pares de conexiones aleatorias.

## 6. Interfaz común

Definir una interfaz común nos permite aprovechar el polimorfismo. Desde el punto de vista algorítmico, podemos escribir un proceso de exploración una sola vez apoyándonos en los métodos abstractos. Así, el código funcionará perfectamente sin importar si en la memoria el grafo está construido con listas de adyacencia o con matrices.

## 7. Implementación 1: `GrafoListaAdyacencia`

Por su misma definición axiomática, un conjunto (`set`) no permite tener elementos duplicados. Al intentar insertar un nodo vecino que ya existe en el conjunto, la estructura ignora la operación silenciosamente, lo cual es perfecto para mantener nuestro modelo como un grafo simple sin aristas redundantes.

## 8. Implementación 2: `GrafoMatrizAdyacencia`

Al agregar un vértice, la dimensionalidad del espacio aumenta. Debemos agregar una nueva fila de booleanos (todos inicializados en falso) para representar las posibles conexiones de este nuevo vértice, y además debemos añadir una nueva columna al final de todas las filas que ya existían.

## 9. Comparación

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Proporcional a los nodos y aristas | Proporcional al cuadrado de los nodos |
| Facilidad de implementación | Directa, los diccionarios son muy naturales | Requiere mapear nombres a índices numéricos |
| Consultar vecinos | Muy rápido, se devuelve el conjunto de inmediato | Lento, requiere recorrer toda la fila de la matriz |
| Consultar si existe arista | Implica buscar dentro del conjunto del nodo | Instantáneo, acceso directo a la celda en tiempo constante |
| Grafos dispersos | Altamente eficiente y compacta | Desperdicia mucha memoria almacenando ceros lógicos |
| Grafos densos | Aceptable, aunque con algo de sobrecarga | Extremadamente eficiente tanto en almacenamiento como en consultas |

## 11. Convertir implementación propia a NetworkX

Delegar tareas complejas nos permite enfocarnos en la algoritmia base. Nos conviene poder trasladar nuestras estructuras matemáticas puras a bibliotecas externas para poder aprovechar sus potentes rutinas de cálculo de visualización (layouts) y análisis estadístico sin tener que programar esas herramientas geométricas desde cero.

## 12. Diseño de pruebas

1. **Prueba de vértice aislado:** Verificar que al agregar un vértice sin declarar aristas, el método que consulta vecinos devuelva un conjunto vacío. Esto asegura que la inicialización no genera conexiones fantasma.
2. **Prueba de arista duplicada:** Agregar exactamente la misma arista entre dos nodos un par de veces y verificar que el conteo total de aristas se mantenga en uno, validando la integridad del grafo simple.

## 13. Patrón descubierto

El patrón de modelado de relaciones consiste en abstraer las entidades de un sistema complejo a simples puntos (nodos) y sus interacciones a líneas que los conectan (aristas). Esto transforma problemas logísticos, espaciales o de redes en objetos topológicos sobre los cuales podemos calcular distancias y caminos.

## 14. Cierre

1. Ganamos marco teórico al reducir distintos problemas a grafos, podemos resolverlos usando las mismas herramientas algorítmicas sin importar su contexto de origen.
2. Usaría una lista de adyacencia cuando el grafo es muy disperso, como en el modelado de redes de carreteras, donde cada nodo se conecta a un número ínfimo de otros nodos en relación al total.
3. Usaría una matriz de adyacencia cuando el grafo es sumamente denso, o cuando necesite operar con álgebra lineal, como al calcular los autovalores del grafo.
4. Una visualización sin rigor analítico puede ocultar distancias reales y direccionalidad. El dibujo en 2D podría hacer parecer que dos nodos están cerca geométricamente, aunque topológicamente la distancia en aristas sea inmensa.
5. Necesitaremos recurrir a los clásicos algoritmos de exploración sistemática de grafos, específicamente la búsqueda en anchura (BFS) y la búsqueda en profundidad (DFS).