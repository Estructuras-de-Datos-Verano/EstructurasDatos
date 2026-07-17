# Clase 12: Notebook
#### Nombre: Patricio Navarro

## Motivación
Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.
- Por ejemplo, en una lista de compras, si tienes muchos elementos, puede que buscar lo que te falta se vuelva complicado o confuso, y tienes que ir leyendo la lista elemento por elemento hasta encontrarlo.
En cambio, si divides esa lista en sublistas acomodadas por importancia o por tipo de producto, será mucho más sencillo encontrar eso que necesitas. Así, lo que espero que mejore es poder descartar aquellos elementos que no aportan a mi búsqueda para poder reducir mi rango de búsqueda.

## Lista vs BST
¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?
- Lo que tiene es que su estructura ya está ordenada dejando a la izquierda los datos menores y a la derecha los datos mayores, entonces a la hora de buscar basta con comparar en que relación cae el dato con cada nodo empezando por la raíz. Y como es binario, pues solo salen dos ramas de cada nodo, entonces vas descartando de mitad en mitad en cada comparación.

## Conteo manual de comparaciones
Árbol balanceado de ejemplo con inserción `8, 4, 12, 2, 6, 10, 14`.
Árbol degenerado de ejemplo con inserción `1, 2, 3, 4, 5, 6, 7`.

Cuenta cuántos nodos se comparan al buscar `14` en ambos árboles.

- Árbol balanceado: 
    1. 14 > 8, -> está a la derecha.
    2. 14 > 12, -> está a la derecha.
    3. 14 = 14, lo encontramos.
    Se comparan 3 nodos.
- Árbol degenerado:
    - Ya sabemos que es como una lista, se tiene que comparar con los 7 nodos porque 14 es mayor que todos los elementos.

**Pregunta.** ¿Qué cambió: los datos o la forma del árbol?
- Los datos, el árbol respetó su estructura, pero los datos estaban ordenados de manera distinta.

## Altura
¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?
- Porque parece que la cantidad de comparaciones que tiene que hacer el programa al buscar son las mismas que los niveles del árbol. Es decir, 
                    `No. de comparaciones = altura`

## Árbol balanceado y árbol degenerado
Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.
- Un bst degenerado es básicamente una recta en diagonal, creciente cuando los datos se ingresaron en órden decreciente y decreciente cuando los datos se ingresaron en órden creciente. Aparece porque como el árbol no admite repeticiones y tiene una regla clara de donde colocar el nodo a la hora de ingresar un dato con respecto al valor del padre, entonces todos los datos se acomodan a la izquierda o a la derecha, y cada nodo tiene un solo hijo.

## Búsqueda y altura
¿Qué relación hay entre profundidad, altura y número de comparaciones?
- Las 3 son directamente proporcionales, porquemientras mayor profundidad, mayor numero de nodos que se deben recorrer, es ecir, comparar y a mayo número de altura pasa lo mismo.

## Animaciones
¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?
- Que las comparaciones y la altura hacen el mismo recorrido y aumentan al mismo tiempo.

## Complejidad
¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?
- Porque si no está balanceado hay la posibilidad de que sea degenerado, y en ese caso buscar en el árbol tiene la misma complejidad que una lista porque la estructura es prácticamente la misma.

## Problemas rlacionados
Elige uno y explica qué concepto de esta clase practica.
- Problema seleccionado: Company queries I
- Concepto de clase: Búsqueda en árbol y conteo de comparaciones o de altura, para definir el nivel en el que está el jefe en la jerarquía y quién es.

## Pruebas y evaluar.py
¿Qué problema resuelve permitir `tests_extra`?
- Que ahora ya podemos hacer el pytest desde cualquier archivo de pruebas que tengamos no solo el test publico y ahora se las podemos aplicar a otrs códigos.

## Revisión técnica de PR
¿Qué debe incluir un comentario técnico útil en el PR?
- Si pasó todas las pruebas o las falló y en caso de que las fallara por qué pudo haber sido.

## Patrón descubierto
Explica el patrón con tus palabras.
- Lo que hace la búsqueda es recorrer únicamente el nodo que le funciona en cada nivel, por eso es importanteque el árbol esté balanceado, así a la hora de buscar sin importar si el valor es menor o mayor, tardaría el mismo tiempo en buscarlo de un lado que del otro siempre que esté en el mismo nivel.

## Cierre
1. ¿Un BST siempre es mejor que una lista?
    - No, cuando el BST está degenerado es prácticamente igual y para tareas simples toda su construcción puede que no sea la más eficiente, hay tareas para las que una lista será mejor por la facilidad de su implementación.
2. ¿Qué relación hay entre altura y comparaciones?
    - Son directamente proporcionales, y por lo que observamos en esta clase el numero de comparaciones es igual a la altura.
3. ¿Cómo se degenera un BST?
    - Ingresando valores ya ordenados.
4. ¿Qué evidencia experimental usarías para justificar tu respuesta?
    - Los tests que realizamos, o una animación.
5. ¿Qué problema relacionado practicarías después?
    - Me llamó la atención el de los counting queries, porque es recorrer el árbol como al revés y además parar en un nivel arbitrario.
