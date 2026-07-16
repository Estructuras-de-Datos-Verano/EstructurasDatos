# Reflexion tecnica - Clase 08

Nombre: José Iván Reyna Blanco

## Ideas recurrentes

Que ideas aparecieron en varios recursos?

- Estructuras ocultas: Varias herramientas avanzadas se construyen encima de estructuras más simples. Por ejemplo, los arreglos dinámicos y los heaps usan arreglos estáticos/listas normales por debajo, mientras que los grafos se representan con diccionarios y listas estándar.
- Intercambio entre tiempo y memoria (Trade-offs): Mejorar la velocidad de una operación suele requerir más espacio. Esto se vio claramente al comparar listas simples con listas dobles (más memoria para punteros a cambio de borrar rápido al final) o al usar `deque` para operaciones optimizadas en los extremos.
- La importancia de la eficiencia asintótica $O(1) vs O(n): Todos los recursos justifican el uso de una estructura específica demostrando matemáticamente cómo reduce el tiempo de ejecución en operaciones críticas (como búsquedas, inserciones o eliminaciones). Suele convenirnos que las operaciones dependan en la menor proporcion posible de n, 

## Comparacion critica

Compara al menos dos recursos.

| Aspecto | Recurso A (Video: Linked Lists - WilliamFiset) | Recurso B (Texto: Documentación `collections` - Python) |
| --- | --- | --- |
| Claridad | Alta. Va despacio y explica de manera muy intuitiva el concepto de nodos y referencias. | Media. Es directo en sus resúmenes, pero el lenguaje se vuelve seco y puramente técnico más adelante. |
| Ejemplos | Muy didácticos. Muestra problemas típicos como el conteo desde índice cero y cómo se rompen los enlaces. | Prácticos pero planos. Muestra bloques de código reales (como usar `Counter`), pero sin explicar el trasfondo. |
| Profundidad | Básica. Se enfoca en que entiendas el concepto visual y la lógica de los punteros sin saturar con código. | Alta. Explica detalles de la implementación del lenguaje y métodos específicos de las clases. |
| Visualizaciones | Excelente. Uso de animaciones digitales fluidas que muestran cómo se conectan y desconectan los nodos. | Ninguna. Es un manual de referencia en texto plano. |
| Codigo | No incluye en este video. Se reserva la implementación en código para la siguiente parte de su lista de reproducción. | Abundante. Incluye ejemplos de código listos para copiar, pegar y probar directamente en la terminal. |

## Recurso mas util

Cual fue el recurso mas util para ti y por que?

- La documentación de deque. No había entendido bien sus operaciones ni el principio de origen de su implementación.

## Recurso menos recomendable

Cual fue el recurso menos recomendable o menos claro y por que?

- El vídeo: 1.11 Best Worst and Average Case Analysis. El instructor tiene una metodologpia muy ingenieril de saltarse la teoría y volver toda explicación en uso de intuición disfrazada de lógica cuando en ciertos casos es mejor contar todas las operaciones (aunque parezcan despreciables) por el uso de memoria. 

## Relacion con el curso

Como se conecta esta investigacion con Josephus, Nearest Smaller Values, pilas, colas, diccionarios o pruebas?

- Pilas y Colas: Las estructuras analizadas en `collections` (como `deque`) y las listas enlazadas son la base óptima para implementar pilas y colas con operaciones de inserción y extracción en tiempo constante O(1).
- Problema de Josephus: Se resuelve de forma eficiente utilizando una cola (implementada mediante un `deque`), donde los elementos se eliminan del frente y se vuelven a añadir al final (rotación) de forma sucesiva en tiempo O(1).
- Nearest Smaller Values: Este problema depende del uso de una pila para mantener un registro de los candidatos a ser el menor valor más cercano. El análisis de arreglos y tiempos de acceso explica por qué una pila basada en arreglos dinámicos o listas enlazadas mantiene el algoritmo en tiempo lineal O(n).
- Diccionarios y Grafos: La investigación sobre grafos demuestra que los diccionarios nativos de Python son la estructura perfecta para mapear nodos (como llaves) con sus listas de vecinos (como valores), permitiendo representar redes complejas de manera limpia y nativa.

## Preguntas nuevas

Formula al menos tres preguntas tecnicas que quieras resolver en las siguientes clases.

1. ¿Cómo maneja internamente Python la memoria cuando un `deque` crece, considerando que no usa un bloque de memoria contiguo único como las listas normales?
2. Si un Min-Heap mantiene el elemento mínimo arriba en tiempo constante O(1), ¿cuál es el costo temporal real si necesito buscar o borrar un elemento cualquiera que esté atrapado en un lugar lejos de las orillas del heap?
3. Para algoritmos de grafos que modifican constantemente sus conexiones en tiempo de ejecución, ¿es más eficiente utilizar una Lista de Adyacencia o una Matriz de Adyacencia en términos de velocidad de actualización/tiempos de búsqueda?

## Que explicarias diferente

Si tuvieras que explicar uno de los temas investigados a otro estudiante, que cambiarias respecto a los recursos que consultaste?

- Explicaría la complejidad con más cautela en el paso a paso de contar operaciones en vez de hacerlo informal. 
