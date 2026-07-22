# Notebook - Clase 07 - Gustavo Torres

## 1. Presentación del laboratorio

    ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos? Comparar problemas nos permite aislar sus propiedades matemáticas algebraicas y relacionales fundamentales. Al contrastar un problema contra otros (variantes, contraejemplos o extensiones), logramos entender qué invariantes exige la pregunta

## 2. Lectura estratégica

    1. ¿Qué está pidiendo exactamente el problema?

    Para cada índice i (con 1 < i < n) dentro de un arreglo A, debemos determinar la posición o índice j más cercano a la izquierda (es decir, el máximo j < i) tal que satisfaga la desigualdad estrictamente menor: A[j] < A[i].

    2. ¿Cuál es la entrada?

    Un enteron n que denota la cantidad de elementos o tamaño del arreglo. 

    3. ¿Cuál es la salida?
    4. ¿Qué significa “más cercano a la izquierda”?
    5. ¿Qué pasa si no existe un valor menor?

    Si el conjunto de candidatos estrictamente menores a la izquierda es vacío ($S_i = \emptyset$), el problema exige imprimir como respuesta un valor centinela de 0

    6. ¿Qué casos extremos parecen importantes?

    Arreglo estrictamente creciente: (ej. [1, 2, 3, 4]). Cada elemento encuentra inmediatamente a su vecino izquierdo como el menor. La salida es [0, 1, 2, 3].
    
    Arreglo estrictamente decreciente: (ej. [4, 3, 2, 1]). Ningún elemento tiene un valor menor a su izquierda. La salida es [0, 0, 0, 0].
    
    Arreglo constante o con valores repetidos: (ej. [3, 3, 3, 3]). Como la condición pide un valor estrictamente menor, los valores iguales no sirven. La salida es [0, 0, 0, 0]. 
    
    Mínimos globales intermitentes: Valores muy pequeños que obligan a saltar un bloque masivo de elementos mayores.


## 3. Ingeniería inversa del algoritmo

    1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?

    Para cada posición i, coloco mi dedo en el índice i-1 y me muevo hacia atrás uno por uno. 

    2. ¿Qué información miras repetidamente?

    Los valores de los elementos que se encuentran en las posiciones pasadas pero recientes, especialmente cuando el elemento actual es relativamente grande y no logra superarlos de inmediato, provocando que vuelva a examinar elementos que ya revisé en pasos anteriores.

    3. ¿Qué información se vuelve inútil?

    Si tengo un elemento a la izquierda en la posición j y luego aparece un elemento en la posición k tal que el valor es menor o igual, el elemento de la posición j se vuelve completamente inútil para cualquier futura consulta i > k. Porque si un elemento futuro fuera mayor, la posición k está más cerca de i que la posición j, el índice k "eclipsará" al índice j por siempre.

    4. ¿Qué operaciones se repiten?

    La inspección de elementos hacia atrás y el descarte lógico de valores masivos que quedan atrapados entre un valor menor anterior y un valor menor actual.

    5. ¿Qué estructura podría ayudar?

    Una estructura de tipo Pila (Stack) estructurada de forma monótona, capaz de almacenar pares de la forma (valor, posición), manteniendo siempre sus valores en orden estrictamente creciente desde el fondo hasta el tope.


## 4. Solución ingenua

    - ¿Qué significa que un candidato sea útil?

    La complejidad temporal asintótica en el peor caso es $O(n^2)$. Esto se debe a que para cada uno de los n elementos, en el peor escenario podríamos realizar hasta i.1 comparaciones. 

    - ¿Por qué algunos candidatos dejan de servir?

    En un arreglo estrictamente decreciente o no creciente. En este caso, para el i-ésimo elemento se recorrerán todos los i-1 elementos anteriores sólo para llegar al inicio y concluir con un 0.

    - ¿Qué propiedad debería mantener la estructura?

    Se revisan repetidamente los elementos grandes del pasado que ya fallaron al compararse con elementos anteriores, ignorando el hecho de que si un elemento anterior era menor que ellos, actuaría como un "escudo" protector.

## 5. Descubrimiento de la pila monótona

    - ¿Qué elementos vuelves a inspeccionar varias veces aunque ya conocías su información?

    Aquellos elementos cuyos valores son altos y ya han sido superados por un elemento posterior más pequeño. En la solución ingenua, el algoritmo es "amnésico": no recuerda que esos elementos altos ya perdieron toda relevancia frente a elementos más bajos y más cercanos.

    - ¿Qué condición hace que un valor anterior nunca vuelva a ser la mejor respuesta para un elemento futuro?

    La condición de dominancia geométrica por transitividad.

    - ¿Qué comparación concreta puedes hacer con el elemento actual para decidir inmediatamente que un candidato ya no volverá a ser útil?

    - ¿Qué significa que un candidato sea útil?

    Un candidato en el índice j es "útil" si y sólo si representa un mínimo estricto local de cola.

    - ¿Por qué algunos candidatos dejan de servir?

    Porque la llegada de un nuevo valor actúa como una barrera.

    - ¿Qué propiedad debería mantener la estructura?

    Debe mantener una monotonía estricta creciente desde la base de la pila hasta el tope

## 6. Pseudocódigo

    - ¿Por qué se usa “mayor o igual” y no solo “mayor”?

    Si un elemento en el tope de la pila es estrictamente mayor. Si un elemento en el tope es exactamente igual

    - ¿Qué representa el tope de la pila después de descartar candidatos?

    Representa exactamente la posición del primer elemento a la izquierda que tiene un valor estrictamente menor que el elemento actual. Si la pila queda vacía después del proceso de descarte, significa que no existe tal elemento en todo el prefijo analizado, por lo que la respuesta es 0. 

    - ¿Cuál es el invariante de la pila?

    Al inicio y al final de cada iteración del bucle principal, los elementos almacenados en la pila están ordenados de manera estrictamente creciente tanto por sus valores como por sus índices de posición.

## 7. Variante: Nearest Greater Values

    - ¿Qué cambia?

    El objetivo ahora es encontrar la posición del elemento más cercano a la izquierda cuyo valor sea estrictamente mayor que el valor actual en lugar de menor.  

    - ¿Qué comparación se modifica?

    En el bucle while que limpia o desapila candidatos obsoletos, invertimos el signo relacional de descarte.

    - ¿Se conserva la misma estructura?

    Sí, se conserva exactamente la misma estructura abstracta: una Pila Monótona.  

    - ¿La complejidad cambia?

    No. La complejidad asintótica se mantiene en $O(n)$ tiempo y $O(n)$ espacio.

## 8. Contraejemplo: Maximum Subarray Sum

    - ¿Serviría una pila monótona?

    No. Una pila monótona no es la herramienta adecuada para este problema.  

    - ¿Qué información parece importante?

    Es crucial llevar el seguimiento de la suma prefija acumulada máxima que termina exactamente en la posición actual y contrastarla con el máximo global.

    - ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?

    Porque en el problema de la subcadena de suma máxima, la validez de unir un subarreglo anterior con el elemento actual.

## 9. Vista al futuro: Sliding Window

    - ¿Qué información entra?
    
    El nuevo elemento que se desliza y entra por el extremo derecho de la ventana de tamaño fijo k.

    - ¿Qué información sale?

    El elemento más antiguo que queda fuera de la ventana, es decir, el que se encontraba en el extremo izquierdo.
  
    - ¿Qué información permanece?

    Los elementos que se encuentran vigentes dentro del intervalo activo actual de índices [i - k + 1, i].  
    - ¿Por qué recalcular todo sería costoso?

    Si para cada uno de los n-k+1 desplazamientos de la ventana recalculáramos la mediana o reordenáramos los k elementos desde cero.

    - ¿Qué tipo de estructura podría ayudar?

    Para el cálculo de medianas o mantenimiento del orden estricto en ventanas dinámicas, se requiere una estructura balanceada indexada.

## 10. Diseño de pruebas

    - Diseña al menos dos pruebas propias.

    Prueba 1:

    Entrada: [4, 4, 2, 2, 5]

    Salida esperada: [0, 0, 0, 0, 4]

    Prueba 2:

    Entrada: [10, 1, 10, 1, 10]

    Salida esperada: [0, 0, 2, 0, 4]

    - Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.

    Con el operador incorrecto (>), al evaluar el segundo 3, el primer 3 no es desapilado porque la condición 3 > 3 es falsa. El algoritmo vería al tope y diría que el menor más cercano para el segundo elemento está en la posición 1, retornando erróneamente [0, 1]. Una prueba con valores adyacentes iguales rompe y expone este bug algorítmico al instante.

    - ¿Qué caso límite no debe faltar?  

    El arreglo de tamaño mínimo posible n = 1 (ej. [42], donde la salida siempre es invariablemente [0]). Un arreglo con todos los elementos idénticos (ej. [7, 7, 7, 7], donde la respuesta debe ser obligatoriamente un vector de ceros [0, 0, 0, 0]). 

## 11. ¿Qué patrón descubrimos?

    - ¿Qué aprendimos sobre diseñar algoritmos?

    Aprendimos que la optimización algorítmica fundamental frecuentemente no proviene de procesar más rápido, sino de identificar y eliminar el trabajo redundante  

    - ¿Qué significa conservar candidatos útiles?

    Significa mantener en memoria exclusivamente aquellos elementos que poseen la viabilidad de ser la respuesta correcta para alguna consulta en el futuro.

    - ¿Qué invariante mantiene la pila?

    Mantiene el invariante estructural de Monotonía Estricta Creciente en Valores y Posiciones:

    - ¿Qué cambia entre simular y optimizar?

    Simular ejecuta de manera ciega la definición literal del problema paso a paso recalificando datos pasados y optimizar aprovecha las propiedades algebraicas estructurales (como transitividad y orden geométrico) para mantener un estado depurado

    - ¿Por qué no todos los problemas con arreglos usan la misma estructura?

    Porque cada estructura de datos está construida en torno a una invariante particular que responde a un tipo específico de flujo de información.
