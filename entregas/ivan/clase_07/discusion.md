1. Problema y primera idea.
- Encontrar el valor menor más cercano a la izquierda de un entero en una lista de enteros.
2. Por qué la solución ingenua repite trabajo.
- Porque repite las comparaciones por cada entero. 
3. Información útil e información descartable.
-Útil: Enteros menores al actual
-Descartable: Enteros mayores o iguales.
4. Elección de estructura.
-Lista/Pila
5. Variante: Nearest Greater Values.
-No cambia nada más que una comparación
6. Contraejemplo: Maximum Subarray Sum.
-Necesitamos una estrategia que evite sumar los elementos de cada subconjunto y compararlos.
7. Sliding Window.
-Puede servir una pila, pero quizás con una estrategia como la de maximum subarray sum es mejor.
8. Invariante.
-El mínimo
9. Pruebas.
-Diseñé pruebas para listas crecientes/decrecientes y con negativos.
10. Complejidad.
-En el peor necesario, vimos que es O(n^2). Con el algortimo que diseñe, es O(n) porque solo haces una operación por cada elemento de la lista. 
11. Cómo descubrimos el algoritmo.
- Siguiendo la nueva metodología del curso
12. Pregunta abierta.
- ¿ Cómo podemos determinar la estructura más conveniente para los problemas de forma general ?
