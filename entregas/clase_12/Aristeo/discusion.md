# Discusión técnica

## 1. ¿Un BST siempre es eficiente?
No. La eficiencia de un Árbol Binario de Búsqueda (BST) no es una garantía estática de su estructura, sino una propiedad dinámica que depende directamente de su topología. Teóricamente, un BST promete búsquedas en tiempo logarítmico, pero esta promesa asume que el árbol se ramifica uniformemente. Si la estructura pierde simetría, la eficiencia se degrada progresivamente hasta perder toda ventaja algorítmica frente a estructuras lineales.

## 2. Lista vs BST
La diferencia fundamental radica en la explotación del invariante de orden. Una lista desordenada obliga a realizar una búsqueda secuencial exhaustiva porque carece de información predictiva sobre la posición de los datos. En contraste, un BST introduce una restricción jerárquica: para cualquier nodo N, todos los elementos en su subárbol izquierdo son menores que N y todos los del derecho son mayores. Esta propiedad de descarte condicional es la que permite segmentar el espacio de búsqueda en cada paso, siempre y cuando la topología del árbol lo permita.

## 3. Altura y comparaciones
Existe una correlación directa y estricta entre la altura de un árbol y el número de comparaciones en el peor caso. El camino crítico de una búsqueda (sea exitosa o fallida) se mide por la cantidad de aristas que se deben recorrer desde la raíz hasta un nodo hoja o una referencia nula. Cada cambio de nivel representa exactamente una comparación lógica. Por lo tanto, el número máximo de operaciones de comparación está estrictamente acotado por la función de altura del árbol: C_{max} = H.

## 4. Árbol balanceado vs árbol degenerado
* Árbol Balanceado: Distribuye de manera uniforme sus nodos entre los subárboles izquierdo y derecho. Su altura se minimiza óptimamente a un orden de log_2(n + 1), garantizando que cualquier camino hacia una hoja sea corto.
* Árbol Degenerado: Carece por completo de ramificación interna. Se presenta cuando todos los nodos (a excepción de la hoja terminal) poseen un único hijo. Visual y estructuralmente se transforma en una lista enlazada simple orientada diagonalmente, maximizando su altura hasta un orden de $n$.

## 5. Orden de inserción
El factor determinante que transforma un BST balanceado en uno degenerado es el orden cronológico en el que se introducen los datos. Si un conjunto de claves ya ordenadas (ascendente o descendente) se inserta de forma secuencial, cada nuevo elemento fallará sistemáticamente en la validación del invariante hacia un lado del nodo actual, anidándose de manera unireccional. La inserción ordenada anula la bifurcación y produce la degeneración máxima de la estructura.

## 6. Complejidad
Sostener de forma genérica que la complejidad de búsqueda en un BST es O(log n) es un error conceptual e incompleto. La notación Big-O debe discriminar escenarios topológicos:
* Caso Promedio / Balanceado: O(log n), debido a la subdivisión binaria del espacio de búsqueda.
* Peor Caso / Degenerado: O(n), ya que el algoritmo se ve forzado a realizar un recorrido lineal idéntico al de un arreglo unidimensional desordenado.

## 7. Experimentos y evidencia
Para validar estas afirmaciones de manera empírica, implementamos pruebas métricas que registran el comportamiento de la función `comparaciones_busqueda(valor)` bajo condiciones controladas:
1.  Evidencia de Altura: Insertar una secuencia ordenada de $n$ elementos genera un conteo exacto de nodos (`cantidad_nodos() == n`) y una medición de `altura() == n`, demostrando experimentalmente la mutación a estructura lineal.
2.  Evidencia de Búsqueda: La evaluación de consultas en el extremo inferior de árboles degenerados arroja un crecimiento de comparaciones con pendiente constante (lineal), mientras que en árboles con distribución balanceada, el incremento de comparaciones ante variaciones de tamaño de muestra sigue un comportamiento asintótico horizontal (logarítmico).

## 8. Animaciones
El análisis visual de las animaciones de inserción y búsqueda corrobora el comportamiento analítico del código. Se observa con claridad cómo en un BST balanceado el flujo de ejecución "salta" drásticamente entre niveles descartando volúmenes masivos de datos en milisegundos. En contraposición, las animaciones del modelo degenerado evidencian una marcha secuencial monótona nodo por nodo, acumulando comparaciones idénticas al costo de iterar sobre una lista enlazada tradicional.

## 9. Pruebas propias
Con el fin de garantizar la robustez de la implementación ante escenarios límite (edge cases), diseñamos pruebas complementarias orientadas a:
* Tratamiento de Duplicados: Validar que la reinserción de claves existentes no altere la consistencia del tamaño (`cantidad_nodos`) ni la altura calculada del árbol.
* Asimetría Inversa: Verificar que la inserción puramente decreciente (que produce un árbol degenerado estrictamente hacia la izquierda) sea reconocida correctamente por el método `es_degenerado()`.
* Consultas Fallidas Extreman: Medir el conteo de comparaciones cuando se busca un elemento inexistente en la base de un árbol balanceado, asegurando que la cota superior respete el límite de la altura.

## 10. Revisión técnica del PR
La metodología de integrar `tests_extra` en el script `evaluar.py` mitiga el sesgo de la prueba propia. Al inyectar la suite de pruebas del estudiante sobre el código fuente de otro desarrollador durante la revisión de un Pull Request, es posible descubrir vulnerabilidades lógicas o fallos de diseño que las pruebas públicas estandarizadas pasan por alto (tales como la gestión de referencias nulas o efectos secundarios en los punteros de los nodos).

## 11. Problemas relacionados
El dominio conceptual de la altura, balance e invariantes habilita la resolución de problemas avanzados en plataformas como LeetCode:
* LeetCode 110 (Balanced Binary Tree): Exige calcular recursivamente las alturas de subárboles para verificar que las diferencias de nivel no superen la unidad en ningún punto.
* LeetCode 98 (Validate Binary Search Tree): Requiere asegurar el cumplimiento del rango dinámico del invariante del BST en cada llamada recursiva, impidiendo desviaciones en la estructura.

## 12. Pregunta abierta
A la luz de lo analizado, surge una interrogante arquitectónica crítica para el diseño de software: Si un BST convencional es altamente vulnerable al orden de entrada de los datos, degradando su rendimiento de forma catastrófica en escenarios del mundo real, ¿cómo podemos garantizar búsquedas logarítmicas estables sin depender de la suerte del orden de inserción? Esto abre las puertas a la necesidad de implementar mecanismos de auto-balanceo dinámico en tiempo de ejecución, tales como las rotaciones en Árboles AVL o Árboles Rojo-Negro.