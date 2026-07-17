# Clase 17: Notebook
#### Nombre: Patricio Navarro

## Pregunta inicial
¿Qué estructura necesitamos cuando todos los pendientes tienen la misma prioridad, y qué cambia cuando existen dos niveles de prioridad?
- Cuando todos los elementos tienen la misma prioridad un grafo con BFS funciona perfecto.
- Cuando existen dos niveles de prioridad conviene más algo como un Heap queue, pero mezclado con alguna otra estructura podría ser.

## Presentación de la clase
**¿Qué aspecto del problema cambia cuando pasamos de una sola prioridad a dos prioridades?**
- Que ya no es solo atender los problemas conforme llegan, sino también definir cuales son de mayor prioridad dependiendo su costo.

## Problema inicial con pop(0)
**¿Qué trabajo repetido introduce pop(0) y por qué una referencia al frente lo evita?**
- `pop(0)` necesita recorrer todos los elementos de la lista, algo que se vuelve muy costoso.
- Una referencia al frente en vez solo recorre los índices sin tener que recorrer los elementos.

## Nodo y referencias
**¿Cuál es la diferencia entre el valor guardado, un nodo y la estructura que administra los nodos?**
- Valor: Es el dato individual.
- Nodo: Es la "caja" que envuelve ese valor y guarda la referencia hacia el siguiente elemento.
- Estructura contenedora: Es la que pone las reglas  e incluye el control general de todo el conjunto de nodos.

## Lista ligada simple
**¿Qué operación sería costosa si una lista simple solo guardara la referencia al inicio?**
- Agregar un elemento al final sería muy costoso. Tendrías que recorrer todos los nodos de la cadena, uno por uno, para encontrar dónde enganchar el nuevo elemento.

## Cola ligada
**¿Por qué necesitamos frente y final para que las dos operaciones dominantes sean O(1)?**
- Porque desencolar ocurre exclusivamente en el frente y encolar ocurre en el final. Guardar ambas referencias permite acceder directamente a los extremos sin tener que recorrer la cadena.

## Invariantes de cola
**¿Qué tres afirmaciones deben ser simultáneamente ciertas después de desencolar el único elemento?**
- La variable frente debe quedar en None.
- La variable final también debe quedar en None.
- El tamaño registrado debe ser 0.

## Operaciones manuales
**Actividad:** Dibuja cada nodo, las referencias externas y el tamaño. Los primeros pasos sirven de modelo; completa el resto.
| Paso | Operación | frente | final | cadena | tamaño | valor devuelto |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear cola | `None` | `None` | vacía | 0 | — |
| 1 | `encolar("A")` | A | A | A | 1 | — |
| 2 | `encolar("B")` | A | B | A → B | 2 | — |
| 3 | `encolar("C")` | A | C | A → B → C | 3 | — |
| 4 | `desencolar()` | B | C | B → C | 2 | - |
| 5 | vaciar | `None` | `None` | vacía | 0 | - |
| 6 | `encolar("Z")` | Z | Z | Z | 1 | — |

**En la secuencia manual, ¿qué referencias cambian al desencolar A de la cadena A → B → C?**
- La referencia `frente` avanza para apuntar a `B`. Además, el tamaño se reduce en uno. El final no sufre ningún cambio.

## Complejidad
**¿Por qué buscar un valor sigue siendo O(n) aunque encolar y desencolar sean O(1)?**
- Porque solo tenemos acceso directo a los extremos de la cola. Si quieres encontrar un elemento que está en medio, seguirás obligado a recorrer toda la cadena desde el frente.

## BFS y cola
**¿Qué relación existe entre el orden FIFO y el procesamiento por capas de BFS?**
- El orden FIFO asegura que los nodos descubiertos antes se procesen primero. Esto es exactamente lo que BFS necesita para explorar respetando las distancias de menor a mayor.

## Visitados al encolar
**¿Qué duplicación puede ocurrir si un vértice se marca solo al desencolarse?**
- El mismo vértice podría volver a encolarse múltiples veces si se descubre desde diferentes caminos antes de que salga de la cola.

## Predecesores
**¿Qué información mínima permite reconstruir un camino sin guardar rutas completas durante el recorrido?**
- Solo necesitas guardar a su primer predecesor, es decir, el vecino responsable de haberlo descubierto inicialmente.

## Reconstrucción del camino
**¿Cómo distingues un destino inalcanzable de una tabla de predecesores corrupta?**
- Es inalcanzable si la cadena termina en None antes de lograr llegar al origen.
- Está corrupta si te topas con un nodo repetido (lo que indica un ciclo) o si hay referencias a claves que no existen en tu registro.

## Práctica guiada de BFS
**Actividad:** Usa el grafo conductor y respeta el orden de vecinos:

```python
{"A": ["B", "C"], "B": ["A", "D", "E"],
 "C": ["A", "E"], "D": ["B", "F"],
 "E": ["B", "C", "F"], "F": ["D", "E"]}
```

| paso | sale | cola después | nuevos predecesores |
| ---: | --- | --- | --- |
| 0 | — | A | A: `None` |
| 1 | A | B, C | B: A; C: A |
| 2 | B | C, D, E | D: B; E: B |
| 3 | C | D, E | `None`|
| 4 | D | E, F | F: D  |

**¿Por qué puede cambiar el camino concreto sin cambiar su longitud mínima cuando cambia el orden de vecinos?**
- Porque a una misma distancia (misma "capa") pueden existir varios caminos igualmente cortos. Cambiar el orden simplemente hace que el algoritmo escoja otra de las opciones válidas.

## Lista doblemente ligada
**¿Qué nueva capacidad obtenemos con anterior y qué obligación de consistencia aparece?**
- Obtenemos la capacidad de retirar o agregar nodos rápidamente en ambos extremos. La obligación es que ambos enlaces deben coincidir: si A apunta a B hacia adelante, B debe apuntar a A hacia atrás.

## Invariantes de lista doble
**¿Cómo comprobarías automáticamente que los enlaces anterior y siguiente son consistentes?**
- Recorriendo la lista de inicio a fin y revisando que el nodo anterior de cada paso corresponda al nodo que acabas de dejar atrás. Luego, compruebas que la cantidad de elementos coincida al hacerlo en ambas direcciones.

## Deque ligada
**¿Por qué una deque no determina por sí sola si el comportamiento será FIFO o LIFO?**
- Porque la deque solo proporciona las herramientas como insertar y quitar por ambos extremos pero el algoritmo quien toma la decisión de qué lado usar para lograr el comportamiento deseado.

## Operaciones manuales de deque
**Actividad:** Traza cada cambio en ambas direcciones:

| paso | operación | inicio | cadena | final | tamaño | devuelve |
| ---: | --- | --- | --- | --- | ---: | --- |
| 0 | crear | `None` | vacía | `None` | 0 | — |
| 1 | `agregar_inicio("B")` | B | B | B | 1 | — |
| 2 | `agregar_inicio("A")` | A | A ⇄ B | B | 2 | — |
| 3 | `agregar_final("C")` | A | A ⇄ B ⇄ C | C | 3 | — |
| 4 | `agregar_final("D")` | A | A ⇄ B ⇄ C ⇄ D | D | 4 | — |
| 5 | `quitar_inicio()` | B | B ⇄ C ⇄ D | D | 3 | - |
| 6 | `quitar_final()` | B | B ⇄ C | C | 2 | - |

**Después de quitar el inicio A de A ⇄ B ⇄ C ⇄ D, ¿qué cuatro hechos deben comprobarse?**
- Que el nuevo inicio (B) tenga su enlace anterior como `None`.
- Que el nodo retirado (A) tenga su enlace siguiente limpio a `None`.
- Que el nodo retirado (A) tenga su enlace anterior limpio a `None`.
- Que el tamaño total se haya ajustado.

## Que problema resuelve 0-1 BFS
**¿Por qué BFS común puede fallar cuando algunas aristas cuestan 0?**
- Porque BFS solo cuenta "saltos" asumiendo que todos valen igual. Prefiere un camino de 1 salto, ignorando uno de 3 saltos gratuitos que en realidad sería la mejor opción.

## Deque como estructura de prioridad 
**¿Qué información del peso decide el extremo de inserción y por qué?**
- Peso 0: Se agrega al inicio para que se revise de inmediato, porque no incrementa el costo actual.
- Peso 1: Se agrega al final para que quede detrás en la fila de espera, pues representa un costo mayor.

## Ejecución manual de 0-1 BFS
**Actividad:** Usa el grafo conductor:

```python
{"A": [("B", 0), ("C", 1)], "B": [("D", 0), ("E", 1)],
 "C": [("D", 0)], "D": [("F", 1)],
 "E": [("F", 0)], "F": []}
```

| paso | sale | arista | decisión | deque inicio→final | cambio de distancia |
| ---: | --- | --- | --- | --- | --- |
| 0 | — | — | agregar origen | A | d(A)=0 |
| 1 | A | A→B (0) | inicio | B | d(B)=0 |
| 2 | A | A→C (1) | final | B,C | d(C)=1 |
| 3 | B | B→D (0) | inicio | D,C | d(D)=0 |
| 4 | B | B→E (1) | final | D,C,E | d(E)=1 |

**Cuando X mejora de distancia 1 a 0, ¿qué valores cambian y dónde se agrega X?**
- Cambia su valor registrado de distancia y su predecesor. El nodo X se vuelve a insertar, pero esta vez al inicio de la deque por tener un peso de mejora 0.

## Implementación
**¿Qué ventaja tiene implementar y probar cada estructura antes de integrarla al algoritmo?**
- Garantizas que si algo falla más adelante, sabrás que el error proviene del algoritmo y no de una estructura de soporte rota, facilitando su corrección.

## Casos límite
**¿Por qué True debe producir TypeError aunque isinstance(True, int) sea verdadero en Python?**
- Aunque Python los trate como números en el fondo, un booleano no representa un costo válido para una arista ni un vértice de grafo bajo un uso correcto, así que se rechaza para evitar problemas lógicos.

## Pruebas
**¿Qué defecto concreto detecta una prueba que vacía y vuelve a llenar la misma estructura?**
- Detecta si quedan "restos" de referencias viejas en el sistema. Si vacías la cola y las variables de extremo no se limpiaron correctamente a None, llenar de nuevo la estructura arrastrará información residual y el test fallará.

## Comparación BFS, 0-1 y Dijkstra
¿Qué operación dominante conduce respectivamente a cola, deque o heap?
- Cola: Conservar el orden de llegada básico.
- Deque: Adelantar inmediatamente prioridades 0 y postergar prioridades 1.
- Heap: Buscar de forma constante y dinámica la menor distancia general.

## Cierre
**¿Qué nueva pregunta aparece si queremos seleccionar aristas baratas sin formar ciclos?**
- Aparece el desafío de unir componentes individuales de forma óptima sin que formen caminos circulares. 