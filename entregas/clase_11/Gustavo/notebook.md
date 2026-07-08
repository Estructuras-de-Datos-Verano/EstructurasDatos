# Notebook - Clase 11 - Gustavo Torres 

## 1. Motivación

¿Qué problema aparece cuando buscamos muchas veces en una lista?

Que la lista no mantiene un orden y tiene repetición, entonces al introducir una gran cantidad de datos, si llegan a haber algunos repetidos puede llegar a generar problemas.

## 2. Problemas relacionados

Elige uno de estos problemas y explica qué concepto de la clase parece practicar.

Problema: 
Concepto: 

## 3. Conceptos básicos

Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.

                        x
                       /  \ 
                      y    z
                     / \  / \ 
                    a   b c  d

## 4. Árbol binario de búsqueda

¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?



## 5. Búsqueda

¿Qué nodos comparas y qué parte descartas en cada paso?

1. Comparas con 8, es mayor se va a la derecha.
2. Comparas con 10, es menor, se va a la izquierda
3. Finalmente el 9 queda abajo a la izquierda del 10


## 6. Inserción

Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

                    8
                   / \
                  4   10
                 / \  / \
                2   6 9  12

Tomo 4, veo si es mayor ó menor a 8, después toma su lugar, así con cada uno de los números dados.

## 7. Altura

¿Qué relación hay entre altura y costo de búsqueda?

Es directamente proporcional

## 8. Recorridos

¿Por qué inorden produce valores ordenados en un BST?

Debido a la combinación directa entre la forma en que se visitan los nodos y la propiedad fundamental (invariante) de la estructura.

## 9. Animaciones

¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

Comprender como vamos tomando posiciones en realidad en una lista para ponerlo en el árbol.

## 10. Implementación

¿Qué métodos parecen depender naturalmente de recursión?

La gran mayoría de sus métodos principales dependen naturalmente de la recursión para su implementación.

## 11. Pruebas

¿Qué problema resuelve `evaluar.py`?

Que al podemos llamar las funciones sin necesidad de tener dentro de las carpetas algunas definiciones. Así podemos llamar archivos de distintas carpetas para poder ejecutarla en una nueva carpeta.

## 12. Patrón descubierto

Explica con tus palabras el patrón descubierto
Consideramos datos, examinamos varias veces si dato dentro de la lista existe. Luego verificamos el lugar que corresponde al dato para más tarde 
## 13. Cierre
1. ¿Qué ganamos frente a una lista?

    Ganamos una mayor eficiencia en las búsquedas

2. ¿Qué propiedad mantiene el BST?

    Mantiene el invariante de que, para cada nodo, todos los valores de su subárbol izquierdo son estrictamente menores y todos los de su subárbol derecho son estrictamente mayores.

3. ¿Qué pasa si insertamos datos ordenados?

    El árbol se desbalancea por completo y se convierte en una estructura lineal o degenerada, perdiendo todas sus ventajas de distribución jerárquica.

4. ¿Cuándo podría degradarse un BST?

    Se degrada cuando los elementos se introducen en un orden secuencial (ya sea estrictamente creciente o decreciente), lo que hace que su altura sea igual al número total de nodos.

5. ¿Qué problema relacionado puedo practicar?

    Puedo practicar el problema "Subordinates" de la plataforma CSES o los problemas 700 ("Search in a Binary Search Tree") y 701 ("Insert into a Binary Search Tree") en LeetCode.


