# Arturo Prudencio Bonilla

## pregunta inicial

¿Cómo conectamos todos los nodos con el menor costo total sin crear ciclos?

## seccion 1

¿Qué producto final esperamos obtener hoy y en qué se diferencia de un camino desde un origen?


Esperamos obtener un "árbol de expansión mínima" (MST), que es un subconjunto de carreteras que conecta absolutamente todas las ciudades de la red con el costo total más bajo posible. Se diferencia de los caminos mínimos (como los de Dijkstra) en que no optimizamos la distancia de un nodo origen hacia los demás, sino el costo global de mantener unida toda la infraestructura

## seccion 2

¿Qué operación dominante distingue a Kruskal de BFS, 0-1 BFS y Dijkstra?


La operación dominante que ejecutamos una y otra vez en Kruskal es preguntarnos: "¿Estos dos extremos ya pertenecen a la misma componente?". A diferencia de usar colas o heaps para extraer el nodo más cercano, aquí necesitamos una estructura (Union-Find) especializada en fusionar conjuntos y verificar conectividad rápidamente

## seccion 3

¿Por qué no basta aceptar automáticamente todas las carreteras en orden creciente de costo?


Porque una carretera muy barata se vuelve inútil y redundante si las dos ciudades que conecta ya tienen un camino trazado entre ellas gracias a otras carreteras previamente seleccionadas o eso entiendo por el modelo


## seccion 4

¿Qué optimiza cada algoritmo y cuál de ellos necesita un origen?


Dijkstra necesita un origen porque su objetivo es optimizar y garantizar la distancia más corta desde ese punto de partida


Kruskal no tiene un nodo de origen; optimiza la suma total de los pesos de la red completa para garantizar que todos los nodos queden conectados de la forma más barata


## seccion 5

¿Por qué un árbol de expansión conectado con V vértices tiene exactamente V−1 aristas?


Porque construimos la red de forma incremental: empezamos con $V$ componentes separadas y cada arista válida une dos componentes, reduciendo el total en uno


## seccion 6

¿Qué información mínima necesitamos antes de aceptar una arista u–v?


Necesitamos saber si $u$ y $v$ ya están conectados


## seccion 7

¿Qué cambia en la partición cuando aceptamos una arista entre componentes distintas?


Las dos componentes distintas se fusionan en un solo conjunto disjunto


## seccion 8

¿Por qué conviene que union(a, b) devuelva un booleano?


Porque centraliza la decisión y la actualización en un solo paso. Un retorno True indica que los nodos estaban separados y la unión fue efectiva (aceptamos la arista), mientras que un False indica que ya estaban conectados, permitiendo al algoritmo rechazar la arista inmediatamente por formar un ciclo


## seccion 9 

¿Qué condición permite reconocer una raíz en el arreglo padre?


En la representación interna mediante un arreglo de índices, reconocemos una raíz cuando el nodo se apunta a sí mismo, es decir, cuando padre[elemento] == elemento


## seccion 10

¿Por qué debemos validar explícitamente los índices negativos?


el contrato matemático de Union-Find no lo concibe. Consultar find(-1) debe arrojar un IndexError para evitar fallos lógicos ocultos donde accidentalmente consultemos el representante de otro nodo distinto

## seccion 11

¿Qué error aparece si union enlaza nodos arbitrarios sin encontrar primero sus raíces?


Si enlazamos $a$ y $b$ directamente, podríamos estar uniendo nodos que están a mitad de una cadena, lo cual rompe la representación de las componentes y crea árboles fracturados


## seccion 12
¿Qué invariantes viola padre = [1, 0, 2]?


Viola dos invariantes críticos: "toda cadena termina en una raíz" y "no existen ciclos salvo el lazo raíz→raíz"


## seccion 13
¿Qué cambia y qué permanece igual durante la compresión de caminos?


Lo que cambia es la representación interna de la estructura: el árbol se vuelve mucho más plano porque todos los nodos visitados pasan a apuntar directamente a la raíz, ahorrando tiempo en consultas futuras


## seccion 14
¿Por qué colocar el árbol pequeño debajo del grande limita el crecimiento de altura?


Al colgar el árbol con menos elementos bajo la raíz del más poblado, la mayoría de los nodos conserva su distancia a la raíz, evitando cadenas largas que volverían lenta a la función find


## seccion 15
¿Qué devuelve union(0, 3) después de unir las componentes {0,1} y {2,3}?


Devolverá True. Aunque los nodos ya forman grupos, el grupo de 0 y el grupo de 3 son componentes completamente distintas

## seccion 16
¿Cómo usa Kruskal el booleano devuelto por union?


Lo usa como filtro condicional: si union(u, v) es True, Kruskal acepta la arista, suma su peso al costo total y avanza el contador de aristas seleccionadas; si es False, simplemente ignora la arista y continúa con la siguiente

## seccion 17 
¿Cuál es el costo final del ejemplo conductor y por qué se detiene después de cuatro aristas?


El costo final acumulado de las aristas seleccionadas (C–D:1, A–C:2, D–E:2 y B–D:3) es 8. El algoritmo se detiene tras procesar exactamente 4 aristas porque el grafo tiene 5 vértices, y sabemos matemáticamente que un árbol conectado requiere $V-1$ aristas, por lo que revisar el resto de las carreteras ordenadas sería trabajo redundante

## seccion 18
¿Qué condición permite distinguir un MST completo de un bosque desconectado?


La condición de parada

## seccion 19
¿Por qué un test con pesos empatados no debe exigir siempre una lista exacta de aristas?


Porque ante carreteras que cuestan exactamente lo mismo, Kruskal puede producir múltiples árboles de expansión válidos dependiendo del orden interno del algoritmo de ordenamiento

## seccion 20
¿Qué parte domina la complejidad total de Kruskal?


La etapa de ordenar las aristas por peso al inicio del algoritmo es la que domina la complejidad

## seccion 21 
¿Qué dos adaptaciones separan el formato de CSES de nuestra función reutilizable?


1. CSES indexa las ciudades del 1 al $n$, mientras que nuestra implementación matemática usa arreglos indexados en cero (del 0 al $n-1$), por lo que hay que restar 1 al leer
2. CSES requiere que el programa imprima la cadena "IMPOSSIBLE" si el grafo está desconectado, mientras que nuestra función señala este fallo devolviendo None


## seccion 22
¿Qué cambia entre Redundant Connection y Kruskal aunque ambos usen Union-Find?


Kruskal necesita obligatoriamente ordenar todas las aristas de menor a mayor costo antes de procesarlas para asegurar que minimiza la suma. En Redundant Connection, el ordenamiento no es necesario

## seccion 23
¿Qué responsabilidades deben estar probadas antes de integrar Union-Find dentro de Kruskal?


Debemos probar exhaustivamente la estructura subyacente de forma aislada: la validación de índices y tipos, la correcta inicialización de padres y tamaños, que find respete la compresión de caminos, y que union mantenga el conteo de componentes y aplique correctamente la regla del tamaño

## seccion 24
¿Qué invariante protege una prueba de unión repetida?


Protege el invariante que estipula que una unión redundante "no cambia nada". Si llamamos a union sobre dos nodos que ya pertenecen a la misma componente, el método debe devolver False y, si o si, el contador interno de raíces (número de componentes) debe permanecer idéntico


## seccion 25
¿Qué estructura se necesitaría para procesar tareas cuando unas dependen de otras?


Se necesita combinar el conteo de dependencias (grados de entrada) con una cola