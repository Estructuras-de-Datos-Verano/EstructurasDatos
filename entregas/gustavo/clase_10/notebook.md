# Notebook - Clase 10

## 1. Presentación de la clase

**¿Qué cambia entre representar un grafo y recorrerlo?**
Representar un grafo es simplemente modelar las relaciones o conexiones entre las cosas. Por otro lado, recorrerlo significa que me pongo a visitar esos nodos viajando por sus conexiones (aristas) mientras voy recordando por dónde ya pasé, para no perderme ni dar vueltas en círculos.

---

## 2. Problemas CSES

1. **¿Qué representa un nodo?** Representa una ubicación específica, como una casilla de un tablero, una habitación en un cuarto o una persona en la red.
2. **¿Qué representa una arista?** Es el pasillo, la puerta o el enlace que me permite moverme de una ubicación a otra.
3. **¿Qué significa visitar un nodo?** Significa llegar físicamente a esa posición en mi exploración y tomar nota de sus caminos disponibles.
4. **¿Qué información necesito recordar para no visitar lo mismo muchas veces?** Necesito llevar un registro de los lugares donde ya estuve (un historial) para no volver a entrar ahí y quedarme atrapado en un ciclo infinito.

---

## 3. Recorridos manuales sin nombres

*(Las respuestas de los recorridos se encuentran en las siguientes secciones)*

---

## 4. Estrategia por niveles

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | C, D, E | A, B | B |
| 3 | D, E, F | A, B, C | C |
| 4 | E, F | A, B, C, D | D |

**¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?**
Aparece una **cola** o fila, donde el primero en llegar es el primero que atiendo.

---

## 5. Estrategia por profundidad

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B, C | A | A |
| 2 | B, F | A, C | C |
| 3 | B | A, C, F | F |
| 4 | D, E | A, C, F, B | B |

**¿Qué estructura aparece si siempre atendemos el pendiente más reciente?**
Aparece una **pila**, similar a una pila de platos, donde el último que puse es el primero que quito para continuar mi camino.

---

## 6. Nacen BFS y DFS

**¿Por qué BFS usa cola y DFS usa pila?**
* **BFS usa cola** porque explora por niveles o a lo ancho. Si quiero revisar primero a todos mis vecinos inmediatos antes de ir más lejos, necesito ponerlos en una fila para no olvidarme de ninguno de ellos.
* **DFS usa pila** porque su meta es irse a lo más profundo por una sola ruta. Al usar una pila, siempre atiende la ubicación más nueva que acaba de descubrir, lo que lo obliga a seguir bajando por esa misma rama hasta que ya no puede más.

---

## 7. Pseudocódigo

**¿Qué pasaría si en BFS cambiamos la cola por una pila?**
Si leo el pseudocódigo del BFS y simplemente reemplazo la herramienta de la cola por una pila, automáticamente lo transformo en el algoritmo DFS. Al sacar las cosas desde arriba de la pila, empezaría a explorar a lo profundo en lugar de irme por niveles.

---

## 8. Implementación

**¿Por qué necesitamos un conjunto de descubiertos o visitados?**
Lo necesito para no trabajar de más ni quedarme atascado infinitamente si el mapa tiene ciclos cerrados. Es como dejar migajas de pan para decir "por aquí ya pasé, ignoremos esta puerta".

---

## 9. Registro paso a paso

**¿Qué ventaja tiene registrar la ejecución paso a paso?**
Me permite separar la lógica del algoritmo de lo que quiero dibujar después. Al guardar el estado actual de la cola o la pila, el nodo actual y las aristas por cada pasito, puedo analizar lentamente qué está pensando el programa sin que todo suceda de golpe.

---

## 10. Visualización

**¿Qué puede mostrar una animación que una lista de nodos no muestra?**
Una simple lista solo me da el resultado final. En cambio, con la animación, y manteniendo las posiciones fijas, puedo ver la vida del algoritmo: veo en colores los nodos que todavía están pendientes en la fila y distingo al instante por dónde se está esparciendo el recorrido de forma visual.

---

## 11. Diseño de pruebas

**Diseña dos pruebas propias y explica qué comportamiento verifican:**
1. **Prueba de un nodo aislado:** Probaría con un pequeño grafo de un solo lugar, como `{"A": []}`. Esto verifica que mi código no falle si arranco en un punto que no tiene vecinos. El resultado solo debería ser `["A"]`.
2. **Prueba para no visitar repetidos:** Usaría un mapa que forma un círculo cerrado. Para verificar el comportamiento, revisaría que el tamaño de mi recorrido total sea igual al tamaño del recorrido si le quito los duplicados usando un conjunto. Esto me asegura de que no pasé por la misma habitación dos veces.

---

## 12. CSES aplicado

1. **¿Cuál algoritmo usarías para Message Route y por qué?**
   Usaría **BFS**. Como quiero mandar un mensaje por la menor cantidad de personas, necesito asegurar el camino más corto en cantidad de pasos.
2. **¿Cuál usarías para Counting Rooms?**
   Usaría **DFS**. Aquí solo me interesa recorrer toda la mancha del cuarto para contarla como una sola unidad; no me importa encontrar el camino más rápido.
3. **¿Cómo aparecería un recorrido en Labyrinth?**
   Si uso BFS para buscar la salida, el recorrido se vería como anillos de agua expandiéndose uniformemente en el mapa desde mi punto de inicio, revisando paso a pasito todas las rutas posibles.

---

## 13. Patrón descubierto

**Explica con tus palabras el patrón de recorrido de grafos.**
Para mí, es una herramienta general para resolver cualquier situación donde haya elementos conectados que quiero explorar. Básicamente es agarrar mi mapa, definir un punto de inicio, y decidir mi estilo de explorar (con una cola para barrer poco a poco, o con una pila para hundirme hasta el fondo), anotando siempre por dónde he pisado para no perderme.

---

## 14. Cierre

1. **¿Qué ganamos al recorrer un grafo?** Ganamos la capacidad de resolver problemas de navegación reales: encontrar cosas, ver si dos puntos están conectados o simplemente descubrir el mapa completo.
2. **¿Qué relación hay entre cola y BFS?** La cola es el motor de BFS: hace que los vecinos viejos tengan prioridad, logrando esa búsqueda en forma de ondas.
3. **¿Qué relación hay entre pila y DFS?** La pila es el motor del DFS: al atender siempre lo más nuevo, obliga a la búsqueda a seguir una sola línea hacia lo profundo.
4. **¿Qué caso te parece más fácil de visualizar?** Me parece más fácil visualizar el BFS. Me resulta muy natural imaginar una mancha que crece nivel a nivel hacia todos lados al mismo tiempo.
5. **¿Qué pregunta técnica te queda abierta?** Ya que aquí no usamos caminos ponderados, me queda la duda de qué tendría que cambiarle a la cola o al código para encontrar la ruta más rápida si un pasillo mide 5 metros y otro mide 100 metros.