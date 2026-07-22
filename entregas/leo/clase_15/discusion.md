# Discusión clase 15 - Leonardo Daniel Arenas Serafín

## 1. Diferencia entre distancia por aristas y por pesos.
La distancia por aristas se toma en cuenta cuando todas las aristas tienen un mismo costo unitario predeterminado o normaliado, en cambio por pesos, cad arista tiene un costo propio y el costo no es proporcional al número de aristas.

## 2. Significado de distancia tentativa.
Esto signfica que al hacer el algoritmo, no se llega a una distancia definitiva luego luego, sino que uno mientras va avanzando va viendo cuál es el camino más óptimo y con base en ello sigue midiendo para podr llegar a una distancia definitiva.

## 3. Relajación con un ejemplo numérico.
        A ---2---B
        |      /
        1    2
        |  /
        C

En este ejemplo, tenemos costo de 0 al iniciar en A y es la única opción, por lo que hacemos relajación para ver cuál es el mejor camino a B. Para ir directamente a B nos cuesta 2 e ir C nos cuesta 1, por lo que la distancia óptima tentativa es (1,C). Entonces tomamos este camino y volvemos a hacer relajación, vemos que de C a B tenemos costo de 2, que al final nos daría 3, por lo que el camino óptimo es A->B pues tiene el menor costo: 2.

## 4. Razón para usar min-heap.
Se usa porque nosotros queremos encontrar el camino más óptimo, el cual es el del costo mínimo, por lo que usamos MinHeap para poder acceder a este mínimo, además que es muy útil al trabajar con las distancias tentativas.

## 5. Entrada obsoleta y eliminación perezosa.
La entrada obsoleta se da cuando no tenemos más camino conectado por aristas, por lo que no se puede llegar a ninguna parte. La eliminación perezosa es que cuando tenemos un camino muy costoso, en vez de eliminarlo de la lista, simplemente lo ignoramos para evitar futuros errores y complicaciones

## 6. Reconstrucción mediante predecesores.
La función predecesores te dice de donde vino el nodo actual, de esta forma el camino se construye de adelante hacia atrás. Sin embargo esto puede traer problemas de ciclos o que los nodos no vengan del origen, por lo que esto debemos evitarlo en la realización del código

## 7. Complejidad temporal y espacial.
Este algoritmo no tiene una complejidad en términos de recursos temporales ni espaciales porque nunca estamos recorriendo el grafo, sino que tiene una complejidad relacionda con los costos.

## 8. Restricción de pesos no negativos.
Tiene la restricción de que no puede haber costos negativos, ya que el algoritmo le da prioridad a los caminos encontrados como más óptimos, el problema con pesos negaivos es que un camino que al inicio pueda ser costoso, con pesos negativos se puede volver mucho más óptimos que los demás, pero como al inicio no tiene prioridad por ser costoso, no se descubriría este camino.

## 9. Caso donde BFS falla.
Falla cuando se deja de trabajar con costos unitarios o normalizados y se trabaja solo con costos, pues así no tenemos prioridades.

## 10. Evidencia de tus pruebas.
Yo implementé las siguientes pruebas: test_distancia_mejora_y_descarta_entrada_obsoleta_LEO(), test_destino_inalcanzable_LEO(), test_ruta_indirecta_es_mejor_que_directa_LEO() y las 3 pasaron.

## 11. Hallazgo de la revisión técnica.

