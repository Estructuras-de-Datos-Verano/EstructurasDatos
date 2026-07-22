# Notebook
# Nombre: José Iván Reyna Blanco
## 1. Pregunta inicial
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
Identificamos la acción que más se repite para resolver el problema (operación dominante). Con base en esa acción, elegimos la estructura que la hace más rápido, lo que casi en automático nos dice qué algoritmo usar.

## 2. Recuperación
**¿Qué operación repetida justifica cada una de las cinco estructuras mostradas al inicio?**
La cola procesa datos en orden de llegada; el deque permite agregar o quitar rápido por ambos lados. El heap extrae al instante el valor más importante, Union-Find agrupa elementos rápidamente, y los grados de entrada ayudan a ver qué tareas ya están libres.

## 3. Del enunciado a una decisión
**¿Por qué es peligroso elegir un algoritmo únicamente por una palabra clave del enunciado?**
Porque las palabras tienen múltiples significados y te pueden engañar. "Conectar", por ejemplo, puede pedirte una ruta corta, revisar si hay paso, o armar una red completa, requiriendo soluciones totalmente distintas.

## 4. Identificar el objetivo
**¿Qué diferencia observable hay entre la salida de un camino mínimo, un MST y un orden topológico?**
Un camino mínimo te da el paso a paso exacto para ir de un punto a otro. Un MST te da las conexiones necesarias para unir todos los puntos. Un orden topológico te da una lista de tareas organizadas para no atorarte.

## 5. Dirección y significado de las aristas
**¿Qué decisión incorrecta podría producirse si tratamos una dependencia dirigida como una arista no dirigida?**
Alteraríamos la lógica del problema al cambiar quién depende de quién. Una tarea que en realidad necesitaba de otra previa parecería que se puede hacer al revés o al mismo tiempo.

## 6. Clasificar el dominio de pesos
**¿Por qué el dato 'hay pesos' es insuficiente para elegir entre 0-1 BFS y Dijkstra?**
Porque no importa solo que haya un costo, sino qué valores tiene. Si los costos son solo 0 y 1, usas un método muy rápido (0-1 BFS); si hay valores variados, necesitas uno que soporte esa variedad (Dijkstra).

## 7. Matriz de decisión integradora
**¿Qué columna de la matriz explica mejor por qué se eligió una estructura de datos concreta?**
La operación dominante. Esta te dice exactamente cuál es la acción que harás sin parar, obligándote a elegir la estructura que sea más eficiente para realizarla.

## 8. Laboratorio de decisión interactivo
**¿Qué debes predecir antes de revelar el algoritmo y qué evidencia usarás para corregir tu predicción?**
Debes predecir tu objetivo final y qué estructura de datos te ayudará mejor. Para saber si acertaste, revisas si tu idea respeta las reglas de los datos, pasa pruebas engañosas y funciona rápido.

## 9. Caso de caminos sin pesos: BFS
**¿Qué invariante permite afirmar que el primer descubrimiento de un nodo en BFS usa el mínimo número de aristas?**
Que busca avanzando como ondas en el agua por niveles. Al tocar un punto por primera vez, es seguro que llegaste por el camino más directo, pues ya revisaste todas las rutas previas.

## 10. Caso de pesos 0/1: 0-1 BFS
**¿Por qué una mejora de peso 0 entra al frente del deque y una de peso 1 al final?**
Porque los pasos gratuitos (peso 0) se pueden atender de inmediato poniéndolos al inicio de la fila. Los pasos que cuestan (peso 1) se mandan atrás para revisarlos después.

## 11. Caso de pesos generales: Dijkstra
**¿Qué operación repetida hace que un heap sea adecuado para Dijkstra?**
La necesidad constante de encontrar la opción más barata entre todas las disponibles. Un heap es ideal porque siempre mantiene el elemento más pequeño listo para usarse.

## 12. BFS, 0-1 BFS y Dijkstra no forman una competencia
**¿En qué sentido Dijkstra puede ser correcto pero no la elección más adecuada para pesos 0/1?**
Dijkstra dará la respuesta correcta, pero es un método demasiado pesado para algo tan simple. 0-1 BFS es la herramienta especializada que resolverá lo mismo muchísimo más rápido.

## 13. Pesos negativos: rechazar con precisión
**¿Cómo justificarías técnicamente la respuesta 'ninguno de los estudiados' ante pesos negativos?**
Estos algoritmos asumen que avanzar siempre suma costo. Si un camino te "devuelve dinero" (costo negativo), sus reglas fallan, se confunden y dan resultados incorrectos.

## 14. Conexión global: Kruskal y Union-Find
**¿Qué consulta repetida de Kruskal justifica usar Union-Find?**
La necesidad de preguntar constantemente si dos puntos ya están conectados por otro lado. Union-Find responde esto rapidísimo, evitando que formes ciclos inútiles.

## 15. Árbol de caminos mínimos no es MST
**¿Por qué un árbol de predecesores producido por Dijkstra no tiene que minimizar el costo total de todas sus aristas?**
Porque Dijkstra busca el viaje más rápido para un individuo desde un punto inicial, sin importarle el costo global. Un MST (Kruskal) busca conectar a todos gastando lo mínimo en total, aunque algunos viajes individuales tarden más.

## 16. Dependencias: Kahn y grados de entrada
**¿Qué significa que un nodo tenga grado de entrada cero durante Kahn?**
Significa que a esa tarea ya no le falta ningún requisito previo. Está completamente libre y lista para que empieces a trabajar en ella.

## 17. BFS y Kahn comparten cola, no invariante
**¿Qué información adicional a la cola permite distinguir una ejecución de BFS de una de Kahn?**
La información que guardan para organizarse. BFS anota a qué distancia está un punto descubierto, mientras que Kahn anota cuántos requisitos previos le siguen faltando a una tarea.

## 18. Contratos antes de ejecutar
**¿Qué responsabilidades conserva el código integrador aunque reutilice una implementación ya probada?**
Tu deber es entregarle la información correcta al código (por ejemplo, validar que no haya costos negativos). También eres responsable de saber interpretar la respuesta que te devuelva.

## 19. Reutilización en lugar de recopia
**¿Por qué copiar una implementación previa es peor que importarla y adaptar únicamente la entrada y salida?**
Porque si copias y pegas el mismo código muchas veces, corregir un error significa buscarlo en mil lugares distintos. Es mejor tener un solo código central e invocarlo cuando lo necesites.

## 20. Diseñar pruebas que distinguen decisiones
**¿Qué hace que una prueba sea distintiva y no solo un caso de ejemplo?**
Que está diseñada con "trampa" para hacer fallar a las soluciones incorrectas. No solo confirma que tu idea sirve, sino que demuestra por qué otras opciones fallarían.

## 21. Clínica de selecciones incorrectas
**Elige dos propuestas incorrectas y explica objetivo, contrato violado, operación dominante y corrección.**
No puedes usar BFS normal si las calles tienen diferentes tiempos; necesitas Dijkstra para sacar el costo mínimo. Tampoco uses Kahn para buscar rutas en mapas; ese sirve para organizar prerrequisitos de proyectos.

## 22. Trabajo en equipo A: movilidad urbana
**¿Cómo cambian estructura y algoritmo entre A1, A2 y A3 aunque el objetivo general siga siendo llegar con costo mínimo?**
Cambian según los costos: si todas las calles miden igual, usas fila simple (BFS); si hay atajos gratis y calles normales, fila doble (0-1 BFS); y si hay tiempos variados, un Heap (Dijkstra).

## 23. Trabajo en equipo B: construir y planificar
**¿Por qué reutilizar los mismos nodos no permite reutilizar automáticamente el mismo algoritmo en las dos necesidades?**
Porque los puntos y conexiones significan cosas distintas en cada problema. Construir tuberías es unir lugares (Kruskal/MST), pero planificar permisos es seguir un orden de reglas (Kahn/Orden topológico).

## 24. Comunicación técnica de una decisión
**¿Qué elementos mínimos debe contener una justificación técnica para que otra persona pueda auditar la elección?**
Debes explicar claramente tu objetivo, cómo son los costos y direcciones, y qué acción se repetirá más. Luego, justificas qué estructura hace eso más rápido y por qué descartaste las otras.

## 25. Reflexión final del curso
**¿Qué cambió en tu proceso de decisión desde la primera clase hasta este laboratorio final?**
Ahora me enfoco en entender qué pide realmente el problema y su acción principal. Ya no elijo el código más fácil de escribir, sino el que cumple mejor con las reglas del escenario.

## Síntesis y cierre
**Ante un problema nuevo, ¿cómo identificamos la operación dominante y elegimos la estructura de datos y el algoritmo adecuados?**
Primero defines si buscas una ruta, conectar todo o un orden. Analizas las reglas para saber qué acción se repetirá más, y eliges la estructura que la haga más rápido, llevándote al algoritmo correcto.