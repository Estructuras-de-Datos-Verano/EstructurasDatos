1. Dependencias

Significa estrictamente que la tarea A debe finalizar por completo antes de poder iniciar la tarea B.  

2. DAGEs un grafo con dirección y sin retornos circulares; es indispensable porque un ciclo imposibilita establecer una precedencia temporal válida.  

3. Grado de entrada

Representa la cantidad exacta de prerrequisitos que todavía están pendientes para poder ejecutar ese nodo.  

4. Nodos disponibles

Porque al llegar a cero requisitos pendientes, ya no existe ninguna restricción temporal que impida su ejecución inmediata.  

5. Actualización

Indica que una de las dependencias requeridas por ese nodo acaba de finalizar satisfactoriamente.  

6. Cola

Para manejar en O(1) los nodos independizados secuencialmente, asegurando procesarlos sin introducir sobrecostos de ordenamientos innecesarios.  

7. BFS frente a Kahn

Comparten el uso de una cola; difieren en que BFS procesa en el primer descubrimiento y Kahn restringe el ingreso hasta satisfacer todos los requisitos.  

8. Invariantes

Es indispensable que todo nodo que ingrese a la cola tenga su grado de entrada actual en estricto cero.  

9. Ciclos

Al finalizar la ejecución, la longitud del orden procesado resultará estrictamente menor que la cantidad total de nodos normalizados.  

10. Órdenes múltiples

Porque al haber ramas desconectadas o paralelas en el flujo, múltiples nodos alcanzan grado cero a la vez y admiten permutaciones. 

11. Validación

Mapeando índices y comprobando que para cada arista dirigida, la posición del origen sea numéricamente inferior a la del destino.  

12. Duplicados

Porque una dependencia multiplicada infla el grado de entrada, provocando que el nodo se quede atascado en grados positivos permanentemente.  

13. Nodos aisladosDeben figurar exactamente una vez dentro de la secuencia final del orden topológico.  

14. Cola ligada

Sí es factible, dado que expone el mismo contrato y tiempo constante para encolar y desencolar elementos.  

15. Heap

Se implementa si la especificación requiere explícitamente obtener el orden alfabético o numérico más pequeño en cada iteración.  

16. Complejidad

Cada nodo se procesa una única vez para encolarlo, y cada arista individual se evalúa una sola vez en el bucle interior, resultando aditivo.  

17. ComparaciónBFS/Cola (niveles), 0-1 BFS/Deque (costos binarios), Dijkstra/Heap (costos variables), Kruskal/Union-Find (componentes), Kahn/Cola+Grados (dependencias).  

18. Cierre

La repetición constante de localizar, extraer y procesar tareas que hayan alcanzado un estado libre de dependencias previas.  