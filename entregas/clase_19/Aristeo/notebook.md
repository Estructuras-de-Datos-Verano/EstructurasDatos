# Notebook Clase 19 Aristeo

## Sección 0 (Pregunta inicial)

¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?

Podemos dibujar las tareas como un grafo de conexiones y usar un algoritmo que ordene los pasos asegurando que ningún requisito se quede sin hacer.

## Sección 1 (Presentación de la clase)

En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?

Necesitamos buscar repetidamente qué cursos ya no tienen requisitos pendientes, anotarlos en el plan y quitarlos de la lista de esperas.

## Sección 2 (El nuevo problema: dependientas)

¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?

Por la manera en la que implementamos la estructara es posible que si empezamos en otro punto con el mismo programa no corra de manera correcta

## Sección 3 (Interpretación de aristas dirigidas)

¿Por qué A → B y B → A representan restricciones diferentes?

Porque la dirección de la flecha cambia por completo el sentido de la regla: A -> B significa que primero debes hacer la tarea A, mientras que B -> A significa que la prioridad la tiene B.

## Sección 4 (Qué es un DAG)

¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?

Porque así lo quiso Dios.

## Sección 5 (Ejemplos con y cin ciclos)

En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?

Porque un ordenamiento topológico debe incluir obligatoriamente a todos los nodos del grafo. Dejar nodos fuera no soluciona el problema completo y rompe el objetivo del algoritmo.

## Sección 6 (Grado de entrada)

¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?

Tienen grados o 1 o 0

## Sección 7 (Nodos disponible)

¿En qué momento exacto debe encolarse Estructuras de Datos?

Cuando el grado del nodo sea igual a 0

## Sección 8 (Descubrimient de Kahn)

¿Qué representa disminuir en uno el grado de entrada de un vecino?

Representa que ya completamos uno de sus requisitos previos, por lo que ese nodo vecino está un paso más cerca de quedar completamente liberado.

## Sección 9 (Ejecución manual)

Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?

deberian de aparecer ABCD con 1 0 0 0

## Sección 10 (Uso de la cola)

¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?

Porque deque de Python está optimizada de manera nativa para agregar y sacar elementos por los extremos muy rápido, lo que hace el código más eficiente.

## Sección 11 (Invariantes)

¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?

Se viola la regla de que la cola solo acepta nodos con grado de entrada igual a 0. Si entra con grado 1, se procesaría una tarea sin haber terminado todos sus requisitos obligatorios.

## Sección 12 (Implementación paso a paso)

¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?

La estructura de Union-Find pareciera la más indicada para poder solucionar este problema.

## Sección 13 (Detección de ciclos)

¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?

Porque de esa manera se puede ver si no son diferentes, cuando sea así quiere decir que deberiamos de evitarlo porque hay un posible ciclo

## Sección 14 (BFS frente a Kahn)
¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?

La principal diferencia es que en una metemos los nodos nada más cuando los vamos viendo y en la otra dependemos de los grados que programamos para que no haya errores con el orden.

## Sección 15 (Órdenes no únicos)
¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?

Porque como no están conectados directamente entre ellos, exigir un solo orden generaría errores, ya que cualquiera de los dos podría ir primero por la manera en que se implementa.

## Sección 16 (Validación de un orden)
Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.

Fallan porque no respetan la invariante del orden de los nodos, entonces al hacer los diferentes cambios al resultado ya no coinciden con las restricciones iniciales que les pusimos.

## Sección 17 (Normalización y dependencias)
¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?

Porque si lo aumentamos dos veces el valor se va a pasar y luego el nodo nunca va a llegar a 0, haciendo que el programa no corra de manera correcta y se quede atorado.

## Sección 18 (Casos límite)
¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?

Pueden ir en cualquier lugar del resultado final. Como tienen grado 0 desde el inicio y nadie depende de ellos, no alteran ni rompen ninguna regla del mapa.

## Sección 19 (Problemas de curso)
¿Qué significa exactamente el par (2, 5) en ordenar_cursos?

Significa que para poder hacer uno necesitas primero tener el otro, dependiendo de cómo hayamos adaptado el código para leerlos desde el principio.

## Sección 20 (CSES Course Schedule)
¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?

Necesitamos ajustar los números para que el programa no se salga de la estructura, y si hay ciclo se debería imprimir un mensaje de error diciendo que es imposible hacer el plan.

## Sección 21 (LeetCode Course Schedule)
¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?

Se relacionan en que todas usan básicamente el mismo código que ya programamos, solo que unas te piden el arreglo completo y las otras nada más te regresan si es posible o no.

## Sección 22 (Complejidad)
¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?

Porque por la manera en la que implementamos la estructura, no checamos todos los nodos todas las veces, sino que solo pasamos por los que necesitamos y así evitamos que se tarde tanto.

## Sección 23 (Pruebas)
¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?

Tienes que hacer una prueba que no exija un solo resultado exacto, sino que revise si el orden de los nodos no viola las reglas para que el test no marque errores falsos.

## Sección 24 (Extensión con heap)
¿Qué cambio de contrato justifica sustituir la cola por un heap?

Se justifica si el problema nos exige desempatar de una forma específica cuando hay varias tareas disponibles.
## Sección 25 (Cierre integrador)
Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?

Analizamos qué acción se va a repetir la mayor cantidad de veces y elegimos la estructura que haga esa operación específica en el menor tiempo posible.
