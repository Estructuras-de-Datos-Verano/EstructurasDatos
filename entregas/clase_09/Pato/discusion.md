# Clase 09: Discusión
#### Nombre: Patricio Navarro

1. De secuencias a relaciones.
    - En una secuencia los únicos elementos que se conectan son el actual, su predecesor y su sucesor, y además tiene un órden.
    `predecesor -> actual -> sucesor`
    Mientras tanto, al modelar relaciones, solo te importa que los elementos cumplan cierta condición y no necesariamente importa realmente el órden en que se conecten, tampoco tiene por qué marcar una jerarquía (cosa que en una secuencia sí hay).
2. Problemas CSES.
    - Building Roads: Buscamos encontrar como conectar a n-ciudades con m- carretars de froma qu cualquieras dos ciudades estén conectadas por una carretera. 
        - Los nodos son las ciudades y las aristas las carreteras.
    - Counting Rooms: Buscamos contar los cuartos en un plano de n*m de un edificio.
        - Notamos que los nodos son cada cuadrito de piso y que las aristas son los cuadritos de piso que se conectan.
    - Labyrinth: Buscamos resolver un laberinto llegando de un punto `a` a un punto `b`.
        - Los nodos y las aristas funcionan prácticamente igual que en el de los cuartos.
    - Message Route: Buscamos el mínimo de computadoras para mandar un mensaje.
        - Los nodos son la computadoras y las aristas son la conexión de red.
3. Elección de representación.
    - Grafos, con listas de adyacencias principalmente.
4. Polimorfismo.
    - Grafos con matrices de adyacencias.
5. NetworkX.
    - Una librería que permite modelar y visualizar las relaciones que creamos.
6. Pruebas.
    - ```python
        def test_todo_guardar_visualizacion_grafo():
        grafo = modulo.GrafoListaAdyacencia()
        grafo.agregar_arista("A", "B")
        grafo.agregar_arista("B", "C")
        modulo.guardar_visualizacion_grafo(grafo, "grafo_ejemplo.png")
        assert os.path.exists("grafo_ejemplo.png"), "No se generó el archivo de visualización."
        def test_todo_construir_grafo_ejemplo():
        grafo = modulo.construir_grafo_ejemplo()
        assert grafo.contiene_arista("A", "B")
        assert grafo.contiene_arista("B", "C")
        assert grafo.contiene_arista("C", "D")
        assert grafo.contiene_arista("D", "A")
        assert grafo.contiene_arista("C", "E")
        ```

7. Patrón descubierto.
    - Es un modelo de relaciones que se usa cuando queremos ver como se pueden conectar ciertas cosas a partir de relaciones o de condiciones, en este patrón los objetos se pueden ver como nodos y las condiciones que los unen son las aristas. Dependiendo el sentido de las rlaciones son dirigidas o no y dependiendo el valor que les quieras asignar son ponderadas o no.
8. Pregunta abierta.
    - ¿Una vez que tenemos todo estructurado en relaciones, que operaciones son las que más se optimizan para trabajar con los datos?