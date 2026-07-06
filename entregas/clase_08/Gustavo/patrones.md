# Catálogo Técnico de Patrones de Resolución de Problemas

En este documento analizo 4 patrones algorítmicos clave, separando su base matemática, las estructuras de datos que los hacen funcionar y las situaciones concretas en las que deberíamos utilizarlos en nuestro código.

---

## Patrón 1: Simulación

### Problema ejemplo
El problema clásico de **Josephus**: un grupo de personas se organiza en un círculo y se elimina a cada $k$-ésima persona de manera sistemática y continua hasta que solamente queda un sobreviviente. Queremos saber la posición original de la última persona en pie.

### Pregunta detonadora
*¿Cómo podemos modelar de manera precisa y paso a paso el cambio de estado físico o lógico de un proceso, respetando estrictamente sus reglas secuenciales sin que nuestro programa pierda la noción del tiempo o del orden?*

### Estructuras que suelen aparecer
* Colas de doble fin (`collections.deque` en Python).
* Arreglos estáticos circulares o arreglos dinámicos con índices controlados por aritmética modular (`índice % n`).
* Listas enlazadas circulares.

### Ejemplo visto en clase o encontrado en recursos
En la simulación algorítmica con una cola (`deque`), representamos a las personas con los números del $1$ al $n$. Para imitar el avance en el círculo, tomamos al primer elemento con un `.popleft()` y, si no le toca ser eliminado, lo reinsertamos al final de la fila con un `.append()`. Si le toca ser eliminado, simplemente lo descartamos y no vuelve a entrar. Repetimos este ciclo una y otra vez hasta que la longitud de nuestra cola sea igual a $1$.

### Cuándo usarlo
* Cuando las reglas del problema dictan un comportamiento dependiente del paso anterior y resulta muy complejo encontrar una fórmula directa que resuelva todo en un solo cálculo algebraico.
* Cuando el volumen de entradas ($n$) es pequeño o moderado, permitiendo que la computadora procese cada paso en un tiempo razonablemente rápido.
* En modelado de redes, sistemas de atención telefónica, videojuegos o simulación de sistemas operativos (como la asignación de tiempo en un procesador estilo *Round Robin*).

### Cuándo no usarlo
* Cuando el número de iteraciones o los valores de entrada son extremadamente grandes (por ejemplo, $n = 10^9$) y una simulación paso a paso excedería el tiempo límite de ejecución (*Time Limit Exceeded*).
* Cuando existe una solución matemática cerrada o una fórmula analítica directa conocida para calcular el resultado final en tiempo constante $O(1)$ o logarítmico $O(\log n)$.

---

## Patrón 2: Información Monotónica

### Problema ejemplo
El problema de **Nearest Smaller Values** (Valores menores más cercanos) o **Daily Temperatures** (Temperaturas diarias): dado un arreglo de números que representan mediciones secuenciales, queremos encontrar para cada elemento cuál es el primer valor estrictamente menor o mayor que se encuentra justo a su izquierda (o derecha).

### Pregunta detonadora
*¿Qué elementos pasados del arreglo puedo eliminar por completo y para siempre de mi memoria auxiliar, sabiendo con certeza matemática que jamás volverán a ser una respuesta válida para los elementos futuros que voy a evaluar?*

### Estructuras que suelen aparecer
* Pila Monótona (*Monotonic Stack*), implementada comunmente con una lista nativa en Python (`list`).
* Cola Monótona (*Monotonic Deque*).

### Ejemplo visto en clase o encontrado en recursos
Imaginemos que estamos buscando el valor anterior más pequeño en el arreglo `[4, 5, 2, 10]`. Empezamos evaluando el `4` y lo guardamos en nuestra pila. Cuando pasamos al `5`, vemos el tope de la pila (que es `4`); como `4 < 5`, descubrimos que `4` es su respuesta y apilamos el `5` al final (la pila queda `[4, 5]`). Sin embargo, al pasar al `2`, nos damos cuenta de que el `5` y el `4` son más grandes. Los eliminamos de la pila con `.pop()` de forma definitiva porque el número `2` es más pequeño y está "tapando el paso". Cualquier número que venga después preferirá ver este nuevo `2` en lugar de un `4` o `5` que quedaron atrás.

### Cuándo usarlo
* En problemas que nos piden encontrar los elementos siguientes o anteriores con una condición estricta de orden (el "siguiente mayor", "anterior menor", "trampa de agua", etc.).
* Cuando necesitamos optimizar un problema que de forma ingenua y directa tomaría dos ciclos anidados lentos $O(n^2)$ y queremos reducirlo a una solución lineal $O(n)$ de una sola pasada por los datos.

### Cuándo no usarlo
* Cuando el problema nos exige responder consultas arbitrarias en cualquier posición de la lista sin un orden continuo de izquierda a derecha (en esos casos son mejores los *Segment Trees* o tablas dispersas).
* Cuando el orden relativo y la posición original de cada dato descartado no se pueden perder en ningún momento del procesamiento general.

---

## Patrón 3: Ventana Deslizante (Sliding Window)

### Problema ejemplo
Encontrar la longitud de la subcadena continua más larga en un texto que contenga como máximo $k$ caracteres distintos, o hallar la suma máxima posible entre todos los subarreglos continuos de tamaño fijo $m$.

### Pregunta detonadora
*Al avanzar nuestro rango de búsqueda un paso hacia adelante en el arreglo, ¿cómo podemos actualizar el resultado general en un instante $O(1)$ agregando el nuevo elemento de la derecha y eliminando el elemento viejo de la izquierda, en lugar de volver a sumar todo el bloque desde cero?*

### Estructuras que suelen aparecer
* Dos variables enteras de índice (`left` y `right`) funcionando como límites en un arreglo tradicional.
* Tablas de frecuencias, diccionarios (`dict`), o estructuras `collections.Counter` para llevar el control temporal de lo que hay dentro de nuestra ventana actual.

### Ejemplo visto en clase o encontrado en recursos
Si queremos hallar la suma máxima de 3 elementos continuos en `[2, 1, 5, 1, 3, 2]`, primero sumamos los primeros tres números: $2 + 1 + 5 = 8$. Para revisar la siguiente agrupación (`[1, 5, 1]`), en lugar de volver a sumar esos tres números por separado, tomamos nuestro $8$, le restamos el extremo izquierdo que dejamos atrás (el $2$) y le sumamos el nuevo elemento de la derecha (el $1$). Nuestra nueva suma se calcula como $8 - 2 + 1 = 7$. Repetimos este movimiento suave hasta llegar al final de toda la lista.

### Cuándo usarlo
* Cuando el problema nos habla estrictamente de **subarreglos contiguos**, secuencias ininterrumpidas o porciones seguidas de una cadena de texto.
* Cuando podemos mantener o recalcular un estado (como sumas totales, conteos de letras o promedios temporales) agregando un elemento nuevo y sacando uno viejo en muy pocas operaciones.

### Cuándo no usarlo
* Cuando los elementos que debemos seleccionar o agrupar **no necesitan estar juntos ni contiguos** en el arreglo original (problemas de subsecuencias generales o combinaciones libres).
* Cuando la lista contiene números positivos y negativos mezclados y las condiciones del problema no nos permiten saber de forma lógica cuándo encoger o estirar nuestra ventana.

---

## Patrón 4: Búsqueda por Niveles (Breadth-First Search / BFS)

### Problema ejemplo
Encontrar la cantidad mínima de pasos que necesita un caballero de ajedrez para llegar de una casilla de inicio a una casilla final dentro del tablero, o descubrir el camino más rápido para salir de un laberinto con obstáculos.

### Pregunta detonadora
*¿Cómo puedo explorar de forma sistemática y ordenada todas las posibilidades inmediatas que tengo a un paso de distancia antes de atreverme a investigar las que se encuentran a dos o más pasos de distancia?*