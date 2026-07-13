La operación dominante será encontrar un mínimo o máximo, según el caso. La diferencia principal con FIFO es que FIFO elige por anitgüedad. En esta, eso no es relevante. La prioridad se define distinto. Un BST o AVL es bueno para búsqueda arbitraria. Un heap encuentra mínimos. Depende del caso cuál es más útil. Un heap se puede representar como un arreglo, pero también se puede ver como una estructura similar a un árbol BST.
Shift-up significa subir un elemento que sea menor que el padre, porque va en orden ascendente. Shift-down es lo contrario. Baja elementos.
La complejidad de exztraer un mínimo es O(1), de insertar es O(log n), de extraer es O(log n).
Last stone weight es un ejemplo muy bueno, porque sigue agregando elementos, pero sólo elije los máximos. 
Mir pruebas verifican, como suelo hacer, que se comporte correctamente según se agregan elementos.
*** revisión técnica. Modifica el compañero
Se relaciona con Dijkastra porque éste busca rutas más cortas, que es equivalente a buscar un mínimo. 
Pregunta abierta: ¿qué operación haría preferible otra estructura?
Sacar elementos por antigüedad.