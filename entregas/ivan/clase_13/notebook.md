# Notebook - Clase 13

## 1. Motivación

**Pregunta para `notebook.md`:** ¿por qué un BST básico no garantiza por sí solo búsquedas rápidas? Porque si el BST es muy grande y además degenerado, en el peor de los casos dónde el valor buscado esté en el último nodo, tendremos que hacer n+1 comparaciones y n búsquedas donde n es el tamaño de nodos.

## 2. Degeneración

**Pregunta para `notebook.md`:** ¿qué operación se vuelve costosa cuando el árbol se degenera? La búsqueda de un elemento pues hay que recorrer todos los nodos y comparar con todos más la raíz.

## 3. Altura y balance

**Pregunta para `notebook.md`:** si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado? En este ejemplo, a la izquierda. Pero es absurdo calcularlo así porque en un BST lo que está a la derecha de la raíz es mayor. No tiene sentido decir cargado a la izquierda cuando la diferencia es 2 porque todos los elementos son menores a la izquierda y hay más elementos menores que mayores. 

## 4. Factor de balance

1. ¿Qué problema intenta resolver AVL? El costo de explorar árboles degenerados en su totalidad mediante el balanceo del árbol.
2. ¿Qué información extra debe recordar cada nodo?  Qué hijos tiene, y en que órden están.
3. ¿Qué operación se repite después de insertar? Rebalancear. 
4. ¿Qué propiedad debe conservarse aunque rotemos? El órden invariante en BST. 
5. ¿Cómo detectarías con papel y lápiz que hace falta una rotación? Si el árbol no está balanceado, poniendo el lapiz en horizontal y viendo que una rama tiene una hoja en el segundo nivel encima (o más arriba) del lápiz.
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
```
## 5. Rotaciones

¿ Qué tengo que poner aquí ? Ni siquiera coincide el órden del notebook con el de la estructura sugerida. Tampoco hay instrucciones claras.

## 6. Casos LL RR LR RL

1. ¿Qué observas que cambia en la forma del subárbol? Sube el hijo de en medio y baja el padre para que quede balanceado
2. ¿Cómo se obtiene el factor `+2` del nodo 30? La altura del nodo 20 es `+1`, le sumas la altura propia de cuando se crea el nodo 30 que es `+1`
3. ¿Por qué la corrección es una rotación derecha? Porque tienes una degeneración en el subárbol local formado por el nodo 20 como raíz. Como tienes una carga de dos niveles a la izquierda, se reinserta el 10 como hijo derecho de 20. 
4. ¿Por qué el inorden debe ser `10, 20, 30` antes y después? Porque mantiene un órden creciente

1. ¿Qué parte del árbol permanece estable en el nivel 2? Todos las ramas superiores, solo cambia el orden del nodo 75, 70 y 80.
2. ¿Por qué el factor de balance es negativo? Porque los nodos están a la derecha. Porque ahora el desbalance ocurre a partir del 10, entonces el lado que balanceas es el opuesto.
3. ¿Por qué la corrección es una rotación izquierda? Análogo a la anterior explicación.
4. Comprueba el inorden antes y después de rotar. Igual. Creciente.

1. ¿Qué nodo ocupa la posición interior que obliga a usar dos pasos? La tercer posición del sub árbol.
2. ¿Cuál es el factor del nodo 30 cuando se detecta LR? +2
3. ¿Qué corrige la primera rotación y qué corrige la segunda? La primera reordena el árbol: 10 - 20 - 30, la segunda baja el nodo 30 como hoja.
4. Verifica el inorden en los tres estados de la tabla. Todos son iguales.

1. ¿En qué sentido RL es el espejo de LR? Hace las mismas operaciones pero en sentido opuesto.
2. ¿Por qué el factor del nodo 10 es `-2`? Porque tiene todos los nodos a la derecha.
3. ¿En qué orden se aplican las dos rotaciones? Primero derecha, luego izquierda.
4. Explica por qué el inorden no cambia. No cambia en ningún caso porque las rotaciones mueven un subárbol desbalanceado de la siguiente forma:
- Se toma un segmento Padre, hijos.
- Raíz se convierte en hijo izquierdo o derecho dependiendo de si es menor o mayor que el nodo anterior.
- Si está balanceado, termina.
- Si no, nuevo segmento y se repite.
Al explorar el árbol izq-nodo-derecha el órden no va a cambiar.

## Número quién sabe cuál porque no coincide el órden.

**Responde en `notebook.md`:** ¿en qué momento se separan claramente las alturas y qué trabajo adicional realiza AVL?  A partir del paso 3. AVL hace el trabajo adicional de balancear el árbol(sorpresa).

## 7. Implementación

Nuevamente, ***no coincide el órden y tampoco hay instrucciones de qué poner aquí.*** 

## 8. Complejidad

## 9. Pruebas
## 10. Revisión técnica
## 11. Discusión