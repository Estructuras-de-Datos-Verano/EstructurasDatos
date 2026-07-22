## 1. Motivación

**Pregunta.** Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.

Si metes un montón de números al azar en un arreglo y buscas uno que no está o que quedó al final, tienes que recorrerlo completo. Con el BST, si está bien armado, la idea es ir partiendo la búsqueda a la mitad en cada paso para que el costo baje a algo tipo, que es más rápido.

## 2. Lista vs BST

**Pregunta.** ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?

El BST aprovecha que los datos ya están ordenados bajo una regla fija: los chicos a la izquierda y los grandes a la derecha. La lista desordenada no tiene ninguna estructura, así que no te da pistas de dónde buscar; te tocaría revisar uno por uno.

## 3. Conteo manual de comparaciones

**Pregunta.** ¿Qué cambió: los datos o la forma del árbol?

Los datos que metimos son exactamente los mismos en ambos árboles. Lo único que cambió fue el orden en el que los fuimos insertando, lo que hizo que el dibujo o la "forma" del árbol cambiara por completo.

## 4. Altura

**Pregunta.** ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?

Porque la altura te dice cuál es el peor camino que podrías llegar a recorrer en una búsqueda. De nos sirve saber que el árbol tiene 1000 nodos en total si todos están formados en una sola línea; lo que te importa es qué tan profundo tienes que bajar para encontrar lo que se buscas.

## 5. Árbol balanceado y árbol degenerado

**Pregunta.** Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.

Un BST degenerado es una lista, donde los nodos solo tienen un hijo. Esto pasa cuando le metes los datos ya ordenados, porque cada número nuevo siempre es más grande que el anterior y se va colgando todo del lado derecho.

## 6. Búsqueda y altura

**Pregunta.** ¿Qué relación hay entre profundidad, altura y número de comparaciones?

La profundidad te dice a cuántos pasos está un nodo específico de la raíz, o sea, cuántas comparaciones vas a hacer para encontrarlo. Como la altura es el punto más profundo del árbol, representa el peor de los casos.

## 7. Experimentos

**Pregunta.** ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?

Sí, en el balanceado el costo sube muy lento, mientras que en el degenerado sube de uno en uno con cada nodo nuevo (lineal).

## 8. Animaciones

**Pregunta.** ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?

Muestra de forma  visual que un árbol balanceado abre sus ramas hacia los lados, manteniendo los nodos cerca de la raíz y haciendo que las búsquedas sean cortas. En cambio, el degenerado se va de largo hacia abajo, acumulando comparaciones en un camino eterno porque nunca se abre.

## 9. Complejidad

**Pregunta.** ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?

Porque decir que un BST es O(log n) es una verdad a medias. Esa velocidad solo se cumple si el árbol está balanceado, cuando no su complejidad real se cae a O(n), igual que una lista.

## 10. Problemas relacionados

**Pregunta.** Elige uno y explica qué concepto de esta clase practica.

Balanced Binary Tree trata justo de calcular la altura de los subárboles de cada nodo para ver si se llevan por más de 1 de diferencia.
## 11. evaluar.py y pruebas

**Pregunta.** ¿Qué problema resuelve permitir `tests_extra`?

Sirve para que puedas armar tus propios casos que tal vez no vienen en las pruebas obligatorias. Así aseguras de que tu código no se rompa con nada antes de entregarlo.

## 12. Revisión técnica de PR

**Pregunta.** ¿Qué debe incluir un comentario técnico útil en el PR?

Debe traer el error exacto que saltó si no pasó la prueba, pero también comentarios sobre el código del otro, por ejemplo, si notas que hace llamadas recursivas de más que vuelven lento el programa o si se le olvidó validar los casos con None.

## 13. Patrón descubierto

Patrón de la clase:

**Pregunta.** Explica el patrón con tus palabras.

Que programar la estructura no te asegura que vaya a ser rápida. Depende de que se cumplan ciertas propiedades geométricas mientras el árbol va creciendo.

## 14. Cierre

1. ¿Un BST siempre es mejor que una lista?

No, si está degenerado rinde igual de mal que una lista y aparte gasta más memoria por los punteros.

2. ¿Qué relación hay entre altura y comparaciones?

La altura es el tope; es el número máximo de comparaciones que harás si buscas algo que está en el fondo o que no existe.

3. ¿Cómo se degenera un BST?

Insertando los datos ya ordenados de menor a mayor (o de mayor a menor).

4. ¿Qué evidencia experimental usarías para justificar tu respuesta?

Hacer un script que mida el número de comparaciones al buscar en un árbol que creció con datos aleatorios contra uno con datos ordenados, y graficar los resultados.

5. ¿Qué problema relacionado practicarías después?

El 110 de LeetCode, para dejar clara la lógica de cómo medir y comparar alturas.











