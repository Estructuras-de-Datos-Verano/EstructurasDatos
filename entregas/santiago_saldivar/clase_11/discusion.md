### Discusión

Santiago Saldívar

La diferencia entre una lista y un árbol es la jerarquïa: la lsita meramente mantiene orden, el árbol relaciona los elementos, permitiendo, además de avanzar, elegir entre izquierda y derecha.

La motivación sería la búsqueda. En una lista, hay que comparar hasta con todos los elementos en el peor de los casos. En un árbol, como cada comparación implica descartar un trozo del árbol y no sólo ese nodo, se vuele mucho más eficiente.

El Invariante es muy útil, porque sirve de guía para la búsqueda. Menor, izquierda. Mayor, derecha. Éxito.

La isnerción le sigue a la búsqueda muy de cerca. En vez de detenerse, sin embargo, tran encontrar el elemento, lo agrega donde correspoda, comparando de la misma forma que hizo siempre.

Recorrer el árbol se logra como la búsqueda, comparando a cada paso. Es más eficiente que otras estructuras de datos.

La altrua es el largo de la rama más larga, o los niveles que tiene. Puede verse de ambas maneras. La eficiencia será igual, porque es el número de comparaciones necesarias.

Las pruebas fueron muy importantes, porque, si no se inserta correctamente un número, ya sea que se repita, o se vaya al lado equivocado, el árbol deja de funcionar.

El evaluar.py nos ayudó porque ahora el pytest busca archivos específicos, y no revisa a ver qué encuentra. Pero, al ser nuevo, fue más confuso.

Los problemas relacionas fueron interesantes. Yo elegí el de los subordinados del CSES. Aplica el árbol porque conserva jerarquía. Puede acomodarlos y hacer la cuenta.

¿Qué ventaja tiene un árbol binario sobre otr que no lo sea?

