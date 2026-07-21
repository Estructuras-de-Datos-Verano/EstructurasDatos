# Arturo Prudencio Bonilla

## Pregunta inicial
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
Para identificar la operación dominante y elegir adecuadamente, aplicamos una ruta estructurada: partimos de definir el problema y determinar su objetivo (camino, conexión u orden) Luego, modelamos el tipo de grafo identificando la dirección, los pesos y el significado de sus aristas A partir de estas restricciones, reconocemos cuál es la operación que dictará el costo al repetirse (operación dominante) y seleccionamos la estructura de datos que haga barata dicha operación Esto nos lleva naturalmente al algoritmo compatible, el cual sometemos a validación mediante contratos, precondiciones y pruebas distintivas antes de comunicar su complejidad

---

## 1. Recuperación: primero aparecen las estructuras
**¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?**
*   **Cola:** Retirar en orden de llegada
*   **Deque:** Agregar y retirar por ambos extremos
*   **Heap:** Consultar y extraer una prioridad extrema
*   **Union-Find:** Preguntar si dos nodos ya están conectados y fusionarlos
*   **Grados de entrada + cola:** Detectar tareas sin requisitos pendientes

---

## 2. Del enunciado a una decisión
**¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?**
Es peligroso porque saltar desde una simple palabra del enunciado hasta un algoritmo genera asociaciones muy frágiles Por ejemplo, la palabra "conectar" puede referirse a buscar la alcanzabilidad, buscar una ruta específica o conectar globalmente toda una red, y cada uno de esos objetivos requiere algoritmos distintos

---

## 3. Identificar el objetivo
**¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?**
*   La salida de un camino mínimo toma la forma de una **ruta** específica entre un origen y otros nodos
*   La salida de un MST (conexión mínima global) toma la forma de un **conjunto de aristas**
*   La salida de un orden topológico toma la forma de una **secuencia de nodos**

---

## 4. Dirección y significado de las aristas
**¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?**
Tratar una dependencia dirigida como una arista simétrica (no dirigida) cambiaría por completo quién bloquea a quién Esto destruiría el significado lógico de las dependencias o de elementos como calles de un solo sentido, provocando recorridos completamente inválidos

---

## 5. Clasificar el dominio de pesos
**¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?**
Porque es el dominio completo de los pesos lo que decide cuál invariante algorítmico es válido 0-1 BFS necesita obligatoriamente que los pesos sean exclusivamente 0 y 1 para que su estructura de dos prioridades (frente y fondo) funcione[cite: 8], mientras que Dijkstra requiere y soporta distancias con pesos no negativos generales

---

## 6. Matriz de decisión integradora
**¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?**
La columna de la **"Operación dominante"** explica mejor esta decisión Las estructuras de datos se eligen primordialmente para abaratar o volver eficiente la operación que el problema repetirá de manera constante

---

## 7. Laboratorio de decisión interactivo
**¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?**
Antes de revelar, debes predecir el objetivo, la estructura de datos a usar y el algoritmo La evidencia que usarás para corregir o confirmar tu predicción incluye el contrato, la prueba distintiva y la complejidad asintótica de la solución

---

## 8. Caso de camino sin pesos: BFS
**¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?**
El invariante clave es que todas las capas de distancias anteriores ya fueron exploradas, y la estructura de cola asegura estrictamente ese orden Esto garantiza que cuando se descubre un nodo nuevo, ninguna ruta futura con menor cantidad de aristas puede aparecer

---

## 9. Caso de pesos 0/1: 0-1 BFS
**¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?**
Una mejora de peso 0 entra al frente porque representa un avance donde se conserva exactamente el mismo costo actual, priorizándose su exploración Una de peso 1 se envía al final del deque porque lógicamente debe quedar a la espera, detrás de los candidatos que mantienen el costo actual

---

## 10. Caso de pesos generales: Dijkstra
**¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?**
La operación repetida de consultar y extraer continuamente la menor distancia tentativa desde un origen entre múltiples candidatos disponibles

---

## 11. BFS, 0-1 BFS y Dijkstra no forman una competencia
**¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?**
Dijkstra es un algoritmo correcto para pesos 0 y 1 porque dichos pesos cumplen su contrato de ser valores no negativos Sin embargo, no es la elección más especializada ni adecuada porque añade un costo de procesamiento innecesario de $\mathcal{O}((V+E) \log V)$, cuando el algoritmo 0-1 BFS puede aprovechar ese dominio de pesos limitado para resolver el problema eficientemente en $\mathcal{O}(V+E)$

---

## 12. Pesos negativos: rechazar con precisión
**¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?**
La justificaría articulando tres aspectos: 
1. Que existe un **contrato violado** al haber pesos negativos en la red
2. Que **se pierde el invariante** de seguridad de que una distancia extraída como mínima es "definitiva", ya que podría mejorar en el futuro sumando una arista negativa
3. Estableciendo el **alcance**, confirmando honestamente que ninguno de los algoritmos revisados resuelve este caso general

---

## 13. Conexión global: Kruskal y Union-Find
**¿Qué consulta repetida de Kruskal justifica usar Union-Find?**
La consulta crítica de verificar rápida y repetidamente si los extremos de una arista ya pertenecen a la misma componente conectada, así como la operación de fusionar eficientemente dichas componentes sin crear ciclos

---

## 14. Árbol de caminos mínimos no es MST
**¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?**
Porque Dijkstra está diseñado exclusivamente para minimizar las distancias individuales trazadas desde un nodo origen específico, no para optimizar la red completa Por el contrario, Kruskal (MST) no prioriza rutas desde un origen, sino que busca minimizar de forma global la suma total de la red que interconecta a todos

---

## 15. Dependencias: Kahn y grados de entrada
**¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?**
Significa que la tarea o nodo evaluado ya no cuenta con requisitos pendientes que lo bloqueen En ese preciso instante se vuelve disponible para ingresar a la cola

---

## 16. BFS y Kahn comparten cola, no invariante
**¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?**
Se distinguen mediante su estado auxiliar y su regla de entrada BFS utiliza un mapa de visitados o distancias y encola un nodo por el simple hecho de ser descubierto Kahn utiliza los grados de entrada como estado auxiliar y exige como regla que el nodo ingrese a la cola únicamente cuando su grado alcanza el cero

---

## 17. Contratos antes de ejecutar
**¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?**
El código integrador tiene la responsabilidad fundamental de validar el contrato verificando la representación, los nodos, los pesos y la dirección del grafo Además, es responsable de adaptar los datos sin adulterar su significado original e interpretar correctamente qué significan los retornos especiales de la función (como listas vacías o valores nulos)

---

## 18. Reutilización en lugar de recopia
**¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?**
Porque importar y diseñar un adaptador estrecho permite verificar que los componentes se integran correctamente sin generar copias divergentes de código en la base del proyecto

---

## 19. Diseñar pruebas que distinguen decisiones
**¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?**
Una prueba es verdaderamente distintiva cuando está obligada a fallar frente a una alternativa algorítmica plausible, evidenciando las decisiones que los separan Si la prueba solamente verifica un escenario "feliz" donde todos los candidatos podrían llegar al mismo resultado o funcionar bien, entonces no sirve para proteger o distinguir la decisión técnica

---

## 20. Clínica de selecciones incorrectas
**Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.**
*   **Propuesta 1 ("Usaré BFS... calles tienen tiempos 2 y 9"):** El objetivo real es buscar un camino mínimo con costos heterogéneos El contrato violado es que BFS no modela ni acepta pesos dispares La operación dominante debe ser extraer la menor distancia tentativa acumulada La elección algorítmica adecuada es Dijkstra
*   **Propuesta 2 ("Usaré Dijkstra para conectar todas las sedes"):** El objetivo real es la conexión mínima global de la red, no la ruta a las sedes desde un punto origen El contrato violado involucra aplicar Dijkstra para un objetivo que no le corresponde La operación dominante debe ser unir componentes mediante la arista más barata La elección adecuada es el algoritmo de Kruskal utilizando Union-Find

---

## 21. Trabajo en equipo A: movilidad urbana
**¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?**
*   En **A1**, la red no posee pesos (o son unitarios), por ende, la estructura usada es una cola procesada con BFS
*   En **A2**, el dominio de los pesos se limita a 0 y 1, cambiando la estructura idónea a una deque y el algoritmo a 0-1 BFS
*   En **A3**, se tienen costos variados y no negativos; esto demanda el uso de un heap como estructura y Dijkstra como algoritmo

---

## 22. Trabajo en equipo B: construir y planificar
**¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?**
Porque a pesar de compartir los nodos (edificios), las aristas representan dinámicas completamente distintas La primera necesidad pide conexión simétrica y global (Kruskal), mientras que la segunda necesidad exige precedencias técnicas estrictamente dirigidas (Kahn) 

---

## 23. Comunicación técnica de una decisión
**¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?**
Debe incluir el objetivo claro, el tipo de grafo (su dirección y pesos), la operación dominante a realizar, la estructura de datos acoplada con el algoritmo, el contrato con las precondiciones estipuladas, la prueba que lo valida, la complejidad expresada en V y E, la interpretación de la respuesta y las razones exactas para descartar alternativas

---

## 24. Reflexión final del curso
**¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?**
1.  Antes elegía una estructura guiándome por simple intuición o familiaridad; ahora primero identifico la operación que domina el costo del problema
2.  El contrato que más me ayudó a detectar un error fue validar el dominio de pesos porque evitó tratar de solucionar todo ciegamente con un mismo algoritmo, como usar Dijkstra ante pesos negativos
3.  Ante un algoritmo que no aplica, ahora puedo rechazar una alternativa explicando con mucha precisión técnica qué contrato o invariante estaría rompiéndose

---

## 25. Síntesis y cierre
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
1.  Comenzamos determinando lo que el problema quiere producir: un camino, una conexión u orden 
2.  Modelamos el problema y sus aristas dictando si tiene dirección y el dominio de los pesos 
3.  Evaluamos qué cálculo o validación repetiremos más, convirtiéndola en la **operación dominante** 
4.  Buscamos la estructura que hace eficiente esa operación y la unimos al **algoritmo** diseñado sobre ella 
5.  Finalmente, aseguramos la robustez con un **contrato** y evidenciamos los casos frontera usando una **prueba distintiva**