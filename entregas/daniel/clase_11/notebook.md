# Notebook - Clase 11: Árboles binarios de búsqueda

Este documento contiene las respuestas breves a los desafíos y preguntas de análisis planteados en la clase.

---

## 1. Motivación
 **Pregunta:** ¿Qué problema aparece cuando buscamos muchas veces en una lista?

El gran problema es la ineficiencia. En el peor de los casos (cuando el dato no existe o está al final), una lista te obliga a hacer una búsqueda lineal revisando los elementos uno por uno. Si tienes millones de datos y necesitas hacer miles de consultas, el programa se volverá sumamente lento porque su costo de tiempo crece de forma proporcional a la cantidad de elementos.

---

## 2. Problemas relacionados
 **Pregunta:** Elige uno de estos problemas y explica qué concepto de la clase parece practicar.

Elegí **"700. Search in a Binary Search Tree"**. Este problema practica directamente el concepto del **invariante del BST**. Para resolverlo, necesitas aplicar la lógica de decisión básica: si el valor que buscas es menor que el del nodo actual, te mueves al subárbol izquierdo; si es mayor, te vas al derecho. Es el ejemplo puro de cómo descartar la mitad del camino en cada paso.

---

## 3. Conceptos básicos
 **Pregunta:** Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.

Imaginen el nodo raíz con el valor `10`. De él salen dos ramas: a su izquierda se conecta el nodo `5` y a su derecha el nodo `15`. En esta estructura, `5` y `15` actúan como los hijos de la raíz, pero al no tener ninguna conexión hacia abajo, también cumplen el rol de hojas.

---

## 4. Árbol binario de búsqueda
 **Pregunta:** ¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?

Porque funciona como el juego de adivinar un número con pistas de "más alto" o "más bajo". Como sabemos con total certeza que todo lo menor está a la izquierda y todo lo mayor a la derecha, una sola comparación en el nodo actual nos da permiso para ignorar por completo toda una mitad del árbol. No tenemos que perder tiempo revisando esos nodos descartados.

---

## 5. Búsqueda
 **Pregunta:** ¿Qué nodos comparas y qué parte descartas en cada paso? (Buscando `9` en el árbol de ejemplo)

1. **Comparas con la raíz `8`:** Como `9` es mayor, descartas de golpe la raíz y todo su subárbol izquierdo (nodos `4`, `2` y `6`). Te mueves a la derecha.
2. **Comparas con el nodo `10`:** Como `9` es menor, descartas el subárbol derecho (nodo `12`). Te mueves a la izquierda.
3. **Comparas con el nodo `9`:** Los valores coinciden, encontraste el objetivo y termina la búsqueda.

---

## 6. Inserción
 **Pregunta:** Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

Siguiendo las reglas de "menor a la izquierda, mayor a la derecha", el árbol se construye así paso a paso:
* `8`: Se convierte en la **raíz** principal.
* `4`: Es menor que `8`, queda como su **hijo izquierdo**.
* `10`: Es mayor que `8`, queda como su **hijo derecho**.
* `2`: Menor que `8` y menor que `4`, se vuelve **hijo izquierdo de `4`**.
* `6`: Menor que `8` pero mayor que `4`, se vuelve **hijo derecho de `4`**.
* `9`: Mayor que `8` pero menor que `10`, se vuelve **hijo izquierdo de `10`**.
* `12`: Mayor que `8` y mayor que `10`, se vuelve **hijo derecho de `10`**.

---

## 7. Altura
 **Pregunta:** ¿Qué relación hay entre altura y costo de búsqueda?

La altura del árbol define el **peor escenario posible** (el costo máximo) para una búsqueda. Como en cada paso bajamos exactamente un nivel, el número de comparaciones que haremos nunca va a superar la altura del árbol. A menor altura (árbol más equilibrado), las búsquedas serán mucho más rápidas.

---

## 8. Recorridos
 **Pregunta:** ¿Por qué inorden produce valores ordenados en un BST?

Por la forma en que está definida su secuencia: **Izquierda, Raíz, Derecha**. Como el invariante del propio árbol ya garantiza que todo lo que está a la izquierda es menor que la raíz, y todo lo que está a la derecha es mayor, el recorrido inorden simplemente visita los elementos exactamente en su orden natural de menor a mayor.

---

## 9. Animaciones
 **Pregunta:** ¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

La animación te permite ver la **toma de decisiones en tiempo real** y la estructura geométrica. En una lista estática solo ves el resultado final, pero la animación te muestra visualmente cómo el algoritmo va "rebotando" de un nodo a otro hacia la izquierda o derecha antes de acomodar o encontrar un dato.

---

## 10. Implementación
 **Pregunta:** ¿Qué métodos parecen depender naturalmente de recursión?

Todos los que implican explorar la estructura hacia el fondo: `insertar`, `contiene` (búsqueda), `altura`, y sin duda alguna los tres recorridos (`inorden`, `preorden`, `postorden`). Como un árbol está hecho de subárboles más pequeños que repiten la misma estructura, resolver el problema para el nodo actual y llamar al método para sus hijos es una transición completamente natural para la recursión.

---

## 11. Pruebas
 **Pregunta:** ¿Qué problema resuelve `evaluar.py`?

Resuelve los típicos dolores de cabeza con las rutas y las importaciones de Python en las entregas de los alumnos. Al encargarse de verificar que los archivos existan y configurar automáticamente el entorno (`PYTHONPATH`), nos permite a nosotros escribir imports limpios y directos en los tests públicos, garantizando que el sistema evalúe el archivo correcto sin importar la configuración de carpetas del usuario.

---

## 12. Patrón descubierto
 **Pregunta:** Explica con tus palabras el patrón descubierto.

El patrón consiste en usar una **organización jerárquica** para acelerar las búsquedas mediante el descarte masivo de datos. En lugar de formarse en una fila infinita donde tienes que revisar a todos, los datos se ordenan en una estructura de decisiones binarias. Se activa siempre que manejamos un volumen grande de información ordenable en la que necesitamos hacer consultas constantes de existencia o pertenencia de manera ágil.

---

## 13. Cierre
1. **¿Qué ganamos frente a una lista?** Ganamos velocidad y eficiencia. Pasamos de revisar elemento por elemento a poder descartar enormes porciones de datos en cada paso del camino.
2. **¿Qué propiedad mantiene el BST?** Mantiene el invariante de que para cualquier nodo, todo su subárbol izquierdo contiene valores estrictamente menores, y su subárbol derecho contiene valores estrictamente mayores.
3. **¿Qué pasa si insertamos datos ordenados?** El árbol pierde todo su balance y se deforma, convirtiéndose esencialmente en una lista ligada inclinada hacia un solo lado.
4. **¿Cuándo podría degradarse un BST?** Se degrada cuando los datos ingresan en un orden perfectamente secuencial (ya sea ascendente o descendente), arruinando la distribución equilibrada de las ramas.
5. **¿Qué problema relacionado puedo practicar?** El problema de LeetCode *701. Insert into a Binary Search Tree*, que sirve perfectamente para afianzar la lógica de navegar y modificar la estructura respetando el invariante.