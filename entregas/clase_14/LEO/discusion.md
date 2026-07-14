# Discusión clase 14 - Leonardo Daniel Arenas Serafín (REVISO A TIAGO)

## 1. Operación dominante.
La operación dominante en esta estructura es la de comparación para encontrar ek menor, ya que esta estructura es un orden parcial que busca encontrar ek valor menor para darle prioridad.

## 2. FIFO vs prioridad.
FIFO es un tipo de comportamiento secuencial que le da prioridad de salida al primer elemento que fue ingresado a la estructura, mientras que en el MinHeap, nuestra prioridad depende de un criterio que no solamente toma en cuenta el orden de llegada de los elementos, sino el propio valor de cada elemento, ordenandolo de forma que le da prioridad al menos de éstos.

## 3. BST/AVL vs heap.
Estas 3 estructuras son un árbol binario, por lo que en el fondo son la misma estructura matemática, sin embargo heap no es para nada lo mismo que un BST/AVL. Un heap sigue un comportamiento de orden parcial, donde todo el árbol se rellena completamente por niveles y la única regla a seguir es que los hijos siempre sean mayores o iguales que el padre, a diferencia de loe BST/AVL, que siguen un comportamiento invariante en el cual los valores menores estrictos siempre van a la izquierda del padre y los mayores estrictos a la derecha, evitando así repetidos.

## 4. Propiedad min-heap.
La propiedad del min-heap es que siempre los hijos sean mayores iguales a los padres, de esta forma se puede asegurar que la raíz del árbol es el valor mínimo de la estructura, dándole así prioridad de salida.

## 5. Representación por arreglo.
Un heap en arreglo es exactamente lo mismo que en un árbol, la diferencia está en que el árbol simplemente en la representación visual del heap para hacerlo más didáctico, mientras que el arreglo es su estructura base. Como un heap se rellena siempre de izquierda a derecha, nivel por nivel, es posible llevar una relación entre el valor y su índice que nos dice la posición dentro del árbol. Se siguen 3 fórmlas para conocer los índices: 

        padre(i) = (i - 1) // 2
        izquierdo(i) = 2 * i + 1
        derecho(i) = 2 * i + 2

## 6. Sift-up.
Este algoritmo se sigue a la hora de insertar un nuevo elemento en la estructura. Como se rellena el árbol de izquierda a derecha por niveles, el último elemento ingresado es el último de la estructura, por lo que es necesario comparar el valor de dicho elemento con sus padres para no violar la regla de comparación entre padre e hijo. Así, un elemento insertado va subiendo hasta encontrar su posición final. El algoritmo se para al encontrar un padre que sea menor.

## 7. Sift-down.
Este algoritmo se sigue a la hora de retirar el mínimo de la estructura. Como en el heap no nos importa cómo esté ordenado el medio de la estructura sino que nos importa poder tener acceso claro al elemento de máxima prioridad, después de este primer elemento no sabemos si la estructura está correctamente ordenada para indicarnos el siguiente mínimo, por lo que debemos de retirar el último elemento de la estructura y ponerlo en la raíz, pero si es mayor que sus hijos esto viola la regla, por lo que debemos ir comparándolo con sus hijos para ir bajándolo hasta que llegue a su posición real y así meter el siguiente mínimo hasta arriba. Aquí es necesario comparar el padre con el menor de los hijos para evitar quense siga violando la regla. El algoritmo se para al encontrar dos hijos que sean mayores o iguales.

## 8. Complejidad.
La complejidad del retiro del mínimo es O(1), pues es el primero, y para insertar o extraer tenemos una complejidad de O(log n), pues por cada nivel debemos hacer una comparación, y como el crecimiento de los niveles es exponencial, la complejidad se hace logarítmica

## 9. Last Stone Weight.
En este problema buscamos el máximo, no el mínimo, esto se soluciona al ingresar los valores con su signo inverso.

## 10. Pruebas propias.
Yo implementé las siguientes pruebas que verifican el comportamiento de insersión, extracción y de Last Stone Weight en extremo: test_varios_cambios_por_insercion_LEO(), test_extraccion_varios_niveles_LEO(), test_ultima_piedra_caso_extremo_LEO()

## 11. Revisión técnica.


## 12. Relación con Dijkstra.
En este problema lo que nos interesa es saber cuál es el camino más corto u óptimo para llegar de un punto a otro, por lo que después de analizar cada camino posible, vamos metiendo su costo en un heap para poder saber cuál es el mínimo de los costos y tomar una decisión.

## 13. Pregunta abierta: ¿qué operación haría preferible otra estructura?
Si queremos solamente buscar y encontrar si un valor se encuentra dentro de una estructura, los heaps no son útiles pues no tenemos un orden para todos los elementos, por lo que sería muy costoso encontrar un elemento en un caso extremo. En este caso sería mejor un BST/AVL por ejemplo, pues vamos comparando y descartando con una complejidad de O(log n), mientras que en el heap sería O(n).