## 1
- 1. ¿Un BST siempre es mejor que una lista? 
- no



## 2
- 1. Escribe un ejemplo donde buscar en una lista sea costoso y explica qué esperas que un BST mejore.
- por ejemplo en un recorrer una lista para encontrar un elemento y devolver no si este no esta es muy costoso para la lista, especialmente si la cardinalidad de la lista es muy grande. En este caso un BST mejoraria la optimización

## 3
- 3. ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?
- utiliza una desigualdad para ver que lado de la lista o arbol le dará prioridad

## 4
- 4. ¿Qué cambió: los datos o la forma del árbol?
- cambia la forma del arbol por que los datos no guardan la misma relación y recordemos que el ejemplo con incerción trata de desigualdades y entrada entrada nos se cumple

## 5
- 5. ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?
- por que te ayuda a cer la cantidad de nuodos y también con su relación entre ellos permite descartar algunos facilmente

## 6
- 6. Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.
- es una diagonal invertida que va hacia abajo y inserta valores decendientes

## 7
- 7. ¿Qué relación hay entre profundidad, altura y número de comparaciones?
- entre mas profundidad y altura, mas número de comparaciones

## 8
- 8. ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?
no por que como solo es una raiz unica no hay mas comparaciones

## 9
- 9. ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?
- muestra que es mas sencillo iterar un arbol degenerado que uno con varias raices 

## 10
- 10. ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?
- por que falta la variable de cantidad de datos, si esta es muy grande entonces si pero si es pequeñoa entonces no 
- 10. Elige uno y explica qué concepto de esta clase practica.
- usa un arbol donde el nodo hoja es el jefe y cada subordinado tiene a su vez otros subordinados y es un arbol balanceado
## 11
- 11. ¿Qué problema resuelve permitir tests_extra?

## 12
- 12. ¿Qué debe incluir un comentario técnico útil en el PR?
- constructividad ante todo

## 13
- 13. Explica el patrón con tus palabras.
- el parton es la forma en la que va a recorrer tu BST con ciertas regulaciones

## 14
- 14. ¿Un BST siempre es mejor que una lista?
- en algunos casos si
- 14. ¿Qué relación hay entre altura y comparaciones?
- entre mas profundidad y altura, mas número de comparaciones
- 14. ¿Cómo se degenera un BST?
- con solo una opción a considerar
- 14. ¿Qué evidencia experimental usarías para justificar tu respuesta?
- un arbol degenerado no tiene opciones entonces la BST suele fallar
- 14. ¿Qué problema relacionado practicarías después?
- un arbol degenerado con varias cosas y veria si el BST es mas eficiente que la lista
