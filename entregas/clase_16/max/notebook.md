# Notebook Clase 16 Max

## Sección 0 (Pregunta inicial)

¿Cómo se convierte en una implementación confiable, reutilizable y testeable?

La manera principal es solucionando errores o asegurandonos que no los hay, luego hay que ver que los costos de cada carretera esten implementados correctamente para evitar errores.

## Sección 1 (De algoritmo de software correcto a confiable)

¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?

Las responsibilidades principales que aparecen son las de  mantener los pesos correctamente, luego las de ver que no haya errores a la hora de volver a implementarse, y por ultimo ver que la relajación, el min-heap y demas se estan implementando correctamente.

## Sección 2 (Un orden profesional de lectura)

¿Por qué conviene leer firma y docstring antes que el while principal?

Porque una cosa es lo que hace el código y otra muy diferente s lo que se supono que debería de hacer, leyendo los docstrings podemos ver que es lo que realmente debería de hacer, mientras que viendo el código unicamnete veremos lo que realmente hace.

## Sección 3 (Tipos como decisiones de diseño)

¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?

Que se puede generalizar un poco más la implementación de este código, ademas a la hora de importar las librerias se nos va a facilitar el trabajo de implementar las cosas en menos lineas de código.

## Sección 4 (Normalización y copia defensiva)

¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?

Los problemas principales que resuelve la función de normalizar grafo son las de ver que los vecinos esten conectados unos a otros de manera correcta y que cada peso en cada carretera por las que se conectes los vecinos tambien esten implementadas de manera correcta.

## Sección 5 (TypeError y ValueError cuentan historias distintas)

¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?

TypeError cuando la información no se implementa correctamente pero en cuestiones de strings y cosas por el estilo, mientras que el ValueError salta en cosas de valores, por poner un ejemplocuando hay algo negativo o no hay nada.

## Sección 6 (Bool, NaN e infinito)

¿Por qué True y NaN requieren comprobaciones específicas?

La respuesta la podemos ver muy claramente en un assert, que al ver que estas operaciones no son equivalentes con nada a la hora de comparar con otras cosas van a saltar errores cuando puede que no los haya, entonces hay que tener cuidado en esto.

## Sección 7 (Vecinos implícitos y representación total)

¿Qué fallo evita resultado.setdefault(vecino, [])?

Lo que evita principalmente es que sexistan vecinos que no tienen salidas o que no estan conectadas a nada, con esto podremos ver que los grafos esten bien echos y ya una vez que se hayan realizado de manera correcta ya podemos trabajar con ellos.

## Sección 8 (El contrato de dijkstra)

¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?

Poruqe en los diccionarios viene implicitamente los caminos que se agarraron, o sea de donde a donde va cada cosa con cuales costos etc...

## Sección 9 (Estado inicial y tablas totales)

¿Qué invariante establecen las comprensiones antes del while?

Los invariantes principales que tenemos dependen más que nada de donde comenzamos, ya que esto nos a dictaminar la manera en la que todo va a ser analizado.

## Sección 10 (El guard clause de entradas obsoletas)

¿Qué garantiza la comparación inmediatamente posterior a heappop?

esta muy interesante esto, por que lo que esta buscando antes de seguir avanzando en lo demas es que efectivamente el cambio se haya realizado y que la nueva heap no contenga el dato que acabamos de eliminar.

## Sección 11 (Relajación y actualización atómica)

¿Qué datos deben actualizarse juntos cuando una candidata mejora?

Se deben de actualizar tres cosas, la primera siendo la candidata en cuestiómn ya que esta ya no es la candidata obviamente, los predecesores eue aca la ya excandidate se les va a unir, porque obviamente ya no es una candidata y por ultimo actualizar el mismo heap.

## Sección 12 (Reconstruir es otro problema)

¿Qué diferencia hay entre destino inalcanzable y destino ausente?

Para el camino inalcanzable quiere decir que si hay un punto B al cual podemos llegar partiendo de A, pero que no existe un camino en medio de los dos para poder llegar a el, por otro lado el camino inexistente quiere decir que no existe este punto B para el cual llegar, por lo que aun que tengamos la carrretera no podriamos llegar.

## Sección 13 (Coordinación sin duplicación)

¿Qué responsabilidades delega camino_minimo?

Delega el echo de ver que el camino que estemos viendo si sea alcanzable y existente en primer lugar, como que esto lo da por valido sea así o no ylo delega a funciones secundarias para poder ver que sean tanto alcanzables como existentes.

## Sección 14 (Del contrato a una matriz de pruebas)

¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?

Al ver el costo finale stamos viendo que el resultado salga, pero no vamos a saber si la implementación se llevoa  cabo correctamente, entonces puede que haya casos en los que se dispare un error y no corra.

## Sección 15 (Auditoría de una implementación frágil)

¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?

el primer error que encuentro en la implementacion de este código es que no hay Mapping ni sequence para los grafos, esto puede tender a tener errores, el segundo es que en predecesores se piden dos variables en lugar de una, ya que pide str dos veces, y la tercera es que tanto distancias como actual se estan actualizando para tener el valor de la nueva heap pero ya sin los pendientes, y esto esta mal, no deberia de ser así.


    1. contrato incumplido:

        El código va a haber casos en los que te debuelve la respuesta correcta, pero habra otros en los que el código en cuestión ni va a correr, por lo que se incumple la implementación.
        
    2. entrada mínima reproducible:

        {"A" :("B", 0), "B": []}

    3. resultado observado:

        0

    5. prueba automatizada:

        {"A" :("B", 10)("C", 12)("D", 8), "B": ("C", 3)("D", 6)}

    6. cambio localizado:

        De: 

        distancia, actual = heapq.heappop(pendientes)

        A:

        ```python
        if candidata < distancias[vecino]:
        distancias[vecino] = candidata
        predecesores[vecino] = actual
        heapq.heappush(pendientes, (candidata, vecino))
        ```

## Sección 16 (Clínica de depuración)

¿Qué información mínima debe contener un reporte de fallo útil?

Debería de contener en que línea se produjo el fallo y que tipo de fallo es, así el programador podra ubucarlo facilmente y poder resolverlo de manera correcta. 


## Sección 17 (Revisión profesional de código)

¿Qué hace que un comentario de revisión sea accionable y verificable?

Lo que hace es que encuentra el problema, pero tambien encuentra lo que debería de hacer, o sea de nada sirve ver que esta mal si no se sabe de buenas a primeras que debería de tener bien.

## Sección 18 (Complejidad sin perder robustez)

¿La normalización cambia la complejidad asintótica de Dijkstra?

No la cambia perce, pero si realmente, ya que para el usuario si va a haber una mejora a la hora de comparar tiempos entre ambas funciones, entonces si se va a notar una complejidad menor.

## Sección 19 (Cuatro algoritmos, cuatro operaciones dominantes)

¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?

Al final el día todo lo que se presenta en estea tablita se sigue de una sola cosa, la cual es las colas que estan solitas se van a desprender de las pilas,lugo si bien todas funcionan de manera diferentes y ninguna es mejor o peor que la anterior, es claro que todo viene del mismo lugar.

## Sección 20 (Cierre)

¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?

La cadena de normalizar lo implementado, ya que una vez que se normaliza esto con la función prentada anteriormente en el notebook, podremos ver que se va a volver confiable, ya que no existiran caminos inalcanzables ni nada por el estilo.