# Notebook Aristeo
## 1. Motivación
### Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.
Ejemplo: Imagina una lista desordenada que almacena las identificaciones de un millón de usuarios [8432, 1021, 9943, ...]. 
Si queremos buscar un usuario que está al final de la lista o que ni siquiera existe, nos veremos obligados a inspeccionar los $1,000,000 de elementos uno por uno costo lineal O(n).
Mejora esperada con el BST: Si el BST está bien balanceado, esperamos que aproveche su estructura jerárquica para descartar la mitad de los elementos en cada paso. En lugar de un millón de operaciones, resolveríamos la búsqueda en aproximadamente log_2(1,000,000) aprox. 20 comparaciones costo logarítmico  (O(log n)).
## 2. Lista vs BST
### ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?
El BST utiliza la relación de orden e invariante de la estructura: para cualquier nodo, todos los elementos en su subárbol izquierdo son menores que él, y todos los del subárbol derecho son mayores. Una lista desordenada carece de estructura o criterio de orden, obligándonos a revisar todo porque el elemento buscado podría estar en cualquier posición.
## 3. Conteo manual de comparaciones
### Cuenta cuántos nodos se comparan al buscar `14` en ambos árboles.
Árbol Balanceado (8, 4, 12, 2, 6, 10, 14): Se realizan 3 comparaciones. Comparamos 14 con la raíz 8 (ir a la derecha), luego con 12 (ir a la derecha), y finalmente encontramos el 14.

Árbol Degenerado (1, 2, 3, 4, 5, 6, 7): Si buscamos 14 (un valor mayor que todos), compararemos consecutivamente contra 1, 2, 3, 4, 5, 6, 7. Al llegar al final (7) su hijo derecho es None, por lo que se determina que no está. Se realizan 7 comparaciones.
### ¿Qué cambió: los datos o la forma del árbol?
Los datos del árbol balanceado y el degenerado son conceptualmente similares en cuanto a ordenamiento, pero lo que cambió drásticamente fue la forma del árbol. Esta forma fue determinada puramente por el orden de inserción de los datos.
## 4. Altura
### ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?
Porque la altura define el peor escenario posible (el camino más largo) que puede recorrer un algoritmo de búsqueda. Dos árboles pueden tener exactamente el mismo número de nodos (n = 7), pero si uno tiene altura 3 (balanceado) la búsqueda toma a lo más 3 pasos, mientras que si el otro tiene altura 7 (degenerado), podría tomar hasta 7 pasos. La cantidad de nodos determina la capacidad del árbol, pero la altura determina su eficiencia real.
## 5. Árbol balanceado y árbol degenerado
### Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.
Un BST degenerado tiene una forma completamente lineal, idéntica a una lista enlazada simple o una "línea recta" inclinada hacia un lado.

Aparece al insertar valores secuenciales ordenados (por ejemplo: 1, 2, 3, 4, 5) porque cada nuevo elemento insertado siempre será mayor (o menor, si es descendiente) que el anterior. Al ser siempre mayor, se acomodará constantemente en el hijo derecho del último nodo, sin generar jamás ramificaciones hacia la izquierda.
## 6. Búsqueda y altura
### ¿Qué relación hay entre profundidad, altura y número de comparaciones?
El número de comparaciones en una búsqueda exitosa equivale a la profundidad del nodo donde se encuentra el valor (más 1, dependiendo de si cuentas la raíz como nivel 1).

En el peor de los casos (buscar un elemento que no existe o que está en las hojas más profundas), el número máximo de comparaciones posibles está estrictamente acotado por la altura del árbol.
## 7. Experimentos
### ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?
Sí, crece exponencialmente en comparación al balanceado. En un árbol degenerado, añadir $n$ elementos implica que la búsqueda en el peor caso crecerá linealmente (O(n)). Mientras que en el balanceado, al aumentar el tamaño, las comparaciones apenas crecen de forma logarítmica (O(log n)). A mayor escala, la brecha de rendimiento es inmensa.
## 8. Animaciones
### ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?
Muestran visualmente que en el árbol balanceado la búsqueda desciende "saltando" niveles rápidamente gracias a la división de caminos (poca altura recorrida).

En cambio, en el árbol degenerado o la lista, el contador de comparaciones acumuladas aumenta de uno en uno con cada nodo del camino, debido a que se ve obligado a recorrer secuencialmente toda la altura del árbol sin posibilidad de descarte eficiente.
## 9. Complejidad
### ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?
Porque la cota O(log n) es una propiedad del caso ideal o promedio (cuando el árbol está razonablemente balanceado). Si omitimos el estado de balance, estamos ignorando que el peor caso de un BST es una estructura degenerada cuya complejidad real se degrada a O(n), rindiendo exactamente igual que una lista común.
## 10. Problemas relacionados
### Elige uno y explica qué concepto de esta clase practica.
Balanced Binary Tree: Este problema requiere implementar una función que determine si un árbol binario está balanceado calculando recursivamente la altura de los subárboles izquierdo y derecho de cada nodo. Practica directamente el concepto de altura y la definición matemática de balance (que la diferencia de alturas no sea mayor a 1).
## 11. evaluar.py y pruebas
### ¿Qué problema resuelve permitir `tests_extra`?
Resuelve el problema de la caja negra en las revisiones de código. Permite que pruebes tu propia suite de pruebas (test_estudiante.py) en la solución de otro compañero (o viceversa) para descubrir casos esquina (edge cases) o errores lógicos que los tests genéricos públicos no cubren.
## 12. Revisión técnica de PR
### ¿Qué debe incluir un comentario técnico útil en el PR?
Debe incluir el comando exacto que ejecutaste, la salida completa de la prueba en un bloque de código limpio, y un análisis u observación constructiva y objetiva sobre los resultados (por ejemplo, reportar si falló algún método específico como es_degenerado ante valores duplicados).
## 13. Patrón descubierto
### Explica el patrón con tus palabras.
Significa que usar una estructura de datos "avanzada" (como un BST) no nos vuelve mágicamente rápidos, así nomás. El software es dinámico; si no cuidamos las propiedades internas de la estructura mientras muta (como mantener el árbol balanceado al insertar datos), la estructura perderá sus ventajas teóricas y fallará en darnos la eficiencia que prometía.
## 14. Cierre
### 1. ¿Un BST siempre es mejor que una lista? 
No, depende de cada caso lo que es necesario implementar para resolver el problema correspondiente.
### 2. ¿Qué relación hay entre altura y comparaciones?
La altura del árbol dicta el límite máximo absoluto de nodos que el algoritmo de búsqueda puede visitar. Cada nivel del árbol por el que descendemos representa exactamente una comparación.
### 3. ¿Cómo se degenera un BST?
Un BST se degenera cuando los datos se insertan en un orden estrictamente secuencial (ya sea de forma ascendente o descendente, como 1, 2, 3, 4, 5).
### 4. ¿Qué evidencia experimental usarías para justificar tu respuesta?
Buscar el último elemento del peor escenario en ambos árboles y registrar el resultado de comparaciones_busqueda(valor). Al graficar o tabular cómo aumentan estas comparaciones conforme crece n, se evidenciaría una curva lineal (O(n)) para el degenerado y una curva logarítmica (O(log n)) para el balanceado.
### 5. ¿Qué problema relacionado practicarías después?
Practicaría el problema LeetCode 110 — Balanced Binary Tree o LeetCode 98 — Validate Binary Search Tree.