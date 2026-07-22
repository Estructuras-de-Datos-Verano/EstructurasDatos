# Notebook clase 12 Max

## Sección 1 (Motivación)

Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.

Un claro ejemplo de cuando una lista es bastante más costoso que en un arbol, es cuando se necesita revisar el listo dato del mismo, ya que en la lista se tienen que recorrer todos los valores, mientras que en el arbol se pueden ignorar varios para llegar al final.

## Sección 2 (Lista vs BST)

¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?

Las listas solamente tienen orden pero no cuentan con una jerarquia, los arboles si, esta es la diferencia elemental que te ayuda a descartar partes del arbol.

## Sección 3 (Conteo manual de comparaciones)

¿Qué cambió: los datos o la forma del árbol?

Lo que cambia es que en el primer caso, el arbol esta bien acomodado, o sea tiene la regla que va lo menor del lado izquierdo y lo mayor del lado derecho, en el segundo arbol no queda bastante clara cual es la implementación realmente, ya se pueden confundir las ramas.

## Sección 4 (Altura)

¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?

Porque la altura de un arbool nos dice que tan profundo tienen que ir nuestras busquedas, ya que no es lo mismo buscar en un arbol de tres nodos con altura dos que en uno igualmente de tres nodos pero de altura 3.

## Sección 5 (Árbol balanceado y árbol degenerado)

Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.

La forma que tiene es como si colgaramos un ancla desde el techo, cada eslavon es un nodo y así hasta llegar al ancla que es la hoja, osea se comporta de manera de lista, ya que los elementos se de la lista nse recorren de manera unilateral (izq a der) y los de este arbol igual (arriba a abajo).


## Sección 6 (Búsqueda y altura)

¿Qué relación hay entre profundidad, altura y número de comparaciones?

La profundidad del algoritmo esta estrictamente relacionada a la altura del arbol, ya que entre más alto sea el arbol, más profunda sera la busqueda y pues entre más profunda sea la busqueda habra un mayor número de comparaciones.

## Sección 7 (Experimentos)

¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?

No realmente, ya que la complejidad de esta busqueda siempre sera lineal, por lo mismo que se parece a una lista.

```python
valores_balanceados = [8, 4, 12, 2, 6, 10, 14]
valores_degenerados = [1, 2, 3, 4, 5, 6, 7]
objetivos = [2, 6, 10, 14]

print('Usa estos datos para comparar altura y comparaciones en tu implementación.')
print('Balanceado:', valores_balanceados)
print('Degenerado:', valores_degenerados)
print('Objetivos sugeridos:', objetivos)

valores_balanceados = [8, 4, 12, 2, 6, 10, 14]
valores_degenerados = [1, 2, 3, 4, 5, 6, 7]
objetivos = [2, 6, 10, 14]

arbol_balanceado = None
for v in valores_balanceados:
    arbol_balanceado = insertar(arbol_balanceado, v)

arbol_degenerado = None
for v in valores_degenerados:
    arbol_degenerado = insertar(arbol_degenerado, v)
```
El analizis de esto se ve claramente que nos iguales, las implementaciones de lor arboles varia realmente en su implementación y altura.

## Sección 8 (Animaciones)

¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?

Lo que muestra es lo que ya sabiamos, que es que buscar en unarbol es bastante más eficiente que hacerlo en una lista, ya que no se recorre completamente, solamente lo hace en una fracción del arbol, y es por eso que el arbol degenerado se parece mucho a una lista.

## Sección 9 (Complejidad)

¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?

Poruqe para ver que la complejidad crece de manera logaritmica es necesario ver que este balanceado, ya que de no estarlo podemos caer en el caso de un arbol degenerado, en donde la complejidad es continua.

## Sección 10 (Problemas relacionados)

Elige uno y explica qué concepto de esta clase practica.

El problema que voy a elegir es el de el diametro del arbol, y este problema es bastante util a la hora de examinar cual es la altura de un arbol, ya que el diametro del arbol se define como la distancia entre el nodo principal y la "ultima hoja" del arbol, y esto viene siendo la altura.

## Sección 11 (Evaluar.py y pruebas)

¿Qué problema resuelve permitir `tests_extra`?

Resuelve el problema que cuando queramos aplicar los test que nosotros creamos los podamos aplicar a nuestros compañeros, o sea permite que e ocupe en diferentes programas sin la necesidad de andar implementando cosas.

## Sección 12 (Revisión técnica de PR)

¿Qué debe incluir un comentario técnico útil en el PR?

Debería incluir el nombre de la carpeta en la que se encuentra la implementación (En nuestro caso es bastante obvio porque todos tenemos el mismo nombre por formato), pero en el caso de usarlo en una empresa donde cada quien guarda las cosas en carpetas con nombres a conveniencia entonces el poner el nombre en el comentario nos va a ayudar a saber de donde vamos a jalas la implementación para correr las pruebas.

## Sección 13 (Patrón)

Explica el patrón con tus palabras.

El patron descubierto es que vamos a poder saber mas o menos si esta balanciado o no el arbol sabiendo el número de nodos y la ultura, y ya sabiendo esto sabremos que metodo ocupar para analizarlo, ya que si esta balanceado podemos ocupar metodos de los arboles tradicionales, y si no lo esta podemos utilizar los metodos de las listas.

## Sección 14 (Cierre)

1. ¿Un BST siempre es mejor que una lista?
```text
Por lo general si, ya que nos ayuda a ahorraarnos checar cosas de más que normalmente resultan ser innecesarias, entonces con esto podemos ahorrar tiempo y recursos.

```

2. ¿Qué relación hay entre altura y comparaciones?
```text
Entre mayor sea la altura mayor va a ser la profundidad, y por lo tanto mayores seran el número de comparaciones.

```

3. ¿Cómo se degenera un BST?
```text
Se genera de manera escalonada acomodando los valores si es que agarramos la clase Arbolbinariobusqueda, si ocupamos el ".construir" las cosas se iran agregando en el orden correspondiente.

```

4. ¿Qué evidencia experimental usarías para justificar tu respuesta?
```text
Usaría los asserts que ya estan implementados, que ahí se ve claro lo que digo.

```

5. ¿Qué problema relacionado practicarías después?
```text
practicaria con el nuevo tipo de arboles degenerados para ver que tipo de cosas se pueden hacer.

```