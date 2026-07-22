# Revision bibliografica - Clase 08

Nombre: José Iván Reyna Blanco

## Recurso 1

- Tipo: Video
- Titulo: 1.5.1 Time Complexity #1
- Autor/canal: Abdul Bari
- Idioma: Inglés
- Duracion si aplica: 09:44
- Enlace: https://www.youtube.com/watch?v=9TlHvipP5yA&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=6Tema
- Tema principal:  Análisis de Complejidad Temporal (Time Complexity) y cálculo de la notación Big O
- Nivel: Intermedio
- Que explica bien: Cómo cambian las variables en cada iteración para convertir "el coste" de la ejecución del ciclo en una regla matemática.
- Que fue confuso: Que al inicio se toma muy poco tiempo para definir la complejidad y justificar el costo de cada operación.
- Que ejemplo fue util: El último ejemplo donde el bucle depende de una variable acumulativa P <= N (donde P = P + i), deduce padre por qué su complejidad es O(sqrt(n))
- Como se relaciona con el curso: En todo, es importante considerar la complejidad de cualquier algortimo para ver si su eficiencia nos conviene. 
- Lo recomendarias: Sí.
- Pregunta tecnica:  ¿Cómo se demuestra matemáticamente que un bucle anidado, cuyo límite interior depende del valor del iterador exterior (ej. j < i), resulta en una complejidad de O(n^2) y no de O(n)

## Recurso 2

- Tipo: Video
- Titulo: 1.11 Best Worst and Average Case Analysis
- Autor/canal: Abdul Bari
- Idioma: Inglés
- Duracion si aplica: 18:56
- Enlace: https://www.youtube.com/watch?v=lj3E24nnPjI&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=16
- Tema principal: Análisis del Mejor, Peor y Caso Promedio (Best, Worst, Average Case) de los algoritmos y la desmitificación sobre cómo se aplican las notaciones asintóticas (Big O, Omega, Theta) a dichos casos
- Nivel: Intermedio
- Que explica bien: La clarificación crucial [10:43] de que cualquier caso (mejor, peor o promedio) puede ser expresado utilizando cualquier notación asintótica (Big O, Omega o Theta). La gente suele confundir incorrectamente "Peor caso = Big O" o "Mejor caso = Omega", y el instructor explica muy bien por qué eso es un error conceptual, ya que las notaciones describen el crecimiento matemático de una función, no la situación del caso
- Que fue confuso:La parte donde habla del análisis del caso promedio del arreglo lineal
- Que ejemplo fue util: La comparación entre un Árbol Binario de Búsqueda (BST) balanceado [12:00] y uno "sesgado" (skewed) 
- Como se relaciona con el curso: Es conocimiento indispensable para una clase universitaria de estructuras de datos. En Python, al usar listas, diccionarios o implementar árboles personalizados, un estudiante debe entender que decir "el tiempo es Big O" no significa "es el peor caso".
- Lo recomendarias: Sí, está padre conocer nueva notación de complejidad
- Pregunta tecnica: ¿Cómo justificarías matemáticamente que el tiempo del mejor caso de búsqueda lineal (donde la función de costo siempre es 1) puede expresarse de manera correcta tanto en O(1), Omega(1), como Theta(1)?

## Recurso 3

- Tipo: Video
- Titulo: Dynamic and Static Arrays
- Autor/canal:  William Fiset
- Idioma: Inglés
- Duracion si aplica: 11:52
- Enlace: https://www.youtube.com/watch?v=PEnFFiQe1pM&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=4Tema
- Tema principal: Fundamentos de los arreglos (arrays) estáticos y dinámicos, sus operaciones comunes, y análisis de complejidad espacial/temporal
- Nivel: Básico
- Que explica bien: Cómo funciona la mecánica interna de un arreglo dinámico [09:50]. Explica paso a paso que internamente de un arreglo dinámico hay un arreglo estático, y muestra visualmente cómo este duplica su capacidad e invierte tiempo copiando los datos cada vez que se queda sin espacio disponible.
- Que fue confuso: La parte donde explica por qué mover un elemento a la derecha y redimensionar son operaciones de complejidades distintas. 
- Que ejemplo fue util: EL recordatorio sobre el comienzo de los índices porque cambia la forma natural de hacerlo.
- Como se relaciona con el curso: Las listas (lists) de Python, que usamos a diario en programación, son precisamente arreglos dinámicos subyacentes. Entender la diferencia entre un arreglo estático y uno dinámico explica por qué a veces añadir a una lista de Python (.append()) toma O(1), pero en ciertos momentos requiere un tiempo O(n) bajo el capó para redimensionarse
- Lo recomendarias: Sí
- Pregunta tecnica:  Basado en el video, si hacer append() en un arreglo dinámico provoca a veces re-dimensionamiento en tiempo O(n), ¿por qué matemáticamente se considera que la complejidad temporal de append() es O(1) (tiempo constante amortizado)?

## Recurso 4

- Tipo: Video
- Titulo: Linked Lists Introduction
- Autor/canal: William Fiset
- Idioma: Inglés
- Duracion si aplica: 14:43
- Enlace: https://www.youtube.com/watch?v=-Yn5DU0_-lw&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=6Tema
- Tema principal: Introducción a las listas enlazadas simples (singly) y dobles (doubly), incluyendo terminología, pros y contras, y cómo insertar o eliminar nodos
- Nivel: Básico/medio
- Que explica bien: La forma adecuada de insertar y borrar elementos sin modificar el orden/funcionamiento de la estructura.
- Que fue confuso: La parte sobre cómo remover nodos en una lista enlazada simple [08:47]
- Que ejemplo fue util: La explicación sobre la complejidad de remover un nodo desde la "cola" (tail) [13:28]. Señala muy bien que, en una lista simple, aunque tengas la referencia directa al tail, al borrarlo no puedes saber quién era el nodo anterior para asignarlo como el nuevo tail, lo que fuerza a que la eliminación en la cola sea $O(n)$ en listas simples, mientras que es O(1) en listas dobles.
- Como se relaciona con el curso: Creo que es la base de un deque en general.
- Lo recomendarias: Sí, en especial por el apoyo visual que provee para entender el reacomodo
- Pregunta tecnica: ¿Que utilidad tiene esto respecto a usar matrices?

## Recurso 5

- Tipo: Página Web de documentación
- Titulo: collections — Container datatypes
- Autor/canal: Python Software Foundation
- Idioma: Inglés
- Duracion si aplica: Nel
- Enlace: https://docs.python.org/3/library/collections.html
- Tema principal: Deque
- Nivel: Básico
- Que explica bien: El propósito de origen y las operaciones del deque.
- Que fue confuso: Aún después de leerlo sigo sin entender intuitivamente bien lo de que es una doble lista. Creo que es confuso decirlo así, basta con explicar que permite hablar de "izquierda" o "derecha" de un elemento sin redimensionar la estructura como en arreglos dinámicos ordinarios.
- Que ejemplo fue util: El de por qué pop(0) o insert(0, v) disparan la complejidad. También que mencione que se pueden usar pesos y lo que ocurre. 
- Como se relaciona con el curso: Los deques son estructuras muy importantes y generalizan a las pilas.
- Lo recomendarias: Más o menos, creo que un video es más intuitivo pero esto es más corto.
- Pregunta tecnica: ¿Por qué un deque se ve por dentro para python como una lista doble?

## Recurso 6

- Tipo: Página web (Documentación oficial)
- Titulo: heapq — Heap queue algorithm
- Autor/canal: Python Software Foundation
- Idioma: Inglés 
- Duracion si aplica: Nel
- Enlace: https://docs.python.org/3/library/heapq.html
- Tema principal: Uso de heaps que son como colas de prioridad
- Nivel: Medio/alto
- Que explica bien: Las funciones rápidas como nlargest y nsmallest. Te explica de forma muy clara que si tienes miles de datos y solo quieres obtener los 3 más grandes o los 5 más pequeños, es mucho más rápido usar estas herramientas en lugar de ordenar toda la lista completa.
- Que fue confuso: Python decide por defecto que el elemento hasta arriba siempre sea el más pequeño (conocido como min-heap). La parte donde explican cómo hacer lo contrario (un max-heap donde el más grande esté arriba) multiplicando los números por -1 o modificando las clases se siente como un"parche" confuso.
- Que ejemplo fue util: La sección al final llamada "Priority Queue Implementation Notes" . Muestra un ejemplo excelente de cómo hacer un sistema de tareas donde asignas un "nivel de prioridad" a cada tarea, asegurando que las más urgentes se atiendan primero.
- Como se relaciona con el curso: Con como trabajar con grafos/problemas que requieran asignar pesos o importancias.
- Lo recomendarias: Sí, es una herramienta útil y el artículo es conciso
- Pregunta tecnica: ¿Cuál es el método más parecido a .peek() de una pila pero para ver el elemento más pequeño sin modificarlo?

## Recurso 7

- Tipo: Video
- Titulo: Graph Theory Algorithms (Introducción)
- Autor/canal: WilliamFiset
- Idioma: Inglés
- Duracion si aplica: 3:11
- Enlace: https://www.youtube.com/watch?v=DgXR2OWQnLc
- Tema principal: Una introducción visual a qué son los grafos, los tipos que existen (dirigidos, no dirigidos, con peso) y cómo se usan para representar redes del mundo real.
- Nivel: Básico a Intermedio.
- Que explica bien: Las animaciones. Hace un trabajo excelente mostrando cómo un dibujo de un grafo con círculos y líneas se puede traducir a una tabla (matriz) o a una lista en la memoria de la computadora.
- Que fue confuso: Al ser un video corto e introductorio, menciona muchos nombres de algoritmos avanzados de golpe al final sin explicarlos y me abrumó.
- Que ejemplo fue util: Las analogías del mundo real. Muestra cómo los grafos no son solo matemáticas abstractas, sino que son exactamente la forma en la que se modelan mapas de metro, redes sociales de amigos o las carpetas de tu computadora.
- Como se relaciona con el curso: Sirve para entender el "por qué" antes del "cómo". En clase vamos a usar grafos (como en la siguiente práctica), y este video te da la imagen mental perfecta de lo que tu código realmente está construyendo.
Lo recomendarias: Totalmente. Es uno de los mejores videos para entender los grafos visualmente antes de tocar una sola línea de código.
- Pregunta tecnica: El video menciona dos formas de guardar un grafo: Matriz de Adyacencia (tabla) y Lista de Adyacencia. Ejemplifica un uso correcto de cada uno. 
## Recurso 8

- Tipo:
- Titulo:
- Autor/canal:
- Idioma:
- Duracion si aplica:
- Enlace:
- Tema principal:
- Nivel:
- Que explica bien:
- Que fue confuso:
- Que ejemplo fue util:
- Como se relaciona con el curso:
- Lo recomendarias:
- Pregunta tecnica:

- Tipo: Ensayo / Artículo Oficial
- Titulo: Python Patterns - Implementing Graphs
- Autor/canal: Guido van Rossum (creador de Python)
- Idioma: Inglés
- Duracion si aplica: Nel
- Enlace: https://www.python.org/doc/essays/graphs/
- Tema principal: Cómo construir y navegar por un grafo en Python utilizando únicamente las herramientas básicas que ya trae el lenguaje (diccionarios y listas), sin instalar librerías externas.
- Nivel: Intermedio.
- Que explica bien: Cómo usar un diccionario normal para armar el grafo. Explica que las "llaves" del diccionario son los puntos del grafo (nodos) y los "valores" son listas que guardan los vecinos conectados a ese punto.
- Que fue confuso: El texto original es de 1998. Aunque la lógica es perfecta, algunas pequeñas partes de cómo está escrito el código (la sintaxis) se ven un poco antiguas comparadas con el Python moderno que usamos hoy en clase.
- Que ejemplo fue util: La función find_path(). Muestra paso a pasito cómo el código salta de un nodo a otro buscando un destino, y cómo guarda un registro de los lugares que ya visitó para no quedarse dando vueltas en círculos.
- Como se relaciona con el curso: Es la aplicación práctica por excelencia.
- Lo recomendarias: Sí, se ve que es un recurso clásico. Es muy inspirador leer y entender un código escrito de forma tan simple por el mismísimo creador del lenguaje.
- Pregunta tecnica: Cuando se busca un camino entre dos puntos, se utiliza una lista llamada path para recordar los nodos ya visitados. ¿Qué pasaría con el programa si olvidamos hacer esa comprobación (el if node not in path) en un grafo que tiene rutas circulares (ciclos)?
## Tabla comparativa

| Recurso | Claridad | Ejemplos | Profundidad | Visualizaciones | Lo recomendarias |
| --- | --- | --- | --- | --- | --- |
| 1 | Alta en el paso a paso de las variables | For acumulativo (p=p+i) | Intermedia, ideal para entender la notación O(n) | Pocas, solo son palabras en pizarrón | Sí |
| 2 | Alta al aclarar mitos de las notaciones | La búsqueda lineal y cómo el "peor caso" en árboles cambia si el árbol está chueco o equilibrado | Intermedio. Clave para aprender a evaluar un código sin caer en los errores comunes de conceptos. | Media. Diagramas de árboles y listas dibujadas en pizarra para apoyar la teoría. | Sói |
| 3 | Regular, pero alta al mostrar cómo se duplica la memoria, aunque mezcla un poco el mover datos con redimensionar  | Recordatorio con índices | Intermedia | Excelente, animaciones claras y modernas | Sí |
| 4 | Alta en el movimiento de las conexiones, aunque el truco de usar dos flechas para borrar puede ser enredado. | La demostración de por qué borrar al final de una lista simple es lento, pero en una lista doble es instantáneo. | Básico. Te ayuda a entender por qué existen estructuras alternativas a los arreglos tradicionales. | Excelente. Animaciones en pantalla que muestran de forma muy viva cómo se conectan y desconectan los datos. | Sí |
| 5 | Regular. Los resúmenes iniciales son directos, pero el texto se vuelve seco y muy técnico en los detalles profundos. | El uso de Counter para contar palabras repetidas en un texto largo con solo un par de líneas de código | Básico/Intermedio. Te muestra las herramientas reales y ultra optimizadas que Python ya tiene listas para ti. | Ninguna. Es un manual de texto puro con ejemplos de código. | Sí |
| 6 | Regular. Muy claro para buscar los datos más grandes o chicos, pero confuso al explicar cómo invertir la prioridad. | La guía práctica para armar una fila de tareas donde las más urgentes se atienden primero automáticamente. | Intermedio. Conecta los árboles binarios de la teoría con su uso práctico del día a día en Python. | Ninguna (por las mismas razones que arriba) | Sí |
| 7 | Alta al definir qué es una red, pero abruma un poco al soltar muchos nombres de algoritmos difíciles al final. | Casos del mundo real como mapas de transporte, redes de amigos en internet o las carpetas de tu PC. | Básico. Te guarda la imagen mental de la estructura antes de que te metas a escribir código de verdad | Excelente. Gráficos animados muy claros que muestran cómo las redes se convierten en tablas de datos | Sí. Excelente para entender para qué sirven los grafos antes de programarlos |
| 8 | Alta. Explica de forma muy limpia cómo usar diccionarios y listas básicas para representar redes complejas. | La función find_path(), que te enseña a saltar de un punto a otro sin quedarte atrapado dando vueltas en círculos. | Intermedio. Muestra lógica avanzada con código simple, aunque la sintaxis se siente un poco antigua (1998). | Ninguna. Es un artículo de lectura en texto plano con bloques de código de ejemplo. | Sí |



## Verificacion de requisitos

- [ ] Consulte al menos 8 recursos.
- [ ] Inclui al menos 4 videos.
- [ ] Inclui al menos 2 recursos escritos.
- [ ] Inclui al menos 2 recursos encontrados por mi.
- [ ] Inclui al menos 1 recurso en ingles.
- [ ] Use recursos de autores, canales o sitios variados.
