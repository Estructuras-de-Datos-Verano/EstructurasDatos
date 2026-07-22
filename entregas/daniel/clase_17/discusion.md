# Discusión técnica — Clase 17

## 1. Nodo y lista ligada
Un nodo es simplemente un contenedor individual, una cajita que guarda un dato y tiene una o más variables apuntando hacia donde se encuentra su vecino en la memoria. Por el contrario, una lista ligada es la estructura organizadora completa; es decir, el sistema que sabe dónde empieza la cadena, dónde termina, cuántos elementos hay en total y qué reglas se deben seguir para añadir o quitar esos nodos de forma ordenada.

## 2. Cola ligada
Para que una cola funcione de manera eficiente, necesitamos poder meter elementos por detrás y sacarlos por delante de forma inmediata. Si solo tuviéramos una referencia al frente, descubrir el final para añadir un nuevo elemento nos obligaría a recorrer toda la cadena nodo por nodo, lo que haría que encolar fuera sumamente lento. Al mantener ambas referencias directas, tanto la entrada como la salida se resuelven en un solo paso rápido.

## 3. Invariantes
Cuando nuestra cola está completamente vacía, se deben cumplir tres condiciones lógicas al mismo tiempo para asegurar que la estructura está sana:
* La referencia que apunta al frente de la cola debe estar vacía y valer `None`.
* La referencia que apunta al final de la cola también debe estar vacía y valer `None`.
* El contador que lleva el registro del tamaño de la cola debe marcar exactamente cero.

## 4. Lista simple y lista doble
La gran ventaja de añadir la referencia `anterior` es la libertad de movimiento; ahora podemos retroceder por la lista o eliminar elementos desde cualquier extremo sin tener que empezar a buscar siempre desde el principio. Sin embargo, esto tiene un costo: cada nodo consume un poco más de memoria para guardar este puntero extra, y además, nuestro código se vuelve más delicado porque cada vez que insertamos o quitamos un elemento debemos asegurarnos de actualizar los enlaces en ambas direcciones para no romper la consistencia de la cadena.

## 5. Deque
Una deque es una cola de doble extremo que exige poder agregar y quitar elementos tanto por el principio como por el final con la misma rapidez. Una lista doblemente ligada es perfecta para esto porque sus punteros de ida y vuelta nos permiten desenganchar o colgar nodos en cualquiera de los dos extremos de manera inmediata, manteniendo un rendimiento excelente sin importar qué tan larga sea la cadena de datos.

## 6. Complejidad
En Python, las listas estándar están construidas por debajo como arreglos contiguos de memoria. Cuando usamos una instrucción para retirar el primer elemento, el sistema se ve obligado a desplazar físicamente todos los elementos restantes una posición hacia la izquierda para ocupar el espacio vacío. Este reajuste de posiciones hace que la operación tarde más tiempo a medida que la lista crece, a diferencia de nuestra cola ligada donde solo movemos un puntero en un instante constante.

## 7. BFS
En el recorrido BFS, si esperamos a marcar un nodo como visitado hasta el momento en que lo sacamos de la cola, corremos el riesgo de que otros nodos que estamos procesando en el mismo nivel descubran a ese mismo vecino y lo vuelvan a meter a la fila. Esto genera duplicados innecesarios dentro de la cola, lo que provoca un desperdicio enorme de memoria y tiempo de procesamiento, especialmente en redes que están muy conectadas.

## 8. Predecesores
La única y gran responsabilidad de este mapa es registrar la procedencia de cada nodo durante la exploración. Al guardar la relación de quién descubrió a quién, el mapa funciona como un rastro de migas de pan que nos permite reconstruir el camino exacto de vuelta hacia el origen una vez que logramos alcanzar el destino.

## 9. Reutilización
Tanto BFS como Dijkstra exploran el grafo de maneras diferentes, pero al final del día, ambos algoritmos construyen exactamente la misma estructura de datos para recordar el recorrido: un mapa o diccionario donde cada nodo señala a su predecesor inmediato. Como la lógica para caminar hacia atrás usando ese mapa es idéntica en ambos casos, podemos escribir una sola función de reconstrucción de caminos y usarla para cualquiera de los dos algoritmos sin cambiarle una sola línea.

## 10. 0-1 BFS
Cuando encontramos un camino conectado por una arista que cuesta cero, significa que podemos llegar a ese vecino sin acumular costo adicional en nuestro viaje. Al colocar este nodo al principio de la deque, nos aseguramos de explorar todas las opciones gratuitas e inmediatas antes de ponernos a procesar los caminos que sí incrementan el costo de la ruta, garantizando que siempre encontremos la alternativa más barata primero.

## 11. Comparación
* **BFS tradicional:** Asume que todos los pasos tienen exactamente el mismo valor o costo, por lo que avanza estrictamente por niveles de cercanía física usando una cola simple.
* **0-1 BFS:** Maneja dos costos posibles (pasos gratis de valor cero o pasos de valor uno). Utiliza una deque para colar las rutas gratis al frente y las costosas atrás, logrando resolver el problema de forma óptima sin la pesadez de ordenar constantemente.
* **Dijkstra:** Es el más general y potente, diseñado para lidiar con cualquier costo positivo a través de una cola de prioridad que extrae en cada paso el nodo con el menor costo acumulado hasta ese momento.

## 12. Elección de estructura
La decisión depende de qué operación necesitemos priorizar en el corazón de nuestro algoritmo:
* Si la prioridad es estrictamente el orden de llegada en un flujo continuo, la operación dominante es el comportamiento de primero en entrar, primero en salir, lo que nos lleva directo a una **cola**.
* Si necesitamos reaccionar de inmediato ante elementos urgentes colocándolos al frente y relegando los demás al fondo, la flexibilidad de una **deque** es la mejor opción.
* Si el orden depende de un valor dinámico que cambia constantemente y siempre necesitamos extraer el elemento con el valor más pequeño del conjunto, un **heap** es la estructura que domina la solución.

## 13. Producción
En un entorno de desarrollo real, preferimos usar `collections.deque` de la biblioteca estándar de Python porque está programada directamente en C y optimizada a bajo nivel. Es una estructura sumamente veloz, robusta, libre de errores de punteros manuales y cuenta con una gestión de memoria excelente que ha sido probada y pulida durante años por la comunidad.

## 14. Riesgos
El peligro más grande en las listas doblemente ligadas ocurre durante las inserciones o eliminaciones cuando la lista tiene un solo elemento o se queda vacía. Es muy fácil olvidar actualizar el enlace `anterior` del nodo que queda como nuevo extremo, o dejar referencias huérfanas apuntando a nodos viejos. Esto provoca fugas de memoria, ciclos infinitos donde el código se queda atrapado saltando de un nodo a otro, o errores inesperados al intentar acceder a valores nulos.

## 15. Cierre
Para un escenario con pesos de cero, uno y dos, la mejor elección general sería utilizar el algoritmo de **Dijkstra tradicional con una cola de prioridad**. 

La técnica de 0-1 BFS ya no se puede aplicar directamente porque su diseño depende exclusivamente de tener dos estados (el frente de la deque para costo cero y el final para costo uno). En el momento en que introducimos un tercer costo como el valor dos, perdemos la capacidad de mantener los nodos ordenados por costo usando solo dos extremos; necesitaríamos un "punto intermedio" de inserción en la deque, lo cual rompería la eficiencia de tiempo constante y nos obligaría a clasificar los elementos, que es precisamente la tarea para la que se diseñó un heap.