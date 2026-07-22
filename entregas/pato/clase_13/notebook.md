# Clase 13: Notebook
#### Nombre: Patricio Navarro

## Motivación
¿Por qué un BST básico no garantiza por sí solo búsquedas rápidas?
    Porque en el peor de los caso, cuando el BST está degenerado, se comporta igual que una lista y ahí ya no haces búsquedas rápidas.

## Degeneración
¿Qué operación se vuelve costosa cuando el árbol se degenera?
    La búsqueda, porque tienes que revisar todos los nodos.

## Altura y balance
Si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?
    Está cargado a la izquierda.

## Ingeniería inversa del algoritmo
1. ¿Qué problema intenta resolver AVL?
    - Que el árbol siempre esté balanceado o lo más posible.
2. ¿Qué información extra debe recordar cada nodo?
    - Qué hijos tiene, y en que órden están.
3. ¿Qué operación se repite después de insertar?
    - Rebalancearse
4. ¿Qué propiedad debe conservarse aunque rotemos?
    - El inorden
5. ¿Cómo detectarías con papel y lápiz que hace falta una rotación?
    - Si el árbol no está balanceado y no tiene la estructura buscada.
6. Escribe pseudocódigo breve de inserción AVL.
    ```text
    def insertar(nodo, valor):
        inserción normal de BST
        nodo.altura = 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))

        factor_balance = altura(nodo.izquierdo) - altura(nodo.derecho)
        si factor_balance > 1 y valor < nodo.valor:
            regresar rotar_derecha(nodo)
        si factor_balance < -1 y valor > nodo.valor:
            regresar rotar_izquierda(nodo)
        si factor_balance > 1 y valor > nodo.izquierdo.valor:
            nodo.izquierdo = rotar_izquierda(nodo.izquierdo)
            regresar rotar_derecha(nodo)
        si factor_balance < -1 y valor < nodo.derecho.valor:
            nodo.derecho = rotar_derecha(nodo.derecho)
            regresar rotar_izquierda(nodo)
        
        regresar nodo

## Descubrimiento de las rotaciones
### Caso LL
1. ¿Qué observas que cambia en la forma del subárbol?
    - Sube el hijo de en medio y baja el padre para que quede balanceado
2. ¿Cómo se obtiene el factor `+2` del nodo 30?
    - Porque la altura del nodo 20 es `+1` y a eso le sumas la altura propia de cuando se crea el nodo 30 que es `+1`
3. ¿Por qué la corrección es una rotación derecha?
    - Porque es como si fijaras al dos como pivote y lo jalaras hacia arriba, entonces cae el padre y queda en la froma que queremos.
4. ¿Por qué el inorden debe ser `10, 20, 30` antes y después?
    - Porque el inorden siempre mantiene un orden creciente.
    
### Caso RR
1. ¿Qué parte del árbol permanece estable en el nivel 2?
    - Todos las ramas superiores, solo cambia el orden del nodo 75, 70 y 80.
2. ¿Por qué el factor de balance es negativo?
    - Porque los nodos están a la derecha.
3. ¿Por qué la corrección es una rotación izquierda?
    - Porque se hace la misma correccion pero ahora el desbalance ocurre desde el 10, entonces el lado que balanceas es el opuesto.
4. Comprueba el inorden antes y después de rotar.
    - Se mantiene igual.

### Caso LR
1. ¿Qué nodo ocupa la posición interior que obliga a usar dos pasos?
    - La tercer posición del sub árbol.
2. ¿Cuál es el factor del nodo 30 cuando se detecta LR?
    - `+2`
3. ¿Qué corrige la primera rotación y qué corrige la segunda?
    - La primera reordena el órden para que el 10 se conecte con 20 y 20 se conecte con 30, la segunda baja el nodo 30 a donde va.
4. Verifica el inorden en los tres estados de la tabla.
    - Todos son iguales.

### Caso RL
1. ¿En qué sentido RL es el espejo de LR?
    - Hace las mismas operaciones pero en sentido opuesto.
2. ¿Por qué el factor del nodo 10 es `-2`?
    - Porque tiene todos los nodos a la derecha.
3. ¿En qué orden se aplican las dos rotaciones?
    - Primero derecha, luego izquierda.
4. Explica por qué el inorden no cambia.
    - Primero porque no hay nodos a la izquierda entonces va a la raíz, luego baja al nodo de la izquierda  de su lado derecho y luego a la raíz de ese nodo.
    - En la segunda solo lo recorre en orden descendente y despúes vueve a hacer izquierda, raíz, derecha.

## BST vs AVL
¿En qué momento se separan claramente las alturas y qué trabajo adicional realiza AVL?
1. A partir del paso 3.
2. AVL realiza el trabajo extra de rotar y acomodar para que la forma del árbol siempre sea balanceada.

## Cuando no hace falta rotar
¿Por qué una rotación sería innecesaria e incluso confusa en este ejemplo?
    Porque los valores ya están dados en una secuencia que asgura que el árbol esté balanceado, si se rotara hasta balancearse solo terminarías en el mismo árbol.

## Varias rotaciones durante una secuencia
Identifica los casos que aparecen y explica por qué AVL se mantiene balanceado continuamente.
1. LL, LR, RL, RL, RR.
2. Porque en cada inserción hace rotaciones de ser necesario.

## Complejidad
¿Qué costo adicional pagamos al insertar para conservar baja la altura?
    Las rotaciones y guardar el estado de altura interno de cada nodo.

## Notebook vs Discusion
Escribe una diferencia concreta entre ambos documentos.
    Notebook son preguntas guiadas, discusión son nuestras interpretaciones y aprendizajes.

## Revisión Técncia
¿qué evidencia debe incluir una buena revisión técnica?
    Los resultados de las pruebas.

## Cierre
Explica en una frase la idea central de AVL como decisión de diseño.
    Mantener los árboles siemre balanceados para poder tener búsquedas optimizadas siempre.
    



    