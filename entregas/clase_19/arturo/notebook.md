# Arturo Prudencio Bonilla 


## Pregunta inicial
**¿Cómo encontramos un orden válido para ejecutar tareas cuando unas dependen de otras?**
Lo encontramos repitiendo la operación de elegir una tarea que ya no tenga requisitos pendientes Esto se representa llevando un conteo de los grados de entrada (requisitos pendientes) y utilizando una cola para procesar aquellos que lleguen a grado cero

---

## 1. Presentación de la clase
**En el problema de cursos, ¿qué operación necesitamos repetir para construir un plan válido?**
Necesitamos repetir la operación de elegir una tarea (o curso) que no tenga requisitos pendientes

---

## 2. El nuevo problema: dependencias
**¿Qué debe ocurrir antes de Proyecto Final y por qué puede haber más de una respuesta correcta?**
Antes de Proyecto Final, se deben completar sus dos ramas previas: Algoritmos y Optimización Puede haber más de una respuesta correcta porque algunas tareas no están ordenadas entre sí y pueden procesarse en distintas secuencias siempre que se respeten los prerrequisitos individuales

---

## 3. Interpretación de aristas dirigidas
**¿Por qué A → B y B → A representan restricciones diferentes?**
Porque `A → B` significa que A debe completarse obligatoriamente antes que B, marcando una relación asimétrica Invertir la flecha a `B → A` cambia completamente el contrato, obligando a terminar B primero

---

## 4. Qué es un DAG
**¿Por qué el ciclo A → B → C → A impide cualquier orden topológico?**
Porque exige simultáneamente que A se complete antes que B, B antes que C, y C antes que A, por lo que ninguna secuencia lineal puede satisfacer todas esas restricciones Un grafo dirigido solo tiene orden topológico si no contiene ciclos

---

## 5. Ejemplos con y sin ciclos
**En el grafo mixto, ¿por qué procesar D y E no permite devolver un orden parcial como solución?**
Porque procesar la parte acíclica (D y E) no rescata al grafo completo, ya que los nodos A, B y C seguirán bloqueados por su ciclo interno Procesar una componente acíclica no demuestra que todo el grafo sea acíclico

---

## 6. Grado de entrada
**¿Qué grados de entrada tienen Algoritmos, Optimización y Proyecto Final en el problema conductor?**
Basado en las dependencias del problema, Algoritmos tiene un grado de 1 (espera a Estructuras de Datos) Optimización tiene un grado de 1 (espera a Álgebra) Proyecto Final tiene un grado de 2 (espera a Algoritmos y Optimización)

---

## 7. Nodos disponibles
**¿En qué momento exacto debe encolarse Estructuras de Datos?**
Debe encolarse exactamente cuando su grado de entrada actual llega a cero, lo cual ocurre después de que se hayan procesado Programación y Matemáticas Discretas

---

## 8. Descubrimiento de Kahn
**¿Qué representa disminuir en uno el grado de entrada de un vecino?**
Representa que una de las dependencias de ese vecino acaba de quedar satisfecha

---

## 9. Ejecución manual
**Completa los pasos 3 y 4: ¿qué valores y orden final deben aparecer?**
En el paso 3, el nodo actual es C, el vecino es D, el grado anterior es 1 y el grado nuevo es 0; la acción es encolar D, quedando el orden parcial en `A, B, C` En el paso 4, el nodo actual es D, no hay vecinos, la acción es terminar y el orden final es `A, B, C, D`

---

## 10. Uso de la cola
**¿Por qué la solución evaluada usa deque aunque ColaLigada pueda implementar la misma política?**
Porque usar `collections.deque` con sus métodos `append` y `popleft` en O(1) permite concentrar la práctica en la lógica de grados y dependencias, evitando que un error previo de implementación de enlaces se convierta en un nuevo bloqueo

---

## 11. Invariantes
**¿Qué invariante se viola si un nodo entra a la cola cuando su grado todavía es 1?**
Se viola el invariante central que dicta que todo nodo presente en la cola debe tener un grado de entrada actual de exactamente cero

---

## 12. Implementación paso a paso
**¿Qué cuatro estructuras locales necesita mantener orden_topologico y para qué sirve cada una?**
Necesita mantener:
1. Una copia normalizada del grafo
2. Una estructura (`grados`) para registrar los grados de entrada
3. Una cola (`disponibles`) para alojar los nodos con grado cero
4. Una lista (`orden`) para ir guardando la secuencia de los nodos ya procesados

---

## 13. Detección de ciclos
**¿Por qué len(orden) != len(normalizado) es evidencia de un ciclo?**
Porque la desigualdad detecta que alguna componente no pudo liberar sus dependencias, impidiendo que sus grados lleguen a cero y provocando que el bucle se detenga antes de cubrir todo el grafo

---

## 14. BFS frente a Kahn
**¿Cuál es la diferencia decisiva entre la regla para encolar en BFS y en Kahn?**
En BFS, un nodo se encola simplemente por ser un vecino no descubierto En Kahn, el nodo debe esperar y solo se encola cuando **todas** sus dependencias se han procesado y su grado llega a cero

---

## 15. Órdenes no únicos
**¿Por qué un test que exige exactamente [A, B, C] es incorrecto para A→C y B→C?**
Porque para ese grafo, la secuencia `B, A, C` también es válida ya que A y B no tienen dependencias entre sí Comparar únicamente con una lista esperada fija rechazaría soluciones correctas

---

## 16. Validación de un orden
**Clasifica las cuatro secuencias incompletas de la tabla y explica la primera regla que falla.**
*   `B,A,C`: Sí es válida, respeta ambas aristas
*   `C,A,B`: Es inválida porque C aparece antes que A, violando la regla `A → C` (la posición de u debe ser menor a la de v)
*   `A,C`: Es inválida porque omite a B, fallando la cobertura de longitud correcta
*   `A,A,C`: Es inválida porque presenta elementos repetidos

---

## 17. Normalización y dependencias duplicadas
**¿Por qué una dependencia duplicada no debe aumentar dos veces el grado de entrada?**
Porque si se cuenta dos veces, al procesar el origen solo se reducirá el grado una vez, dejando al vecino bloqueado indefinidamente Si se redujera de más, aparecerían grados negativos

---

## 18. Casos límite
**¿Cómo deben aparecer los nodos aislados en un orden topológico y por qué?**
Deben aparecer exactamente una vez en el resultado, porque tienen un grado de entrada inicial de cero y están disponibles desde el principio

---

## 19. Problema de cursos
**¿Qué significa exactamente el par (2, 5) en ordenar_cursos?**
Significa que el curso 2 es un prerrequisito para el curso 5, es decir, existe una arista dirigida hacia el curso que espera (2 → 5)

---

## 20. CSES Course Schedule
**¿Qué conversiones de índices necesita la adaptación de CSES y qué debe imprimirse si hay ciclo?**
Necesita leer los pares indexados desde 1 (1-based), restarles uno para poder reutilizar la función `ordenar_cursos`, y luego sumarles uno al momento de imprimir el resultado Si hay un ciclo, debe imprimirse la cadena `IMPOSSIBLE`

---

## 21. LeetCode Course Schedule
**¿Cómo se relacionan ordenar_cursos, puede_completar_cursos y las preguntas de LeetCode 207/210?**
LeetCode utiliza una convención inversa `[curso, prerrequisito]` que debe transformarse primero Después de adaptar los pares en el borde, LeetCode 207 delega directamente en `puede_completar_cursos`, y LeetCode 210 delega en `ordenar_cursos`

---

## 22. Complejidad
**¿Por qué el bucle anidado sobre nodos y vecinos no implica O(VE)?**
Porque las fases son consecutivas y aditivas, no multiplicativas Cada nodo se encola y procesa como máximo una sola vez, y cada arista se cuenta y reduce exactamente una sola vez, manteniendo el costo total en O(V+E)

---

## 23. Pruebas
**¿Cómo debe probarse un resultado cuando el grafo admite varios órdenes topológicos?**
Debe probarse verificando sus propiedades en lugar de una lista estricta: asegurar que aparecen todos los nodos, que no hay duplicados ni desconocidos, y que para cada arista `u → v`, la posición de `u` es menor que la de `v`

---

## 24. Extensión con heap
**¿Qué cambio de contrato justifica sustituir la cola por un heap?**
Se justificaría si el contrato exigiera devolver el orden lexicográficamente mínimo, lo que obligaría a extraer siempre el menor nodo disponible en lugar de procesar cualquier elemento válido

---

## 25. Cierre integrador
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos adecuada?**
Identificamos la operación dominante analizando qué trabajo repetido necesita hacer el algoritmo (por ejemplo: procesar por niveles, atender costo cero, extraer distancia mínima o procesar sin requisitos) y luego elegimos la estructura (cola, deque, heap, Union-Find o cola + grados) que implementa exactamente esa política