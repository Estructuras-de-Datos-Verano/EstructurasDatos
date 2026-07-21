## Pregunta inicial

**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**

Identificamos la operación analizando el objetivo, la dirección y los pesos del modelo. Con esto, elegimos la estructura que abarata la operación y un algoritmo cuyo contrato coincida.

## 1. Recuperación: primero aparecen las estructuras

**Pregunta:** ¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?

Cola: retirar en orden; Deque: retirar/agregar extremos; Heap: prioridad; Union-Find: conectar; Grados: dependencias.

## 2. Del enunciado a una decisión

**Pregunta:** ¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?

Palabras como "conectar" pueden significar alcanzabilidad, ruta o red global. Esto genera asociaciones frágiles y algoritmos erróneos.

## 3. Identificar el objetivo

**Pregunta:** ¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?

Un camino mínimo da una ruta, la conexión mínima global da un conjunto de aristas y un orden de dependencias da una secuencia.

## 4. Dirección y significado de las aristas

**Pregunta:** ¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?

Invertir la flecha cambia quién bloquea a quién, alterando el orden topológico y creando dependencias falsas.

## 5. Clasificar el dominio de pesos

**Pregunta:** ¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?

Porque 0-1 BFS aprovecha el dominio binario usando un deque en O(V+E), mientras Dijkstra gasta más tiempo con su heap.

## 6. Matriz de decisión integradora

**Pregunta:** ¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?

La columna "Operación dominante" justifica perfectamente qué estructura abarató el trabajo repetitivo.

## 7. Laboratorio de decisión interactivo

**Pregunta:** ¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?

Hay que predecir el objetivo, la estructura y el algoritmo. Corregimos con la evidencia del contrato y la prueba distintiva.

## 8. Caso de camino sin pesos: BFS

**Pregunta:** ¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?

Al procesar por capas, ninguna capa posterior podrá encontrar una ruta con menos pasos hacia un nodo ya descubierto.

## 9. Caso de pesos 0/1: 0-1 BFS

**Pregunta:** ¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?

La mejora de peso 0 no suma costo y toma máxima prioridad al frente; el peso 1 pospone el vértice al fondo.

## 10. Caso de pesos generales: Dijkstra

**Pregunta:** ¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?

Extraer continuamente la menor distancia tentativa descubierta hasta el momento.

## 11. BFS, 0-1 BFS y Dijkstra no forman una competencia 

**Pregunta:** ¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?

Aunque es correcto, usar un heap añade sobrecarga O((V+E) log V) a un problema que un deque resuelve en O(V+E).

## 12. Pesos negativos: rechazar con precisión

**Pregunta:** ¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?

Se viola el contrato: extraer una distancia no garantiza que sea mínima porque una arista negativa futura podría mejorarla. Ninguno estudiado lo soporta.

## 13. Conexión global: Kruskal y Union-Find

**Pregunta:** ¿Qué consulta repetida de Kruskal justifica usar Union-Find?

Preguntar repetidamente si los vértices de una nueva arista ya están conectados en la misma componente para evitar ciclos.

## 14. Árbol de caminos mínimos no es MST

**Pregunta:** ¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?

Dijkstra optimiza independientemente cada ruta desde un punto central, mientras que Kruskal conecta toda la red priorizando aristas globales baratas.

## 15. Dependencias: Kahn y grados de entrada

**Pregunta:** ¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?

Significa que la tarea ya no tiene prerrequisitos bloqueantes y puede entrar a la cola para ejecutarse.

## 16. BFS y Kahn comparten cola, no invariante

**Pregunta:** ¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?

BFS guarda estados de visita y distancias; Kahn usa un arreglo auxiliar de grados de entrada.

## 17. Contratos antes de ejecutar

**Pregunta:** ¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?

Validar la representación, nodos y pesos antes de delegar la ejecución, y luego interpretar los retornos según el dominio.

## 18. Reutilización en lugar de recopia

**Pregunta:** ¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?

Previene copias divergentes y errores; solo requiere un adaptador estrecho de entradas y salidas respetando la dirección y pesos.

## 19. Diseñar pruebas que distinguen decisiones

**Pregunta:** ¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?

Debe forzar a que los objetivos discrepen y fallar claramente para el algoritmo alternativo descartado.

## 20. Clínica de selecciones incorrectas

**Pregunta:** Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.

Propuesta 2: el objetivo es MST (Kruskal), no rutas; Dijkstra viola el contrato de costo total. Propuesta 4: Dependencias son dirigidas (Kahn), Kruskal exige no dirigido.

## 21. Trabajo en equipo A: movilidad urbana

**Pregunta:** ¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?

A1 usa cola y BFS (sin pesos); A2 usa deque y 0-1 BFS (pesos 0/1); A3 usa heap y Dijkstra (pesos positivos).

## 22. Trabajo en equipo B: construir y planificar

**Pregunta:** ¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?

La red física es simétrica y busca conectar (Kruskal); la renovación usa precedencias dirigidas (Kahn). El objetivo transforma el problema.

## 23. Comunicación técnica de una decisión

**Pregunta:** ¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?

Objetivo, restricciones, operación, estructura, algoritmo, contrato, prueba distintiva, complejidad, interpretación y alternativa rechazada.

## 24. Reflexión final del curso

**Pregunta:** ¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?

1. Elegía por intuición; ahora identifico la operación dominante. 2. Pesos no negativos porque evitó que extrajera distancias falsas. 3. Rechazar con precisión indicando el contrato violado.

## 25. Síntesis y cierre

**Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?

Determinamos qué objetivo, dirección y pesos forman la operación repetida. Luego asignamos la estructura óptima y verificamos el contrato.