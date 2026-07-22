# Discusión

## 1. Problema y primera idea
Para cada elemento del arreglo, encontrar la posición más cercana a la izquierda cuyo valor sea estrictamente menor. La primera idea natural es revisar hacia atrás hasta encontrar tal valor, pero esa estrategia es demasiado lenta, no jala tan chido en listas de cardinalidad n con un n muy grande.

## 2. Por qué la solución ingenua repite trabajo
La versión ingenua vuelve a inspeccionar elementos que ya había visto en pasos anteriores, cuando un valor no sirve para una posición sigue estando presente en la revisión de las siguientes posiciones, aunque ya sabemos que no es una buena respuesta para el futuro inmediato, lo que genera un costo que crece de forma cuadrática, O(n^2) en el peor caso.

## 3. Información útil e información descartable
La información útil es la que puede todavía convertirse en la respuesta correcta para alguna posición futura. En cambio, los valores que ya fueron superados por un elemento más cercano y más pequeño dejan de ser relevantes. El algoritmo necesita conservar solo aquello que todavía puede influir en una decisión futura.

## 4. Elección de estructura
La estructura adecuada es una pila monótona. Permite mantener candidatos ordenados y retirar rápidamente los que ya no sirven, porque el elemento actual puede invalidar varios candidatos a la vez. Esta elección reduce el tiempo total al hacer que cada elemento entre y salga de la estructura una sola vez.

## 5. Variante: Nearest Greater Values
La variante cambia el criterio de comparación: ahora se busca el valor mayor más cercano a la izquierda, el mismo esquema sirve, pero el sentido de la eliminación se invierte. En lugar de descartar valores mayores o iguales al actual, se descartan los menores o iguales.

## 6. Contraejemplo: Maximum Subarray Sum
Maximum Subarray Sum muestra que no todo problema de arreglos se resuelve con una estructura monótona, lo importante no es encontrar un “mejor vecino”, sino decidir cómo combinar prefijos y subarreglos para maximizar una suma. La información relevante ya no es solo un conjunto de candidatos ordenados, sino también el estado acumulado.

## 7. Sliding Window
En un problema de ventana deslizante, cada paso incorpora un nuevo elemento y elimina otro. El reto no es recomenzar desde cero, sino actualizar la información de forma incremental. Por eso aparecen estructuras que soportan inserciones y borrados eficientes mientras la ventana se mueve.

## 8. Invariante
El invariante de la pila es que, al procesar cada elemento, la pila contiene exactamente los candidatos todavía potencialmente útiles, organizados de forma creciente de abajo hacia arriba. Además, el tope representa la mejor opción actual para responder la consulta de ese momento.

## 9. Pruebas
Conviene probar casos sencillos y casos que revelen errores de comparación, es importante es el uso de valores repetidos, porque un algoritmo incorrecto puede fallar cuando aparece un valor igual. También es útil incluir arreglos crecientes, decrecientes y un caso de un solo elemento, para comprobar los límites del comportamiento.

## 10. Complejidad
La solución basada en pila monótona tiene complejidad temporal O(n) en el peor caso, porque cada elemento se inserta una vez y se elimina a lo sumo una vez. El uso de memoria es O(n) en el peor caso, aunque en la práctica suele ser menor.

## 11. Cómo descubrimos el algoritmo
El algoritmo apareció al preguntarnos qué información realmente necesitábamos. En lugar de mirar hacia atrás una y otra vez, observamos que muchos valores eran descartados de inmediato cuando aparecía un elemento más cercano y más pequeño. Esa observación llevó a mantener solo los candidatos que aún podían ser útiles.

## 12. Pregunta abierta
¿En qué otros problemas de arreglos podría aparecer el mismo patrón de conservar información útil y descartar lo que ya no sirve, aunque el problema no sea buscar vecinos y como se podria aplicar a la vida diaria?
