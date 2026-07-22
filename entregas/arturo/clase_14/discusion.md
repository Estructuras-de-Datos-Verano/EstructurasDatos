# Discusion - Arturo Prudencio Bonilla

## Operación dominante.
    Para cada problema tenemos una operacion que repertiemos contsantemente, esta la denominamos operacione dominante a lo largo de esta clase, dependiendo de la naturaleza de esat operacion, definiremos nuestro pan de accion hacia el problema, pues seguramente sera la operacion que mas deberemos optimizar

## FIFO vs prioridad.
    Una cola regular (FIFO) valora las cosas basada en el tiempo de llegada, como la fila de un supermercado. Por otro lado, una cola de prioridad valora la urgencia o el peso, como la sala de urgencias de un hospital

## BST/AVL vs heap.
    BST/AVL siguen siendo mejores para busqueda de datos, pero por el otro lado heap es una estructura excelente para obtener minimos y tener los datos de una especifica

    De nuevo, cada una cumple una funcion que nos puede ayudar en algun problema o partde de alguno
## Propiedad min-heap.
    Es la regla estructural que hace que el montículo funcione: todo padre debe ser menor o igual a sus hijos. A diferencia de un BST donde el orden es estricto


## Representación por arreglo.
    Parece ser mas util o mejor optimizado a mayores niveles pues al eliminar los punteros hacia otros nodos, ahorramos mucha memoria
## Sift-up.
    Es el mecanismo de balance o reacomodo "de abajo hacia arriba". Cuando un elemento nuevo entra al final del arreglo, sift-up es el proceso mediante el cual este elemento se gana su lugar comparándose únicamente con sus ancestros directos
## Sift-down.
    Es el mecanismo de balance o reacomodo "de arriba hacia abajo" y el motor del método extraer_min. Al quitar el elemento de la raíz y poner una hoja en su lugar, sift-down restaura el orden dejando que el elemento "pesado" se hunda intercambiándose iterativamente con el menor de sus hijos; con esto nos ahorramos no tener que reordenar todo el arreglo desde cero
## Complejidad.
    El verdadero poder que veo del heap radica en su estructura de árbol balanceado, lo que garantiza una altura mínima. Esto permite que operaciones que normalmente tomarían tiempo lineal, como encontrar e insertar de manera ordenada, caigan a una complejidad de O(\log n)

## Last Stone Weight.
    es el ejemplo perfecto de cuándo usar esta estructura. Si intentáramos resolverlo ordenando una lista en cada turno, creo que el programa seria lentisimo

## Relación con Dijkstra.
    El algoritmo de Dijkstra depende de explorar constantemente el camino más corto disponible. El Min-Heap es el motor que hace esto posible a gran escala.
## Pregunta abierta: ¿qué operación haría preferible otra estructura?
    Si nuestra operación dominante se convirtiera en buscar un valor arbitrario específico, el Min-Heap sería ineficiente (tomaría tiempo O(n)), aqui mejor usamos un BST 