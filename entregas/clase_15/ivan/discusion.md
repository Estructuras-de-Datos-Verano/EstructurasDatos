# Discusion.md - José Iván Reyna Blanco
1. Diferencia entre distancia por aristas y por pesos.
La de pesos es acumulativa y requiere "simular" recorrer cualquier camino.
2. Significado de distancia tentativa.
La distancia a otro nodo mediante un camino candidato, es decir, que aún no ha sido probado como el definitivo de menor longitud. Es la menor hasta el momento.
3. Relajación con un ejemplo numérico.
Extracción: (10, E). Actual: (11, E). Entonces se elige (10, E) y se añade al heap. 
4. Razón para usar min-heap.
En este problema permite darle prioridad de procesar caminos en órden de distancias (con peso), lo que permite probar de forma simultánea las distancias y decidir cuales dejar/quitar usando heappop() y heappush().
5. Entrada obsoleta y eliminación perezosa.
Una entrada obsoleta es aquella tupla (distancia, nodo) cuya distancia es mayor que la de un camino que ya se procesó. En ese caso, la eliminación perezosa es simplemente ignorar la entrada en vez de meterla al heap. 
6. Reconstrucción mediante predecesores.
Se construye una cadena de predecesores con un diccionario de los mismos de tipo {padre : hijo}. Para ver el camino hasta ahí, invertimos la lista.
7. Complejidad temporal y espacial.
O(V+E)\log(V)
8. Restricción de pesos no negativos.
Tener pesos negativos crea caminos alternativos que pueden partir de una entrada originalmente obsoleta que ya fue ignorada, entonces rompe el órden del heap. 
9. Caso donde BFS falla.
Cuando lo más lejos a lo ancho es de mayor peso.
10. Evidencia de tus pruebas.
``` text
def test_camino_mejora_dos_veces():
    """
    Prueba el camino mínimo con un grafo donde el camino más corto mejora dos veces antes de llegar al destino.
    """
    grafo = {"A": [("B", 5), ("C", 1)], 
             "B": [("C", 1)], 
             "C": []}
    costo, camino = camino_minimo(grafo, "A", "B")
    assert costo == 5
    assert camino == ["A", "B"]

def test_destino_inalcanzable():
    """
    Prueba el camino mínimo con un grafo donde el destino es inalcanzable.
    """
    grafo = {"A": [("B", 2)], "B": [], "X": []}
    costo, camino = camino_minimo(grafo, "A", "X")
    assert costo == float("inf")
    assert camino == []

def test_entrada_obsoleta_con_ruta_directa_costosa():
    """
    Prueba el camino mínimo con un grafo donde hay una ruta directa costosa y una ruta más barata indirecta.
    """
    grafo = {"A": [("B", 10), ("C", 1)], 
             "B": [("D", 1)], 
             "C": [("D", 1)], 
             "D": []}
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 2
    assert camino == ["A", "C", "D"]
```
11. Hallazgo de la revisión técnica.
No sé que poner aquí. El pytest ejecutó todas las pruebas de forma efectiva. 