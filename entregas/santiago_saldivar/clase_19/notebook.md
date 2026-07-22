# Clase 19 asíncrona: ordenamiento topológico y Kahn

## Pregunta inicial

**¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?**
Asignando ciertas prioridades. 

## 1. Presentación de la clase

**Pregunta:** En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?
Completar todas las tareas pendientes y elegir la mejor forma de hacerlo.

## 2. El nuevo problema: dependencias
**Pregunta:** ¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?
Que se complete lo necesario
Porque puede cumplirse todo en orden distinto

## 3. Interpretación de aristas dirigidas
**Pregunta:** ¿Por qué A → B y B → A representan restricciones diferentes?
Porque implican distinto orden

## 4. Qué es un DAG
**Pregunta:** ¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?
Porque ninguna secuencia lineal lo satisface todo

## 5. Ejemplos con y sin ciclos

**Pregunta:** En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?
porque no rescata el grafo completo

## 6. Grado de entrada
*Pregunta:** ¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?
3
1
2


## 7. Nodos disponibles
**Pregunta:** ¿En qué momento exacto debe encolarse Estructuras de Datos?
Cuando tenga grado 0, es decir, se hayan encolado sus requisitos


## 8. Descubrimiento de Kahn
**Pregunta:** ¿Qué representa disminuir en uno el grado de entrada de un vecino? 
Que se cumplió un requisito

## 9. Ejecución manual
| Paso | Cola antes | Actual | Vecino | Grado anterior | Grado nuevo | Acción | Orden |
| ---: | --- | --- | --- | ---: | ---: | --- | --- |
| 1 | A, B | A | C | 2 | 1 | sigue bloqueado | A |
| 2 | B | B | C | 1 | 0 | encolar C | A, B |
| 3 | C | C | D | 0 | 1 | encolar | A,B,C |
| 4 | - | D | — | — | — | terminar | A,B,C,D |

## 10. Uso de la cola
**Pregunta:** ¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?
Conerva el orden de aparición entre fuentes

## 11. Invariantes
**Pregunta:** ¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?
Que sólo entran con grado 0

## 12. Implementación paso a paso
**Pregunta:** ¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?
los grados, la cola, las salidas los vecinos

## 13. Detección de ciclos
**Pregunta:** ¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?
Porque deberían ser iguales. Si no lo son, uno está agregando continuamente

## 14. BFS frente a Kahn
**Pregunta:** ¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?
Khan necesita varios requisitos, BFS sólo contempla uno para cada nodo: su rpedecesor

## 15. Órdenes no únicos
**Pregunta:** ¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?
Porque podrían cumplirse las tareas en orden distinto. Sólo necesitamos que se cumplan todas.

## 16. Validación de un orden

**Pregunta:** Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.

## 17. Normalización y dependencias duplicadas
**Pregunta:** ¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?
Porque basta con cumplirse una vez

## 18. Casos límite
**Pregunta:** ¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?
Con grado 0, porque nada los precede

## 19. Problema de cursos
**Pregunta:** ¿Qué significa exactamente el par (2, 5) en ordenar_cursos?
El requisito y el nodo

## 20. CSES Course Schedule
**Pregunta:** ¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?
Restar en los índices cuando se cumpla el requisito.
error

## 21. LeetCode Course Schedule
**Pregunta:** ¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?
Completar curso depende del orden de ordenar
Leetcode pregunta lo mismo que puede completar

## 22. Complejidad
**Pregunta:** ¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?
Porque las fases son consecutivas

## 23. Pruebas
**Pregunta:** ¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?
Tomando en cuenta las posibilidades o dando al grafo una manera de ordenar específica y probar eso

## 24. Extensión con heap
**Pregunta:** ¿Qué cambio de contrato justifica sustituir la cola por un heap?
Prioridades como mínimo o máximo

## 25. Cierre integrador
**Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?
Entiendiendo qué exactamenet pide el problema.