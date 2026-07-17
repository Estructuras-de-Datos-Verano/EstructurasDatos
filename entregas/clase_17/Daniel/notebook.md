
### Pregunta Inicial: Prioridades y Estructuras Auxiliares
* **Pregunta:** ¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?
* **Respuesta:** Si todas las tareas urgen por igual, una **cola simple (FIFO)** es la herramienta ideal, ya que procesa en estricto orden de llegada. En el momento en que se introducen dos prioridades (aristas de peso 0 y 1), necesitamos una **deque (cola de doble extremo)** para poder insertar elementos por ambos lados según su urgencia. Si tuviéramos prioridades generales, ya tendríamos que dar el salto a un heap.




### 1. Presentación de la Clase
* **Pregunta:** ¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades?
* **Respuesta:** Cambia la forma en que gestionamos la cola de pendientes. En vez de simplemente añadir todo al final del camino, ahora debemos decidir en tiempo real si el nodo recién descubierto merece ser atendido de inmediato (peso 0) o si debe esperar su turno al final de la fila (peso 1).

### 2. El Problema Inicial con `pop(0)`
* **Pregunta:** ¿Qué trabajo repetido introduce `pop(0)` y por qué una referencia al frente lo evita?
* **Respuesta:** En Python, usar `pop(0)` sobre una lista estándar obliga al sistema a desplazar todos los elementos restantes un espacio hacia la izquierda para rellenar el hueco, lo cual cuesta un tiempo de $O(n)$. Al usar un puntero directo al frente en nuestra propia lista ligada, simplemente movemos ese puntero al siguiente nodo en $O(1)$ sin molestar al resto de la estructura.

### 3. Nodo y Referencias
* **Pregunta:** ¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos?
* **Respuesta:** 
  * **Valor:** Es la información útil que guardamos (por ejemplo, el nombre de un vértice `"A"`).
  * **Nodo:** Es la "cajita" física que envuelve ese valor y que además contiene las flechas (referencias como `siguiente` o `anterior`) para conectarse con otras cajitas.
  * **Estructura contenedora:** Es la lógica de control (como `ColaLigada`) que impone las reglas de juego: decide por dónde se entra, por dónde se sale, y se asegura de actualizar los punteros y el tamaño.

### 4. Lista Ligada Simple
* **Pregunta:** ¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?
* **Respuesta:** Insertar un nodo al final (operación `encolar`) se volvería sumamente lenta. Al no tener una referencia directa al final de la lista, tendríamos que viajar nodo por nodo desde el inicio hasta el último elemento para poder enganchar el nuevo nodo, lo que arruinaría el rendimiento transformándolo en un costoso $O(n)$.

### 5. Cola Ligada
* **Pregunta:** ¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean $O(1)$?
* **Respuesta:** Necesitamos el puntero al frente para poder desencolar de inmediato sin buscar nada, y el puntero al final para encolar nuevas tareas al final de la fila directamente, sin tener que recorrer toda la estructura de inicio a fin.

### 6. Invariantes de la Cola
* **Pregunta:** ¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento?
* **Respuesta:** 
  1. El puntero `_frente` debe ser nulo (`None`).
  2. El puntero `_final` debe ser nulo (`None`).
  3. El tamaño de la cola (`_tamano`) debe ser exactamente $0$.

### 7. Operaciones Manuales de Cola (Traza)
A continuación, se detalla la evolución de la estructura paso a paso:

| Paso | Operación | `_frente` | `_final` | Cadena interna | Tamaño | Valor devuelto |
| :---: | :--- | :---: | :---: | :--- | :---: | :---: |
| 0 | Crear cola | `None` | `None` | está vacía | 0 | — |
| 1 | `encolar("A")` | Nodo A | Nodo A | Nodo A de manera aislada | 1 | — |
| 2 | `encolar("B")` | Nodo A | Nodo B | Nodo A enlazado hacia el Nodo B | 2 | — |
| 3 | `encolar("C")` | Nodo A | Nodo C | Nodo A enlazado a B, que a su vez apunta a C | 3 | — |
| 4 | `desencolar()` | Nodo B | Nodo C | Nodo B enlazado hacia el Nodo C | 2 | El valor `"A"` |
| 5 | Vaciar | `None` | `None` | se encuentra vacía | 0 | — |
| 6 | `encolar("Z")` | Nodo Z | Nodo Z | Nodo Z de manera aislada | 1 | — |

* **Pregunta de la sección:** ¿Qué referencias cambian al desencolar A de la cadena donde A apunta a B, y B apunta a C?
* **Respuesta:** La referencia `_frente` de la cola se desplaza para apuntar directamente al nodo que contiene a `B`. Adicionalmente, el nodo saliente `A` debe desvincularse de la estructura asignando su puntero `siguiente` a `None`, lo que permite que el recolector de basura de Python limpie la memoria de forma correcta.

### 8. Complejidad
* **Pregunta:** ¿Por qué buscar un valor sigue siendo $O(n)$ aunque encolar y desencolar sean $O(1)$?
* **Respuesta:** Porque las listas ligadas no tienen índices directos ni memoria contigua. Si buscas un dato específico, no queda de otra más que empezar desde el inicio e ir saltando de nodo en nodo hasta encontrarlo, lo cual requiere revisar los $n$ elementos en el peor de los casos.

---


### 9. BFS y Cola
* **Pregunta:** ¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS?
* **Respuesta:** Como la cola procesa de manera estricta en orden de llegada, nos garantiza que todos los nodos que están a una distancia $d$ de nuestro origen se procesen por completo antes de empezar a evaluar a los vecinos que están a distancia $d+1$. Esto es lo que crea la característica exploración por capas de BFS.

### 10. Visitados al Encolar
* **Pregunta:** ¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse?
* **Respuesta:** Si no marcas un nodo al encolarlo, este puede ser descubierto múltiples veces a través de distintos vecinos que se están procesando en el mismo nivel. Esto provocaría que metas el mismo nodo a la cola una y otra vez, desperdiciando muchísima memoria y tiempo de procesamiento en grafos densos.

### 11. Predecesores
* **Pregunta:** ¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido?
* **Respuesta:** Un simple diccionario de predecesores (`predecesores[vecino] = actual`). Con este mapa, podemos trazar la ruta hacia atrás desde cualquier destino hasta llegar al origen.

### 12. Reconstrucción del Camino
* **Pregunta:** ¿Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta?
* **Respuesta:** Un destino es inalcanzable si, al intentar volver sobre nuestros pasos hacia el origen, nos topamos con un nodo que no tiene predecesor asignado (o apunta a `None`) antes de haber alcanzado el origen. En cambio, si la tabla está corrupta, nos toparemos con ciclos infinitos (el mismo nodo se repite en el camino de vuelta) o claves inexistentes.

### 13. Práctica Guiada de BFS (Traza de Camino de A a F)
Traza detallada utilizando el orden alfabético de vecinos:

| Paso | Sale | Cola resultante | Nuevos predecesores registrados |
| :---: | :---: | :--- | :--- |
| 0 | — | A | A tiene como predecesor a `None` |
| 1 | A | B, C | B proviene de A; C proviene de A |
| 2 | B | C, D, E | D proviene de B; E proviene de B |
| 3 | C | D, E | *(E ya estaba encolado y se omite)* |
| 4 | D | E, F | F proviene de D |
| 5 | E | F | *(F ya estaba encolado y se omite)* |
| 6 | F | vacía | *(Se ha completado la exploración)* |

* **Pregunta de la sección:** ¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos?
* **Respuesta:** Porque en muchos grafos existen varias rutas de igual costo o longitud para llegar a un destino. Al cambiar el orden de los vecinos, el algoritmo descubrirá primero un camino u otro, registrándolo antes en el diccionario de predecesores y resolviendo el "empate" según ese orden de descubrimiento.



### 14. Lista Doblemente Ligada
* **Pregunta:** ¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece?
* **Respuesta:** Obtenemos la capacidad de movernos en ambas direcciones por la lista, lo que nos permite insertar o retirar nodos en ambos extremos con un rendimiento constante de $O(1)$. La obligación que surge es mantener la simetría de los enlaces: si el nodo `A.siguiente` es `B`, obligatoriamente `B.anterior` debe ser `A`.

### 15. Invariantes de Lista Doble
* **Pregunta:** ¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentemente inversos?
* **Respuesta:** Recorremos la lista desde el `_inicio` hasta el `_final` contando los nodos y verificando sus enlaces `siguiente`. Luego, hacemos el camino de regreso desde el `_final` hasta el `_inicio` usando los enlaces `anterior`. Ambos recorridos deben coincidir exactamente en el orden de los elementos y en el número total almacenado en `_tamano`.

### 16. Deque Ligada
* **Pregunta:** ¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO?
* **Respuesta:** Porque la deque es solo un contenedor de bajo nivel que ofrece operaciones en ambos extremos. Depende únicamente de nosotros y de la lógica de nuestro algoritmo decidir cómo usarla (por ejemplo, insertar al final y sacar por el inicio para FIFO, o insertar al final y sacar por el final para LIFO).

### 17. Operaciones Manuales de Deque (Traza)
Siguiendo las instrucciones del cuaderno:

| Paso | Operación | `_inicio` | Cadena resultante | `_final` | Tamaño | Devuelve |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| 0 | Crear | `None` | se encuentra vacía | `None` | 0 | — |
| 1 | `agregar_inicio("B")` | Nodo B | Nodo B de manera aislada | Nodo B | 1 | — |
| 2 | `agregar_inicio("A")` | Nodo A | Nodo A enlazado bidireccionalmente con B | Nodo B | 2 | — |
| 3 | `agregar_final("C")` | Nodo A | Nodo A enlazado con B, que a su vez se enlaza con C | Nodo C | 3 | — |
| 4 | `agregar_final("D")` | Nodo A | Nodos en cadena bidireccional desde A pasando por B y C hasta D | Nodo D | 4 | — |
| 5 | `quitar_inicio()` | Nodo B | Nodos en cadena bidireccional desde B pasando por C hasta D | Nodo D | 3 | El valor `"A"` |
| 6 | `quitar_final()` | Nodo B | Nodo B enlazado bidireccionalmente con C | Nodo C | 2 | El valor `"D"` |

* **Pregunta de la sección:** Después de quitar el inicio A de la cadena bidireccional que conecta A con B, B con C, y C con D, ¿qué cuatro hechos deben comprobarse?
* **Respuesta:** 
  1. Que se devuelva el valor correcto `"A"`.
  2. Que el nuevo `_inicio` apunte al nodo que contiene a `B`.
  3. Que la referencia `B.anterior` se limpie y quede establecida en `None`.
  4. Que los punteros `siguiente` y `anterior` de la cajita retirada (la que almacenaba a `"A"`) se pongan en `None` para asegurar la liberación de recursos.




### 18. Qué Problema Resuelve 0-1 BFS
* **Pregunta:** ¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0?
* **Respuesta:** Porque BFS asume que cada arista avanzada suma exactamente un costo de 1. Si hay caminos gratis (costo 0), es muy probable que una ruta con más aristas pero con costo acumulado menor sea mejor que una ruta directa que cuesta 1. BFS común elegirá la de menos aristas e ignorará la opción más barata.

### 19. Deque como Estructura de Prioridad
* **Pregunta:** ¿Qué información del peso decide el extremo de inserción y por qué?
* **Respuesta:** El peso de la arista relajada. Si el peso es $0$, significa que el nodo se mantiene en el mismo nivel de costo actual, así que se inserta al **inicio** de la deque para procesarse ya mismo. Si el peso es $1$, se inserta al **final** para que espere su turno ordenadamente.

### 20. Ejecución Manual de 0-1 BFS (Traza)
Traza completa sobre el grafo conductor:

| Paso | Sale | Arista | Decisión | Deque resultante (desde el inicio hacia el final) | Cambio de distancia |
| :---: | :---: | :---: | :--- | :--- | :--- |
| 0 | — | — | Inicio con el origen | Nodo A | La distancia de A se establece en 0 |
| 1 | A | A hacia B con costo 0 | Insertar al inicio | Nodo B | La distancia de B se establece en 0 |
| 2 | A | A hacia C con costo 1 | Insertar al final | Nodo B, seguido del Nodo C | La distancia de C se establece en 1 |
| 3 | B | B hacia D con costo 0 | Insertar al inicio | Nodo D, seguido de C | La distancia de D se establece en 0 |
| 4 | B | B hacia E con costo 1 | Insertar al final | Nodos ordenados como D, C y finalmente E | La distancia de E se establece en 1 |
| 5 | D | D hacia F con costo 1 | Insertar al final | Nodos ordenados como C, E y finalmente F | La distancia de F se establece en 1 |
| 6 | C | C hacia D con costo 0 | No mejora el costo | Nodos restantes: E y F | La distancia de D se mantiene en 0 |
| 7 | E | E hacia F con costo 0 | Mejora el costo | Nodo F queda como único elemento | F tiene nueva distancia de 1 con predecesor E |
| 8 | F | — | — | La deque queda vacía | — |

* **Pregunta de la sección:** Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X?
* **Respuesta:** Se actualiza su distancia en el mapa (`distancias[X] = 0`), su predecesor apunta al nuevo nodo responsable del camino más corto, y `X` se agrega al **inicio** de la deque debido a que la mejora fue gracias a una arista de costo 0.


### 21. Implementación
* **Pregunta:** ¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo?
* **Respuesta:** Nos ayuda a encapsular y depurar los errores lógicos por separado. Si algo falla a nivel de algoritmos de grafos, tendremos la total seguridad de que nuestras estructuras de datos funcionan de manera robusta y que el problema está en la lógica de búsqueda o relajación.

### 22. Casos Límite
* **Pregunta:** ¿Por qué True debe producir `TypeError` aunque `isinstance(True, int)` sea verdadero en Python?
* **Respuesta:** Porque en Python `bool` hereda directamente de `int`. Sin embargo, semánticamente un valor booleano representa una bandera de verdadero/falso, no una magnitud real de peso de arista para caminos mínimos, por lo que debe rechazarse explícitamente.

### 23. Pruebas
* **Pregunta:** ¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura?
* **Respuesta:** Detecta referencias residuales y estados inconsistentes de los extremos. Si al vaciar la estructura olvidamos limpiar `_frente` o `_final`, la siguiente inserción de elementos arrastrará nodos y relaciones viejas, corrompiendo la nueva cadena de datos.

### 24. Comparación de Algoritmos
* **Pregunta:** ¿Qué operación dominante conduce respectivamente a cola, deque o heap?
* **Respuesta:** 
  * Una **cola simple** domina cuando el procesamiento es puramente cronológico por capas de igual costo (FIFO).
  * Una **deque** domina cuando los costos se limitan estrictamente a incrementos de 0 o 1, permitiendo colocar las cosas prioritarias al inicio de forma inmediata.
  * Un **heap** es la operación dominante cuando los costos son números reales no negativos arbitrarios y necesitamos extraer dinámicamente el menor costo de un conjunto general de prioridades.

### 25. Cierre: Hacia Union-Find y Kruskal
* **Pregunta:** ¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos?
* **Respuesta:** ¿Cómo podemos agrupar de manera eficiente nuestros vértices en "conjuntos conectados" y verificar rápidamente si dos nodos ya pertenecen al mismo grupo antes de añadir la arista que los une? (Esa es precisamente la pregunta que nos abrirá paso a Union-Find y al algoritmo de Kruskal en las próximas clases).