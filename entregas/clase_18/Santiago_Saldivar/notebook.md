# Clase 18 presencial: Union-Find y Kruskal

## Pregunta inicial
**¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?**
Guardando los que ya visitamos

## 1. Presentación de la clase
**Pregunta:** ¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?
Todas las ciudades conectadas.

## 2. Recuperación de estructuras anteriores
**Pregunta:** ¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?
Conectar todos los nodos sin un origen específico.

## 3. Nueva pregunta: conectar toda la red
**Pregunta:** ¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?
Podría ser redundante

## 4. Dijkstra frente a Kruskal

**Pregunta:** ¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?

Dijkstra, cada distancia desde A. Kruskal la suma del conjunto que conecta todo
Dijkstra necesita origen

## 5. Árboles de expansión
**Pregunta:** ¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?
Porque todos están conectados entre sí, sin ciclos ni redundancias

## 6. Por qué evitar ciclos
**Pregunta:** ¿Qué información mínima necesitamos antes de aceptar una arista u–v?
Si ya existe 

## 7. Componentes conexas
**Pregunta:** ¿Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?
Que ahora están conectados y se convierten en un mismo componente

## 8. Necesidad de Union-Find
**Pregunta:** ¿Por qué conviene que union(a, b) devuelva un booleano?
Porque toma una decisión sobre si aceptar o no la arista

## 9. Representación mediante padres
**Pregunta:** ¿Qué condición permite reconocer una raíz en el arreglo padre?
Se apunta a sí 

## 10. Operación find
**Pregunta:** ¿Por qué debemos validar explícitamente los índices negativos?
Porque Union FInd no los acepta

## 11. Operación union
**Pregunta:** ¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?
Una redundancia

## 12. Invariantes
**Pregunta:** ¿Qué invariantes viola padre = [1, 0, 2]?
no existen ciclos salvo el lazo raíz→raíz.

## 13. Compresión de caminos
**Pregunta:** ¿Qué cambia y qué permanece igual durante la compresión de caminos?
Cambia la representación interna y dismunuye el trabajo futuro. No cambian las componentes, tamaños lógicos ni contador.

## 14. Unión por tamaño
**Pregunta:** ¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?

Porque no sube de más

## 15. Ejecución manual de Union-Find
**Pregunta:** ¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?

[0,1,2,3]

## 16. Algoritmo de Kruskal
**Pregunta:** ¿Cómo usa Kruskal el booleano devuelto por union?
Acepta sólo cuando union(u,v) devuelve true

## 17. Ejecución manual de Kruskal

| Paso | Arista | raíces | decisión | elegidas | costo |
| ---: | --- | --- | --- | --- | ---: |
| 1 | C–D:1 | C / D | aceptar | C–D | 1 |
| 2 | A–C:2 | A / C | aceptar | + A–C | 3 |
| 3 | D–E:2 | A / E | aceptar | + D-E | 5 |
| 4 | B–D:3 | A / E | rechazar | - | 0 |

**Pregunta:** ¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?
5
porque se inserta raro en medio

## 18. Grafo desconectado
**Pregunta:** ¿Qué condición permite distinguir un MST completo de un bosque desconectado?
Si todos los nodos se conectan por aristas

## 19. Pesos negativos, empates y casos especiales
**Pregunta:** ¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?
Porque puede haber varios pesos empatados

## 20. Complejidad
**Pregunta:** ¿Qué parte domina la complejidad total de Kruskal?
ordenar

## 21. CSES Road Reparation
**Pregunta:** ¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?
La falta de origen y los númeroes de las ciudades

## 22. LeetCode Redundant Connection
**Pregunta:** ¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?
Redundant tiene una arista extra

## 23. Implementación

**Pregunta:** ¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?
Validar índices, iniciar padres, tamaño cotador. Find y union bien implementados. Normalizar con una copia. 

## 24. Pruebas
**Pregunta:** ¿Qué invariante protege una prueba de unión repetida?
Protege contra la redundancia

## 25. Cierre hacia ordenamiento topológico
**Pregunta:** ¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?
Linked list