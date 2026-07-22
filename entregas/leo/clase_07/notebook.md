# Notebook - Clase 07 - Leonardo Daniel Arenas Serafín

## 1. Presentación del laboratorio

#### ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?
Porque te ayuda a ir creando intuición sobre qué tipo de herramientas se usan en cada tipo de problema, te ayuda a salirte del caso particular del problema en concreto para ir a la parte abstracta de la herramienta.

## 2. Lectura estratégica

#### ¿Qué está pidiendo exactamente el problema?
Está pidiendo que regresemos una lista cuyos elementos sean numeros enteros no negativos que representen la posición más cercana a la izquierda cuyo valor sea menor de cada elemento de una lista original


#### ¿Cuál es la entrada?
La entrada es una lista de números 

#### ¿Cuál es la salida?
La salida es igualmente una lista de números

#### ¿Qué significa “más cercano a la izquierda”?
Significa que el algoritmo va recorriendo la lista hacia la izquierda y cuando encuentre un número que sea menor, el algoritmo parará y guardará la información de la posición de dicho número en una lista

#### ¿Qué pasa si no existe un valor menor?
Se regresa "0"

#### ¿Qué casos extremos parecen importantes?
Sí, para poder medir la complejidad de distintas herramientas.


## 3. Ingeniería inversa del algoritmo

####  ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?
Primero escribiría arriba de los elementos de la lista original sus posiciones para no perderlas de vista, después empezaría en cada número e iriía uno por uno comparando hacia la izquiera hasta encontrar un número menos para después anotarlo, y así hasta agotar la lista.

####  ¿Qué información miras repetidamente?
Repetidamente miro la información del valor del número escogido de la lista para comparar con sus elementos a su izquierda, pues por cada elemento a la izquierda que tomemos, debemos compararlo con el elegido.

####  ¿Qué información se vuelve inútil?
Toda la información que está a la derecha del número elegido.

####  ¿Qué operaciones se repiten?
Comparaciones.

####  ¿Qué estructura podría ayudar?
Una estructura de for, para que pueda iterar los elementos de la lista y una estructura que cuando encuentre un número menor al elegido, guarde la información de su posición sin importar los demás elementos.


## 4. Solución ingenua

####  ¿Cuál sería la complejidad en el peor caso?
En el peor caso, la complejidad sería O((n-1)*n/2), pues por cada elemento i de la lista, tendría que revisar todos los i-1 elementos para encontrar una solución. De esta forma, tendría que haber la suma de los primeros n-1 naturales comparaciones para poder llegar a una solución. Así, tendría una complejidad cuadrática.

####  ¿En qué tipo de arreglo se repetiría más trabajo?
En un arreglo en donde los elementos estén arreglados de mayor a menor

####  ¿Qué información se vuelve a revisar muchas veces?
Repetidamente se revisa la información del valor del número escogido de la lista para comparar con sus elementos a su izquierda, pues por cada elemento a la izquierda que tomemos, debemos compararlo con el elegido.

####   ¿Qué trabajo se repite?
El comparar continuamente los mismos valors anteriores

####   ¿Qué valores anteriores pueden descartarse?
Todos los anteriores al valor menor más próximo del elemento elegido.

####   ¿Cómo notarías que un valor ya no será buen candidato?
Cuando hay un valor menor a su derecha, pues ese siempre será elegido primero


## 5. Descubrimiento de la pila monótona

####  ¿Qué significa que un candidato sea útil?
Un candidato es útil cuando no tiene ningún elemento a su derecha que sea menor a él hasta donde hayamos recorrido de la lista original.

####  ¿Por qué algunos candidatos dejan de servir?
Porque tienen a su derecha números menores a él, que al recorrer hacia la izquierda siempre serán primera opción antes de ellos.

####  ¿Qué propiedad debería mantener la estructura?
Debería descartar los elementos inútiles y solo mantener los elementos útiles en orden de entrada de izquierda a derecha

## 6. Pseudocódigo

####  ¿Por qué se usa “mayor o igual” y no solo “mayor”?
Porque nosotros estamos busando números que sean estrictamente menores al elemento elegido, por lo que si solo usaramos "mayor" permitiríamos el menor igual.

####  ¿Qué representa el tope de la pila después de descartar candidatos?
Representa el primer elemento que no fue mayor igual, es decir, el primer elemento menor

####  ¿Cuál es el invariante de la pila?
El invariante es que si la pila está vacía, se regresará "0"

## 7. Variante: Nearest Greater Values

#### ¿Qué cambia?
Para cada iteración de la lista original, la pila cambia respecto a cuáles son los candidatos, pues para comparar, descarta los valores que ya son mayores a sus siguientes en la orden de la lista.

#### ¿Qué comparación se modifica?
La única comparación que se modifica es que en vez de usarse `>=` se usa `<=`

#### ¿Se conserva la misma estructura?
Sí, la estructura de pila

#### ¿La complejidad cambia?
No, es exactamente lo mismo

## 8. Contraejemplo: Maximum Subarray Sum

#### ¿Serviría una pila monótona?
No creo que serviría porque en este caso usamos la pila pues vamos en un orden de izquierda a derecha, pero al hacer subconjuntos perdemos totalmente la noción de orden y no creo que sea conveniente

#### ¿Qué información parece importante?
Más que el orden considero que sería importante la longitud del arreglo


#### ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?
Porque para empezar debríamos primero establecer un criterio para ordenar, lo cual es difícil y no sería de mucha ayuda para trabajar con la pila

## 9. Vista al futuro: Sliding Window

#### ¿Qué información entra?
Supongo que lo que entra son nuevos elementos hacia la lista original y la información de las nuevs posiciones

#### ¿Qué información sale?
Sale la información de los elementos de la lista original que salieron y la información de las antiguas posiciones

#### ¿Qué información permanece?
Los elementos que no salen ni entran, los que ya estaban en la lista original


#### ¿Por qué recalcular todo sería costoso?
Porque por cada cambio que hay, debemos actualizar las nuevas posiciones y el poder saber cuáles son todas las operaciones hechas para recalcular todo sería muy costoso

#### ¿Qué tipo de estructura podría ayudar?
Podría ayudar un diccionario en donde las claves sean las posiciones y los valores sean los distintos elementos en esas posiciones a cada cambio.


## 10. Diseño de pruebas

#### Diseña al menos dos pruebas propias.
Diseñe las pruebas de convexidad y concavidad, es decir, cuando primero la lista original es decreciente ybluego cambia a creciente y viceversa.

#### Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.
Porque al solo usar `>` estás permitiendo que haya una igualdad de valores, cuando el problema te pide que encuentre valores que sean estrictamente menores. Por lo que es crucial que este error sea detectado para poder resolver el problema correctamente tal como se pide.

#### ¿Qué caso límite no debe faltar?
El caso en el que solo hay un solo elemento.


## 11. ¿Qué patrón descubrimos?

#### ¿Qué aprendimos sobre diseñar algoritmos?
Aprendimos que a veces es mucho más sencillo primero el intentar analizar cuál herramienta podría ser más útil antes de empezar a programar, pues puede pasar que primero te pongas a programar y a terminar tu algortimo te des cuenta de que es muy complejo y que hay otra alternativa que usa una herramienta que lo hace muy fácilmente sin tanta complejidad.

#### ¿Qué significa conservar candidatos útiles?
Signfica dejar esos candidatos en la pila para que sean comparados con los siguientes elementos

#### ¿Qué invariante mantiene la pila?
Mantiene el invariante de que si la pila está vacía, siempre la respuesta será "0"

#### ¿Qué cambia entre simular y optimizar?
El simular solamente hace lo que una persona naturalmente haría pero desde un algoritmo. Esto cambia al optimizar, pues al optimizar no necesariamente se encuentras soluciones naturales y no es algo que una persona haría, pero que una computadora puede hacer sin mayor problema.

#### ¿Por qué no todos los problemas con arreglos usan la misma estructura?
Porque cada problema pide mantener cierta información, como puede ser un orden específico o la frecuencia, cosa que no cualquier estructura hace.
