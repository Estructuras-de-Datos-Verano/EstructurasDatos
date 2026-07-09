Santiago Saldívar Garcini

Un BST sólo será eficiente si está balanceado. De lo contrario, hará comparaciones excesivas. 
Si el BST no está balanceado, se parecerá a una lista en su ineficiencia. La lista es muy útil cuando se necesita guardar orden, pero es ineficiente al buscar. El BST busca resolver ese problema, pero si no se usa bien y no se aprovecha, no servirá de nada.
La altura es el máximo nivel. Es igual al número de comparaciones en el peor caso.
Cuando un árbol está balanceado, será eficiente. Los árboles degenerados parecerán listas, lo que los hace ineficientes para lo que se quiere.
El Orden de inserción es importante, porque define si estará o no balanceado. Debería empearce como por la mitad de los valores, e ir agregando chicos y grandes. Si se insertan en orden, no será balanceado.
Si es balanceado la complejidad es O(logn), si no, es O(n).
Los experimentos al respecto se pueden hacer fácilmente. Notamos en el código que el árbol degenerado es más lento. Eso se ve aun mejor en las animaciones.
Las pruebas, además de revisar que funcione todo bien, comparan el balance y el degenere, notando que el primero es más eficiente.
Agregué las pruebas:
    -test_agregado_1_balance_mas_eficiente, compara eficiencia.
    -test_agregado_2_altura_maxima, compara altura.
    -test_agregado_3_busqueda_degenerada, compara crecimiento.

Yo elegí el problema de la sitancia entre nodos, y es una muy buena forma de comparar el balance, porque aumenta dramáticamente si es degenerado.
¿Qué otros errores debo evitar con esta y otras estructuras de datos?