# Discusión técnica

## 1. Lista vs árbol

Una lista impone una restricción de vecindad estrictamente secuencial indexada por enteros positivos, donde la única relación explícita entre elementos es la adyacencia posicional. Un árbol, bajo una perspectiva de teoría de grafos, es un grafo conexo y acíclico que modela dependencias jerárquicas directas. Matemáticamente, pasamos de una dimensión lineal a una estructura ramificada que permite explotar propiedades topológicas para optimizar la localización de subconjuntos.

## 2. Motivación del BST

La motivación interior para construir un BST es el principio de "divide y vencerás". El objetivo es minimizar la incertidumbre del espacio de búsqueda con el menor número de comparaciones posibles. Al organizar los datos bajo un criterio algebraico de orden, transformamos la búsqueda de una exploración exhaustiva elemento por elemento a una secuencia de decisiones binarias óptimas.

## 3. Invariante

El invariante del BST es también una restricción estructural global aplicada localmente en cada nodo. Si x es un nodo y y es un nodo en su subárbol izquierdo, entonces y < x. Esta propiedad formal de asimetría nos permite asegurar que las consultas sobre el árbol se comporten como cotas que delimitan de forma estricta los intervalos válidos en cada bifurcación.

## 4. Inserción

El proceso de inserción en esta práctica es determinista y no destructivo respecto al orden preexistente, pero carece de un mecanismo de reestructuración o rotación. La topología final del árbol es sensible a la permutación inicial de los datos de entrada; esto implica que el mismo conjunto de datos puede generar configuraciones morfológicas completamente distintas dependiendo estrictamente del orden cronológico en el que se ejecuten las llamadas al método insertar.

## 5. Recorridos

Los recorridos en profundidad (DFS) representan distintas formas de proyectar la estructura bidimensional del árbol sobre un espacio unidimensional. La equivalencia entre el recorrido inorden y el orden canónico de los números enteros demuestra que la geometría del BST codifica de forma implícita la ordenación de los elementos, permitiendo extraer la información de manera ordenada sin requerir un algoritmo de ordenamiento adicional sobre los arreglos resultantes.

## 6. Altura y eficiencia

En condiciones ideales de simetría (un árbol perfectamente balanceado), la altura está acotada por h = log_2(n + 1) , lo que garantiza que el costo de las operaciones fundamentales sea asintóticamente eficiente, de orden O(log n). No obstante, en ausencia de balanceo dinámico, el peor escenario posible transforma la estructura en un árbol degenerado (equivalente a una lista enlazada) con altura h = n, lo que degrada la complejidad a O(n) y anula la ventaja teórica de la estructura.

## 7. Pruebas

El diseño de pruebas unitarias en test_estudiante.py se estructuró con base en el análisis de valores frontera y casos de degeneración. Se determinó prioritario evaluar el comportamiento del método altura ante secuencias monótonas crecientes y el manejo de búsquedas estériles (valores que exceden las cotas del árbol). Esto valida que las implementaciones de los métodos manejen correctamente las referencias nulas (None) sin generar interrupciones en la pila de llamadas.

## 8. Cambio técnico: evaluar.py

La incorporación de evaluar.py modifica el flujo de trabajo al abstraer la manipulación de variables de entorno del sistema operativo. Al inyectar la ruta de entrega de forma explícita en el vector de búsqueda de módulos de Python (sys.path), se elimina el acoplamiento rígido de los scripts de prueba respecto a las carpetas locales. Esto garantiza la reproducibilidad de los resultados con independencia de la estructura de directorios desde la cual se invoque el comando.

## 9. Problemas relacionados

El análisis de problemas como Subordinates en CSES traslada los conceptos del BST a árboles generales no binarios donde el orden izquierdo-derecho no es prioritario, sino la cardinalidad de los subárboles dependientes. Esto demuestra que las técnicas de recorrido recursivo aprendidas son extensibles al análisis de dependencias directas en sistemas complejos y redes jerárquicas generalizadas.

## 10. Pregunta abierta

¿Existe algún algoritmo eficiente de ordenamiento de listas cuya secuencia exacta de comparaciones coincida bit a bit con la secuencia de decisiones tomadas al construir e inspeccionar mediante inorden un árbol binario de búsqueda balanceado?