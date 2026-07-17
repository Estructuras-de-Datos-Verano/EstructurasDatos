

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

## Punto 8: 8. Caso de camino sin pesos: BFS
- **Pregunta:** ¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?

## Punto 9: 9. Caso de pesos 0/1: 0-1 BFS
- **Pregunta:** ¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?

## Punto 10: 10. Caso de pesos generales: Dijkstra
- **Pregunta:** ¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?

## Punto 11: 11. BFS, 0-1 BFS y Dijkstra no forman una competencia
- **Pregunta:** ¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?

## Punto 12: 12. Pesos negativos: rechazar con precisión
- **Pregunta:** ¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?

## Punto 13: 13. Conexión global: Kruskal y Union-Find
- **Pregunta:** ¿Qué consulta repetida de Kruskal justifica usar Union-Find?

## Punto 14: 14. Árbol de caminos mínimos no es MST
- **Pregunta:** ¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?

## Punto 15: 15. Dependencias: Kahn y grados de entrada
- **Pregunta:** ¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?

## Punto 16: 16. BFS y Kahn comparten cola, no invariante
- **Pregunta:** ¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?

## Punto 17: 17. Contratos antes de ejecutar
- **Pregunta:** ¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?

## Punto 18: 18. Reutilización en lugar de recopia
- **Pregunta:** ¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?

## Punto 19: 19. Diseñar pruebas que distinguen decisiones
- **Pregunta:** ¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?

## Punto 20: 20. Clínica de selecciones incorrectas
- **Pregunta:** Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.

## Punto 21: 21. Trabajo en equipo A: movilidad urbana
- **Pregunta:** ¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?

## Punto 22: 22. Trabajo en equipo B: construir y planificar
- **Pregunta:** ¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?

## Punto 23: 23. Comunicación técnica de una decisión
- **Pregunta:** ¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?

## Punto 24: 24. Reflexión final del curso
- **Pregunta:** ¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?

## Punto 25: 25. Síntesis y cierre
- **Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?