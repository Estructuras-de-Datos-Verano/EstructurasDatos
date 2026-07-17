# Notebook Clase 19 Max

## Sección 0 (Pregunta inicial)

¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?

## Sección 1 (Presentación de la clase)

En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?

## Sección 2 (El nuevo problema: dependientas)

¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?

## Sección 3 (Interpretación de aristas dirigidas)

¿Por qué A → B y B → A representan restricciones diferentes?

## Sección 4 (Qué es un DAG)

¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?

## Sección 5 (Ejemplos con y cin ciclos)

En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?

## Sección 6 (Grado de entrada)

¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?

## Sección 7 (Nodos disponible)

¿En qué momento exacto debe encolarse Estructuras de Datos?

## Sección 8 (Descubrimient de Kahn)

¿Qué representa disminuir en uno el grado de entrada de un vecino?

## Sección 9 (Ejecución manual)

Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?

## Sección 10 (Uso de la cola)

¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?

## Sección 11 (Invariantes)

¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?

## Sección 12 (Implementación paso a paso)

¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?

## Sección 13 (Detección de ciclos)

¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?

## Sección 14 (BFS frente a Kahn)

¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?

## Sección 15 (Órdenes no únicos)

¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?

## Sección 16 (Validación de un orden)

Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.

## Sección 17 (Normalización y dependencias)

¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?

## Sección 18 (Casos límite)

¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?


## Sección 19 (Problemas de curso)

¿Qué significa exactamente el par (2, 5) en ordenar_cursos?

## Sección 20 (CSES Course Schedule)

¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?

## Sección 21 (LeetCode Course Schedule)

¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?

## Sección 22 (Complejidad)

¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?

## Sección 23 (Pruebas)

¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?

## Sección 24 (Extensión con heap)

¿Qué cambio de contrato justifica sustituir la cola por un heap?

## Sección 25 (Cierre integrador)

Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?

## Sección 26 ()



## Sección 27 ()