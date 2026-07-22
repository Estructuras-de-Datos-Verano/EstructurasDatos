## 1. Presentación de la clase

**Pregunta.** ¿Qué cambia entre representar un grafo y recorrerlo?

El garfo es diseñar, pero recorrerlo es como hacer el trayecto mediante las aristas.

# 2. Análisis de Problemas CSES: Modelado y Recorrido


## 2.1 Counting Rooms

* **¿Qué representa un nodo?** Cada celda individual que sea transitable, es decir, los espacios de piso marcados con un punto. Las paredes simplemente no son nodos.
* **¿Qué representa una arista?** La posibilidad de moverte de una celda de piso a otra contigua. Es una relación implícita en las 4 direcciones cardinales (arriba, abajo, izquierda, derecha), siempre y cuando la celda vecina también sea piso.
* **¿Qué significa visitar un nodo?** Procesar esa celda de piso específica para marcarla como parte de la habitación actual y, desde ahí, expandirse hacia sus vecinos para descubrir los límites de esa misma habitación.
* **¿Qué información necesito recordar?** Una matriz de visitados del mismo tamaño que el mapa para saber qué celdas ya fueron contadas. 

---

## 2.2 Labyrinth

* **¿Qué representa un nodo?** Al igual que el anterior, cada celda transitable, incluyendo específicamente la celda de inicio A y la de fin B.
* **¿Qué representa una arista?** La conexión directa de paso entre celdas vecinas transitables (arriba, abajo, izquierda, derecha).
* **¿Qué significa visitar un nodo?** Entrar a una celda para verificar si llegamos al destino B. Si no es B, se usa para seguir explorando los caminos adyacentes.
* **¿Qué información necesito recordar?** Una estructura de visitados para no volver atrás ni dar vueltas en círculos. 
---

## 2.3 Message Route

* **¿Qué representa un nodo?** Una computadora individual de la red.
* **¿Qué representa una arista?** Un cable de red bidireccional que conecta directamente a dos computadoras.
* **¿Qué significa visitar un nodo?** Procesar una computadora para revisar su lista de conexiones directas y meter esas computadoras vecinas en la fila de exploración.
* **¿Qué información necesito recordar?** Un arreglo de visitados para no procesar la misma computadora dos veces si hay bucles en la red.

## 3. Recorridos manuales sin nombres

Usaremos este grafo:

```text
A: B, C
B: A, D, E
C: A, F
D: B
E: B
F: C
```

Primero no diremos BFS ni DFS. Solo probaremos dos estrategias.

Responde las tablas siguientes en `notebook.md`.

## 4. Estrategia por niveles

Completa en `notebook.md`:

| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B,C | A | A |
| 2 | C,D,E | A,B | B |
| 3 | D,E,F | A,B,C | C |
| 4 | E,F | A,B,C,D | D |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más antiguo?

Se aparece una cola.

## 5. Estrategia por profundidad

Estrategia: avanzar todo lo posible por una rama y regresar cuando no se pueda continuar.


| Paso | Pendientes | Visitados | Nodo actual |
| --- | --- | --- | --- |
| 0 | A | - | - |
| 1 | B,C | A | A |
| 2 | D,E,C | A,B | B |
| 3 | E,C | A,B,D | D |
| 4 | C | A,B,D,E | E |

**Pregunta.** ¿Qué estructura aparece si siempre atendemos el pendiente más reciente?

Se aparece una pila

## 6. Nacen BFS y DFS

**Pregunta.** Explica con tus palabras por qué BFS usa cola y DFS usa pila.

BFS usa cola porque queremos atender el orden estricto de llegada, así nos aseguramos de visitar a todos los vecinos, va por capas. Mientras que DFS usa pilas porque queremos avanzar y volver por donde vinimos, la pila nos obliga a agarrar lo más reciente.

## 7. Pseudocódigo

**Pregunta.** ¿Qué pasaría si en BFS cambiamos la cola por una pila?

El algoritmo cambia, deja de buscar por capas y empieza a buscar en profundidad.

## 8. Implementación

**Pregunta.** ¿Por qué necesitamos un conjunto de descubiertos o visitados?

Porque es como la memoria o historial del algoritmo.

## 9. Registro paso a paso

**Pregunta.** ¿Qué ventaja tiene registrar la ejecución paso a paso?

Así tenemos una estructura general del algoritmo, y también un tipo de memoria 

## 10. Visualización

**Pregunta.** ¿Qué puede mostrar una animación que una lista de nodos no muestra?

Pues por ejemplo no tenemos el recorrido visual, que puede otrogar más comprensión a la hora de analizar su comportamiento, también es más ameno al mostrar los estados de forma didáctica.

## 11. Diseño de pruebas

**Pregunta.** Diseña dos pruebas propias y explica qué comportamiento verifican.

### Prueba 1: test_grafo_dirigido_camino_unidireccional

Verifica que los algoritmos de recorrido respeten la dirección de las aristas en un grafo dirigido.

### Prueba 2: test_origen_inexistente

Verifica la los errores y que tan fuerte es de las implementaciones ante datos de entrada inválidos. 

## 12. CSES aplicado

1. ¿Cuál algoritmo usarías para Message Route y por qué?

Usaría BFS, porque nos piden encontrar la ruta que use la menor cantidad de computadoras posibles. Como el grafo no tiene pesos (todos los cables de red valen lo mismo), BFS es la mejor opción.

2. ¿Cuál usarías para Counting Rooms?

Usaría DFS, aunque en realidad cualquiera de los dos funciona perfectamente porque aquí no nos importa encontrar un camino corto, sino simplemente marcar todo el territorio de una misma habitación. 

3. ¿Cómo aparecería un recorrido en Labyrinth?

Se comportaría como BFS. Conforme el algoritmo avanza celda por celda en todas direcciones para buscar la salida, cada casilla nueva que descubre es anotada con una flecha apuntando a la casilla de la que vino; en el instante en que esa onda toca el destino final, el algoritmo simplemente deja de explorar y reconstruye el camino caminando hacia atrás, siguiendo esas flechas guardadas hasta regresar al inicio para dibujar la ruta con letras como U, D, L, R.

## 13. Patrón descubierto

**Pregunta.** Explica con tus palabras el patrón de recorrido de grafos.

Es como el plano mental que usas cuando necesitas explorar una red de elementos interconectados sin perderte ni caminar en círculos. Se activa en tu cabeza en tres situaciones clave: cuando necesitas "inundar" o mapear una zona completa (como las habitaciones en Counting Rooms), cuando quieres descubrir si existe una conexión real entre dos puntos lejanos, o cuando te urge calcular la ruta más rápida midiendo el menor número de saltos posibles (como en Message Route). Para que funcione, el patrón nos da las herramientas según lo necesitemos: si buscamos expansión por capas uniformes para encontrar el camino más corto, usas BFS con una cola; pero es necesario explorar de forma obsesiva hasta el fondo de un camino antes de regresar a ver las alternativas, usas DFS con una pila.

## 14. Cierre

1. ¿Qué ganamos al recorrer un grafo?

Obtenemos algo así como una vista en primera persona del comportamiento del grafo 

2. ¿Qué relación hay entre cola y BFS?

BFS necesita explorar la cercanía de los vecino o ir por capas, y una cola para DFS, al atender bajo el principio FIFO, es la única estructura que garantiza que terminemos de revisar por completo el nivel actual antes de que se nos permita avanzar al siguiente.

3. ¿Qué relación hay entre pila y DFS?

DFS busca explorar un camino lo más profundo posible antes de mirar hacia los lados. Una pila, al funcionar bajo el principio LIFO, nos obliga a priorizar siempre el nodo más reciente que acabamos de descubrir.

4. ¿Qué caso te parece más fácil de visualizar?

El BFS

5. ¿Qué pregunta técnica te queda abierta?

¿Es posible algún tipo de combinación que tenga ambas implementaciones?






