# Reflexion tecnica - Clase 08

Nombre: José Daniel Molina Carrillo

## Ideas recurrentes

Que ideas aparecieron en varios recursos?

- en los basicos cosas de pilas y colas y si no cosas bastante sencillas de entender 
  en cambio en los videos avanzados no entendi mucho ni si quiera con la IA

## Comparacion critica

Compara al menos dos recursos.

| Aspecto | Recurso A | Recurso B |
| --- | --- | --- |
| Claridad | buenisima | meh  |
| Ejemplos | como uso una cola para sacar los turnos de una fila de espera | ni se que hizo :(  |
| Profundidad | superficial | profundisima |
| Visualizaciones |buenas y facil de hacer  | muy pocas |
| Codigo |claro  |avanzado  |

## Recurso mas util

Cual fue el recurso mas util para ti y por que?

- en lo personal el recurso A, porque son cosas con las que ya estoy familiarizado y son mas faciles de entender

## Recurso menos recomendable

Cual fue el recurso menos recomendable o menos claro y por que?

- el recurso B creo no fue el adecuado por que como ya mencioné es muy avanzado para lo que estamos viendo aperte el ingles del profe era chafa

## Relacion con el curso

Como se conecta esta investigacion con Josephus, Nearest Smaller Values, pilas, colas, diccionarios o pruebas?

-Josephus Problem: Se resuelve eficientemente rotando elementos en una cola de doble extremo (collections.deque), permitiendo eliminar personas en tiempo constante $O(1)$. 

Nearest Smaller Values: Se soluciona mediante una pila monótona (ordenada). Reduce la búsqueda del menor elemento cercano de un costo ingenuo de $O(n^2)$ a uno óptimo de $O(n)$.

Pilas y Colas: Son las estructuras base. collections.deque implementa ambas: funciona como Pila (LIFO) usando .append() / .pop(), y como Cola (FIFO) usando .append() / .popleft().

Diccionarios: A diferencia de los montículos (que priorizan mínimos/máximos en $O(\log n)$), los diccionarios buscan claves exactas en $O(1)$, pero no mantienen los datos ordenados.

Pruebas: Los jueces en línea (CSES/USACO) evalúan con miles de datos. Usar la estructura correcta (heapq, deque, bisect) evita que el código falle por límite de tiempo (TLE).

## Preguntas nuevas

Formula al menos tres preguntas tecnicas que quieras resolver en las siguientes clases.

1.¿Cuándo es necesario implementar un Árbol Binario de Búsqueda (BST) manual en Python si bisect.insort ya busca en $O(\log n)$ pero inserta en $O(n)$?

2.¿Cuál es la forma más eficiente y limpia de simular un Max-Heap usando heapq cuando los elementos son tuplas o estructuras complejas?

3.¿Cómo se puede adaptar una deque monótona para resolver el problema de la ventana deslizante (Sliding Window) si el tamaño de la ventana cambia dinámicamente?

## Que explicarias diferente

Si tuvieras que explicar uno de los temas investigados a otro estudiante, que cambiarias respecto a los recursos que consultaste?

- explicaria pilas y colas que es lo que mas tengo interiorizado