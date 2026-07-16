# Notebook - Clase 09

## 1. Problemas motivadores CSES
**Pregunta.** ¿Qué diferencia hay entre modelar una secuencia y modelar relaciones? Una secuencia tiene por dominio enteros positivos mientras que una relación entre dos cosas pude tener por dominio cualquier otro conjunto. Esto hace que simular una relación cualesquiera exija pensar también en un "paso", en vez de solo usar unidades de tiempo.
## 2. Modelado de relaciones
### Building Roads
1. ¿Qué representa un nodo? Una ciudad.
2. ¿Qué representa una arista? Una carretetera entre (estrictamente) dos ciudades.
3. ¿Es dirigido? No, podría ir en dos sentidos. 
4. ¿Es ponderado? No.
5. ¿Qué pregunta algorítmica aparece? ¿Cómo relaciono los elementos de una estrctura de datos dos a dos minimizando la cantidad de relaciones?
### Counting Rooms
1. ¿Qué representa un nodo? Un cuarto.
2. ¿Qué representa una arista? Cuartos contiguos (separados por solo una pared).
3. ¿Es dirigido? No.
4. ¿Es ponderado? No.
5. ¿Qué pregunta algorítmica aparece? ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula y contar ciertos espacios de interés?
### Labyrinth
1. ¿Qué representa un nodo? Puntos en una cuadrícula.
2. ¿Qué representa una arista? Un camino entre dos puntos en la cuadícula.
3. ¿Es dirigido? Sí, es necesario asumir que vas estrictamente de "A" a "B" ya que ir al revés te devuelve al inicio del laberinto. 
4. ¿Es ponderado? No, aumque los pesos a cada forna de llegar se pueden asignar según la longitud de pasos. En este caso preferimos un peso pequeño.
5. ¿Qué pregunta algorítmica aparece? ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad?
### Message Route
1. ¿Qué representa un nodo? Una computadora.
2. ¿Qué representa una arista? Una conexión (biunívoca) entre dos computadoras distintas.
3. ¿Es dirigido? Sí, es necesario asumir que vas estrictamente de "A" a "B" ya que ir al revés te devuelve al remitente. 
4. ¿Es ponderado? No, aunque los pesos a cada forna enviar el mensaje se pueden asignar según la longitud de la red de conexiones. En este caso preferimos un peso pequeño.
5. ¿Qué pregunta algorítmica aparece? ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad?
| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Ciudad | Carretera | No | No | ¿Cómo relaciono los elementos de una estrctura de datos dos a dos minimizando la cantidad de relaciones? |
| Counting Rooms | Cuarto  | Cuartos contiguos | No | No | ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula y contar ciertos espacios de interés? |
| Labyrinth | Puntos (plano coordenado) | Camino entre dos puntos | Sí | No | ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad? |
| Message Route | Computadora | Conexión(biunívoca) | Sí | No | ¿Qué estructura de datos es más eficiente para recorrer una cuadrícula de múltiples formas posibles sin incrementar mucho la cpmplejidad? |
## 3. Conceptos básicos de grafos
**Pregunta.** Da un ejemplo propio de grafo dirigido y otro de grafo no dirigido.
- Dirigido: Formas de llegar de una ciudad A a B (excluyendo caminos de una sola carretera)
- No dirigido: Contar personas en un mapa.
## 4. Representaciones
**Pregunta.** ¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué? Listar vecinos porque es lo que genera interés, los nodos que no conectan no tienen relaciones útiles para el problema. Si enlisto todos los nodos guardo información inútil.
## 5. Interfaz común
**Pregunta.** ¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz? Porque ambas son implementaciones útiles para el mismo problema que convenimos usar en un caso u otro, pero las operaciones en general se conservam porque estamos usando la misma estructura de fondo, solo con una reprsentacion distinta.
## 6. Implementaciones
**Pregunta.** ¿Por qué un `set` ayuda a evitar aristas duplicadas? Porque el set elimina automáticamente repeticiones.
**Pregunta.** ¿Qué debe pasar con la matriz cuando agregas un vértice nuevo? Debería crear una nueva fila y en cada columna un False por defecto hasta que añadamos una arista nueva y entonces cambiamos el False. Ejemplo: Agregar arista entre 1 y 2 -> Cambia a True en la celda (1,2) y (2,1) porque no son dirigidos
## 7. Visualización con NetworkX
**Pregunta.** ¿Por qué un `set` ayuda a evitar aristas duplicadas? Porque el set elimina repeticiones. 
**Pregunta.** ¿Qué debe pasar con la matriz cuando agregas un vértice nuevo? Se debe ver un 'True' en las coordenadas (n,k) y (k,n) donde k y n son la fila/columna que corresponde a un vértice y así el punto (n,k) representa si hay arista entre ambas. 

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| **Memoria** | **Eficiente:** Solo guarda los vértices y las aristas que realmente existen. | **Ineficiente:** Reserva espacio para todas las conexiones posibles, sean `True` o `False`. |
| **Facilidad de implementación** | **Media:** Requiere manejar diccionarios con colecciones internas (listas o conjuntos) que crecen dinámicamente. | **Alta:** Es una estructura muy directa (una tabla/lista bidimensional de booleanos o números). |
| **Consultar vecinos** | **Muy rápida:** O(1) para acceder a la lista del vértice, o O(vecinos) para recorrerlos. | **Lenta:** O(vecinos). Tienes que recorrer toda la fila del vértice de principio a fin para ver quién tiene un `True`. |
| **Consultar si existe arista** | **Media/Rápida:** O(vecinos) si los vecinos son una lista, o O(1) si usas conjuntos (`set`) con  `in`. | **Ultra rápida:** O(1). Vas directo a la coordenada exacta en la matriz matriz[origen][destino]. |
| **Grafos dispersos** *(pocas aristas)* | **Ideal:** No desperdicia espacio en memoria guardando conexiones inexistentes. | **Mala opción:** La gran mayoría de las celdas de la matriz estarán llenas de `False`, desperdiciando RAM. |
| **Grafos densos** *(muchas aristas)* | **Aceptable:** Pierde su ventaja de memoria ya que, al estar casi todos conectados, se acerca al tamaño de la matriz. | **Ideal:** Como el grafo está lleno de conexiones, la matriz se aprovecha al máximo y sus consultas son inmediatas. |
## 8. Diseño de pruebas
``` text
def test_sencillo_cantidad_nodos_y_aristas():
    """Verifica que el grafo de ejemplo tenga exactamente 3 vértices y 2 aristas."""

    grafo = modulo.construir_grafo_ejemplo() $

    assert grafo.cantidad_vertices() == 3, f"El grafo de ejemplo debería tener exactamente 3 vértices"

    assert grafo.cantidad_aristas() == 2, f"El grafo de ejemplo debería tener exactamente 2 aristas"


def test_sencillo_conexion_vecinos():
    """Verifica que el nodo 'A' esté correctamente conectado a sus vecinos correspondientes."""

    grafo = modulo.construir_grafo_ejemplo()

    vecinos_de_A = set(grafo.vecinos("A"))

    assert vecinos_de_A == {"B", "C"}, "Los vecinos de 'A' deberían ser únicamente 'B' y 'C'"
    
    # 'B' no debería tener a 'C' como vecino directo
    assert "C" not in grafo.vecinos("B"), "No debería existir una arista directa entre 'B' y 'C'"
```
## 9. Patrón descubierto
Hemos descubierto que las relaciones entre objetos tienen representaciones visuales y pueden compartir rasgos como: biunivocidad, dirección, pesos, etc. Además, en el sentido algorítmico, según la información que busquemos preservar o indagar podemos elegir implementaciones distintas. Para acceder a la lista vecinos rápido, podemos usar diccionarios ya que acceder al valor de una llave es poco costoso (O(1)) y no usa mucha memoria adicional. Para encontrar quizás la posición doble de una arista, usar una matriz con un diccionario de vértices nos puede ayudar si queremos visualizar mejor un grafo denso. Observar si existe un nodo requiere solo acceder al elemento matriz[n][m] que tiene complejidad O(1).
## 10. Cierre
Durante esta práctica hemos entendido el uso de los grafos como estructura de datos, las operaciones que requiere tener, se exploró un poco sobre los "costos" de éstas en términos de complejidad tiempo-memoria y se discutió sobre problemas que requieren de implementar esta nueva estructura de datos para poderles dar una representación natural. 