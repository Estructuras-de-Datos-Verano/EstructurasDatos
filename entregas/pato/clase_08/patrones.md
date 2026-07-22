# Catalogo de patrones - Clase 08

Nombre: Patricio Navarro

## Patron 1: Simulacion

- Problema ejemplo: Crear un sistema de tickets para atención al cliente o programar el botón de "Deshacer" (Control+Z) de un software.
- Pregunta detonadora: "¿Necesito imitar un proceso paso a paso manteniendo estrictamente el orden en el que ocurrieron o llegaron las cosas?"
- Estructuras que suelen aparecer: Pilas (Stacks) y Colas (Queues). También `collections.deque` en Python.
- Ejemplo en clase o recurso consultado: La analogía de los platos sucios apilados (Pila/LIFO) y la fila para subir al autobús (Cola/FIFO) explicada en el video de Alpaca Tech (Recurso 6).
- Cuando usarlo: Cuando las reglas del problema dictan un orden de procesamiento temporal irrompible (el primero en llegar es el primero en ser atendido, o el último en entrar es el primero en salir).
- Cuando no usarlo: Cuando necesites buscar información específica rápidamente a la mitad de los datos, ya que en estas estructuras buscar requiere vaciar los elementos uno por uno.

## Patron 2: Informacion monotonica

- Problema ejemplo: Encontrar eficientemente las medianas móviles en un flujo constante de datos, o mantener siempre rastreado el valor mínimo/máximo.
- Pregunta detonadora: "¿Necesito tener acceso inmediato al elemento más grande o más pequeño en todo momento mientras los datos cambian constantemente?"
- Estructuras que suelen aparecer: Colas de prioridad (Priority Queues) y Heaps (Montículos).
- Ejemplo en clase o recurso consultado: El uso de la librería `heapq` para resolver el problema de las medianas o "ventanas" (Recurso 3, Documentación de Python).
- Cuando usarlo: En problemas donde el enfoque principal es mantener un conjunto de datos ordenado de forma dinámica (siempre decreciente o siempre creciente) sin el costo de reordenar todo el arreglo en cada inserción.
- Cuando no usarlo: Si solo necesitas el orden de llegada de los elementos, independientemente de su valor numérico o peso.

## Patron 3: Búsqueda Rápida / Mapeo

- Problema ejemplo: Contar la frecuencia de palabras en un libro o asociar IDs de usuarios con sus perfiles de forma instantánea.
- Pregunta detonadora: "¿Necesito encontrar, verificar o contar datos específicos en tiempo constante O(1) sin tener que recorrer toda mi colección?"
- Estructuras que suelen aparecer: Diccionarios (Hashmaps / Tablas Hash) y Conjuntos (Sets).
- Ejemplo en clase o recurso consultado: La analogía de los buzones numerados de un edificio de departamentos para explicar los Hashmaps, del video de Sajjad Kadeer (Recurso 2).
- Cuando usarlo: Cuando la optimización del tiempo de búsqueda es tu máxima prioridad y tienes información que funciona como "llaves" (identificadores únicos).
- Cuando no usarlo: Cuando el orden de los datos es importante para el problema, ya que los diccionarios tradicionales (o los Sets) no garantizan un orden secuencial lógico, y cuando tienes recursos de memoria (RAM) extremadamente limitados.

## Patron 4: Secuencias Dinámicas (Nodos)

- Problema ejemplo: Programar el historial de navegación "Adelante/Atrás" de un navegador web, o una lista de reproducción donde mueves canciones de lugar constantemente.
- Pregunta detonadora: "¿Voy a estar insertando y eliminando datos a la mitad de mi secuencia todo el tiempo y quiero evitar que mi programa se congele recorriendo posiciones?"
- Estructuras que suelen aparecer: Listas doblemente enlazadas (Doubly Linked Lists).
- Ejemplo en clase o recurso consultado: La implementación en código de una lista doblemente enlazada y el ejemplo del historial del navegador del video de DeepCodeAI (Recurso 1).
- Cuando usarlo: Cuando el tamaño de tus datos cambia de manera drástica e impredecible, y las inserciones/eliminaciones ocurren en posiciones arbitrarias.
- Cuando no usarlo: Cuando vas a realizar muchas búsquedas por índice (ej. "dame el elemento en la posición 5000"), ya que, como vimos en el Recurso 7 (Chio Code), los nodos no están juntos en la RAM y tardan O(n) en recorrerse.

## Comparacion breve

Escoge dos patrones y explica en que se parecen y en que se diferencian.

- `Simulación (Pilas/Colas) vs. Búsqueda Rápida (Diccionarios/Sets)`
  Se parecen en que ambos sirven para retener datos temporalmente en memoria para su posterior uso. 
  Se diferencian radicalmente en su filosofía: la Simulación es ciega al valor de los datos y le importa al 100% el orden cronológico en el que llegaron. La Búsqueda Rápida es ciega al orden cronológico y le importa al 100% el valor/identificador para poder encontrar la información instantáneamente.

## Pregunta abierta

Que patron te parece mas dificil de reconocer antes de escribir codigo?

- El patrón de `Información Monotónica` suele ser el más contraintuitivo. Mientras que un diccionario es fácil de imaginar como una agenda telefónica, y una pila como una torre de platos, visualizar un Heap matemáticamente y darse cuenta de que "un árbol binario parcial es la solución óptima para rastrear la mediana en una ventana móvil" requiere mucha más abstracción algorítmica y práctica clínica con problemas de optimización.
