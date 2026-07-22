# Discusión técnica — Clase 18 - Aristeo

## 1. Problema
¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?
Los caminos mínimos optimizan la distancia total desde un nodo origen hacia los demás, minimizando el costo individual de cada ruta específica, mientras que el Árbol de Expansión Mínima (MST), por el contrario, busca minimizar el peso global requerido para mantener conectados todos los vértices de la red, sin importar si la ruta resultante entre dos nodos individuales no es la más corta o directa.

## 2. Árbol de expansión
¿Por qué una solución tiene \(V-1\) aristas?

Porque no se necesita tener más cosas conectadas puede que existan, pero que esten ahí no quiere decir que necesitamos haberlas pasado.

## 3. Ciclos
¿Por qué se rechaza una arista cuyos extremos ya están conectados?

Porque si no, se pueden crear ciclos y no va a correr Kruskal correctamente.

## 4. Componentes
¿Qué representa una componente en Union-Find?

Un punto para unir las aristas.

## 5. Representantes
¿Qué significa la raíz de un elemento?

El punto de partida para el aloritmo.

## 6. `find`
¿Qué operación realiza `find`?

Buscar los vertices para hacer el arbol.

## 7. `union`
¿Por qué conviene que `union` devuelva un booleano?

Porq nos permite ver si hay qu cabiar algo en el códio.

## 8. Compresión
¿Qué cambia y qué no cambia con la compresión de caminos?

Cambia la manera en la que se entienden los caminos y lo se mantiene la forma en la que se crean los caminos.

## 9. Unión por tamaño
¿Por qué se coloca el árbol pequeño debajo del grande?

Porque si no se generan problemas.

## 10. Invariantes
¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?

Los caminos ya recorridos.

## 11. Kruskal
¿Cuál es la operación dominante de Kruskal?

Elejir los caminos correspondientes.

## 12. Grafo desconectado
¿Por qué Kruskal puede terminar con un bosque?

Porque crea varios arboles y luego elige el optimo.

## 13. Pesos negativos
¿Por qué Kruskal acepta pesos negativos y Dijkstra no?

Porque Kruskal permite filtrar.
## 14. Empates
¿Por qué puede haber varios árboles de expansión mínima?

Porque podemos ponderar las opciones que tenemos y pues elegir el más optimo.

## 15. Complejidad
¿Qué parte domina la complejidad de Kruskal?

La ponderacion entre arboles.

## 16. Comparación
Compara cola, deque, heap y Union-Find según la operación que optimizan.

Lo que cambia más que nada es la forma en la que funcionan, ya que si bien todas son una especie de arbol pero con diferentes caracteristicas, depemndiendo de lo que necesitemos.

## 17. Producción
¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?

Nos podría arrojar un valor negativo, lol.

## 18. Cierre
¿Qué estructura se necesitaría para procesar tareas según dependencias?

alguno como min-heap maybe.