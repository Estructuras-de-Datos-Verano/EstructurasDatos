# Notebook - Clase 13

## 1. Motivación

**Pregunta para `notebook.md`:** ¿por qué un BST básico no garantiza por sí solo búsquedas rápidas?

Porque un BST básico depende completamente del orden en el que entran los datos. El árbol no abre ramas y crece en línea recta hacia un solo lado.

## 2. Degeneración

**Pregunta para `notebook.md`:** ¿qué operación se vuelve costosa cuando el árbol se degenera?

La búsqueda, junto con la inserción y la eliminación

## 3. Altura y balance

**Pregunta para `notebook.md`:** si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?

Está cargado hacia el lado izquierdo.

## 4. Ingeniería inversa del algoritmo
Antes de escribir una sola línea de AVL, responde en `notebook.md`:

1. ¿Qué problema intenta resolver AVL?

Evitar la degeneración del árbol manteniendo la altura bajo control de manera automática, garantizando que el costo de las operaciones principales se mantenga siempre en O(log n).

2. ¿Qué información extra debe recordar cada nodo?

Cada nodo debe guardar un número entero extra que represente su altura actual (o directamente su factor de balance).

3. ¿Qué operación se repite después de insertar?

Se repite la actualización de alturas y el cálculo del factor de balance en cada nodo del camino de regreso hacia la raíz, aplicando rotaciones en donde se detecte un desbalance.

4. ¿Qué propiedad debe conservarse aunque rotemos?

El invariante del BST.

5. ¿Cómo detectarías con papel y lápiz que hace falta una rotación?

Contando los niveles de los subárboles de cada nodo de abajo hacia arriba. 

6. Escribe pseudocódigo breve de inserción AVL.

Función insertar(nodo, valor):
    Si nodo es nulo: Regresar NuevoNodo(valor)

    Si valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    Sino si valor > nodo.valor:
        nodo.derecho = insertar(nodo.derecho, valor)
    Sino:
        Regresar nodo // Duplicado, no se hace nada

    nodo.altura = 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))
    fb = balance(nodo)

    // Casos de desbalance y rotaciones
    Si fb > 1 y valor < nodo.izquierdo.valor:  Regresar rotar_derecha(nodo) (Caso LL)
    Si fb < -1 y valor > nodo.derecho.valor:  Regresar rotar_izquierda(nodo) (Caso RR)
    Si fb > 1 y valor > nodo.izquierdo.valor:
        nodo.izquierdo = rotar_izquierda(nodo.izquierdo)
        Regresar rotar_derecha(nodo) (Caso LR)
    Si fb < -1 y valor < nodo.derecho.valor:
        nodo.derecho = rotar_derecha(nodo.derecho)
        Regresar rotar_izquierda(nodo) (Caso RL)

## 6. Casos LL RR LR RL

**Pregunta para `notebook.md`:** ¿cómo se refleja RL respecto a LR?

Mientras que LR ocurre en el subárbol izquierdo porque metiste un nodo a la derecha de un hijo izquierdo, RL pasa en el subárbol derecho porque metiste un nodo a la izquierda de un hijo derecho.

**Pregunta para `notebook.md`:** ¿qué pasaría si intentaras corregir LR con una sola rotación derecha?

No se arreglaría el problema

**Pregunta para `notebook.md`:** ¿por qué el caso RR es simétrico al caso LL?

Porque ambos representan un desbalance lineal hacia un extremo

**Pregunta para `notebook.md`:** ¿por qué el caso LL se corrige con rotación derecha?

Porque el peso está en la izquierda y necesitas "bajar" el nodo superior hacia la derecha para que el nodo del medio (el hijo izquierdo) suba y tome el control como la nueva raíz equilibrada, nivelando ambos lados.

## 7. Complejidad

**Pregunta para `notebook.md`:** ¿qué costo adicional pagamos al insertar para conservar baja la altura?

El costo adicional es el tiempo que toma recalcular las alturas de los nodos visitados y ejecutar las rotaciones de punteros en el camino de regreso.

## 8. notebook.md y discusion.md

**Pregunta para `notebook.md`:** escribe una diferencia concreta entre ambos documentos.

El notebook funciona como una guía técnica o manual del código para entender la teoría y el funcionamiento del algoritmo paso a paso, mientras que el discusion es una bitácora de análisis para nosotros.


## 9. Revisión técnica

**Pregunta para `notebook.md`:** ¿qué evidencia debe incluir una buena revisión técnica?


## 10. Cierre

**Pregunta final para `notebook.md`:** explica en una frase la idea central de AVL como decisión de diseño.

AVL es la decisión de gastar un poco de esfuerzo extra reorganizando enlaces en cada inserción para garantizar que las búsquedas futuras sean siempre lo más rápidas posibles.