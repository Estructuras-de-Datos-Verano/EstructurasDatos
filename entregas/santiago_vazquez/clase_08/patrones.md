# Catálogo de patrones - Clase 08

Nombre: Santiago Vázquez Serna

## Patrón 1: Simulación

Problema ejemplo: Josephus Problem.
Pregunta detonadora: "¿El tamaño del problema (n) es suficientemente pequeño como para que simplemente hacer paso a paso lo que dice el enunciado pase en tiempo?"
Estructuras que suelen aparecer: Colas, Arreglos.
Ejemplo en clase: Resolver Josephus pasando el primer elemento al final de la cola hasta que quede uno.
Cuándo usarlo: Cuando las reglas son arbitrarias, no hay un patrón matemático inmediato o la complejidad O(n^k) es tolerable por el tamaño de la entrada.
Cuándo no usarlo: Cuando el número de iteraciones ya es muy grande.

## Patrón 2: Información monotónica

Problema ejemplo: Nearest Smaller Values.
Pregunta detonadora: "¿Hay información pasada que, lógicamente, jamás volverá a ser la respuesta óptima debido a que un dato más reciente la 'domina'?"
Estructuras que suelen aparecer: Pilas (Stacks), Colas de prioridad.
Ejemplo en clase: Usar una pila para descartar (pop) valores grandes cuando encontramos un valor más pequeño a su derecha.
Cuándo usarlo: Cuando necesitamos encontrar el "siguiente mayor/menor" y el problema permite descartar candidatos permanentemente basándonos en una relación de orden (transitividad).
Cuándo no usarlo: Cuando necesitamos realizar consultas o modificaciones históricas de elementos aislados (para eso mejor un Árbol de Segmentos).

## Patrón 3: Ventana Deslizante (Sliding Window)

Problema ejemplo: Encontrar la suma máxima de un subarreglo contiguo de tamaño exactamente $k$.
Pregunta detonadora: "¿El problema me pide optimizar una métrica sobre un segmento contiguo que avanza hacia la derecha progresivamente?"
Estructuras que suelen aparecer: Colas dobles, Acumuladores de suma, Diccionarios (para frecuencias).
Ejemplo en clase o recurso consultado: NeetCode / William Fiset. Avanzar el puntero derecho para agregar elementos y avanzar el izquierdo para sacar los que ya "caducaron".
Cuándo usarlo: Cuando recalculamos estados sobre segmentos contiguos y traslapados. Permite bajar de O(n \k) a O(n).
Cuándo no usarlo: Si los elementos no son contiguos (subsecuencias en lugar de subarreglos) o si no hay orden lógico para expandir/contraer la ventana.

## Patrón 4: Dos Punteros (Two Pointers)

Problema ejemplo: Encontrar dos números en un arreglo ordenado que sumen un valor x.
Pregunta detonadora: "¿Tengo un arreglo ordenado y necesito encontrar un par o un subconjunto que cumpla cierta propiedad acotando los extremos?"
Estructuras que suelen aparecer: Arreglos ordenados.
Ejemplo en clase o recurso consultado: GeeksforGeeks. Un puntero al inicio y otro al final; según la suma, movemos el izquierdo a la derecha (para aumentar) o el derecho a la izquierda (para disminuir).
Cuándo usarlo: Para problemas de pares, inversiones o particiones en espacio extra O(1).
Cuándo no usarlo: Cuando el arreglo no puede ser ordenado porque perderíamos los índices originales, y usar diccionarios sería más rápido.

## Comparación breve

Escoge dos patrones y explica en qué se parecen y en qué se diferencian.

Ventana Deslizante vs Dos Punteros: Ambos utilizan punteros de índice (izquierdo y derecho) que avanzan en una sola dirección, logrando tiempo lineal O(n). Sin embargo, la Ventana Deslizante siempre analiza la información contenida entre los punteros (un subarreglo contiguo), mientras que los Dos Punteros suelen analizar combinaciones de pares ubicados exactamente *en* la posición de los punteros, y generalmente requieren que los datos estén ordenados previamente.

## Pregunta abierta

¿Qué patrón te parece más difícil de reconocer antes de escribir código?

Probablemente la Información Monotónica.