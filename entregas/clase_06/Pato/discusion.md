# Clase 07: Discusión
#### Nombre: Patricio Navarro

## 1. Problema y primera idea.
Encontrar los valores más chicos a la izquierda de cada número en un arreglo y poner su posición en una lista.
## 2. Por qué la solución ingenua repite trabajo.
Porque debe recorrer todos los números anteriores a cada dato del arreglo, haciendoq ue el peor de los casos ea `O(n^2)`
## 3. Información útil e información descartable.
Información descartable son todos los valores anteriores mayores o iguales al actual, pues realmente no nos aportan nada, la útil es lo contrario.
## 4. Elección de estructura.
Una pila, esto porque el comportamiento para conocer el mínimo por así decirlo en cada iteración de los números tenía un comportamiento LIFO.
## 5. Variante: Nearest Greater Values.
Es un caso análogo a NSV, lo único que cambió en la implemntación fue que en vez de utilizar `>=` utilizamos `<=` para el descarte.
## 6. Contraejemplo: Maximum Subarray Sum.
Este la verdad no sabría como implementarlo, me hace ruido como puedes guardar esos subconjuntos para buscar de forma rápida el que te de la mayor suma, tenemos un buen criterio en que si hay números negativos su valor absoluto debe ser menor estricto que los demás, pero aún así su optimización no creo que sea trivial.
## 7. Sliding Window.
Este fue más sencillo de visualizar, pero creo el mayor problema está en que son muchas operaciones que una pila no podría optimizar, porque al tener un conjunto de n números, y tomar subconjuntos de k números, primero se deben crear esos subconjuntos, ordenarlos, buscar el valor medio y si los subconjuntos son de una cantidad par además debes tomar el menor y la complejidad siento que sube mucho.
## 8. Invariante.
Al inicio yo creí que el invariante es el caso del primer número, porque sin importar que número sea no hay uno menor que él a su izquierda, entonces resultados siempre empieza con 0, pero también pueden ser los valores que no se descartan porque son útiles.
## 9. Pruebas.
Creo que las más importantes e intuitivas era ver que pasaba con un arreglo creciente, con uno decreciente y el caso límite, me gustó la implementación paravalidar la importancia de que fuera una desigualdad no estricta, y creo que debo mejorar planetando mis pruebas para números muy grandes.
## 10. Complejidad.
Sabemos por lo que dijimos antes de la solución ingenua que nuestra complejidad inicial pudo haber sido cuadrática, sin embargo, tras optimizar yo creo que esto se acerca mucho más a un caso `O(n)` o inclusive en un buen caso más no el mejor necesariamente a un `O(log(n))` dependiendo el contenido del array.
## 11. Cómo descubrimos el algoritmo.
Aunque al inicio no entendí bien lo que nos pedían, contestando el notebook me di cuenta de lo útil que podía ser la pila para ir guardando valores y de forma que soi había valores mayores o iguales no los tomaramos en cuenta y pudieramos solo saltar a lo que ya sabíamos de ellos, aunque no lo sé explicar bien así, ya leyendo el pseudocódigo me quedó más claro y de ahí fue un poco más intuitivo todo. Sabíamos que íbamos a necesitar una pila, una lista y comparar los valores para guardar las posiciones.
## 12. Pregunta abierta.
1. ¿Nuestro algoritmo podría ser `O(1)` en el mejor caso?
2. ¿Qué estructura será la que nos convenga para el contraejemplo y el problema de la ventana?