# Sección 1 (Presentación de laboratorio)

**-¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?**

Por que a priori podría parecer que no necesitamos algun tipo de cosa, pero a la mera hora no solamente la necesitamos, si no que era indespensable para resolver el problema, entonces si hacemos este proceso de comparación podemos adelantarnos e implementar cosas que pensabamos que no debiamos ocupar.

# Sección 3 (Lectura Estrategica)

**1. ¿Qué está pidiendo exactamente el problema?**
    Lo que esta haciendo el problema es indexar los elementos de la lista pero empezando a indexarlos deslde el 1, o sea la función principal de estas líneas de código es reindexar los elementos de la primera lista, que es la que se ingresa.

**2. ¿Cuál es la entrada?**
    La entrada, es la primera lista desordenada con los numeros que queremos reindexar.

**3. ¿Cuál es la salida?**
    La salida es la misma lista(sin modificar los elementos dentro de ella) pro con las pocisiones reindexadas de los elementos de la misma.

**4. ¿Qué significa “más cercano a la izquierda”?**
    Agarrando el número que queremos como pivote empezamos a analizar dentro de la lista desde ese pivote hasta el final hacia el lado izquiero del mismo y el primer numero que su valor sea más chico es el número que buscamos.

**5. ¿Qué pasa si no existe un valor menor?**
    En este primer ejemplo no hace nada pero en el problema original nos dice que hacer, que en este caaso es arrojar de manera automatica el número cero, por eso la importancia de reindexar empezando en el uno.

**6. ¿Qué casos extremos parecen importantes?**
    En el contraejemplo enunciado, cados importantes parecieran ser en los que los numeros positivos y negativos estan intercalados.

# Sección 4 (Ingenieria inversa del algoritmo)

**1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?**
    Yo creo que haciea una tabla, donde la primera fila son los números ingresados, la segunda fila los indices que te regresa, y cada columna es la entrada de cada número que vamos a analizar, adicionalmente, escribiria las reglas o condiciones que estoy siguiendo en lenguaje natural por si alguien extreno llega a leer la tabla sepa que esta pasando.

**2. ¿Qué información miras repetidamente?**
```text
    Ya con las lineas de codígo de la sección pasada, los datos que más se analizan durante el algoritmo son:
        - La reindexación de los números
        - Todos los valores a la izquierda cada número cuando los agarremos de pivote
    Y ya, si bien checamos varias veces estos datos no es como que chequemos más datos para ponerlos aca.
```

**3. ¿Qué información se vuelve inútil?**
    Los indices originales de la lista de números ingresada.

**4. ¿Qué operaciones se repiten?**
    Se repite muchisimo la operación de menor que, ya que se tiene que repetri por todos los números a la izquierda de nuestro pivote hasta que se encuentre uno menos, entonces en el mejor esenario en el que esten acomodaddos de menor a mayor, si tenemos n numeros la comparación se realiza n veces.

**5. ¿Qué estructura podría ayudar?**
    Yo creo que la estrictura que más puede ayudar es una cola tipo deque obviamente implementando un while.

# Sección 5 (Solución Ingenua)

**- ¿Cuál sería la complejidad en el peor caso?**

Veamos algunos casos para poder determinar la complejidad utilizando el metodo Big-O


| Lista de entrada | Lista de salida | Comparaciones | # Total de comparaciones |
| --- | --- | --- | --- |
| 6 | 0 | 1 | 1 |
| 65 | 00 | 11 | 2 |
| 654 | 000 | 112 | 4 |
| 6543 | 0000 | 1123 | 7 |
| 65432 | 00000 | 11234 | 11 |
| 654321 | 00000 | 112345 | 16 |

Observemos que aquí estan pasando varias cosas, para empezar el primer númeo aun que no tenga ningun otro a la izquierda se toma como si tuviera una comparación, de ahí en adelante todos los demas números la comparación con la pocisión 0 Que seria el número fuera de la lista que si se cuenta en el primer indice no se cuenta, es por eso que para el 6 y el 5 solamente se cuenta una comparación, ahora este es el caso más complicado porque en cada iteración sobre las lista se tienen que recorrer todos los valores.
Luego si para 1 la complejidad es de 1 y para 6 la complejidad es de 16 la complejidad crecee de manera cuadratica.

**- ¿En qué tipo de arreglo se repetiría más trabajo?**
    Como lo mencione en l tabla sería una lista de n elementos acomodada de mayor a menor.

**- ¿Qué información se vuelve a revisar muchas veces?**
    La lista original de lus números ingresados.

# Seccion 6 (Pseudocódigo Parcial)

**- ¿Por qué se usa “mayor o igual” y no solo “mayor”?**
    Según yo esto esta mal, no debería de ser mayor o igual, debería de ser unicamente mayor que,porque si esta enunciado éxplicitamente en el problema original que lhay que analizar los números de la izquierda HASTA enconcontrar un número MEROR al que estamos analizando, no MENOR O IGUAL, por lo que no siento que sea correcto utilizar el mayor o igual.

**- ¿Qué representa el tope de la pila después de descartar candidatos?**
    El tope de la pila representa el ultimo número ingresado a la pila.

**- ¿Cuál es el invariante de la pila?**
    lo que varia son los indices de los elemtos de la pila, por lo tanto lo que no cambia son los valores de los números de la pila originl, o sea si tenemos un 5 en la pocisión que originalmete sería la 0, etonces si va a variar la pocisión de 0 a 1 pero el valor del 5 no cambia, o sea que nunca mutara a volverse un 6 o algo por el estilo.

# Sección 10 (Variante: Nearest Greater Values)

**- ¿Qué cambia?**
    Lo unico que cambiaria en la implementación del algoritmo para resolver este problema, es que en lugar de colocar el simbolo de mayor que, colocaremos el de menor que.

**- ¿Qué comparación se modifica?**
    La comparación del pivote con el valor de los elementos de la izquierda siguen siendo exactamente los mismos, pero la camporaración que cambia s la que mencione en la pregunta anterior y es la compración de mayor que con la de menor que.

**- ¿Se conserva la misma estructura?**
    Si, ya que a priori el algoritmo raliza lo mismo, unicamente con el cambio ya mencionado.

**- ¿La complejidad cambia?**
    No. Deberia de ser la misma, ahora a diferencia del pasado el peor escenario posible en lugar de ser n, n-1, n-2, ... ahora es 0,1,2,...,n
    osea en lugar de que los valores de los números vayan descendiendo, ahora iran ascendiendo.

# Sección 11 (Contraejemplo: Maximum Subarray Sum)

**- ¿Serviría una pila monótona?**
    Lo dudo demasiado, porque como tanto en las listas como en las pilas las cosas se leen de izquierda a derecha la cola acaba siendo los elementos de la izquierda entonces en el caso que el cubconjunto que nos funcione este en la cola, una pila ordinaria no nos dejaria ocupar esta cola para hacer el subconjunto.

**- ¿Qué información parece importante?**
    Para este ejercicio la información más importante es saber suales son todos los subconjuntos conexos (Osea que los elementos esten juntos ejemplo: en el conjunto {1,2,3} el subconjunto {1,2} es candidato pero el {1,3} no, porque los elementos no estan juntos en el conjunto original) del conjunto original, ya con esta información podemos hcaer las sumas de los elementos de dichos conjuntos y con esto resolver el problema deseado.

**- ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?**
    Porque para lograr obtener estos sunbconjuntos conexos ocupamos ir eliminando elementos de la izquierda y de la derecha del sicho conjunto original, tambien por eso pude parecer importante el usar una deque y no una pila normal, para ahorrar memoria a la hora de reindexar las cosas, por lo que la lista final muy probablemente no obtenga el mismo orden los candidatos originales, pero no por esto deja de ser la respuesta correcta.

# Sección 12 (Vista al futuro: Sliding Window)

**- ¿Qué información entra?**
    Tenemos 3 imputs, el primer imput es el número de elementos de mi conjunto, el segundo el números de elementos que tiene que tener cada subconjunto iniciando de izquierda a derecha, y el tercero es es el conjunto en el que vamos a aplicar el algoritmo.

**- ¿Qué información sale?**
    Lo que escupe este algoritmo es la lista de con las medianas de todos los subconjuntos del tamaño que indicamos del conjunto original.

**- ¿Qué información permanece?**
    EL tamaño de los subconjuntos es lo unico que permanece, ya que el conjunto original se va subdividiendo y las medianas cambiando su valor dependiendo del subconjunto analizado.

**- ¿Por qué recalcular todo sería costoso?**
    Para contestar esta pregunta primero coy a plantear en lenguaje natural el algoritmo que para mi resuelve este problema, muy por enima, lo que hace el algoritmo será agarrar el conjunto, y luego de izquierda a derecha ir creando los subconjuntos del tamñao indicado, cada que se cree un subconjunto lo va a acomodar de menos a mayor y agarrar su media y adjuntarla a la lista de resultados, asi sucesibamento por cada subconjunto generado, entonces lo que estamos haciendo con esto es que estamos reacomodando todos los elementos necesarios de el conjunto original de una manera conveniente para nocotros.
    Con esto, lo que yo entiendo qpor calcular la mediana es este acomodo, por lo que el recalculamiento de la misma va a ser cambiar el tamaño del subconjunto y calcular una vez más su mediana, y pues suponiendo que esto se refiere con recalcular, entonces esto va a ser muy costoso porque hay que volver a repetir todo el proceso una vez más para sacar el resultado.

**- ¿Qué tipo de estructura podría ayudar?**
    Sin duda lo que más ayudaria seía ocupar las pilas tipo deque, no podemos ocupar sets porque te va a quitar tanto el orden como los repetidos.

# Sección 13 (Diseño de pruebas)

**- Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.**
    No funciona por el caso que las listas tengas el mismo nümero repetido siempre, o sea por decir un ejemplo [3,3,3]

**- ¿Qué caso límite no debe faltar?**
    Para mi es test crucial es donde se muestra que toda lista de mismos valores regresa una lista unicamente con ceros, porque ahí es dodne de fondo se ve bien que todos lo valores vayan siendo analizados.

# Sección 14 (¿Qué patron descubrimos)

**- ¿Qué aprendimos sobre diseñar algoritmos?**
    Con lo que más me quedo de la clase de hoy es que hay que aprender bien cual es el problema planteado para poder hacer bien el código usando las herramientas que nos convengan.

**- ¿Qué significa conservar candidatos útiles?**
    Descartar la información que no es necesaria para el problema para quedarnos con la que realmente utilizaremos

**- ¿Qué invariante mantiene la pila?**
    El valor de los datos dento de ella, ya que etos nunca van a cambiar.

**- ¿Qué cambia entre simular y optimizar?**
    Simular practicamente es unicamente realizar pruebas y optimizar es que una vez que las prueas fueron

**- ¿Por qué no todos los problemas con arreglos usan la misma estructura?**
Porque en escencia son el mismo problema