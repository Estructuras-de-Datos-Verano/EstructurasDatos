# Discusión técnica - Leonardo Daniel Arenas Serafín

## 1. Problema que resuelve AVL
Resuelve el problema de poder tener un mucho mayor control a la hora de buscar tener árboles balanceados y no degenerados. Tenemos mayor orden

## 2. Factor de balance
El factor que permite el balance es mantener que la altura de los subárboles de cada nodo no tenga una diferencia importante.

## 3. Rotaciones e invariante BST
Las rotaciones permiten que las raíces no se muevan para mantener un orden de menores y mayores, pero se mueven sus hijos para tener un orden muchom más profundo

## 4. Casos LL RR LR RL
Dependiendo del desbalance y de la inclinación de cada subárbol se realizan rotaciones que permiten llegar balance fácilmente 

## 5. Complejidad
Esta estructura busca que las operaciones de búsqueda de elementos dentro de ésta misma tienda a ser logarítmica, pues por cada nivel, los hijos crecen de manera exponenical uniformemente, permitiendo un descarte proporcionalmente logarítmico

## 6. Pruebas propias
Yo implementé las siguientes pruebas: test_rotacion_ll_LEO(), test_rotacion_lr_LEO, test_busqueda_LEO(). Buscan verificar que las rotaciones funcionen como se espera.

## 7. Revisión técnica recibida


## 8. Revisión técnica realizada


## 9. Pregunta abierta
Hasta ahora solo hemos trabajado con enteros, pero ¿cómo se podría implementar las estructuras de BST y AVL con otro tipo de valores?