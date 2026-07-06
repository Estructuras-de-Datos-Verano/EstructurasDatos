**Responde en `notebook.md`:** ¿Por qué crees que comparar problemas ayuda a elegir estructuras de datos?

***Porque así vemos las distintas implementaciones y diferentes usos***

## 1. Lectura estratégica

Responde en `notebook.md`:

1. ¿Qué está pidiendo exactamente el problema?

***Que para cada elemento de una sucesión, encontrar el índice (basado en 1) del elemento más cercano a su izquierda que sea estrictamente menor a él.***

2. ¿Cuál es la entrada?

***Un número n y un arreglo de n enteros.***

3. ¿Cuál es la salida?

***Un arreglo de n enteros que representan las posiciones (índices) de los valores menores más cercanos.***

4. ¿Qué significa “más cercano a la izquierda”?

***Pues que para una posición i, buscamos el máximo índice j tal que j < i y A[j] < A[i].***

5. ¿Qué pasa si no existe un valor menor?

***Se devuelve 0***

6. ¿Qué casos extremos parecen importantes?

***Arreglos estrictamente crecientes (todos tienen un menor a la izquierda), arreglos estrictamente decrecientes (ninguno tiene un menor a la izquierda), y arreglos con valores repetidos.***

## 2. Ingeniería inversa del algoritmo

Responde en `notebook.md`:

1. ¿Cómo resolverías un ejemplo pequeño con papel y lápiz?

***Pues primero revisaría el número actual y miro hacia atrás uno por uno hasta encontrar un número menor. Anoto su posición.***

2. ¿Qué información miras repetidamente?

***Los números que acabo de procesar recientemente.***

3. ¿Qué información se vuelve inútil?

***Sería el número grande que está a la izquierda de un número pequeño. El número pequeño siempre será un "mejor candidato" (por ser más pequeño y estar más cerca) para cualquier elemento futuro.***

4. ¿Qué operaciones se repiten?

***Retroceder posiciones índice por índice.***

5. ¿Qué estructura podría ayudar?

***Una Pila, ya que el acceso a los datos sigue LIFO. Porque miramos siempre a los vecinos más recientes primero.***

## 3. Solución ingenua

Primera idea: para cada posición, caminar hacia la izquierda hasta encontrar el primer valor menor.

Pseudocódigo parcial:

```text
para cada posición i:
    respuesta = 0
    revisar j = i - 1, i - 2, ..., 1
        si numeros[j] < numeros[i]:
            respuesta = j
            detener búsqueda
```

Responde en `notebook.md`:

- ¿Cuál sería la complejidad en el peor caso?

***En el peor caso la complejidad es O(n^2) porque para el elemento i retrocedemos i-1 pasos.***

- ¿En qué tipo de arreglo se repetiría más trabajo?

***Arreglos ordenados de forma descendente ([5, 4, 3, 2, 1]).***

- ¿Qué información se vuelve a revisar muchas veces?

***Los elementos grandes que nunca serán respuesta para nadie, pero que la búsqueda ingenua tiene que "saltar" una y otra vez.***

## 4. ¿Por qué la solución ingenua no escala?

Si para muchas posiciones caminamos casi todo el arreglo hacia atrás, el costo puede acercarse a `O(n^2)`.

Responde en `notebook.md`:

- ¿Qué elementos vuelves a inspeccionar varias veces aunque ya conocías su información?

***Inspeccionamos repetidamente elementos que sabemos que son más grandes que los elementos recientes.***

- ¿Qué condición hace que un valor anterior nunca vuelva a ser la mejor respuesta para un elemento futuro?

***Si un elemento A[j] \ A[i] con j < i, el elemento A[j] está "dominado" por A[i]. Nunca será la respuesta para un índice futuro k > i.***

- ¿Qué comparación concreta puedes hacer con el elemento actual para decidir inmediatamente que un candidato ya no volverá a ser útil?

***Si el candidato anterior es mayor o igual al elemento actual, lo descartamos permanentemente.***

## 5. Descubrimiento de la pila monótona

La idea central:

> conservar únicamente candidatos útiles.

Si un valor anterior es mayor o igual que el valor actual, deja de ser útil para posiciones futuras donde el valor actual esté más cerca y sea menor o igual.

Esto sugiere mantener candidatos en una estructura donde podamos quitar los candidatos recientes que ya no sirven.

Responde en `notebook.md`:

- ¿Qué significa que un candidato sea útil?

***Un elemento que aún tiene posibilidad de ser el "menor más cercano" para algún elemento a su derecha.***

- ¿Por qué algunos candidatos dejan de servir?

***Porque aparece un elemento más a la derecha que es igual o más pequeño, volviéndolo obsoleto.***

- ¿Qué propiedad debería mantener la estructura?

***Los elementos en la estructura deben estar estrictamente ordenados de menor a mayor (una pila monótona creciente).***


## 6. Pseudocódigo parcial

Completa la explicación en `notebook.md`.

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

Responde en `notebook.md`:

- ¿Por qué se usa “mayor o igual” y no solo “mayor”?

***Si usamos solo "mayor", dejaríamos en la pila valores que son idénticos al actual. Si buscamos el estrictamente menor, un valor igual no nos sirve y bloquea la búsqueda de uno que sí sea menor.***

- ¿Qué representa el tope de la pila después de descartar candidatos?

***Representa exactamente la posición del valor menor más cercano a la izquierda del elemento actual.***

- ¿Cuál es el invariante de la pila?

***Desde la base hasta el tope, los valores almacenados son siempre estrictamente crecientes.***

## 7. Variante: Nearest Greater Values

Variante natural: para cada posición, encontrar la posición más cercana a la izquierda con valor mayor.

Responde en `notebook.md`:

- ¿Qué cambia?

***Buscamos el mayor en vez del menor.***

- ¿Qué comparación se modifica?

***Descartamos mientras el tope sea menor o igual al actual.***

- ¿Se conserva la misma estructura?

***Se conserva la pila monótona, pero su invariante cambia a ser monótona decreciente.***

- ¿La complejidad cambia?

***Sigue siendo O(n), ya que cada elemento entra y sale de la pila a lo sumo una vez.***

## 8. Contraejemplo: Maximum Subarray Sum

Referencia: [CSES Problem Set - Maximum Subarray Sum](https://cses.fi/problemset/task/1643/)

Este problema pide encontrar la suma máxima de un subarreglo no vacío.

No lo resolveremos completo.

Responde en `notebook.md`:

- ¿Serviría una pila monótona?

***No***

- ¿Qué información parece importante?

***Importa la suma acumulada (sumas prefijas) y el valor mínimo histórico de dicha suma, no solo una relación de orden elemento por elemento.***

- ¿Por qué este problema no es simplemente “conservar candidatos ordenados”?

***No estamos descartando candidatos individuales basados en un orden de acual está pegado, sino evaluando segmentos contiguos completos.***

## 9. Vista al futuro: Sliding Window

Referencia: [CSES Problem Set - Sliding Window Median](https://cses.fi/problemset/task/1076/)

En una ventana deslizante, algunos elementos entran, otros salen y otros permanecen.

No lo resolveremos completo.

Responde en `notebook.md`:

- ¿Qué información entra?

***El nuevo elemento que desliza a la derecha***

- ¿Qué información sale?

***El elemento más antiguo de la ventana (caduca por tiempo/índice).***

- ¿Qué información permanece?

***Los candidatos viables dentro del tamaño de la ventana k.***

- ¿Por qué recalcular todo sería costoso?

***Sería ineficiente.***

- ¿Qué tipo de estructura podría ayudar?

***Una colaDeque porque necesitamos descartar por valor (como en la pila) y descartar por antigüedad (como en una cola).***

## 10. Diseño de pruebas

Ahora tú también debes diseñar pruebas.

Las pruebas públicas completas incluyen:

- ejemplo oficial;
- arreglo creciente;
- arreglo decreciente.

En `tests/test_publico_nearest_smaller.py` hay TODOs guiados.

Responde en `notebook.md`:

- Diseña al menos dos pruebas propias.
- Explica por qué una prueba debe detectar el error de usar `>` en lugar de `>=`.

***Una prueba como [2, 2] fallaría con > porque la pila mantendría el primer 2 y diría erróneamente que el menor más cercano es la posición 1, cuando debería ser 0 (no hay un valor estrictamente menor).***

- ¿Qué caso límite no debe faltar?

Un arreglo de un solo elemento [10].

## 11. ¿Qué patrón descubrimos?

Ficha de patrón:

```text
Patrón: información monotónica
Pregunta que lo activa: ¿estoy recalculando información que ya conocía?
Información que se conserva: candidatos útiles
Estructura típica: pila monótona o deque monótona
Problemas ejemplo: Nearest Smaller Values, Nearest Greater Values, Sliding Window
Problema donde no aplica directamente: Maximum Subarray Sum
```

Responde en `notebook.md`:

- ¿Qué aprendimos sobre diseñar algoritmos?

***Optimizar muchas veces significa identificar un "invariante" y usar una estructura que lo preserve naturalmente.***

- ¿Qué significa conservar candidatos útiles?

***Guardar solo la información que, lógicamente, tiene posibilidad de ser parte de la solución en iteraciones futuras.***

- ¿Qué invariante mantiene la pila?

***La pila mantiene elementos ordenados estrictamente de menor a mayor.***

- ¿Qué cambia entre simular y optimizar?

***Simular es traducir el problema literalmente, y optimizar es usar propiedades algebraicas o lógicas de los datos para evitar redundancias.***

- ¿Por qué no todos los problemas con arreglos usan la misma estructura?

***Pues porque evidentemente varian las implementaciones y soluciones a los diferentes problemas***