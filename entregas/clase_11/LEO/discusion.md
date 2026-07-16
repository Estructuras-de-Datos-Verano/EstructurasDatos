# Discusión técnica clase 11 - Leonardo Daniel Arenas Serafín

## 1. Lista vs árbol

La ventaja respecto al árbol sobre la lista es que la lista tiene un criterio de jerarquía muy débil, pues solamente es una secuencia de inserciones, mientras que el árbol establece una jerarquía mucho más profunda. De esta manera, el buscar un elemento en un árbol es mucho menos complejo que el buscarlo en una lista.

## 2. Motivación del BST

La motivación detrás del BTS es de qué forma podemos estructurar datos para que tengan una jerarquía.

## 3. Invariante

El aspecto invariante de un árbol es precisamente lo que le otorga esta jerarquía, pues por cada nodo, su subárbol izquierdo contiene valores menores y el derecho mayores. 

## 4. Inserción

Este método sigue la regla de la Invariante y además agrega la caracterísitca de que no sea posible agregar valores repetidos

## 5. Recorridos

Existen 3 recorridos básicos, los cuales priorizar qué lado del árbol se secuencía primero. El más natural es el inorder, pues devuelve los valores de menor a mayor. Y le preorder y postorder van más allá.

## 6. Altura y eficiencia

La altura de un árbol es el número máximo de niveles, de esta forma la complejidad correspondiente a la búsqueda de un valor es en el peor de los casos el número máximo de niveles, es decir, la altura. Esto porque por cada nivel exite una comparación que te guía por el camino del valor buscado.

## 7. Pruebas

De las 15 pruebas realizadas pasaron las 15, lo cual nos quiere decir que tanto la implementación como el diseño de los tests están bien hechos. Yo diseñé las siguientes pruebas TODO: test_todo_preorden(), test_todo_postorden(), test_todo_insercion_en_orden_creciente(), test_todo_repetido_no_aparece_dos_veces(). E implementé por mi propia cuenta las siguientes pruebas: test_todo_inorden_LEO(), test_valor_mayor_a_raiz_hijo_derecho_LEO(), test_valor_menor_a_raiz_hijo_izquierdo_LEO().

## 8. Cambio técnico: evaluar.py
Evaluar.py ofrece una solución a los problemas que hemos tenido anteriormente con la realización de los pytest. 


## 9. Problemas relacionados

Un problema relacionado que considero que los árboles serían muy útiles es el problema de CSES de Labrynth.  Ya que para poder llegar de punto A a punto B, bastaría simplemente con establecer la raíz como A y buscar el valor B para ver si es posible llegar, para posterioirmente calcular las alturas de las ramas que llegan a B y compararlas para encontrar el camino más corto.

## 10. Pregunta abierta

Hast ahora hemos visto como crear un árbol y como insertar valores, pero ¿cómo sería la implementación de elminar valores? ¿Que tan complicado sería hacer este proceso para conservar la estructura invariante del árbol?
