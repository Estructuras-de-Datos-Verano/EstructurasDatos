## 1. Motivación
**¿Por qué un BST básico no garantiza por sí solo búsquedas rápidas?**
Porque su estructura depende totalmente del orden en el que se insertan los elementos. Si los datos se insertan ya ordenados, el árbol se convierte en una estructura lineal (una lista enlazada), perdiendo la eficiencia de la búsqueda binaria.

## 2. Degeneración
**¿Qué operación se vuelve costosa cuando el árbol se degenera?**
La búsqueda (así como la inserción y la eliminación) se vuelve costosa, pasando de una complejidad logarítmica ideal de $O(\log n)$ a una complejidad lineal de $O(n)$.

## 3. Altura y balance
**Si un nodo tiene factor de balance `2`, ¿hacia qué lado está cargado?**
Hacia la izquierda. Esto se debe a que la convención de la fórmula es `altura_izquierda - altura_derecha` (por lo tanto, el subárbol izquierdo es 2 niveles más profundo que el derecho).

## 4. Ingeniería inversa del algoritmo
1. **¿Qué problema intenta resolver AVL?** La degeneración de los árboles binarios de búsqueda y el consecuente empeoramiento de los tiempos de búsqueda, asegurando que siempre se mantengan en $O(\log n)$.
2. **¿Qué información extra debe recordar cada nodo?** Su propia altura local dentro del árbol.
3. **¿Qué operación se repite después de insertar?** La actualización de la altura del nodo, el cálculo de su factor de balance y, si es necesario, una o más rotaciones.
4. **¿Qué propiedad debe conservarse aunque rotemos?** El invariante del BST (los nodos a la izquierda son menores, los de la derecha son mayores) y, por lo tanto, el recorrido inorden debe seguir entregando los elementos ordenados.
5. **¿Cómo detectarías con papel y lápiz que hace falta una rotación?** Restando la altura del hijo derecho a la altura del hijo izquierdo en cada nodo; si el valor absoluto de esa resta es mayor a 1 (es decir, $2$ o $-2$), hace falta rotar.
6. **Escribe pseudocódigo breve de inserción AVL:**
   ```text
   1. Insertar el nodo siguiendo las reglas normales de un BST.
   2. Actualizar la altura del nodo actual.
   3. Calcular el factor_balance = altura(izquierdo) - altura(derecho).
   4. Si balance > 1 y el valor insertado fue a la izquierda: aplicar rotación derecha (LL).
   5. Si balance < -1 y el valor insertado fue a la derecha: aplicar rotación izquierda (RR).
   6. Si balance > 1 y el valor insertado fue a la derecha: rotación izquierda en hijo y derecha en nodo (LR).
   7. Si balance < -1 y el valor insertado fue a la izquierda: rotación derecha en hijo e izquierda en nodo (RL).
   ```

## 6. Caso LL
**¿Por qué el caso LL se corrige con rotación derecha?**
Porque el exceso de nodos y altura se encuentra concentrado en la rama más externa izquierda. Al realizar un giro a la derecha, el hijo izquierdo se eleva para convertirse en la nueva raíz local y el nodo desbalanceado desciende a ocupar la posición de hijo derecho, nivelando el peso.

## 7. Caso RR
**¿Por qué el caso RR es simétrico al caso LL?**
Porque el desbalance se origina exactamente por el mismo fenómeno estructural pero en la dirección opuesta, acumulando el exceso de altura en el extremo derecho. Se corrige utilizando la operación inversa simétrica, que es la rotación izquierda.

## 8. Caso LR
**¿Qué pasaría si intentaras corregir LR con una sola rotación derecha?**
El árbol seguiría desbalanceado. Como el peso se encuentra en el "nieto" interno derecho, una rotación derecha directa simplemente trasladaría el problema de posición o mantendría la misma altura excesiva, sin resolver el quiebre en "zig-zag". Por ello, es obligatorio hacer una rotación izquierda previa en el hijo.

## 9. Caso RL
**¿Cómo se refleja RL respecto a LR?**
Se refleja como una imagen exacta en espejo. Mientras que el caso LR presenta un camino "izquierdo-derecho" y se soluciona rotando primero el hijo a la izquierda y luego la raíz a la derecha; el caso RL presenta un camino "derecho-izquierdo" y se resuelve con rotación derecha sobre el hijo y luego izquierda sobre la raíz.

## 11. Complejidad
**¿Qué costo adicional pagamos al insertar para conservar baja la altura?**
Pagamos un costo constante adicional de tiempo $O(1)$ en el retorno de cada llamada recursiva. Corresponde a la ejecución de operaciones aritméticas simples para actualizar la altura, comprobar el balance y reasignar punteros al rotar. La complejidad total sigue siendo $O(\log n)$.

## 13. `notebook.md` y `discusion.md`
**Escribe una diferencia concreta entre ambos documentos:**
`notebook.md` es un documento de trabajo de carácter pedagógico para responder preguntas conceptuales inmediatas, mientras que `discusion.md` es un reporte formal de arquitectura donde el desarrollador justifica su diseño técnico, analiza la eficiencia y evalúa su estrategia de pruebas.

## 14. Revisión técnica
**¿Qué evidencia debe incluir una buena revisión técnica?**
Debe incluir la salida exacta de las pruebas ejecutadas (como el reporte de errores de `pytest`), la identificación clara del impacto del fallo sobre el comportamiento esperado y una propuesta de solución explícita que guíe al autor.

## 16. Cierre
**Explica en una frase la idea central de AVL como decisión de diseño:**
El diseño AVL es una decisión estratégica donde se acepta pagar conscientemente un pequeño costo operativo en las inserciones para blindar la estructura y garantizar que las búsquedas sean siempre lo más rápidas y eficientes posibles bajo cualquier circunstancia.