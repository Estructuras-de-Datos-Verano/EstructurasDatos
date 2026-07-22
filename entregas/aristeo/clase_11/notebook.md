# Notebook Aristeo
## 1. Motivación
### ¿Qué problema aparece cuando buscamos muchas veces en una lista?

Si la lista no está ordenada, buscar un valor exige revisar elemento por elemento hasta encontrarlo o llegar al final, es decir, un costo que crece linealmente con el tamaño de la lista. Aunque la lista esté ordenada, seguimos pagando ese costo lineal a menos que usemos una estructura que nos permita descartar partes completas del espacio de búsqueda en cada paso, en lugar de revisar un elemento a la vez.

## 2. Problemas relacionados
### Elige uno de estos problemas y explica qué concepto de la clase parece practicar.

Elegí LeetCode 700, "Search in a Binary Search Tree". Practica directamente el invariante del BST: en cada nodo se compara el valor buscado contra el valor del nodo actual y, según sea menor o mayor, se decide bajar al subárbol izquierdo o al derecho, descartando el otro subárbol completo. Es el mismo mecanismo que implementé en `contiene`.

## 3. Conceptos básicos
### Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja.

Un árbol con raíz 8, hijo izquierdo 4 e hijo derecho 10, donde 4 a su vez tiene como hijos a 2 y 6. En este árbol, 8 es la raíz, 4 y 10 son hijos directos de la raíz, y 2, 6 y 10 son hojas porque no tienen hijos (10 sería hoja solo si no tuviera hijos propios; en el ejemplo de los GIFs, 10 tiene hijos 9 y 12, así que las hojas reales de ese árbol son 2, 6, 9 y 12).

## 4. Árbol binario de búsqueda
### ¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda?

Porque el invariante garantiza que todo el subárbol izquierdo de un nodo contiene únicamente valores menores que ese nodo, y todo el subárbol derecho contiene únicamente valores mayores. Entonces, al comparar el valor buscado con el nodo actual, sabemos con certeza en qué mitad del árbol podría estar (o que no está en absoluto), y podemos ignorar la otra mitad sin revisarla.

## 5. Búsqueda
### ¿Qué nodos comparas y qué parte descartas en cada paso?

Buscando 9 en el árbol de la imagen (raíz 8, izquierda 4 con hijos 2 y 6, derecha 10 con hijos 9 y 12): primero comparo 9 con 8; como 9 es mayor, descarto todo el subárbol izquierdo (4, 2, 6). Luego comparo 9 con 10; como 9 es menor, descarto el subárbol derecho de 10 (12). Finalmente comparo 9 con 9 y lo encuentro. En total, tres comparaciones y dos subárboles completos descartados.

## 6. Inserción
### Inserta manualmente los valores del ejemplo y describe dónde queda cada uno.

Con la secuencia `8, 4, 10, 2, 6, 9, 12`: 8 se inserta como raíz. 4 es menor que 8, así que queda como hijo izquierdo de 8. 10 es mayor que 8, queda como hijo derecho de 8. 2 es menor que 8 y menor que 4, queda como hijo izquierdo de 4. 6 es menor que 8 pero mayor que 4, queda como hijo derecho de 4. 9 es mayor que 8 pero menor que 10, queda como hijo izquierdo de 10. 12 es mayor que 8 y mayor que 10, queda como hijo derecho de 10.

## 7. Altura
### ¿Qué relación hay entre altura y costo de búsqueda?

El costo de una búsqueda (o inserción) en el peor caso es proporcional a la altura del árbol, porque el algoritmo sigue un único camino desde la raíz hasta un nodo o hasta encontrar un hueco (`None`), y la cantidad máxima de pasos en ese camino es justamente la altura. Un árbol bien balanceado tiene altura del orden de `log(n)`, mientras que un árbol degenerado tiene altura del orden de `n`, lo que hace que la búsqueda se comporte como en una lista.

## 8. Recorridos
### ¿Por qué inorden produce valores ordenados en un BST?

Porque inorden visita primero todo el subárbol izquierdo, luego el nodo actual y después todo el subárbol derecho. Como el invariante del BST garantiza que el subárbol izquierdo tiene solo valores menores y el derecho solo valores mayores, al aplicar esta regla recursivamente en cada nodo se termina visitando los valores exactamente en orden ascendente.

## 9. Animaciones
### ¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores?

La animación deja ver la forma jerárquica del árbol y el camino específico que sigue cada operación: qué nodo se compara primero, hacia qué lado se avanza y qué parte queda descartada. En una lista de valores esa información se pierde, porque una lista no muestra relaciones de "padre e hijo" ni permite visualizar qué porción del espacio de búsqueda se está eliminando en cada paso.

## 10. Implementación
### ¿Qué métodos parecen depender naturalmente de recursión?

`insertar`, `contiene`, `altura` y los tres recorridos (`inorden`, `preorden`, `postorden`) dependen naturalmente de recursión, porque todos ellos se definen en términos de "resolver el problema en un subárbol izquierdo o derecho y combinar el resultado con el nodo actual". Cada nodo es en sí mismo la raíz de un árbol más pequeño, así que el mismo procedimiento aplicado al nodo se puede reutilizar en sus hijos.

## 11. Pruebas
### ¿Qué problema resuelve `evaluar.py`?

Resuelve el problema de que los tests públicos necesiten encontrar mi `implementacion.py` sin importar desde qué carpeta se ejecuten. El script verifica que exista mi carpeta de entrega y mi archivo `implementacion.py`, agrega esa carpeta al `PYTHONPATH` y luego corre `pytest -v`, de modo que los tests puedan hacer `from implementacion import ArbolBinarioBusqueda, Nodo` sin que cada alumno tenga que configurar manualmente las rutas de importación.

## 12. Patrón descubierto
### Explica con tus palabras el patrón descubierto.

El patrón es "organización jerárquica con invariante de orden para descartar información". En vez de guardar los datos en una secuencia plana donde hay que revisarlos uno por uno, se organizan en una estructura de árbol donde cada nodo divide el espacio de búsqueda en dos partes según una regla de orden. Este patrón aplica siempre que necesito consultar muchas veces si un dato existe, mis datos tienen una relación de orden bien definida, y quiero poder descartar una fracción grande del espacio en cada paso en lugar de revisarlo completo.

## 13. Cierre
### 1. ¿Qué ganamos frente a una lista?

Ganamos, en el caso promedio y en árboles balanceados, un costo de búsqueda e inserción del orden de `log(n)` en lugar de `n`, porque en cada paso descartamos aproximadamente la mitad de los datos restantes.

---
### 2. ¿Qué propiedad mantiene el BST?

Mantiene el invariante de orden: para cada nodo, todos los valores del subárbol izquierdo son menores que el valor del nodo, y todos los valores del subárbol derecho son mayores.

---
### 3. ¿Qué pasa si insertamos datos ordenados?

El árbol se degenera en una especie de lista enlazada: cada nuevo valor se inserta siempre en el mismo lado (por ejemplo, siempre a la derecha si los datos vienen ascendentes), y la altura crece linealmente con la cantidad de elementos en vez de mantenerse cercana a `log(n)`.

---
### 4. ¿Cuándo podría degradarse un BST?

Se degrada cuando los datos se insertan en un orden ya ordenado (ascendente o descendente) o casi ordenado, porque entonces las inserciones se van acumulando siempre hacia el mismo lado y el árbol pierde su forma balanceada, acercándose a una lista.

---
### 5. ¿Qué problema relacionado puedo practicar?

Puedo practicar LeetCode 701 "Insert into a Binary Search Tree", que es prácticamente el mismo mecanismo que implementé en `insertar`, y también CSES "Subordinates" para trabajar con árboles y jerarquías en un contexto distinto al de búsqueda.