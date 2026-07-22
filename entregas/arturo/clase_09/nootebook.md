# Arturo Prudencio Bonilla

## seccion 1

¿Que diferencia hay entre modelar una secuencia y modelar relaciones?
    supongo que como se interpretan y como se adquiere los datos, tambien su froma de organizarlos y sobre todo la visualizacion y con ello la posible interfaz

## seccion 2

### Buildind roads
1. ¿Qué representa un nodo?
    Una ciudad
2. ¿Qué representa una arista?
    Una carretera que conecta dos ciudades
3. ¿Es dirigido?
    No. Las carreteras permiten viajar en ambos sentidos entre las dos ciudades que conectan.
4. ¿Es ponderado?
    No
5. ¿Qué pregunta algorítmica aparece?
    encontrar la cantidad de ciudades conectadas 

### Counting Rooms
1. ¿Qué representa un nodo?
    un suelo
2. ¿Qué representa una arista?
    que haya dos suelos conectados (adyacentes)
3. ¿Es dirigido?
    No
4. ¿Es ponderado?
    No
5. ¿Qué pregunta algorítmica aparece?
    encontrar el numero de conexiones que hay

### Labyrinth
1. ¿Qué representa un nodo?
    suelos, inicio o final
2. ¿Qué representa una arista?
    que te puedas mover hacia esa casilla
3. ¿Es dirigido?
    No
4. ¿Es ponderado?
    No
5. ¿Qué pregunta algorítmica aparece?
    hay que encontrar el camino mas corti (si es que hay)

### Message Route
1. ¿Qué representa un nodo?
    Una computadora.
2. ¿Qué representa una arista?
    Una conexión de red directa entre dos computadoras.
3. ¿Es dirigido?
    No
4. ¿Es ponderado?
    No
5. ¿Qué pregunta algorítmica aparece?
    Búsqueda del camino más corto

## seccion 3

| Problema | Nodo | Arista | Dirigido | Ponderado | Pregunta algorítmica |
| --- | --- | --- | --- | --- | --- |
| Building Roads | Una ciudad | Carretera entre 2 ciudades | No | No | Encontrar la cantidad de ciudades conectadas |
| Counting Rooms | Un suelo | Adyacencia entre 2 suelos | No | No | Encontrar el número de conexiones que hay |
| Labyrinth | Suelo, inicio o final | Movimiento válido a otra casilla | No | No | Encontrar el camino más corto (si hay) |
| Message Route | Una computadora | Conexión de red directa | No | No | Búsqueda del camino más corto |


## seccion 4

- Grafo dirigido: Un grafo que modele una ciudad y sus avenidas entre puntos de interes con el sentido de las avenidas

- Grafo no dirigido: cualquiera de los ejemplos de esta clase es no dirigido

## seccion 5

¿Qué operación te parece más importante en un grafo: listar vecinos o preguntar si existe una arista? ¿Por qué?
    - Listar vecinos, pues con esa infromacion se puede confirmar cuantas aristas existen

## seccion 6

¿Por qué conviene que `GrafoListaAdyacencia` y `GrafoMatrizAdyacencia` tengan la misma interfaz?
    Para poder hacer pruebas con mayor facilidad por el polimorfismo

## seccion 7

¿Por qué un `set` ayuda a evitar aristas duplicadas?
        Porque por la naturaleza del set no puede tener elementos repertidos

## seccion 8

¿Qué debe pasar con la matriz cuando agregas un vértice nuevo?
    Se deben actualizar los estados de las entradas y las adyacentes al nuevo vertices

## seccion 9

| Aspecto | Lista de adyacencia | Matriz de adyacencia |
| --- | --- | --- |
| Memoria | Solo almacena nodos y aristas existentes (Eficiente) | Cuadrática; almacena celdas para cada par de nodos (Ineficiente) |
| Facilidad de implementación | Muy intuitiva; un diccionario maneja las llaves dinámicamente | Requiere mapear los nombres a índices numéricos y gestionar una cuadrícula 2D |
| Consultar vecinos | Rápido; iteración directa sobre los vecinos del nodo | Lento; requiere recorrer toda una fila buscando valores `True` |
| Consultar si existe arista | Depende de la estructura interna usada | Inmediato por acceso directo a índices |
| Grafos dispersos | Ideal | Desperdicia demasiada memoria en celdas vacías |
| Grafos densos | Funciona bien, pero tiene más overhead estructural | Ideal; aprovecha el acceso continuo de la memoria |

## seccion 11

¿Por qué conviene poder convertir una implementación propia a una biblioteca externa?
    para poder usarla con mayor facilidad para otros ptoyectos 

## seccion 12 (Pruebas)
```python
def test_pruebas_extras():
    grafo = modulo.GrafoListaAdyacencia()
    grafo.agregar_arista("A","B")
    grafo.agregar_arista("A","Z")
    grafo.agregar_arista("A","S")

    assert not grafo.contiene_arista("A", "C")
    assert grafo.cantidad_aristas() == 3
```


    En mis dos pruebas simultaneas verifique que no haya aristas con vertices inexistentes y tambien que con varios vertices, las aristas creadas son correctas

## seccion 13
Entiendo que para modelar relaciones necesitamos primero sentar bien las baces de como se relacionan nuestro datos y que datos son, serviria contestar primer mentalmente las definiciones; 
    - ¿Que hace que un vertice tenga vecinos? ¿Que es un vertices? ¿Que es una arista?

Y asi podemos empezar a modelar diferentes tipos de datos en grafos

## seccion 14

1. ¿Qué ganamos al modelar relaciones como grafo?
    tenemos mayor control sobre cierta infromacion; como la relacion que hay entre los datos en los vetices
2. ¿Cuándo usarías lista de adyacencia?
    cuando necesite necesite consultar los vecinos de un vertice constantemente
3. ¿Cuándo usarías matriz de adyacencia?
    cuando necesite un panorama general de las aristas creadas
4. ¿Qué puede ocultar una visualización?
    la infromacion menos utiles
5. ¿Qué algoritmo necesitaremos para recorrer el grafo?
    no se