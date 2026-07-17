## 1. Motivación

**Pregunta.** Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.

Un ejemplo donde la lsita sea costoso sería si el elemento que buscamos es el último. Se espera que el árbol mejore la eficiencia.

## 2. Lista vs BST

**Pregunta.** ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?

El invariante, porque garantiza que todo a la izquierda es menor, y todo a la derecha es mayor. 

## 3. Conteo manual de comparaciones
**Actividad.** Cuenta cuántos nodos se comparan al buscar `14` en ambos árboles.
En el árbol, 3. En la lista, 7.

**Pregunta.** ¿Qué cambió: los datos o la forma del árbol?
La forma. El segundo parece una lista.

## 4. Altura

**Pregunta.** ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?
Porque no comparamos todos los nodos, pero en el caso máximo, compararemos tantas veces como haya nodos, lo que define la altura.

## 5. Árbol balanceado y árbol degenerado

**Pregunta.** Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.

La forma del árbol degenerado es más como una línea. Aparece al ordenar los valores porque, si cada uno es mayor al anterior, sólo se inserta a la derecha.

## 6. Búsqueda y altura

**Pregunta.** ¿Qué relación hay entre profundidad, altura y número de comparaciones?
Que, en el peor caso, donde el número buscado es el último revisado, su profundidad es igual a la altura de su subárbol, pero no necesariamente de todo el árbol. En ese caso, se hacen todas las comparaciones.

## 7. Experimentos

**Pregunta.** ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?
Sí, porque se aumenta una. SI está balanceado, no necesariamente.

## 8. Animaciones

**Pregunta.** ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?
Que ambas aumentan mucho si el árbol no está balanceado.

## 9. Complejidad

**Pregunta.** ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?
Porque, si no está balanceado, puede ser O(n), como una lista.

## 10. Problemas relacionados

**Pregunta.** Elige uno y explica qué concepto de esta clase practica.
Tree Diameter. 
Consiste en determinar la distancia máxima entre cualesquira dos nodos. Se relaciona porque esa distancia aumentará dramáticamente si es degenerado, porque se separará mucho, y será n-1.

## 11. evaluar.py y pruebas
**Pregunta.** ¿Qué problema resuelve permitir `tests_extra`?
Que no habrá problema cuando agregemos pruebas.

## 12. Revisión técnica de PR
**Pregunta.** ¿Qué debe incluir un comentario técnico útil en el PR?
Explicaciones sobre qué hace el código y sobre de dónde está tomando las importaciones.

## 13. Patrón descubierto
**Pregunta.** Explica el patrón con tus palabras.
El patrón consiste en reconocer el buen uso de las estructuras. Aunque esté bien implementado, no servirá de nada si no aprovechamos sus propiedades. Hay que balancear el árbol para que siga siendo eficiente.

## 14. Cierre

1. ¿Un BST siempre es mejor que una lista?

No, sólo si no se necesita guardar orden y si está balanceado.

2. ¿Qué relación hay entre altura y comparaciones?

La altura es igual al número de comparaciones en el peor caso.

3. ¿Cómo se degenera un BST?

Cuando se agregan datos sin balance.

4. ¿Qué evidencia experimental usarías para justificar tu respuesta?

Las animaciones agregadas y el análisis de la complejidad.

5. ¿Qué problema relacionado practicarías después

Cómo garantizar el balance de un árbol.