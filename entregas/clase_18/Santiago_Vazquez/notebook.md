# Respuestas del notebook — Clase 18

## Pregunta inicial

¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?
Ordenando las aristas de menor a mayor costo y agregando cada una al conjunto final solo si no conecta dos nodos que ya pertenecen a la misma componente.

## Secciones 1–25

### 1. Presentación de la clase
Esperamos obtener un árbol de expansión mínima. Se diferencia en que conecta todos los nodos de la red optimizando el costo total de las conexiones, mientras que el camino mínimo optimiza la distancia desde un único origen específico.

### 2. Recuperación de estructuras anteriores
La operación de verificar de manera eficiente si dos nodos ya se encuentran conectados en la misma componente para evitar la formación de ciclos.

### 3. Nueva pregunta: conectar toda la red
Porque aceptar aristas por su bajo costo sin validación puede generar ciclos redundantes y dejar componentes de la red completamente aisladas entre sí.

### 4. Dijkstra frente a Kruskal
Dijkstra optimiza la distancia individual desde un origen específico. Kruskal optimiza el costo total acumulado de las conexiones en toda la red y no requiere ningún origen.

### 5. Árboles de expansión
Cada unión efectiva reduce en uno el número de componentes conexas iniciales. Para unir las $V$ componentes aisladas en un solo árbol se requieren exactamente $V-1$ uniones efectivas.

### 6. Por qué evitar ciclos
Necesitamos saber si los extremos $u$ y $v$ ya se encuentran conectados dentro de la misma componente del bosque de expansión mínima seleccionado.

### 7. Componentes conexas
Dos conjuntos disjuntos de la partición se fusionan en un único conjunto que agrupa a todos sus elementos bajo un mismo representante.

### 8. Necesidad de Union-Find
Porque nos permite decidir si aceptamos una arista y actualizar la estructura en un único paso atómico, evitando consultas y actualizaciones redundantes.

### 9. Representación mediante padres
Una posición en el arreglo de padres actúa como raíz si el valor guardado coincide con su propio índice, es decir, `padre[i] == i`.

### 10. Operación find
Porque Python permite la indexación negativa desde el final de la lista, lo que causaría consultas accidentales de elementos incorrectos sin levantar un error directo.

### 11. Operación union
Se podrían crear ciclos internos en la estructura o perder la propiedad de que cada cadena de padres termine correctamente en una única raíz válida.

### 12. Invariantes
Viola el invariante de que no existen ciclos (salvo el lazo raíz-padre), ya que los índices 0 y 1 se apuntan mutuamente y la cadena nunca terminaría en una raíz.

### 13. Compresión de caminos
Cambia la estructura del árbol apuntando los nodos visitados directo a la raíz para aplanar la jerarquía; permanecen iguales la partición lógica, los tamaños y el número de componentes.

### 14. Unión por tamaño
Al conectar el árbol de menor tamaño bajo la raíz del mayor, limitamos el crecimiento de la altura máxima a un comportamiento logarítmico.

### 15. Ejecución manual de Union-Find

| Operación | raíces | efectiva | padres | tamaños en raíces | componentes |
| --- | --- | --- | --- | --- | ---: |
| inicio | — | — | `[0,1,2,3,4,5]` | seis unos | 6 |
| union(0,1) | 0 / 1 | sí | `[0,0,2,3,4,5]` | raíz 0: 2 | 5 |
| union(2,3) | 2 / 3 | sí | `[0,0,2,2,4,5]` | raíz 2: 2 | 4 |
| union(1,3) | 0 / 2 | sí | `[0,0,0,2,4,5]` | raíz 0: 4 | 3 |
| union(0,3) | 0 / 0 | no | `[0,0,0,2,4,5]` | raíz 0: 4 | 3 |

*   `find(3)` devuelve `0`.
*   `tamano_componente(1)` devuelve `4`.
*   `conectados(0,4)` devuelve `False`.

### 16. Algoritmo de Kruskal
Si la unión es efectiva (`True`), Kruskal acepta la arista y la añade al árbol acumulando su peso. Si devuelve `False`, la descarta porque cerraría un ciclo.

### 17. Ejecución manual de Kruskal

| Paso | Arista | raíces | decisión | elegidas | costo |
| ---: | --- | --- | --- | --- | ---: |
| 1 | C–D:1 | C / D | aceptar | C–D | 1 |
| 2 | A–C:2 | A / C | aceptar | + A–C | 3 |
| 3 | D–E:2 | D / E | aceptar | + D–E | 5 |
| 4 | B–D:3 | B / D | aceptar | + B–D | 8 |

El costo final es 8. Se detiene porque ya se seleccionaron 4 aristas ($V-1$), conectando plenamente los 5 vértices de la red.

### 18. Grafo desconectado
Se alcanza un MST completo únicamente si logramos elegir exactamente $V-1$ aristas. Si el bucle termina con menos aristas seleccionadas, el grafo está desconectado.

### 19. Pesos negativos, empates y casos especiales
Porque con aristas de peso empatado existen múltiples combinaciones válidas que producen el mismo costo mínimo total de expansión sin alterar el resultado del algoritmo.

### 20. Complejidad
El ordenamiento inicial de las aristas del grafo, el cual toma un tiempo dominante de $O(E \log E)$.

### 21. CSES Road Reparation
Se deben restar uno a los índices de las ciudades para mapearlas de base 1 a base 0, y retornar la cadena `"IMPOSSIBLE"` si Kruskal no logra conectar toda la red.

### 22. LeetCode Redundant Connection
En Redundant Connection las aristas se procesan en el orden estricto de entrada sin ordenar, buscando solo la arista que cierra el ciclo inicial.

### 23. Implementación
Se debe probar la consistencia interna de `UnionFind`: validación de tipos, detección de ciclos, compresión de caminos, unión por tamaño y el correcto mantenimiento del contador de componentes.

### 24. Pruebas
Garantiza que intentar unir componentes que ya están conectadas no altera la consistencia interna, no reduce el contador de componentes ni muta la jerarquía de tamaños.

### 25. Cierre hacia ordenamiento topológico
Se requeriría calcular el grado de entrada de cada tarea y utilizar una cola de procesamiento para estructurar un orden de ejecución válido, como en el algoritmo de Kahn.