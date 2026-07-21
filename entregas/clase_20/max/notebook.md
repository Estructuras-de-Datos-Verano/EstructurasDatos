# Notebook Clase 20  Max

## Sección 0 (Preguntal Inicial)

¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?

La manera en que la identificamos es viendo que necesita resolver el problema en primer lugar, luego, podemos elegir el algoritmo correspondiente y resolverlo

## Sección 1 (Recuperación: primero aparecen las estructuras)

¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?

Las pilas, si bien todo hacen cosas diferentes, en el fondo son el mismo tipo de estructuras

## Sección 2 (Del enunciado de una decisión)

¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?

Porque si lo hacemos no estamos analizando el problema, y si no lo analizamos vamos a poder agarrar una ruta alterna que no nos conviene

## Sección 3 (Identificar el objetivo)

¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?

Que el orden topologico no respeta orden de buenas a primeras mientras que el MST si lo hace.

## Sección 4 (Dirección y significado de las aristas)

¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?

Podemos tener problemas de dirreción en el cual una aristq eus e supone que no deberia ir en ese orden lo termine haciendo.

## Sección 5 (Clasificar el dominio en pesos)

¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?

Porque nos falta bastante más información como si es que el peso es negativo, o si pesa bastante más y cosas por el estilo.

## Sección 6 (Matriz de decisión integradora)

¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?

La que explica mejor es la Operacióndominante porque en esa sección, es donde mejor se explica que hace cada cosa.

## Sección 7 (Laboratorio de decisión interactivo)

¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?

Lo que siento que deberiamos de predecir es que si va a pasar las pruebas, yua que de si hacerlo quiere decir que la implementación es correcta.

## Sección 8 (Caso de camino sin pesos: BFS)

¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?

El invariante que nos permite conocerlo es el de la manera en la que estan conectados los nodos.

## Sección 9 (Caso de pesos 0/1 : 0-1 BFS)

¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?

Porque de esta manera podemos tener un orden de las cosas, y así de cierta manera podemos llegar a ignorar que sea como una forma de corlas la cola.

## Sección 10 (Caso de pesos generales: Dijkstra)

¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?

La operación de ir recorriendo los diferentes caminos varias veces.

## Sección 11 (BFS, 0-1 BFS y Dijkstra no forman una competencia)

¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?

En el sentido que puede llegar a ser ineficiente  la hora de ahorrar recursos para buscar la información necesaria.

## Sección 12 (Pesos negativos: rechazar con precisión)

¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?

La justificamos diciendo que las normas iniciales de la implementación se violaron, o sea para que a sabiendas el usuario sepa que puede ser incorrecto.

## Sección 13 (Conexión global: Kruskal y Union-Find)

¿Qué consulta repetida de Kruskal justifica usar Union-Find?

La consulta repetitiva de no tener que cerrer las opciones diponibles para así poder repasarlas o volverlas a analizar.

## Sección 14 (Árbol de caminos mínimos no es MST)

¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?

Por que de hacerlo podemos tener muchos problemas y resultados erroneos.

## Sección 15 (Dependencias: Kahn y grados de entrada)

¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?

Quiere decir que ya entro a la cola, entonces el grado 0 no es más que un indicador.

## Sección 16 (BFS y Kahn comparten cola, no invariante)

¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?

El grado de ejecución de cada nodo respectivamente, luego el objeto a analizar para ver si es valido o no lo es.

## Sección 17 (Contratos antes de ejecutar)

¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?

Las de encontrar el camino correcto al menor costo posible y llevar en cuenta el camino que se recorrio.

## Sección 18 (Reutilización en lugar de recopia)

¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?

Porque aquí se pueden generar varios errores, como el que la función se corra dos veces o que la función no trague exactamente lo mismo, entonces a la hora de copiar y pegar no vaya a funcionar y cosas por el estilo.

## Sección 19 (Diseñar pruebas que distinguen decisiones)

¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?

El que sea como de forma general, o sea que si bien se hace con numeros y letras, diseñar la prueba de forma que si camnbiamos estos números y letras el resultado siga arrojando lo que debe de ser de manera correcta.

## Sección 20 (Clínica de selecciones incorrectas)

Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.

3. “Usaré Kahn porque hay una cola”, pero se pide la ruta con menos saltos.

Corrección: Usaré Kahn porque hay una cola

5. “Usaré Dijkstra aunque existe una arista −3”.

Corrección: Usaré Dijkstra cuando no exista una arista −3

## Sección 21 (Trabajo en equipo A: movilidad urbana)

¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?

Lo que cambia es que la primera va a ser Dijkstra, la segunda va a ser de Kruskal y la tercera sera topologicos

## Sección 22 (Trabajo en equipo B: construir y planificar)

¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?

Por que dependiendo del algoritmo vamos a tener resultados completamente diferentes.

## Sección 23 (Comunicación técnica de una decisión)

¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?

Debe de conteer cual es el error, cual es el tipo de rror, donde es que se encuentra el error, o sea que función y cosas por el estilo, y por ultimo debe e contener una posible solución o una recomendacion de la misma.

## Sección 24 (Reflexión final del curso)

¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?

Lo que cambio principalmente fue elenfoque que le di a la manera en la que podemos analizar los problemas para poder implementar el algoritmo correcto para la solución indicada por el problema original.

## Sección 25 (Síntesis y cierre)

Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?

Lo podremos ver casi casi que de manera jerarquija para así poder adecuar el logaritmo indicado.