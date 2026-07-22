## 1. Motivación

**Pregunta.** ¿Qué problema aparece cuando buscamos muchas veces en una lista?

El costo de hacer aquella operación y la complejidad del tiempo, la búsqueda lineal como hemos visto requiere una complejidad O(n).

## 2. Problemas relacionados


**Pregunta.** Elige uno de estos problemas y explica qué concepto de la clase parece practicar.

En el de **LeetCode 700: Search in a Binary Search Tree** se practica directamente la aplicación del invariante del BST para la toma de decisiones bifurcadas. 

## 3. Conceptos básicos

**Pregunta.** Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.

 **Raíz**: 

Nodo A que contiene el valor central inicial.

 **Hijos**:

 El nodo A tiene dos hijos directos: un hijo izquierdo (B) y un hijo derecho (C).

 **Hojas**: 

Los nodos B y C no tienen descendientes, por lo tanto, ambos cumplen la condición de ser nodos hoja (grado cero).

## 4. Árbol binario de búsqueda

**Pregunta.** ¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?

El invariante establece que para cualquier nodo con valor V, todos los elementos de su subárbol izquierdo son estrictamente menores que V y todos los del subárbol derecho son estrictamente mayores que V. Al realizar una comparación en la raíz, si el valor buscado es menor, por la propiedad transitiva del orden, se garantiza que no se encuentra en el subárbol derecho. Esto permite descartar formalmente la mitad de las trayectorias o subconjuntos potenciales en cada nivel de la jerarquía.

## 5. Búsqueda

**Pregunta.** ¿Qué nodos comparas y qué parte descartas en cada paso?

**Paso 1**: 

Se compara con la raíz (8). Como 9 > 8, nos desplazamos al hijo derecho (10) y descartamos por completo el subárbol izquierdo (nodos 4, 2, 6).

**Paso 2**: 

Se compara con el nodo (10). Como 9 < 10, nos desplazamos al hijo izquierdo (9) y descartamos el subárbol derecho (nodo 12).

**Paso 3**: 

Se compara con el nodo (9). Como 9 = 9, la búsqueda concluye con éxito.

## 6. Inserción

**Pregunta.** Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

* **8**: 

Se establece como la raíz del árbol.

* **4**: 

Menor que 8, se posiciona como hijo izquierdo de 8.

* **10**: 

Mayor que 8, se posiciona como hijo derecho de 8.

* **2**: 

Menor que 8 y menor que 4, se coloca como hijo izquierdo de 4.

* **6**: 

Menor que 8 y mayor que 4, se coloca como hijo derecho de 4.

* **9**: 

Mayor que 8 y menor que 10, se coloca como hijo izquierdo de 10.

* **12**: 

Mayor que 8 y mayor que 10, se coloca como hijo derecho de 10.

## 7. Altura

**Pregunta.** ¿Qué relación hay entre altura y costo de búsqueda?

Existe una relación directa entre la altura h de la estructura y el costo de la búsqueda en el peor de los casos. Dado que cada comparación nos hace descender un nivel en el árbol, el número máximo de comparaciones requeridas para encontrar un elemento o determinar su ausencia es igual a la altura del árbol (h).

## 8. Recorridos

**Pregunta.** ¿Por qué inorden produce valores ordenados en un BST?

El recorrido inorden procesa los nodos bajo la secuencia. Debido al invariante del BST, el subárbol izquierdo contiene por definición únicamente valores menores que la raíz, y el derecho contiene valores mayores. 

## 9. Animaciones

**Pregunta.** ¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

Una animación permite visualizar la naturaleza dinámica y secuencial de los algoritmos sobre la estructura. A diferencia de una lista estática de valores, ayuda a identificar los caminos de decisión, las ramificaciones descartadas en tiempo real y cómo cambia la geometría o altura del árbol ante cada inserción.

## 10. Implementación

**Pregunta.** ¿Qué métodos parecen depender naturalmente de recursión?

Los métodos que dependen naturalmente de la recursión son insertar, contiene, altura, inorden, preorden y postorden. Esto se debe a que un árbol es una estructura de datos inductiva o autosemejante: cada subárbol es, a su vez, un árbol binario válido.

## 11. Pruebas

**Pregunta.** ¿Qué problema resuelve `evaluar.py`?

Lo que hace es estandarizar el entorno de ejecución del intérprete, también resuelve el problema de la gestión de rutas absolutas y relativas modificando dinámicamente el PYTHONPATH del sistema. Esto permite que los archivos de prueba localizados independientes importen los módulos de entrega sin el ModuleNotFoundError.

## 12. Patrón descubierto

**Pregunta.** Explica con tus palabras el patrón descubierto.

El patrón identificado es la estructuración jerárquica basada en relaciones de orden para optimizar operaciones de acceso. Se activa cuando el espacio de estados o datos posee un orden total definido, se requiere alta frecuencia de consultas y es posible aplicar una partición del espacio para evitar búsquedas exhaustivas.

## 13. Cierre

1. ¿Qué ganamos frente a una lista?

Reducimos la complejidad promedio de búsqueda de un comportamiento lineal O(n) a un comportamiento logarítmico O(log n).

2. ¿Qué propiedad mantiene el BST?

El invariante de ordenamiento espacial.

3. ¿Qué pasa si insertamos datos ordenados?

El árbol pierde su propiedad de ramificación simétrica, convirtiéndose en una estructura lineal no bifurcada.

4. ¿Cuándo podría degradarse un BST?

Se degrada cuando los datos de entrada se insertan con una ordenación monótona, llevando la altura a su valor máximo, h = n.

5. ¿Qué problema relacionado puedo practicar?

El de LeetCode Insert into a Binary Search Tree.

