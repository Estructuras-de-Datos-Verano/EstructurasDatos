# Clase 15: Discusión
#### Nombre: Patricio Navarro

## 1. Diferencia entre distancia por aristas y por pesos.
- BFS: Distancia por aristas, regresa el camino más corto en aristas.
- Dijkstra: Distancia por pesos, cada arista representa una distancia y regresa el camino cuya distancia total es la más chica.
## 2. Significado de distancia tentativa.
- Distancia mínima que se conoce hasta un momento dado, porque pueden cambiar conforme avanza el algoritmo.
## 3. Relajación con un ejemplo numérico.
- A -> C = 15 minutos
- A -> B = 4 minutos
- B -> C = 7 minutos
Entonces A -> C = 11 minutos pasando por B.
## 4. Razón para usar min-heap.
- Necesitamos una cola de prioridad, donde la distancia es la prioridad.
## 5. Entrada obsoleta y eliminación perezosa.
- Cuando la nueva candidata es mayor a la distancia que se recorría antes se considera obsoleta y se elimina de la cola.
## 6. Reconstrucción mediante predecesores.
- Cada nodo apunta hacia su predecesor, entonces empezamos haciendo una cadena del destino al origen y la invertimos.
## 7. Complejidad temporal y espacial.
- Temporal: O((V+E)log(V)) donde:
    - V = vértices/nodos
    - E = aristas
    - En el peor de los casos, el algoritmo tiene que visitar todas las ciudades ($V$) y recorrer cada una de las carreteras disponibles ($E$). Cada vez que evaluamos una ruta o encontramos un atajo, interactuamos con nuestra agenda de prioridades (el Heap). Como el Heap se reorganiza automáticamente para darte siempre el nodo más barato, esa reorganización "cuesta" un tiempo de $log V$. Al multiplicar el esfuerzo de recorrer el mapa por el esfuerzo de ordenar la agenda, obtenemos el tiempo total.
- Espacial: O(V+E) con las mismas asignaciones.
    - La memoria total es directamente proporcional al tamaño del mapa. Si sumas el espacio para guardar la red completa ($V + E$), la libreta con las distancias récord ($V$) y la agenda de tareas pendientes ($E$), el consumo global nunca superará el total de ciudades más el total de carreteras juntas: $O(V + E)$.
## 8. Restricción de pesos no negativos.
- Si hubieran pesos negativos la distancia no sería la real sino que se distorsionaría, por lo tanto debe ser no negativa.
## 9. Caso donde BFS falla.
- Cuando cada arista tiene un peso distinto.
## 10. Evidencia de tus pruebas.
- 
```python
def test_distancia_mejora_dos_veces():
   
    grafo = {
        "A": [("E", 20), ("B", 5), ("C", 2)],
        "B": [("E", 10)],
        "C": [("D", 2)],
        "D": [("E", 2)],
        "E": []
    }
    
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["E"] == 6
    
    costo, camino = camino_minimo(grafo, "A", "E")
    assert costo == 6
    assert camino == ["A", "C", "D", "E"]


def test_destino_inalcanzable_contrato():
    
    grafo = {
        "A": [("B", 10)],
        "B": [],
        "X": [("Y", 5)],  
        "Y": []
    }
    
    costo, camino = camino_minimo(grafo, "A", "X")
    
    assert math.isinf(costo), "El costo hacia un nodo inalcanzable debe ser infinito."
    assert camino == [], "El camino hacia un nodo inalcanzable debe ser una lista vacía."


def test_entrada_obsoleta_ruta_directa_costosa():
    
    grafo = {
        "A": [("B", 100), ("C", 1)],
        "B": [],
        "C": [("B", 1)]
    }
    
    costo, camino = camino_minimo(grafo, "A", "B")
    
    assert costo == 2
    assert camino == ["A", "C", "B"]
    
    distancias, predecesores = dijkstra(grafo, "A")
    assert distancias["B"] == 2
    assert predecesores["B"] == "C"
```
## 11. Hallazgo de la revisión técnica.