## Pregunta inicial

Ya entendemos la idea de Dijkstra. ¿Cómo se convierte en una implementación confiable, reutilizable y testeable?

Se logra separando las responsabilidades de tu código

## 1. De algoritmo correcto a software confiable

**Pregunta:** ¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?

Pasar a código real exige validar que los datos de entrada no rompan el sistema, definir tipos de datos claros, documentar el comportamiento esperado y estructurar la función para que sea fácil de probar en entornos reales.

## 2. Un orden profesional de lectura

Leer la firma y el docstring te permite entender el contrato (qué entra, qué sale y qué promete hacer) antes de meterte en el barro de la lógica y los bucles.

**Pregunta:** ¿Por qué conviene leer firma y docstring antes que el while principal?

## 3. Tipos como decisiones de diseño

**Pregunta:** ¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?

Aceptar Mapping/Sequence hace que tu código funcione con cualquier estructura compatible (como defaultdict o tuplas), mientras que exigir dict/list acopla tu software a implementaciones rígidas y limita al usuario.

## 4. Normalización y copia defensiva

**Pregunta:** ¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?

Evita que cambios externos muten el grafo original a mitad del proceso y estandariza posibles inconsistencias en los datos para trabajar siempre sobre un estado predecible y seguro.

## 5. TypeError y ValueError cuentan historias distintas

**Pregunta:** ¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?

Lanzas TypeError si te pasan un tipo de dato incorrecto (como un string en lugar de un diccionario) y ValueError si el tipo es correcto pero el valor es inválido para el algoritmo (como pesos de aristas negativos).

## 6. Bool, NaN e infinito

**Pregunta:** ¿Por qué True y NaN requieren comprobaciones específicas?

En Python, True equivale a 1 (lo que puede arruinar tus índices si usas enteros) y NaN rompe las comparaciones de orden porque cualquier evaluación con él da falso, lo que destruye la lógica de la cola de prioridad.

## 7. Vecinos implícitos y representación total

**Pregunta:** ¿Qué fallo evita resultado.setdefault(vecino, [])?

Evita que el código lance un KeyError al intentar explorar nodos "hoja" (destinos que no tienen aristas salientes y, por ende, no están declarados como claves en el diccionario del grafo).

## 8. El contrato de dijkstra

**Pregunta:** ¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?

Devuelve los costos mínimos y los predecesores porque con esa información puedes reconstruir el camino más corto a cualquier nodo, separando el cálculo pesado del grafo de la consulta de una ruta específica.

## 9. Estado inicial y tablas totales

**Pregunta:** ¿Qué invariante establecen las comprensiones antes del while?

Aseguran que todos los nodos del grafo arranquen con una distancia infinita y sin predecesor, garantizando que el algoritmo maneje correctamente incluso los nodos que resulten ser completamente inalcanzables.

## 10. El guard clause de entradas obsoletas

**Pregunta:** ¿Qué garantiza la comparación inmediatamente posterior a heappop?

Evita procesar nodos con distancias desactualizadas que se quedaron atrapados en la cola de prioridad ("búsqueda perezosa"), ahorrando iteraciones innecesarias y costosas en grafos grandes.

## 11. Relajación y actualización atómica

**Pregunta:** ¿Qué datos deben actualizarse juntos cuando una candidata mejora?

Debes actualizar al mismo tiempo el costo acumulado hacia el nodo vecino en tu tabla de distancias y registrar su predecesor en el mapa de rutas para que ambos estados se mantengan siempre sincronizados.

## 12. Reconstruir es otro problema

**Pregunta:** ¿Qué diferencia hay entre destino inalcanzable y destino ausente?

Un destino "inalcanzable" es un nodo que existe en el grafo pero al que no se puede llegar (distancia infinita), mientras que un destino "ausente" es un nodo que directamente no forma parte del mapa de datos.

## 13. Coordinación sin duplicación

**Pregunta:** ¿Qué responsabilidades delega camino_minimo?

Se encarga únicamente de validar que los nodos existan, llamar al motor de Dijkstra y orquestar la reconstrucción del camino paso a paso, delegando la lógica pesada a otras funciones enfocadas.

## 14. Del contrato a una matriz de pruebas

**Pregunta:** ¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?

No verifica si el camino de predecesores devuelto es realmente el óptimo, ni valida si el algoritmo exploró y relajó los nodos intermedios en el orden correcto establecido por el contrato.

## 15. Auditoría de una implementación frágil

**Pregunta:** ¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?

Modifica directamente el grafo que le pasas, se rompe con un KeyError si un nodo no tiene vecinos declarados y entra en bucles infinitos o da rutas erróneas si encuentra pesos negativos.

## 16. Clínica de depuración

**Pregunta:** ¿Qué información mínima debe contener un reporte de fallo útil?

Debe incluir el grafo exacto que causó el fallo, el resultado que esperabas obtener frente al que obtuviste, y el error de Python (traceback) con la línea exacta donde se rompió.

## 17. Revisión profesional de código

**Pregunta:** ¿Qué hace que un comentario de revisión sea accionable y verificable?

Debe ser constructivo: señala el problema técnico de forma objetiva, explica el riesgo o impacto de no corregirlo y propone un contraejemplo de código claro para solucionarlo.

## 18. Complejidad sin perder robustez

**Pregunta:** ¿La normalización cambia la complejidad asintótica de Dijkstra?

No. Normalizar o copiar el grafo toma un tiempo lineal, lo cual es absorbido por la complejidad superior de Dijkstra con cola de prioridad.

## 19. Cuatro algoritmos, cuatro operaciones dominantes

**Pregunta:** ¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?

Dijkstra: Cola de prioridad (heap) para extraer el mínimo.

Bellman-Ford / BFS: Cola FIFO o lista para relajaciones sistemáticas.

Floyd-Warshall: Matrices bidimensionales para programación dinámica.

## 20. Cierre

**Pregunta:** ¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?

Pruebas robustas (casos felices, límites y manejo de errores) combinada con tipado estático estricto y documentación clara que actúe como garantía de que el código hace lo que dice.