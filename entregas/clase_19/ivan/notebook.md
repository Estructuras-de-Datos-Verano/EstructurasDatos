# Notebook - José Iván Reyna Blanco

## Pregunta inicial
**¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?**
Se logra seleccionando iterativamente las tareas sin prerrequisitos pendientes[cite: 1]. Esto se gestiona registrando los grados de entrada de cada nodo y usando una cola para almacenar y procesar aquellos que se reduzcan a cero[cite: 1].

## 1. Presentación de la clase

**En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?** Consiste en elegir de manera reiterada alguna actividad o asignatura que no tenga ninguna restricción de precedencia activa.

## 2. El nuevo problema: dependencias

**¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?** Es obligatorio finalizar primero Algoritmos y Optimización. Existen múltiples soluciones válidas debido a que hay tareas independientes entre sí que pueden alternar su orden sin violar los prerrequisitos individuales.

## 3. Interpretación de aristas dirigidas

**¿Por qué A → B y B → A representan restricciones diferentes?** Establecen un vínculo asimétrico: `A → B` impone que A precede estrictamente a B, mientras que `B → A` invierte por completo la condición, exigiendo que B concluya antes de que A pueda comenzar.


## 4. Qué es un DAG

**¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?** Porque genera una contradicción irresoluble donde cada elemento exige la finalización previa del siguiente de forma circular. Para que exista una secuencia lineal válida, el grafo obligatoriamente debe carecer de ciclos.

## 5. Ejemplos con y sin ciclos

**En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?**
Resolver la zona acíclica no soluciona el bloqueo permanente en A, B y C causado por su ciclo cerrado. Procesar un fragmento libre de ciclos no valida la viabilidad del grafo en su totalidad.

## 6. Grado de entrada

**¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?**
* **Algoritmos**: Tiene un grado de entrada de 1, ya que depende directamente de Estructuras de Datos.
* **Optimización**: Tiene un grado de entrada de 1, puesto que espera a que concluya Álgebra.
* **Proyecto Final**: Tiene un grado de entrada de 2, debido a que requiere completar tanto Algoritmos como Optimización.


## 7. Nodos disponibles

**¿En qué momento exacto debe encolarse Estructuras de Datos?** Justo en el instante en que sus prerrequisitos pendientes caen a cero, lo cual sucede inmediatamente después de haber procesado Programación y Matemáticas Discretas.

## 8. Descubrimiento de Kahn

**¿Qué representa disminuir en uno el grado de entrada de un vecino?** Indica el cumplimiento exitoso de una de las restricciones previas indispensables para habilitar dicho nodo.

## 9. Ejecución manual

**Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?** En el paso 3, el nodo actual es C, el vecino es D, el grado anterior es 1 y el grado nuevo es 0; la acción es encolar D, quedando el orden parcial en `A, B, C`. En el paso 4, el nodo actual es D, no hay vecinos, la acción es terminar y el orden final es `A, B, C, D`.

## 10. Uso de la cola

**¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?**
Utilizar `collections.deque` garantiza operaciones en O(1) con `append` y `popleft`, simplificando la práctica para evitar que posibles fallos en estructuras enlazadas propias interfieran con el aprendizaje del orden topológico.


## 11. Invariantes

**¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?**
Se rompe la regla fundamental que estipula que únicamente los elementos con cero dependencias activas (grado de entrada actual idéntico a cero) pueden ingresar a la estructura de disponibles.


## 12. Implementación paso a paso

**¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?**
1. **Grafo normalizado**: Copia depurada y homogénea de la estructura de adyacencia.
2. **Diccionario de grados**: Registro numérico de las dependencias entrantes de cada nodo.
3. **Cola de disponibles**: Estructura para alojar temporalmente los elementos libres con grado cero.
4. **Lista de orden**: Secuencia final donde se guarda el recorrido lineal definitivo.


## 13. Detección de ciclos
**¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?**
Revela que ciertos nodos se quedaron bloqueados indefinidamente con grados mayores a cero debido a una dependencia circular, interrumpiendo el flujo antes de abarcar la totalidad de los elementos del grafo.


## 14. BFS frente a Kahn

**¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?**
BFS añade cualquier nodo adyacente no visitado al instante de descubrirlo; Kahn restringe el ingreso y exige rigurosamente que todas las tareas predecesoras del nodo hayan sido resueltas (grado reducido a cero).


## 15. Órdenes no únicos

**¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?**
Porque ignora que la combinación `B, A, C` resulta igualmente válida al no existir restricciones mutuas entre A y B. Evaluar contra un único molde estricto descartaría soluciones técnicamente impecables.


## 16. Validación de un orden

**Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.**
* `B,A,C`: **Válida**. Satisface el orden de todas las aristas.
* `C,A,B`: **Inválida**. C antecede a A, infringiendo la restricción de que A debe ir antes que C (`A → C`).
* `A,C`: **Inválida**. Omite por completo al nodo B, incumpliendo la longitud y cobertura del grafo.
* `A,A,C`: **Inválida**. Rompe la propiedad de unicidad al contener elementos duplicados.


## 17. Normalización y dependencias duplicadas

**¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?**
Provocaría que el nodo se quede bloqueado sin alcanzar jamás el grado cero tras procesar su origen, o alteraría el flujo generando conteos negativos incorrectos en reducciones posteriores.

## 18. Casos límite
**¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?**
Deben incluirse exactamente una vez en la lista final, puesto que carecen de dependencias desde el inicio y se encuentran disponibles de forma inmediata en la cola de procesamiento.

## 19. Problema de cursos
**¿Qué significa exactamente el par (2, 5) en ordenar_cursos?**
Determina que la asignatura 2 funciona como prerrequisito obligatorio para cursar la asignatura 5, representando una arista dirigida con sentido `2 → 5'.

## 20. CSES Course Schedule
**¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?**
Requiere decrementar en uno las conexiones para ajustar el formato 1-based al 0-based de la función, y volver a sumar uno antes de imprimir[cite: 1]. Si hay un ciclo, se muestra `IMPOSSIBLE`.



## 21. LeetCode Course Schedule
**¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?**
LeetCode trabaja con la nomenclatura invertida `[curso, prerrequisito]`, por lo que se deben transformar las parejas previamente; luego, el problema 207 recurre a `puede_completar_cursos` y el 210 a `ordenar_cursos`.



## 22. Complejidad
**¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?**
Porque los procesos operan de manera secuencial y aditiva: cada vértice se procesa y encola a lo sumo una vez, y cada conexión se evalúa una única ocasión, manteniendo un costo lineal de O(V+E).



## 23. Pruebas
**¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?**
Comprobando criterios generales en lugar de una cadena fija: constatar que estén todos los componentes sin repeticiones ni extraños, y cerciorarse de que para cada arista `u → v`, el índice de `u` sea menor al de `v`.


## 24. Extensión con heap
**¿Qué cambio de contrato justifica sustituir la cola por un heap?**
Se fundamenta si la especificación del problema obligara a proporcionar el orden lexicográficamente menor, forzando al algoritmo a extraer siempre el nodo disponible con el identificador más bajo.

## 25. Cierre integrador
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?**
Evaluamos la tarea repetitiva clave del algoritmo (como buscar mínimos, procesar restricciones o avanzar por niveles) para emparejarla con la herramienta óptima heap, cola + grados, deque o Union-Find.