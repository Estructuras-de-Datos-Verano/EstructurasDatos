# Notebook Aristeo
## 1. Presentación de la clase
### ¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?
Una secuencia solo nos dice el orden, es más simpe de modelar pues basta con ordenar datos de una u otra forma como con pilas y colas, en cambio el modelado de relaciones nos dice como se conectan los datos entre sí, lo cual es más complejo.

---
## 2. Problemas motivadores CSES
### [BuildingRoads]
### 1. ¿Qué representa un nodo?
Una ciudad.
### 2. ¿Qué representa una arista?
Una carretera entre dos ciudades (existente).
### 3. ¿Es dirigido?
No, es no dirigido.
### 4. ¿Es ponderado?
No, sin pesos.
### 5. ¿Qué pregunta algorítmica aparece?

---
Identificar componentes conectados y añadir el número mínimo de carreteras para conectar todas las componentes (unión de componentes; DFS/BFS o UF).
### [CountingRooms]
### 1. ¿Qué representa un nodo?
Una casilla libre ('.') del tablero.
### 2. ¿Qué representa una arista?
Adyacencia entre casillas libres vecinas (4-direcciones).
### 3. ¿Es dirigido?
No, es no dirigido.
### 4. ¿Es ponderado?
No, sin pesos.
### 5. ¿Qué pregunta algorítmica aparece?
Contar componentes conectadas en la malla (nº de habitaciones) usando DFS/BFS.

---
### [Labyrint]
### 1. ¿Qué representa un nodo?
Una casilla libre (pasable) del laberinto.
### 2. ¿Qué representa una arista?
Movimiento entre casillas adyacentes (4-direcciones).
### 3. ¿Es dirigido?
No, es no dirigido (movimiento reversible).
### 4. ¿Es ponderado?
No, sin pesos (coste uniforme por paso).
### 5. ¿Qué pregunta algorítmica aparece?
Encontrar el camino más corto desde la entrada hasta la salida y reconstruir la ruta (BFS con reconstrucción de camino).

---
### [MessageRoute]
### 1. ¿Qué representa un nodo?:
Una ciudad.
### 2. ¿Qué representa una arista?
Una carretera entre dos ciudades.
### 3. ¿Es dirigido?
No, es no dirigido.
### 4. ¿Es ponderado?
No, sin pesos.
### 5. ¿Qué pregunta algorítmica aparece?
Hallar el camino más corto (mínimo número de aristas) entre dos nodos; usar BFS y reconstrucción de ruta.
## 3. Lectura de modelado
| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudad | Carretera entre ciudades | No | No | Encontrar cuántas carreteras adicionales se necesitan para conectar todas las ciudades (componentes conectados) |
| Counting Rooms | Casilla libre | Adyacencia entre casillas libres | No | No | Contar el número de habitaciones como componentes conectados |
| Labyrinth | Casilla libre pasable | Movimiento entre casillas adyacentes | No | No | Encontrar el camino más corto de la entrada a la salida y reconstruir la ruta |
| Message Route | Ciudad | Carretera entre ciudades | No | No | Encontrar el camino más corto entre dos ciudades (mínimo pasos) |

---
## 4. Conceptos básicos de grafos
### Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.

- Grafo dirigido: un mapa de rutas de avión entre aeropuertos donde cada vuelo tiene un sentido definido (origen → destino).
- Grafo no dirigido: una red de calles entre barrios donde el tránsito puede ir en ambos sentidos sin orientación fija.

---
## 5. Representaciones de grafos

### ¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?

Me parece más importante listar vecinos porque la mayoría de los algoritmos de grafos recorren los vecinos de cada nodo para explorar la estructura completa, buscar caminos o analizar componentes.
Preguntar si existe una arista es útil en casos puntuales, pero listar vecinos es la operación fundamental para navegar y procesar grafos.

---
## 6. Interfaz común

### ¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?

Conviene que ambas implementaciones tengan la misma interfaz porque así el código que usa el grafo no depende de la representación interna. Esto permite cambiar de lista de adyacencia a matriz de adyacencia sin modificar los algoritmos, facilita pruebas comparativas y hace posible reutilizar código con distintas implementaciones.

---
## 7. Implementación 1: `GrafoListaAdyacencia`

### ¿Por qué un `set` ayuda a evitar aristas duplicadas?

Un `set` no permite elementos repetidos, por lo que si se agrega la misma arista varias veces solo se conserva una copia en la lista de vecinos. Esto evita duplicados automáticos y mantiene la representación del grafo limpia y eficiente.

---
## 8. Implementación 2: `GrafoMatrizAdyacencia`

### ¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?

Cuando se agrega un vértice nuevo hay que ampliar la matriz para que tenga una fila y una columna extra. Esto significa extender cada fila existente con un `False` y luego añadir una nueva fila completamente `False` para el nuevo vértice.

---
## 9. Comparación

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Usa memoria proporcional a los arcos reales, es eficiente en grafos dispersos | Usa memoria cuadrática respecto a la cantidad de vértices, puede ser costosa en grafos grandes |
| Facilidad de implementación | Relativamente simple de implementar y extender | Un poco más compleja por la gestión de índices y redimensionamiento |
| Consultar vecinos | Muy eficiente: basta leer la lista/ conjunto de vecinos | Menos eficiente: hay que revisar toda una fila de la matriz |
| Consultar si existe arista | Puede ser eficiente con `set`, pero depende de la representación de vecinos | Muy eficiente: acceso directo a la celda de la matriz |
| Grafos dispersos | Buena elección, ocupa poca memoria y es rápido para iterar vecinos | Mala elección, desperdicia mucha memoria con muchas celdas vacías |
| Grafos densos | Aún funciona bien, aunque la lista puede crecer mucho | Buena elección, la matriz representa bien muchas aristas |

---
## 11. Convertir implementación propia a NetworkX

### ¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?

Conviene poder convertir una implementación propia a una biblioteca externa porque permite validar y visualizar la estructura con herramientas ya desarrolladas, sin perder el aprendizaje de la implementación interna. También facilita integrar el grafo en otros proyectos y comparar fácilmente resultados entre la solución propia y la biblioteca.

---
## 12. Diseño de pruebas

### Prueba 1: crear grafo y agregar aristas
Construir un grafo vacío, agregar vértices y aristas, y verificar que `cantidad_vertices()` y `cantidad_aristas()` devuelvan los valores esperados. Esta prueba verifica el comportamiento público de construcción del grafo y el conteo correcto de aristas sin depender de detalles internos.

### Prueba 2: evitar aristas duplicadas
Agregar la misma arista `A`--`B` dos veces y luego verificar que `cantidad_aristas()` sea 1. Esta prueba asegura que la implementación no duplica aristas cuando se agregan repetidas veces, un comportamiento público importante para grafos no dirigidos.

---
## 13. Patrón descubierto

### ¿Qué significa el patrón de modelado de relaciones?
El patrón de modelado de relaciones consiste en identificar objetos y las conexiones entre ellos, y representar esas conexiones como un grafo. En vez de ver solo datos en orden, se busca capturar relaciones directas entre elementos usando nodos y aristas, y elegir una representación adecuada como lista de adyacencia o matriz de adyacencia.

---
## 14. Cierre

### 1. ¿Qué ganamos al modelar relaciones como grafo?
Modelar relaciones como grafo nos permite representar y analizar conexiones entre entidades de forma explícita, encontrar rutas, detectar componentes y responder preguntas sobre la estructura del sistema en lugar de solo procesar datos secuenciales.

### 2. ¿Cuándo usarías lista de adyacencia?
Usaría lista de adyacencia cuando el grafo es disperso o cuando necesito recorrer vecinos de cada nodo con frecuencia, ya que es eficiente en memoria y en iterar las conexiones existentes.

### 3. ¿Cuándo usarías matriz de adyacencia?
Usaría matriz de adyacencia cuando el grafo es denso o necesito consultas rápidas de existencia de arista entre pares de vértices, porque el acceso es directo y constante.

### 4. ¿Qué puede ocultar una visualización?
Una visualización puede ocultar detalles importantes como direccionalidad, pesos, aristas múltiples y la estructura exacta de conexiones en grafos grandes, dando una impresión simplificada de la red.

### 5. ¿Qué algoritmo necesitaremos para recorrer el grafo?
Necesitaremos un algoritmo de recorrido como DFS o BFS para explorar los nodos y aristas del grafo, visitar vecinos y analizar componentes o caminos.
