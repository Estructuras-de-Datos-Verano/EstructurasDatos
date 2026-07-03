
# Notebook - Clase 07

## 1. Presentación del laboratorio
-¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos? Porque comparando problemas puedes valorar el tipo de procesamiento que requieres implementar para cierta información, y con ver problemas similares puedes notar que usar la misma estructura de datos que usaste previamente es natural para el nuevo problema
## 2. Lectura estratégica
1. ¿Qué está pidiendo exactamente el problema? Que dada una lista con n números, encontremos al menor número a la izquierda, guardemos la posición (contando desde el 1 porque 0 representa que no exista un entero menor) y la metamos en una lista. Al final, como esto ocurre para cada número en la lista, tendremos una lista cuyas entradas son la posición más cercana en la que apareció un entero menor a la izquierda de éste. 
2. ¿Cuál es la entrada? Una lista de números
3. ¿Cuál es la salida? Una lista de números
4. ¿Qué significa “más cercano a la izquierda”? Estar entre el primer elemento list[0] y list[k-1] donde k es el número "iterado" en ese paso.
5. ¿Qué pasa si no existe un valor menor? Se pone cero. 
6. ¿Qué casos extremos parecen importantes? Negativos, números no enteros, longitudes de listas muy grandes, etc. 
## 3. Ingeniería inversa del algoritmo
1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz? Escribiendo la lista como posiciones simbolizadas con guiones bajos donde arriba del guión iría el número original y abajo la posición a la izquierda en la que apareció un número menor. También se me ocurre dibujar dos óvalos (como cuando representas una relación de conjuntos) dónde uno tiene como elementos los de la lista original y el otro las posiciones posibles (que son, naturalmente, todas las posiciones posibles en la lista). El problema con esa segunda representación visual es que, ante repeticiones, tendríamos varias flechas saliendo del mismo número.
2. ¿Qué información miras repetidamente? Los números de la lista. 
3. ¿Qué información se vuelve inútil? Los números a la derecha de el número "iterado" en ese paso. 
4. ¿Qué operaciones se repiten? De momento, iterar, añadir elementos (append) según sea necesario. También, hasta ahora no veo necesidad de borrar cosas, solo usaría dos listas (al inicio una vacía) y en ésta iría guardando la información.
5. ¿Qué estructura podría ayudar? Se me hace natural usar listas (que en realidad son pilas)
- ¿Cuál sería la complejidad en el peor caso? En el peor caso (solución ingenua), teniendo una lista en órden decreciente, se realizan k-1 operaciones por cada entero k (o 1 si k = 1). Como hay n enteros, vamos a hacer "1 + 2+...+n-1" = n((n-1)/2) operaciones. Por lo tanto, la complejidad es O(n^2).
- ¿En qué tipo de arreglo se repetiría más trabajo? En uno decreciente porque hay que comparar con todos los anteriores cada vez. 
- ¿Qué información se vuelve a revisar muchas veces? Los elementos previos. 
- ¿Qué elementos vuelves a inspeccionar varias veces aunque ya conocías su información? Los enteros previos que ya habíamos revisado porque se vuelven a comparar pero ahora con el siguiente iterado. 
- ¿Qué condición hace que un valor anterior nunca vuelva a ser la mejor respuesta para un elemento futuro? Que ninguno de los valores anteriores sea el menor más cercano. En otras palabras, mientras el primer elemento a la izquierda sea menor, va a ser la mejor respuesta en vez de las anteriores. De aquí se sigue que el mejor escenario sea una lista creciente. 
- ¿Qué comparación concreta puedes hacer con el elemento actual para decidir inmediatamente que un candidato ya no volverá a ser útil? Si entero_actual > entero_actual - 1 ya evutamos el resto de comparaciones.
- ¿Qué significa que un candidato sea útil? Que sea menor al actual
- ¿Por qué algunos candidatos dejan de servir? Si ese candidato es mayor al actual se puede descartar inmediatamente
- ¿Qué propiedad debería mantener la estructura? No entiendo la pregunta, pero supongo que el órden, porque la nueva "pila" o lista debe preservar las posiciones en el órden en el que se comparó con ese entero. 
## 4. Solución ingenua
- ¿Cuál sería la complejidad en el peor caso? En el peor caso (solución ingenua), teniendo una lista en órden decreciente, se realizan k-1 operaciones por cada entero k (o 1 si k = 1). Como hay n enteros, vamos a hacer "1 + 2+...+n-1" = n((n-1)/2) operaciones. Por lo tanto, la complejidad es O(n^2).
- ¿En qué tipo de arreglo se repetiría más trabajo? En uno decreciente porque hay que comparar con todos los anteriores cada vez. 
- ¿Qué información se vuelve a revisar muchas veces? Los elementos previos. 
- ¿Qué elementos vuelves a inspeccionar varias veces aunque ya conocías su información? Los enteros previos que ya habíamos revisado porque se vuelven a comparar pero ahora con el siguiente iterado. 
## 5. Descubrimiento de la pila monótona
- ¿Qué elementos vuelves a inspeccionar varias veces aunque ya conocías su información? Los enteros previos que ya habíamos revisado porque se vuelven a comparar pero ahora con el siguiente iterado. 
- ¿Qué condición hace que un valor anterior nunca vuelva a ser la mejor respuesta para un elemento futuro? Que ninguno de los valores anteriores sea el menor más cercano. En otras palabras, mientras el primer elemento a la izquierda sea menor, va a ser la mejor respuesta en vez de las anteriores. De aquí se sigue que el mejor escenario sea una lista creciente. 
- ¿Qué comparación concreta puedes hacer con el elemento actual para decidir inmediatamente que un candidato ya no volverá a ser útil? Si entero_actual > entero_actual - 1 ya evutamos el resto de comparaciones.
- ¿Qué significa que un candidato sea útil? Que sea menor al actual
- ¿Por qué algunos candidatos dejan de servir? Si ese candidato es mayor al actual se puede descartar inmediatamente
- ¿Qué propiedad debería mantener la estructura? No entiendo la pregunta, pero supongo que el órden, porque la nueva "pila" o lista debe preservar las posiciones en el órden en el que se comparó con ese entero. 
## 6. Pseudocódigo
## Pseudocódigo parcial
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
- ¿Por qué se usa “mayor o igual” y no solo “mayor”? Porque ser igual no es ser menor y sólo nos interesan menores. 
- ¿Qué representa el tope de la pila después de descartar candidatos? El menor entero a la izquierda de cada entero en la lista original
- ¿Cuál es el invariante de la pila? Pues, de haber un invariante, este es el menor más cercano de cualquier número a la derecha.
## 7. Variante: Nearest Greater Values
- ¿Qué cambia? Solo que buscamos el mayor valor en vez del menor
- ¿Qué comparación se modifica? while stack_pares and stack_pares[-1][0] >= val, solo cambia el mayor/igual por menor
- ¿Se conserva la misma estructura? Si
- ¿La complejidad cambia? NO
## 8. Contraejemplo: Maximum Subarray Sum
- ¿Serviría una pila monótona? Sí, pero la complejidad sería muy alta. Por cada subconjunto de k elementos harías una suma de todos los elementos. Entonces vas a ser operaciones con absolutamente todos los subconjuntos de todos los tamaños posibles y luego compararlos. 
- ¿Qué información parece importante? Conservar los valores de las sumas.
- ¿Por qué este problema no es simplemente “conservar candidatos ordenados”? Porque se requiere de demasiadas operaciones con ese enfoque, y además podría fallar la lógica de solo a la izquierda si a la derecha hubo una suma más grande.
## 9. Vista al futuro: Sliding Window
- ¿Qué información entra? El tamaño de la lista y el tamaño de las ventanas.
- ¿Qué información sale? Una lista con las medianas de cada ventana.
- ¿Qué información permanece? El número de la lista que corresponde a la mediana.
- ¿Por qué recalcular todo sería costoso? Porque se repiten las operaciones y eso suma más a la complejidad (porque además dependen del tamaño de las ventanas entonces no son solo constantes)
- ¿Qué tipo de estructura podría ayudar? Supongo que Deque.
## 10. Diseño de pruebas
- Diseña al menos dos pruebas propias.
def test_valores_mayores_decreciente():
    """Si la lista va bajando, cada número tiene como mayor cercano al de su izquierda."""
    assert valores_mayores_cercanos([30, 20, 10]) == [0, 1, 2]

def test_valores_menores_creciente():
    """Si la lista va subiendo, cada número tiene como menor cercano al de su izquierda."""
    assert valores_mayores_cercanos([10, 20, 30]) == [0, 1, 2]
def test_valores_menores_negativos():
    """Debe comportarse igual con los signos negativos"""
    assert valores_menores_cercanos([-2, -1, 0]) == [0, 1, 2]

- Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`. Porque si aceptamos usar solo mayor estaríamos considerando com menor cercano a un número anterior igual al actual, y eso va a ser que la lista de respuestas no sea la esperada en el assert del test.
- ¿Qué caso límite no debe faltar? Creo que con checar que funcione con listas crecientes/decrecientes y negativos basta
- ¿Qué aprendimos sobre diseñar algoritmos? Que diseñar uno de forma correcta puede atacar varios problemas con solo algunos camios lógicos.
- ¿Qué significa conservar candidatos útiles? Guardar los números menores al actual. 
- ¿Qué invariante mantiene la pila? El mínimo. 
- ¿Qué cambia entre simular y optimizar? No entiendo estas preguntas, ¿simular qué?
- ¿Por qué no todos los problemas con arreglos usan la misma estructura? Porque muchos, como el contraejemplo que vimos, requieren estructuras de datos que vuelvan menos complejo el algortimo
## 11. ¿Qué patrón descubrimos? 
-No entiendo a qué se refiere la pregunta, pero puedo decir que en general los problemas de comparar enteros tienen siempre una forma de ahorrar operaciones agarrando candidatos y descartándolos/conservándolos según convenga. 