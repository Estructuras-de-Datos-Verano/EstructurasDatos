# Notebook - Clase 11 - Leonardo Daniel Arenas Serafín

## 1. Motivación

#### ¿Qué problema aparece cuando buscamos muchas veces en una lista?
La complejidad del probleme crece mucho, pues en el peor de los casos uno debe recorrer toda la lista para encontrar un solo elemento.

## 2. Problemas relacionados

#### Elige uno de estos problemas y explica qué concepto de la clase parece practicar.
145. Binary Tree Postorder Traversal. 
Parece practicar los grafos, pues se puede notar que un árbol es un grafo que solo tiene a lo más dos aristas por cada nodo. De igual manera, parece ser que el output de este problema es como el output de un recorrido por niveles de un grafo pero al revés.

## 3. Conceptos básicos

#### Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.

            A
           / \
          B   C
         / \   \
        X  Y    Z

Raíz: A
Hijos: B, C de A. X, Y de B. Z de C.
Hojas: X, Y, Z

## 4. Árbol binario de búsqueda

#### ¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?
Porque si estamos buscando un valor específico, al compararlo con un nodo actual, podemos ir descartando mitades hasta llegar al valor que queremos. Pues comparamos el nodo actual con el valor esperado, si el valor del nodo es menor, se descartará todo el subárbol derecho, pues éste contiene valores mayores o viceversa, y así con cada nodo hasta encontrar el qu buscamos.

## 5. Búsqueda

#### ¿Qué nodos comparas y qué parte descartas en cada paso? 

            6
           / \
          4   8
         /     \
        2       9
                 \
                 10
                   \
                    12

En la primera iteración tenemos al 6. Como no es 9 y 9 es mayor que 6, nos movemos al lado derecho y descartamos el izquierdo, es decir, descartamos al 4 y 2. Después sigue 8, como 9 no es igual a 8, avanzamos en la única dirección posible, a la derecha. Llegamos al 9, como 9=9. Paramos el algoritmo ahí y hemos encontrado nuestro valor buscado.


## 6. Inserción

#### Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

            6
           / \
          4   8
         /     \
        2       9
                 \
                 10
                   \
                    12

La raíz la tomamos como 6. Después a la izquierda ponemos el 4 pues es menor que 6 y a la izquierda ponemos el 2 porque es menor que 4. A la derecha de la raíz ponemos 8, porque es mayor que 6, luego a la derecha ponemos 9 porque es mayor que 8, después a la derecha ponemos 10 porque es mayor que 9 y a la derecha ponemos 12 porque es mayor que 10.

Ahora haciéndolo una vez hecha la implementación Para insertar primero inicializamos un arbol vacío. Al querer insertar el 6, como es un árbol vacío y su raíz es None, se agrega el 6 como raíz. Despus queremos agregar el 4. Como la raíz no es None, comparamos. Como 4 es menor a 6 y 6 no tiene hijo izquierde, se inserta a su izquierda 4. Como 4 no tiene hijo a la izquierda y 2 es menor a 4 y 4 a 6, se inserta a su izquierda. Comparamos 8 con 6, como es mayor y 6 no tiene hijo derecho, se inserta a su derecha. Como 8 no tiene hijo a la derecha y 9 es mayor a 8 y 8 a 6, se inserta a su derecha.
Como 9 no tiene hijo a la derecha y 10 es mayor a 9 y 9 a 8 y 8 a 6, se inserta a su derecha. Como 10 no tiene hijo a la derecha y 12 es mayor a 10 y 10 a 9 y 9 a 8 y 8  a 6, se inserta a su derecha.

#### ¿Qué relación hay entre altura y costo de búsqueda?
Como por cada comparación de cada nodo o te quedas con ese nodo, o avanzas a la izquierda o a la derecha, realizas una operación por cada nivel. Esto quiere decir que en el peor de los casos, el número de operaciones realizadas es el número máximo de niveles en el árbol. Es decir, la complejidad de la estructura es su altura.

## 8. Recorridos

#### ¿Por qué inorden produce valores ordenados en un BST?
Porque el árbol esta ordenado para que a la izquierda siempre hayan valores menores a la raíz y a la dereca mayores. Por lo que si tu recorrido es izquierda, raíz, derecha; vas produciendo con valores menores a los siguientes valores y que son siempre mayores a los anteriores. Es decir, nos quedamos con una lista ordenada.

## 9. Animaciones

#### ¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?
En la animación se ve claramente cómo es el proceso de Inserción, de Búsqueda; pero especialmente te ayuda a entender cuáles son los tipos de recorridos en orden.

## 10. Implementación

#### ¿Qué métodos parecen depender naturalmente de recursión?
El método de altura, pues para poder saber cuál es la altura de un árbol, uno debe de checar recursivamente nodo por nodo e ir agregando uno al conteo de niveles. De igual forma, todos los métodos de orden requieren de una recursión naturalmente porque siempre empiezas desde el final y debes de seguir hacia arriba con el mismo patrón.

## 11. Pruebas

#### ¿Qué problema resuelve `evaluar.py`?
Resuelve que ya no tenemos que complicarnos tanto para poder realizar el pytest, sino que ya solamente con escribir una línea de código en la terminal se pueda hacer correctamente.

## 12. Patrón descubierto

#### Explica con tus palabras el patrón descubierto.
El patrón que existe dentro de un árbol binario invariante es que siempre para cada subárbol, las ramas izquierdas son valores menores a la raíz y las derechos son mayores. Esto permite que a la hora de buscar un valor en el árbol, puedas descartar muchos elementos para no tener que revisarlos todos por cada paso, lo cual ahorra muchos recursos. Al ser un árbol binaro, por cada nodo puede haber a lo más dos hijos. Y lo más importante es que este tipo de estructura establece una jerarquía entre los datos almacenados.

## 13. Cierre

#### ¿Qué ganamos frente a una lista?
Ganamos que en una lista el único criterio de orden es la secuencia de los elementos, mientras que en el árbol existe un criterio de jerarquía mucho más profundo. Asimismo, nos ofrece la ventaja de que al querer encontrar un valor dentro de la estructura, puedes descartar revisar muchos elementos paso a paso, mientras que en la lista tendrías que revisar exhaustivamente todos sus elementos.

#### ¿Qué propiedad mantiene el BST?
Mantiene la propiedad de que por cada nodo solo puede haber a lo más dos hijos, los cuales a la derecha son valores menores a la raíz y a la derecha mayores.

#### ¿Qué pasa si insertamos datos ordenados?
Al insertar datos ordenados simplemente se crea una especia de "línea recta" hacia la derecha 

#### ¿Cuándo podría degradarse un BST?
Cuando en las hojas del árbol tenemos valores ordenados, por lo que ya no podríamos insertar nuevos valores que se encuentren en ese rango

#### ¿Qué problema relacionado puedo practicar?
Podríamos practicar el problema de Labrynth. Ya que para poder llegar de punto A a punto B, bastaría simplemente con establecer la raíz como A y buscar el valor B para ver si es posible llegar, para posterioirmente calcular las alturas de las ramas que llegan a B y compararlas para encontrar el camino más corto.