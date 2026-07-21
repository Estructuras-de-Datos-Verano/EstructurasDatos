# Respuestas del notebook — José Iván Reyna Blanco

## Pregunta inicial

#### ¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?
Ordenamos todas las aristas de menor a mayor costo y empleamos la estructura Union-Find para validar la conectividad de sus extremos, aceptando solo aquellas que enlacen componentes independientes y rechazando las que cierren ciclos.

## 1. Presentación de la clase

#### ¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?
Esperamos obtener un árbol de expansión mínima (MST) que conecte la totalidad de los nodos minimizando el costo total global. A diferencia de los caminos mínimos, este no requiere un nodo origen determinado ni calcula distancias individuales.

## 2. Recuperación de estructuras anteriores

#### ¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?
Su operación dominante consiste en determinar si los extremos de una arista ya pertenecen a la misma componente conexa mediante Union-Find, evaluando la red de forma global en lugar de expandirse secuencialmente desde un origen.

## 3. Nueva pregunta: conectar toda la red

#### ¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?
Porque una carretera de bajo costo puede resultar redundante si sus extremos ya se encuentran comunicados a través de otras aristas elegidas previamente, lo cual cerraría un ciclo innecesario que no aporta conectividad.

## 4. Dijkstra frente a Kruskal

#### ¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?
Dijkstra optimiza las distancias individuales calculadas desde un nodo origen específico hacia todos los demás. Kruskal optimiza globalmente la suma total del costo del conjunto de aristas que conecta toda la red, operando sin un origen fijo.

## 5. Árboles de expansión

#### ¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?
Porque el algoritmo inicia con V componentes aisladas y cada unión útil disminuye el contador de componentes exactamente en uno. Para unificar todo el grafo en una sola componente se requieren exactamente V-1 aristas efectivas.

## 6. Por qué evitar ciclos

#### ¿Qué información mínima necesitamos antes de aceptar una arista u–v?
Necesitamos verificar si los nodos u y v ya pertenecen a la misma componente conexa del bosque seleccionado, lo cual indicaría que la arista cerrará un ciclo y debe ser rechazada.

## 7. Componentes conexas

#### Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?
Las dos componentes independientes se fusionan en un único conjunto disjunto dentro de la partición general del grafo, provocando que el contador global de componentes conexas disminuya exactamente en uno.

## 8. Necesidad de Union-Find

#### ¿Por qué conviene que union(a, b) devuelva un booleano?
Porque unifica la toma de decisiones y la actualización de la estructura en un solo paso: devuelve True si conecta componentes distintas de forma efectiva (arista aceptada) y False si los nodos ya compartían raíz (arista rechazada).

## 9. Representación mediante padres

#### ¿Qué condición permite reconocer una raíz en el arreglo padre?
Una raíz se reconoce de forma matemática dentro del arreglo de control cuando el valor almacenado en su índice apunta directamente a sí mismo, cumpliendo estrictamente la condición `padre[i] == i`.

## 10. Operación find

#### ¿Por qué debemos validar explícitamente los índices negativos?
Porque Python admite la indexación negativa por defecto y accedería por accidente a las posiciones del final de la lista, rompiendo el contrato operativo de Union-Find y corrompiendo el rastreo correcto de raíces.

## 11. Operación union

#### ¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?
Se generarían estructuras inconsistentes y subárboles mal estructurados que no apuntan a los líderes reales de la componente conexa, provocando fallas graves de transitividad en las búsquedas posteriores de find.

## 12. Invariantes

#### ¿Qué invariantes viola padre = [1, 0, 2]?
Viola la invariante de que toda cadena debe finalizar en una raíz y la prohibición de ciclos. Aquí los índices 0 y 1 se apuntan mutuamente en un bucle cerrado infinito, impidiendo que find localice jamás una raíz válida.

## 13. Compresión de caminos

#### ¿Qué cambia y qué permanece igual durante la compresión de caminos?
Cambia la estructura interna al aplanar el árbol para que todos los nodos del camino apunten directo a su raíz, optimizando búsquedas futuras. Permanecen idénticos los tamaños lógicos, las componentes y el contador global.

## 14. Unión por tamaño

#### ¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?
Porque la profundidad del árbol de mayor tamaño solo se incrementará cuando se le acople uno de tamaño igual o superior. Al subordinar siempre al más pequeño, controlamos el balanceo y aseguramos costos de operación casi constantes.

## 15. Ejecución manual de Union-Find

| Operación | raíces | efectiva | padres | tamaños en raíces | componentes |
| --- | --- | --- | --- | --- | ---: |
| inicio | — | — | `[0,1,2,3,4,5]` | seis unos | 6 |
| union(0,1) | 0 / 1 | sí | `[0,0,2,3,4,5]` | raíz 0:2 | 5 |
| union(2,3) | 2 / 3 | sí | `[0,0,2,2,4,5]` | raíz 2:2 | 4 |
| union(1,3) | 0 / 2 | sí | `[0,0,0,2,4,5]` | raíz 0:4 | 3 |
| union(0,3) | 0 / 0 | no | `[0,0,0,2,4,5]` | raíz 0:4 | 3 |

#### ¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?
Devuelve False, ya que ambos nodos pasaron a formar parte de la misma componente conexa debido a la unión efectiva realizada previamente entre los elementos 1 y 3.

## 16. Algoritmo de Kruskal

#### ¿Cómo usa Kruskal el booleano devuelto por union?
Si recibe True, agrega formalmente la arista al conjunto del MST y acumula su peso en el costo total. Si recibe False, ignora la arista inmediatamente por ser un ciclo redundante y continúa con la siguiente.

## 17. Ejecución manual de Kruskal

| Paso | Arista | raíces | decisión | elegidas | costo |
| ---: | --- | --- | --- | --- | ---: |
| 1 | C–D:1 | C / D | aceptar | C–D | 1 |
| 2 | A–C:2 | A / C | aceptar | C–D, A–C | 3 |
| 3 | D–E:2 | C / E | aceptar | C–D, A–C, D–E | 5 |
| 4 | B–D:3 | B / C | aceptar | C–D, A–C, D–E, B–D | 8 |

#### ¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?
El costo final es 8. Se detiene tras procesar la cuarta arista porque el grafo posee 5 vértices, alcanzando la condición de parada óptima al haber seleccionado exactamente V-1 aristas válidas.

## 18. Grafo desconectado

#### ¿Qué condición permite distinguir un MST completo de un bosque desconectado?
Un MST completo logra seleccionar exactamente V-1 aristas conectando todos los nodos de la red. Un bosque desconectado se identifica porque las aristas disponibles se agotan por completo sin alcanzar dicha meta, retornando None.

## 19. Pesos negativos, empates y casos especiales

#### ¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?
Porque los empates de costo abren la posibilidad de construir múltiples configuraciones de MST igualmente válidas. Las pruebas deben evaluar las propiedades invariantes del resultado (costo total y conectividad) y no una secuencia rígida.

## 20. Complejidad

#### ¿Qué parte domina la complejidad total de Kruskal?
La etapa de copiar y ordenar el conjunto total de las E aristas del grafo por peso en orden ascendente, lo cual establece la complejidad algorítmica dominante del proceso en O(E log E).

## 21. CSES Road Reparation

#### ¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?
El formato CSES utiliza una indexación basada en 1 (lo que requiere restar 1 para mapear a 0...n-1) y exige capturar el retorno None de la función para imprimir textualmente la palabra "IMPOSSIBLE" ante grafos desconectados.

## 22. LeetCode Redundant Connection

#### ¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?
Kruskal requiere realizar un ordenamiento previo por costo para optimizar la red global. Redundant Connection procesa las aristas respetando su estricto orden de entrada para hallar la primera de ellas que cierre un ciclo.

## 23. Implementación

#### ¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?
Se debe validar de forma independiente el comportamiento de Union-Find: control de índices negativos, uniones efectivas y redundantes, el manejo del contador de componentes y la correcta actualización de tamaños en las raíces.

## 24. Pruebas

#### ¿Qué invariante protege una prueba de unión repetida?
Protege la invariante del contador de componentes y los tamaños en las raíces, asegurando que invocar operaciones redundantes sobre elementos ya enlazados mantenga intacto el estado lógico sin alterar los registros.

## 25. Cierre hacia ordenamiento topológico

#### ¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?
Se requiere modelar las dependencias de las tareas mediante un grafo dirigido, resolviendo el flujo de precedencias a través de una cola de soporte que estructure el algoritmo de ordenamiento topológico.