# Clase 07: Notebook
#### Nombre: Patricio Navarro

## Presentación Laboratorio
1. ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?
    - Porque puede que tengan un comportamiento parecido y a la hora de comparar varios puedes entender mejor alguno, o lo que tinene en común y de ahí poder empezar a planetar la solución.

## Lectura Estratégica
1. ¿Qué está pidiendo exactamente el problema?
    - Que dado un arreglo de números, para cada número encontremos la posición mas cercana a la izquierda con un número menor.
2. ¿Cuál es la entrada?
    - El tamaño del arreglo y el arreglo en sí.
3. ¿Cuál es la salida?
    - Una lista con las posiciones mas cercanas a cada número que tuvieran un número menor.
4. ¿Qué significa “más cercano a la izquierda”?
    - Que este lo más cerca posible en posiciones y que sea menor su índice.
5. ¿Qué pasa si no existe un valor menor?
    - Se pone 0.
6. ¿Qué casos extremos parecen importantes?
    - El caso mínimo debe marcar solo 0, el caso máximo, que pasa cuando son mas enteros que la restricción, que pasa si el arreglo tiene números demasiado grandes, si el arreglo fuera de todos un mismo número la salida debe ser un arreglo de 0s.

## Ingeniería Inversa del Algoritmo
1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?
    - Pues nada mas compararía uno por uno con los números anteriores, si no tiene un número menor a lado entonces 0, si lo encuentro pongo la posición del número que fue menor.
2. ¿Qué información miras repetidamente?
    - El valor guadado en cada posición, y las posiciones en sí. También tu valor actual y el anterior.
3. ¿Qué información se vuelve inútil?
    - El valor que fue menor, solo nos importa su posición.
4. ¿Qué operaciones se repiten?
    - Escoger valor inicial, buscar valor menor, agregar su posición a una lista.
5. ¿Qué estructura podría ayudar?
    - Supongo que una pila, que es más rápida en tareas de buscar y guardar, y así solo vamos apilando las posiciones que encontremos para cada número. Pero tampoco veo mal una lista o una cola.

## Solución ingenua
1. ¿Cuál sería la complejidad en el peor caso?
    - El peor caso es que tenga que recorrer todos los números antes, entonces creo que sería `O(n^2)`, porque es checar todos los números anteriores para cada número del arreglo.
2. ¿En qué tipo de arreglo se repetiría más trabajo?
    - Con una lista o con algo que necesitara dos ciclos, como un for anidado dentro de otro.
3. ¿Qué información se vuelve a revisar muchas veces?
    - Las posiciones y los valores de cada una de esas posiciones.

## ¿Por qué la solución ingenua no escala?
1. ¿Qué trabajo se repite?
    - Buscar en todas las posiciones anteriores para cada número.
2. ¿Qué valores anteriores pueden descartarse?
    - Pues si ya sabes que un número en una posición `y` tiene un valor menor en `x` posición, en caso de no encontrar nada hasta el número con posición `y` entonces puedes usar al mismo número con posición `x`. Así ya no tienes que revisar a todos.
3. ¿Cómo notarías que un valor ya no será buen candidato?
    - Que sea el más grande del arreglo o mayor o igual que los que tiene a ambos lados.

## Descubrimiento de la pila monótona
1. ¿Qué significa que un candidato sea útil?
    - Que vale la pena revisarlo, entonces debe ser no solo menor sino que el mínimo de los valores que vas a revisar.
2. ¿Por qué algunos candidatos dejan de servir?
    - Porque al ser mayores o iguales no cumplen la regla ye tnonces no vale la pena revisarlos a todos.
3. ¿Qué propiedad debería mantener la estructura?
    - Que el último valor útil se guarde y si se necesita usar pues sea el primero en salir para no tener que recorrer los demás.

## Pseudocódigo parcial
1. ¿Por qué se usa “mayor o igual” y no solo “mayor”?
    - Porque el problema te pide que sean menores, entonces si son iguales el valor deja de ser útil.
2. ¿Qué representa el tope de la pila después de descartar candidatos?
    - El mínimo que te sirve para los demás datos que no han sido revisados o descartados.
3. ¿Cuál es el invariante de la pila?
    - Que si esta vacía la respuesta es 0.

## Variante: NGV
1. ¿Qué cambia?
    - Ahora los valores se recorren a la derecha, se compara en el pseudocodigo con menor o igual.
2. ¿Qué comparación se modifica?
    - La de los valores con los de la derecha utilizando menor o igual, para descartar.
3. ¿Se conserva la misma estructura?
    - Yo digo que sí.
4. ¿La complejidad cambia?
    - Yo digo que no.

## Contraejemplo: Maximum Subarray Sum
1. ¿Serviría una pila monótona?
    - Creo que no necesariamente, porque ahora buscas subconjuntos dentre del arreglo yq eud eben estar todos juntos, no sabría como guardar eso en una pila.
2. ¿Qué información parece importante?
    - Los signos y las posiciones.
3. ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?
    - Porque además dentro del arreglo deben de estar juntos y su suma debe ser la más grande posible.

## Vista al futuro: Sliding Window
1. ¿Qué información entra? 
    - El número de elementos y el tamaño de la ventana (de los subconjuntos), además damos el contendio del arreglo.
2. ¿Qué información sale?
    - Los valores de en medio de los subconjuntos de k elementos.
3. ¿Qué información permanece?
    - Los tamaños y los datos.
4. ¿Por qué recalcular todo sería costoso?
    - Porque serian muas operaciones entre crear los nuevos arreglos, ordenarlos, buscar el número de en medio y guardarlo en una lista y eso para cada subconjunto.
5. ¿Qué tipo de estructura podría ayudar?
    - Un hashmap yo digo. ¿Cómo? No sé, pero me suena.

## Diseño de Pruebas
1. Diseña al menos dos pruebas propias.
    - Haré una con muchos numeros, y otra con un caso base sencillo.
2. Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.
    - Porque entonces estariamos admitiendo casos que no son solución del problema.
3. ¿Qué caso límite no debe faltar?
    - Cuando n pasa el límite superior.

## ¿Qué patrón descubrimos?
1. ¿Qué aprendimos sobre diseñar algoritmos?
    - Que tenemos que considerar la complejidad, la estrucura a utilizar y lo que realmente pide el problema para no trabajar con información que no nos sirve.
2. ¿Qué significa conservar candidatos útiles?
    - Que los datos que no nos servirán en la resolución los podemos ignorar o descartar.
3. ¿Qué invariante mantiene la pila?
    - Los datos útiles que no fueron reemplazados.
4. ¿Qué cambia entre simular y optimizar?
    - Simular funciona para ver el comportamiento del problema, optimizar es buscar la solución mas eficiente.
5. ¿Por qué no todos los problemas con arreglos usan la misma estructura?
    - Porque no todos buscan el mismo comportamiento o tienen más trabas o condiciones.
