# seccion 1
¿Qué problema aparece cuando buscamos muchas veces en una lista?
    Se consume mucha memoria y no es optimo 

# seccion 2
Problema eleigdo:

- [Subordinates](https://cses.fi/problemset/task/1674/): árboles y jerarquías.

    El problema de CSES nos pide calcular cuántos subordinados directos e indirectos tiene cada empleado dentro de una empresa. Para nosotros, está lidiando con un árbol enraizado donde el empleado $1$ (el director general) es la raíz, y cada empleado puede tener múltiples hijos (subordinados).

# seccion 3
```python
[1,2,3,4,5,null,8,null,null,6,7,9]
```
Explicacion: 

- La raiz es el 1: del uno salen dos nuevos nodos, 2 y 3
- De 2 salen 4 y 5
- De 3 solo sale 8
- De 5 sale 6 y 7 
- De 8 sale 9

# seccion 4
¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?

    Porque cuando eliges un lado, sabes que tu objetivo de busqueda tiene una relacion de valor estrcita (<,>) respecto al otro lado no elegido, asi, descartas todo lo demas

# seccion 5
¿Qué nodos comparas y qué parte descartas en cada paso?

    1. Partimos de 8
    2. Eligo 10, descarto 4
    3. Eeligo 9, descarto 12

# seccion 6
Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

```python
[8, 4, 10, 2, 6, 9, 12]
```    
- El 8 queda como raiz
- El 4 a la izquierda del 8
- El 10 a la derecha del 8
- el 2 a la izquierda del 4
- El 6 a la derecha del 4
- el 9 a la izquierda del 8
- el 12 a la derecha del 10

# seccion 7
¿Qué relación hay entre altura y costo de búsqueda?

    a mas altura, mas costo 

# seccion 8
¿Por qué inorden produce valores ordenados en un BST?

    Por el invariante del modelo, pues la relacion de orden queda asi:
izquierda $>$ raiz $>$ derecha

# seccion 9
¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

    Ayuda mucho a visualizar como funciona y el orden el arbol, sobre todo a ver como estan insertados los hijos, pues en la lista es confuso 

# seccion 10
¿Qué métodos parecen depender naturalmente de recursión?

    todos aquellos que necesitan recorrer todo el arbol (altura, los ordenes, insertar)

# seccion 11
¿Qué problema resuelve `evaluar.py`?
    para mi, tuve varios problemas pues tuve que mover mis pruebas al test_publicos y aho correr el comando para las pruebas

# seccion 12
Para nuetra estrategia, primero necesitamos entender como funcionan los arboles BST y con ello podemos manejar los datos; Para emepzar la forma en que se ordena los datos nos prestan mucha facilidad para buscar datos con rapidez por la relacion de orden de mis datos, a la izquierda los menores y a la derecha los mayores (el invariante de BST)

# seccion 13
1. ¿Qué ganamos frente a una lista?
    Mas facilidad para bsucar y sobre todo visuzalizar los datos
2. ¿Qué propiedad mantiene el BST?
    - todos los valores del subárbol izquierdo son menores que el valor del nodo;
    - todos los valores del subárbol derecho son mayores que el valor del nodo.
3. ¿Qué pasa si insertamos datos ordenados?
    de manera ascendente, se crea un arbol de una linea recta
4. ¿Cuándo podría degradarse un BST?
    cuando no se aprovecha la capacidad que tiene el arbol para desechar muchos datos en un solo paso
5. ¿Qué problema relacionado puedo practicar?
    respuesta dada por una IA:
    El Problema a Practicar: "Invertir un Árbol Binario"
    El problema es simple de enunciar pero muy revelador: dado un árbol binario, convierte cada nodo en su "espejo". Esto significa que, para cada nodo, todos sus hijos izquierdos deben pasar a ser hijos derechos, y viceversa.

