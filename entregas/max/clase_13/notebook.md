# Clase 13 (Árboles ALV) Max

## Sección 0 (Pregunta inicial)

Si un BST puede convertirse en una lista, ¿cómo podemos impedirlo?

Lo que se me ocurre de como lo podriamos resolver esto es programando un raise Error en los casos en los que se hagan arboles degenerados. 

## Sección 1 (Motivación)

¿por qué un BST básico no garantiza por sí solo búsquedas rápidas?

Por lo mismo que hay casos en los que se pueden crear arboles degenerados, el tema con este tipo de arboles es justo que se parecen a una lista, ademas de esto no necesita ser estrictamente degenerado, simplemente mientras menos balanceado este el arbol, menos se garantizan las busquedas rapidas.

## Sección 2 (Degeneración)

¿qué operación se vuelve costosa cuando el árbol se degenera?

La operación que más ostosa se vuelve a la hora de degenerar un árbol es la de buscar la hoja, ya que aca unicamente hay una unica hoja, la cual se encuentra al final del todo,, y como el arbol esta degenerado existe un unico camino para llegar a ella, el cual necesita ser recorrido en su totalidad para poder llegar a la hoja.

## Sección 3 (Altura y balance)

si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?

Si mal no entendí quiere decir que esta cargado hacia el lado derecho, por lo que contiene más nodos, por lo que no esta del todo balanciado.

## Sección 4 (Ingeniería inversa del algoritmo)

1. ¿Qué problema intenta resolver AVL?
```text

Lo que intenta resolver es justamente los casos en los que se le entrgan datos a manera de listas, en la cual los datos estan acomododados, por lo que a la hora de correrlos, pierden justamente esa caracteristicas de árboles que los hace tan especiales que es que puedas descartar los datos a mitadas.

```

2. ¿Qué información extra debe recordar cada nodo?
```text
Lo que debe de reordar es en que altura esta situado el nodo, ya que a la hora de colocarse es bastante importante tener esto en claro, porque no vamos a poder reacomodar algo de manera efectiva sin antes conocer a ciencia exacta su posición original.

```

3. ¿Qué operación se repite después de insertar?
```text
La operación que más se repite despues de insertar un nodo es la de acomodarlo de manera correcta, ya que constantemente hayq ue estar chacando de manera correcta hasta que si se quede en su lugar indicado, de esta manera el arbol quedara balanceado y ya que el arbol este balanceado ganamos esta eficiencia de los arboles que tanto anelamos.

```

4. ¿Qué propiedad debe conservarse aunque rotemos?
```text
La propiedad que se sebe de preservar de los áboles aun que la rotemos es que a la derecha van a quedar los datos más grandes que el dato raíz y del lado izquierdo los datos más chicos, entonces ganamos esta facilidad de poder descartar a mitades.

```

5. ¿Cómo detectarías con papel y lápiz que hace falta una rotación?
```text
Lo podriamos detectar facilmente unicamente a ojo viendo que la grafica que hicimos no esta bien balanceda por el simple echo de que hay un dato menor o mayor del lado que no corresponda.

```

6. Escribe pseudocódigo breve de inserción AVL.
```text
Inicio
definimos la función rotar izquierda:
definimos la función rotar derecha:
definimos la función AVL:
    si la función no estan balanceada:
        si la función esta cargada a la izq:
            rotar derecha.
        si la función esta cargada a la der:
            rotar izquierda.

```

## Sección 6 (Caso LL)

¿por qué el caso LL se corrige con rotación derecha?

Porque el caso entregado es que los datos se ingresaron de mayor a menor, por lo que l hoja queda como el menor de los datos, luego la reordenación necesaria para el arbol es que debemos de mover a la derecha los datos que quedaron de manera descendente del lado izquierdo del arbol.

1. ¿Qué observas que cambia en la forma del subárbol?

Lo que observo es que lo que hace AVL es que agarra los subarboles como si fueran arboles y ahí es donde aplica las funciones de rotar.

2. ¿Cómo se obtiene el factor `+2` del nodo 30?

Se obtiene de restar la altura del lado derecho y la altura del lado izquierdo del arbos, y como 2 es mayor a 1 reacomoda los satos.

3. ¿Por qué la corrección es una rotación derecha?

Por que es lo que se necesita para balacear bien el arbol, si fuera una roatación izquierda en lugar de una derecha, entonces el arbol ya no quedaria como un arbol binario bien definido.

4. ¿Por qué el inorden debe ser `10, 20, 30` antes y después?

Por la naturaleza en la que funciona inorden, ya que de modificar el orden de 10, 20,30 a algo diferente ya no quedaría la el mismo orden de información (Obviamente) y etso genera problemas a la hora de buscar datos.

## Sección 7 (Caso RR)

¿por qué el caso RR es simétrico al caso LL?

Porque hace exactamente lo mismo pero en sentido contrario, entonces resulta ser un caso realmente analogo al caso LL pero con acomodando los datos de la manera que necesitamos, así que tampoco me atreveria a decir que hay un caso peor o mejor, si no que simplemente se usan a conveniencia.

1. ¿Qué parte del árbol permanece estable en el nivel 2?

La parte que permanece estable en el nivel dos es que los datos en esa altura del arbol no se modifican ya que estan bien orenados, entonces su estabilidad se basa en que no hay que modificar los datos.

2. ¿Por qué el factor de balance es negativo?

Porque en este caso el lado derecho queda más grande que el izquiero entonces a la hora de restar la altura de los extremos vemos que queda un número negativo.

3. ¿Por qué la corrección es una rotación izquierda?

Porque de no hacerlo no lo vamos a balancear de manera correcta, ya que nos quedaria la altura incorrecta.

4. Comprueba el inorden antes y después de rotar.

Antes de rotar se tiene que los datos no estan bien acomodados, por lo que no es la manera más eficiente para analizarlos, y despues de hacerlo se tiene que la altur del arbol ya esta acomodada de manera conveniente, por lo que se ve funciono


## Sección 8 (Caso LR)

¿qué pasaría si intentaras corregir LR con una sola rotación derecha?

No quedaia bien definido, porque la raíz quedaria siendo el número 10, luego del lado izquierdo quedaría el 20, lo cual no es menor a 10, por lo que el árbol binario no quedaría bien definido.

1. ¿Qué nodo ocupa la posición interior que obliga a usar dos pasos?

el nodo que ocupa la posición interior es el que queda de en medio de los 3 nodos eu estamos analizando y se obliga a realizar dos pasos, porque primero hay que rotarlo con la hoja y ya despues se toma en nuevo novo en la posición interior como la nueva raíz.

2. ¿Cuál es el factor del nodo 30 cuando se detecta LR?

Cuando se detecta que  LR el nuevo factor es que se agarra como pivote para así poder agarrar las nodos que nos interesan como un nuevo subarbol, y en este nuevo subarbol ya podemos modificar las cosas a conveneincia para poder terminar con un arbol binario bien definido.

3. ¿Qué corrige la primera rotación y qué corrige la segunda?

La primera corrige la posición interior, para que ne la segunda ´podamos tomarla como la nueva raíz.

4. Verifica el inorden en los tres estados de la tabla.

No cambia. (No se que más gregar)

## Sección 9 (Caso RL)

¿cómo se refleja RL respecto a LR?

Al igual que RR es una situación analoga a LL pero en sentido contrario, RL es analogo a LR pero contrario, de nuevo no hay una mejor que otrs, simplemente las utilizamos segun conveniencia dependiendo del caso en el que nos encontremos.

1. ¿En qué sentido RL es el espejo de LR?

En el que hace exactamente lo mismo pero de manera contraria.

2. ¿Por qué el factor del nodo 10 es `-2`?

Porque esta cargado hacia la derecha este arbol, entonces a la hora de hacer la resta nos queda como factor el -2

3. ¿En qué orden se aplican las dos rotaciones?

Se aplican de manera horaria me parece.

4. Explica por qué el inorden no cambia.

No quedaia bien definido, porque la raíz quedaria siendo el número 10, luego del lado izquierdo quedaría el 20, lo cual no es menor a 10, por lo que el árbol binario no quedaría bien definido.

## Sección 10 (Comparacón entre BST y AVL)

¿en qué momento se separan claramente las alturas y qué trabajo adicional realiza AVL?

Apartir de la cuarta iteracón ya tenemos una diferencia de alturas de dos, lo cual ya nos permitiria utilizar ALV para olucionar este problema.

## Sección 11 (Complejidad)

¿qué costo adicional pagamos al insertar para conservar baja la altura?

Pagamos el costo de tener una comparación extra a la hora de insertar, la cúal es la de ver si el arbol esta o no esta bien acomodado.
## Sección 12 (Varias rotaciones durante una secuencia)

identifica los casos que aparecen y explica por qué AVL se mantiene balanceado continuamente.

Por la revisón constante que se le hace al arbol, si solamente se revisara una unica ocasión esto no sucederia, pero como se analiza varias veces se ve más o menos como va quedando.

## Sección 13 (notebook.md y discusion.md)

escribe una diferencia concreta entre ambos documentos.

La difernecia más concreta entre ambos tipos de documentos, es que en el notebook s contestan cosas relacionadas a la clase del día en cuestión, mientras que en el de discusión se contestn cosas que tienen que ver más que nada con las decisiones tomadaas y nuestro entendimiento con el tema.

## Sección 14 (Revisión técnica)

¿qué evidencia debe incluir una buena revisión técnica?

Debería de incluir cuales fueron los errores y los asiertos que se tuvieron tanto en la implementación como en el notebook, ademas de marcar tuvo que haber sido la respuesta correcta.

## Sección 16 (Cierre)

explica en una frase la idea central de AVL como decisión de diseño.

La idea central es indexar de manera correcta.
