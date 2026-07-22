1. De Representar a Recorrer
A ver, una cosa es guardar el grafo (con tus listas o matrices de adyacencia) y otra muy diferente es hacer algo útil con él. Guardarlo es dejarlo ahí congelado, como una foto estática de quién se lleva con quién. Pero cuando empiezas a recorrerlo, es cuando el código cobra vida de verdad. Pasas de tener datos guardados a moverte por los nodos usando lógica de estados y tiempos de visita. Si no lo recorres, tu código jamás va a saber si puedes llegar de un punto A a un punto B, si hay un camino cerrado (ciclo) o cuál es la ruta más corta para resolver el problema.

2. Estrategias Manuales

Antes de meterle nombres mamalones a los algoritmos, si te dan un papel con un grafo y te piden que busques un nodo a mano, por puro instinto vas a hacer una de estas dos cosas. La primera es irte por capas: revisas primero los que tienes a un paso de distancia, luego los que están a dos pasos, luego a tres... como una onda en el agua que se expande. La segunda es irte a lo loco por una rama: eliges un camino y le das derecho hasta el fondo. Si chocas con pared o con un nodo donde ya estuviste, te echas para atrás con un backtracking y buscas otra ramita. Al final, la única diferencia real entre los algoritmos no es cómo guardas los nodos, sino a cuál le das prioridad cuando tienes varios pendientes en la lista.

3. BFS (Breadth-First Search)

El BFS es la formalización de irte por capas o niveles. Su motor principal es una cola, que funciona bajo la regla FIFO (First-In, First-Out), lo que significa que el primero que llega es el primero que atiendes. El flujo es sencillo: sales del origen, sacas a todos sus vecinos directos que forman la capa uno, los mandas al final de la cola y los vas atendiendo exactamente en ese orden de llegada para descubrir la capa dos. Como el código siempre saca de la cola al nodo que lleva más tiempo esperando, te aseguras de revisar todo lo cercano antes de irte más lejos. Por eso, si tu grafo no tiene pesos raros en las aristas, el BFS te va a dar la ruta óptima y más corta sí o sí.

4. DFS (Depth-First Search)

El DFS es el que se clava con una sola rama hasta el fondo sin mirar a los lados. Este usa una pila bajo la regla LIFO (Last-In, First-Out), donde el último en llegar es el primero que sale, que es exactamente lo que pasa cuando usas funciones recursivas y las llamadas se van apilando en la memoria del sistema. El algoritmo arranca en el inicio, se clava con el primer vecino, luego con el vecino de ese vecino, y no se detiene hasta que topa con pared o con un fin de camino. En ese momento se regresa un paso y busca otra alternativa profunda. El DFS es súper agresivo; no te sirve para buscar rutas cortas, pero es una joya para ver si todo el grafo está conectado, encontrar ciclos o resolver laberintos donde tienes que probar combinaciones hasta que una jale.

5. El Tiro: BFS vs DFS

Si ponemos a competir a ambos algoritmos, saltan a la vista sus diferencias más cabronas. El BFS procesa de forma horizontal usando una cola, lo que le da la ventaja de garantizar la ruta más corta en grafos sin ponderar. El problema es que si el nivel actual es gigante, puede consumir un buen de memoria guardando tantos nodos pendientes. Por otro lado, el DFS procesa de forma vertical metiendo recursión o una pila. No te asegura para nada la distancia mínima, te da la primera ruta que encuentre, pero su consumo de memoria suele ser más noble porque solo depende de qué tan profunda sea la rama que está explorando. Ambos tienen la misma complejidad temporal de O(V + E), pero sus intenciones son completamente opuestas.

6. Visualización Dinámica

Hacer que el código te escupa una lista de letras da hueva y la verdad no entiendes nada de lo que está pasando adentro. Al usar matplotlib y networkx para guardar los archivos .png paso a paso, como paso_0.png o paso_1.png, puedes ver en tiempo real cómo piensa tu código. Con el BFS, ves en las imágenes cómo los nodos se van pintando en círculos concéntricos perfectos que se expanden desde el centro. Con el DFS, ves cómo se dibuja una línea rápida que cruza el grafo de un extremo a otro antes de empezar a rellenar los huecos que dejó atrás. Además, si la riegas y dejas un bucle infinito porque olvidaste marcar un nodo como visitado, en las fotos vas a ver de volada el par de nodos donde se quedó trabado el código dando vueltas.

7. Modelado con Problemas de CSES

Cuando juegas en CSES, te das cuenta de que los problemas de la vida real son puros grafos camuflajeados. En Counting Rooms te dan un mapa con paredes y pasillos libres. Cada punto limpio es un nodo y sus vecinos son aristas; contar cuartos es básicamente correr un DFS o BFS para pintar un cuarto entero, ver cuántos nodos limpiaste, y pasar al siguiente espacio en gris hasta mapear todo. En Labyrinth te piden salir de un laberinto pero con la ruta más corta. Aquí el DFS no sirve porque se perdería en las esquinas; tienes que usar un BFS obligatorio y meterle un truco al código para que cada nodo recuerde a su "papá" (el nodo que lo descubrió) y así reconstruir la ruta al revés desde la meta. En Message Route es una red de computadoras donde quieres mandar un mensaje con los menores saltos posibles; metes un BFS y en el primer milisegundo que toque el nodo final, ya tienes la ruta más rápida asegurada.

8. Pruebas para ver si el código aguanta

Hacer tests con pytest no es solo para ver si el camino feliz funciona cuando todo está bonito. Hay que meterle escenarios donde el código se pueda romper para ver si es robusto. Por ejemplo, los grafos dirigidos de una vía validan que si A apunta a B, el algoritmo no sea capaz de regresarse a la mala de B a A. Los tests con nodos fantasma u orígenes inexistentes cuidan que si buscas empezar en un nodo Z que ni está en el mapa, el código regrese una lista vacía bien fresco en lugar de crashear horrible con un KeyError. Finalmente, probar islas o grafos desconectados asegura que los conjuntos de visitados de verdad sirvan como cortafuegos para que el código no se quede dando vueltas como loco para siempre.

9. El Patrón Descubierto

El gran 'insight' de esta clase es que todo en esta vida se puede modelar como un grafo si lo piensas bien: las pantallas de una app, los estados de un juego, los amigos de Facebook o las calles de tu ciudad. Si el problema te pide optimizar pasos iguales, buscar lo más cercano o asegurar el menor gasto de movimientos, la respuesta automática es usar una Cola con BFS. Si el problema se trata de explorar todas las opciones posibles, validar combinaciones, hacer backtracking o ver si algo está conectado de punta a punta de la red, la respuesta fija es una Pila o Recursión con DFS.

10. Pregunta Abierta

Ya vimos que el BFS es el rey de la ruta corta porque se mueve de forma ordenada por niveles. Pero ponte a pensar en esto:

Si cambiamos las reglas del juego y ahora cada calle tiene tráfico diferente, semáforos o cuesta dinero pasar por ahí (es decir, metemos aristas con pesos o costos variables), ¿por qué el BFS y el DFS valen queso y ya no sirven para encontrar el camino óptimo? ¿Qué tendríamos que cambiarle a nuestra estructura de datos de pendientes para poder resolver un mapa de la vida real?