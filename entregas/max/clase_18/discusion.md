# Discusión técnica — Clase 18 - Max

## 1. Problema
¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?

Los caminos minimos se fijan entre dos nodos, no en toda la red.

## 2. Árbol de expansión
¿Por qué una solución tiene \(V-1\) aristas?

Porque no se necesita tener más cosas conectadas puede que existan, pero que esten ahí no quiere decir que necesitamos haberlas pasado.

## 3. Ciclos
¿Por qué se rechaza una arista cuyos extremos ya están conectados?

porque de no rechazarse se pueden crear ciclos en los cuales no se va poder correr correctamente el algoritmo Kruskal.

## 4. Componentes
¿Qué representa una componente en Union-Find?

Lo que representa es un punto donde podremos tener aristas unir las diferentes aristas.

## 5. Representantes
¿Qué significa la raíz de un elemento?

La raíz de un elemento quiere decir el punto de partida de donde podemos ver el algoritmo.

## 6. `find`
¿Qué operación realiza `find`?

Lo que hace es que busca los puntos necesarios para poder hacer el arbol correctamente.

## 7. `union`
¿Por qué conviene que `union` devuelva un booleano?

Porque de esta manera podemos ver si se necesita cambiar algo de una manera bastante clara.

## 8. Compresión
¿Qué cambia y qué no cambia con la compresión de caminos?

Lo que cambia es la manera en la que podemos entender los caminos necesarios y lo que no cambia es la manera en la que se crean los caminos.

## 9. Unión por tamaño
¿Por qué se coloca el árbol pequeño debajo del grande?

Porque si no se generan problemas.

## 10. Invariantes
¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?

Loscaminos ya recorrido y las raices de donde salen.

## 11. Kruskal
¿Cuál es la operación dominante de Kruskal?

La operación dominante es la elejir los caminos correspondientes.

## 12. Grafo desconectado
¿Por qué Kruskal puede terminar con un bosque?

Porque crea los diferentes arboles sin importar el camino, y ya una vez que tiene el bosque elige el mejor árbol.

## 13. Pesos negativos
¿Por qué Kruskal acepta pesos negativos y Dijkstra no?

Porque aca los podemos filtrar para ver cuales son los que menos nos convienen.

## 14. Empates
¿Por qué puede haber varios árboles de expansión mínima?

Porque así podemos ponderar las opciones que tenemos.

## 15. Complejidad
¿Qué parte domina la complejidad de Kruskal?

La parte de elegir correctamente que árbol necesitamos utilizar, ya que a partir de ahí se define el resto del árbol

## 16. Comparación
Compara cola, deque, heap y Union-Find según la operación que optimizan.

Lo que cambia más que nada es la forma en la que funcionan, ya que si bien todas son una especie de arbol pero con diferentes caracteristicas, depemndiendo de lo que necesitemos.

## 17. Producción
¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?

Los riesgos que tendría es que al final nos podria arrojar un resultado negativo.

## 18. Cierre
¿Qué estructura se necesitaría para procesar tareas según dependencias?

Para mi el mejor algoritmo para este tipo de problemas es uno de tipo heap.