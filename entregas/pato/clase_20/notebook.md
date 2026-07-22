# Clase 20: Notebook
#### Nombre: Patricio Navarro

## Pregunta inicial
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
- Operación dominante: la operación que más se repite y que define el comportamiento del problema.
- Estructura: Dependiendo de la operación ya sabemos si se comporta como una cola, un heap, un árbol AVL, etc.
- Algoritmo: ya que tenemos la estructura definimos las operaciones necesarias.

## Recuperación
| Recurso | Operación que vuelve barata | Situación donde fue necesario |
| --- | --- | --- |
| Cola | retirar en orden de llegada | Comparación BFS con Dijkstra |
| Deque | agregar y retirar por ambos extremos | Listas doblemente enlazadas |
| Heap | consultar y extraer una prioridad extrema | Algoritmo de Dijkstra |
| Union-Find | preguntar si dos nodos ya están conectados y fusionarlos | Kruskal |
| Grados de entrada + cola | detectar tareas sin requisitos pendientes | 0-1 BFS |

¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?
- Cola: Sirve para retirar los elementos exactamente en el mismo orden en el que llegaron.  
- Deque: Permite agregar y quitar datos de forma rápida por cualquiera de los dos extremos (al principio o al final).  
- Heap: Se usa para consultar y extraer rápidamente un valor que tiene una prioridad extrema.  
- Union-Find: Funciona para preguntar si dos puntos ya están conectados entre sí y, si no lo están, fusionarlos.  
- Grados de entrada + cola: Útil para detectar cuáles tareas ya no tienen requisitos pendientes por cumplir.

## Del enunciado a una decisión
**¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?**
- Porque guiarse por una sola palabra crea conexiones débiles. Por ejemplo, "conectar" puede significar que buscas si es posible llegar a un punto, o que quieres una ruta específica, o que necesitas unir toda una red de puntos.

## Identificar el objetivo
**Actividad.** Para cada frase, escribe la forma de la salida: una ruta, un conjunto de aristas o una secuencia de nodos. Esa forma suele revelar el objetivo antes de pensar en código.
- “Llegar barato de A a D”: Una ruta con costo mínimo.
- “tender la red total más barata”: Conjunto de aristas.
- “instalar equipos después de sus requisitos”: Secuencia de nodos.

¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?
- Camino mínimo: Su salida es una ruta `A -> B -> C`.  
- MST: Su salida es un conjunto de aristas `(A - B), (B - C), (C - D)`  
- Orden topológico: Su salida es una secuencia de nodos. 
    ```text
    1. Analizar
    2. Implementar
    3. Probar
    ```

## Dirección y significado de las aristas
**¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?**
- Si tratamos una dependencia como si fuera una conexión de doble sentido, alteraríamos quién bloquea a quién. Duplicar la flecha de forma automática destruye las dependencias dirigidas.

## Clasificar el dominio de pesos
**¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?**
- Saber que "hay pesos" no alcanza porque el dominio completo de esos pesos es lo que define qué algoritmo usar. Si los pesos son estrictamente 0 y 1, usas 0-1 BFS porque saca ventaja de tener solo esas dos prioridades. Si los pesos son números generales que no son negativos entonces usas Dijkstra.

## Matriz de decisión integradora
**¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?**
- Operación dominante, te dice exactamente qué necesita el problema y como se comporta.

## Laboratorio de decisión interactivo
**Actividad:** Escribe una predicción para el reto que hayas elegido.
- Reto: Ruta más rápida para una ambulancia:
    - Objetivo: camino de costo mínimo, el costo es el tiempo.
    - Dirección: depende del costo mínimo pero es unidireccional.
    - Pesos: el tiempo que toma un tramo.
    - Operación dominante: suma no negativa mínima.
    - Estructura: Heap
    - Algoritmo: Dijkstra
    - Contrato: Devolver la ruta cuya suma sea la menor posible. No aceptar valores negativos en los pesos, trabajar con heap.
    - Prueba distintiva: Crear un caso donde una ruta con más calles tome menos tiempo que una ruta de una sola calle. 
    - Complejidad: `O((V+E)log (V))`, donde `V` representa las intersecciones de la ciudad y `E` representa los tramos de calles.  
    - Interpretación: La salida te da la secuencia exacta de calles que garantizan el menor tiempo posible para la ambulancia.

¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?
- El objetivo del problema, la estructura de datos que se necesita y el algoritmo a usar.
- Contratos, pruebas y complejidad.

## Caso de caminos sin pesos: BFS
**¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?**
- El invariante es que BFS procesa la información por capas. Una vez que un nodo se descubre desde una capa anterior, es seguro que ninguna ruta futura podrá llegar a él usando menos aristas, porque ya se recorrieron todas las rutas con menos aristas.

## Caso de pesos 0/1: 0-1 BFS
**¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?**
- Porque la de peso 0 es casi inmediata, mientras que la de peso 1 requiere más tiempo, entonces es de menor prioridad.

## Caso de pesos generales: Dijkstra 
**¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?**
- Que se ncesita la menor distancia tentativa, osea el mínimo. Heap justo está ordenado así.

## BFS, 0-1 BFS y Dijkstra no forman una competencia
**¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?**
- Dijkstra puede resolver un grafo de pesos 0 y 1 correctamente, pero es una herramienta menos especializada para este caso. 0-1 BFS es mucho más adecuado porque aprovecha que solo hay dos valores para resolver el problema con un costo más barato de `O(V+E)`.

## Pesos negativos: rechazar con precisión
**¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?**
1. El contrato se viola porque existen pesos negativos. 
2. El argumento central se rompe: una distancia que ya se extrajo podría mejorar después si se topa con un peso negativo. 
3. Concluir que ninguno de los algoritmos estudiados resuelve este caso general.

## Conexión global: Kruskal y Union-Find
**¿Qué consulta repetida de Kruskal justifica usar Union-Find?**
- La consulta de saber si los dos extremos de una conexión ya pertenecen a la misma componente. 

## Árbol de caminos mínimos no es MST
**¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?**
- Porque buscan objetivos muy diferentes. 
    - Dijkstra intenta hacer que cada distancia sea la mínima posible partiendo desde un origen específico. 
    - Kruskal, en cambio, busca minimizar la suma de toda la red en conjunto para que todos estén conectados.

## Dependencias: Kahn y grados de entrada
**¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?**
- Significa que esa tarea o nodo ya está disponible para ejecutarse porque no tiene requisitos pendientes que lo bloqueen.

## BFS y Kahn comparten cola, no invariante
**¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?**
- El estado auxiliar que guardan nos permite distinguirlos. 
    - BFS usa la cola para guardar nodos descubiertos apoyándose en distancias o visitados
    - Kahn guarda nodos disponibles fijándose en los grados de entrada.

## Contratos antes de ejecutar
**¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?**
- Validar la representación de los datos, los nodos, los pesos y la dirección de las aristas. 
- Interpretar correctamente los retornos especiales de acuerdo al contrato.

## Reutilización en lugar de recopia
**¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?**
- Porque copiar el mismo código muchas veces genera varias versiones y puede que se genere un error.

## Diseñar pruebas que distinguen decisiones
**¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?**
- Debe estar diseñada para fallar ante una alternativa incorrecta que parecía buena idea. 

## Clínica de selecciones incorrectas
**Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.**
1. “Usaré BFS porque hay que llegar de A a B”, pero las calles tienen tiempos 2 y 9.
    - El objetivo real es buscar el camino mínimo.
    - Se viola el contrato porque BFS no maneja pesos generales. 
    - La operación dominante debe ser extraer la menor distancia.
    - La elección correcta es usar un heap con Dijkstra.  
3. “Usaré Kahn porque hay una cola”, pero se pide la ruta con menos saltos. 
    - El objetivo real es recorrer una ruta.
    - Se viola porque Kahn organiza precedencias dirigidas, no rutas. 
    - La operación dominante es procesar el grafo por capas.
    - Lo adecuado es usar una cola con BFS.

## Trabajo en equipo A: movilidad urbana
**¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?**
- Para A1, como no hay pesos, la estructura es una cola y el algoritmo es BFS. 
- Para A2, como los pesos son estrictamente 0 y 1, la estructura cambia a un deque usando 0-1 BFS.
- Para A3, al haber tiempos generales no negativos, la estructura requerida es un heap utilizando Dijkstra. 

## Trabajo en equipo B: construir y planificar
**¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?**
- No se puede usar el mismo algoritmo porque las conexiones significan cosas muy diferentes en cada problema. 
    - Para tender la red se usan conexiones simétricas y se busca un MST. 
    - Para la renovación se usan dependencias dirigidas que marcan prerrequisitos y bloqueos.

## Comunicación técnica de una decisión
**¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?**
- Debe tener: 
    - El objetivo del problema, cómo es la dirección y el dominio de pesos del grafo, y la operación dominante. 
    - Explicar la estructura elegida, el algoritmo, su contrato, cómo se prueba y cuál es su complejidad. 
    - Indicar cómo se interpreta la salida y por qué se descartaron otras opciones.

## Reflexión final del curso
**Actividad:** Completa las frases
1. “Antes elegía una estructura por lo que fuera más fácil implementar ahora primero identifico que me está pidiendo realmente con la operación dominante.”
2. “El contrato que más me ayudó a detectar un error fue validar el tipo de pesos porque hay varios algoritmos que trabajan con pesos pero algunso son más óptimos para ciertos tipos aunque varios pudieran resolver el mismo problema.”
3. “Ante un algoritmo que no aplica, ahora puedo rechazarlo y corregir.”

¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?
- Basarme más por el comportamiento del problema que por la solución tal cual.

## Síntesis y cierre
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
1. Identificamos si queremos producir un camino, una conexión global o un orden.
2. Revisamos cómo es el modelo y con esto determinamos cuál será la operación que más se va a repetir. 
3. Sabiendo esa operación dominante, podemos elegir la estructura de datos que la hace más barata y, por consiguiente, el algoritmo que sea compatible.