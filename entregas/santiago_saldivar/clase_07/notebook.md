# Notebook - Clase 07

## 1. Presentación del laboratorio

¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?
Porque así podemos entender en qué se parecen y en qué se diferencian, y ver cómo eso encaja con los métodos de las estructuras.

## 2. Lectura estratégica

1. ¿Qué está pidiendo exactamente el problema?

La posición más cercana a la izquierda que tenga un valor menor.

2. ¿Cuál es la entrada?

La cantidad de números.

3. ¿Cuál es la salida?

Las posiciones de los números menores.

4. ¿Qué significa “más cercano a la izquierda”?

Que sea anterior y que su posición sea mayor respecto del resto de números anteriores.

5. ¿Qué pasa si no existe un valor menor?

Regresa 0.

6. ¿Qué casos extremos parecen importantes?

El que no tiene valor menor y el que tiene todos los valores menores.


## 3. Ingeniería inversa del algoritmo

1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?

Anotando los números y escribiendo las posiciones una por una si son menores.

2. ¿Qué información miras repetidamente?

El valor de los números.

3. ¿Qué información se vuelve inútil?

La que no esté a la izquierda.

4. ¿Qué operaciones se repiten?

Comparar los números para saber cuál es mayor y cuál menor. Y guardar los índices.

5. ¿Qué estructura podría ayudar?

Una pila.

## 4. Solución ingenua

- ¿Cuál sería la complejidad en el peor caso?

n al cuadrado

- ¿En qué tipo de arreglo se repetiría más trabajo?

Una cola.

- ¿Qué información se vuelve a revisar muchas veces?

Los valores de los números.
## 4.5. ¿Por qué la solución ingenua no escala?

- ¿Qué trabajo se repite?

Las comparaciones.

- ¿Qué valores anteriores pueden descartarse?

Los que sepamos mayores.

- ¿Cómo notarías que un valor ya no será buen candidato?

Si es mayor al que estamos trabajando.

## 5. Descubrimiento de la pila monótona

- ¿Qué significa que un candidato sea útil?

Que podría ser menor que el número que trabajamos, y así ser candidato para resolver el problema.

- ¿Por qué algunos candidatos dejan de servir?

Porque son mayores o iguales.

- ¿Qué propiedad debería mantener la estructura?

Los índices.

## 6. Pseudocódigo

- ¿Por qué se usa “mayor o igual” y no solo “mayor”?

Porque tiene que ser estrictamente menor. Valores iguales no queremos.

- ¿Qué representa el tope de la pila después de descartar candidatos?

El valor anterior más chico.

- ¿Cuál es el invariante de la pila?

El orden.

## 7. Variante: Nearest Greater Values

- ¿Qué cambia?

La condición del while será <=, pero nada más, realmente.

- ¿Qué comparación se modifica?

La del while: ahora busca valores menores o iguales. 

- ¿Se conserva la misma estructura?

Sí.

- ¿La complejidad cambia?

No.

## 8. Contraejemplo: Maximum Subarray Sum

- ¿Serviría una pila monótona?

Sí.

- ¿Qué información parece importante?

El valor de los números.

- ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?

Porque también depende del valor y de un grupo de ellos, que suman un entero.

## 9. Vista al futuro: Sliding Window

- ¿Qué información entra?

La cantidad de enteros y el tamaño de la ventana.

- ¿Qué información sale?

Las medianas.

- ¿Qué información permanece?

El valor de los enteros.

- ¿Por qué recalcular todo sería costoso?

Porque es hacer todas las comparaciones de nuevo.

- ¿Qué tipo de estructura podría ayudar?

Una pila.

## 10. Diseño de pruebas

- Diseña al menos dos pruebas propias.

Vaciar pila correctamente: revisa que el while vacíe la pila correctamente si es necesario.

Regresa lista: revisa que el return tenga el formato requerido.

- Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.

Porque buscamos valores estrictamente menores. Si sólo eliminamos valores menores, se nos puede escapar uno igual.

- ¿Qué caso límite no debe faltar?

El de un solo dato.

## 11. ¿Qué patrón descubrimos?

- ¿Qué aprendimos sobre diseñar algoritmos?

Que sirve mucho analizar el problema y hacer muchas pruebas con ejemplos para entenderle.

- ¿Qué significa conservar candidatos útiles?

No tener que recalcular la información que podría ser importante.

- ¿Qué invariante mantiene la pila?

El orden.

- ¿Qué cambia entre simular y optimizar?

Simular es como un experimento, pero al optimizar hacemos que corra más eficientemente.

- ¿Por qué no todos los problemas con arreglos usan la misma estructura?

Porque piden información y returns distintos.