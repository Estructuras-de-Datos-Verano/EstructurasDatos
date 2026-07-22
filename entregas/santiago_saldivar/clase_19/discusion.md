# Discusión técnica — Clase 19

## 1. Dependencias
¿Qué significa una arista \(u \to v\) en un grafo de dependencias?
Que u es requisito de v

## 2. DAG
¿Qué es un grafo dirigido acíclico y por qué es necesario?
Uno que no permite que se regrese a una arista formando un bucle
porque un bucle correría por siempre y se rompería
## 3. Grado de entrada
¿Qué representa el grado de entrada de un nodo?
Los requisitos sin cumplir
## 4. Nodos disponibles
¿Por qué un nodo con grado cero puede procesarse?
Porque no tiene pendientes
## 5. Actualización
¿Qué representa disminuir el grado de un vecino?
Que se cumple un requisito
## 6. Cola
¿Por qué Kahn utiliza una cola?
Para sacar los más antiguos
## 7. BFS frente a Kahn
¿En qué se parecen y en qué se diferencian?
BFS contempla una arista para cada nodo
Kahn necesita varios requisitos
## 8. Invariantes
¿Qué propiedad debe cumplir todo nodo que está en la cola?
grado 0
## 9. Ciclos
¿Cómo detecta Kahn que existe un ciclo?
Si una tarea es requisito de su requisito
## 10. Órdenes múltiples
¿Por qué puede haber más de un orden topológico?
Porque se pueden cumplir ciertos requisitos en cierto orden si dependen de cosas distintas
## 11. Validación
¿Cómo puede verificarse un orden sin ejecutar nuevamente Kahn?
Comparando
## 12. Duplicados
¿Por qué conviene eliminar dependencias repetidas?
Para evitar redundancias y errores en los grados
## 13. Nodos aislados
¿Cómo debe aparecer un nodo aislado en el resultado?
sin requisitos
## 14. Cola ligada
¿Podría utilizarse la ColaLigada de la Clase 17?
Sí
## 15. Heap
¿Cuándo convendría sustituir la cola por un heap?
Si se pide mínimo
## 16. Complejidad
¿Por qué la complejidad es \(O(V+E)\)?
Porque las fases son consecutivas

## 17. Comparación
Compara BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn.
BFS busca rutas
0-1 BFS también, pero hay aristas que pueden valer 0
Dijkstra contempla pesos distintos para las aristas
Kruskal conecta todos los nodos
Kahn contempla varios requisitos 
## 18. Cierre
¿Cuál es la operación dominante del ordenamiento topológico?
Cumplir los requisitos
