

## Sección Inicial: Pregunta inicial
- **Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?
- Para esto, analizamos qué acción repetitiva consume más recursos en el enunciado, ya que esa operación específica nos indica qué estructura la abarata y qué algoritmo respeta sus restricciones.

## Punto 1: 1. Recuperación: primero aparecen las estructuras
- **Pregunta:** ¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?
- Buscamos abaratar operaciones clave; por ejemplo, la cola agiliza salidas en orden de llegada, el deque permite accesos en ambos extremos y el heap optimiza la extracción de prioridades.

## Punto 2: 2. Del enunciado a una decisión
- **Pregunta:** ¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?
- Esto es arriesgado porque términos como "conectar" pueden referirse a cosas muy distintas como la alcanzabilidad de un nodo o a una red global, lo que nos puede llevar a un diseño incorrecto.

## Punto 3: 3. Identificar el objetivo
- **Pregunta:** ¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?
- Sus estructuras finales difieren totalmente, ya que un camino mínimo nos devuelve una ruta específica, un MST nos entrega un conjunto de conexiones globales y el orden topológico resulta en una secuencia lineal.

## Punto 4: 4. Dirección y significado de las aristas
- **Pregunta:** ¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?
- Podríamos generar un error grave en la secuencia de ejecución, ya que ignorar el sentido de las dependencias permite realizar tareas sin haber completado obligatoriamente sus prerrequisitos.

## Punto 5: 5. Clasificar el dominio de pesos
- **Pregunta:** ¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?
- Para esto requerimos conocer el dominio exacto de los valores, ya que 0-1 BFS exige estrictamente valores binarios mientras que Dijkstra funciona con cualquier número no negativo.

## Punto 6: 6. Matriz de decisión integradora
- **Pregunta:** ¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?
- La columna de la operación dominante es la que justifica esta elección, ya que cada estructura se diseña específicamente para que esa acción crítica sea lo más eficiente posible.

## Punto 7: 7. Laboratorio de decisión interactivo
- **Pregunta:** ¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?
- Debemos anticipar el objetivo, la estructura y el algoritmo adecuado, utilizando posteriormente las restricciones y las pruebas distintivas como evidencia para ajustar nuestro análisis.

## Punto 8: 8. Caso de camino sin pesos: BFS
- **Pregunta:** ¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?
- Esto se debe a que BFS procesa el grafo estrictamente por capas de distancia de forma que los nodos más cercanos siempre se exploran antes que cualquier ruta más larga.
## Punto 9: 9. Caso de pesos 0/1: 0-1 BFS
- **Pregunta:** ¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?
- Hacemos esto para mantener la cola ordenada por prioridad de costo, ya que las rutas gratuitas deben procesarse de inmediato mientras que las de costo uno se postergan.

## Punto 10: 10. Caso de pesos generales: Dijkstra
- **Pregunta:** ¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?
- El heap es ideal para esto porque su propósito principal es consultar y extraer de manera barata la menor distancia tentativa que se encuentra acumulada en cada paso.

## Punto 11: 11. BFS, 0-1 BFS y Dijkstra no forman una competencia
- **Pregunta:** ¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?
- Aunque Dijkstra encuentra la solución real, no es óptimo para este caso ya que introduce una complejidad de orden logarítmico que el algoritmo 0-1 BFS resuelve de forma lineal.

## Punto 12: 12. Pesos negativos: rechazar con precisión
- **Pregunta:** ¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?
- Explicaría que se viola el contrato de Dijkstra, ya que la presencia de valores negativos rompe el invariante de que una distancia ya extraída del heap es definitiva.

## Punto 13: 13. Conexión global: Kruskal y Union-Find
- **Pregunta:** ¿Qué consulta repetida de Kruskal justifica usar Union-Find?
- Kruskal requiere verificar constantemente si los extremos de una arista ya están conectados, para lo cual Union-Find es perfecto ya que realiza esta validación casi instantáneamente.

## Punto 14: 14. Árbol de caminos mínimos no es MST
- **Pregunta:** ¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?
- Esto ocurre porque Dijkstra se enfoca en optimizar las rutas individuales partiendo desde un único origen, mientras que un MST busca abaratar la suma total de la red.

## Punto 15: 15. Dependencias: Kahn y grados de entrada
- **Pregunta:** ¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?
- Significa que esa tarea no tiene requisitos pendientes, por lo cual se encuentra completamente disponible para ser procesada e integrada en la secuencia final.

## Punto 16: 16. BFS y Kahn comparten cola, no invariante
- **Pregunta:** ¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?
- Para diferenciarlos observamos los estados auxiliares, ya que BFS utiliza un registro de nodos visitados y distancias mientras que Kahn depende del control de los grados de entrada.

## Punto 17: 17. Contratos antes de ejecutar
- **Pregunta:** ¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?
- Sigue siendo responsable de validar que los datos cumplan las precondiciones, ya que debe adaptar los formatos de entrada y dar una interpretación correcta al resultado.

## Punto 18: 18. Reutilización en lugar de recopia
- **Pregunta:** ¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?
- Duplicar código genera problemas de mantenimiento y posibles inconsistencias, mientras que usar un adaptador estrecho mantiene la lógica original limpia y centralizada.

## Punto 19: 19. Diseñar pruebas que distinguen decisiones
- **Pregunta:** ¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?
- Una prueba es distintiva porque está diseñada para que una alternativa incorrecta falle, demostrando con un caso límite por qué un algoritmo es mejor que otro para ese escenario.

## Punto 20: 20. Clínica de selecciones incorrectas
- **Pregunta:** Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.
- Usar BFS con calles de tiempos variables viola el contrato de costo uniforme; para esto requerimos extraer el costo mínimo con un heap y aplicar Dijkstra. Igualmente, usar Kruskal en dependencias falla porque el objetivo requiere un orden dirigido que se resuelve con Kahn.

## Punto 21: 21. Trabajo en equipo A: movilidad urbana
- **Pregunta:** ¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?
- Cambian según el dominio de los pesos de la red, ya que la ausencia de pesos nos lleva a BFS, los valores binarios a 0-1 BFS y los pesos generales a Dijkstra.
## Punto 22: 22. Trabajo en equipo B: construir y planificar
- **Pregunta:** ¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?
- Esto se debe a que las aristas representan conceptos distintos, ya que el primer problema busca una conexión global no dirigida y el segundo un orden de precedencias dirigidas.
## Punto 23: 23. Comunicación técnica de una decisión
- **Pregunta:** ¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?
- Debe declarar el objetivo, el tipo de grafo, la operación dominante, la estructura de datos elegida junto con su algoritmo, las precondiciones y su complejidad.

## Punto 24: 24. Reflexión final del curso
- **Pregunta:** ¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?
- Antes seleccionaba las herramientas por pura familiaridad, mientras que ahora identifico primero la operación dominante y las restricciones del problema para elegir con fundamentos.

## Punto 25: 25. Síntesis y cierre
- **Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?
-  Para lograrlo, seguimos una ruta lógica que conecta el objetivo y el tipo de grafo con la operación repetitiva más costosa, ya que esto nos asegura compatibilidad total.  