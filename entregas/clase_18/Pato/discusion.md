# Clase 18: Discusión 
#### Nombre: Patricio Navarro

## 1. Problema
¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?
- Camino mínimo: es una secuencia y no garantiza ni pide que todos los nodos sean parte del camino.
- Árbol de expansión mínimo: Conecta todos los nodos pero no tiene ciclos.

## 2. Árbol de expansión
¿Por qué una solución tiene \(V-1\) aristas?
- Porque si tienes dos nodos, necesitas una línea para conectarlos.
- Si tienes tres nodos en un árbol, necesitas dos aristas para conectar todos.
- Si tienes siete nodos en un árbol, necesitas 6 aristas
    - Dos para conectar la raíz con los dos del segundo nivel.
    - Dos para cada nodo del segundo nivel con sus dos nodos del tercer nivel. Es decir, 4 aristas en total para conectar el segundo con el 3er nivel.
- Así, por recursividad se ve que para n vértices se necesitan n-1 aristas.

## 3. Ciclos
¿Por qué se rechaza una arista cuyos extremos ya están conectados?
- Porque te crearía un ciclo, o puede que añada costo que no es necesario.

## 4. Componentes
¿Qué representa una componente en Union-Find?
- Elementos que están unidos entre sí.

## 5. Representantes
¿Qué significa la raíz de un elemento?
- Su padre.

## 6. `find`
¿Qué operación realiza `find`?
- Su función principal es encontrar y devolver la raíz del conjunto al que pertenece el elemento x.

## 7. `union`
¿Por qué conviene que `union` devuelva un booleano?
- Para definir cuando se puede unir o no y usar ese resultado para tomar la siguiente decisión.

## 8. Compresión
¿Qué cambia y qué no cambia con la compresión de caminos?
- Cambia a donde apunta cada elemento, no cambian los elementos ni su orden.

## 9. Unión por tamaño
¿Por qué se coloca el árbol pequeño debajo del grande?
- Para restringir la altura.

## 10. Invariantes
¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?
- En el arreglo de padres:
    - La regla del líder (raíz): Un nodo es el líder de su grupo si y solo si apunta a sí mismo (_padres[i] == i).
    - Sin caminos infinitos: Si sigues la cadena de padres de cualquier nodo hacia arriba, tienes la garantía de llegar a un líder. Es imposible quedarse atrapado dando vueltas en un círculo.

- En el arreglo de tamaños:
    - Solo importa el tamaño del líder: El número en _tamanos[i] solo es real y correcto si el nodo i es un líder activo. Si un nodo deja de ser líder (porque lo uniste a otro), su tamaño ya no sirve de nada y el código lo ignora.
    - La suma total se conserva: Si sumas los tamaños de todos los líderes que quedan activos, el resultado siempre debe ser igual a la cantidad total de elementos con los que iniciaste el programa.

## 11. Kruskal
¿Cuál es la operación dominante de Kruskal?
- Ordenamiento de aristas por peso.

## 12. Grafo desconectado
¿Por qué Kruskal puede terminar con un bosque?
- Porque puede haber nodos que no se conecten entre ellos.

## 13. Pesos negativos
¿Por qué Kruskal acepta pesos negativos y Dijkstra no?
- Kruskal: Busca conectar todos los nodos al menor costo total sin importar la distancia entre nodos específicos. Una arista con peso negativo simplemente se interpreta como una arista "extremadamente barata" que el algoritmo querrá elegir primero. Como Union-Find previene la formación de ciclos de forma estructural, los números negativos no rompen la lógica.
- Dijkstra: Se basa en la premisa de que agregar aristas a un camino solo puede hacer que este sea más costoso o igual. Si hay pesos negativos, esta premisa se destruye: un camino con más aristas podría terminar siendo más barato que uno directo ya procesado. Dijkstra "marca" nodos como visitados permanentemente bajo la suposición de que ya encontró su ruta óptima; los pesos negativos hacen que sea necesario reconsiderar nodos ya cerrados, rompiendo su estrategia codiciosa.

## 14. Empates
¿Por qué puede haber varios árboles de expansión mínima?
- Porque cuando hay empates en los pesos el árbol deja de ser único.

## 15. Complejidad
¿Qué parte domina la complejidad de Kruskal?
- El ordenamiento de las aristas.

## 16. Comparación
Compara cola, deque, heap y Union-Find según la operación que optimizan.
| Estructura | Operación principal que optimiza | Complejidad de la operación | Caso de uso típico |
| :--- | :--- | :--- | :--- |
| **Cola (Queue)** | Acceso FIFO (*First-In, First-Out*). Inserción al final y extracción al inicio. | **O(1)** | Recorridos en anchura (BFS), sistemas de turnos. |
| **Deque** | Inserción y extracción en ambos extremos (izquierdo y derecho). | **O(1)** | Algoritmo de caminos mínimos con costo 0-1, mantener ventanas deslizantes. |
| **Heap (Max/Min)** | Acceso inmediato al elemento con mayor o menor prioridad. | **O(1)** consulta, **O(log N)** extracción/inserción | Algoritmo de Dijkstra, Prim, ordenamiento por montículos (*Heapsort*). |
| **Union-Find** | Comprobación de conectividad (`find`) y fusión de conjuntos (`union`). | **O(α(N))** (casi constante) | Algoritmo de Kruskal, detección de ciclos en tiempo real, conectividad de redes. |

## 17. Producción
¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?
1. **Corrupción de datos interna:** Si un cliente solicita conectar el nodo `-1` con el `2`, Python no lanzará un error. En su lugar, asociará silenciosamente el último elemento de tu arreglo `_padres` con el nodo `2`.
2. **Ciclos infinitos indeseados:** Podrías conectar accidentalmente el final del arreglo con el inicio, rompiendo la propiedad de aciclicidad de los árboles. Esto causará que el método `find` entre en un bucle infinito la próxima vez que se consulte.
3. **Dificultad de depuración:** Al no lanzarse una excepción inmediata (como un `IndexError`), el sistema seguirá funcionando con datos corruptos en memoria, haciendo que el error se manifieste mucho después y sea sumamente difícil de rastrear.

## 18. Cierre
¿Qué estructura se necesitaría para procesar tareas según dependencias?
- Una mezcla entre Kruskal y Dijkstra.
