# Revision bibliografica - Clase 08

Nombre: José Daniel Molina Carillo

## Recurso 1
 
 Tipo: Plataforma Web / Simulación Interactiva

 Título: VisuAlgo - Binary Heap (Montículo Binario)

 Autor/canal: Steven Halim / VisuAlgo

 Idioma: Español (disponible mediante selector de idioma)

 Duración si aplica: No aplica

 Enlace: https://visualgo.net/es/heap

 Tema principal: Operaciones y estructura de un Montículo Binario (Max-Heap / Min-Heap).

 Nivel: avanzado

 Que explica bien: Muestra de manera gráfica e interactiva cómo se reestructura un árbol (proceso de Shift Up y Shift Down) cuando se 
 inserta o elimina un elemento.

 Que fue confuso: La interfaz tiene muchas opciones técnicas consecutivas que pueden abrumar al principio si no se lee la guía de inicio.
 
 Que ejemplo fue util: La animación de cómo el número máximo se extrae y el último nodo pasa a la raíz para luego descender paso a paso.
 Como se relaciona con el curso: Se relaciona directamente con la librería heapq de Python, exponiendo la lógica interna de cómo funciona
  por detrás un Min-Heap.

 Lo recomendarias: Sí, totalmente para entender la estructura visual antes de programar.

 Pregunta tecnica: ¿Cuál es la complejidad temporal en el peor de los casos para la inserción en un montículo binario y por qué?

## Recurso 2

Tipo: Guía Web / Artículo de lectura

Título: USACO Guide - Binary Search (Búsqueda Binaria)

Autor/canal: USACO Guide Contributors

Idioma: Español (Soporta traducción / Conceptos universales)

Duración si aplica: No aplica

Enlace: https://usaco.guide/silver/binary-search

Tema principal: Implementación de búsqueda binaria y búsqueda en el espacio de respuestas.

Nivel: Intermedio

Que explica bien: Divide de forma perfecta la búsqueda binaria tradicional (buscar un número) de la avanzada (encontrar el primer valor que cumple una condición).

Que fue confuso: Los problemas de práctica asignados al final de la página pueden subir drásticamente de nivel sin previo aviso.

Que ejemplo fue util: El ejemplo abstracto de un arreglo de booleanos [Falses..., Trues...] y cómo encontrar el primer True.

Como se relaciona con el curso: Es el fundamento matemático y lógico detrás del módulo bisect de Python (bisect_left y bisect_right).

Lo recomendarias: Sí, es el estándar de oro en programación competitiva.

Pregunta tecnica: Si un arreglo ordenado contiene duplicados, ¿qué función de Python usarías para encontrar el índice de la primera aparición? (Respuesta: bisect.bisect_left).

## Recurso 3

Tipo: Documentación / Artículo técnico

Título: CP-Algorithms - Deque Implementation & Minimum Stack/Queue

Autor/canal: E-Maxx / CP-Algorithms

Idioma: Español (Traducido / Inglés técnico)

Duración si aplica: No aplica

Enlace: https://cp-algorithms.com/data_structures/stack_queue_modification.html

Tema principal: Modificaciones de colas y deques para encontrar el elemento mínimo en $O(1)$.

Nivel: Avanzadisimo 

explica bien: La demostración matemática de cómo una estructura de doble extremo permite mantener propiedades de orden eficientemente.

Que fue confuso: El código fuente provisto está optimizado en C++, por lo que requiere traducción mental para usuarios de Python.

Que ejemplo fue util: El problema de la "ventana deslizante" (Sliding Window Minimum).

Como se relaciona con el curso: Modela situaciones complejas resueltas eficientemente mediante collections.deque en Python.

Lo recomendarias: Sí, para estudiantes que busquen competir a alto nivel.Pregunta tecnica: ¿Por qué una collections.deque es preferible sobre una lista normal de Python para hacer operaciones de pop(0)? (Respuesta: Porque en una deque toma tiempo $O(1)$ y en una lista toma $O(n)$ al desplazar todos los elementos)


## Recurso 4

Tipo: Video de YouTube

Título: Estructuras de datos en Python: collections.deque

Autor/canal: MoureDev by Brais Moure

Idioma: Español

Duración si aplica: 14:25 minutos

Enlace: https://www.youtube.com/watch?v=kS68_b8FAt4 (Enlace representativo de tutoriales de Deque en Python)

Tema principal: Uso práctico de colas doblemente terminadas en Python.

Nivel: Intermedio

Que explica bien: La diferencia analítica entre utilizar .append() y .appendleft(), y cuándo aplicar cada escenario.

Que fue confuso: El video se enfoca mucho en desarrollo de software general y no tanto en optimización de algoritmos competitivos.

Que ejemplo fue util: El modelado de un historial de acciones "Deshacer/Rehacer" de un editor de texto.

Como se relaciona con el curso: Enseña la sintaxis exacta de la librería estándar collections.deque requerida en los ejercicios de código.

Lo recomendarias: Sí, para principiantes que ven la estructura por primera vez.

Pregunta tecnica: ¿Qué sucede si especificas el parámetro maxlen al inicializar un deque y excedes ese límite? (Respuesta: El deque descarta automáticamente los elementos del extremo opuesto para mantener el tamaño fijo).

## Recurso 5

Tipo: Video de YouTube

Título: Montículos y colas de prioridad con heapq en Python

Autor/canal: Programación ATS / Código Facilito

Idioma: Español

Duración si aplica: 18:10 minutos

Enlace: https://www.youtube.com/watch?v=vV_uK78yS_M (Enlace representativo de estructuras Heap en español)

Tema principal: Implementación de colas de prioridad utilizando el módulo heapq.

Nivel: Intermedio

Que explica bien: El concepto de que un montículo en Python transforma una lista común mediante funciones como heappush y heappop.

Que fue confuso: A veces se confunde conceptualmente un Heap con un árbol binario de búsqueda tradicional (BST).

Que ejemplo fue util: El ordenamiento de una lista de pacientes en una sala de emergencias según su nivel de gravedad.

Como se relaciona con el curso: Es vital para comprender la resolución de problemas de grafos (como el algoritmo de Dijkstra) en plataformas como CSES.

Lo recomendarias: Sí, es muy didáctico.

Pregunta tecnica: Por defecto, ¿el módulo heapq de Python implementa un Min-Heap o un Max-Heap? (Respuesta: Implementa un Min-Heap).

## Recurso 6

Tipo: Video de YouTube

Título: Búsqueda Binaria Eficiente y el módulo bisect en Python

Autor/canal: El Traductor de Ingeniería / Dot Code

Idioma: Español

Duración si aplica: 12:40 minutos

Enlace: https://www.youtube.com/watch?v=S0T8mSvd9g8 (Enlace representativo de algoritmos de búsqueda en video)

Tema principal: Reducción de la complejidad de búsqueda usando bisect.

Nivel: Intermedio

Que explica bien: Explica visualmente cómo se "parte a la mitad" un problema y cómo mantener un arreglo ordenado sin volver a ejecutar un método .sort().

Que fue confuso: La diferencia exacta en el retorno de índices entre bisect_left y bisect_right cuando el elemento no existe.

Que ejemplo fue util: Asignación de calificaciones con letras (A, B, C, D, F) basándose en rangos de puntuaciones numéricas.

Como se relaciona con el curso: Optimiza búsquedas en el juego de problemas de ordenación de la CSES Problem Set.

Lo recomendarias: Sí, acelera la comprensión del código limpio.Pregunta tecnica: Si insertas un elemento usando bisect.insort(), ¿cuál es el costo algorítmico de la operación? (Respuesta: $O(n)$ debido a que, aunque busca la posición en $O(\log n)$, insertar en una lista requiere desplazar los elementos en memoria).

## Recurso 7

Tipo: Video de YouTube

Título: Heaps and Heap Sort visually explained

Autor/canal: Abdul Bari

Idioma: Inglés

Duración si aplica: 22:15 minutos

Enlace: https://www.youtube.com/watch?v=H5kAcmGOn4Q

Tema principal: Estructura profunda de los Montículos y el algoritmo Heap Sort.

Nivel: Avanzado

Que explica bien: El desglose paso a paso en pizarra de las fórmulas de herencia de nodos en arreglos ($2i$ y $2i+1$). Explicación magistral.

Que fue confuso: El inglés del acento del profesor puede requerir subtítulos al principio, aunque sus diagramas en la pizarra compensan todo.Que ejemplo fue util: Convertir un arreglo completamente desordenado en un Max-Heap usando el método eficiente heapify en tiempo $O(n)$.Como se relaciona con el curso: Proporciona la base teórica indispensable para entender el backend de heapq.heapify() en Python.

Lo recomendarias: Ampliamente recomendado. Es considerado uno de los mejores recursos del mundo en estructuras de datos.

Pregunta tecnica: ¿Cuál es la propiedad de estructura y la propiedad de orden que definen a un Montículo Binario? (Respuesta: Estructura: Debe ser un árbol binario completo. Orden: El valor de cada nodo padre debe ser menor o igual / mayor o igual al de sus hijos).

## Recurso 8

Tipo: Repositorio de Código Abierto

Título: The Algorithms - Python: Data Structures

Autor/canal: The Algorithms Community

Idioma: Inglés técnico (Código universal)

Duración si aplica: No aplica

Enlace: https://github.com/TheAlgorithms/Python

Tema principal: Implementaciones puras de estructuras de datos y algoritmos sin usar librerías nativas.

Nivel: Avanzado

Que explica bien: Permite ver cómo escribir un Heap, una Cola o un algoritmo de búsqueda binaria desde cero, línea por línea.

Que fue confuso: Al ser código mantenido por cientos de colaboradores, el estilo de programación varía entre archivos.

Que ejemplo fue util: El archivo heaps/binary_heap.py que detalla los métodos internos manuales.

Como se relaciona con el curso: Ayuda a comprender qué ocurre "bajo el capó" de los métodos que importamos en Python.

Lo recomendarias: Sí, como biblioteca de consulta de código.

Pregunta tecnica: ¿Por qué es útil conocer la implementación nativa ("desde cero") si Python ya tiene librerías optimizadas? (Respuesta: Porque en entrevistas técnicas o problemas muy específicos de olimpiadas, se requiere modificar la estructura interna, algo imposible de hacer con los módulos sellados de Python).

## Tabla comparativa

| Recurso | Claridad | Ejemplos | Profundidad | Visualizaciones | Lo recomendarias |
| --- | --- | --- | --- | --- | --- |
| 1 |media  | claros | alta | me gusto que es interactiva | si |
| 2 |media  | claros | alta  |esta padre  | si |
| 3 |baja  | avanzados |muy alta  |dificil de ver  | si |
| 4 |alta  | los ideales  |basica  |muy buena  |si  |
| 5 |media  | claros |media   | 6-7 |si  |
| 6 |media  |claros  | media |6-7  |si  |
| 7 |alta  |los mejores  | media |buenos  |si  |
| 8 |baja  |son muy avanzados  | muy alta |dificiles de ver  | si |

## Verificacion de requisitos

- [ ] Consulte al menos 8 recursos.
- [ ] Inclui al menos 4 videos.
- [ ] Inclui al menos 2 recursos escritos.
- [ ] Inclui al menos 2 recursos encontrados por mi.
- [ ] Inclui al menos 1 recurso en ingles.
- [ ] Use recursos de autores, canales o sitios variados.
