# Clase 20 presencial y final: laboratorio integrador

## Pregunta inicial
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
Entiendiendo qué pide el problema.

## 1. Recuperación: primero aparecen las estructuras
**Actividad diagnóstica.** Sin nombrar algoritmos todavía, escribe junto a cada recurso una situación de las Clases 16–19 donde fue necesario. Después compara: dos algoritmos pueden compartir cola y aun así mantener invariantes distintos.

| Recurso | Operación que vuelve barata | Situación |
| --- | --- | --- |
| Cola | retirar en orden de llegada | Una sala de espera |
| Deque | agregar y retirar por ambos extremos | Implementar una pila, atender el elemento agregado más recientemente, como en un historial |
| Heap | consultar y extraer una prioridad extrema | Elegir un valor mínimo con prioridad |
| Union-Find | preguntar si dos nodos ya están conectados y fusionarlos | Unir todas las ciudades en un mapa |
| Grados de entrada + cola | detectar tareas sin requisitos pendientes | Cursos seriados en un plan de estudios |

**Pregunta:** ¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?
Porque podríamos equivocarnos. Es más importante saber qué requiere el problema.

## 3. Identificar el objetivo
**Actividad.** Para cada frase, escribe la forma de la salida: una ruta, un conjunto de aristas o una secuencia de nodos. Esa forma suele revelar el objetivo antes de pensar en código.

- **camino mínimo:** optimizar una ruta entre un origen y otros nodos;
Una ruta entre dos nodos y la suma de los pesos
- **conexión mínima global:** conectar todos los nodos minimizando el costo total de la red;
Mapa de todos los nodos conectados 
- **orden de dependencias:** producir una secuencia que respete precedencias.
Un orden válido

**Pregunta:** ¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?
Un camino mínimo conecta dos nodos específicos
Un MST conecta todo con todo
Un orden topológico espera que se hayan cumplido ciertos requisitos

## 4. Dirección y significado de las aristas
**Pregunta:** ¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?
El algoritmo podría tomar relaciones que, en realidad, no existen,y entregar rutas incorrectas

## 5. Clasificar el dominio de pesos
**Pregunta:** ¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?
Porque ambos tienen aristas ponderadas

## 6. Matriz de decisión integradora
**Pregunta:** ¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?
Operación dominante

## 7. Laboratorio de decisión interactivo
**Actividad:** BST
**Pregunta:** ¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?
Qué algoritmo usará

## 8. Caso de camino sin pesos: BFS
**Pregunta:** ¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?
Que todas las aristas pesan 1

## 9. Caso de pesos 0/1: 0-1 BFS
**Pregunta:** ¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?
Porque le da prioridad a los de 0

## 10. Caso de pesos generales: Dijkstra
**Pregunta:** ¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?
Elegir con prioridad

## 11. BFS, 0-1 BFS y Dijkstra no forman una competencia
**Pregunta:** ¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?
Dijkstra podría aplicar a 0-1 BFS porque también considera los pesos, pero Dijkstra considera muchos pesos distintos

## 12. Pesos negativos: rechazar con precisión
**Pregunta:** ¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?
Ninguno contempla restas en el peso, sólo sumas

## 13. Conexión global: Kruskal y Union-Find
**Pregunta:** ¿Qué consulta repetida de Kruskal justifica usar Union-Find?
Consulta si existe una unión entre los nodos, y une los que estén separados y se puedan unir

## 14. Árbol de caminos mínimos no es MST
**Pregunta:** ¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?
Porque sólo le preocupa conectar dos nodos específicos

## 15. Dependencias: Kahn y grados de entrada
**Pregunta:** ¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?
Que no tiene pendientes y puede agregarse 

## 16. BFS y Kahn comparten cola, no invariante
**Pregunta:** ¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?
El grado de entrada

## 17. Contratos antes de ejecutar
**Pregunta:** ¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?
Validar las entradas

## 18. Reutilización en lugar de recopia
**Pregunta:** ¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?
Porque trabaja de más y no se adapta del todo

## 19. Diseñar pruebas que distinguen decisiones
**Pregunta:** ¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?
Que verifica un caso específico y relevante

## 20. Clínica de selecciones incorrectas
**Pregunta:** Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.

1. “Usaré BFS porque hay que llegar de A a B”, pero las calles tienen tiempos 2 y 9.
- Objetivo. Encontrar la ruta mínima
- Contrato violado. Las aristas deberían pesar igual
- Operación dominante. Revisar la suma del peso de las aristas
- Corrección. Dijkstra

2. “Usaré Dijkstra para conectar todas las sedes”, pero se minimiza el costo total de la red.
- Objetivo. Conectar todo
- Contrato violado. Dijkstra sólo conecta dos nodos
- Operación dominante. Conectar todo
- Corrección. Kurkal

## 21. Trabajo en equipo A: movilidad urbana
**Pregunta:** ¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?

Cambian los algoritmos necesarios
- A1. BST
- A2. BST 0 1
- A3. Kurkal

## 22. Trabajo en equipo B: construir y planificar
**Pregunta:** ¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?

Porque los problemas funcionan diferente


## 23. Comunicación técnica de una decisión
**Pregunta:** ¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?
Razonamiento detrás y estructura y contrato del problema

## 24. Reflexión final del curso
1. “Antes elegía una estructura por comodidad; ahora primero identifico las necesidades del problema.”
2. “El contrato que más me ayudó a detectar un error fue el de no aceptar infinitos o negativos, porque mi código al inicio fallaba por eso.”
3. “Ante un algoritmo que no aplica, ahora puedo revisar otras opciones y cambiarlo.”

**Pregunta:** ¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?
Ahora tengo más opciones e identifico mejor sus ventajas y desventajas para aplicarlo a un conexto específico.

## 25. Síntesis y cierre
**Pregunta:** Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?
Entendiendo el problema