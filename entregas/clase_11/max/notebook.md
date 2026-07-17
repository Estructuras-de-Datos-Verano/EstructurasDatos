# Clase_11_Max

## Sección 1 (Motivación)

¿Qué problema aparece cuando buscamos muchas veces en una lista?

El mayor problema de buscar muchas veces en una lista es que despues de muchas itraciones se vuelve bastante ineficiente, ya que es buscar sobre el mismo lugar un número bastante grande de veces, por lo sue es repetir pasos varias veces.

## Sección 2 (Problemas relacionados)

Elige uno de estos problemas y explica qué concepto de la clase parece practicar.

El problema qur elegí es el 144 (Binary Tree Preorder Traversal) El concepto que se parece practicar en este ejercicio es el de los nodos, y en más concreto va a ser del modo DFS por que, al buscarse los datos va a ser la manera más eficiente para solucionar este tipo de problemas en especifico. Ademas por lo que alcanzo a leer en el ejercicio 3, los arboles unicamente pueden tener a lo más dos hijos del lado izquierdo y del lado derecho.

## Sección 3 (Conceptos basicos)

Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.

Lo describire por que no se como dibujarlo acá en el notebook, todo empieza en un punto central que se llama nodo, de donde van a salir todas las demas ramas, ahora en el caso de que solamente tenga dos ramas se llamara arbol binario y las ramas se llaman, la del lado izquierdo, y la del lado deerecho, que ademas todo lo demas que va a salir de este nodo sera llamado como un hijo, ahora una hoja es un nodo que no esta conectado a nada más, osea como un punto muerto en donde termina el arbol, Su altura total del arbol va a ser el número más alto de nodos contando desde la hoja hasta el nodo principal, y un subarbol vendría siendo como un subconjunto del arbol original.

## Sección 4 (Árbol binario de búsqueda)

¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?

Poruq esi lo que buscamos es un número grande, de entiende que podemos ignorar por completo el lado de los números chicos, y lo mismo pasa con los números chicos analogamente, entonces, es un modo más eficiente de busqueda, ya que no solamente tienes que analizar la mitad de los datos, si no que tambien por la manera en la que estan ordenadas los números ya sabes hacia a donde ir.

## Sección 5 (Búsqueda)

¿Qué nodos comparas y qué parte descartas en cada paso?

Lo primero que pasa es que veo que el nodo actual en el que estoy no es el número que estoy buscando, entonces procedo a buscarlo, como veo que del lado derecho se pasa del número que quiero, que es el número 9, entonces me procedo a mover al lado izquierdo, luego una vez en este lado repito el proceso, del lado izquierdo observo que el número que busco es menor al que quiero, hací que volteo a ver el del lado derrecho y veo que es el que busco y ahí acabo el código.

## Sección 6 (Inserción)

Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

Como empezamos en el 8, este será el nodo, luego del lado de la rama izquierda tenemos al número 4 y de la rama del lado derecho al número 10, luego del 4, sale como rama izquierda el número2 y como rama derecha el número 6, y de la rama derecha del 8 (O sea el número 10) tendremos como rama izquierda al 9, y como rama derecha al 12.

Ahora como se pidio en clase voy a explicar lo que pasa cuando def.insertar, aca lo que esta pasando es que que es primerose valida que el valor actual (En el que estoy parado) no sea None, porque si si lo es lo puedo actualizar en valor rapidamente, si no 

## Sección 7 (Altura)

¿Qué relación hay entre altura y costo de búsqueda?

Mientras mayor sea la altura de un arbol, más tiempo de busqueda va a necesitar y por lo tanto más recursos seran gastados para encontrar el valor deseado en el mismo.

## Sección 8 (Recorridos)

¿Por qué inorden produce valores ordenados en un BST?

Por la maera que va iterando sobre el arbol, como se va moviendo de izquierda, a arriba luego vuelve a bajar a la derecha, el arbol queda de manera ordenada para el ojo humano, ya que es la manera natural en la qu leemos.

## Sección 9 (Animaciones)

¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

Lo que siento que más nos ayuda es a ver que tipo de busqueda se tiene en este mismo arbol, por decir un ejemplo, nos ayuda a ver si es de tipo BFS o DFS a la hora e buscar la información del nodo, ahora no creo que nos ayude a ver como son los arboles, ya que como unicamente estamos trabajando con arboles binarios, con ver la lista se lo puede imaginar uno.

## SecciÓn 10 (Implementación)

¿Qué métodos parecen depender naturalmente de recursión?

Los metodos, altura, inorden, postorden y preorden, porque son los cuales necesitas analizar todo el arbol antes de hacer cosas, si no definimos algo recursivamente, entonces tenemos problemas a la hora de resolver los problemas ya que lo que analizo que ha pasado es que te vas por una rama erronea.


## Sección 11 (Pruebas)

¿Qué problema resuelve `evaluar.py`?

El problema que intenta resolver este archivo es el de facilitar las pruebas con los test en el archivo de los teste_publicos.

## Sección 12 (Patrón descubierto)

Explica con tus palabras el patrón descubierto.

El patrón que descubri a lo largo de la clase de hoy es que no se necesitan analizar absolutamente todos los datos en un arbol para poder obtener lo que necesitamos, y esto es muy importante porque de esta manera economisamos recursos.

## Sección 13 (Cierre)

1. ¿Qué ganamos frente a una lista?

Ganamos que podemos jerarquizar cosas en primer lugar, luego que con esta jerarquización podemos buscar datos de una manera más eficiente.

2. ¿Qué propiedad mantiene el BST?

La de preorden, ya que tiene el mismo tipo de busqueda con los vecinos.

3. ¿Qué pasa si insertamos datos ordenados?

No pasa nada por la manera en la que definimos la función insertar

4. ¿Cuándo podría degradarse un BST?

Cuando intentamos hacer el metodo de preorden, ya que en este metodo nos convendria más utilizar algo del estilo DFS ya que se tiene que definir una función auxiliar para ir hasta el fondo del todo.

5. ¿Qué problema relacionado puedo practicar?

Puedo intentar ver arboles separados e intentar relacionarlos.