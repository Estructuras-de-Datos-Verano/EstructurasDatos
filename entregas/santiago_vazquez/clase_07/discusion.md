# Discusión Técnica: Nearest Smaller Values

## 1. Problema y primera idea
El problema exige encontrar, para cada elemento de un arreglo, el índice del elemento estrictamente menor más cercano hacia la izquierda. La primera idea intuitiva (simulación) es iterar hacia atrás desde la posición actual hasta encontrar dicho valor.

## 2. Por qué la solución ingenua repite trabajo
El modelo ingenuo tiene una complejidad de O(n^2)en el peor caso. Si analizamos un arreglo monótono decreciente, para calcular la respuesta del elemento $i$, tenemos que verificar inútilmente los $i-1$ elementos anteriores, repitiendo esta búsqueda exhaustiva para cada paso.

## 3. Información útil e información descartable
Si un elemento en la posición j es mayor o igual a un elemento en la posición i (con j < i), entonces el elemento j jamás será la respuesta para un índice futuro k > i. La información útil son aquellos valores que pueden seguir siendo un mínimo para elementos venideros.

## 4. Elección de estructura
Pila. Nos permite siempre comparar nuestro número actual contra el "mejor candidato disponible más cercano", y si ese candidato resulta inservible, lo expulsamos (pop) en tiempo constante amortizado.

## 5. Variante: Nearest Greater Values
Basta con alterar la condición analítica: en lugar de descartar candidatos mayores o iguales, descartamos candidatos menores o iguales. La pila mantendrá un invariante monótono decreciente.

## 6. Contraejemplo: Maximum Subarray Sum
Encontrar la suma máxima no depende exclusivamente de un orden estricto de adyacencia de elementos singulares, sino de cómo se acumulan (sumas prefijas). Una pila no nos sirve porque no podemos simplemente "descartar" un elemento individual, su valor contribuye a toda la subsecuencia.

## 7. Sliding Window
Cuando hay una ventana de tamaño fijo, la información caduca por su antigüedad (su índice queda fuera de la ventana). Aunque la noción de descartar información inservible por dominancia se mantiene, una pila no basta porque no podemos sacar elementos del fondo fácilmente; requerimos una doble cola (Deque).

## 8. Invariante
El núcleo de la demostración de correctitud es el invariante de la estructura: En cualquier iteración, los elementos vivos dentro de la pila configuran una sucesión estrictamente creciente tanto en sus valores como en sus posiciones originales.

## 9. Pruebas
Diseñé pruebas clave como el arreglo de elementos iguales. Si no somos estrictos con `>=`, la pila interpretaría elementos idénticos como menores.

## 10. Complejidad
El algoritmo parece anidado (un `while` dentro de un `for`), pero un análisis riguroso nos dice que cada elemento es apilado (Push) exactamente una vez, y es desapilado (Pop) a lo sumo una vez. Por lo tanto, el número total de operaciones de pila es como máximo 2n. Esto arroja una complejidad temporal óptima de O(n) y espacial O(n)

## 11. Cómo descubrimos el algoritmo
Pasamos de intentar forzar la respuesta recalculando todo, a pensar deductivamente: "¿Qué condición garantiza que un dato anterior es absoluta y definitivamente inútil para el futuro?".

## 12. Pregunta abierta
¿Cómo modificaríamos eficientemente esta estructura si el arreglo de entrada estuviese siendo actualizado en tiempo real?