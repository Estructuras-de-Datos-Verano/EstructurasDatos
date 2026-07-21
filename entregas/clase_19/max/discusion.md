# Discusión técnica — Clase 19

## 1. Dependencias
¿Qué significa una arista \(u \to v\) en un grafo de dependencias?

Significa que para poder hacer uno primero tienes que terminar el otro, por la manera en que están conectados en el programa

## 2. DAG
¿Qué es un grafo dirigido acíclico y por qué es necesario?

Es un grafo que no tiene ciclos, y es necesario porque si los tuviera se quedaría atorado y no correría de manera correcta al intentar sacar un orden válido

## 3. Grado de entrada
¿Qué representa el grado de entrada de un nodo?

Representa cuántas cosas necesitas terminar antes de poder procesar ese nodo sin que te genere errores a la hora de correrlo

## 4. Nodos disponibles
¿Por qué un nodo con grado cero puede procesarse?

Porque como ya no depende de nada más para empezar, lo podemos indexar y agregar a la cola luego luego para hacer el resultado

## 5. Actualización
¿Qué representa disminuir el grado de un vecino?

En que de esa manera le decimos al código que ya terminamos un requisito, y así el vecino se acerca a 0 para poder encolarse

## 6. Cola
¿Por qué Kahn utiliza una cola?

Porque de esta manera podemos ir metiendo y sacando los nodos que ya están listos con cierto orden y así adaptar el código más fácil

## 7. BFS frente a Kahn
¿En qué se parecen y en qué se diferencian?

Se parecen en que los dos usan una cola para ir procesando las cosas, pero la diferencia es que Kahn depende totalmente de los grados que programamos para no meter nodos antes de tiempo

## 8. Invariantes
¿Qué propiedad debe cumplir todo nodo que está en la cola?

La invariante es que su valor del grado tiene que ser exactamente 0, ya que si no es así no se podrá agregar de manera correcta a la fila

## 9. Ciclos
¿Cómo detecta Kahn que existe un ciclo?

Porque al final revisamos si el tamaño del resultado no es el mismo que los nodos totales; cuando pasa eso quiere decir que hay un posible ciclo

## 10. Órdenes múltiples
¿Por qué puede haber más de un orden topológico?

Por la manera en la que implementamos la estructura, a veces hay varios nodos en 0 al mismo tiempo y cualquiera de ellos podría ir primero sin generar errores en las restricciones

## 11. Validación
¿Cómo puede verificarse un orden sin ejecutar nuevamente Kahn?

Necesitas revisar que cada nodo en tu resultado respete las dependencias que les pusimos al inicio, para ver si son correctas o si no lo son sin correr todo de nuevo

## 12. Duplicados
¿Por qué conviene eliminar dependencias repetidas?

Porque si no las quitamos el grado aumentaría dos veces, y luego el nodo nunca llegaría a 0, haciendo que el programa falle a la hora de hacer los cambios

## 13. Nodos aislados
¿Cómo debe aparecer un nodo aislado en el resultado?

Debería aparecer en cualquier lado, ya sea al principio o al final, porque como tiene grado 0 desde el inicio no afecta a los otros nodos conectados

## 14. Cola ligada
¿Podría utilizarse la ColaLigada de la Clase 17?

Sí se podría ya que puede implementar la misma política, pero a veces usamos deque u otra cosa para poder adaptar el código en un futuro a algo más que necesitemos

## 15. Heap
¿Cuándo convendría sustituir la cola por un heap?

Cuando el problema te pida que los nodos salgan con un orden extra, de esta manera el heap ayuda a indexar las cosas automáticamente en lugar de la cola normal

## 16. Complejidad
¿Por qué la complejidad es \(O(V+E)\)?

Porque por la manera en que lo programamos no checamos todos los nodos todas las veces, sino que la estructura solo pasa por los vecinos que necesitamos y así evitamos que se tarde de más

## 17. Comparación
Compara BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn.

Todas estas estructuras parecieran las indicadas para diferentes problemas; unas usan colas normales y otras checan los pesos para ordenar las cosas, dependiendo del resultado deseado que el programa necesite correr

## 18. Cierre
¿Cuál es la operación dominante del ordenamiento topológico?

La operación que necesitas repetir es ir bajando los grados de los vecinos hasta llegar a 0 para así agregarlos al resultado