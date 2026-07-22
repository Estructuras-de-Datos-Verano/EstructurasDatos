1. Motivación¿Por qué un BST básico no garantiza por sí solo búsquedas rápidas? 
- Porque si los datos entran ordenados, el árbol se deforma convirtiéndose en una lista, perdiendo su eficiencia de búsqueda.

2. Degeneración¿Qué operación se vuelve costosa cuando el árbol se degenera? 
- La búsqueda de elementos, ya que pasa de un costo logarítmico a uno.

3. Altura y balanceSi un nodo tiene factor de balance 2, ¿hacia qué lado está cargado?

- Está cargado hacia el lado izquierdo, porque su subárbol izquierdo es más alto que el derecho.

4. Ingeniería inversa del algoritmo
¿Qué problema intenta resolver AVL? 
Evitar que el árbol se estire como una lista, manteniendo las operaciones en tiempo logarítmico .
¿Qué información extra debe recordar cada nodo?
Su propia altura actual para poder calcular los factores de balance.
¿Qué operación se repite después de insertar?
El cálculo del factor de balance y la actualización de alturas mientras se regresa hacia la raíz.
¿Qué propiedad debe conservarse aunque rotemos?
El invariante de BST (los menores a la izquierda y los mayores a la derecha)
.¿Cómo detectarías con papel y lápiz que hace falta una rotación?
Cuando calculas la diferencia de alturas de un nodo y el resultado es menor que -1 o mayor que 1.
Escribe pseudocódigo breve de inserción AVL.

Inserta como BST normal una flecha apuntando a la derecha Actualiza la altura del nodo otra flecha apuntando a la derecha Si hay desbalance, aplica la rotación correspondiente y retorna la nueva raíz.
 
 6. Caso LL¿Por qué el caso LL se corrige con rotación derecha? 
  Porque el peso extra está en el extremo izquierdo; rotar a la derecha baja el nodo actual y sube al hijo izquierdo como nuevo centro equilibrado.
 
 7. Caso RR¿Por qué el caso RR es simétrico al caso LL? 
  Porque el desbalance ocurre exactamente al revés, estando cargado en el extremo derecho, lo que requiere una rotación hacia la izquierda.

 8. Caso LR¿Qué pasaría si intentaras corregir LR con una sola rotación derecha?
   El árbol seguiría desbalanceado, ya que el nieto problemático simplemente cambiaría de lugar sin resolver la forma de zigzag ("<").

 9. Caso RL¿Cómo se refleja RL respecto a LR? 
  Es su reflejo exacto en espejo: el zigzag va en sentido opuesto (">") y requiere primero una rotación derecha seguida de una izquierda.

 11. Complejidad¿Qué costo adicional pagamos al insertar para conservar baja la altura?
   El tiempo extra que toma recalcular las alturas y ejecutar las rotaciones de punteros en el camino de regreso.

 13. notebook.md y discusion.md
 
 Escribe una diferencia concreta entre ambos documentos.  El notebook.md responde al cuestionario guiado de la clase, mientras que discusion.md justifica las decisiones de diseño técnico de tu código.
 
 14. Revisión técnica
 ¿Qué evidencia debe incluir una buena revisión técnica?  Debe incluir comentarios constructivos sobre el código del compañero, sugerencias de diseño y los resultados de las pruebas ejecutadas Cierre: Explica en una frase la idea central de AVL como decisión de diseño. 