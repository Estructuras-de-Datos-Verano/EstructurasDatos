
## Operación dominante y complejidad

El heap sirve para insertar y extraer el mínimo (o máximo). En una lista común, buscar el mínimo cuesta O(n) porque hay que recorrerla entera. El heap lo resuelve en O(log n) porque el árbol está balanceado y el camino máximo desde la raíz a las hojas es corto.

## FIFO vs prioridad.

FIFO atiende por orden de llegada. Esto no sirve en urgencias médicas o procesos del sistema operativo, donde un evento crítico posterior debe pasar al frente. La cola de prioridad ordena por la importancia o urgencia real del dato.

## BST/AVL vs heap.

Un BST o AVL impone un orden total estricto de izquierda a derecha para permitir búsquedas rápidas de cualquier dato. El heap solo impone un orden parcial vertical, diseñado exclusivamente para exponer el mínimo en la raíz.

## Propiedad min-heap.

Es un orden parcial y vertical: el padre siempre es menor o igual que sus hijos, pero los hermanos no tienen orden entre sí. Como el árbol se llena parejo, se guarda en un arreglo contiguo usando fórmulas fijas (2*i + 1 y 2*i + 2). Esto elimina el uso de punteros y optimiza la memoria caché.

## Representación por arreglo.

Al ser un árbol completo, se puede mapear directamente en una lista lineal en memoria usando fórmulas fijas: hijo izquierdo = 2*i + 1, hijo derecho = 2*i + 2. Esto elimina los punteros de memoria y optimiza el uso de la caché del procesador.

## Sift-up.

Se ejecuta al insertar un elemento al final del arreglo. El dato sube (burbujea) comparándose con su padre hasta que encuentra un padre menor o igual, o llega a la raíz (índice 0).

## Sift-down.

Se mueve el último elemento del arreglo a la cima (para no romper la estructura del árbol) y se le hace descender. Es obligatorio intercambiarlo siempre con el hijo menor; de lo contrario, se violaría la propiedad de min-heap en el subárbol vecino.

## Last Stone Weight.

El problema exige extraer los dos valores máximos. Se resuelve de forma óptima simulando un Max-Heap con nuestro HeapMin simplemente invirtiendo el signo de los datos (guardándolos en negativo) al entrar y salir.

## Pruebas propias.

Los tests en test_estudiante.py validaron el comportamiento de los bucles en escenarios donde los elementos debían subir o bajar múltiples niveles de forma consecutiva, asegurando que la reparación no se corte prematuramente.

## Revisión técnica.

SANTIAGO SALDIVAR

Todas las pruebas pasaron. Está muy bien implementado. Todo el código funciona y es claro.

## Relación con Dijkstra.

Este algoritmo necesita extraer iterativamente el vértice con la menor distancia acumulada. El heap almacena tuplas (distancia, vértice), permitiendo leer el mínimo en O(1) y extraerlo en O(log n), evitando que el algoritmo se vuelva lento en grafos grandes.

## Pregunta abierta: ¿qué operación haría preferible otra estructura?

"En Dijkstra, si cambia la distancia de un vértice que ya está dentro del heap, ¿cómo le haríamos para actualizar su prioridad en O(log n) sin tener que buscarlo en todo el arreglo con un bucle O(n)?"