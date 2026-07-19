# Discusión 

## 1. Dependencias
**¿Qué implica la conexión u -> v?**
Indica que la tarea u es un requisito previo indispensable para v. Esta relación establece un orden obligatorio de ejecución.

## 2. DAG
**¿Qué es un DAG y su utilidad?**
Es un grafo con dirección y sin ciclos cerrados. Es indispensable porque un orden topológico válido solo existe si no hay bucles.

## 3. Grado de entrada
**¿Qué indica el grado de entrada?**
Mide cuántas conexiones apuntan hacia un nodo. En dependencias, refleja los requisitos pendientes antes de iniciar dicha labor.

## 4. Nodos disponibles
**¿Por qué procesar nodos con grado cero?**
Porque al carecer de requisitos pendientes, están totalmente libres. Pueden ejecutarse al instante sin romper el orden lógico de la red.

## 5. Actualización
**¿Qué significa reducir el grado de un vecino?**
Simboliza que una de sus tareas previas acaba de completarse. Esto acerca al nodo a quedar totalmente liberado para su ejecución.

## 6. Cola
**¿Por qué usar una cola en Kahn?**
Sirve para guardar y extraer rápidamente (en tiempo constante) los nodos liberados. Evita reescanear todo el grafo buscando tareas listas.

## 7. BFS frente a Kahn
**Diferencias entre algoritmos:**
BFS encola cualquier vecino apenas lo descubre. Kahn exige que el vecino resuelva todas sus dependencias (grado cero) antes de encolarlo.

## 8. Invariantes
**Regla de los nodos encolados:**
La condición inquebrantable es que todo elemento que ingresa a la cola debe tener exactamente cero dependencias pendientes.

## 9. Ciclos
**Detección de ciclos en Kahn:**
Si la cantidad de nodos ordenados al final es menor al total de nodos originales, hay un ciclo. Indica que algunos elementos quedaron bloqueados.

## 10. Órdenes múltiples
**¿Por qué hay varias soluciones?**
Si múltiples tareas quedan libres a la vez, cualquiera puede procesarse primero. El orden entre ellas no altera las restricciones principales.

## 11. Validación
**¿Cómo auditar un resultado?**
Guardando la posición de cada nodo en la secuencia final. Luego, para toda arista u -> v, se verifica que u aparezca antes que v.

## 12. Duplicados
**¿Por qué limpiar dependencias repetidas?**
Para no inflar los requisitos de un nodo, lo cual causaría bloqueos permanentes o conteos negativos. Normalizar asegura una contabilidad real.

## 13. Nodos aislados
**Manejo de elementos sueltos:**
Los nodos sin dependencias arrancan con grado cero. Entran directo a la cola inicial y figuran exactamente una sola vez en el resultado.

## 14. Cola ligada
**¿Sirve nuestra propia ColaLigada?**
Totalmente, cualquier estructura FIFO funciona. Sus métodos básicos de encolar y desencolar bastan para gestionar el flujo de tareas.

## 15. Heap
**¿Cuándo usar un min-heap?**
Cuando el problema exija un orden secundario específico, como el alfabético. El heap garantiza extraer siempre el nodo prioritario disponible.

## 16. Complejidad
**Razón del costo O(V+E):**
Las operaciones son consecutivas y aditivas. Cada vértice y conexión se evalúa una sola vez, manteniendo un rendimiento puramente lineal.

## 17. Comparación
**Resumen de algoritmos de grafos:**
BFS agrupa por niveles; 0-1 BFS usa deques para costos binarios; Dijkstra minimiza pesos con heaps; Kruskal previene ciclos; Kahn ordena dependencias.

## 18. Cierre
**Operación central del algoritmo:**
La acción principal e iterativa es identificar, extraer y procesar aquellas tareas que ya no tengan dependencias pendientes.