# Clase 19: Discusión
#### Nombre: Patricio Navarro

## 1. Dependencias
**¿Qué significa una arista u -> v en un grafo de dependencias?**
- Significa que la tarea `u` es un requisito estricto y debe completarse antes de poder iniciar la tarea `v`. 

## 2. DAG
**¿Qué es un grafo dirigido acíclico y por qué es necesario?**
- Es un grafo donde las flechas tienen un sentido único y no hay bucles que te hagan regresar al punto de partida. 
- Es necesario porque si existiera un ciclo, las tareas se bloquearían mutuamente y sería imposible organizarlas en una secuencia temporal.

## 3. Grado de entrada
**¿Qué representa el grado de entrada de un nodo?**
- Representa la cantidad de requisitos previos o tareas que un nodo todavía está esperando que se completen.

## 4. Nodos disponibles
**¿Por qué un nodo con grado cero puede procesarse?**
- Porque su grado cero indica que ya no tiene ningún requisito pendiente, por lo que está libre y listo para realizarse sin romper ninguna regla.

## 5. Actualización
**¿Qué representa disminuir el grado de un vecino?**
- Representa que acabas de terminar uno de sus requisitos previos, dejándolo un paso más cerca de estar disponible.

## 6. Cola
**¿Por qué Kahn utiliza una cola?**
- Para ir almacenando de forma eficiente todas las tareas que van llegando a grado cero, permitiendo procesarlas en orden.

## 7. BFS frente a Kahn
**¿En qué se parecen y en qué se diferencian?**
- Se parecen en que ambos utilizan una cola para ir procesando nodos a medida que avanzan. 
- Se diferencian drásticamente en la regla para meterlos: 
    - En BFS un nodo entra apenas es descubierto.
    - En Kahn un nodo debe esperar a que todos sus predecesores hayan terminado antes de poder entrar.

## 8. Invariantes
**¿Qué propiedad debe cumplir todo nodo que está en la cola?**
- Debe tener un grado de entrada actual de exactamente cero.

## 9. Ciclos
**¿Cómo detecta Kahn que existe un ciclo?**
- Al final de la ejecución, cuenta cuántos nodos logró guardar en la lista final y lo compara con el total de nodos del grafo. Si la lista tiene menos nodos, significa que el resto se quedó atrapado en un bucle y nunca llegó a grado cero.

## 10. Órdenes múltiples
**¿Por qué puede haber más de un orden topológico?**
- Porque a menudo se liberan varias tareas al mismo tiempo, cuando tienes más de una tarea con grado cero, puedes hacerlas en el orden que quieras y el resultado global seguirá siendo completamente válido.

## 11. Validación
**¿Cómo puede verificarse un orden sin ejecutar nuevamente Kahn?**
- Comprobando que la lista tenga la longitud correcta, no repita elementos y, lo más importante, revisando cada flecha del grafo original para confirmar que la tarea de origen se colocó en una posición anterior a la tarea de destino.

## 12. Duplicados
**¿Por qué conviene eliminar dependencias repetidas?**
- Porque si una misma flecha se cuenta dos veces, el grado de entrada subirá de más, así cuando termines esa tarea previa, el grado solo bajará en uno y el nodo quedará bloqueado de por vida por un "requisito fantasma".

## 13. Nodos aislados
**¿Cómo debe aparecer un nodo aislado en el resultado?**
- Debe aparecer exactamente una vez en la lista final, como no tiene requisitos de entrada, comienza con grado cero y entra a la cola desde el inicio.

## 14. Cola ligada
**¿Podría utilizarse la ColaLigada de la Clase 17?**
- Sí, porque aplica la misma política fundamental de encolar y desencolar que el algoritmo necesita.

## 15. Heap
**¿Cuándo convendría sustituir la cola por un heap?**
- Cuando el problema tenga una regla extra de desempate; por ejemplo, si te exigen que ante varias tareas disponibles siempre proceses la menor alfabética o numéricamente.

## 16. Complejidad
**¿Por qué la complejidad es O(V+E)?**
- Porque el algoritmo no repite recorridos desde el principio, cada nodo se procesa una única vez, y cada conexión se revisa y reduce una sola vez. Se suma el esfuerzo, no se multiplica.

## 17. Comparación
**Compara BFS, 0-1 BFS, Dijkstra, Kruskal y Kahn.**
- BFS: Procesa caminos por niveles (costo uniforme) usando una cola.
- 0-1 BFS: Da prioridad a los caminos de costo cero usando una deque.
- Dijkstra: Busca el camino más corto evaluando pesos acumulados usando un heap.
- Kruskal: Conecta redes al menor costo consultando componentes con Union-Find.
- Kahn: Ordena dependencias evaluando grados de entrada usando una cola.

## 18. Cierre
**¿Cuál es la operación dominante del ordenamiento topológico?**
- Elegir y procesar las tareas que se encuentran disponibles por no tener requisitos pendientes.