# Discusión

Pasar de secuencias a relaciones permitió ver que muchos problemas no se resuelven solo con listas o diccionarios, sino con estructuras que representan conexiones entre elementos. En este caso, los grafos son una forma natural de modelar relaciones, ya sea entre personas, tareas, nodos o estados.

La elección de representación depende del uso que se le vaya a dar. La lista de adyacencia es más simple y eficiente para recorrer vecinos en grafos dispersos, mientras que la matriz de adyacencia es útil cuando se necesita consultar rápidamente si existe una conexión entre dos vértices. Al implementar ambas bajo una interfaz común, se mostró el valor del polimorfismo: el mismo código puede trabajar con cualquiera de las dos representaciones.

NetworkX facilitó la comparación entre la implementación propia y una biblioteca estándar, además de permitir generar una visualización del grafo. Esto ayudó a verificar que la estructura creada fuera consistente y que las aristas se estaban agregando correctamente.

En cuanto a las pruebas, fue importante comprobar no solo que el grafo se construyera, sino también que las operaciones básicas fueran correctas ante casos como aristas duplicadas, vértices aislados y comparación entre implementaciones. El patrón descubierto fue que la lógica de negocio puede mantenerse igual aunque cambie la representación interna, lo que hace más flexible y mantenible el diseño.
