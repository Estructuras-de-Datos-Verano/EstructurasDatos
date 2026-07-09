# Notebook - Clase 12

## 1. Motivación
**Pregunta:** Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.
**Respuesta:** En una lista desordenada de 1,000,000 de registros telefónicos, buscar un número inexistente o ubicado al final obliga a realizar un millón de operaciones ($O(n)$). En un BST balanceado, se espera que la estructura jerárquica permita descartar aproximadamente la mitad de los elementos en cada paso, reduciendo el peor de los casos a solo unas 20 comparaciones ($O(\log n)$).

## 2. Lista vs BST
**Pregunta:** ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?
**Respuesta:** El BST se fundamenta en su relación de orden e invariante: todo elemento a la izquierda de un nodo es estrictamente menor, y todo elemento a la derecha es estrictamente mayor. Una lista desordenada carece de esta propiedad de separación espacial y condicional, lo que impide descartar elementos sin visitarlos de forma explícita.

## 3. Conteo manual de comparaciones
**Pregunta:** ¿Qué cambió: los datos o la forma del árbol?
**Respuesta:** Para buscar el número `14`:
- En el árbol balanceado se visitan 3 nodos (`8 -> 12 -> 14`), requiriendo **3 comparaciones**.
- En el árbol degenerado se visitan 7 nodos (`1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`), requiriendo **7 comparaciones**.
**Lo que cambió es la forma (topología) del árbol**, ya que el conjunto de datos de entrada es conceptualmente análogo en volumen pero estructurado de forma diametralmente opuesta debido al orden de inserción.

## 4. Altura
**Pregunta:** ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?
**Respuesta:** Porque la altura determina la longitud máxima del camino (peor escenario posible) desde la raíz hasta cualquier nodo hoja. Un árbol con 10,000 nodos puede tener una altura ideal de 14 (búsqueda ultrarrápida) o una altura de 10,000 (búsqueda lineal ineficiente); el volumen de nodos por sí solo no describe el rendimiento operativo.

## 5. Árbol balanceado y árbol degenerado
**Pregunta:** Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.
**Respuesta:** Un BST degenerado tiene una forma lineal y alargada, idéntica a una lista enlazada, donde cada nodo padre posee como máximo un único hijo. Aparece al insertar valores secuenciales (ya sean estrictamente crecientes o decrecientes) porque cada nuevo elemento es unánimemente mayor (o menor) que todos los anteriores, anexándose sistemáticamente a un solo extremo sin ramificaciones secundarias.


## 6. Búsqueda y altura
**Pregunta:** ¿Qué relación hay entre profundidad, altura y número de comparaciones?
**Respuesta:** La profundidad indica el nivel exacto de un nodo específico. La altura limita superiormente la profundidad del árbol entero. El número de comparaciones de una búsqueda exitosa equivale a `profundidad + 1`, y para una búsqueda infructuosa estará acotado directamente por la `altura` máxima recorrida en esa rama.

## 7. Experimentos
**Pregunta:** ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?
**Respuesta:** Sí, crece de manera lineal y proporcional. En un árbol balanceado el aumento de tamaño impacta logarítmicamente ($O(\log n)$), mientras que en el degenerado impacta de forma lineal ($O(n)$). Por ende, la brecha de rendimiento entre ambas formas se expande drásticamente a medida que $n$ se vuelve más grande.

## 8. Animaciones
**Pregunta:** ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?
**Respuesta:** Muestran que el árbol balanceado amortiza velozmente el número de operaciones distribuyendo los accesos uniformemente a través de niveles compactos, mientras que la animación degenerada muestra un crecimiento acumulativo continuo y costoso paso a paso, arrastrando ineficiencia lineal en su trayectoria vertical.

## 9. Complejidad
**Pregunta:** ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?
**Respuesta:** Es una imprecisión técnica peligrosa. Un BST solo ofrece complejidad $O(\log n)$ cuando está óptimamente balanceado. En ausencia de balance, carece de garantías operativas estables, pudiendo degradarse por completo hasta un escenario de peor caso con complejidad de tiempo $O(n)$.

## 10. Problemas relacionados
**Pregunta:** Elige uno y explica qué concepto de esta clase practica.
**Respuesta:** El problema **LeetCode 110 — Balanced Binary Tree**. Practica directamente el concepto de balance recalculando de forma recursiva la altura de los subárboles izquierdo y derecho para evaluar si su diferencia absoluta es menor o igual a 1 en cada nodo del sistema.

## 11. evaluar.py y pruebas
**Pregunta:** ¿Qué problema resuelve permitir `tests_extra`?
**Respuesta:** Permite inyectar pruebas asimétricas y personalizadas diseñadas por otros estudiantes o profesores sin alterar la suite pública original, ayudando a descubrir casos extremos ("edge cases") no contemplados inicialmente y fortaleciendo el proceso de integración continua.

## 12. Revisión técnica de PR
**Pregunta:** ¿Qué debe incluir un comentario técnico útil en el PR?
**Respuesta:** Debe contener el comando exacto ejecutado, la salida textual íntegra de la prueba (`pytest -v`), y un análisis constructivo y específico sobre el código evaluado (por ejemplo, detectar fallos de control de tipos o desviaciones en el cálculo de fronteras vacías).

## 13. Patrón descubierto
**Pregunta:** Explica el patrón con tus palabras.
**Respuesta:** El patrón nos recuerda que usar una estructura avanzada no regala rendimiento de forma automática. La eficiencia no es una propiedad estática del "nombre" de la estructura, sino un comportamiento dinámico condicionado por las invariantes de forma y balance que mantengamos vivas durante el ciclo operativo.

## 14. Cierre
**Respuestas:**
1. **No**, si se encuentra degenerado posee el mismo rendimiento que una lista secuencial.
2. La altura representa el peor de los casos en número de comparaciones de acceso.
3. Se degenera al insertar datos pre-ordenados de forma secuencial.
4. La medición del crecimiento de `comparaciones_busqueda(valor)` frente a colecciones de tamaño variable $n$.
5. Continuaría con *LeetCode 110 (Balanced Binary Tree)* para dominar la detección matemática del desbalance estructural.