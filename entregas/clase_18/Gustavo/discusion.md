# Discusión técnica — Clase 18

## 1. Problema
**¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?**
Caminos mínimos (como Dijkstra) busca la ruta más corta desde un único punto de origen hacia todos los demás de forma individual. El Árbol de Expansión Mínima (como Kruskal) busca el esqueleto global más barato para conectar todos los nodos de la red juntos, sin importar un punto de partida ni optimizar distancias entre pares específicos.

## 2. Árbol de expansión
**¿Por qué una solución tiene \(V-1\) aristas?**
Al inicio tienes $V$ nodos totalmente aislados (cada uno es su propia componente). Cada arista útil que agregas funciona como un puente que fusiona dos componentes en una sola, reduciendo el conteo total de grupos en 1. Para unificar los $V$ grupos en un único gran grupo conectado sin crear caminos redundantes, necesitas exactamente $V-1$ fusiones (aristas).

## 3. Ciclos
**¿Por qué se rechaza una arista cuyos extremos ya están conectados?**
Porque si los dos extremos ya están conectados a través de otros caminos del árbol, agregar esta nueva arista no aporta ninguna conectividad real; solo cierra un circuito cerrado (ciclo). Al hacer esto, estarías gastando presupuesto en una conexión redundante que no ayuda a cumplir el objetivo de expansión.

## 4. Componentes
**Qué representa una componente en Union-Find?**
Representa un conjunto disjunto o "equipo" de elementos. Todos los nodos que pertenecen a una misma componente están conectados entre sí de alguna manera directa o indirecta dentro del bosque actual.

## 5. Representantes
**¿Qué significa la raíz de un elemento?**
Es el líder o "jefe máximo" de la componente a la que pertenece ese elemento. Sirve como identificador único del grupo: si dos nodos diferentes devuelven la misma raíz al ser consultados, significa que ya juegan en el mismo equipo.

## 6. `find`
**¿Qué operación realiza `find`?**
Sigue la cadena de punteros hacia arriba desde el nodo consultado hasta encontrar su raíz (el representante). Además, aprovecha ese viaje para aplicar la compresión de caminos, haciendo que los nodos visitados apunten directamente al jefe máximo para acelerar futuras consultas.

## 7. `union`
**¿Por qué conviene que `union` devuelva un booleano?**
Porque permite centralizar la decisión y la acción en un solo paso. Devuelve `True` si los elementos estaban en grupos distintos y los fusionó con éxito (arista aceptada para el árbol), y devuelve `False` si ya compartían la misma raíz (arista rechazada por ciclo), lo que le ahorra a Kruskal tener que preguntar primero y actualizar después.

## 8. Compresión
**¿Qué cambia y qué no cambia con la compresión de caminos?**
Cambia la estructura y forma interna del árbol, volviéndolo mucho más plano y directo porque los nodos pasan a apuntar directo a la raíz. Lo que **no cambia** es la lógica de los conjuntos: las componentes siguen integradas por los mismos miembros, los tamaños totales no varían y el número de grupos se mantiene intacto.

## 9. Unión por tamaño
**¿Por qué se coloca el árbol pequeño debajo del grande?**
Para controlar la altura (profundidad) del árbol resultante. Si cuelgas el grupo con menos nodos debajo de la raíz del grupo más grande, la distancia que deben recorrer la mayoría de los elementos hacia su raíz no aumenta, manteniendo las operaciones de búsqueda con un costo casi constante.

## 10. Invariantes
**¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?**
* En el arreglo de **padres**: cada valor debe ser un índice válido dentro del rango, toda cadena de punteros debe terminar obligatoriamente en una raíz, una raíz debe apuntarse a sí misma (`padre[i] == i`) y no pueden existir ciclos infinitos entre nodos comunes.
* En el arreglo de **tamaños**: solo el valor almacenado en la posición de una raíz vigente es correcto y debe reflejar con precisión la suma total de elementos de esa componente entera.

## 11. Kruskal
**¿Cuál es la operación dominante de Kruskal?**
Conceptualmente, la operación que repite una y otra vez es la pregunta de conectividad: *"¿estos dos extremos ya pertenecen a la misma componente para saber si acepto o rechazo la arista?"*.

## 12. Grafo desconectado
**¿Por qué Kruskal puede terminar con un bosque?**
Porque si el grafo de entrada tiene comunidades o islas que están completamente aisladas entre sí, el algoritmo procesará todas las conexiones posibles y se quedará sin aristas disponibles antes de poder juntar todo en un solo árbol, terminando con varios árboles independientes (un bosque) y devolviendo `None`.

## 13. Pesos negativos
**¿Por qué Kruskal acepta pesos negativos y Dijkstra no?**
Kruskal simplemente ordena las aristas globalmente y las va evaluando de menor a mayor peso; una conexión con peso negativo califica como "muy barata" y entra sin problemas al árbol si no genera ciclos. Dijkstra falla con pesos negativos porque es un algoritmo avaro local: asume de forma definitiva que al extraer un nodo del heap ya encontró su camino más corto absoluto, una regla que se rompe si más adelante aparece una arista negativa que reduce costos retroactivamente.

## 14. Empates
**¿Por qué puede haber varios árboles de expansión mínima?**
Cuando existen diferentes aristas que tienen exactamente el mismo peso mínimo, el orden en el que se procesen puede hacer que se elija una autopista en lugar de otra para romper el mismo ciclo. Ambas opciones logran conectar los mismos puntos con la misma efectividad y el mismo costo final acumulado, generando estructuras distintas pero igualmente óptimas.

## 15. Complejidad
**¿Qué parte domina la complejidad de Kruskal?**
El ordenamiento inicial de todas las aristas del grafo por su peso, el cual toma un tiempo de $O(E \log E)$. Como las operaciones del Union-Find optimizado son sumamente rápidas, el ordenamiento se convierte en el cuello de botella del rendimiento.

## 16. Comparación
**Compara cola, deque, heap y Union-Find según la operación que optimizan.**
* **Cola estándar (en BFS):** Optimiza el orden de descubrimiento por niveles para hallar caminos mínimos en grafos sin pesos (menor número de aristas).
* **Deque (en 0-1 BFS):** Optimiza la inserción prioritaria colocando los elementos de costo 0 al frente y los de costo 1 al final.
* **Heap / Cola de prioridad (en Dijkstra):** Optimiza la extracción rápida de la distancia tentativa más pequeña en cada paso.
* **Union-Find (en Kruskal):** Optimiza la consulta de pertenencia grupal y la fusión rápida de conjuntos independientes para evitar ciclos.

## 17. Producción
**¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?**
En Python, pasar un índice negativo como `-1` no levanta un error por defecto, sino que accede al último elemento de la lista. Si no se valida, el algoritmo avanzaría leyendo y modificando ciegamente nodos incorrectos al final del arreglo, rompiendo por completo las relaciones de parentesco lógicas y produciendo falsos ciclos o corrupciones de memoria silenciosas imposibles de depurar.

## 18. Cierre
**¿Qué estructura se necesitaría para procesar tareas según dependencias?**
Necesitas construir un orden topológico. Para implementarlo de forma eficiente (como en el algoritmo de Kahn), requerirías llevar el conteo de los grados de entrada de cada nodo (cuántas dependencias le quedan pendientes) y usar una **cola** estándar para ir procesando y liberando las tareas cuyos prerrequisitos ya estén en cero.