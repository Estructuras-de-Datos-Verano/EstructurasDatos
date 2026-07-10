# Discusión técnica

## 1. Problema que resuelve AVL

Evita que un árbol binario de búsqueda se deforme y quede como una lista enlazada cuando los datos entran ordenados. Su objetivo es mantener la altura del árbol lo más baja posible para garantizar que las búsquedas, inserciones y eliminaciones se ejecuten siempre de forma rápida y eficiente.

## 2. Factor de balance

Es un indicador numérico que mide el equilibrio de cada nodo calculando la diferencia entre la altura de su hijo izquierdo y la de su hijo derecho. Para cumplir con el criterio de AVL, esta diferencia nunca debe pasar de uno en valor absoluto en ningún nodo del árbol.

## 3. Rotaciones e invariante BST

Las rotaciones son operaciones que reordenan los enlaces entre los nodos para equilibrar el árbol. Lo importante es que cambian la estructura física pero preservan intacto el orden de los datos, asegurando que los elementos a la izquierda de un nodo sigan siendo menores y los de la derecha sigan siendo mayores.

## 4. Casos LL RR LR RL

LL: El peso está en el extremo izquierdo. Se arregla con una sola rotación hacia la derecha sobre el nodo desbalanceado.

RR: El peso está en el extremo derecho. Se arregla con una sola rotación hacia la izquierda sobre el nodo desbalanceado.

LR: El peso está en el subárbol interno izquierdo. Requiere primero rotar a la izquierda el hijo izquierdo y luego rotar a la derecha el nodo principal.

RL: El peso está en el subárbol interno derecho. Requiere primero rotar a la derecha el hijo derecho y luego rotar a la izquierda el nodo principal.

## 5. Complejidad

Tiempo: Al mantener el árbol balanceado, el camino desde la raíz hasta las hojas es corto, por lo que buscar o insertar toma un tiempo logarítmico respecto al total de elementos. Las operaciones de rotación toman un tiempo constante por nivel, manteniendo la eficiencia general.

Espacio: Cada nodo gasta una cantidad mínima y fija de memoria extra para almacenar su propia altura, evitando tener que calcularla desde cero en cada operación.

## 6. Pruebas propias

Se programaron pruebas en el archivo de evaluación para validar los casos que el material base no revisaba. Se probó el comportamiento con un árbol completamente vacío, el control de elementos duplicados para evitar que rompan la estructura, y ejecuciones dirigidas para forzar de forma controlada cada uno de los cuatro tipos de rotaciones.

## 7. Revisión técnica recibida



## 8. Revisión técnica realizada



## 9. Pregunta abierta

¿Existirá algún beneficio real si permitimos que los nodos tengan un margen de desbalance un poco mayor antes de obligarlos a rotar, buscando reducir el número de rotaciones en inserciones masivas sin perder demasiada velocidad en las búsquedas?