# Notebook - Clase 12 - Leonardo Daniel Arenas Serafín

## 1. Motivación

#### Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.
Por ejemplo, imaginemos que tenemos una lista con todos los enteros ordenados del 1 al 1,000,000 y nosotros queremos encontrar el número 999,000. En una lista, encontrar este número nos tomaría 999,000 pasos para encontrar dicho número. Ahora tomemos un árbol que empiece en 500,000 y a la izquierda esté 250,000 y a la derecha 750,000. Es decir, partimos a la mitad el millón, para luego volver a partir a la mitad con los hijos y así repetidamente hasta terminar. Por ejemplo, el siguiente nivel sería: 125,000 a la izquierda de 250,000 y 375,000 a su derecha. 625,000 a la izquierda de 750,000 y 875,00 a la derecha. De esta forma, solamente en los primeros 3 pasos ya llevamos 875,000 pasos menos que en una lista.

## 2. Lista vs BST

#### ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?
En un BST no solo importa el orden, sino que importa el valor del elemento. En el árbol, podemos discernir sobre si ir a la izquierda o a la derecha dependiendo del nodo en que nos encontremos al comparar su valor con el del buscado: En cambio en una lista, lo único que existe es el orden secuencial, mientras que los valores de los elementos no tienen relevancia alguna.

## 3. Conteo manual de comparaciones

#### Cuenta cuántos nodos se comparan al buscar `14` en ambos árboles.
- `8, 4, 12, 2, 6, 10, 14`: 3
- `1, 2, 3, 4, 5, 6, 7`: 7

#### ¿Qué cambió: los datos o la forma del árbol?
Cambiaron ambos. Principalmente cambiaron los datos y éstos cambiaron la forma del árbol.

## 4. Altura

#### ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?
Porque la complejidad de la búsqueda en un árbol es la altura, ya que en el peor de los casos es el número de comparaciones necesarias para llegar a un resultado. En cambio la cantidad de nodos en sí sola no nos dice nada directamente. Es cierto que existe una proporcionalidad directa entre nodos y altura, pero la cantidad de nodos puede variar mucho en cuanto a complejidad.

## 5. Árbol balanceado y árbol degenerado

#### Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.
Un BST tiene una forma similar a una "recta" pues cada nodo tien a lo más un hijo y eso provoca que solamente haya una dirección. Puede aparecer al insertar valores ordenados porque si tu insertas todos los primeros n naturales en orden, l árbol irá insertando cada número a la derecha del anterior, formando la dichosa recta.

## 6. Búsqueda y altura

#### ¿Qué relación hay entre profundidad, altura y número de comparaciones?
El número de comparaciones es el costo propio de hacer una búsqueda de un número, mantiene relación con la altura en sentido de que en el peor de los casos, la complejidad de una búsqueda es la altura. De esta forma, esto se relaciona con la profundidad pues éste es el nivel en el que un número buscado se encuentra, el cual es exactamente el número de comparaciones y a lo más puede ser la altura.

## 7. Experimentos

#### ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?

```python
valores_balanceados = [8, 4, 12, 2, 6, 10, 14]
valores_degenerados = [1, 2, 3, 4, 5, 6, 7]
objetivos = [2, 6, 10, 14]

print('Usa estos datos para comparar altura y comparaciones en tu implementación.')
print('Balanceado:', valores_balanceados)
print('Degenerado:', valores_degenerados)
print('Objetivos sugeridos:', objetivos)

from implementacion import *

arbol_b = ArbolBinarioBusqueda()
arbol_d = ArbolBinarioBusqueda()

for v in [8, 4, 12, 2, 6, 10, 14]:
    arbol_b.insertar(v)
for v in [1, 2, 3, 4, 5, 6, 7]:
    arbol_d.insertar(v)
for v in [2, 6, 10, 14]:
    print("Balanceado: objetivo", v, ":", arbol_b.comparaciones_busqueda(v))
    print("Degenerado: objetivo", v, ":", arbol_d.comparaciones_busqueda(v))
```
        Usa estos datos para comparar altura y comparaciones en tu implementación.
        Balanceado: [8, 4, 12, 2, 6, 10, 14]
        Degenerado: [1, 2, 3, 4, 5, 6, 7]
        Objetivos sugeridos: [2, 6, 10, 14]
        Balanceado: objetivo 2 : 3
        Degenerado: objetivo 2 : 2
        Balanceado: objetivo 6 : 3
        Degenerado: objetivo 6 : 6
        Balanceado: objetivo 10 : 3
        Degenerado: objetivo 10 : 7
        Balanceado: objetivo 14 : 3
        Degenerado: objetivo 14 : 7

No necesariamente. Es cierto que la diferencia de comparaciones tiende a aumentar directamente proporcional tamaño del árbol degenerado, pero no es una regla. Depende mayormente de los valores de los datos del árbol.

## 8. Animaciones

#### ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?
Muetra que un árbol balanceado tiende a hacer menos comparaciones comparado con un árbol degenerado. Además que el límite de comparaciones de un árbol balanceado es la altura, la cual es mucho menor que el número de nodos; mientras que en un árbol degenerado el límite de comparaciones es el número de nodos.

## 9. Complejidad

#### ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?
Porque cuando el árbol en cuestión se acerca más a ser un árbol balanceado, la complejidad tiende a ser O(log n), mientras que cuando el árbol se acerca más a ser un árbol degenerado, la complejidad tiende a ser O(n), pues se empieza a parecer a la estructura que tiene la lista y la lista tiene esta complejidad. Por lo tanto el balance del árbol influye fuertemente en su complejidad.

## 10. Problemas relacionados

#### Elige uno y explica qué concepto de esta clase practica.
- Subordinates: Este problema se trata acerca de que representamos la estructura de una compañía como un árbol, el cúal es la estructura de poder. Este problema busca saber cuál es el número de subordinados de un empleado. Para hacer esto, primero necesitamos aplicar el método de contiene() para primero encontrar al empleado buscado. Posteriormente debemos de tomar al empleado encontrado como la raíz de su subárbol, para después aplicarle el método de cantidad_nodos() para ver cuántos nodos hay en dicho subárbol y así obtener el número de subordinados. 

## 11. evaluar.py y pruebas

#### ¿Qué problema resuelve permitir `tests_extra`?
A partir de esta clase, al hacer la revsión de otro compañero, buscaremos no solo revisar que sus tests con su implementación hayan sido correctos, sino que tus propios tests con su implementación también sean correctos para hacer una verificación mucho más profunda. De esta forma, `tests_extra` busca resolver todos los problemas relacionados con acceder a los documentos del compañero y tener que hacer muchos commandos al simplemente ser una función que al correr un solo comando se haga todo.

## 12. Revisión técnica de PR

#### ¿Qué debe incluir un comentario técnico útil en el PR?
Debe incluir un análisis y una interpretación de la salida de la terminal al correr el comando de hacer la verificación para resaltar errores o para revalidar la implementación.

## 13. Patrón descubierto

#### Explica el patrón con tus palabras.
Se ha visto que en un árbol balanceado, la altura siempre es menor al número de nodos, mientras que en el árbol degenerado, la altura siempre es igual al número de nodos. De esta manera, el límite de comparaciones que se pueden hacer en un árbol balanceado es la altura, mientras que en uno degenerado es el número de nodos. Por otro lado, hemos visto que para que un árbol tienda a ser balanceado o degenerado, importa mucho tanto cuáles son los valores de los datos insertados, pero principalmente cuál es el orden de los valores insertados, ya que estos dos aspectos cambian totalmente la estructura del árbol. 

## 14. Cierre

#### ¿Un BST siempre es mejor que una lista?
No siempre, en la mayoría de ocasiones suele ser mejor aunque sea por una operación, pero cuando tenemos un árbol degenerado, es el igual que una lista.

#### ¿Qué relación hay entre altura y comparaciones?
La altura es el límite de comparaciones que se pueden hacer para encontrar un valor dentro del árbol.

#### ¿Cómo se degenera un BST?
Se degenera cuando agregas valores de datos que van de menor a mayor o vicecersa en orden consecutivo. 

#### ¿Qué evidencia experimental usarías para justificar tu respuesta?
La evidencia encontrada en la seccion 7. Experimentos.

#### ¿Qué problema relacionado practicarías después?
Siguendo con el mismo problema de las clases pasadas, en el problema de CSES de Labrynth, si el camino que tenemos disponible es un árbol degenerado, implica que solamente hay un único camino disponible a seguir, pero si tenemos un árbol balanceado, tendremos muchas más posibilidades de caminos, lo que complica el llegar a una respuesta.