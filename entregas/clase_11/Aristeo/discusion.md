# Discusión técnica

## 1. Lista vs árbol

Una lista guarda los datos en secuencia, así que no hay forma de saber, sin revisarla, en qué región está un valor: buscar exige comparar contra los elementos uno por uno en el peor caso. Un árbol binario de búsqueda agrega estructura jerárquica más una regla de orden por nodo, y esa regla es justo lo que permite tomar una decisión de "izquierda o derecha" en cada paso y descartar una parte del espacio de búsqueda sin revisarla. La diferencia no es solo de forma de almacenamiento, sino de qué información queda disponible en cada punto de la estructura para guiar una decisión.

## 2. Motivación del BST

El BST resuelve el caso de uso de muchas consultas de existencia sobre datos ordenables: IDs, matrículas, claves, etc. Si los datos fueran estáticos y solo se necesitara construir la estructura una vez para muchas búsquedas, otras alternativas (por ejemplo un arreglo ordenado con búsqueda binaria) también servirían. La ventaja específica del BST frente a un arreglo ordenado es que permite inserciones intercaladas con búsquedas sin tener que desplazar elementos, algo costoso en un arreglo.

## 3. Invariante

El invariante que implementé es: para cada nodo, todos los valores del subárbol izquierdo son estrictamente menores que el valor del nodo, y todos los valores del subárbol derecho son estrictamente mayores. Decidí no permitir duplicados (si valor == nodo.valor, insertar simplemente no hace nada), en lugar de, por ejemplo, contarlos o guardarlos a un lado, porque la práctica lo pedía explícitamente y porque mantiene el invariante simple: cada valor aparece como máximo una vez en el árbol.

## 4. Inserción

insertar compara el valor nuevo contra el nodo actual y decide bajar a la izquierda o a la derecha, repitiendo el proceso hasta encontrar un hueco (None) donde colocar el nuevo nodo. Implementé esto de forma recursiva (_insertar_recursivo) porque cada subárbol es, en sí mismo, un árbol donde aplica exactamente la misma regla: el caso base es "no hay nodo, entonces aquí se inserta" y el caso recursivo es "hay nodo, entonces se decide un lado y se repite el proceso ahí". Una alternativa iterativa con un puntero que recorre el árbol también sería válida y evitaría la profundidad de la pila de llamadas en árboles muy degenerados, pero la version recursiva es más directa de leer y corresponde uno a uno con la definición del invariante.

## 5. Recorridos

Los tres recorridos comparten la misma estructura recursiva y solo cambian el momento en que se "visita" (se agrega a la lista de resultado) el valor del nodo actual respecto a sus dos llamadas recursivas:

- preorden: se visita el nodo antes de recorrer sus hijos (raíz, izquierda, derecha);
- inorden: se visita el nodo entre recorrer el hijo izquierdo y el derecho (izquierda, raíz, derecha);
- postorden: se visita el nodo después de recorrer ambos hijos (izquierda, derecha, raíz).

Inorden es especialmente importante en un BST porque, combinado con el invariante de orden, termina emitiendo los valores en orden ascendente: primero todo lo menor (subárbol izquierdo), luego el propio valor, y después todo lo mayor (subárbol derecho), y esa misma regla se cumple recursivamente en cada subárbol.

## 6. Altura y eficiencia

Seguí la convención de la clase: árbol vacío tiene altura 0, y un árbol con solo la raíz tiene altura 1. La altura importa porque acota el número de comparaciones que hace contiene o insertar en el peor caso, ya que ambas operaciones siguen un único camino desde la raíz. En un árbol balanceado la altura es del orden de log(n), así que las operaciones también lo son; en el peor caso (árbol degenerado, por ejemplo insertando datos ya ordenados), la altura crece hasta n y el BST pierde su ventaja frente a una lista.

## 7. Pruebas

Escribí siete pruebas en test_estudiante.py, cubriendo: árbol vacío, preorden y postorden en un árbol con varios niveles, altura de un árbol degenerado, búsqueda de un valor inexistente cerca de valores existentes, manejo de duplicados, y una mezcla de valores negativos y positivos. Elegí estos casos porque cada uno prueba una parte distinta del invariante o de la lógica de las operaciones, y no solo el camino más simple.

En este entorno no tuve acceso a `evaluar.py` ni a la carpeta de tests públicos del curso (`clase_11/tests`), así que ejecuté mis propias pruebas de forma manual para verificar mi implementación (ver `reporte_pytest.md` para el detalle).

## 8. Cambio técnico: evaluar.py

El cambio principal que introduce evaluar.py en este flujo es que los tests públicos ya no necesitan probar varias rutas de importación posibles: evaluar.py se encarga de agregar mi carpeta de entrega al PYTHONPATH antes de correr pytest -v, así que los tests pueden hacer directamente `from implementacion import ArbolBinarioBusqueda, Nodo`. Esto simplifica los tests públicos y hace explícito que la única fuente de verdad de mi entrega es mi propio implementacion.py.

## 9. Problemas relacionados

LeetCode 700 (Search in a Binary Search Tree) y 701 (Insert into a Binary Search Tree) son prácticamente el mismo ejercicio que "contiene" e "insertar". LeetCode 94, 144 y 145 (recorridos inorden, preorden y postorden) corresponden directamente a los tres métodos de recorrido. CSES "Subordinates" usa árboles con una estructura distinta (no necesariamente binaria ni de búsqueda), pero comparte la idea de recorrer una jerarquía recursivamente y combinar resultados de subárboles.

## 10. Pregunta abierta

Si tuviera que insertar una gran cantidad de datos que llegan ya ordenados, ¿cómo podría evitar que el árbol se degrade a una lista sin cambiar por completo la estructura de Nodp y como podría aplicarlo a un problema del día a día?