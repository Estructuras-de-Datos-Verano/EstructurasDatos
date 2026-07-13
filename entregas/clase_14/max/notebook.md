# Notebook Clase 14 Max

## Sección 1 (Motivación)

¿Qué operación domina en dos de estos escenarios?

Domina la operacón de reacomodar las cosas, ya que constantemente estamos reacomodadndo las cosas para que queden de manera conveniente, dejando lo más importante (Las cosas con menor valor) hasta la cima.

Si llegan muchas tareas mientras también atendemos tareas urgentes, ¿qué desventaja tendría mantener toda la lista siempre ordenada?

Que si de manera continua siguen llegando tareas urgentes, entonces nunca vamos a atender la  tareas que no lo son, ya que se seguiran quedando al final, al cual nunca llegaremos por esta checando siempre las tareas urgentes.

## Sección 2 (Operación dominante)

¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?

Lo que se repite constantemente son dos cosas principalmente, primero sera la revisión constante para buscar el minimo, y ademas la comparación con los demnas elementos para así efectivamente ver que son minimos, ya que aca el ejempo es sobre una lista cualquiera, no un heap, por lo cual no sabemos ni quien es el mínimo ni cuanto vale.


## Sección 3 (Cola FIFO vs cola de prioridad)

¿Cuándo sería incorrecto usar una cola FIFO?

Como bien podemos recordad FIFO quiere decir fist in fist out, por lo que cupar una cola del tipo FIFO llega a ser contraproducente cuando necesitamos hacer cosas con jerarquia de valores, por poner el ejemplo del hospital, el FIFO sería atender  los pacientes conforme van llegando y una cola de prioridad sera atenter primero a la mujer que esta llegando en labor de parto, por lo que amba cosas son importantes realmente.

## Sección 4 (Descubrimiento manual)



| Valor que llega | Arreglo provisional | Comparación necesaria | Arreglo después de reparar | Intercambios |
| ---: | --- | --- | --- | ---: |
| 7 | `[7]` | no tiene padre | `[7]` | 0 |
| 3 | `[7, 3]` | `3 < 7` | `[3, 7]` | 1 |
| 9 | [7, 3, 9] | 3 < 7 < 9 | [3, 7, 9] | 0 |
| 1 | [7, 3, 9, 1] | 1 < 3 < 7 < 9 | [1, 3, 7, 9] | 3 |
| 6 | [7, 3, 9, 1, 6] | 1 < 3 < 6 < 7 < 9 | [1, 3, 6, 7, 9] | 2 |
| 5 | [7, 3, 9, 1, 6, 5] | 1 < 3 < 5 < 6 < 7 < 9 | [1, 3, 5, 6, 7, 9] | 3 |
| 9 | [7, 3, 9, 1, 6, 5, 9] | 1 < 3 < 5 < 6 < 7 < 9 =< 9 | [1, 3, 5, 6, 7, 9, 9] | 0 |

¿Qué permanece estable después de insertar un valor?

Lo que permanece estable al insertar un valor tenga el valor que tenga sera que una vez ya que todo quede reacomodado, re vera que la raíz siempre va a quedar el elemento más chico como padre de todos los demas elementos.

Completa la fila correspondiente a insertar `9` y explica por qué se detiene la reparación.

Al insertar un 9 no pasa absaolutamente nada a la hora de reordenar las cosas ya que el elemento 9 cumple que es menor igual al 9 que ya tenemos que resulta ser el ultimo elemento de nuestra cola de prioridad, por lo que lo unico que sucede es que se agrega al final de la fila sin tener ningun tipo de modificación.


## Sección 5 (Qué es un heap)

¿Por qué un heap no es un BST?

Lo que sucede es que los BST tienen un orden por decirlo de alguna manera como que total, entonces si se retira algun elemente, ya con las herramientas que ya tenemos implementadas de las clases anteriores podriamos agarrar una nueva raíz y así empezar con el árbol nuevamente,entonces un heap no podría hacer esto.

## Sección 6 (Propiedad de min-heap)

¿Los hermanos deben estar ordenados entre sí?

No, porque de la manera en la que esta definida un heap, es que no hay orden total, si no que unicamente parcial, por lo que si se elimina a un padre esxiste el csao en el que los demas hijo s sean iguales, luego los hermanos no estarian ordenados.

## Sección 7 (Árbol binario completo)

¿Qué ventaja da esta forma para almacenar el árbol?

Que en esta forma de ordenamiento, las ocasas se comportanc más como listas que como cualquier otra cosa, por lo que podemos crear implementaciones de listas que se compartan con los arboles, ahora, esto tambien nos ayuda a analizar los datos más pequeños, ya que acatodo nos va a quedar de alguna manera medio ordenado de menor a mayor.

## Sección 8 (Representación por arreglo)

Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?

Por la manera en la que se ordena en el indice 2, nos quedaría el valor 4.

## Sección 9 (Fórmulas de índices)

¿Cuáles son los hijos del índice 2?

Los indices de los hijos seran: 1 y 2

## Sección 10 (Inserción)

¿Por qué no insertamos directamente en la raíz?

Porque de alguna manera queremos mantener la prioridad que ya tenemos en estos árboles, ademas de no hacerlo y ser agregado a la raíz se puede modificar todo el árbol.

Si insertas `1` en `[2, 5, 4, 9, 8, 7]`, ¿con qué valores esperas que se compare antes de llegar a su posición final?

Se esperaría que se compare con todos los elementos de la lista, cuando se vea que el elemento es el menor se esperaria que quedara como la raíz, o se a que queda como el elemento minimo del cual se van a desprender todos los demas elementos.

## Sección 11 (Sift-up)

¿Cuándo se detiene sift-up?

Se detiene cuando el número que estamos insertando se "levanta" lo suficiente hasta llegar a la posición que le ecorresponde, por poner otro ejemplo, acá si en lugar del 1 hubiese sido 2, hubiese llegado hasta el antipenultimo indice que en este caso sería el 1 no el 0.

## Sección 12 (Extracción del mínimo)

¿Por qué se mueve el último elemento?

Por lo que entiendo, mi teoria es que se agrrara el ultimo elemento, porque hay que recordar que esto no esta bien ordenado, si no que esta parcialmente ordenado, por lo que de no agarra el ultimo elemento, lo que sucedería es que puede que se rompa la manera en la que el heap funciona, entonces al agarra el ultimo elemento y luego proceder a ordenarlo, lo que estamos haciendo es que nos estamos asegurando de que quede bien ordenado todo este asunto.

## Sección 13 (Sift - down)

¿Por qué debemos elegir el hijo menor?

Porque recordemos que a difererncia del arbol binario, aca las cosas no estan odernadas del lado derecho lo más grande y del izquierdo lo pequeño, entonces si caemos en el error de elegir lo del lado izquierdo, entonces muy probablemente vamos a equivocarnos de agarrar el valor minimo como raíz del problema, entonces para evitar esto, directamente hay que agarrar el menor.

## Sección 14 (Visualizaciones ipywidgets)

¿Qué relación observas entre la celda del arreglo y el nodo resaltado?

Lo que observo es que como lo habiamos dicho anteriormente es que se van acomodando las cosas según les corresponde el lugar indicado.


## Sección 15 (Comparación BST, AVL, heap)

¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?

Para busquedas arbitrarias eligiria el AVL por la forma en la que estan almacenados los datos, y para extraere minimos utilizaria el heap, ya que estan como raíz de los demas, entonces estariamos unicamente extrayendo raices

## Sección 16 (Complejidad)

¿Por qué sift-up y sift-down son logarítmicos?

Porque si bien su complejidad va creciendo cada que agregamos más datos, hay un punto donde est complejidad no crec tan rapido, por la manera en la que estan ordenadas los datos, entonces por eso es logaritmico.

## Sección 17 (Last Stone Weight)

¿Cuál es la operación dominante y el resultado del ejemplo?

La operación dominante en estos casos siempre sera el mayor y menor que y no se de cúal ejemplo se habla para dar el resultado.

Pseudocódigo:

```text
Inicio
crear heap con -peso para cada piedra
mientras existan al menos dos:
    mayor = negativo de extraer_min()
    segundo = negativo de extraer_min()
    si mayor != segundo:
        insertar -(mayor - segundo)
devolver el peso restante o 0
```

## Sección 18 (Pruebas)

¿Qué error específico detecta una extracción con varios descensos?

El error en especifico que se detecta en una extracción con varios descendsos es que se puede sacar algo que no sea la raíz, por la maneraen lo queesta definido esto, por lo que hay que tener mucho cuidado a la hora de hacerlo.

Diseña, sin escribir todavía el código completo, una entrada que obligue a `_bajar` a elegir el hijo derecho y explica qué afirmaciones

Esto esta más complicado porque como no esta ordenado como un arbol binario normal del lado derecho no es como que haya algo más grande que lo demas, entonces se me hace que hay que elegir directamente la entrada dle hijo derecho para poder hacerlo, osea se ve la raíz e inmediatamente seleccionas al hijo derecho de esta raíz.


## Sección 19 (Revisión técnica)

¿Qué debe incluir `revision_nombre_revisor.md`?

Nada nuevo que no sepamos, debe de incluir nuestras prubas, el check list y poco más.

¿Qué alerta usarías para indicar que el diff contiene archivos de otro alumno y por qué?

Ocuparía el comentario para así bloquear la insersión a la rama principal y poder hacer los cambios correspondientes.

## Sección 20 (Preparacón)

¿Qué guardaría la prioridad en Dijkstra?

No entiendo muy bien, pero por lo poco que alcanzo a entender es que guardaria el nodo en el que nos encontramos como la prioridad.

Después de procesar C y descubrir una distancia 2 hacia D, ¿qué elemento debería salir antes: B con 4 o D con 2? Justifica usando la operación dominante.

No logro entender la verdad.

## Sección 21 (Cierre)

¿Qué criterio usarás para elegir una estructura en un problema nuevo?

Primero analizaria el problema par aver cual ocupar, ya que a la vista si es bastnte intuitivo cual ocupar, por ejemplo si ocupo hacer algo en jerarquia de importancia ocuparia un heap, si ocupo algo para analizar datos de maner más eficiete, ocuparia un FIFO, en el caso del peso todavia no entiendo muy bien su funcionamiento y por ende no se donde lo podría ocupar.