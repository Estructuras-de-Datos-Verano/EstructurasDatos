# Notebook_clase_17_Max

# notebook17.md

# Sección 1 (Pregunta inicial)

**- ¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?**
    Cuando todo vale lo mismo ocupamos una cola (ColaLigada) para hacer un BFS normalito. Cuando ya tenemos dos niveles de prioridad (como costos de 0 y 1) la cosa cambia y necesitamos una deque para poder meter las cosas que cuestan cero al inicio y las que cuestan uno al final, haciendo un 0-1 BFS.

# Sección 1 (Presentación de la clase)

**- ¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades?**
    Que ya no importa nomas quien llego primero, ahora la pregunta es a quien conviene procesar antes, porque algunas acciones te cuestan cero y se pueden resolver luego luego, y otras cuestan uno.

# Sección 2 (Problema inicial con pop(0))

**- ¿Qué trabajo repetido introduce pop(0) y por qué una referencia al frente lo evita?**
    Cuando ocupas pop(0) en una lista de python normal, quitas el primero pero todos los demas elementos se tienen que recorrer una pocisión para atras, entonces repites el trabajo y te cuesta O(n). Si usas una referencia al frente, nomas mueves la referencia al siguiente nodo y ya, no tienes que compactar nada y el costo es O(1).

# Sección 3 (Nodo y referencias)

**- ¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos?**
    El valor es nomas el dato (onda una "A"), el nodo es la pieza que guarda ese valor y las referencias al siguiente, y la estructura (como ColaLigada) son las reglas que dicen como se modifica la cola, que se permite hacer y que invariantes se mantienen.

# Sección 4 (Lista ligada simple)

**- ¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?**
    Encolar un elemento al final sería carisimo, porque tendrias que recorrer todaaa la lista desde el inicio hasta encontrar el ultimo nodo para poder conectarlo.

# Sección 5 (Cola ligada)

**- ¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean O(1)?**
    Porque para encolar ocupas ir directo al final y enlazar el nuevo nodo, y para desencolar ocupas sacar del frente. Si tienes las dos referencias no tienes que recorrer la cadena para ninguna de las dos cosas.

# Sección 6 (Invariantes de cola)

**- ¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento?**
    Como ya se quedo vacia, debe pasar que el frente sea None, el final sea None, y el tamaño se vuelva 0. 

# Sección 7 (Operaciones manuales)

**- En la secuencia manual, ¿qué referencias cambian al desencolar A de la cadena A → B → C?**
    El frente cambia para apuntar ahora a B, y el nodo A que sale se le limpia su referencia al siguiente para que no jale la cadena completa accidentalmente.

# Sección 8 (Complejidad)

**- ¿Por qué buscar un valor sigue siendo O(n) aunque encolar y desencolar sean O(1)?**
    Porque no tenemos referencias directas a los nodos del medio, si quieres saber si un valor esta ahi a fuerza tienes que empezar desde el frente e ir caminando nodo por nodo hasta encontrarlo.

# Sección 9 (BFS y cola)

**- ¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS?**
    BFS va descubriendo todo por capas (primero distancia 0, luego 1, etc). El orden FIFO de la cola hace que exactamente lo que descubriste primero se procese primero, respetando ese orden natural de las capas.

# Sección 10 (Visitados al encolar)

**- ¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse?**
    Si lo marcas hasta que sale, podria ser que dos nodos diferentes apunten al mismo vecino y los dos lo metan a la cola, entonces se duplica en la cola y repites muchisimo trabajo a lo menso, aparte de que sobreescribes sus predecesores.

# Sección 11 (Predecesores)

**- ¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido?**
    Guardar nomas un mapa compacto tipo diccionario donde guardas predecesores[vecino] = actual, con eso es suficiente para luego irte para atras desde el destino hasta el origen.

# Sección 12 (Reconstrucción del camino)

**- ¿Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta?**
    Un destino inalcanzable simplemente va llendo hacia atras y topa con None antes de llegar al origen (regresas una lista vacia). Una tabla corrupta es si el camino hace un ciclo (un nodo ya aparecio antes) o si de plano hay un nodo en el camino que no existe como clave en el diccionario.

# Sección 13 (Práctica guiada de BFS)

**- ¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos?**
    Porque para llegar a la misma capa todos los caminos usan la misma cantidad de aristas, pero dependiendo de a quien encoles primero se va a guardar ese como su primer predecesor, entonces la ruta cambia pero la distancia es la misma.

# Sección 14 (Lista doblemente ligada)

**- ¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece?**
    Obtenemos la capacidad de retirar o agregar en AMBOS extremos en tiempo O(1). La obligación es que los enlaces tienen que concordar en ambas direcciones (si A apunta a B, B tiene que apuntar a A por fuerza).

# Sección 15 (Invariantes de lista doble)

**- ¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentes?**
    Recorriendo la lista de inicio a final contando nodos y checando que el anterior del actual sea el nodo que acabas de visitar, y luego hacer lo mismo de reversa, y que las dos cuentas den igual al tamaño guardado.

# Sección 16 (Deque ligada)

**- ¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO?**
    Porque la deque te deja meter y sacar por donde sea (inicio y final), ya depende de ti y de tu algoritmo si quieres usarla como cola, como pila o combinada.

# Sección 17 (Operaciones manuales de deque)

**- Después de quitar el inicio A de A ⇄ B ⇄ C ⇄ D, ¿qué cuatro hechos deben comprobarse?**
    Que el nuevo inicio (B) tenga su anterior en None, que el nodo retirado (A) tenga ambos enlaces en None para no arrastrar basura, y que el tamaño se haya restado en uno.

# Sección 18 (Qué problema resuelve 0-1 BFS)

**- ¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0?**
    Porque el BFS normal asume que todas cuestan lo mismo (costo 1 por arista digamos), entonces siempre elige caminos con menos saltos, pero si hay aristas gratis podrias tener un camino de 3 saltos que cueste cero y el BFS normal agarraria uno de 1 salto que cueste uno, entonces falla.

# Sección 19 (Deque como estructura de prioridad)

**- ¿Qué información del peso decide el extremo de inserción y por qué?**
    Si la arista cuesta 0 la agregamos al inicio de la deque porque significa que tiene el mismo costo actual y hay que revisarla luego luego, si cuesta 1 la metemos al final porque va despues de los que tienen el costo actual.

# Sección 20 (Ejecución manual de 0-1 BFS)

**- Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X?**
    Cambia su distancia guardada de 1 a 0, se actualiza su predecesor al nuevo nodo que lo descubrio con esa distancia mejorada y se vuelve a agregar a la deque pero ahora por el inicio.

# Sección 21 (Implementación)

**- ¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo?**
    Que si falla el algoritmo ya sabes que la bronca esta en la logica del algoritmo y no en que tu cola o tu deque se rompan o esten arrastrando referencias de basura.

# Sección 22 (Casos límite)

**- ¿Por qué True debe producir TypeError aunque isinstance(True, int) sea verdadero en Python?**
    Porque un booleano no es un peso logico para la arista, aunque python lo trate como int debajo del agua, hay que rechazarlo explicitamente para que nuestro contrato sea robusto.

# Sección 23 (Pruebas)

**- ¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura?**
    El clasico error de que al quitar el ultimo elemento no limpiaste bien las referencias del inicio y el final, y al meter cosas nuevas te salen cosas de la cadena vieja que "segun tu" ya habias borrado.

# Sección 24 (Comparación BFS, 0-1 BFS y Dijkstra)

**- ¿Qué operación dominante conduce respectivamente a cola, deque o heap?**
    Para BFS la operacion es procesar por orden de llegada (cola). Para 0-1 BFS es adelantar los de costo 0 y posponer los de costo 1 (deque). Y para Dijkstra es siempre extraer la menor distancia posible de un monton de pesos variados (min-heap).

# Sección 25 (Cierre hacia Union-Find y Kruskal)

**- ¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos?**
    Ya no es nomas buscar el camino minimo desde un origen, la nueva pregunta es ver como conectar cosas (unir componentes) de la forma más barata y asegurarnos de no formar ciclos cerrados.