Santiago Saldívar

# Clase 13: Árboles AVL
**Pregunta inicial**
Si un BST puede convertirse en una lista, ¿cómo podemos impedirlo?
Asegurando que esté balanceado.

## 1. Motivación
**Pregunta para `notebook.md`:** ¿por qué un BST básico no garantiza por sí solo búsquedas rápidas?
Porque podría ser degenerado.

## 2. Degeneración
**Pregunta para `notebook.md`:** ¿qué operación se vuelve costosa cuando el árbol se degenera?
Buscar un elemento.

## 3. Altura y balance
**Pregunta para `notebook.md`:** si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?
Izquierda.

## 4. Ingeniería inversa del algoritmo

1. ¿Qué problema intenta resolver AVL?

El balance de los árboles.

2. ¿Qué información extra debe recordar cada nodo?

Su factor de balance.

3. ¿Qué operación se repite después de insertar?

El cálculo del factor de balance.

4. ¿Qué propiedad debe conservarse aunque rotemos?

El factor de balance.

5. ¿Cómo detectarías con papel y lápiz que hace falta una rotación?

Si dibujo un esquema y veo que hace más sentido al mover el papel.

6. Escribe pseudocódigo breve de inserción AVL.

Si el nodo es None, pues nadota

si el valor es menor, a la izquierda recursivamente
si es mayor, a la derecha recursivamente
si es igual, no lo agrega

balancea

Balance:
si está torcido a la izquierda y el hijo también, rota derecha 2 veces
si está torcido a la derecha y el hijo también, rota izquierda 2 veces
si está torcido a la izquierda y el hijo no, rota  derecha e izquierda
si está torcido derecha y el hijo no, rota izquierda y derecha

***

## 6. Caso LL

**Pregunta para `notebook.md`:** ¿por qué el caso LL se corrige con rotación derecha?

Porque preserva el recorrido inorden, y deja como raíz un elemento que haya estado en medio de la cadena.

¿Qué observas que cambia en la forma del subárbol?

Cambia la raíz pero permanecen las aristas.

¿Cómo se obtiene el factor +2 del nodo 30?

Porque tiene dos nodos a la izquierda, pero ninguno a la derecha.

¿Por qué la corrección es una rotación derecha?

Porque está desbalanceado a la izquierda.

¿Por qué el inorden debe ser 10, 20, 30 antes y después?

Porque el inorden los ordena.

## 7. Caso RR
**Pregunta para `notebook.md`:** ¿por qué el caso RR es simétrico al caso LL?

Porque hace lo mismo, pero al lado contrario.

¿Qué parte del árbol permanece estable en el nivel 2?
La raíz.

¿Por qué el factor de balance es negativo?
Porque tiene mucho a la derecha.

¿Por qué la corrección es una rotación izquierda?
Porque está torcido a la derecha.

Comprueba el inorden antes y después de rotar.
Se mantiene.

## 8. Caso LR

**Pregunta para `notebook.md`:** ¿qué pasaría si intentaras corregir LR con una sola rotación derecha?
No queda balanceado.

¿Qué nodo ocupa la posición interior que obliga a usar dos pasos?
El que los desbalancea.

¿Cuál es el factor del nodo 30 cuando se detecta LR?
1
¿Qué corrige la primera rotación y qué corrige la segunda?
Desbalance a la izquierda, desbalance a la derecha.
Verifica el inorden en los tres estados de la tabla.
Se mantiene.
## 9. Caso RL

**Pregunta para `notebook.md`:** ¿cómo se refleja RL respecto a LR?

Hace lo mismo, pero invirtiendo el orden de las rotaciones.

¿En qué sentido RL es el espejo de LR?
Mismas rotaciones, orden inverso.

¿Por qué el factor del nodo 10 es -2?
Porque tiene 2 nodos más a la izquierda que a la derecha.

¿En qué orden se aplican las dos rotaciones?
Derecha - izquierda.
Explica por qué el inorden no cambia.
Porque regresa los nodos en orden.

## 10. Comparación entre BST y AVL

Responde en notebook.md: ¿en qué momento se separan claramente las alturas y qué trabajo adicional realiza AVL? 
Se separan cuando aumentan los nodos. AVL los reorganiza correctamente.

## 11. Complejidad

**Pregunta para `notebook.md`:** ¿qué costo adicional pagamos al insertar para conservar baja la altura?


El de buscar dónde guardar.

Responde en notebook.md: ¿por qué una rotación sería innecesaria e incluso confusa en este ejemplo?

Porque ya está balanceado. Sería redundante.

## 12. Varias rotaciones durante una secuencia

Responde en notebook.md: identifica los casos que aparecen y explica por qué AVL se mantiene balanceado continuamente.

Se mantiene porque rota para que los nodos no tiendan demasiado en una dirección.

## 13. `notebook.md` y `discusion.md`
**Pregunta para `notebook.md`:** escribe una diferencia concreta entre ambos documentos.
Notebook responde las preguntas de la clase. Discusión es como platicar al respecto y sobre lo que aprendimos.

## 14. Revisión técnica
**Pregunta para `notebook.md`:** ¿qué evidencia debe incluir una buena revisión técnica?
El reporte de las pruebas.

## 16. Cierre
**Pregunta final para `notebook.md`:** explica en una frase la idea central de AVL como decisión de diseño.
El AVL es un árbol con rotación, que nos permite balancear un árbol sin cambiar las relaciones entre los nodos.


