 # Respuestas del notebook — Clase 18- Aristeo

## Pregunta inicial

¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?
ordenando las aristas, iteramos para contar costos y buscar que no caiga en bucle.

## 1. Presentación de la clase

### ¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?
Buscamos un MST que no necesite empezar en el origen, se diferencia en que no es solo un camino del origen al destino.

## 2. Recuperación de estructuras anteriores

### ¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?
Detectar ciclos y crear caminos distintos al desde el origen.

## 3. Nueva pregunta: conectar toda la red

### ¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?
Porque en una de esas se nos hace un ciclo.

## 4. Dijkstra frente a Kruskal

### ¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?
El árbol de caminos mínimos optimiza cuál es el camino mínimo entre dos nodos, un árbol de expansión mínima encuentra el camino mínimo que alcanza más nodo desde un origen,  Dijsktra optimiza distancias desde un origen, Kruskal optimiza la red que conecta todos los nodos, sin necesidad de un origen.

## 5. Árboles de expansión

### ¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?
Porque en un árbol de este tipo, cada camino puede ser optimizado por una sola arista, entonces, como en V nodos hay V-1 caminos solo puede haber estas aristas.

## 6. Por qué evitar ciclos

### ¿Qué información mínima necesitamos antes de aceptar una arista u–v?
Saber si ya existe una conexión entre ellos.

## 7. Componentes conexas

### Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?
El número de conjuntos que componen la partición baja en uno por cada arista aceptada

## 8. Necesidad de Union-Find

### ¿Por qué conviene que union(a, b) devuelva un booleano?
Porque nos permite saber si se acepta o no crear el camino con base en si ya están previamente unidos.

## 9. Representación mediante padres

### ¿Qué condición permite reconocer una raíz en el arreglo padre?
Que el tamaño sea menor que el arreglo.

## 10. Operación find

### ¿Por qué debemos validar explícitamente los índices negativos?
Porque a find no se le pueden ingresar índices negativos.

## 11. Operación union

### ¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?
Podría hacerse una representación entre nodos que no son reales, lo cual causaria una incosistencia en los contratos.

## 12. Invariantes

### ¿Qué invariantes viola padre = [1, 0, 2]?
No son índices válidos.

## 13. Compresión de caminos

### ¿Qué cambia y qué permanece igual durante la compresión de caminos?
Cambia la representación interna del árbol, se vuelve mucho más plano apuntando directamente a la raíz para acelerar operaciones futuras.

## 14. Unión por tamaño

### ¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?
Porque así se comparan las alturas y se evita que profundidad

## 15. Ejecución manual de Union-Find

| Operación | raíces | efectiva | padres | tamaños en raíces | componentes |
| --- | --- | --- | --- | --- | ---: |
| inicio | — | — | `[0,1,2,3,4,5]` | seis unos | 6 |
| union(0,1) | 0 / 1 | sí | `[0,0,2,3,4,5]` | raíz 0:2 | 5 |
| union(2,3) | 2 / 3 | sí | `[0,0,2,2,4,5]` | raíz 2:2 | 4 |
| union(1,3) | 1 / 3  | no | `[0,0,2,2,4,5]` | raíz 2:2 | 4 |
| union(0,3) | 0 / 3 | no | `[0,0,2,2,4,5]` | raíz 2:2 | 4 |

### ¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?
False

## 16. Algoritmo de Kruskal

### ¿Cómo usa Kruskal el booleano devuelto por union?
Si devuelve True, Kruskal acepta y añade la arista al conjunto acumulado del MST. Si devuelve False, la ignora por redundante.

## 17. Ejecución manual de Kruskal

| Paso | Arista | raíces | decisión | elegidas | costo |
| ---: | --- | --- | --- | --- | ---: |
| 1 | C–D:1 | C / D | aceptar | C–D | 1 |
| 2 | A–C:2 | A / C | aceptar | + A–C | 3 |
| 3 | D–E:2 | D / E | aceptar | C–D + | 5 |
| 4 | B–D:3 | B / D | aceptar | C–D + | 8 |

### ¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?
8, porque la siguiente iteración sería unir A y B y eso crearía un ciclo, lo mimso con A y D y C y E.

## 18. Grafo desconectado

### ¿Qué condición permite distinguir un MST completo de un bosque desconectado?
Que un bosque desconectado provoca que se devuelva None, mientras que en el MST se devuelve el árbol

## 19. Pesos negativos, empates y casos especiales

### ¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?
Porque cuando hay empates en los pesos, pueden existir múltiples árboles de expansión mínima (MST) diferentes pero válidos con el mismo costo acumulado.

## 20. Complejidad

### ¿Qué parte domina la complejidad total de Kruskal?
El ordenamiento de las aristas por peso.

## 21. CSES Road Reparation

### ¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?
Que en el formato CSES no se usan índices desde cero sino desde uno, por lo que hay que restarle uno. Además si el costo de la carretera es None se considera que no hay camino posible y lanza error, mientras que en el nuestro solo pasa si no se llega a V-1 caminos.

## 22. LeetCode Redundant Connection

### ¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Fin
Que en redundant connection no se detecta error si se quiere hacer la unión en sentido inverso, pues no detecta que se crea otro camino, mientras que en Kruskal lo detecta como ciclo y devuelve False.

## 23. Implementación

### ¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?
Detectar ciclos, que los autoenlaces no sean posibles, que al llegar a V-1 se diga cual es el resultado y que si se detecta un bosque desconectado lanze imposible.

## 24. Pruebas

### ¿Qué invariante protege una prueba de unión repetida?
Que el único lazo en ciclo es el de la raíz consigo mismo, por lo que si hay una unión protegida se podría detectar un ciclo con otras raíces.

## 25. Cierre hacia ordenamiento topológico

### ¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?
Arboles.