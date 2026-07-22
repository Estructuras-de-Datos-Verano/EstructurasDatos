# Clase-07 Aristeo 
## Presentación del laboratorio
### ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?
Ayuda porque nos permite ver como se debería de comportar la solución del problema que vamos a resolver con respecto a otros problemas de los cuales ya se conocen las estructuras y así poder elegir que estructura usar para el problema en particular.

---
## Lectura estratégica
### ¿Qué está pidiendo exactamente el problema?
Evaluar un conjunto ordenado de numeros y elegir la posición del numero inmediato menor a la izquierda y en caso de no haber, tomar la posición como 0, luego devolver la lista de esas evaluaciones.

---
### ¿Cuál es la entrada?
Una lista de numeros

---
### ¿Cuál es la salida?
Lista de posiciones y 0 

---
### ¿Qué significa “más cercano a la izquierda”?
El numero en la posicion i-1 siendo i la posición del numero que queremos evaluar, excepto si está en la posición 0, pues entonces se iría al ultimo elemento de la lista, el cual no está a la izquierda del numero de posición 0.

---
### ¿Qué pasa si no existe un valor menor?
Se guarda la posición como 0

---
### ¿Qué casos extremos parecen importantes? 
Donde no haya menor en ningun caso, donde solo hay un numero.

---
## Ingeniería inversa del algoritmo
### ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?
Vería mi lista, enumeraría cada numero dentro de ella dependiendo de su posición, me fijaría si hay un numero a la izquierda de cada elemento, si no lo hay anoto un 0, si lo hay y es menor también escribo un 0, y si lo hay y es menor, entonce escribo la posición de ese numero menor y así hasta crear una lista en orden de la posiciones de los numeros menores y los 0 en caso de no haber un numero menor en la izquierda.

---
### ¿Qué información miras repetidamente?
Las posiciones, los numeros y el respectivo numero a su izquierda.

---
### ¿Qué información se vuelve inútil?
Los numeros a 2 o más posiciones a la izquierda del numero evaluado en turno.

---
### ¿Qué operaciones se repiten?
La comparación de numeros y la escritura de la posición en la otra listas

---
### ¿Qué estructura podría ayudar?
Quizás las pilas ir sacando los elementos de forma LIFO.

---
## Solución Ingenua
### ¿Cuál sería la complejidad en el peor caso?
Sería O(n²), porque para cada posición se podría recorrer casi toda la parte izquierda del arreglo antes de encontrar un valor menor o llegar al final.

---
### ¿En qué tipo de arreglo se repetiría más trabajo?
Se repetiría más en un arreglo decreciente (o casi decreciente), donde no aparece un valor menor temprano y hay que revisar muchos elementos.

---
### ¿Qué información se vuelve a revisar muchas veces?
Se revisan muchas veces los valores de la izquierda, especialmente los que no son menores que el elemento actual, porque para cada nueva posición hay que volver a compararlos.

---
## ¿Por qué la solución ingenua no escala?
### ¿Qué elementos vuelves a inspeccionar varias veces aunque ya conocías su información?
Vuelvo a inspeccionar los elementos anteriores que no eran menores al elemento actual, porque cada vez que avanzo a una nueva posición los tengo que comparar otra vez.

---
### ¿Qué condición hace que un valor anterior nunca vuelva a ser la mejor respuesta para un elemento futuro?
Si un valor anterior es mayor o igual que el elemento actual, entonces no puede ser el menor inmediato a la izquierda de ningún elemento que aparezca después, porque el nuevo elemento actual ya lo supera y el candidato queda descartado.

---
### ¿Qué comparación concreta puedes hacer con el elemento actual para decidir inmediatamente que un candidato ya no volverá a ser útil?
Si el candidato anterior es mayor o igual que el elemento actual, entonces ya no sirve como respuesta para ese nuevo elemento ni para los siguientes, porque el valor actual es menor y será mejor candidato.

---
## Descubrimiento de la pila monótona
### ¿Qué significa que un candidato sea útil? 
Un candidato es útil si aún puede ser la respuesta correcta para algún elemento futuro, es decir, si todavía podría ser el menor más cercano a la izquierda que necesitamos encontrar.
### ¿Por qué algunos candidatos dejan de servir?
Dejan de servir cuando aparece un nuevo valor menor o igual que ellos, porque ese nuevo valor queda más cerca y es mejor candidato para las posiciones futuras.
### ¿Qué propiedad debería mantener la estructura?
Debería mantener los candidatos en orden creciente desde la base hasta la cima, de modo que los valores más grandes se vayan descartando cuando aparece uno menor, y así siempre quede el conjunto de opciones más útiles.

---
## Pseudocódigo parcial
### ¿Por qué se usa “mayor o igual” y no solo “mayor”?
Porque si el valor anterior es igual al actual, también deja de ser útil: el actual está más cerca y, para la búsqueda del menor inmediato a la izquierda, un igual no puede ser mejor que el nuevo elemento si ambos comparten valor y la posición es más reciente.

---
### ¿Qué representa el tope de la pila después de descartar candidatos?
Representa al candidato más reciente que todavía puede ser la respuesta válida para el elemento actual, es decir, el primer valor a la izquierda que podría ser el menor inmediato.

---
### ¿Cuál es el invariante de la pila?
La pila contiene candidatos ordenados de forma creciente de abajo hacia arriba, y todos ellos son potencialmente útiles para el elemento actual o para alguno que venga después; además, los elementos más antiguos y más grandes ya fueron eliminados.

---
## Variante: Nearest Greater Values
### ¿Qué cambia?
Cambia el objetivo, en lugar de buscar el menor a la izquierda, ahora se busca el mayor más cercano a la izquierda.

---
### ¿Qué comparación se modifica?
La comparación cambia de “menor” a “mayor”; en el algoritmo, en vez de descartar candidatos cuando son mayores o iguales al actual, se descartan cuando son menores o iguales.

---
### ¿Se conserva la misma estructura?
Se conserva la misma idea de una pila monótona, pero con la orientación del criterio invertida.

---
### ¿La complejidad cambia?
No, la complejidad sigue siendo O(n) en el peor caso porque cada elemento entra y sale de la pila a lo sumo una vez.

---
## Contraejemplo: Maximum Subarray Sum
### ¿Serviría una pila monótona?
No directamente porque este problema no se resuelve simplemente descartando candidatos por comparación de tamaño como en el caso de vecinos menores o mayores.

---
### ¿Qué información parece importante?
Parece importante la suma acumulada de los subarreglos y cómo esa suma cambia al ir agregando o quitando elementos.

---
### ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?
Porque aquí no basta con mantener un conjunto de valores “útiles” según su orden; también importa cómo combinar partes del arreglo para obtener la mejor suma, y eso depende de relaciones acumulativas, no solo de comparaciones locales.

---
## Vista al futuro: Sliding Window
### ¿Qué información entra?
Entran los nuevos elementos que se agregan a la ventana cuando se desliza.

---
### ¿Qué información sale?
Saliendo de la ventana quedan los elementos que ya no pertenecen a la nueva ventana.

---
### ¿Qué información permanece?
Permanece la información de los elementos que siguen dentro de la ventana y que aún pueden influir en la respuesta.

---
### ¿Por qué recalcular todo sería costoso?
Porque cada movimiento de la ventana obliga a revisar de nuevo muchos datos, y hacerlo desde cero repetiría trabajo que ya se había procesado.

---
### ¿Qué tipo de estructura podría ayudar?
Una estructura que permita insertar, eliminar y consultar rápidamente el elemento más relevante, como un deque o una estructura de datos ordenada especializada.

---
## Diseño de pruebas
### Diseña al menos dos pruebas propias.
Una prueba podría ser para un arreglo con valores repetidos, por ejemplo `[5, 5, 5]`, donde la respuesta esperada es `[0, 0, 0]`, porque ningún valor a la izquierda es estrictamente menor. Otra prueba podría ser `[4, 1, 3, 2]`, donde la respuesta esperada es `[0, 0, 2, 2]`.

---
### Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.
Porque si el algoritmo usa `>` en lugar de `>=`, no descartará un candidato igual al actual, y eso puede bloquear incorrectamente a un valor que debería haber sido reemplazado. Un caso como `[2, 2, 1]` revela el problema, porque el segundo `2` debería hacer que el primer `2` deje de ser candidato.

---
### ¿Qué caso límite no debe faltar?
Un arreglo de un solo elemento, como `[7]`, cuya respuesta debe ser `[0]`.

---
## ¿Qué patrón descubrimos?
### ¿Qué aprendimos sobre diseñar algoritmos?
No basta con encontrar una solución que funcione, sino que también hay que preguntarse si repite trabajo innecesario y si existe una forma de conservar información útil.

---
### ¿Qué significa conservar candidatos útiles?
Significa guardar solo los elementos que todavía pueden ser la respuesta correcta para algún futuro paso, descartando los que ya no sirven.

---
### ¿Qué invariante mantiene la pila?
Mantiene una secuencia de candidatos ordenados de forma creciente y con los valores más grandes descartados, de modo que el tope siempre representa la mejor opción actual.

---
### ¿Qué cambia entre simular y optimizar?
Simular consiste en seguir una idea directa paso a paso, optimizar consiste en identificar qué información se puede reutilizar y cómo evitar revisar lo mismo una y otra vez.

---
### ¿Por qué no todos los problemas con arreglos usan la misma estructura?
Porque cada problema tiene una propiedad distinta, algunos necesitan conservar un orden relativo, otros necesitan sumar, insertar,etc. una sola estructura no sirve para todos.


