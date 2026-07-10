# Notebook - Clase 13

## 1. Motivación
Un BST básico no garantiza por sí solo búsquedas rápidas porque su estructura depende totalmente del orden en el que se insertan los elementos. Si los datos se insertan ya ordenados (ascendente o descendentemente), el árbol no se ramifica y se convierte en una estructura lineal (una lista enlazada), perdiendo la eficiencia de la búsqueda binaria.

## 2. Degeneración
Cuando el árbol se degenera, la operación de **búsqueda** (así como la inserción y la eliminación) se vuelve costosa, pasando de una complejidad logarítmica ideal de $O(\log n)$ a una complejidad lineal de $O(n)$.

## 3. Altura y balance
Si un nodo tiene un factor de balance de `2`, está **cargado hacia la izquierda**. Esto se debe a que la convención de la fórmula es `altura_izquierda - altura_derecha` (por lo tanto, el subárbol izquierdo es 2 niveles más profundo que el derecho).

## 4. Factor de balance (Ingeniería inversa del algoritmo)
1. **¿Qué problema intenta resolver AVL?** La degeneración de los árboles binarios de búsqueda y el consecuente empeoramiento de los tiempos de búsqueda, asegurando que siempre se mantengan en $O(\log n)$.
2. **¿Qué información extra debe recordar cada nodo?** Su propia altura local dentro del árbol.
3. **¿Qué operación se repite después de insertar?** La actualización de la altura del nodo, el cálculo de su factor de balance y, si es necesario, una o más rotaciones.
4. **¿Qué propiedad debe conservarse aunque rotemos?** El invariante del BST (los nodos a la izquierda son menores, los de la derecha son mayores) y, por lo tanto, el recorrido inorden debe seguir entregando los elementos ordenados.
5. **¿Cómo detectarías con papel y lápiz que hace falta una rotación?** Restando la altura del hijo derecho a la altura del hijo izquierdo en cada nodo; si el valor absoluto de esa resta es mayor a 1 (es decir, $2$ o $-2$), hace falta rotar.
6. **Pseudocódigo breve de inserción:**
   ```text
   1. Insertar el nodo siguiendo las reglas normales de un BST.
   2. Actualizar la altura del nodo actual.
   3. Calcular el factor_balance = altura(izquierdo) - altura(derecho).
   4. Si balance > 1 y el valor insertado fue a la izquierda: aplicar rotación derecha (LL).
   5. Si balance < -1 y el valor insertado fue a la derecha: aplicar rotación izquierda (RR).
   6. Si balance > 1 y el valor insertado fue a la derecha: rotación izquierda en hijo y derecha en nodo (LR).
   7. Si balance < -1 y el valor insertado fue a la izquierda: rotación derecha en hijo e izquierda en nodo (RL).

## 5. Rotaciones

Las rotaciones modifican de forma local los punteros entre un nodo padre, su hijo desbalanceado y un subárbol intermedio. Conservan el invariante del BST porque reubican los subárboles respetando sus cotas relativas: el subárbol intermedio que cambia de posición contiene elementos mayores al hijo que sube pero menores al padre que baja, manteniendo intacto el orden lógico del recorrido inorden.

## 6. Casos LL RR LR RL

* **¿Por qué el caso LL se corrige con rotación derecha?**
  Porque el exceso de nodos y altura se encuentra concentrado en la rama más externa izquierda (hijo izquierdo de un hijo izquierdo). Al realizar un giro a la derecha, el hijo izquierdo se eleva para convertirse en la nueva raíz local y el nodo desbalanceado desciende a ocupar la posición de hijo derecho, nivelando el peso de ambos lados de forma inmediata.

* **¿Por qué el caso RR es simétrico al caso LL?**
  Porque el desbalance se origina exactamente por el mismo fenómeno estructural pero en la dirección opuesta, acumulando el exceso de altura en el extremo derecho (hijo derecho de un hijo derecho). Se corrige utilizando la operación inversa simétrica, que es la rotación izquierda.

* **¿Qué pasaría si intentaras corregir LR con una sola rotación derecha?**
  El árbol seguiría desbalanceado. Como el peso se encuentra en el "nieto" interno derecho, una rotación derecha directa sobre el nodo crítico simplemente trasladaría el problema de posición o mantendría la misma altura excesiva en la subestructura, sin resolver el quiebre en "zig-zag". Por ello, es obligatorio hacer una rotación izquierda previa en el hijo para alinearlo en un caso LL puro antes de rotar a la derecha.

* **¿Cómo se refleja RL respecto a LR?**
  Se refleja como una imagen exacta en espejo. Mientras que el caso LR presenta un camino "izquierdo-derecho" y se soluciona rotando primero el hijo a la izquierda y luego la raíz a la derecha; el caso RL presenta un camino "derecho-izquierdo", resolviéndose mediante una rotación derecha sobre el hijo seguida de una rotación izquierda sobre la raíz desbalanceada.

## 7. Implementación

Para cumplir con la interfaz técnica sin duplicar código completo, la implementación delega la inserción a un método recursivo privado que devuelve la nueva raíz local balanceada. Métodos como `altura()` y `esta_balanceado()` se apoyan en funciones auxiliares que manejan los nodos `None` de forma segura, asignándoles una altura de 0 y un factor de balance de 0 para evitar errores de ejecución durante los recorridos.

## 8. Complejidad

* **Pregunta del cuaderno:** ¿Qué costo adicional pagamos al insertar para conservar baja la altura?
  Pagamos un costo constante adicional de tiempo $O(1)$ en el retorno de cada llamada recursiva. Este costo extra corresponde a la ejecución de operaciones aritméticas simples para actualizar el campo de altura, comprobar el factor de balance y reasignar un máximo de tres o cuatro punteros de memoria cuando se ejecutan las rotaciones. La complejidad asintótica total se mantiene óptima en $O(\log n)$.

## 9. Pruebas

El conjunto de pruebas públicas se enfoca en validar que los estados mínimos del árbol (vacío y con pocos elementos) funcionen, que los cuatro casos de rotación reestructuren la raíz de manera correcta, y que los valores duplicados no alteren la estructura. Las pruebas del estudiante extienden este alcance validando la estabilidad ante secuencias largas de inserciones y la preservación del recorrido inorden bajo escenarios de balanceo sucesivo.

## 10. Revisión técnica

* **Pregunta del cuaderno:** ¿Qué evidencia debe incluir una buena revisión técnica?
  Debe incluir la salida exacta o traza de las pruebas ejecutadas (como el reporte de errores de `pytest`), la identificación clara del impacto del fallo sobre el comportamiento esperado del código (por ejemplo, pérdida del invariante de balance o punteros huérfanos) y una propuesta de solución explícita orientada a la lógica que guíe al autor del código de manera constructiva.

## 11. Discusión

* **Diferencia concreta entre ambos documentos:**
  `notebook.md` es un documento de trabajo de carácter pedagógico diseñado para asimilar y responder preguntas conceptuales inmediatas sobre el algoritmo, mientras que `discusion.md` es un reporte formal de arquitectura de software en el cual el desarrollador justifica el diseño técnico de su solución, analiza la eficiencia asintótica y evalúa críticamente su estrategia de pruebas.

* **Idea central de AVL como decisión de diseño:**
  El diseño de un árbol AVL es una decisión estratégica donde se acepta pagar de forma consciente un pequeño costo operativo de procesamiento y memoria en las fases de escritura (inserción) para blindar y garantizar que los accesos y lecturas (búsquedas) sean siempre lo más rápidos y eficientes posibles bajo cualquier circunstancia.
    
