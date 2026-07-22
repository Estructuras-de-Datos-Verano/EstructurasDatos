# Arturo Prudencio Bonilla 

## Pregunta inicial
**¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?**
Cuando todos los pendientes tienen la misma prioridad, necesitamos una cola para aplicar un procesamiento secuencial basado en FIFO. Cuando existen dos niveles de prioridad, la política cambia y necesitamos una deque (double-ended queue) que nos permita elegir si el candidato se procesa pronto o si se relega detrás de los candidatos del costo actual 


## 1. Presentación de la clase
**¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades?**
Cambia la regla de procesamiento: en una sola prioridad solo nos importa "qué llegó primero", pero con dos prioridades (por ejemplo, acciones con costo cero frente a costo uno) nos importa "qué candidato conviene procesar antes", permitiendo que los elementos de menor costo adelanten posiciones frente a los que cuestan más


## 2. Problema inicial con pop(0)
**¿Qué trabajo repetido introduce pop(0) y por qué una referencia al frente lo evita?**
`pop(0)` introduce el trabajo repetido de tener que desplazar todos los elementos posteriores del arreglo una posición hacia atrás, lo que hace que retirar el primero cueste $\mathcal{O}(n)$ Una referencia al frente en una cola ligada evita este costo porque desencolar simplemente significa mover el puntero `frente` al siguiente nodo, manteniendo la operación en $\mathcal{O}(1)$


## 3. Nodo y referencias
**¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos?**
El *valor* es la carga útil guardada. El *nodo* es una pieza individual de memoria que contiene ese valor junto con una o más referencias hacia otros nodos. Finalmente, la *estructura contenedora* es la entidad que organiza las referencias, agrega reglas, controla qué extremo se modifica y mantiene los invariantes de las operaciones permitidas


## 4. Lista ligada simple
**¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?**
Si la lista simple solo guardara el `inicio`, la operación de encolar (agregar al final) sería muy costosa, ya que se tendría que recorrer linealmente toda la cadena desde el frente para localizar al último nodo y poder enlazar el nuevo elemento detrás de él


## 5. Cola ligada
**¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean O(1)?**
Necesitamos `frente` para que desencolar (retirar el inicio y devolver su valor) ocurra en tiempo constante, y necesitamos `final` para poder encolar (crear un nodo y enlazarlo después del último) directamente sin necesidad de recorrer recursivamente toda la cadena


## 6. Invariantes de cola
**¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento?**
Después de desencolar el único elemento, debe cumplirse simultáneamente que `frente` sea `None`, `final` sea `None`, y el `_tamano` de la estructura regrese estrictamente a $0$


## 7. Operaciones manuales
**En la secuencia manual, ¿qué referencias cambian al desencolar A de la cadena A → B → C?**
Al retirar $A$, la variable `frente` de la cola se actualiza para apuntar a $B$ Además, la variable `_tamano` disminuye su contador en $1$


## 8. Complejidad
**¿Por qué buscar un valor sigue siendo O(n) aunque encolar y desencolar sean O(1)?**
Porque buscar un valor arbitrario puede requerir inspeccionar los nodos sistemáticamente desde el frente, recorriendo toda la cadena de referencias `siguiente` hasta encontrar una coincidencia, ya que las variables `_frente` y `_final` solo ofrecen acceso directo a los extremos


## 9. BFS y cola
**¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS?**
El orden FIFO preserva la prioridad de descubrimiento, garantizando que un nodo que fue descubierto antes (en una capa menos profunda) se desencole y procese antes que los nodos descubiertos después (en capas más profundas) Esta sincronía hace que las distancias aparezcan de forma no decreciente de forma natural


## 10. Visitados al encolar
**¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse?**
Si un vértice $E$ se marca solo cuando sale de la cola, y resulta que es alcanzable desde dos nodos $B$ y $C$ que ya están encolados simultáneamente, tanto $B$ como $C$ volverán a encolar una copia de $E$ porque lo considerarán "no visitado" Esto provoca duplicaciones que pueden crecer rápidamente en grafos densos


## 11. Predecesores
**¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido?**
Basta con guardar un mapa compacto donde cada clave es un nodo y su valor asociado es su primer predecesor (`predecesores[vecino] = actual`), formando un vínculo hacia el nodo desde el cual fue descubierto originalmente


## 12. Reconstrucción del camino
**¿Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta?**
Un destino inalcanzable se evidencia si al escalar por el mapa de predecesores la cadena termina limpiamente en `None` antes de llegar al origen En contraste, una tabla de predecesores corrupta se identifica porque, al retroceder, encontramos un nodo que ya habíamos visitado previamente, evidenciando un ciclo lógico y provocando que el bucle `while` teóricamente no termine


## 13. Práctica guiada de BFS
**¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos?**
El orden en que evaluamos la lista de adyacencia de un nodo puede hacer que descubramos a un vecino destino desde dos padres diferentes Aunque el árbol BFS resultante mostrará topologías diferentes y por lo tanto una cadena de nodos (camino) distinta, la longitud del camino permanecerá igual porque ambas ramas descubren al destino en el mismo número de saltos dentro de la misma capa de prioridad


## 14. Lista doblemente ligada
**¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece?**
Obtenemos la capacidad simétrica de retirar o agregar nodos desde ambos extremos de forma directa en $\mathcal{O}(1)$ A cambio, aparece la obligación estricta de que ambas direcciones concuerden: si un enlace va de izquierda a derecha (el `siguiente` de $A$ es $B$), su inverso debe ir en dirección contraria (el `anterior` de $B$ debe ser $A$)


## 15. Invariantes de lista doble
**¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentes?**
Se comprobaría recorriendo la cadena desde el inicio hasta el final e inspeccionando en cada paso que la propiedad `actual.anterior` apunte exactamente al objeto del nodo visitado justo antes Adicionalmente, se puede recorrer de manera inversa desde el final hacia el inicio y verificar que ambas cuentas de nodos coincidan con la variable `_tamano`


## 16. Deque ligada
**¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO?**
Porque la deque es simplemente una estructura versátil que expone cuatro operaciones atómicas de manipulación en ambos extremos Carece de políticas internas, por lo que recae en el algoritmo o desarrollador decidir y acoplar el orden de uso (qué combinación de inserción y extracción utilizar)


## 17. Operaciones manuales de deque
**Después de quitar el inicio A de A ⇄ B ⇄ C ⇄ D, ¿qué cuatro hechos deben comprobarse?**
Se debe comprobar que el nodo retirado $A$ tenga sus variables `anterior` y `siguiente` en `None`, y que el nuevo inicio ($B$) tenga ahora a `None` como `anterior`


## 18. Qué problema resuelve 0-1 BFS
**¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0?**
BFS común supone que todas las aristas cuestan lo mismo (costo unitario), por lo que siempre favorece el camino con menor cantidad de saltos o vértices Al tener aristas con costo cero, un camino de $3$ saltos (todos con peso $0$) tiene en realidad un costo real menor que un camino de un solo salto con peso $1$. BFS fallaría al ignorar este costo ponderado global


## 19. Deque como estructura de prioridad
**¿Qué información del peso decide el extremo de inserción y por qué?**
Si el peso del candidato es cero, significa que la ruta mejora conservando su costo actual y debe procesarse pronto, por lo que se agrega al frente (`inicio`) Si el peso es uno, significa que la ruta queda detrás de los candidatos del costo actual, y debe procesarse después, por lo que se anexa al `final`


## 20. Ejecución manual de 0-1 BFS
**Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X?**
La variable de su distancia actual mejora estrictamente (baja su costo), por lo que cambia su valor en la tabla, actualiza su predecesor y se agrega o empuja forzosamente hacia el `inicio` (frente) de la deque


## 21. Implementación
**¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo?**
Garantiza que primero consolidamos una base lógica libre de errores Al asegurar las propiedades del TDA de forma atómica antes de fusionarlo con el algoritmo principal, se aíslan y mitigan los fallos, logrando que el rastreo y solución de errores dentro de BFS o 0-1 BFS no apunten falsamente a los enlaces de la cola


## 22. Casos límite
**¿Por qué True debe producir TypeError aunque isinstance(True, int) sea verdadero en Python?**
Porque aunque la herencia del lenguaje lo avale, un booleano no representa semánticamente el dominio numérico matemático que el grafo ponderado requiere (un peso o distancia), por lo que debe rechazarse explícitamente para cumplir el contrato lógico de los pesos


## 23. Pruebas
**¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura?**
Detecta defectos relacionados con referencias residuales, comprobando si el estado contradictorio de la estructura persiste al manipularla repetidamente e introduciendo nuevamente cadenas muertas y referencias viejas al dominio en vez de reiniciarse como corresponde


## 24. Comparación BFS, 0-1 BFS y Dijkstra
**¿Qué operación dominante conduce respectivamente a cola, deque o heap?**
-   **Cola:** Procesar secuencialmente por orden de llegada y estratificación por capas (costos unitarios)
-   **Deque:** Adelantar los pesos gratuitos y posponer jerárquicamente las aristas de peso $1$ hacia atrás
-   **Heap:** Extraer siempre, en cada iteración, la menor distancia no definitiva o candidata disponible sin importar el orden cronológico o prioridades binarias (pesos no negativos generales)


## 25. Cierre hacia Union-Find y Kruskal
**¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos?**
Aparece la pregunta sobre qué estructura auxiliar se debe elegir si la prioridad ya no trata sobre buscar caminos desde un origen (como BFS o Dijkstra), sino de organizar lógicamente las pertenencias para unir componentes evitando reconexiones redundantes