# Arturo Prudencio Bonilla - Notebook

## seccion 1

¿Qué operación domina en dos de estos escenarios?

    Elegeir que elemtno es la prioridad 

## seccion 2

¿Qué costo se repite si extraemos mínimos desde una lista sin ordenar?

    reordenar la lista para tener el minimo libre para sacarlos

## seccion 3

¿Cuándo sería incorrecto usar una cola FIFO?

    Cuando nuestro problema no nos pide que la prioridad este dada por la antiguedad de llegada de los datos

## seccion 4

¿Qué permanece estable después de insertar un valor?

    el minimo 


| Inserción | Arreglo después de sift-up | Intercambios | Mínimo |
| ---: | --- | ---: | ---: |
| 7 | 7 | - | 7 |
| 3 | 3 7 | 3 -> inicio | 3 |
| 9 | 3 7 9 | 9 -> final | 3 |
| 1 | 1 3 7 9 | 1 -> inicio | 1 |
| 6 | 1 3 6 7 9 | 6 entre 3 y 7 | 1 |
| 5 | 1 3 5 6 7 9 | 5 entre 3 y 6 | 1 |

## seccion 5

¿Por qué un heap no es un BST?

    Porque no mantiene el invariante de los BST 

## seccion 6

¿Los hermanos deben estar ordenados entre sí?

    no creo 

## seccion 7

¿Qué ventaja da esta forma para almacenar el árbol?

    guarda orden parcial

## seccion 8

Para `[2, 5, 4, 9]`, ¿qué valor está en el índice 2?

    4 

## seccion 9 

¿Cuáles son los hijos del índice 2?

     5 y 6

## seccion 10

¿Por qué no insertamos directamente en la raíz?

    para consrvar la forma completa

## seccion 11

¿Cuándo se detiene sift-up?

    se detiene si el valor catual es mayor al valor de su padre

## seccion 12

¿Por qué se mueve el último elemento?

    por el TDA shif-up

## seccion 13

¿Por qué debemos elegir el hijo menor?

    por el orden de la estructura

## seccion 14

¿Qué relación observas entre la celda del arreglo y el nodo resaltado?

## seccion 15

¿Qué elegirías para búsquedas arbitrarias y qué para extraer mínimos?

    AVL para busquedas y heap para extrar minimos

## seccion 16

¿Por qué sift-up y sift-down son logarítmicos?

    Porque deben recorrer la altura del arbol en su totalidad y ya conociamos esa complejidad y era logaritmica

## seccion 17

¿Cuál es la operación dominante y el resultado del ejemplo?

    Buscar maximos 

    [2, 4, 1, 1, 1]

## seccion 18

¿Qué error específico detecta una extracción con varios descensos?


## seccion 19

¿Qué debe incluir revision_nombre.md?

    criticas constructivas y comentariso utiles sobre la implementacion

## seccion 20

¿Qué guardaría la prioridad en Dijkstra?

    la menor distancia

## seccion 21

¿Qué criterio usarás para elegir una estructura en un problema nuevo?

    Que quiero optimizar 