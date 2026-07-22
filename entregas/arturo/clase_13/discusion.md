# Discusión técnica: Arturo Prudencio Bonilla

## 1. Problema que resuelve AVL
    Esta nueva estructura vista hoy resulve el problema de ayer, que un BST degenerado pierde toda su frotaleza frente a a operacion de busqueda, esto lo resuleve rebalanceando el arbol con cada insersion para que mantega siempre su propiedad de BST
## 2. Factor de balance
    Este parametro nos sirve para saber cuando un arbol esta segado a la izquierda o derecha y entorno a este decidimos como rotar el arbol para reordenarlo de forma que rcupere su invariante de BST
## 3. Rotaciones e invariante BST
    La rotaciones a como lo entendi, fija un punto desde el cula vamos a rotar y dependiendo el sentido, mueve a sus hijos o a uno de ellos para que el arbol se reacomodo y recupere sus propiedades de BST.

    Por ello en la seccion anterior mencione el invarinate, pues esas propiedades que facilitan la busqueda en BST (al menos en arboles balanceados) son las que queremso mantener en todos los casos
## 4. Casos LL RR LR RL
    - Caso LL (Izquierda-Izquierda): Ocurre cuando el desbalance es causado por una inserción en el subárbol izquierdo del hijo izquierdo. Se soluciona aplicando una única rotación a la derecha sobre el nodo desbalanceado.

    - Caso RR (Derecha-Derecha): Sucede cuando la inserción se realiza en el subárbol derecho del hijo derecho. Se corrige aplicando una única rotación a la izquierda sobre el nodo desbalanceado.

    - Caso LR (Izquierda-Derecha): Se presenta cuando el nuevo nodo se inserta en el subárbol derecho del hijo izquierdo. Requiere una rotación doble para corregirse: primero se aplica una rotación a la izquierda sobre el hijo izquierdo, y posteriormente una rotación a la derecha sobre el nodo original.

    - Caso RL (Derecha-Izquierda): Ocurre cuando la inserción recae en el subárbol izquierdo del hijo derecho. También necesita una rotación doble: primero una rotación a la derecha sobre el hijo derecho, y finalmente una rotación a la izquierda sobre el nodo desbalanceado.
## 5. Complejidad
    La principal ventaja de un árbol AVL frente a un Árbol Binario de Búsqueda (BST) tradicional radica en su mecanismo de rotaciones. Al mantener las diferencias de altura estrictamente controladas, el AVL garantiza que la altura del árbol nunca exceda un orden logarítmico respecto al número total de nodos. Esto evita el peor escenario de un BST simple, donde los datos ordenados pueden degenerar la estructura hasta convertirla en una lista enlazada.

    Es por eso que mi hipotesis a lo largo de esta clase fue que la complejidad se queda igual, O(logn) pues creo que el ajuste, o sea las rotaciones tienen complejidad O(1)

## 6. Pruebas propias
    EN mis pruebas verifique el caso LL y LR con un arbol sencillo y creado especificamente para ese comportamiento, a su vez verifique repeticion en la insercion y por ultimo verifique todas las propiedades generales del arbol

## 7. Revisión técnica recibida

## 8. Revisión técnica realizada

## 9. Pregunta abierta
    ¿Como se comportara el codigo con un arbol con muchos datos?