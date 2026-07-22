# Catalogo de patrones - Clase 08

Nombre:

## Patron 1: Simulacion

- Problema ejemplo: El problema de Josephus (eliminar personas en un círculo saltando cada $k$ posiciones hasta que quede solo una).
- Pregunta detonadora: ¿Cómo cambia el estado de un sistema paso a paso si sigo de manera estricta y literal las reglas o instrucciones de un proceso?
- Estructuras que suelen aparecer: Colas dobles o de dos extremos (`collections.deque`), listas circulares.
- Ejemplo en clase: La resolución de Josephus rotando elementos al final de la cola y eliminando al que queda al frente en cada turno.
- Cuando usarlo: Cuando el problema describe un juego, un sistema de turnos o una secuencia temporal de eventos donde el orden exacto de los movimientos importa y se debe replicar fielmente.
- Cuando no usarlo: Cuando el número de iteraciones o pasos es masivo (por ejemplo, $10^9$ o más). En esos casos, intentar simular paso a paso causará que el programa tarde demasiado, por lo que es mejor buscar un patrón matemático o una fórmula directa.


## Patron 2: Informacion monotonica

- Problema ejemplo: Nearest Smaller Values.
- Pregunta detonadora: ¿Cómo puedo mantener un historial de datos ordenados de forma estrictamente creciente/decreciente para descartar de inmediato los elementos que ya nunca me van a servir?
- Estructuras que suelen aparecer: Pilas monotónicas (`list` usando `.append()` y `.pop()`) o colas monotónicas.
- Ejemplo en clase: Mantener una pila donde sacamos los números más grandes que el valor actual antes de insertarlo, garantizando que los elementos dentro de la pila siempre estén ordenados de menor a mayor.
- Cuando usarlo: Cuando necesitas buscar el primer elemento anterior o posterior que cumple con una condición de desigualdad (un número mayor o menor), y quieres evitar revisar todo el arreglo hacia atrás con dos ciclos anidados.
- Cuando no usarlo: Cuando los datos no tienen una relación de orden secuencial obvia o si el problema requiere buscar valores exactos (en cuyo caso es mucho mejor usar un Diccionario o Tabla Hash).

## Patron 3: Priority Queues(Heaps)
- Problema ejemplo: Diseñar un sistema de atención médica en urgencias o encontrar los 10 puntajes más altos en un flujo constante de millones de datos.
- Pregunta detonadora: ¿Cuál es el elemento con la mayor urgencia o el valor más pequeño en este preciso momento, considerando que sigo metiendo y sacando datos continuamente?
- Estructuras que suelen aparecer: Formas doblemente indexadas (*Heaps*) mediante la librería nativa `heapq`.
- **Ejemplo en clase o recurso consultado:** La documentación oficial de `heapq` y sus implementaciones para "Priority Queues".
- Cuando usarlo: Cuando la operación principal de tu programa consiste en consultar y extraer repetidamente el elemento mínimo (o máximo) de un conjunto dinámico que cambia de tamaño constantemente.
- Cuando no usarlo: Si necesitas buscar elementos en medio de la estructura por su valor exacto, o si tus datos son fijos (estáticos) y te basta con ordenarlos una sola vez al principio usando `.sort()`.

## Patron 4: Grafos

- Problema ejemplo: Encontrar la ruta más corta entre dos ciudades o modelar una red de computadoras interconectadas.
- Pregunta detonadora: ¿Cómo se conectan estas entidades independientes entre sí y qué caminos o puentes existen para viajar de una a otra?
- Estructuras que suelen aparecer: Diccionarios (`dict`) implementados como Listas de Adyacencia, donde la llave es el nodo y el valor es una lista con sus vecinos. Listas dobles también para Matrices de Adyacencia como en clase 09.
- Ejemplo en clase o recurso consultado: El ensayo clásico de Guido van Rossum (*Python Patterns - Implementing Graphs*) y, por suouesto, la clase 09 gracias a la prórroga.
- Cuando usarlo: Cuando el problema involucra redes, interconexiones, dependencias de tareas (como prerrequisitos de materias) o mapas de laberintos.
- Cuando no usarlo: Si las relaciones son puramente jerárquicas simples de uno a muchos (donde un árbol tradicional es suficiente), o si las conexiones son estrictamente secuenciales (donde basta una lista o arreglo normal).

## Patrones adicionales opcionales

Ya me da flojera llenar tanto, pero si veo que otro patrón extra que incluso no hemos trabajado es la de ponderar soluciones cuantitativamente. Podríamos hacer pytests, guardar los tiempos y eso guardarlo en una Priority Queue (conforme los va ejecutando pytest, nos apoyamos con Time) para ver que implementaciones dan tiempos mínimos/máximos sin solo quedarnos en lo teórico,

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

-Patrones elegidos: *Simulación* e *Información Monotónica*.

- En qué se parecen: Ambos procesan los elementos de un arreglo o flujo de datos de manera secuencial (por lo general, de izquierda a derecha), y ambos necesitan apoyarse en estructuras de datos lineales (como pilas o colas) para ir manteniendo un registro temporal del estado del problema.
- En qué se diferencian: La Simulación es conservadora y literal ya que mantiene el orden operativo de los datos y procesa cada paso tal cual lo dicem las reglas del juego sin destruir la estructura original de pasos. Por el contrario, la Información Monotónica es destructiva y selectiva puesto a que elimina activamente datos antiguos de la pila (mediante pops) si estos rompen la propiedad de orden (creciente o decreciente), bajo la premisa de que esos datos eliminados ya no aportarán ninguna solución en el futuro.

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- Ninguno hasta el momento.
