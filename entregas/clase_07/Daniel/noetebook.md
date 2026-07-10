# primera sección

Responde  ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?
 - vemos las caracteristicas de cada problema y deliberamos para ver que estructura
   de datos nos va a ayudar mas y la capacidad de decidir lo hara la prectica




## 3. Lectura estratégica

1. ¿Qué está pidiendo exactamente el problema?
  - que dada una lista s va recorriendo número por número y a cada numero le dice la posición
    mas cercana hacia la izquierda de un numero menor sobre el cual estamos trabajando
2. ¿Cuál es la entrada?
  - es una lista de números enteros
3. ¿Cuál es la salida?
  - una lista de posiciones, marcadas con numeros naturales
4. ¿Qué significa “más cercano a la izquierda”?
  - en la posición de izquierda a derecha donde se encuentra el número menor al número en el que estamos trabajando
5. ¿Qué pasa si no existe un valor menor?
  - si no eiste un número menor  -> devuelve un 0 en la respuesta en esa posición específica
6. ¿Qué casos extremos parecen importantes?
  - donde nos devuelva puros 0 que lo conseguimos haciendo una lista en orden descendente




## 4. Ingeniería inversa del algoritmo


1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?
  - escribira una lista de muneros y me fijaria en el primero y como no hay ningun número a su izquierda regresaria un cero 
    y para el otro número veria si es mayor que el primero si si pongo 1 y si no pongo 0 y asi susesivamente hasta terminar
    con la lista.
2. ¿Qué información miras repetidamente?
  - identificar si es cero o algun número natural ya que esto se ve si los números anteriores son mas grandes o hay alguno que
    no, eso es facil identificarlo
   3. ¿Qué información se vuelve inútil?
  - se vuelve inútil pues todos los números que no te sirven para la revisión es decir que son mayores
4. ¿Qué operaciones se repiten?
  - el ciclo que se repite es el de verificar si en los puestos anteriores hay numeros menores y en que lugar del puesto
5. ¿Qué estructura podría ayudar?
  - una cola, el FIFO es muy util para empezar a trbajar en orden los elementos


## 5. Solución ingenua


- ¿Cuál sería la complejidad en el peor caso?
  - anteriormente mencionamos el peor caso que seria con una lista en orden descendiente y la complejidad radica en que 
    en escencia toda la repuesta sera 0 y esto obliga al programa a trabajar de más 
- ¿En qué tipo de arreglo se repetiría más trabajo?
  - como anteriormente mencionamos le costaria mas trabajo a la maquina por el hecho de recorrer mas filas
- ¿Qué información se vuelve a revisar muchas veces?
  - por ejemplo si los números son menores se lleva a cabo la opercion de verificar si son menores que los 
    siguientes números


## 6. ¿Por qué la solución ingenua no escala?


- ¿Qué trabajo se repite?
  - identificar si es cero o algun número natural ya que esto se ve si los números anteriores son mas grandes o hay alguno que
    no, eso es facil identificarlo
- ¿Qué valores anteriores pueden descartarse?
  - los que son maximos y no aportan demasiado a la lectura
- ¿Cómo notarías que un valor ya no será buen candidato?
  - si acaso noto que en número es demasiado grande en comparación con los otros valores ya los sescartaría como buen candidato

## 7. Descubrimiento de la pila monótona

- ¿Qué significa que un candidato sea útil?
  - que relativamente sea menor a la media de todos los valores 
- ¿Por qué algunos candidatos dejan de servir?
  - por que son mayores a la media y ya no son muy considerados a la hora de hacer la acción
- ¿Qué propiedad debería mantener la estructura?
  - el que sea clara y no cometa errores de intención 

## 8. Pseudocódigo parcial



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
en este pseudocodigo podemos notar que al inicio crea la pila que nos servira para hacer el programa
personalimente hubiese preferido una cola y recorre posicion por posición y ejecuta el programa y hace
su lista de posiciones y esa la regresa


- ¿Por qué se usa “mayor o igual” y no solo “mayor”?
  - en escencia por que como python empieza en cero si es mayor igual sera mayor estricto en teminos tecnicos
- ¿Qué representa el tope de la pila después de descartar candidatos?
  - al valor maximo de la lista 
- ¿Cuál es el invariante de la pila?
  - el primero que siempre regresa un cero debido a que no tiene númeroa a su izquierda
    y si si? tiene entonces no es el primero

## 10. Variante: Nearest Greater Values

Variante natural: para cada posición, encontrar la posición más cercana a la izquierda con valor mayor.

- ¿Qué cambia?
  - en escencia es otro problema lo prinncipal que llega a cambiar es que ahora en ves de buscar un numero menor
    ahora buscara un numero mayor
- ¿Qué comparación se modifica?
  - en lugar de menor igual, sera maypr igual
- ¿Se conserva la misma estructura?
  - en escencia si solo cambiamos el menor por el mayor
- ¿La complejidad cambia?
  - si, ahora el caso mas complejo es cuando 

## 11. Contraejemplo: Maximum Subarray Sum

Este problema pide encontrar la suma máxima de un subarreglo no vacío.

- ¿Serviría una pila monótona?
  - si por la acumulacion de valores de algun lado de la pila
- ¿Qué información parece importante?
  - lo de la necesidad de monotonia para mayor facilidad
- ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?
  - porque ya es hablar de subconjuntos y eso es mas complejo

## 12. Vista al futuro: Sliding Window)

En una ventana deslizante, algunos elementos entran, otros salen y otros permanecen.

- ¿Qué información entra?
  - una pila de n números
- ¿Qué información sale?
  - la media de esos n números
- ¿Qué información permanece?
  - toda la información de la pila 
- ¿Por qué recalcular todo sería costoso?
  - por que las posibilidades se vuelven factorialmente muy grandes y hacer todos esos calculos es muy costoso para la pc
- ¿Qué tipo de estructura podría ayudar?
  - una pila ayudaria bastante

## 13. Diseño de pruebas

- Diseña al menos dos pruebas propias.
  - por ejemplo ahora que el menor este ha la derecha y que el mayor este a la derecha con la misma plantlla anterior
- Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.
  - por que python como empieza a contar en 0 con el > pierdes generalidad
- ¿Qué caso límite no debe faltar?
  - si, no debe faltar siempre conocer el limite del codigo


## 14. ¿Qué patrón descubrimos?

- ¿Qué aprendimos sobre diseñar algoritmos?
  - es importante saber que estas haciendo antes de hacerlo
- ¿Qué significa conservar candidatos útiles?
  - ahorrarle chamba a la pc
- ¿Qué invariante mantiene la pila?
  - un programa que vayaacorde a la pila
- ¿Qué cambia entre simular y optimizar?
  - simular es unicamente ver que funcione en cambio optimizar es hacerlo mejor para que funcione mejor
- ¿Por qué no todos los problemas con arreglos usan la misma estructura?
  - por que los problemas son diferentes

      






