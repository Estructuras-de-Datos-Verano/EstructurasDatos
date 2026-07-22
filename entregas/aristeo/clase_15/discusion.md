# Discusión Teórica — Práctica 15
### 1. Diferencia entre distancia por aristas y por pesos
La distancia por aristas mide únicamente la cantidad de pasos entre nodos interconectados.
La distancia por pesos calcula la suma algebraica total de los valores, básicamente es el coste real de recorrer la distancia.

### 2. Significado de distancia tentativa
Es valor provicional para encontrar el camino más corto o con menor costo.

### 3. Relajación con un ejemplo numérico
La relajación es el acto de actualizar la distancia tentativa de un nodo si encuentras un camino más corto para llegar a él.

### 4. Razón para usar min-heap
La razón principal para usar un min-heap en algoritmos de rutas es la eficiencia en tiempo.

### 5. Entrada obsoleta y eliminación perezosa
Una entrada obsoleta es cuando se realiza una relajación, se descubres un camino más corto hacia un nodo que ya estaba en el min-heap y como no se puede modificar la distancia del elemento existente, la solución es insertar el mismo nodo otra vez, pero con la nueva distancia menor
La eliminacion perezoza es cuando en lugar de perder tiempo buscando y borrando inmediatamente la entrada obsoleta dentro del árbol, el algoritmo decide no hacer nada en ese momento, la deja ahí y lidia con ella después.

### 6. Reconstrucción mediante predecesores
La reconstrucción mediante predecesores es el proceso final de un algoritmo de rutas para obtener el camino exacto paso a paso.

### 7. Complejidad temporal y espacial
* **Temporal:** O((V+E)logV) utilizando listas de adyacencia combinadas con un min-heap (`heapq`), debido a que cada arista se relaja a lo sumo una vez y cada actualización/extracción del heap cuesta proporcionalmente al logaritmo de los vértices.
* **Espacial:** O(V + E) para albergar las listas del grafo, el diccionario de distancias, mapeo de predecesores y el tamaño máximo de elementos coexistiendo dentro del heap.

### 8. Restricción de pesos no negativos
La restricción de pesos no negativos es un requisito obligatorio para que el algoritmo de Dijkstra funcione correctamente. Significa que ninguna conexión (arista) en el grafo puede tener un valor menor que cero (costo, tiempo o distancia negativos).

### 9. Caso donde BFS falla
Falla cuando se intenta encontrar la ruta más corta en un grafo donde las aristas tienen pesos diferentes.

### 10. Evidencia de tus pruebas
``` python
def test_distancia_mejora_multiples_veces():
    """1. Protege el caso donde un nodo mejora su costo más de una vez dejando

    entradas obsoletas en el heap que deben ser ignoradas de forma perezosa.
    """
    grafo = {
        "A": [("B", 100), ("C", 10)],
        "C": [("B", 40), ("D", 5)],
        "D": [("B", 5)],
        "B": []
    }
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 20
    assert predecesores["B"] == "D"
    assert reconstruir_camino(predecesores, "A", "B") == ["A", "C", "D", "B"]


def test_destino_inalcanzable():
    """2. Protege el contrato ante destinos completamente aislados o inalcanzables.

    Se espera que la distancia sea infinito y el camino devuelto sea vacío [].
    """
    grafo = {
        "A": [("B", 5)],
        "B": [],
        "Z": []  
    }
    costo, camino = camino_minimo(grafo, "A", "Z")
    assert math.isinf(costo)
    assert camino == []


def test_ruta_indirecta_supera_directa_costosa():
    """3. Protege la lógica codiciosa contra BFS. Una arista directa masiva

    debe ser descartada a favor de una ruta con múltiples aristas pero menor costo total.
    """
    grafo = {
        "A": [("B", 10), ("D", 50)],
        "B": [("C", 10)],
        "C": [("D", 10)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 30
    assert camino == ["A", "B", "C", "D"]
```

### 11. Hallazgo de la revisión técnica