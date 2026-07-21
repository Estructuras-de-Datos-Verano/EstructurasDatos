# Discusion - José Iván Reyna Blanco

## Pregunta Inicial

**¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?** La verdad es imposible responder esa pregunta antes de leer el notebook. Me imagino que haciendo muchos de golpe y mejorándo las conexiones que correspondan si aparecen mejores condiciones de conexión (con pesos me imagino).

## 1. Problema

**Preguta:** ¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?
Los caminos mínimos optimizan las distancias individuales partiendo desde un nodo origen específico. El árbol de expansión mínima optimiza de forma global la suma total del costo de las aristas para conectar a toda la red sin requerir un origen fijo.

## 2. Árbol de expansión

**Preguta:**¿Por qué una solución tiene V-1 aristas? Porque se inicia con V componentes aisladas y cada arista útil reduce el número de componentes como máximo en uno. Se requieren V-1 uniones efectivas para lograr conectar todo el grafo, ya que una arista adicional cerraría un ciclo.

## 3. Ciclos

**Preguta:** ¿Por qué se rechaza una arista cuyos extremos ya están conectados? Porque si sus extremos pertenecen a la misma componente, la arista cierra un ciclo y resulta redundante. Una solución de costo mínimo no necesita conservar ciclos completos para mantener la conectividad global.

## 4. Componentes

**Preguta:** ¿Qué representa una componente en Union-Find? Representa un conjunto disjunto de nodos mutuamente conectados dentro de una partición de la red. Todos los elementos que pertenecen a la misma componente producen la misma raíz al ser consultados mediante find.

## 5. Representantes
**Preguta:**¿Qué significa la raíz de un elemento? Es el nodo líder o representante supremo de su respectiva componente conexa. En el arreglo de control se reconoce porque se apunta a sí mismo como su propio padre.

## 6. `find`
**Preguta:** ¿Qué operación realiza `find`? Sigue de forma ascendente la cadena de padres desde el nodo consultado hasta encontrar y devolver la raíz de su componente.

## 7. `union`
**Preguta:** Porque reúne la decisión y la actualización en un solo paso, devolviendo True si conectó componentes distintas de manera efectiva o False si la arista fue rechazada por cerrar un ciclo.

## 8. Compresión
**Preguta:** ¿Qué cambia y qué no cambia con la compresión de caminos? Cambia la representación interna del árbol al conectar los nodos visitados directamente con su raíz para optimizar búsquedas futuras. No cambian las componentes, los tamaños lógicos ni el contador de componentes.

## 9. Unión por tamaño
**Preguta:**¿Por qué se coloca el árbol pequeño debajo del grande? Para limitar el crecimiento en la altura de la estructura y evitar que alcance una profundidad extrema. Al mantener el árbol balanceado junto con la compresión, las operaciones toman un costo casi constante en la práctica.

## 10. Invariantes
**Preguta:**¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños? Cada padre debe ser un índice válido, toda cadena debe finalizar en una raíz (la cual es su propio padre), el tamaño vigente solo se consulta en la raíz y el contador coincide con el número de raíces[cite: 1].

## 11. Kruskal
**Preguta:** ¿Cuál es la operación dominante de Kruskal? La operación dominante de Kruskal es ordenar la copia de todas las aristas del grafo por su peso en orden creciente antes de iterar sobre ellas.

## 12. Grafo desconectado
**Preguta:** ¿Por qué Kruskal puede terminar con un bosque? Porque si las aristas disponibles se agotan antes de alcanzar exactamente V-1 selecciones, el algoritmo no logra unificar la red global. Esto genera múltiples árboles aislados en lugar de un árbol de expansión único.

## 13. Pesos negativos
**Preguta:** ¿Por qué Kruskal acepta pesos negativos y Dijkstra no? Kruskal procesa aristas globalmente ordenadas por peso, por lo que los valores negativos se evalúan primero de forma válida. Dijkstra los prohíbe porque una distancia considerada final puede verse reducida erróneamente mediante caminos posteriores.

## 14. Empates
**Preguta:** ¿Por qué puede haber varios árboles de expansión mínima? Porque al existir aristas con pesos empatados se pueden construir distintas configuraciones de red con el mismo costo mínimo global. Por ello, las pruebas deben validar propiedades como costo y conectividad, no una lista exacta.

## 15. Complejidad
**Preguta:** ¿Qué parte domina la complejidad de Kruskal? El proceso de copiar y ordenar las E aristas del grafo por peso, lo cual define la complejidad total del algoritmo como O(E log E).

## 16. Comparación
**Preguta:** Compara cola, deque, heap y Union-Find según la operación que optimizan. La cola optimiza el orden FIFO; la deque gestiona eficientemente operaciones por ambos extremos; el heap prioriza la menor distancia tentativa (Dijkstra) y Union-Find agiliza la verificación de pertenencia a la misma componente.

## 17. Producción
**Preguta:** ¿Qué riesgos tendría implementar Union-Find sin validar índices negativos? Provocaría que Python consulte elementos desde el final de la lista por accidente, alterando la detección de raíces y corrompiendo la conectividad global.

## 18. Cierre
**Preguta:** ¿Qué estructura se necesitaría para procesar tareas según dependencias? Un grafo dirigido para modelar las dependencias, procesando los grados de entrada de los nodos mediante una cola para generar un ordenamiento válido.