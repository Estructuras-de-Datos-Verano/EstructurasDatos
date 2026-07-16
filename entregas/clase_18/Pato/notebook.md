# Clase 18: Notebook
#### Nombre: Patricio Navarro

## Pregunta inicial
**¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?**
- Que cada que insertemos un nodo se conecte a todos los nodos ya creados.

## Presentación de la clase
**¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?**
- Esperamos encontrar una red donde todos los nodos se conecten pero sin que existan ciclos. 
- Se diferencia de un camino en el sentido de que no hay una única ruta conectando ciudad en ciudad, como tipo secuencia, sino que es una red conectada completamente.

## Recuperación de estructuras anteriores
**¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?**
- Los otros te hablan de encontrar un camino mínimo, Kruskal de conectar todo con el menor costo.

## Nueva pregunta: conectar toda la red
**Actividad:** marca qué carreteras aceptarías y conserva el costo acumulado. Todavía no uses el nombre del algoritmo.
1. C -> D; Sí se acepta; Costo: 1
2. B -> D; Sí se acepta; Costo: 3
3. A -> C; Sí se acepta; Costo: 2
4. D -> E; Sí se acepta; Costo: 2
Costo acumulado: 8

**¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?**
- Porque estaríamos aceptando rutas redundantes como la de `A -> B` donde te lleva a D pero ya no es necesario porque tienes la de `A -> C` que tiene un menor costo.

## Dijkstra frente a Kruskal
**¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?**
- Dijkstra: 
    - Optimiza camino de menor costo.
    - Sí necesita un origen.
- Kruskal:
    - Optimiza la red de menor costo.
    - No necesita un origen porque todo está conectado.

## Árboles de expansión
**¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?**
- Porque si tienes dos nodos, necesitas una línea para conectarlos.
- Si tienes tres nodos en un árbol, necesitas dos aristas para conectar todos.
- Si tienes siete nodos en un árbol, necesitas 6 aristas
    - Dos para conectar la raíz con los dos del segundo nivel.
    - Dos para cada nodo del segundo nivel con sus dos nodos del tercer nivel. Es decir, 4 aristas en total para conectar el segundo con el 3er nivel.
- Así, por recursividad se ve que para n vértices se necesitan n-1 aristas.

## Por qué evitar ciclos
**¿Qué información mínima necesitamos antes de aceptar una arista u–v?**
- El costo y si ya tienes un camino que una el origen con el destino que sea de menor costo.

## Componentes conexas
**¿Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?**
- Se van agrupando como si fueran un mismo elemento de la partición.

## Necesidad de Union - Find
**¿Por qué conviene que union(a, b) devuelva un booleano?**
- Porque solo debe marcar si se pudo hacer la unión o si no, así ya sabes que si la aceptó es porque convenía para el costo, si no es porque ya había un camino de menor costo.

## Representación mediante padres
**¿Qué condición permite reconocer una raíz en el arreglo padre?**
- Su índice. La raíz debe ser padre[0].

## Operación find
**¿Por qué debemos validar explícitamente los índices negativos?**
- Porque como siguen siento enteros, la función si los acepta, pero nunca encontrará nada y nos mandará un error o un índice que no es correcto, entonces mejor lo validamos y nos quedamos con el puro conjunto Omega como el dominio.

## Operación unión
**¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?**
- Que puede crear asitas repetidas o que no convienen para el costo mínimo.

## Invariantes
**¿Qué invariantes viola padre = [1, 0, 2]?**
- Toda cadena termina en una raíz y que cada raíz es su propio padre.

## Compresión de caminos
**¿Qué cambia y qué permanece igual durante la compresión de caminos?**
- Los elementos son los mismos, solo cambia a donde apuntan.

## Unión por tamaño
**¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?**
- Al colgar el árbol co n menos elementos bajo la raíz del más poblado, la mayría mantiene su misma distancia a la raíz, evitando cadenas largas que voverían lenta la función de find.

## Ejecución manual de Union-Find. 
**Actividad:** Completa la tabla y ejecuta `find(3)`, `tamano_componente(1)` y `conectados(0,4)`. Luego compara con las cinco secuencias visuales.
| Operación | raíces | efectiva | padres | tamaños en raíces | componentes |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **inicio** | — | — | `[0, 1, 2, 3, 4, 5]` | seis unos | 6 |
| **union(0,1)** | 0 / 1 | sí | `[0, 0, 2, 3, 4, 5]` | raíz 0: 2 | 5 |
| **union(2,3)** | 2 / 3 | sí | `[0, 0, 2, 2, 4, 5]` | raíz 2: 2 | 4 |
| **union(1,3)** | 0 / 2 | sí | `[0, 0, 0, 2, 4, 5]` | raíz 0: 4 | 3 |
| **union(0,3)** | 0 / 0 | no | `[0, 0, 0, 2, 4, 5]` | raíz 0: 4 | 3 |
| **union(4,5)** | 4 / 5 | sí | `[0, 0, 0, 2, 4, 4]` | raíz 0: 4, raíz 4: 2 | 2 |

- find(3)
    - Sin compresión de caminos: Seguimos la cadena de padres: 3 -> 2 -> 0. Devuelve 0.

    - Con compresión de caminos (comportamiento estándar y optimizado): Al buscar la raíz de 3, el algoritmo conecta a 3 directamente con la raíz principal 0.

    - Resultado: Devuelve 0.

    - Efecto en el arreglo de padres: Se actualiza a [0, 0, 0, 0, 4, 4] (el nodo 3 ahora apunta directo a 0).

- tamano_componente(1)
    - Buscamos la raíz del elemento 1, que es 0.

    - Leemos el tamaño guardado para la raíz 0.

    - Resultado: Devuelve 4 (que corresponde al grupo formado por {0, 1, 2, 3}).

- conectados(0,4)
    - Comparamos si sus raíces son iguales: find(0) == find(4).

    - Como find(0) es 0 y find(4) es 4, las raíces son distintas.

    - Resultado: Devuelve False (están en componentes separadas).

¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?
- `False`

## Algoritmo de Kruskal
**¿Cómo usa Kruskal el booleano devuelto por union?**
- Para decidir si se acepta y se suma o si se rechaza.

## Ejecución manual de Kruskal
**Actividad:** Completar tabla

| Paso | Arista | raíces | decisión | elegidas | costo |
| ---: | --- | :---: | :---: | :--- | ---: |
| 1 | C–D:1 | C / D | aceptar | C–D | 1 |
| 2 | A–C:2 | A / C | aceptar | + A–C | 3 |
| 3 | D–E:2 | A / E | aceptar | + D–E | 5 |
| 4 | B–D:3 | B / A | aceptar | + B–D | 8 |

¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?
- Costo total = 17
- Porque ya tenemos v-1 aristas y nos podemos detener.

## Grafo desconectado
**¿Qué condición permite distinguir un MST completo de un bosque desconectado?**
- Que se puedan unir todos los nodos con v-1 selecciones.

## Pesos negativos, empates y casos especiales
**¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?**
- Porque el MST no es único.

## Complejidad
**¿Qué parte domina la complejidad total de Kruskal?**
- El ordenamiento de las aristas por su peso.

## CSES Road Reparation
**Actividad:** modela lista de aristas, explica la conversión, predice qué carretera cierra un ciclo y diseña una prueba desconectada.
1. Lista de aristas en formato (costo, nodo_u, nodo_v) con índices 0-based
```python
aristas = [
    (3, 0, 1),  
    (5, 1, 2),  
    (2, 1, 3),  
    (8, 2, 3),  
    (7, 4, 0),  
    (4, 4, 3),  
]
```
2. Porque los índices naturales son con naturales pero en programación se empieza en 0.
3. La carretera 5–1 con costo 7 (representada como (7, 4, 0)) es la primera en cerrar un ciclo durante la ejecución del algoritmo de Kruskal.
4. 4 nodos pero solo dos aristas.
4 2
1 2 10
3 4 20

**¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?**
- Los índices empiezan en 1.
- La salida `None`por `"IMPOSSIBLE"`.

## LeetCode Redundat Connection
**¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?**
- Mientras que Kruskal usa Union-Find como una herramienta de soporte para su estrategia codiciosa (greedy), Redundant Connection utiliza Union-Find en su estado más puro: como un detector de ciclos en tiempo real sobre un flujo de conexiones.

## Implementación
**¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?**
- Inicialización.
- Búsqueda.
- Unión.
- Robustez de entradas válidas.

## Pruebas
**¿Qué invariante protege una prueba de unión repetida?**
- Protege la invariante cuantitativa de componentes y la estabilidad estructural de la estructura Union-Find.

## Cierre
**¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?**
- Una mezcla entre Dijkstra y Kruskal.