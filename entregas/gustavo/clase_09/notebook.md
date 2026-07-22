# Notebook - Clase 09

## 1. Presentación de la clase 

¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?

Una secuencia es como una fila: un elemento va detrás de otro en un orden fijo (como una lista de compras). En cambio, al modelar relaciones con grafos, es como dibujar un mapa o una red de amigos: cualquier elemento puede estar conectado con uno, con varios o con ninguno al mismo tiempo, sin seguir una línea recta.

## 2. Problemas motivadores CSES

1. ¿Qué representa un nodo?
2. ¿Qué representa una arista?
3. ¿Es dirigido?
4. ¿Es ponderado?
5. ¿Qué pregunta algorítmica aparece?

* **Building Roads:**
  1. **Nodo:** Una ciudad.
  2. **Arista:** Una carretera de doble sentido entre dos ciudades.
  3. **Dirigido:** No.
  4. **Ponderado:** No (solo importa si están conectadas o no).
  5. **Pregunta algorítmica:** ¿Cuántas carreteras nuevas necesito construir para que todas las ciudades queden conectadas entre sí?

* **Counting Rooms:**
  1. **Nodo:** Una casilla de piso (`.`) por donde se puede caminar.
  2. **Arista:** El paso hacia una casilla vecina (arriba, abajo, izquierda o derecha).
  3. **Dirigido:** No.
  4. **Ponderado:** No.
  5. **Pregunta algorítmica:** ¿Cuántas habitaciones separadas por paredes hay en total en el mapa?

* **Labyrinth:**
  1. **Nodo:** Una casilla por donde se puede caminar (piso `.`, inicio `A` o salida `B`).
  2. **Arista:** Un paso válido hacia una casilla adyacente.
  3. **Dirigido:** No.
  4. **Ponderado:** No (cada paso cuenta como 1 movimiento).
  5. **Pregunta algorítmica:** ¿Cuál es el camino más corto para llegar desde `A` hasta `B` y qué pasos debo dar?

* **Message Route:**
  1. **Nodo:** Una computadora.
  2. **Arista:** Un cable o conexión directa entre dos computadoras.
  3. **Dirigido:** No.
  4. **Ponderado:** No.
  5. **Pregunta algorítmica:** ¿Cuál es la ruta que pasa por la menor cantidad de computadoras para enviar un mensaje desde la computadora 1 hasta la última?

## 3. Modelado de relaciones

| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudad | Carretera entre dos ciudades | No | No | ¿Cuántas carreteras faltan para conectar todas las ciudades? |
| Counting Rooms | Casilla de piso (`.`) | Paso a una casilla vecina | No | No | ¿Cuántas habitaciones (grupos separados) hay en el mapa? |
| Labyrinth | Casilla transitable | Paso a una casilla adyacente | No | No | ¿Cuál es el camino más corto de A hasta B? |
| Message Route | Computadora | Conexión de red directa | No | No | ¿Cuál es la ruta más rápida (menos saltos) de la PC 1 a la N? |

## 4. Conceptos básicos de grafos

Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.

* **Mi ejemplo de grafo dirigido:** Los prerrequisitos de las materias en la universidad. Si para tomar *Cálculo II* primero debo pasar *Cálculo I*, la flecha va en un solo sentido. No puedo hacerlo al revés.
* **Mi ejemplo de grafo no dirigido:** Los amigos en Facebook. Si yo te agrego y aceptas, automáticamente somos amigos mutuamente; la conexión va en ambos sentidos por igual.

## 5. Representaciones

¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?

Para mí, lo más importante es **listar vecinos**. 

La razón es simple: para recorrer un mapa, un laberinto o una red (que es lo que hacen casi todos los algoritmos como BFS o DFS), lo primero que necesitas saber en cada paso es: *"¿A qué lugares puedo moverme desde donde estoy parado ahora mismo?"*. Si esa operación es lenta, todo el programa será lento.

## 6. Interfaz común

¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?

Porque así puedo cambiar la forma en que guardo el grafo por dentro (pasar de lista a matriz o viceversa) sin tener que reescribir el resto de mi código. Es como cambiarle el motor a un auto pero mantener el mismo volante y los mismos pedales: se conduce exactamente igual por fuera.

## 7. Implementaciones

¿Por qué un `set` ayuda a evitar aristas duplicadas?

Porque los *sets* (conjuntos) en Python eliminan los elementos repetidos de forma automática. Si intento agregar la conexión `"A" -> "B"` dos veces, el *set* simplemente ignora la segunda repetición. Eso me ahorra tener que escribir un `if` para revisar si la conexión ya existía.

¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?

La matriz tiene que hacerse más grande. Si tengo 3 nodos y agrego uno nuevo, la matriz pasa de ser una tabla de 3x3 a una de 4x4. Para lograrlo:
1. Le agrego una columna extra llena de `False` al final de cada fila existente.
2. Agrego una fila completamente nueva llena de `False` hasta el fondo.

## 8. Comparación

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Ocupa poco espacio (solo guarda las conexiones reales). | Ocupa mucho espacio (guarda una tabla gigante, llena de `False`). |
| Facilidad de implementación | Muy fácil usando diccionarios y *sets* en Python. | Regular (hay que manejar índices numéricos y redimensionar tablas). |
| Consultar vecinos | Súper rápido (ya están agrupados en una lista o *set*). | Lento (hay que revisar toda la fila casilla por casilla). |
| Consultar si existe arista | Rápido gracias a la búsqueda en el *set*. | Instantáneo (revisas directo la fila y columna). |
| Grafos dispersos | **La mejor opción.** Ahorra muchísima memoria y es rápida. | **Mala opción.** Desperdicia espacio guardando conexiones que no existen. |
| Grafos densos | Buena opción, funciona bastante bien. | **La mejor opción.** Aprovecha súper bien el espacio y es ultra directa. |

## 9. Visualización con NetworkX--

¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?

Porque me permite juntar lo mejor de dos mundos. Por un lado, hago mi propio código para aprender y entender cómo funciona un grafo por dentro. Por otro lado, al exportarlo a NetworkX, puedo usar herramientas profesionales ya listas para hacer dibujos geniales o cálculos complejos en segundos, sin tener que programar todo desde cero.

## 10. Diseño de pruebas

Diseña al menos dos pruebas propias y explica qué comportamiento verifican.

1. **Prueba de doble sentido (`test_simetria`):**
   * **Qué verifica:** Que al conectar A con B en un grafo no dirigido, el sistema recuerde automáticamente conectar B con A.
   * **Cómo lo pruebo:** Agrego una arista entre "A" y "B". Luego reviso con un `assert` que "B" aparezca en la lista de vecinos de "A", y que "A" también aparezca en la lista de vecinos de "B".

2. **Prueba contra repetidos (`test_sin_duplicados`):**
   * **Qué verifica:** Que el grafo no cuente conexiones repetidas si las agrego por error varias veces.
   * **Cómo lo pruebo:** Conecto "X" con "Y" tres veces seguidas en mi código. Luego reviso con un `assert` que la cantidad total de aristas siga siendo solo 1.

## 11. Patrón descubierto

Explica con tus palabras el patrón de modelado de relaciones.

Es una técnica para resolver problemas que consiste en transformar cualquier situación de la vida real en "puntos y líneas".
* Los **puntos (nodos)** son las cosas que me interesan (ciudades, personas, casillas).
* Las **líneas (aristas)** son las reglas o caminos que conectan esas cosas.

Cuando logras ver un problema como puntos y líneas, deja de ser un problema confuso y se convierte en un mapa fácil de resolver usando recetas clásicas (como encontrar el camino más corto).

## 12. Cierre

1. ¿Qué ganamos al modelar relaciones como grafo?
Ganamos orden. Podemos usar algoritmos famosos que ya están probados para resolver problemas complejos muy rápido, en vez de tratar de inventar una solución complicada desde cero.

2. ¿Cuándo usarías lista de adyacencia?
Casi siempre. Es ideal para mapas, redes sociales o laberintos, porque normalmente las cosas están conectadas con pocos vecinos (un mapa tiene pocas calles saliendo de cada esquina) y ahorra mucha memoria.

3. ¿Cuándo usarías matriz de adyacencia?
Solo cuando el grafo es muy pequeño (por ejemplo, menos de 1000 nodos) y además casi todos los nodos están conectados contra todos.

4. ¿Qué puede ocultar una visualización?
Un dibujo puede engañar. A veces, para que el gráfico se vea bonito en pantalla, el programa junta dos nodos y hace parecer que están muy conectados o cercanos, cuando en realidad matemáticamente están lejos. También, si hay muchos puntos, se vuelve un "nido de pájaros" ilegible.

5. ¿Qué algoritmo necesitaremos para recorrer el grafo?
Necesitaremos principalmente dos:
* **BFS (Búsqueda en Anchura):** Explora por capas (como ondas en el agua) y es perfecto para encontrar el camino más corto.
* **DFS (Búsqueda en Profundidad):** Explora un camino hasta el final antes de regresar; sirve mucho para ver si todo el mapa está conectado o encontrar grupos aislados.