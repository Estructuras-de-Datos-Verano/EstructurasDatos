# Discusión técnica

## 1. ¿Un BST siempre es eficiente?
No, ya que si los datos entran acomodados con un mal orden, el árbol pierde su capacidad de ramificarse y se vuelve igual de lento que cualquier arreglo lineal que tengamos que recorrer desde el principio.

## 2. Lista vs BST
La diferencia clave es el orden interno. La lista guarda cosas una detrás de otra en secuencia sin importar el valor, obligándote a buscar a ciegas elemento por elemento. El BST usa una regla de orden total: los chicos a la izquierda, los grandes a la derecha. Si el árbol está bien hecho, esa regla te permite ignorar pedazos enteros con cada decisión que tomas.

## 3. Altura y comparaciones
Están conectadas directamente. Cada paso que bajas en el árbol es un nodo que visitas y una comparación que haces. Por eso la altura marca el peor de los casos posibles: si buscas algo que está en la punta más baja o un dato que ni siquiera existe, vas a terminar haciendo un número de comparaciones igual a la altura total del árbol.

## 4. Árbol balanceado vs árbol degenerado
Un árbol balanceado abre sus ramas de forma simétrica hacia los lados, manteniendo a todos los nodos lo más cerca posible de la raíz para que los caminos sean cortos. El degenerado no se abre porque se va en una sola línea recta vertical hacia abajo como si fuera una lista común y corriente, lo que destruye el propósito de tener un árbol.

## 5. Orden de inserción
La forma final del árbol depende al 100% de cómo le vayas metiendo los números. Si metes datos bien mezclados al azar, el árbol se equilibra solo por probabilidad. Pero si se te ocurre meter los datos ya ordenados (del 1 al 10, por ejemplo), cada número nuevo siempre va a ser el más grande de todos y se irá colgando a la derecha, creando un árbol degenerado.

## 6. Complejidad
En el mejor escenario o en el promedio, cuando el árbol está balanceado, la complejidad de la búsqueda es de orden logarítmico O(log n), lo cual es rapidísimo. Pero en el peor de los casos, cuando el árbol se degenera y se vuelve una línea recta, la complejidad se cae por completo a un orden lineal O(n).

## 7. Experimentos y evidencia
Cuando mides las búsquedas con código, la teoría se nota clarito en los números. Al meter 1,000 elementos desordenados y buscar uno, el conteo de operaciones se queda en poco más de 10 comparaciones. Si haces lo mismo pero metiendo esos 1,000 elementos ya ordenados, el contador se dispara hasta hacer las 1,000 comparaciones completas.

## 8. Animaciones
En los archivos visuales se ve perfecto cómo trabaja cada estructura. En el caso balanceado, el camino de búsqueda avanza rápido abriéndose paso por niveles que se acaban pronto. En el caso degenerado, ves la línea interminable de nodos y cómo el algoritmo tiene que bajar escalón por escalón en un recorrido larguísimo.

## 9. Pruebas propias
Para validar de verdad nuestra estructura diseñamos tres escenarios específicos en test_estudiante.py:

9.1 test_arbol_totalmente_vacio: 

Validamos las precondiciones base. Asegura que un árbol sin datos marque altura 0, nodos 0 y que no mienta diciendo que está degenerado, además de que buscar en él cueste exactamente 0 comparaciones.

9.2 test_arbol_con_un_solo_nodo: 

El primer caso con datos. Sirve para ver que la altura sea 1 y que al buscar cualquier elemento (esté o no), el código se detenga tras la primera comparación en la raíz sin lanzar errores de punteros vacíos.

9.3 test_arbol_en_linea_recta: 

Forzamos la degeneración metiendo una secuencia ordenada. Así comprobamos que es_degenerado() devuelva True y que el método de comparaciones de búsqueda asuma el peor caso posible, dando un costo igual al total de nodos del árbol.

## 10. Revisión técnica del PR
Cuando revisas el código de un compañero, no solo ves que este funcionando, sino también cómo lo pensó. Te fijas en detalles de rendimiento, como evitar que su algoritmo calcule la altura repitiendo recorridos en nodos que ya visitó (lo que haría lento el programa) o ver si controló bien los casos donde no hay hijos.

## 11. Problemas relacionados
El problema 110 de LeetCode (Balanced Binary Tree) sirve mucho para aplicar esto. Te obliga a escribir una función recursiva que calcule las alturas de los subárboles izquierdo y derecho de cada nodo para validar que no se lleven más de 1 de diferencia.

## 12. Pregunta abierta
¿Existe alguna propiedad probabilística o umbral matemático exacto que nos permita predecir cuántas inserciones consecutivas ordenadas tolera un BST promedio antes de que su costo de búsqueda deje de comportarse como O(log n) y empiece a pesar como O(n)?