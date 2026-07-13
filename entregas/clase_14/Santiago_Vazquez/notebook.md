## 1. Motivación

**Pregunta:** ¿Qué operación domina en dos de estos escenarios?

La operación dominante es elegir o extraer repetidamente el elemento con prioridad extrema (el mínimo o el máximo según el contexto).

## 2. Operación dominante

**Pregunta:** ¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?

Si se extraen mínimos desde una lista sin ordenar, se repite un costo de búsqueda lineal de O(n) en cada extracción.

## 3. Cola FIFO vs cola de prioridad

**Pregunta:** ¿Cuándo sería incorrecto usar una cola FIFO?

Sería incorrecto usar una cola FIFO cuando el orden de atención o procesamiento no deba depender del orden temporal de llegada, sino de una clave de urgencia o importancia (prioridad).

## 4. Descubrimiento manual

**Pregunta:** ¿Qué permanece estable después de insertar un valor?

Después de insertar un valor y realizar los intercambios necesarios, el resto de las ramas y posiciones del árbol permanecen estables; la reestructuración solo afecta al camino directo entre la posición insertada y la raíz.

## 5. Qué es un heap

**Pregunta:** ¿Por qué un heap no es un BST?

Un heap no es un BST porque mantiene un orden parcial (donde todo padre es menor o igual a sus hijos en un min-heap) en lugar de un orden total. No permite realizar recorridos completamente ordenados de manera directa ni optimiza la búsqueda de elementos arbitrarios.

## 6. Propiedad de min-heap

**Pregunta:** ¿Los hermanos deben estar ordenados entre sí?

No, los hermanos no deben estar ordenados entre sí. La propiedad de min-heap solo exige una relación de orden vertical jerárquico entre padres e hijos.

## 7. Árbol binario completo

**Pregunta:** ¿Qué ventaja da esta forma para almacenar el árbol?

Esta forma permite almacenar el árbol de manera compacta en un arreglo contiguo sin dejar huecos ni desperdiciar memoria, haciendo posible calcular las posiciones de padres e hijos mediante fórmulas aritméticas simples.

## 8. Representación por arreglo

**Pregunta:** Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?

En una indexación basada en cero, el valor ubicado en el índice 2 es 4 (ya que el índice 0 es 2, el índice 1 es 5 y el índice 2 es 4).

## 9. Fórmulas de índices

**Pregunta:** ¿Cuáles son los hijos del índice 2?

Aplicando las fórmulas para el índice i = 2:

Hijo izquierdo: 2x2 + 1 = índice 5
Hijo derecho: 2x2 + 2 = índice 6

## 10. Inserción

**Pregunta:** ¿Por qué no insertamos directamente en la raíz?

No se inserta directamente en la raíz porque se destruiría la forma del árbol binario completo y requeriría un desplazamiento masivo e ineficiente de los elementos. Insertar al final preserva la estructura completa y limita la reparación a un único camino.

## 11. Sift-up

**Pregunta:** ¿Cuándo se detiene sift-up?

## 12. Extracción del mínimo

**Pregunta:** ¿Por qué se mueve el último elemento?

Se mueve el último elemento a la raíz para preservar inmediatamente la condición de árbol binario completo. De esta forma, la única propiedad violada provisionalmente es la de orden jerárquico, la cual se repara fácilmente hacia abajo.

## 13. Sift-down

**Pregunta:** ¿Por qué debemos elegir el hijo menor?

Se debe elegir el hijo menor para asegurar que, al realizar el intercambio, el nuevo padre colocado sea menor o igual que ambos hijos, manteniendo así el invariante del min-heap de forma correcta.

## 14. Visualizaciones ipywidgets

**Pregunta:** ¿Qué relación observas entre la celda del arreglo y el nodo resaltado?

Existe una correspondencia directa biunívoca: cada celda del arreglo representa el valor almacenado exactamente en el nodo del árbol que comparte su mismo índice. Son dos vistas del mismo estado de la estructura.

## 15. Comparación BST, AVL y heap

**Pregunta:** ¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?

Elegiría un BST/AVL para búsquedas arbitrarias costo  y un min-heap para la consulta O(1) y extracción O(log n) de mínimos. 

## 16. Complejidad

**Pregunta:** ¿Por qué sift-up y sift-down son logarítmicos?

Son logarítmicos porque la altura de un árbol binario completo está acotada por O(log n), y ambas funciones mitigan o resuelven las violaciones operando exclusivamente a lo largo de un solo camino de dicha altura.

## 17. Last Stone Weight

**Pregunta:** ¿Cuál es la operación dominante y el resultado del ejemplo?

La operación dominante es la extracción del máximo (y posterior inserción de la diferencia). El resultado final del ejemplo provisto es 1.

## 18. Pruebas

**Pregunta:** ¿Qué error específico detecta una extracción con varios descensos?

Detecta fallas en la lógica de sift-down, específicamente el error común de no evaluar correctamente ambos hijos antes de decidir el intercambio o detener el descenso prematuramente antes de que se cumpla la propiedad de heap en niveles inferiores.

## 19. Revisión técnica

**Pregunta:** ¿Qué debe incluir `revision_nombre_revisor.md`?

Debe incluir la reproducción de los tests, una descripción de la evidencia encontrada, el reconocimiento de las fortalezas del código evaluado y propuestas de mejoras accionables para el autor.

## 20. Preparación para Dijkstra

**Pregunta:** ¿Qué guardaría la prioridad en Dijkstra?

Guardaría las distancias tentativas o candidatas más cortas conocidas desde el origen hacia cada uno de los vértices pendientes por procesar.

## 21. Cierre

**Pregunta:** ¿Qué criterio usarás para elegir una estructura en un problema nuevo?

El criterio fundamental consiste en analizar detenidamente los requisitos del problema para identificar cuál es la operación dominante y entonces elegir la estructura especializada que minimice su costo computacional.
