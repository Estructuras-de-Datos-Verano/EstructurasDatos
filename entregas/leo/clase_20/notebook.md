# Respuestas del notebook — Clase 20

Nombre: Leonardo Daniel Arenas Serafín

## Pregunta inicial

#### **Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
Debemos de analizar el problema para ver qué es lo que pide solucionar y mediante qué criterio, saber qué se prioriza.

## 1. Recuperación: primero aparecen las estructuras

#### ¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?

| Recurso | Situación |
| --- | --- |
| Cola | clase 16 para BFS |
| Deque | clase 17 0-1 BFS |
| Heap | clase 17 para Dijkstra |
| Union-Find | clase 18 para Kruskal |
| Grados de entrada + cola | clase 19 para Kahn |

#### **Actividad diagnóstica.** Sin nombrar algoritmos todavía, escribe junto a cada recurso una situación de las Clases 16–19 donde fue necesario. Después compara: dos algoritmos pueden compartir cola y aun así mantener invariantes distintos.

#### ¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?
La búsqueda del elemento prioritario y de menor costo.

## 2. Del enunciado a una decisión

#### ¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?
Porque puede ser que no sea el óptimo.

## 3. Identificar el objetivo

#### ¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?
El camino mínimio tiene dos salidas, una lista con el camino a seguir y su costo, un MST devuelve un árbol y orden topológico devuelve una secuencia de orden de salida de elementos.

## 4. Dirección y significado de las aristas

#### ¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?
Se podría pensar que está en ambos sentidos, por lo que se cae en un ciclo y se rompe el algoritmo

## 5. Clasificar el dominio de pesos

#### ¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?
Porque no solamente hay que delimitar el si hay o no pesos, sino su dominio para conocer las invariantes

## 6. Matriz de decisión integradora

#### ¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?
La operación dominante

## 7. Laboratorio de decisión interactivo

#### ¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?
- Objetivo: Conocer el camino de costo mínimo
- Dirección: Origen -> Destino
- Pesos: no negativos
- Operación dominante: buscar el mínimo
- Estructura: Heap
- Algoritmo: Dijkstra
- Contrato: costos no negativos
- Prueba distintiva: Verificar que no se basa en número de aristas
- Complejidad: O(E log(E))
- Interpretación: Es un Dijkstra aplicado
Usaré el display interactivo para corregir

## 8. Caso de camino sin pesos: BFS

#### ¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?
Que toda arista tiene peso 1

## 9. Caso de pesos 0/1: 0-1 BFS

#### ¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?
Para poder diferenciar entre camino conveniente y no conveniente, bien podría hacerse al revés y no cambiaría nada

## 10. Caso de pesos generales: Dijkstra

#### ¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?
Priorizar el mínimo.

## 11. BFS, 0-1 BFS y Dijkstra no forman una competencia

#### ¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?
Puede ser correcto en el sentido de que encontraría el camino mínimo, pero no sería la elección más adecuada porque aumenta la complejidad

## 12. Pesos negativos: rechazar con precisión

#### ¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?
Porque cada algoritmo tiene sus propias invariantes que los distinguen y los especializan para ser más eficientes al resolver ciertos problemas, por lo que no existe un caso general que funcione ´de manera óptima.

## 13. Conexión global: Kruskal y Union-Find

#### ¿Qué consulta repetida de Kruskal justifica usar Union-Find?
El revisar si es que dos nodos ya están conectados para decidir si conectarlos o no

## 14. Árbol de caminos mínimos no es MST

#### ¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?
Porque Dijkstra lo único que hace es mappear el grafo, otra función es la encargada de minimzar el costo

## 15. Dependencias: Kahn y grados de entrada

#### ¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?
Que no tiene ningún prerrequisito para poder ser procesado.

## 16. BFS y Kahn comparten cola, no invariante

#### ¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?
Que Kahn usa la cola con elementos que ya pueden ser procesados para ir avanzando al tener grado 0 como invariante, mientras que en BFS solo da la información de cuáles posibles caminos hay para seguir avanazando.

## 17. Contratos antes de ejecutar

#### ¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada
Que debe de  verificar que efectivamente las invariantes sean respetadas y que pueda detectar errores, así como poder normalizar entradas en algunos casos

## 18. Reutilización en lugar de recopia

#### ¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?
Porque puede ser que la implementación previa coma cosas distintas y regrese cosas distintas a las que se pide, lo cual no satifacería lo que se pide. 

## 19. Diseñar pruebas que distinguen decisiones

#### ¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?
Que pruebe no solamente los casos felices, que tenga versatilidad

## 20. Clínica de selecciones incorrectas

#### Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.
1. “Usaré BFS porque hay que llegar de A a B”, pero las calles tienen tiempos 2 y 9: Está mal porque BFS trabaja con pesos unitarios o normalizados, no con pesos diferentes. Aquí la correción sería usar 0-1 BFS en vez d BFS
5. “Usaré Dijkstra aunque existe una arista −3”.:  Esto está incorrecto porque viola la invariante de que Dijkstra no permite pesos negativos, lo que se podría hacer para corregirlo es sumar +3 a todas las aristas para así evitar violar el contrato.

## 21. Trabajo en equipo A: movilidad urbana

#### ¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?
En A1 tenemos mismo costo para todas las aristas, por lo que no hay que buscar caminp mínimo por costos, solo por cantidad, por lo que se usaría cola BFS. A2 tiene costos 0 y 1, por lo que se usaría un deque y 0-1 BFS. A3 tiene costos distintos no negativos, por lo que se usaría heap en Dijkstra.

## 22. Trabajo en equipo B: construir y planificar

#### ¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?
Porque lo que cambian son las aristas, cambian su signficiado, su "peso" y su sentido

## 23. Comunicación técnica de una decisión

#### ¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?
Objetivo del problema, tipo de aristas, operación dominante, estructura y algoritmo a utilizar y su contrato e invariantes.

## 24. Reflexión final del curso

1. “Antes elegía una estructura por comodidad; ahora primero identifico el objetivo del problema.”
2. “El contrato que más me ayudó a detectar un error fue las invariantes porque son reglas explícitas que delimitan el algoritmo.”
3. “Ante un algoritmo que no aplica, ahora puedo adaptarlo.”

#### ¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?
Que antes no tenía realmente un proceso de decisión, simplemente era intuición. Ahora puedo hacer un proceso de análisis y evaluación de posibles estructras aplicadas para encontrar la que resuelva el problema de manera óptima.

## 25. Síntesis y cierre

#### Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?
Analizando qué es lo que el problema come y qué debe devolver.