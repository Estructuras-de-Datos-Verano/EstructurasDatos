# Notebook - Clase 11 - jose Iván Reyna Blanco
## 1. Motivación
**Pregunta.** ¿Qué problema aparece cuando buscamos muchas veces en una lista? Se recorren todos los elementos uno por un y se compara si es el deseado cada vez.
## 2. Problemas relacionados
**Pregunta.** Elige uno de estos problemas y explica qué concepto de la clase parece practicar.
- 700 Search in a Binary Search Tree: Dado un árbol binario y un valor a buscar, éste problema pide explorar el árbol gasta llegar a un nodo cuyo valor sea el buscado y devolver el árbol "truncado" hasta el paso de ese nodo. Esto me recuerda a usar un algoritmo de búsqueda en un grafo, sea bfs y dfs, pero guardando un registro de estados como en la clase anterior y luego usar ese registro para reconstruir una copia truncada del árbol hasta ese nodo.
## 3. Conceptos básicos
**Pregunta.** Dibuja o describe un árbol con raíz, dos hijos y al menos una hoja. 
``` text
            [Raíz]
        /           \
    [Nodo1]         [Nodo2]
       | 
    [Hoja]
```
## 4. Árbol binario de búsqueda
**Pregunta.** ¿Por qué el invariante permite descartar una parte del árbol durante la búsqueda? Porque si todos los elementos de la izquierda son menores y de la derecha mayores solo me hace falta comparar con la raíz el valor buscado para saber de qué lado buscar. Es como si tuvieras la recta real y quieres encontrar visualmente a 3.28. Basta saber que es mayor que cero para no buscarlo a su izquierda. Entonces busco solo en la recta real *positiva*. 
## 5. Búsqueda
**Ejemplo manual.** En el árbol formado por `8, 4, 10, 2, 6, 9, 12`, busca `9`.
**Pregunta.** ¿Qué nodos comparas y qué parte descartas en cada paso? Tomo como raíz al 2 porque es el minimal. Como 9 es mayor que 2, lo busco a la derecha. Primer nodo recorrido es 4 entonces voy al siguiente. Segundo nodo es 6. Tercero es 8. Cuarto es 9 entonces detengo el proceso de búsqueda y devuelvo el árbol del lado derecho hasta aquí. 
## 6. Inserción
Valores de ejemplo:
```text
8, 4, 10, 2, 6, 9, 12
```
**Pregunta.** Inserta manualmente los valores del ejemplo y describe dónde queda cada uno. Dado que los valores de ejemplo proporcionados son exactamente los mismos que los del diccionario dado en el ejemplo manual, voy a simplemente considerar que ya tengo un árbol construido hasta el 9. Entonces tomo como único valor nuevo al 12 que es mayor a la raíz. Recorro nodos a la derecha como arriba hasta llegar al último que es 9 y menor a 12. Por lo tanto, inserto 12 como hoja.
## 7. Altura
**Pregunta.** ¿Qué relación hay entre altura y costo de búsqueda? Usando algoritmos como bfs o dfs, seguramente sea directamente proporcional la relación. Pero en realidad la relación es con la altura del nodo que se busca. Cada búsqueda es moverse entre los items de un diccionario accediendo al valor y eso tiene una complejidad temporal O(1). Si el nodo es de altura k, tenemos un "costo" temporal sumado de k*(O(1)) que nos da una complejidad O(k). Así que parece a priori ser lineal.
## 8. Recorridos
**Pregunta.** ¿Por qué inorden produce valores ordenados en un BST? Porque haciendo eso estás recorriendo los valores de menor a mayor, entonces mientras te asegures de desde el primer paso meter a la raíz e insertar el primer valor menor a la izquierda y el primer valor mayor a la derecha, solo queda en cada paso insertar a la izquierda o derecha (revisando correctamente donde deben insertarse) del nodo.
## 9. Animaciones
**Pregunta.** ¿Qué te ayuda a ver una animación que no se ve tan claro en una lista de valores? En mi caso particular diría que en nada porque me quedó claro como funciona el recorrido de un BST, pero si diría en general que permite visualizar con colores las comparaciones y el nodo actual.
## 10. Implementación
**Pregunta.** ¿Qué métodos parecen depender naturalmente de recursión? Los tres métodos de recorrido. Traté originalmente de hacerlo sin recursión para inorder traversal search, pero fue muy complicado y terminé usando IA. Al final me sugirió recursión, y aunque tarde clase y media en entenderlo bien, fue la implementación natural crear una función para recorrer nodos en el órden deseado.
## 11. Pruebas
Evita errores de importación: Agrega la carpeta de la entrega a la ruta. Esto asegura que los tests puedan encontrar e importar implementacion.py sin configurar rutas manualmente (lo que suele causar el clásico y frustrante error de "módulo no encontrado").

Validación previa: Verifica que el archivo implementacion.py realmente exista antes de intentar correr cualquier prueba.

Automatización: Ejecuta internamente el comando pytest -v para evaluar el código, unificando todo el proceso de calificación en un solo comando.
## 12. Patrón descubierto
## 13. Cierre