# Cuaderno de trabajo — Clase 19

## Pregunta inicial

**¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?**
Hay que buscar las tareas que no tienen requisitos previos y hacerlas primero (como tener los ingredientes pesados antes de empezar a amasar en Lecaroz). Cada vez que terminas una tarea, "tachas" ese requisito de la lista y revisas si se liberó la siguiente tarea para poder meterla a la fila de trabajo.

## Respuestas 1–25

### 1. Presentación de la clase
**Pregunta:** En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?
**Respuesta:** Elegir constantemente una tarea que ya tenga "cero" requisitos pendientes por cumplir.

### 2. El nuevo problema: dependencias
**Pregunta:** ¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?
**Respuesta:** Tienes que haber pasado Algoritmos y Optimización[cite: 1]. Hay más de una respuesta correcta porque no importa en qué orden tomes Álgebra o Programación al inicio, siempre y cuando respetes que van antes de sus materias dependientes[cite: 1].

### 3. Interpretación de aristas dirigidas
**Pregunta:** ¿Por qué A → B y B → A representan restricciones diferentes?
**Respuesta:** Porque las flechas son de un solo sentido (A es requisito para B)[cite: 1]. Si la volteas, cambias las reglas del juego y obligas a terminar B primero[cite: 1].

### 4. Qué es un DAG
**Pregunta:** ¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?
**Respuesta:** Porque se vuelve un círculo vicioso o "pescadilla que se muerde la cola". Nadie puede dar el primer paso porque todos están esperando a que el anterior termine[cite: 1].

### 5. Ejemplos con y sin ciclos
**Pregunta:** En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?
**Respuesta:** Porque el problema nos pide un plan completo para *todas* las tareas[cite: 1]. Si entregas algo a medias (D y E), A, B y C se quedan bloqueados y no resuelves el problema global[cite: 1].

### 6. Grado de entrada
**Pregunta:** ¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?
**Respuesta:** Algoritmos tiene 1 (Estructuras de Datos), Optimización tiene 1 (Álgebra) y Proyecto Final tiene 2 (Algoritmos y Optimización)[cite: 1].

### 7. Nodos disponibles
**Pregunta:** ¿En qué momento exacto debe encolarse Estructuras de Datos?
**Respuesta:** Justo en el momento en que se completa el último de sus dos requisitos (cuando Matemáticas Discretas baja su contador a cero)[cite: 1]. Ni antes ni después.

### 8. Descubrimiento de Kahn
**Pregunta:** ¿Qué representa disminuir en uno el grado de entrada de un vecino?
**Respuesta:** Representa que ese vecino ya cumplió con uno de sus requisitos previos[cite: 1]. Es el equivalente a tachar un pendiente en tu lista[cite: 1].

### 9. Ejecución manual
**Pregunta:** Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?
**Respuesta:** 
- Paso 3: Cola vacía, Actual C, Vecino D, Grado anterior 1, Grado nuevo 0, Acción encolar D, Orden A, B, C.
- Paso 4: Cola vacía, Actual D, sin vecinos, Acción terminar, Orden A, B, C, D.

### 10. Uso de la cola
**Pregunta:** ¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?
**Respuesta:** Porque `deque` ya hace exactamente lo que necesitamos (sacar y meter elementos rápidamente) y nos permite concentrarnos en la lógica de los grados sin arriesgarnos a un error tonto al programar una cola desde cero[cite: 1].

### 11. Invariantes
**Pregunta:** ¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?
**Respuesta:** Se viola la regla principal (el Invariante Central): a la cola solo pueden entrar nodos que tengan grado de entrada "cero"[cite: 1].

### 12. Implementación paso a paso
**Pregunta:** ¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?
**Respuesta:** 
1. El grafo normalizado (para tener una copia limpia y no dañar la original)[cite: 1].
2. Los grados de entrada (para saber cuántos pendientes tiene cada nodo)[cite: 1].
3. La cola de disponibles (para saber quién sigue en la fila)[cite: 1].
4. La lista del orden final (nuestra respuesta)[cite: 1].

### 13. Detección de ciclos
**Pregunta:** ¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?
**Respuesta:** Porque si el tamaño no coincide, significa que el ciclo `while` se detuvo antes de poder atender todos los nodos[cite: 1]. Es decir, algunos se quedaron bloqueados infinitamente esperando un requisito[cite: 1].

### 14. BFS frente a Kahn
**Pregunta:** ¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?
**Respuesta:** BFS mete un nodo a la cola con solo "descubrirlo" una vez[cite: 1]. Kahn es paciente y espera hasta que *todas* las dependencias de ese nodo se hayan completado antes de meterlo a la cola[cite: 1].

### 15. Órdenes no únicos
**Pregunta:** ¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?
**Respuesta:** Porque A y B no dependen la una de la otra y pueden hacerse en cualquier orden[cite: 1]. Exigir estrictamente [A, B, C] marcaría como falso el orden [B, A, C], que también es totalmente válido[cite: 1].

### 16. Validación de un orden
**Pregunta:** Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.
**Respuesta:**
- B, A, C: Válida (respeta ambas aristas).
- C, A, B: Inválida (falla la arista A->C porque C aparece antes que A).
- A, C: Inválida (le falta la longitud correcta porque falta B).
- A, A, C: Inválida (tiene duplicados y falta B).

### 17. Normalización y dependencias duplicadas
**Pregunta:** ¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?
**Respuesta:** Porque si la cuentas dos veces, a la hora de que el origen se procese, solo le bajará "1" al contador[cite: 1]. El destino se quedará atorado en grado 1 para siempre pensando que le falta un requisito fantasma[cite: 1].

### 18. Casos límite
**Pregunta:** ¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?
**Respuesta:** Deben aparecer en alguna parte del resultado final porque, al no depender de nadie (su grado inicial es cero), son procesables en cualquier momento[cite: 1].

### 19. Problema de cursos
**Pregunta:** ¿Qué significa exactamente el par (2, 5) en ordenar_cursos?
**Respuesta:** Significa que el curso 2 es un prerrequisito obligatorio para poder tomar el curso 5[cite: 1]. (La flecha va de 2 a 5).

### 20. CSES Course Schedule
**Pregunta:** ¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?
**Respuesta:** Hay que restarle 1 al leer los datos (para que empiecen en 0 en nuestro código) y sumarle 1 al imprimirlos al final[cite: 1]. Si hay un ciclo, debe imprimirse `IMPOSSIBLE`[cite: 1].

### 21. LeetCode Course Schedule
**Pregunta:** ¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?
**Respuesta:** LeetCode pone los pares al revés `[curso, requisito]`[cite: 1]. Solo hay que invertir el par al leerlo; LeetCode 207 usa `puede_completar_cursos` (solo quiere saber si se puede) y el 210 usa `ordenar_cursos` (quiere la lista del orden)[cite: 1].

### 22. Complejidad
**Pregunta:** ¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?
**Respuesta:** Porque no estás comparando cada nodo contra todos los demás una y otra vez[cite: 1]. El algoritmo solo procesa cada nodo como máximo una vez y cuenta cada arista una vez[cite: 1]. Se suman los esfuerzos, no se multiplican[cite: 1].

### 23. Pruebas
**Pregunta:** ¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?
**Respuesta:** Verificando sus propiedades (que tenga la longitud correcta, sin repetidos y que el origen de cada arista esté antes que el destino), en lugar de compararlo contra una lista fija y quemada en el código[cite: 1].

### 24. Extensión con heap
**Pregunta:** ¿Qué cambio de contrato justifica sustituir la cola por un heap?
**Respuesta:** Se justifica únicamente si el problema nos pide, además de un orden válido, elegir siempre el "menor" nodo disponible (por ejemplo, en orden alfabético) en caso de empate[cite: 1]. 

### 25. Cierre integrador
**Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?
**Respuesta:** Preguntándonos qué decisión tenemos que tomar repetidamente de forma más óptima[cite: 1]. Si es procesar sin requisitos usamos Kahn (cola + grados), si es hallar distancias cortas usamos Dijkstra (heap), etc[cite: 1].