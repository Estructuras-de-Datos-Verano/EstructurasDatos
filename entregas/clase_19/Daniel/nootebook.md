# Cuaderno de trabajo — Clase 19

## Pregunta inicial

Para encontrar un orden válido tenemos que calcular los grados de entrada de cada tarea, ya que esto nos permite identificar cuáles no tienen requisitos pendientes y procesarlas secuencialmente liberando las dependencias de las siguientes.

## Respuestas 1–25

### 1. Presentación de la clase
Para construir un plan válido tenemos que repetir la operación de elegir una tarea sin requisitos pendientes, ya que al encolar solo nodos con grado cero garantizamos que no se viole ninguna prelación del grafo.

### 2. El nuevo problema: dependencias
Antes de Proyecto Final se debe completar la rama de Algoritmos y Optimización; luego, sabemos que puede haber más de una respuesta correcta para esto porque existen tareas paralelas independientes que no poseen un orden jerárquico entre sí.

### 3. Interpretación de aristas dirigidas
Representan restricciones diferentes ya que A a B obliga a procesar $A$ primero, mientras que B a A invierte completamente el contrato de precedencia.

### 4. Qué es un DAG
Impide cualquier ordenamiento ya que se genera una dependencia circular donde cada nodo del ciclo exige que el otro se complete antes, lo que invalida una ordenación lineal.

### 5. Ejemplos con y sin ciclos
No se puede devolver un orden parcial para esto, ya que el contrato del algoritmo exige validar el grafo completo y la presencia del ciclo bloquea indefinidamente a los nodos involucrados.

### 6. Grado de entrada
En el problema conductor, Algoritmos tiene grado 1, Optimización tiene grado 1 y Proyecto Final tiene grado 2, ya que esos son los prerrequisitos directos que apuntan a ellos.

### 7. Nodos disponibles
Estructuras de Datos debe encolarse en el momento exacto en que su grado de entrada actual pasa a ser cero, luego de que Programación y Matemáticas Discretas hayan sido procesadas.

### 8. Descubrimiento de Kahn
Representa que un prerrequisito ya se cumplió; para esto, actualizamos el estado reduciendo el contador de restricciones pendientes de dicho nodo vecino.

### 9. Ejecución manual
* Paso 3: Cola `[C]`, Actual `C`, Vecino `D`, Grado anterior `1`, Grado nuevo `0` (encolar D), Orden `[A, B, C]`.
* Paso 4: Cola `[D]`, Actual `D`, termina la ejecución con el orden final `[A, B, C, D]` u `[B, A, C, D]`.

### 10. Uso de la cola
Se utiliza `deque` porque ofrece inserciones y extracciones eficientes en O(1); para esto, la política se mantiene idéntica sin importar si la librería es interna o propia.

### 11. Invariantes
Se viola el invariante central que dicta que todo nodo en la cola debe tener grado actual cero, ya que se estaría procesando una tarea con requisitos pendientes.

### 12. Implementación paso a paso
Tenemos que mantener el grafo normalizado, un diccionario de grados de entrada, la cola de nodos disponibles y la lista del orden final para asegurar el contrato.

### 13. Detección de ciclos
Es evidencia de un ciclo ya que los nodos atrapados en la dependencia circular nunca alcanzan el grado cero, luego la cola se vacía antes de cubrirlos a todos.

### 14. BFS frente a Kahn
La diferencia decisiva es que BFS encola al descubrir el nodo por primera vez, mientras que Kahn exige estrictamente que el grado de entrada llegue a cero.

### 15. Órdenes no únicos
Es incorrecto porque ambas secuencias `[A, B, C]` y `[B, A, C]` son matemáticamente válidas, ya que $A$ y $B$ no tienen dependencias entre sí.

### 16. Validación de un orden
* `B,A,C`: Válida, respeta las restricciones.
* `C,A,B`: Inválida, $C$ aparece antes que sus prerrequisitos.
* `A,C`: Inválida, falta el nodo $B$.
* `A,A,C`: Inválida, tiene elementos duplicados.

### 17. Normalización y dependencias duplicadas
No debe aumentarlo dos veces ya que provocaría un bloqueo artificial, provocando que el grado del vecino nunca llegue a cero al procesar su origen.

### 18. Casos límite
Deben aparecer al inicio o mezclados como disponibles inmediatos, ya que al tener grado inicial cero no dependen de ninguna otra tarea para ejecutarse.

### 19. Problema de cursos
Significa que el curso 2 es un prerrequisito obligatorio del curso 5; para esto, tenemos que procesar el nodo 2 antes de poder liberar el acceso al nodo 5.

### 20. CSES Course Schedule
Necesita mapear los índices de 1-based a 0-based restando uno; luego, si se detecta un ciclo durante el proceso se debe imprimir la palabra `IMPOSSIBLE`.

### 21. LeetCode Course Schedule
Se relacionan directamente delegando la lógica central; para esto, solo adaptamos la convención inversa del par `[curso, prerrequisito]` antes de invocar el ordenamiento.

### 22. Complejidad
No implica $O(VE)$ ya que el bucle procesa cada nodo exactamente una vez y reduce cada arista una única vez a lo largo de toda la ejecución consecutiva.

### 23. Pruebas
Tenemos que usar una validación por propiedades inspeccionando que se cumpla la relación de índices `posicion[u] < posicion[v]` para cada arista del grafo.

### 24. Extensión con heap
Justifica el cambio cuando el contrato exige devolver el orden lexicográficamente mínimo, ya que requerimos extraer siempre el menor elemento disponible.

### 25. Cierre integrador
Identificamos la operación analizando el criterio de selección repetido; luego elegimos la estructura idónea, que en este caso es una cola combinada con un vector de grados.