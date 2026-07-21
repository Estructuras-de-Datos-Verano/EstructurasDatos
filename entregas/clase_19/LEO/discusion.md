# Discusión técnica — Clase 19 - Leonardo Daniel Arenas Serafín

## 1. Dependencias
#### ¿Qué significa una arista \(u \to v\) en un grafo de dependencias?
Que v depende de u

## 2. DAG
#### ¿Qué es un grafo dirigido acíclico y por qué es necesario?
Es un grafo en donde sus aristas tienen sentido y es acíclico porque si no lo fuera, siempre habría interdependencia y no se podría hacer mada

## 3. Grado de entrada
#### ¿Qué representa el grado de entrada de un nodo?
De cuántos nodos depende

## 4. Nodos disponibles
#### ¿Por qué un nodo con grado cero puede procesarse?
Porque no tiene prerrequisitos

## 5. Actualización
#### ¿Qué representa disminuir el grado de un vecino?
Que uno de sus requisitos ya fue procesado

## 6. Cola
#### ¿Por qué Kahn utiliza una cola?
Porque se debe de ir procesando en orden de libramiento

## 7. BFS frente a Kahn
#### ¿En qué se parecen y en qué se diferencian?
Se parecen en que ambos van de nodo en nodo, se diferencias en que BFS puede llegar a un nodo de una sola arista a pesar de que haya otras sin procesar, mientras que Kahn pide que todas estén procesadas para poder llegar al siguiente nodo

## 8. Invariantes
#### ¿Qué propiedad debe cumplir todo nodo que está en la cola?
Que tenga grado 0

## 9. Ciclos
#### ¿Cómo detecta Kahn que existe un ciclo?
Cuando la cola está vacía, pero aún no se han procesado los nodos

## 10. Órdenes múltiples
#### ¿Por qué puede haber más de un orden topológico?
Porque pueden existir muchos nodos con grado incial 0 y estos no tienen un orden de procesamiento

## 11. Validación
#### ¿Cómo puede verificarse un orden sin ejecutar nuevamente Kahn?
Metiendo el orden en un conjunto

## 12. Duplicados
#### ¿Por qué conviene eliminar dependencias repetidas?
Porque cada nodo puede tener a lo más un peso de dependencia, pues cada nodo puede procesarse una sola vez

## 13. Nodos aislados
#### ¿Cómo debe aparecer un nodo aislado en el resultado?
Como procesado.

## 14. Cola ligada
#### ¿Podría utilizarse la ColaLigada de la Clase 17?
Sí

## 15. Heap
#### ¿Cuándo convendría sustituir la cola por un heap?
Cuando no solo queremos procesar nodos sin dependencia, sino que además tenemos prioridad

## 16. Complejidad
#### ¿Por qué la complejidad es \(O(V+E)\)?
Porque cada fase tiene operaciones consecutivas, mas no multiplicativas

## 17. Comparación
#### Compara BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn.
BFS solo busca todos los caminos posibles. 0-1 BFS tiene un orden de prioridad por pesos. Dijkstra sopesa pesos mínimos para crear un solo camino. Estos 3 dependen de un origen. Kruskal solamente verifica cuál es la opción mínima para crear una red global entre los nodos, no depende de un origen. Kahn busca saber el orden de procesamiento de nodos que dependen de otros.

## 18. Cierre
#### ¿Cuál es la operación dominante del ordenamiento topológico?
Verificar si un nodo tiene dependencia para ver si puede ser encolado o no para su procesamiento.