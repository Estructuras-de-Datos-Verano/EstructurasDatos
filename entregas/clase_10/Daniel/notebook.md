# Notebook - Clase 10: Recorridos de grafos, BFS y DFS

Este documento contiene las respuestas breves a los desafíos y preguntas planteados en la clase.

---

## 1. Presentación de la clase
> **Pregunta:** ¿Qué cambia entre representar un grafo y recorrerlo?

* **Representar:** Es la foto estática en memoria; cómo guardas los nodos y sus uniones (por ejemplo, un diccionario de listas).
* **Recorrer:** Es la película en movimiento; la estrategia activa para caminar por esas uniones sin perderte ni repetir caminos.

---

## 2. Problemas CSES
Respuestas breves para los problemas de motivación:

### Counting Rooms (Contar habitaciones)
1. **¿Qué representa un nodo?** Una celda transitable del mapa (`.`).
2. **¿Qué representa una arista?** La conexión física para moverte arriba, abajo, izquierda o derecha entre celdas transitables.
3. **¿Qué significa visitar un nodo?** Marcar esa celda como "procesada" para que forme parte de una habitación ya contada.
4. **¿Qué información necesito recordar?** Qué celdas ya visité para no volver a contar la misma habitación de forma infinita.

### Labyrinth (Laberinto)
1. **¿Qué representa un nodo?** Cualquier celda libre del suelo, incluyendo la salida y la meta.
2. **¿Qué representa una arista?** Un paso válido en las 4 direcciones cardinales.
3. **¿Qué significa visitar un nodo?** Pisar la celda y chequear si es la salida que buscabas.
4. **¿Qué información necesito recordar?** Los nodos ya visitados y **de dónde vine** (el nodo padre) para reconstruir el camino al final.

### Message Route (Ruta de mensajes)
1. **¿Qué representa un nodo?** Una computadora de la red.
2. **¿Qué representa una arista?** Un cable de red directo entre dos computadoras.
3. **¿Qué significa visitar un nodo?** Revisar esa computadora para ver si es el destino final del mensaje.
4. **¿Qué información necesito recordar?** Las computadoras ya revisadas y la ruta de servidores previa para no dar vueltas en círculos.

---

## 4. Estrategia por niveles
> **Pregunta:** ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?

Aparece una **Cola (Queue)**. Funciona bajo la regla FIFO (*Primero en entrar, primero en salir*). Al procesar lo más viejo primero, obligas al algoritmo a explorar como una onda expansiva, nivel por nivel.

---

## 5. Estrategia por profundidad
> **Pregunta:** ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?

Aparece una **Pila (Stack)**. Funciona bajo la regla LIFO (*Último en entrar, primero en salir*). Al elegir lo más nuevo, el algoritmo se obsesiona con ir al fondo de un camino y solo retrocede si se topa con una pared.

---

## 6. Nacen BFS y DFS
> **Pregunta:** Explica con tus palabras por qué BFS usa cola y DFS usa pila.

* **BFS usa cola** porque busca de manera ordenada y circular; mete a los vecinos al fondo de la fila para terminar de revisar el nivel actual antes de avanzar.
* **DFS usa pila** porque prefiere la aventura vertical; tira un hilo hacia lo profundo y al usar el último nodo agregado, sigue bajando por la misma rama hasta el límite.

---

## 7. Pseudocódigo
> **Pregunta:** ¿Qué pasaría si en BFS cambiamos la cola por una pila?

El algoritmo **deja de ser un BFS y se convierte automáticamente en un DFS**. Al alterar el orden de salida, la búsqueda dejará de ser radial por niveles y pasará a profundizar en ramas verticales instantáneamente.

---

## 8. Implementación
> **Pregunta:** ¿Por qué necesitamos un conjunto de descubiertos o visitados?

Es tu red de seguridad para **evitar bucles infinitos**. Si un grafo tiene ciclos (como una red donde `A` conecta a `B` y `B` a `A`), sin este conjunto te quedarías saltando entre ellos para siempre hasta agotar la memoria.

---

## 9. Registro paso a paso
> **Pregunta:** ¿Qué ventaja tiene registrar la ejecución paso a paso?

Separa la lógica del algoritmo de la interfaz visual. Te permite guardar la "historia" de la ejecución (por ejemplo en un JSON) para poder analizar los errores con calma o crear animaciones fluidas sin mezclar código.

---

## 10. Visualización
> **Pregunta:** ¿Qué puede mostrar una animación que una lista de nodos no muestra?

Muestra el comportamiento en el tiempo: el "ritmo" del algoritmo. Te permite ver el frente de expansión circular de BFS o el camino nervioso que abre DFS y cómo retrocede cuando se encierra.

---

## 11. Diseño de pruebas
> **Pregunta:** Diseña dos pruebas propias y explica qué comportamiento verifican.

* **Prueba 1: `test_lineal_puro`** (Un camino recto como `1 -> 2 -> 3`). Verifica que tanto BFS como DFS devuelvan exactamente el mismo orden cuando no existen bifurcaciones.
* **Prueba 2: `test_nodo_aislado`** (Nodos que no tienen conexiones). Verifica que el algoritmo inicie en el origen, termine de inmediato y no falle ni se rompa al procesar listas vacías.

---

## 13. Patrón descubierto
> **Pregunta:** Explica con tus palabras el patrón de recorrido de grafos.

Es la estrategia estándar para resolver problemas de conectividad ("¿puedo llegar de aquí a allá?") y optimización. Se basa en usar una estructura para agendar el futuro (pila o cola) y otra para recordar el pasado (visitados), logrando explorar cualquier red de forma segura.

---

## 14. Cierre
1. **¿Qué ganamos al recorrer un grafo?** La capacidad de buscar rutas óptimas, rastrear conexiones y resolver problemas complejos de mapas o redes de forma automatizada.
2. **¿Qué relación hay entre cola y BFS?** La cola asegura un trato justo por orden de llegada; eso genera que explores de forma concéntrica o por niveles cercanos.
3. **¿Qué relación hay entre pila y DFS?** La pila prioriza la última opción descubierta, lo que te empuja a explorar a fondo una sola rama antes de mirar al lado.
4. **¿Qué caso te parece más fácil de visualizar?** El BFS, porque se asemeja mucho a cómo se expande una onda de agua al tirar una piedra en un estanque.
5. **¿Qué pregunta técnica te queda abierta?** ¿Cómo cambia el rendimiento de memoria de estos dos algoritmos cuando el grafo es gigantesco o infinito (como las jugadas posibles en el ajedrez)?



