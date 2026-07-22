# Discusión clase 14 - José Iván Reyna Blanco

## 1. Operación dominante.
Las operaciones principales son insertar elementos y extraer el de mayor prioridad.
No es una estructura diseñada para buscar elementos específicos.

## 2. FIFO vs prioridad.
FIFO procesa el primero que llega, como una fila normal.
La cola de prioridad procesa primero al más "importante", sin importar cuándo llegó.
El Heap es la estructura ideal para implementar colas de prioridad.

## 3. BST/AVL vs heap.
Los BST/AVL ordenan todo para buscar rápido, pero consumen más memoria.
Los heaps solo ordenan verticalmente (padre e hijo) para sacar extremos rápido.
Además, los heaps usan arreglos simples en vez de punteros complejos.

## 4. Propiedad min-heap.
El nodo padre siempre tiene que ser menor o igual a sus hijos.
Esto asegura que la raíz del árbol siempre sea el valor más pequeño de todos.

## 5. Representación por arreglo.
El árbol se guarda por niveles en un arreglo continuo de izquierda a derecha.
El hijo izquierdo de "i" es "2i + 1" y el derecho es "2i + 2".
El padre de "i" siempre está en la posición "(i - 1) / 2".

## 6. Sift-up.
Se usa al insertar un elemento al final del arreglo.
Compara el nodo con su padre y los intercambia si rompe la regla del heap.
El nodo sube hasta que encuentra su posición correcta.

## 7. Sift-down.
Se usa al extraer la raíz y reemplazarla con el último elemento del arreglo.
Compara el nodo con sus hijos y lo intercambia con el más pequeño.
El nodo se hunde hasta que la propiedad del heap se restaure.

## 8. Complejidad.
Revisar el mínimo toma tiempo constante O(1).
Insertar o extraer un elemento toma tiempo logarítmico O(log n).
Construir todo el heap desde un arreglo toma tiempo lineal O(n).

## 9. Last Stone Weight.
Se resuelve metiendo todos los pesos en un Max-Heap.
Extraes las dos piedras más pesadas, las chocas y reinsertas la diferencia.
Repites el proceso hasta que quede una piedra o ninguna.

## 10. Pruebas propias.
Hay que verificar que la propiedad se cumpla tras muchas inserciones.
Validar casos límite como evaluar una raíz sin padre o extraer de un heap vacío.
Asegurar que no haya errores de índice al revisar hojas sin hijos.

## 11. Revisión técnica.
El mayor cuidado al programarlos es no desbordar los límites del arreglo.
Siempre hay que verificar que el índice de un hijo exista antes de consultarlo.
La raíz es el único nodo que no tiene padre y hay que ignorarlo en ciertas validaciones.

## 12. Relación con Dijkstra.
Dijkstra siempre necesita procesar el nodo más cercano disponible.
Un Min-Heap permite extraer esta distancia mínima de forma muy rápida.
Esto hace que el algoritmo de rutas sea eficiente en redes muy grandes.

## 13. Pregunta abierta: ¿qué operación haría preferible otra estructura?
Si necesitas buscar un valor específico o borrar un elemento cualquiera.
Ahí es mejor usar árboles como AVL porque el heap es muy lento para buscar.