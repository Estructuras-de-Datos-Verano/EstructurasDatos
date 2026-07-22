# Notebook Aristeo.
## 1. Presentación de la clase
### ¿Qué cambia entre representar un grafo y recorrerlo?
Representar = estructura estática: nodos, aristas, (posibles pesos). Recorrer = proceso dinámico: orden de visitas, estados temporales (pendientes, visitados), objetivo (buscar, contar, medir distancia).
## 2. Problemas CSES
### [CountingRooms]
### 1. ¿Qué representa un nodo?
Una casilla libre del mapa (una posición que podemos visitar).
### 2. ¿Qué representa una arista?
Una conexión entre casillas adyacentes que permite moverse (no es un muro).
### 3. ¿Qué significa visitar un nodo?
Entrar en esa casilla, marcarla como descubierta y procesar sus vecinos.
### 4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Un conjunto o matriz de visitados (booleanos) para evitar revisitas y poder contar componentes.

---
### [Labyrinth]
### 1. ¿Qué representa un nodo?
Una casilla (posición) del laberinto.
### 2. ¿Qué representa una arista?
Un paso válido entre casillas contiguas (sin muro).
### 3. ¿Qué significa visitar un nodo?
Llegar a esa casilla, marcarla y explorar las salidas disponibles.
### 4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
Visitados, y si buscamos ruta mínima: distancia y predecesor por nodo.

---
### [MessageRoute]
### 1. ¿Qué representa un nodo?
Una persona/ciudad/entidad de la red (un vértice del grafo).
### 2. ¿Qué representa una arista?
Una conexión directa donde se puede transmitir un mensaje.
### 3. ¿Qué significa visitar un nodo?
Procesar ese nodo en la propagación del mensaje y considerar sus vecinos.
### 4. ¿Qué información necesito recordar para no visitar lo mismo muchas veces?
- visitados para no repropagar 
- predecesor para reconstruir ruta 
- distancia si interesa la longitud mínima.

---
## 4. Estrategia por niveles

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | C, D | A, B | B |
| 3 | D, E | A, B, C | C |
| 4 | E | A, B, C, D | D |

### ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?
Responde una estructura FIFO: una cola (BFS), que procesa por niveles según distancia desde el origen.
## 5. Estrategia por profundidad

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | C, B | A | A |
| 2 | E, B | A, C | C |
| 3 | B | A, C, E | E |
| 4 | D | A, C, E, B | B |

### ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?
Responde una estructura LIFO: una pila (DFS), que profundiza en una rama antes de retroceder. En la tabla de ejemplo se ha usado el orden de vecinos [B,C] al expandir `A`, lo que provoca visitar `C` antes que `B` debido al comportamiento LIFO.
## 6. Nacen BFS y DFS
### Explica con tus palabras por qué BFS usa cola y DFS usa pila.
BFS usa cola porque queremos procesar nodos en orden de descubrimiento (por niveles), garantizando distancia mínima en grafos no ponderados. DFS usa pila (implícita con recursión) porque se explora un camino hasta el fondo antes de retroceder, lo que sigue un orden LIFO.
## 7. Pseudocódigo
### ¿Qué pasaría si en BFS cambiamos la cola por una pila?
Si cambias la cola por una pila, el orden de visita cambia y el algoritmo se transforma en DFS; pierdes la propiedad de que las distancias sean mínimas en número de aristas.
## 8. Implementación
### ¿Por qué necesitamos un conjunto de descubiertos o visitados?
Porque evita ciclos infinitos y revisitas, garantiza que cada nodo se procese una sola vez (eficiencia) y permite contar componentes o reconstruir rutas correctamente.
## 9. Registro paso a paso
### ¿Qué ventaja tiene registrar la ejecución paso a paso?
Registrar la ejecución paso a paso permite depurar y entender exactamente cómo evoluciona el algoritmo: muestra la frontera (cola/pila) en cada paso, qué aristas se exploran, el orden de visitas y los retrocesos. Esto facilita la visualización, la enseñanza, la reproducción de ejecuciones concretas para pruebas y la generación de animaciones que expliquen el comportamiento.

Ejemplo: las funciones `registrar_bfs` y `registrar_dfs` generan una lista de estados con campos `paso`, `nodo_actual`, `cola_o_pila`, `visitados`, `descubiertos`, `aristas_exploradas` y `linea_pseudocodigo`.
## 10. Visualización
### ¿Qué puede mostrar una animación que una lista de nodos no muestra?
Una animación puede mostrar el orden temporal de visitas, expansión de la frontera (niveles en BFS), retrocesos en DFS y cómo evoluciona la cola/pila en el tiempo.
## 11. Diseño de pruebas
### Diseña dos pruebas propias y explica qué comportamiento verifican.
Prueba 1 — Grafo con ciclo: verifica que `visitados` evita bucles y que todos los nodos alcanzables se visitan exactamente una vez.
Prueba 2 — Grafo desconectado / laberinto con dos componentes: verifica que el flood-fill cuenta correctamente componentes y no cruza entre ellas.
## 12. CSES aplicado
### 1. ¿Cuál algoritmo usarías para Message Route y por qué?
Message Route: BFS — grafo no ponderado, BFS encuentra ruta mínima en número de aristas; usar `predecesor` para reconstruir ruta.
### 2. ¿Cuál usarías para Counting Rooms?
Counting Rooms: DFS o BFS (flood-fill) — ambos cuentan componentes; DFS recursivo suele ser sencillo.
### 3. ¿Cómo aparecería un recorrido en Labyrinth?
Labyrinth: para ruta mínima usar BFS (aparecerá como anillos concéntricos desde la fuente). Para exploración completa cualquiera sirve; DFS mostrará trazas profundas con retrocesos.
## 13. Patrón descubierto
### Explica con tus palabras el patrón de recorrido de grafos.
El patrón de recorrido de grafos trata de explorar vértices conectados siguiendo una estrategia sistemática para responder preguntas de conectividad, alcance y distancia.

Cuándo se activa:
- ¿Tengo que visitar nodos conectados? → usar flood-fill (BFS o DFS).
- ¿Quiero saber si puedo llegar? → basta con buscar hasta encontrar el destino (BFS/DFS).
- ¿Quiero distancia mínima en número de aristas? → usar BFS en grafos no ponderados.

Componentes del patrón:
- Estado visitados para evitar revisitas y ciclos.
- Estructura de frontera: cola (FIFO) para BFS, pila (LIFO) para DFS.
- Opcional: distancia o predecesor para reconstruir rutas o medir longitud.

Cómo se usa (resumen):
- Inicializas el origen, marcas como descubierto y pones sus vecinos en la frontera.
- Procesas elementos de la frontera según la estructura elegida (cola/pila), marcando nuevos descubrimientos y registrando información útil (distancia/predecesor).
- Terminas cuando la frontera se vacía o se cumple la condición de parada (p. ej. encontrar el objetivo).

Notas prácticas:
- BFS garantiza rutas mínimas en número de aristas; DFS es útil para exploración completa, detección de ciclos y backtracking.
- El orden en que se visitan los vecinos afecta el recorrido (útil para control determinista en pruebas/visualizaciones).
## 14. Cierre
### 1. ¿Qué ganamos al recorrer un grafo?
Descubrimos conectividad, rutas, distancias y estructura (componentes, ciclos).
### 2. ¿Qué relación hay entre cola y BFS?
La cola mantiene orden por niveles en BFS → garantiza distancias mínimas en grafos no ponderados.
### 3. ¿Qué relación hay entre pila y DFS?
La pila hace que la exploración profundice (LIFO) → útil para backtracking y detección de ciclos.
### 4. ¿Qué caso te parece más fácil de visualizar?
BFS suele ser más fácil de visualizar (crecimiento por niveles).
### 5. ¿Qué pregunta técnica te queda abierta?
Pregunta técnica abierta típica: ¿qué pasa si las aristas tienen pesos? (usar Dijkstra/A* en lugar de BFS).

