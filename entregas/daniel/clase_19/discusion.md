# Discusión técnica — Clase 19

## 1. Dependencias
Significa que el nodo $u$ debe completarse obligatoriamente antes que el nodo $v$; para esto, la flecha establece un contrato de precedencia unidireccional que prohíbe invertir el orden de ejecución.

## 2. DAG
Es un grafo dirigido acíclico, el cual es completamente necesario ya que la presencia de cualquier ciclo genera un bloqueo mutuo que imposibilita definir una secuencia lineal válida.

## 3. Grado de entrada
Representa la cantidad total de aristas entrantes directas que posee un nodo, ya que esto nos indica cuantitativamente cuántos requisitos previos siguen pendientes al inicio.

## 4. Nodos disponibles
Porque al tener grado de entrada actual cero significa que ya no cuenta con restricciones pendientes; luego, puede procesarse de inmediato sin alterar el orden jerárquico del sistema.

## 5. Actualización
Representa que una tarea previa ya se completó de forma exitosa, ya que al restar uno en el contador de grados de sus vecinos reflejamos que una dependencia quedó satisfecha.

## 6. Cola
Se utiliza para almacenar temporalmente los elementos que van quedando listos para ejecución; para esto, `deque` nos garantiza extraer y añadir nuevas tareas en tiempo constante O(1).

## 7. BFS frente a Kahn
Se parecen en que ambos utilizan una cola como estructura auxiliar, pero se diferencian decisivamente en la regla de encolado ya que Kahn exige que el grado llegue estrictamente a cero.

## 8. Invariantes
El invariante central dicta que todo nodo que ingrese a la cola debe poseer un grado de entrada actual exactamente igual a cero, ya que de lo contrario el flujo sería incorrecto.

## 9. Ciclos
Lo detecta al verificar si la cantidad de nodos agregados al orden final es menor al total del grafo normalizado, ya que los elementos del ciclo jamás alcanzan el grado cero.

## 10. Órdenes múltiples
Ocurre porque existen múltiples fuentes o tareas paralelas independientes entre sí; luego, procesar cualquiera de ellas primero resulta matemáticamente correcto ante el contrato.

## 11. Validación
Se verifica indexando las posiciones de la secuencia resultante; para esto, tenemos que recorrer las aristas originales y confirmar que se cumpla la propiedad `posicion[u] < posicion[v]`.

## 12. Duplicados
Conviene eliminarlos durante la normalización ya que contar dos veces una misma arista provocaría que el grado quede sobreestimado, haciendo que el nodo nunca se libere.

## 13. Nodos aislados
Deben aparecer directamente en el resultado final mezclados entre las fuentes iniciales, ya que al no poseer dependencias entran de inmediato a la cola con grado cero.

## 14. Cola ligada
Sí podría utilizarse perfectamente reutilizando su contrato operativo, ya que la estructura auxiliar solo implementa la política FIFO sin alterar la lógica de grados del algoritmo.

## 15. Heap
Convendría realizar esa sustitución si el contrato técnico cambiara para exigir el orden lexicográficamente mínimo, ya que necesitaríamos extraer siempre el menor valor disponible.

## 16. Complejidad
Es de $O(V+E)$ ya que cada vértice se encola y procesa una sola vez; luego, cada arista se examina una cantidad constante de veces de manera consecutiva y no multiplicativa.

## 17. Comparación
BFS explora niveles sin pesos y 0-1 BFS atiende costos binarios; luego Dijkstra extrae distancias con heap, Kruskal conecta componentes con Union-Find y Kahn ordena dependencias usando grados.

## 18. Cierre
La operación dominante consiste en identificar y procesar repetidamente aquellos nodos cuyos prerrequisitos se hayan reducido a cero, ya que esto destraba el flujo secuencial.