Discusión técnica — Clase 18
1. Problema

¿Qué diferencia existe entre caminos mínimos y árbol de expansión mínima?
Caminos mínimos necesita origen. El otro conecta todo
2. Árbol de expansión

¿Por qué una solución tiene (V-1) aristas?
Porque todos los vértices se conectan y no hay redundancias.
3. Ciclos

¿Por qué se rechaza una arista cuyos extremos ya están conectados?
Para evitar redundancias
4. Componentes

¿Qué representa una componente en Union-Find?
Un subconjunto de nodos conectados entre sí por aristas
5. Representantes

¿Qué significa la raíz de un elemento?
Predecesor. LAs raíces se apuntan a sí
6. find

¿Qué operación realiza find?
Sigue padres hasta encontrar una raíz
7. union

¿Por qué conviene que union devuelva un booleano?
Para que Kruskal decida 

8. Compresión

¿Qué cambia y qué no cambia con la compresión de caminos?
Cambia la representación interna y disminuye el trabajo futuro; no cambian las componentes, tamaños lógicos ni contador.
9. Unión por tamaño

¿Por qué se coloca el árbol pequeño debajo del grande?
Para limitar el tamaño
10. Invariantes

¿Qué invariantes deben mantenerse en los arreglos de padres y tamaños?
1. cada padre es un índice válido;
2. toda cadena termina en una raíz;
3. una raíz es su propio padre;
4. misma raíz equivale a misma componente;
5. el tamaño se consulta en la raíz;
6. componentes coincide con el número de raíces;
7. unión efectiva resta uno; redundante no cambia nada;
8. no existen ciclos salvo el lazo raíz→raíz.
11. Kruskal

¿Cuál es la operación dominante de Kruskal?
En complejidad, ordenar.
12. Grafo desconectado

¿Por qué Kruskal puede terminar con un bosque?
Porque conecta los nodos
13. Pesos negativos

¿Por qué Kruskal acepta pesos negativos y Dijkstra no?
Porque conecta todos los nodos
14. Empates

¿Por qué puede haber varios árboles de expansión mínima?
Porque a veces hay rutas por aristas distintas pero que valen lo mismo
15. Complejidad

¿Qué parte domina la complejidad de Kruskal?
Ordenar
16. Comparación

Compara cola, deque, heap y Union-Find según la operación que optimizan.
Cola optimiza desencolar por atigüedad
deque desencolar en varios casos
heap desencolar según una prioridad, usualmente máximo o mínimo
Union-FInd conecta todos los nodos
17. Producción

¿Qué riesgos tendría implementar Union-Find sin validar índices negativos?
Que el programa se rompe al recibirlos
18. Cierre
¿Qué estructura se necesitaría para procesar tareas según dependencias?
heap