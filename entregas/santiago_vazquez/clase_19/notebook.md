notebook.md
Pregunta inicial

Ejecutando iterativamente las tareas que ya no tienen prerrequisitos pendientes y actualizando el estado de las tareas sucesoras.

1. Presentación de la clase

Decidir qué tarea está disponible en este momento, registrarla y reducir los requisitos de las tareas que esperaban por ella.

2. El nuevo problema: dependencias

Algoritmos y Optimización deben concluir antes. Hay múltiples respuestas válidas porque hay ramas paralelas que no tienen un orden estricto entre sí.

3. Interpretación de aristas dirigidas

Porque es un grafo dirigido y no una relación simétrica; invertir la dirección cambia completamente qué tarea debe completarse primero.

4. Qué es un DAG

Porque obliga circularmente a que A ocurra antes que B, B antes que C y C antes que A, creando restricciones imposibles de satisfacer.

5. Ejemplos con y sin ciclos

Porque A, B y C mantienen dependencias circulares y nunca llegarán a la cola, incumpliendo el objetivo de ordenar todo el grafo.

6. Grado de entrada

Algoritmos inicia con 1, Optimización con 1 y Proyecto Final con 2.

7. Nodos disponibles

Exactamente en el instante en que su grado de entrada llega a cero, lo cual ocurre tras procesar tanto Programación como Matemáticas Discretas.

8. Descubrimiento de Kahn

Representa que una de las dependencias requeridas por ese vecino ha sido completada satisfactoriamente.

9. Ejecución manual

Paso 3: desencolar C, vecino D, grado nuevo 0, encolar D, orden A,B,C. Paso 4: desencolar D, orden A,B,C,D, y terminar.

10. Uso de la cola

Porque deque provee inserción y extracción nativas en O(1), permitiendo enfocarse en la lógica topológica sin arrastrar posibles errores de implementaciones propias.

11. Invariantes

Se viola el invariante fundamental que dicta que todo nodo presente en la cola debe tener un grado de entrada actual estrictamente cero.

12. Implementación paso a paso

normalizado para representación coherente, grados para conteo de requisitos, disponibles como cola de ejecución, y orden para el resultado.

13. Detección de ciclos

Significa que al detenerse el algoritmo, algunos nodos no pudieron liberar sus dependencias, evidenciando una estructura circular imposible de resolver.

14. BFS frente a Kahn

BFS encola un nodo apenas es descubierto, mientras que Kahn exige obligatoriamente esperar hasta que todas sus dependencias previas sean procesadas.

15. Órdenes no únicos

Porque los nodos independientes A y B pueden procesarse en cualquier orden inicial, haciendo a la secuencia [B, A, C] igualmente válida.

16. Validación de un orden

B,A,C: válida. C,A,B: falla por orden invertido. A,C: falla por longitud incorrecta. A,A,C: falla por tener elementos repetidos.

17. Normalización y dependencias duplicadas

Porque al procesarse la tarea original, su reducción ocurrirá una sola vez, dejando falsamente bloqueado al nodo destino.

18. Casos límite

Deben aparecer incluidos en el orden final una única vez, dado que carecen de dependencias y entran a la cola de disponibles desde el inicio.

19. Problema de cursos

Significa de manera estricta que aprobar el curso 2 es un requisito previo indispensable para poder cursar el 5.

20. CSES Course Schedule

Requiere leer índices 1-based, restarles 1 para Kahn, y sumarles 1 en la salida. Si existe un ciclo se imprime explícitamente IMPOSSIBLE.

21. LeetCode Course Schedule

LC 207 consulta puede_completar_cursos y LC 210 usa ordenar_cursos. Ambos invierten la convención, por lo que los pares deben adaptarse antes de delegar el trabajo.

22. Complejidad

Porque cada nodo disponible se extrae exactamente una vez y cada arista de la red se verifica y reduce solo una vez, sumando linealmente O(V+E).

23. Pruebas

Debe verificarse evaluando el cumplimiento de propiedades: cobertura total de nodos, ausencia de duplicados y respeto de cada precedencia.

24. Extensión con heap

El uso del heap se justifica únicamente si el problema exige devolver el orden lexicográficamente mínimo en vez de cualquier secuencia válida.

25. Cierre integrador