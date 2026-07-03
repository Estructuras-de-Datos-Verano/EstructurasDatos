# Arturo Prudencio Bonilla

## seccion 1
- ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?

    Porque si el objetivo de los problemas es parecido o el funcionamiento del algortimo es parecido nos podemos apoyar en esos otros problemas para ver si nuestra estructura de datos es natural 

## seccion 3
1. ¿Qué está pidiendo exactamente el problema?
    - un algortimo que con un arreglo de n numeros, pueda arrojarte un lista con la posicion de los numeros mas pequeños y proximos desde la izquierda a cada posicion del arreglo inicial
2. ¿Cuál es la entrada?
    - un natural n y un arreglo con n de datos 
3. ¿Cuál es la salida?
    - una lista 
4. ¿Qué significa “más cercano a la izquierda”?
    - El umero mas proximo en direccion a la izquierda de la posicion de referencia
5. ¿Qué pasa si no existe un valor menor?
    - colocamos un 0
6. ¿Qué casos extremos parecen importantes?
    - que todos los numeros sean iguales o que no haya numeros


## seccion 4
1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?
    - tomaria cada numero he iria anotando el numero mas pequequeño y proximo a su izquierda 
2. ¿Qué información miras repetidamente?
    - la posicion y el valor del array
3. ¿Qué información se vuelve inútil?
    - los datos que estan a la derecha del numero que estamos tomando 
4. ¿Qué operaciones se repiten?
    - observar el valo y posicion y agregar a una lista
5. ¿Qué estructura podría ayudar?
    - no tengo idea jaja salud2


## seccion 5
- ¿Cuál sería la complejidad en el peor caso?

    cuadratica $O(n^{2})$
- ¿En qué tipo de arreglo se repetiría más trabajo?

    
- ¿Qué información se vuelve a revisar muchas veces?

    la posicion el valor de los elementos del array

## seccion 6
- ¿Qué trabajo se repite?

    revisar todo el array o casi todo¿


- ¿Qué valores anteriores pueden descartarse?

    los que sean mayores al "minimo local"


- ¿Cómo notarías que un valor ya no será buen candidato?

    que es estrictamente mayor que el "minimo local"

## seccion 7

- ¿Qué significa que un candidato sea útil?

    que sea menor o igual que el numero actual
- ¿Por qué algunos candidatos dejan de servir?

    porque exceden la cota local 
- ¿Qué propiedad debería mantener la estructura?

    que el ultimo valor util deba de ser faccil de acceder y que no consuma mucha memoria extraerlo o consultarlo 

## seccion 8 (pseudocodigo)

```text
crear pila vacía de pares (valor, posición)
crear lista de respuestas

para cada valor actual con su posición:
    mientras la pila no esté vacía y el tope sea mayor o igual al actual:
        desapilar

    si la pila está vacía:
        respuesta = 0
    si no:
        respuesta = posición del tope

    apilar (valor actual, posición actual)
```


- ¿Por qué se usa “mayor o igual” y no solo “mayor”?

    Para evitar errores en casos extremos, por ejemplo un array con todos los numeros iguales
- ¿Qué representa el tope de la pila después de descartar candidatos?

    El minimo local al que me referia antes, el cual es el numero mas pequeño y mas proximo al actual 
- ¿Cuál es el invariante de la pila?

    todos los apilados que fueron menores o iguales que el numero inmediato a la derecha (la pila debe comportararse de manera estrictamente creciete de izquieerda a derecha)

## seccion 10
- ¿Qué cambia?

    la relacion que debe haber (ya no es menor sino mayor)
- ¿Qué comparación se modifica?

    la comparacion de valor
- ¿Se conserva la misma estructura?

    si
- ¿La complejidad cambia?

    no 

## seccion 11
- ¿Serviría una pila monótona?

    si, una pila que registre las sumas grandes
- ¿Qué información parece importante?

    las sumas utiles    
- ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?

    porque no solo nos importa la sunma sino si cumple ciertas condicines y tambien de donde se original suma 


## seccion 12

- ¿Qué información entra?

    dos enteros
- ¿Qué información sale?

    una lista con las medianas
- ¿Qué información permanece?

    el array
- ¿Por qué recalcular todo sería costoso?

    porque necesitas hacerlo muchas veces, hasta agotar todo el array
- ¿Qué tipo de estructura podría ayudar?

    no se

## seccion 13

- Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.

    porque si no, las pruebas extras que diseñe no pasarian, por poner un ejemplo, es como la prueba que terminamos, en la cual se bloquea el tope con un numero igual
- ¿Qué caso límite no debe faltar?

    un array de un solo eemento, un array con todos los elementos iguales y no se me ocurre ninguno mas 

## seccion 14

- ¿Qué aprendimos sobre diseñar algoritmos?

    poner multiples barreras de seguridad para que el algortimo funcione como esperamos aunque no se le trate "bien"
- ¿Qué significa conservar candidatos útiles?

    guardar en la memoria datos que necesataremos luego pero ya obtuvimos del pasado
- ¿Qué invariante mantiene la pila?

    los candidatos que no fueron "remplazados" 
- ¿Qué cambia entre simular y optimizar?

    que uno solo cumple y el otro lo hace de la mejor manera posible (idk)
- ¿Por qué no todos los problemas con arreglos usan la misma estructura?

    porque aunque todos usen el mismo datos (arreglos) no todos deben de ser operados igual o no siempre queremos la misma infromacion 