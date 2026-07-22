###    De representar a recorrer.
    En la clase anterior necesitamos solo modelamos los grafos y vimos la informacion que nos puede dar, ahora y con nueva herramienta no solo lo modelamos sino que podemos "pasear" por el grafo y asi ver como fluye o transita la infromacion y con ello tenemos nuevos parametros para otros probelmas
###    Estrategias manuales.

###    BFS.
    Este estrategia se enfoca principalmente en la "profundidad", en agotar un camino e ir a los demas, es muy util cuando necesitas tener una vision rapida sobre un camino hasta el final
###    DFS.
    Esta estrategia se enfoca en abarcar muchos caminos pero de pcoo a poco, yo lo entiendo como un recorrido por capas, cuando terminas una capa avanzas a la siguiente y sigues asi
###    Comparación.
    Ambas estrategias sirven pero cada una sirve para cosas distintas, por ejemplo, BFS se me hace atural para el laberinto, DFS para adquirir mucha infromacion poco a poco (no se me ocurre un ejemplo para DFS)
###   Visualización.
    No la hicimos jaja
###    CSES.
    Para cada problema necesitamos diferentes froma de abordar los grafos que modelamos, pero por ejemplo y el que tengo mas claro
        - El laberinto nosotros lo resolvemos naturalmente a prueba y error, justo como el BFS
###    Pruebas.
    Todas las pruebas buscan que el codigo se comporten de manera esperada y las mias, buscan que el codigo no haga cosas raras con vecinos aislados 
###    Patrón descubierto.
    Necesitamos modelar primero el grafo, entebdner que lo compone y luego entender como pdoemos recorrerlo para que nos ayude a la resolucion de nuestro problema
###    Pregunta abierta.
    ¿Cual es la mas optima forma de recorrer grafos poderados? 