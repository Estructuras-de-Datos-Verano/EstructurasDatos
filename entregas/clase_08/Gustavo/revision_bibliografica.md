# Revisión Bibliográfica de Recursos Técnicos

En este documento presento el registro y análisis de los 8 recursos que consulté para profundizar en estructuras de datos, algoritmos y patrones de diseño. La selección abarca videos y textos en inglés y español, combinando teoría matemática con implementaciones reales en Python.

---

## 1. 2.6 Heap - Heap Sort - Heapify - Priority Queues

* **Tipo:** Vídeo
* **Título:** 2.6 Heap - Heap Sort - Heapify - Priority Queues
* **Autor o canal:** Abdul Bari
* **Idioma:** Inglés
* **Duración:** 48:53
* **Enlace:** https://www.youtube.com/watch?v=HqPJF2L5h9U
* **Tema principal:** Árboles binarios completos (Heaps), algoritmo Heapify y colas de prioridad.
* **Nivel:** Intermedio
* **Qué explica bien:** Explica de forma insuperable la lógica matemática básica de por qué un árbol binario completo se puede guardar en un arreglo regular usando fórmulas de índices (`2i` y `2i+1`), evitando usar punteros complejos en la memoria.
* **Qué fue confuso:** Al ser una clase en un pizarrón físico de estilo universitario clásico, el ritmo a veces es un poco lento y la calidad del audio requiere bastante concentración.
* **Qué ejemplo fue útil:** La comparación paso a paso donde muestra por qué meter elementos uno por uno tarda $O(n \log n)$, mientras que el método *Heapify* reorganiza toda la lista de un golpe en tiempo lineal $O(n)$.
* **Cómo se relaciona con el curso:** Nos ayuda a entender qué hay detrás del módulo `heapq` en Python y cómo gestionar datos cuando necesitamos acceder al máximo o mínimo instantáneamente sin reordenar todo el arreglo.
* **Si lo recomendarías:** Sí, es excelente para aprender las bases teóricas de la estructura antes de tocar el teclado.
* **Una pregunta técnica:** ¿Qué sobrecarga de rendimiento o desventaja en memoria caché existe al representar un árbol en un arreglo estático frente a un arreglo dinámico cuando los datos no dejan de crecer?

---

## 2. Data Structures: Hash Tables

* **Tipo:** Vídeo
* **Título:** Data Structures: Hash Tables
* **Autor o canal:** William Fiset
* **Idioma:** Inglés
* **Duración:** 24:37
* **Enlace:** https://www.youtube.com/watch?v=knV86FlSXJ8
* **Tema principal:** Funciones hash, manejo de colisiones y rendimiento de tablas dispersas.
* **Nivel:** Intermedio
* **Qué explica bien:** Deja clarísimo cómo funciona el "factor de carga" (*load factor*) y por qué la tabla se ve obligada a duplicar su tamaño internamente cuando se empieza a llenar para no perder velocidad.
* **Qué fue confuso:** La parte donde profundiza en el sondeo cuadrático y doble hashing avanza de golpe a un nivel algebraico un poco abstracto sin mostrar mucho código.
* **Qué ejemplo fue útil:** La animación del manejo de colisiones por encadenamiento (*separate chaining*), viendo cómo se crea una pequeña lista enlazada dentro de una misma cubeta cuando dos llaves arrojan el mismo índice.
* **Cómo se relaciona con el curso:** Conecta directamente con el uso diario que le damos a los diccionarios (`dict`) y conjuntos (`set`) en Python, ayudándonos a entender por qué buscar datos ahí toma un tiempo constante $O(1)$.
* **Si lo recomendarías:** Totalmente, sus animaciones visuales hacen que un tema complejo se entienda de inmediato.
* **Una pregunta técnica:** Si nuestra función hash es pésima y todas nuestras llaves caen en el mismo casillero, ¿cómo podemos evitar que el tiempo de búsqueda caiga al peor caso $O(n)$?

---

## 3. Monotonic Stack Explained - Daily Temperatures (LeetCode 739)

* **Tipo:** Vídeo
* **Título:** Monotonic Stack Explained - Daily Temperatures
* **Autor o canal:** NeetCode
* **Idioma:** Inglés
* **Duración:** 11:21
* **Enlace:** https://www.youtube.com/watch?v=cTBiBSnjO3c
* **Tema principal:** Uso de pilas monótonas para resolver problemas de comparación de elementos adyacentes.
* **Nivel:** Intermedio
* **Qué explica bien:** Demuestra muy bien la idea de "descartar información inútil": nos enseña por qué podemos eliminar los valores que ya no nos sirven de la pila sin miedo a perder la solución final.
* **Qué fue confuso:** En la implementación inicial del código, la manera de guardar tuplas de `(temperatura, indice)` en la pila puede confundir un poco el seguimiento visual de qué variable se está comparando en el ciclo `while`.
* **Qué ejemplo fue útil:** La prueba manual (*dry run*) sobre el arreglo `[73, 74, 75, 71, 69, 72, 76, 73]`, viendo visualmente cómo los números pequeños se van apilando hasta que llega un número grande y "limpia" la estructura de golpe.
* **Cómo se relaciona con el curso:** Es la base conceptual directa del problema *Nearest Smaller Values* (Valores menores más cercanos) que hemos analizado en nuestras prácticas algorítmicas.
* **Si lo recomendarías:** Sí, es uno de los mejores canales actuales para traducir lógica algorítmica y abstracta en código limpio de Python.
* **Una pregunta técnica:** ¿En qué situaciones particulares del desarrollo de software real nos conviene más usar un arreglo auxiliar precomputado en lugar de mantener una pila monótona en tiempo real?

---

## 4. Two Pointers & Sliding Window Algorithms Explained (Recurso externo 1)

* **Tipo:** Vídeo
* **Título:** Two Pointers & Sliding Window Algorithms Explained
* **Autor o canal:** Greg Hogg
* **Idioma:** Inglés
* **Duración:** 35:10
* **Enlace:** https://www.youtube.com/watch?v=p-ss2JQha+Y
* **Tema principal:** Técnicas de dos punteros y ventanas deslizantes de tamaño fijo y dinámico.
* **Nivel:** Principiante / Intermedio
* **Qué explica bien:** La transición mental entre usar dos ciclos anidados lentos $O(n^2)$ y optimizarlo a un solo ciclo lineal $O(n)$ simplemente moviendo dos marcadores de posición sobre la lista.
* **Qué fue confuso:** En la explicación de la ventana deslizante dinámica, la lógica matemática de cuándo encoger exactamente el puntero izquierdo (`L`) en el ciclo `while` interno se siente rápida y requiere pausar el video varias veces.
* **Qué ejemplo fue útil:** La resolución del problema de encontrar la subcadena más larga sin caracteres repetidos, usando un conjunto (`set`) para registrar qué letras están actualmente dentro de la ventana de búsqueda.
* **Cómo se relaciona con el curso:** Nos da herramientas prácticas para resolver problemas de compresión de datos y búsquedas eficientes en secuencias continuas sin usar memoria extra innecesaria.
* **Si lo recomendarías:** Sí, el autor es muy claro y escribe código en Python de una manera súper idiomática y fácil de seguir.
* **Una pregunta técnica:** Si los datos del arreglo no están ordenados numéricamente y no podemos gastar tiempo en ordenarlos previamente con `.sort()`, ¿en qué casos específicos sigue siendo válido usar la técnica de dos punteros en los extremos?

---

## 5. Official Documentation: collections.deque

* **Tipo:** Escrito
* **Título:** collections — Container datatypes (deque objects)
* **Autor o canal:** Python Software Foundation
* **Idioma:** Inglés
* **Duración:** No aplica (Lectura de referencia de 15 minutos)
* **Enlace:** https://docs.python.org/3/library/collections.html#collections.deque
* **Tema principal:** Colas doblemente enlazadas (*Double-ended queues*) en la librería estándar de Python.
* **Nivel:** Principiante / Intermedio
* **Qué explica bien:** Contraste explícito en rendimiento: aclara muy bien por qué una lista clásica de Python (`list`) toma un tiempo lineal $O(n)$ para sacar el primer elemento usando `.pop(0)`, mientras que `deque` lo hace de inmediato en $O(1)$.
* **Qué fue confuso:** Al ser una documentación puramente técnica, no te dice cómo usarlo para diseñar un algoritmo; asume que el lector ya sabe qué es y cómo funciona una cola.
* **Qué ejemplo fue útil:** El ejemplo práctico donde configuran un `deque` con un tamaño máximo fijo (`maxlen=3`) para crear una cola que funciona como un historial o "memoria circular" que va borrando lo más viejo automáticamente.
* **Cómo se relaciona con el curso:** Conecta con las simulaciones de colas que estudiamos, en especial para modelar procesos secuenciales estilo el problema de *Josephus*.
* **Si lo recomendarías:** Sí, leer la documentación oficial siempre ayuda a perder el miedo a entender cómo están hechas las herramientas del lenguaje.
* **Una pregunta técnica:** Si `deque` es tan rápido para agregar y quitar elementos por ambos extremos, ¿por qué resulta mucho más lento que una lista común cuando intentamos leer un elemento en medio de la estructura como `mi_deque[500]`?

---

## 6. Breadth-First Search (BFS)

* **Tipo:** Escrito
* **Título:** Breadth-First Search
* **Autor o canal:** CP-Algorithms
* **Idioma:** Inglés
* **Duración:** No aplica (Artículo y guía técnica de 25 minutos)
* **Enlace:** https://cp-algorithms.com/graph/breadth-first-search.html
* **Tema principal:** Búsqueda en anchura en grafos no ponderados y cálculo de caminos mínimos.
* **Nivel:** Intermedio / Avanzado
* **Qué explica bien:** Explica súper bien por qué recorrer un mapa "por niveles de distancia" o capas concéntricas nos asegura encontrar el camino más corto sin tener que probar absolutamente todas las combinaciones posibles.
* **Qué fue confuso:** La implementación en código mostrada está escrita en C++ usando vectores y apuntadores propios de la STL, lo que obliga a traducir mentalmente esa sintaxis si estás acostumbrado solo a Python.
* **Qué ejemplo fue útil:** El uso del arreglo de "padres" (`p[u]`) durante el recorrido de la cola, mostrando cómo al llegar al destino podemos reconstruir todo el camino de regreso paso a paso.
* **Cómo se relaciona con el curso:** Amplía nuestra comprensión del uso práctico de las colas FIFO (*First-In, First-Out*), pasándolas de simples listas de espera a motores de búsqueda en mapas y redes complejas.
* **Si lo recomendarías:** Sí, es uno de los repositorios escritos más rigurosos y respetados para entender la lógica detrás del desarrollo de algoritmos en programación competitiva.
* **Una pregunta técnica:** Si nuestro problema involucra un mapa donde algunas calles cuestan el doble de tiempo que otras (pesos en las aristas), ¿por qué BFS falla en darnos la respuesta correcta y por qué tendríamos que cambiar a Dijkstra?

---

## 7. The Algorithm Design Manual (Capítulo 3: Data Structures)

* **Tipo:** Escrito (Libro)
* **Título:** The Algorithm Design Manual (Capítulo 3)
* **Autor o canal:** Steven S. Skiena
* **Idioma:** Inglés
* **Duración:** No aplica (Capítulo de libro, aprox. 1 hora de lectura)
* **Enlace:** Fragmentos disponibles en consulta bibliográfica / biblioteca
* **Tema principal:** Comparativa entre estructuras contiguas (arreglos) y estructuras enlazadas por punteros.
* **Nivel:** Avanzado
* **Qué explica bien:** Expone con claridad la gran diferencia filosófica del diseño de software: tener todos los datos juntos en un bloque de memoria (rápido de leer) versus tenerlos dispersos en la memoria y conectados mediante enlaces (rápido para insertar y modificar en medio).
* **Qué fue confuso:** Trata la memoria desde una perspectiva muy cercana al hardware y al lenguaje C, por lo que temas como punteros explícitos y recolección de basura pueden sentirse ajenos a la experiencia típica en lenguajes automáticos como Python.
* **Qué ejemplo fue útil:** La tabla comparativa general donde cruza arreglos ordenados, arreglos desordenados y listas enlazadas evaluando el costo matemático *Big-O* de cada operación posible (buscar, insertar, borrar, mínimo, máximo).
* **Cómo se relaciona con el curso:** Nos da el criterio teórico para defender por qué en nuestras prácticas optamos por una estructura de datos particular en lugar de intentar solucionar todo con listas sencillas.
* **Si lo recomendarías:** Definitivamente, es una lectura formativa obligatoria para cualquier estudiante de ciencias de la computación o matemáticas aplicadas.
* **Una pregunta técnica:** ¿Cómo influye la arquitectura moderna de la caché del procesador (L1/L2) en que, en la práctica, recorrer un arreglo contiguo sea muchísimo más rápido que recorrer una lista enlazada, aunque la teoría algoritmica diga que ambos toman tiempo $O(n)$?

---

## 8. Python Stacks, Queues, and Priority Queues in Practice (Recurso externo 2)

* **Tipo:** Escrito
* **Título:** Python Stacks, Queues, and Priority Queues in Practice
* **Autor o canal:** Real Python
* **Idioma:** Inglés
* **Duración:** No aplica (Artículo práctico de 20 minutos)
* **Enlace:** https://realpython.com/queue-in-python/
* **Tema principal:** Comparativa y uso correcto de herramientas integradas de concurrencia y estructuras de Python (`list`, `deque`, `Queue`, `heapq`).
* **Nivel:** Principiante / Intermedio
* **Qué explica bien:** Aclara muy bien la diferencia entre módulos pensados para algoritmos simples (`collections.deque`) y módulos diseñados exclusivamente para sincronizar programas que corren muchos procesos al mismo tiempo (`queue.Queue` o `multiprocessing.Queue`).
* **Qué fue confuso:** La parte donde explica cómo los candados de seguridad de hilos (*thread-safe locking*) alientan las operaciones algorítmicas puede sentirse técnica si no has estudiado concurrencia previamente.
* **Qué ejemplo fue útil:** La demostración con código temporizado (*benchmarking*) que muestra cómo usar `list.insert(0, item)` destruye por completo el rendimiento del programa frente a `deque.appendleft(item)` cuando el volumen de datos escala.
* **Cómo se relaciona con el curso:** Nos da el criterio práctico y la madurez técnica para elegir qué importar y qué escribir desde cero en nuestras entregas del laboratorio.
* **Si lo recomendarías:** Sí, es de las lecturas prácticas más útiles que puedes hacer si vas a programar en Python para proyectos reales.
* **Una pregunta técnica:** Si queremos implementar una cola de prioridad que nos permita cambiar el valor o prioridad de un elemento que ya está adentro del heap, ¿cómo podemos hacerlo en Python sin destruir las propiedades de la estructura al usar el módulo `heapq`?

---

## Tabla Comparativa de Recursos Consultados

| # | Recurso | Tipo | Nivel | Enfoque Principal | Puntos Fuertes | Limitaciones |
|---|---|---|---|---|---|---|
| **1** | *2.6 Heap - Heap Sort - Heapify* (Abdul Bari) | Vídeo | Intermedio | Teórico / Matemático | Explicación del razonamiento algebraico detrás de árboles y arreglos. | No muestra implementaciones en código ni sintaxis moderna. |
| **2** | *Data Structures: Hash Tables* (William Fiset) | Vídeo | Intermedio | Teórico / Visual | Animaciones claras sobre colisiones y factor de carga. | Salto abrupto al explicar métodos matemáticos avanzados de sondeo. |
| **3** | *Monotonic Stack Explained* (NeetCode) | Vídeo | Intermedio | Práctico / Algorítmico | Traducción directa del problema de LeetCode a código claro de Python. | Enfoque algo cerrado a un patrón de problema en particular. |
| **4** | *Two Pointers & Sliding Window* (Greg Hogg) | Vídeo | Principiante / Intermedio | Práctico / Idiomático | Cuatro ejemplos ejecutados en código Python limpio y moderno. | La explicación de ventanas dinámicas es un poco rápida en los ciclos. |
| **5** | *Official Docs: collections.deque* (Python Docs) | Escrito | Principiante / Intermedio | Referencia API | Precisión absoluta sobre los costos de rendimiento y memoria. | No enseña diseño algorítmico ni cómo plantear problemas con esta herramienta. |
| **6** | *Breadth-First Search (BFS)* (CP-Algorithms) | Escrito | Intermedio / Avanzado | Teórico / Algorítmico | Demostraciones rigurosas y claras sobre recorridos por niveles en grafos. | Ejemplos en C++ que requieren traducción si solo trabajas en Python. |
| **7** | *The Algorithm Design Manual* (Steven Skiena) | Escrito | Avanzado | Teórico / Fundamentos | Visión profunda sobre memoria, contigüidad y trade-offs algorítmicos. | Muy inclinado hacia hardware, punteros clásicos y estilo de lenguaje C. |
| **8** | *Python Stacks, Queues in Practice* (Real Python) | Escrito | Principiante / Intermedio | Práctico / Ingeniería | Guía para elegir estructuras según si usas concurrencia o no. | No profundiza en las demostraciones matemáticas rigurosas detrás de las estructuras. |