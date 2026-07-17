# Discusión técnica

## 1. ¿Un BST siempre es eficiente?
No, no siempre es eficiente. Si insertamos los datos en un orden que desbalancee el árbol, este pierde su forma ramificada y se vuelve tan lento como una lista común.

## 2. Lista vs BST
Una lista nos obliga a revisar elemento por elemento hasta encontrar lo que buscamos. Un BST, si está bien estructurado, nos permite descartar la mitad de los datos en cada paso, haciendo la búsqueda muchísimo más rápida.

## 3. Altura y comparaciones
La altura determina el camino más largo desde la raíz hasta las hojas. El número de comparaciones al buscar un elemento siempre estará limitado por esta altura, ya que no podemos visitar más nodos de los que hay en esa línea.

## 4. Árbol balanceado vs árbol degenerado
Un árbol balanceado distribuye sus nodos equitativamente a izquierda y derecha, manteniendo una altura baja y búsquedas rápidas. Un árbol degenerado crece hacia un solo lado como una línea recta, perdiendo todas sus ventajas de velocidad.

## 5. Orden de inserción
El orden en que metemos los datos decide la forma del árbol. Si los metemos mezclados o de forma alterna el árbol se mantendrá balanceado, pero si los metemos perfectamente ordenados (de menor a mayor o viceversa) se creará un árbol degenerado.

## 6. Complejidad
En el mejor de los casos (balanceado), el tiempo de búsqueda crece de manera logarítmica (muy lento y eficiente). En el peor de los casos (degenerado), el tiempo crece de forma lineal, directo con la cantidad de datos que tengamos.

## 7. Experimentos y evidencia
En nuestras pruebas con 10 elementos, el árbol balanceado solo necesitó un puñado de comparaciones para encontrar un valor. En cambio, el degenerado tuvo que recorrer prácticamente los 10 niveles, demostrando el impacto real del diseño.

## 8. Animaciones
Visualizar el árbol ayuda a entender inmediatamente cómo se desbalancea el camino de búsqueda. Ver los saltos que da el algoritmo entre nodos hace que el concepto de "descartar la mitad" sea mucho más claro que solo leer el código.

## 9. Pruebas propias
Diseñar mis propios tests me sirvió para darnme cuenta de detalles finos, como que el contador de comparaciones debe sumar la última visita justo al encontrar el nodo, asegurando que los números coincidan con el recorrido real.

## 10. Revisión técnica del PR
Durante la revisión noté que corregir un bug en un lado (como la altura del árbol) puede revelar fallas ocultas en otros métodos (como las comparaciones). Mantener el código limpio y los tests actualizados es clave para no arrastrar errores.

## 11. Problemas relacionados
El problema de encontrar el antecesor k-ésimo está directamente ligado a este tema. En un árbol balanceado, saltar hacia arriba es rápido porque la altura es corta, pero en uno degenerado, subir "k" niveles es tan lento y tedioso como retroceder uno por uno en una fila.

## 12. Pregunta abierta
¿Cómo podríamos diseñar un mecanismo de auto-balanceo simple que se active cada vez que insertamos un nodo, sin que reordenar el árbol sea más costoso que la búsqueda misma?