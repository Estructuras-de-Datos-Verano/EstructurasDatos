# Revisión bibliográfica - Clase 08

Nombre: [Tu Nombre]

## Recurso 1
- Tipo: Video
- Título: Daily Temperatures - Leetcode 739 - Python
- Autor/canal: NeetCode
- Idioma: Inglés
- Duración si aplica: 14:14
- Enlace: https://www.youtube.com/watch?v=cTBiBSnjO3c
- Tema principal: Uso del patrón "Pila Monótona" (Monotonic Stack) para encontrar el siguiente valor mayor/menor.
- Nivel: Intermedio
- Qué explica bien: El paso de una solución de fuerza bruta O(n^2) a una óptima O(n), mostrando paso a paso cómo los elementos "inútiles" son poppeados de la pila.
- Qué fue confuso: Pasa rápido por la demostración analítica de por qué la complejidad temporal es exactamente O(n). 
- Qué ejemplo fue útil: La analogía gráfica de las temperaturas y cómo un día más cálido invalida a los días anteriores más fríos.
- Cómo se relaciona con el curso: Es lo que vimos en la práctica del problema Nearest Smaller Values.
- Lo recomendarías: Sí, NeetCode es directo y usa el lenguaje Python .
- Pregunta técnica: ¿Cómo adaptaríamos esta estructura si necesitáramos el segundo valor menor más cercano en lugar del primero?

## Recurso 2
- Tipo: Video
- Título: 1. Time Complexity Analysis in Data Structures
- Autor/canal: Abdul Bari
- Idioma: Inglés
- Duración si aplica: 20:00
- Enlace: https://www.youtube.com/watch?v=Mo4vesaut8g
- Tema principal: Análisis de complejidad asintótica O en algoritmos iterativos.
- Nivel: Básico / Intermedio
- Qué explica bien: El uso de funciones polinomiales para representar el tiempo que tarda un bucle. Como estudiantes de matemáticas, nos es muy natural ver la ejecución del código como una sumatoria.
- Qué fue confuso: La calidad del audio y del video puede dificultar leer algunas de las ecuaciones en la pizarra.
- Qué ejemplo fue útil: El análisis detallado de bucles anidados donde el iterador interno depende del externo (similar a la iteración en arreglos bidimensionales).
- Cómo se relaciona con el curso: Ayuda a formalizar las "discusiones técnicas" sobre por qué las soluciones simuladas ingenuas (Clase 06 y 07) no escalan.
- Lo recomendarías: Sí, da una base teórica matemática excelente.
- Pregunta técnica: ¿Cómo cambia el análisis de la cota superior O si la operación dentro del bucle tiene tiempos de ejecución variables (análisis amortizado)?

## Recurso 3
- Tipo: Recurso escrito
- Título: Minimum Stack / Minimum Queue
- Autor/canal: CP-Algorithms
- Idioma: Inglés
- Duración si aplica: N/A
- Enlace: https://cp-algorithms.com/data_structures/stack_queue_modification.html
- Tema principal: Modificación de Pilas y Colas para consultar el mínimo en tiempo O(1).
- Nivel: Avanzado
- Qué explica bien: La invariante algorítmica. Demuestra rigurosamente por qué guardar pares (valor, minimo_actual) en la pila funciona para cualquier secuencia de operaciones de adición/extracción.
- Qué fue confuso: El código está en C++ muy compacto, lo que dificulta un poco su lectura para nosotros que usamos python.
- Qué ejemplo fue útil: El truco matemático de simular una Cola (Queue) usando dos Pilas (Stacks) para mantener un mínimo sin alterar la complejidad temporal.
- Cómo se relaciona con el curso: Muestra que la elección de estructura de datos no solo es sobre ordenar elementos, sino sobre qué "metadatos" (información extra) acompañan a esos elementos.
- Lo recomendarías: Si.
- Pregunta técnica: ¿Qué impacto en caché (cache miss) tiene usar objetos anidados (valor, mínimo) en lenguajes de alto nivel versus arrays separados?

## Recurso 4
- Tipo: Recurso escrito (Documentación)
- Título: collections.deque — Double-ended queues
- Autor/canal: Python Software Foundation
- Idioma: Inglés
- Duración si aplica: N/A
- Enlace: https://docs.python.org/3/library/collections.html#collections.deque
- Tema principal: Uso nativo y complejidad asintótica de la estructura Deque en Python.
- Nivel: Básico
- Qué explica bien: Deja clarísimo que las listas de Python estándar tienen una penalización de O(n) para hacer pop(0), y justifica por qué deque logra O(1) en ambos extremos.
- Qué fue confuso: No detalla en profundidad que Python implementa deque como una lista doblemente enlazada por bloques, lo que puede fragmentar la memoria.
- Qué ejemplo fue útil: El uso del argumento maxlen para crear colas limitadas circulares que descartan información vieja automáticamente.
- Cómo se relaciona con el curso: Es la herramienta obligatoria para implementar eficientemente soluciones tipo *Sliding Window* o el problema de *Josephus*.
- Lo recomendarías: Sí, es lectura obligatoria de manual.
- Pregunta técnica: ¿Por qué deque es más ineficiente que una lista normal de Python si queremos acceder a un elemento aleatorio en el medio (deque[i])?

## Recurso 5 (Encontrado por mí)
- Tipo: Video
- Título: Data Structures: Stacks and Queues
- Autor/canal: HackerRank / Gayle Laakmann McDowell
- Idioma: Inglés
- Duración si aplica: 9:15
- Enlace: https://www.youtube.com/watch?v=wjI1WNcIntg
- Tema principal: Implementación física e intuitiva de LIFO y FIFO.
- Nivel: Básico
- Qué explica bien: Las analogías con el mundo real (apilar platos o hacer fila). Es un excelente puente mental antes de ver el código.
- Qué fue confuso: Solo aborda la implementación básica, no toca las variaciones "monótonas".
- Qué ejemplo fue útil: Visualizar cómo el "Head" y el "Tail" (cabecera y cola) se mueven independientemente en la memoria.
- Cómo se relaciona con el curso: Es el cimiento fundacional de las clases 06 y 07; sin entender LIFO y FIFO, es imposible seguir el flujo del control de los algoritmos.
- Lo recomendarías: Sí, si necesitas un refresco conceptual rápido.
- Pregunta técnica: Si implementamos una Cola usando arreglos estáticos en lugar de memoria dinámica, ¿cómo gestionamos el desbordamiento sin redimensionar el array completo?

## Recurso 6 (Encontrado por mí)
- Tipo: Recurso escrito
- Título: Two Pointers Technique
- Autor/canal: GeeksforGeeks
- Idioma: Inglés
- Duración si aplica: N/A
- Enlace: https://www.geeksforgeeks.org/two-pointers-technique/
- Tema principal: Optimización de problemas de búsqueda de pares usando múltiples punteros en iteraciones lineales.
- Nivel: Intermedio
- Qué explica bien: La demostración analítica de cómo, al tener un arreglo ya ordenado, podemos mover un puntero izquierdo o derecho para acercarnos direccionalmente a la meta, logrando resolver el problema en O(n).
- Qué fue confuso: Algunos bloques de código en la página están mal formateados o desactualizados.
- Qué ejemplo fue útil: El problema clásico de "Encontrar un par cuya suma sea $X$ en un arreglo ordenado".
- Cómo se relaciona con el curso: Es un patrón fundamental que rivaliza con el patrón *Sliding Window*. Nos enseña a buscar "información útil" basándonos en la relación de orden de los números.
- Lo recomendarías: Sí, es un patrón vital para cualquier estudiante de matemáticas aplicadas/computacionales.
- Pregunta técnica: ¿En qué escenario es preferible usar la técnica "Two Pointers" en lugar de un "Hash Map" (diccionario en Python) si ambos dan tiempo lineal?

## Recurso 7
- Tipo: Video
- Título: CS50 2021 - Lecture 5 - Data Structures
- Autor/canal: CS50 (Harvard University)
- Idioma: Inglés
- Duración si aplica: 2:13:03 (Revisados los primeros 45 mins sobre Stacks/Queues)
- Enlace: https://www.youtube.com/watch?v=4IrUAqYKjIA
- Tema principal: Gestión de la memoria subyacente para estructuras de datos.
- Nivel: Básico / Intermedio
- Qué explica bien: David Malan explica visualmente (en pizarra y animaciones) cómo se asigna memoria contigua vs no contigua. Demuestra el costo real en el procesador.
- Qué fue confuso: Al usar C, el concepto de punteros puede abrumar a quienes vienen directamente de Python.
- Qué ejemplo fue útil: El proceso de "redimensionar" (resize) una estructura cuando se queda sin espacio, revelando el costo oculto de O(n) al copiar datos.
- Cómo se relaciona con el curso: En Python no vemos la memoria directamente, pero saber que list.append() a veces causa una copia completa del arreglo ayuda a entender los picos de ineficiencia.
- Lo recomendarías: Definitivamente, para entender qué hace Python tras bambalinas.
- Pregunta técnica: ¿Qué algoritmos de asignación de memoria determinan cuánto espacio extra pre-asigna Python cuando se redimensiona una lista?

## Recurso 8
- Tipo: Recurso interactivo / visual
- Título: VisuAlgo - Linked Lists (Stacks & Queues)
- Autor/canal: Dr. Steven Halim
- Idioma: Inglés
- Duración si aplica: N/A
- Enlace: https://visualgo.net/en/list
- Tema principal: Animaciones interactivas paso a paso de estructuras de datos.
- Nivel: Básico a Avanzado
- Qué explica bien: Te permite "jugar" con la estructura. Puedes hacer clic en "Push" o "Pop" y ver cómo los punteros cambian gráficamente a velocidad ajustable.
- Qué fue confuso: La interfaz tiene tantas configuraciones que puede ser un poco caótica al inicio.
- Qué ejemplo fue útil: Insertar un dato al inicio de un arreglo vs insertarlo al inicio de una lista doblemente enlazada (Dequeue), demostrando visualmente por qué uno es lento y el otro instantáneo.
- Cómo se relaciona con el curso: La clase 06 sugirió fuertemente simular el problema (papel y lápiz). VisuAlgo es la versión digital de esa simulación en papel.
- Lo recomendarías: Altamente recomendable, es la mejor herramienta para construir modelos mentales espaciales de los algoritmos.
- Pregunta técnica: ¿Cómo cambian gráficamente los invariantes estructurales cuando cruzamos Pilas con Árboles (por ejemplo, en un recorrido Depth First Search)?

## Tabla comparativa

| Recurso | Claridad | Ejemplos | Profundidad | Visualizaciones | Lo recomendarías |
| --- | --- | --- | --- | --- | --- |
| NeetCode (Video) | Alta | Código en vivo | Media | Pizarra digital | Sí, muy enfocado |
| CP-Algorithms (Escrito)| Media | Matemáticos abstractos| Alta | Nulas | Sí, para teóricos |
| Abdul Bari (Video) | Alta | Sumatorias | Alta | Pizarra física | Sí |
| VisuAlgo (Interactivo)| Alta | Animaciones guiadas | Media | Dinámicas y excelentes | Sí |