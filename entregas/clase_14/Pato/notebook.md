# Clase 14: Notebook
#### Nombre: Patricio Navarro

## Motivación
¿Qué operación domina en dos de estos escenarios?
- Asignar un valor a cada elemento y que el de mayor jerarquía salga primero.

## Operación Dominante
¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?
- Que se tien que buscar al elemento y compararalo con los demás para ver que sí sea el mínimo.

## Cola FIFO vs Cola de prioridad
¿Cuándo sería incorrecto usar una cola FIFO?
- Por ejemplo en una sala de urgencias, donde puede que primero llegó una persona cuya vida no peligra y después una cuya vida sí, entonces se debeatender primero a la segunda.

## Descubrimiento manual
Con la secuencia `7, 3, 9, 1, 6, 5` completar:

| Inserción | Arreglo después de sift-up | Intercambios | Mínimo |
| ---: | --- | ---: | ---: |
| 7 | [7] | 0 | 7 |
| 3 | [3, 7] | 1 | 3 |
| 9 | [3, 7, 9] | 0 | 3 |
| 1 | [1, 3, 7, 9] | 3 | 1 |
| 6 | [1, 3, 6, 7, 9] | 2 | 1 |
| 5 | [1, 3, 5, 6, 7, 9] | 3 | 1 |

¿Qué permanece estable después de insertar un valor?
- Los elementos del arreglo, y que está ordenado de menor a mayor.

## Qué es un heap
¿Por qué un heap no es un BST?
- Porque la relación del padre con los hijos no es estricta y no hay ninguna relación entre el hijo izquierdo y el derecho (osea que el izquierdo puede ser mayor que el derecho y no hay problema). Por lo mismo, el heap debe estar balanceado siempre.

## Propiedad de Min-Heap
¿Los hermanos deben estar ordenados entre sí?
- No, justo por lo que se dijo en la sección anterior.

## Árbol binario completo
¿Qué ventaja da esta forma para almacenar el árbol?
- Que nunca se degrada, por lo que buscar e insertar elementos es O(log(n)).

## Representación por arreglo
Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?
- Suponiendo que los índices empiezan en 1, el `5` estaría en la posición 2.
- Si empezara en 0, sería el `4`.

## Fórmulas de índices
¿Cuáles son los hijos del índice 2?
- Las posiciones 5 y 6.

## Inserción
¿Por qué no insertamos directamente en la raíz?
- Para conservar la forma completa.

## Sift-up
¿Cuándo se detiene sift-up?
- Cuando el valor actual es mayor o igual a su padre.

## Extracción del mínimo
¿Por qué se mueve el último elemento?
- Por el órden en el que insertamos y porque una vez que extraes el mínimo, osea la raíz te queda un hueco hasta arriba, pero si promovieras a uno de los hijos eso dejaría otro hueco en el árbol que se tendría que llenar haciendo así una reacción en cadena donde puede que el árbol quede con un hueco. En cambio si mueves al último ya no tienes ese problema.

## Sift-down
¿Por qué debemos elegir el hijo menor?
- Para mantener la estructura de `Min-Heap`. Porque al mover el último elemento hasta arriba pues en teoría ese debería ser el mínimo, pero es posible que no lo sea entonces lo vamos intercambiando con sus hijos y al final no quedan huecos y este va a quedar en su lugar correspondiente.

## Visualizaciones ipywidgets
**Actividad:** selecciona “Inserción: varios intercambios”. Antes de presionar Siguiente, predice qué intercambio ocurrirá y justifícalo con índices.
1. Se va a intercambiar el `1` con el `4`, eso es intercambiar las posiciones 6 y 2, eso es que en el arreglo quede `[2, 5, 1, 9, 8, 7, 4]`.
2. Se va a intercambiar el `1` con el `2`, eso es intercambiar las posiciones 0 y 2, entonces el arreglo queda `[1, 5, 2, 9, 8, 7, 4]`. 

¿Qué relación observas entre la celda del arreglo y el nodo resaltado?
- Que la celda del arreglo no hace los cambios uno por uno, si no que hace una relación entre los dos nodos que están conectados y los intercambia directamente. Como si tuvieran una referencia o un apuntador el uno al otro.

## BST vs AVL vs Heap
¿Qué estructura elegirías para cada escenario y qué operación justifica tu decisión?
- Escenario A: AVL, porque quieres buscar y recorrer ordenadamente el árbol.
- Escenario B: Heap, porque quieres ordenarlos por el tiempo que toma y de menor a mayor.

¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?
- Para búsquedas arbitrarias: AVL
- Para extraer mínimos: Min-Heap

## Complejidad
¿Por qué sift-up y sift-down son logarítmicos?
- Porque recorren la altura completa del árbol.

## Last Stone Weight
¿Cuál es la operación dominante y el resultado del ejemplo?
- El sift-down para ordenar todo y el resultado debe ser 0.

## Pruebas
**Pregunta adicional:** Diseña, sin escribir todavía el código completo, una entrada que obligue a `_bajar` a elegir el hijo derecho y explica qué afirmaciones comprobarías.
- Usar `[50, 30, 15]` debe obligar a ir por el hijo derecho porque es el valor maschiquito de todos. 
- Afirmaciones:
    - Que el minimo sea ahora el `15`.
    - Que el `30` se haya quedado como hijo izquierdo.
    - Que se siga cumpliendo la propiedad de heap.

¿Qué error específico detecta una extracción con varios descensos?
- Que sí esté recorriendo todos los valores y acomodándolos de manera correcta.

## Revisión técnica
¿Qué debe incluir `revision_nombre_revisor.md`?
- Su reporte de pruebas, comentarios para mejorar u optimizar, si hubo errores, conclusiones.

## Dijkstra
¿Qué guardaría la prioridad en Dijkstra?
- Las distancias tentativas.

## Cierre
¿Qué criterio usarás para elegir una estructura en un problema nuevo?
- Qué comportamiento me interesa conservar en mi solución del problema.

