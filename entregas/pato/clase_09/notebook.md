# Clase 09: Notebook
#### Nombre: Patricio Navarro

## Presentación de la clase
¿Qué diferencia hay entre modelar una secuencia y modelar relaciones?
    - Que en una secuencia los únicos elementos que se conectan son el actual, su predecesor y su sucesor, y además tiene un órden.
    `predecesor -> actual -> sucesor`
    Mientras tanto, al modelar relaciones, solo te importa que los elementos cumplan cierta condición y no necesariamente importa realmente el órden en que se conecten, tampoco tiene por qué marcar una jerarquía (cosa que en una secuencia sí hay).

## Problemas motivadores: CSES

### Building Roads
1. ¿Qué representa un nodo?
    - Una ciudad.
2. ¿Qué representa una arista?
    - Un camino o carretera.
3. ¿Es dirigido?
    - No, porque va en ambos sentidos.
4. ¿Es ponderado?
    - No, todas las carreteras valen lo mismo.
5. ¿Qué pregunta algorítmica aparece?
    - Encontrar la cantidad de ciudades conectadas.

### Counting Rooms
1. ¿Qué representa un nodo?
    - Un cuadro de piso.
2. ¿Qué representa una arista?
    - Los bordes entre dos cuadros de piso. Es decir, si dos cuadros de piso están unidos por un borde, en el grafo hay una arista que los conecta.
3. ¿Es dirigido?
    - No.
4. ¿Es ponderado?
    - No, todas valen lo mismo.
5. ¿Qué pregunta algorítmica aparece?
    - ¿Cuantos nodos están conectados?

### Labyrinth
1. ¿Qué representa un nodo?
    - Un cuadro de piso y los puntos de partida a y b.
2. ¿Qué representa una arista?
    - Que se pueda pasar de un cuadro de piso a otro. Osea si hay dos cuadros juntos, y ambos son válidos, entonces hay una arista entre ellos.
3. ¿Es dirigido?
    - No.
4. ¿Es ponderado?
    - No.
5. ¿Qué pregunta algorítmica aparece?
    - ¿Cuál es el camino más corto entre los puntos a y b?

### Message Route
1. ¿Qué representa un nodo?
    - Una computadora dentro de la red.
2. ¿Qué representa una arista?
    - El que se pueda mandar mensajes entre dos computadoras.
3. ¿Es dirigido?
    - No.
4. ¿Es ponderado?
    - No.
5. ¿Qué pregunta algorítmica aparece?
    - ¿Cómo se pueden conectar o mandar mensajes dos computadoras no enlazdas de la forma más rápida?

## Lectura de modelado
| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudad | Carretera | No | No | # Ciudades conectadas |
| Counting Rooms | `.` | Dos `.` juntos | No | No | # `.` conectados |
| Labyrinth | `.`, `a`, `b` | espacios habilitados | No | No | Camino más corto |
| Message Route | Computadora | Conexión de red | No | No | Camino más corto |

## Conceptos básicos de grafos
Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.
- Dirigido: Movimientos de dinero, como transferencias o pagos.
- No dirigido: Relaciones de amigos.

## Representaciones de grafos
¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?
- Preguntar si existe una arista. Porque si hay una arista automáticamente hay una relación entre ellos, y entonces ya se pueden considerar y descartar los datos útiles de los que no.

## Interfaz común
¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?
- Porque pueden resolver los mismos problemas, solo que su representación es distinta y puede que una convenga más para unos problemas que para otros.

## Implementación 1: `GrafoListaAdyacencia`
¿Por qué un `set` ayuda a evitar aristas duplicadas?
- Porque cada elemento solo aparece una vez, entonces en automático elimina todos los elementos duplicados y así también las aristas duplicadas.

## Implementación 2: `GrafoMatrizAdyacencia`
¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?
- Se deben actualizar los elementos de la matriz, porque tendrían un nuevo vecino.

## Comparación
| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Eficiente `O(V + E)`: Solo guarda espacio para los vértices existentes y sus aristas reales. | Ineficiente `O(V^2)`: Siempre consume un espacio cuadrático, sin importar cuántas aristas existan realmente. |
| Facilidad de implementación | Alta: En Python es sumamente intuitiva y directa gracias al uso nativo de un diccionario de conjuntos. | Media / Baja: Hacer crecer la matriz dinámicamente (añadir filas y columnas balanceadas) requiere más lógica. |
| Consultar vecinos | Eficiente `O(\text{vecinos})`: Simplemente se accede al conjunto del vértice y se devuelven sus elementos directamente. | Lenta `O(V)`: Obliga a recorrer la fila entera de la matriz de inicio a fin para comprobar qué columnas tienen un `True`. |
| Consultar si existe arista | Rápida (`O(1)` promedio): Gracias a la propiedad de "hashing" que tienen los conjuntos (`set`) en Python. | Instantánea (`O(1)` estricto): Es un acceso directo e inmediato por posiciones de memoria en la lista indexada (`matriz[i][j]`). |
| Grafos dispersos | Excelente: Es la estructura ideal ya que no desperdicia almacenamiento en conexiones que no existen. | Muy mala: Da lugar a una matriz vacía llena de valores `False`, desperdiciando una enorme cantidad de memoria RAM. |
| Grafos densos | Regular: Aunque funciona, la sobrecarga de memoria de los objetos y diccionarios pierde ventajas frente a la matriz. | Excelente: Es la opción ideal cuando el grafo está casi completamente conectado, ya que aprovecha al máximo el espacio reservado. |

## Convertir implementación propia a Networkx
¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?
- Para poder usarla de manera más rápida y comparar como funciona con una biblioteca ya establecida.

## Diseño de pruebas
Diseña al menos dos pruebas propias y explica qué comportamiento verifican.
1. Prueba que el grafo si se cree y se guarde como un png.
```python
    def test_todo_guardar_visualizacion_grafo():
        grafo = modulo.GrafoListaAdyacencia()
        grafo.agregar_arista("A", "B")
        grafo.agregar_arista("B", "C")
        modulo.guardar_visualizacion_grafo(grafo, "grafo_ejemplo.png")
        assert os.path.exists("grafo_ejemplo.png"), "No se generó el archivo de visualización."
```

2. Prueba el ejemplo que usamos en la implementación.
```python
    def test_todo_construir_grafo_ejemplo():
        grafo = modulo.construir_grafo_ejemplo()
        assert grafo.contiene_arista("A", "B")
        assert grafo.contiene_arista("B", "C")
        assert grafo.contiene_arista("C", "D")
        assert grafo.contiene_arista("D", "A")
        assert grafo.contiene_arista("C", "E")
```

## Patrón descubierto 
Explica con tus palabras el patrón de modelado de relaciones.
- Es un patrón que se usa cuando queremos ver como se pueden conectar ciertas cosas a partir de relaciones o de condiciones, en este patrón los objetos se pueden ver como nodos y las condiciones que los unen son las aristas. Dependiendo el sentido de las rlaciones son dirigidas o no y dependiendo el valor que les quieras asignar son ponderadas o no.

## Cierre
1. ¿Qué ganamos al modelar relaciones como grafo?
    - Es más fácil de visualizar y la forma de buscar información es más sencilla porque basta con preguntar si hay una arista entre dos objetos.
2. ¿Cuándo usarías lista de adyacencia?
    - Cuando tuviera muchos datos y quisiera ser muy claro con lo que hago porque es más eficiente y más fácil de entender.
3. ¿Cuándo usarías matriz de adyacencia?
    - Caundo tuviera pocos datos y quisiera un reto.
4. ¿Qué puede ocultar una visualización?
    - Las condiciones que unen los objetos o aquellos que no están relacionados por aristas.
5. ¿Qué algoritmo necesitaremos para recorrer el grafo?
    - Pasar por cada vértice en el órden en que los guardamos y preguntar por sus vecinos directos.