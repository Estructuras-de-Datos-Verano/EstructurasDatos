# Arturo Prudencio Bonilla

## seccion 1
    ¿por qué un BST básico no garantiza por sí solo búsquedas rápidas?

    Porque puede ser un arbol degenerado y con ello la complejidad de las busquedas se equipara a la de una lista O(n)

## seccion 2
    ¿qué operación se vuelve costosa cuando el árbol se degenera?

    la busqueda pues termina siendo lo mismo que en una lista

## seccion 3
     si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?
     
     a la izquierda

## seccion 4
1. ¿Qué problema intenta resolver AVL?

    la busqueda en arboles BST degenerados
2. ¿Qué información extra debe recordar cada nodo?

    la altura entre sus dos nodos hijos
3. ¿Qué operación se repite después de insertar?

    rebalansearse
4. ¿Qué propiedad debe conservarse aunque rotemos?

    debe seguir siendo un un arbol binario de busqueda (BST)
5. ¿Cómo detectarías con papel y lápiz que hace falta una rotación?

    Dibuja un árbol pequeño. Calcula el factor de balance de cada nodo (Altura Izquierda - Altura Derecha).

    Lo mismo que en codigo
6. Escribe pseudocódigo breve de inserción AVL.


## seccion 6
    ¿por qué el caso LL se corrige con rotación derecha?

    porque es el nodo que debe ser balanceado para que sea un BST

## seccion 7
    ¿por qué el caso RR es simétrico al caso LL?

    Porque el desbalance lo tomamos como desde la izquierda

## seccion 8
    ¿qué pasaría si intentaras corregir LR con una sola rotación derecha?

    queda desbalanceado, de hecho no cumple con la propiedad basica de BST
## seccion 9
    ¿cómo se refleja RL respecto a LR?

    Si LR es "bajar izquierda -> subir derecha"

    RL me hace sentido que sea "bajar-derecha ->subir izquierda"

## seccion 11

    ¿qué costo adicional pagamos al insertar para conservar baja la altura?

    el costo de rebalancear el arbol con cada insercion

# seccion 13
    escribe una diferencia concreta entre ambos documentos.

    Notebook debe de ser un archivo donde se responda parcialmente pero bien, mientras que en el de discusiones debemos contesta e indagar mucho mas en los conocimientos adquieridos y los detalles

# seccion 14
    ¿qué evidencia debe incluir una buena revisión técnica?

    debe tener respuestas profundas y que demuestren que el revisor se tomo el teimpo de enetnder el trabajo de su cumpañero revisado

# seccion 16
    En la necesidad de aumentar la eficiencia de busqueda en el caso mas vulnerable del arbol BST, AVL surgue como una opcion para recuperar el fuerte de BST a costo de una operacion mas internamente

