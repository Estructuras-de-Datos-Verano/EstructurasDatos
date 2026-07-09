# Discusión técnica

## 1. Lista vs árbol
Buscar en una lista es como buscar un nombre leyendo un directorio página por página; es lento. Un árbol nos permite buscar descartando mitades enteras del problema a la vez, haciéndolo mucho más rápido.

## 2. Motivación del BST
El objetivo principal era resolver el problema de la lentitud. Necesitábamos una estructura que nos dejara guardar muchos datos y encontrarlos casi al instante sin tener que revisarlos todos uno por uno.

## 3. Invariante
Es la regla de oro que mantiene todo en orden: para cualquier número, los que son más pequeños se guardan a su izquierda y los que son más grandes a su derecha. 

## 4. Inserción
Para agregar un número nuevo, simplemente seguimos la regla de oro empezando desde arriba. Si es menor, vamos a la izquierda; si es mayor, vamos a la derecha, hasta que encontramos un espacio vacío donde colocarlo.

## 5. Recorridos
Son las diferentes formas de "pasear" por el árbol para leer sus datos. El más útil es el recorrido *Inorden* porque, gracias a la regla de oro, nos devuelve todos los números ya ordenados de menor a mayor.

## 6. Altura y eficiencia
La altura es la cantidad de "pisos" que tiene el árbol. Si el árbol está equilibrado (bajito y ancho), buscar es rapidísimo. Si metemos los datos ya ordenados, el árbol se vuelve una sola línea larga y buscar vuelve a ser tan lento como en una lista normal.

## 7. Pruebas
Las pruebas son como un filtro de seguridad. Nos sirven para comprobar automáticamente que el árbol no rompa su regla de oro, que no acepte datos repetidos y que acomode todo donde debe ir.

## 8. Cambio técnico: evaluar.py
Es una pequeña herramienta que automatiza las pruebas. En lugar de ejecutar comandos largos a mano, este archivo busca nuestro código y lo revisa por nosotros de forma rápida y directa.

## 9. Problemas relacionados
Esta estructura no solo sirve para números. Se puede usar en problemas de la vida real que tienen jerarquías, como organizar empleados y jefes en una empresa, o crear sistemas de búsqueda rápida.

## 10. Pregunta abierta
Si esta estructura es tan rápida y eficiente, ¿por qué no la usamos siempre en lugar de las listas normales? ¿Vale la pena el esfuerzo extra de programar un árbol si solo vamos a guardar 5 o 10 datos?