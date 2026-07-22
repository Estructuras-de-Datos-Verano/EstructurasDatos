# Discusión Técnica - Práctica 11 (Árboles BST)

Este documento analiza cómo pensamos el diseño, por qué elegimos esta estructura y qué tan eficiente terminó siendo nuestro árbol binario de búsqueda.



## 1. Lista vs Árbol

La diferencia clave está en cómo se acomodan y se buscan los datos en la memoria del programa:

*   **Lista:** Guarda todo en una fila india. Si buscas un dato y tienes mala suerte, vas a tener que revisar los elementos uno por uno desde el principio hasta el final. Esto hace que el tiempo crezca de forma lineal a medida que agregas más información.
*   **Árbol:** Organiza los datos en una estructura de decisiones. En lugar de recorrer una fila, vas tomando bifurcaciones. Si el árbol está bien armado, te permite descartar la mitad de los datos restantes en cada paso.



## 2. Motivación del BST

Un Árbol Binario de Búsqueda (BST) es ideal cuando tu aplicación necesita consultar datos de manera masiva y constante. Aunque te cuesta un poquito más de esfuerzo acomodar el dato en su lugar correcto al momento de insertarlo, esa pequeña inversión se paga sola cuando haces las búsquedas, ya que pasas de un crecimiento lineal a un ritmo logarítmico que es muchísimo más veloz.


## 3. Invariante

Para que todo este sistema funcione, dependemos de una regla de oro que jamás se puede romper (el invariante):

> Si te paras en cualquier nodo del árbol, absolutamente todo lo que esté en su subárbol izquierdo tiene que ser menor a su propio valor, y todo lo que esté en su subárbol derecho tiene que ser mayor.

Nuestra implementación asegura esta regla en el método `insertar` al decidir hacia qué lado enviar cada número y dejar fuera los valores repetidos para evitar problemas con los datos duplicados.



## 4. Inserción

Escribimos la inserción usando recursión porque los árboles son como fractales: cada rama es, en el fondo, otro árbol más pequeño. El flujo funciona así:

1. Si el lugar donde caemos está vacío, creamos un nuevo nodo con el valor.
2. Si el número es menor al del nodo actual, delegamos la tarea a la rama izquierda.
3. Si el número es mayor, delegamos la tarea a la rama derecha.
4. Si el número ya existe, simplemente regresamos el nodo tal como está, ignorando el duplicado para mantener la estructura limpia.



## 5. Recorridos

Los tres recorridos clásicos juegan con el momento exacto en el que hacemos las llamadas recursivas para lograr cosas muy distintas:

*   **Inorden (vamos a la izquierda, luego a la raíz, luego a la derecha):** Nos devuelve los elementos ordenados de menor a mayor[cite: 3]. Al procesar primero el subárbol izquierdo (los menores), luego el nodo en el que estamos y al final el subárbol derecho (los mayores), aprovechamos la regla del BST para que los datos salgan ordenados sin tener que aplicar ningún algoritmo de ordenamiento extra.
*   **Preorden (vamos a la raíz, luego a la izquierda, luego a la derecha):** Es perfecto si necesitas clonar o guardar el árbol en un archivo. Como procesa al nodo padre antes que a sus hijos, te permite reconstruir la misma estructura exacta más adelante.
*   **Postorden (vamos a la izquierda, luego a la derecha, y al final a la raíz):** Es indispensable para liberar memoria o borrar carpetas. Te asegura procesar y eliminar todos los hijos antes de tocar al padre, evitando que dejes referencias sueltas en el camino.



## 6. Altura y Eficiencia

La velocidad de las operaciones como `insertar` o `contiene` depende por completo de qué tan alto sea el árbol.

*   **El mejor caso (Árbol Equilibrado):** Las ramas crecen parejas a los lados. Buscar un dato entre un millón de registros se vuelve una tarea facilísima que se resuelve en unas 20 comparaciones.
*   **El peor caso (Árbol Degenerado):** Si metes los datos ya ordenados (como vimos en las pruebas), las ramas se van a cargar hacia un solo lado. El árbol pierde su magia jerárquica y se convierte en una lista común y corriente, haciendo que las búsquedas se vuelvan lentas y pesadas.



## 7. Pruebas

Diseñamos la suite en `test_estudiante.py` para poner a prueba los límites del árbol:
*   Revisamos que las listas resultantes de los recorridos `preorden` y `postorden` fueran las correctas.
*   Forzamos la inserción ordenada para ver cómo la altura crecía de forma lineal en el peor de los casos.
*   Nos aseguramos de que los valores repetidos no rompieran nada y que el sistema aceptara números negativos respetando el orden.


## 8. Cambio Técnico: `evaluar.py`

El script `evaluar.py` nos dio una gran mano en la organización del proyecto:
*   **Evita problemas de rutas:** Al configurar el entorno de Python antes de correr los tests, se olvida de las carpetas locales de cada computadora.
*   **Código más limpio:** Nos permite escribir importaciones directas (`from implementacion import ...`), tal como se haría en un proyecto profesional.



## 9. Problemas Relacionados

Dominar el BST te abre la puerta a resolver retos interesantes en plataformas de programación (como el problema *700. Search in a Binary Search Tree* o el *94. Binary Tree Inorder Traversal* en LeetCode)[cite: 3]. Te ayuda a entender cómo moverte con punteros que pueden ser nulos y cómo manejar la memoria cuando usas funciones que se llaman a sí mismas.



## 10. Pregunta Abierta

Pensando en cómo se arruina el árbol si le metemos los datos ya ordenados: **¿Cómo podríamos hacer para que el método de inserción reacomode los nodos por sí mismo cada vez que note que un lado está mucho más pesado que el otro?** ¿Valdría la pena el tiempo extra que tardaría en ordenarse contra lo rápido que se harían las búsquedas después?