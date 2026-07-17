def test_cero_uno_reconstruye_camino_correctamente():
    grafo = {"A": [("B", 0)], "B": [("C", 1)], "C": []}
    distancias, pred = cero_uno_bfs(grafo, "A")
    assert reconstruir_camino(pred, "C") == ["A", "B", "C"]
    assert reconstruir_camino(pred, "A") == ["A"]
    assert reconstruir_camino(pred, "X") == []

def test_deque_reconstruye_camino_correctamente():
    grafo = {"A": [("B", 0)], "B": [("C", 1)], "C": []}
    distancias, pred = cero_uno_bfs(grafo, "A")
    assert reconstruir_camino(pred, "C") == ["A", "B", "C"]
    assert reconstruir_camino(pred, "A") == ["A"]
    assert reconstruir_camino(pred, "X") == []

def test_cola_reconstruye_camino_correctamente():
    grafo = {"A": [("B", 0)], "B": [("C", 1)], "C": []}
    distancias, pred = cero_uno_bfs(grafo, "A")
    assert reconstruir_camino(pred, "C") == ["A", "B", "C"]
    assert reconstruir_camino(pred, "A") == ["A"]
    assert reconstruir_camino(pred, "X") == []

def test_deque_permite_agregar_y_quitar_varios_valores():
    deque = DequeLigada()
    for valor in ("A", "B", "C"):
        deque.agregar_final(valor)
    assert (deque.primero(), deque.ultimo(), len(deque)) == ("A", "C", 3)
    assert deque.quitar_inicio() == "A"
    assert deque.quitar_final() == "C"
    assert deque.quitar_inicio() == "B"
    assert deque.esta_vacia()

def test_cola_permite_encolar_y_desencolar_varios_valores():
    cola = ColaLigada()
    for valor in ("A", "B", "C"):
        cola.encolar(valor)
    assert cola.primero() == "A"
    assert len(cola) == 3
    assert [cola.desencolar() for _ in range(3)] == ["A", "B", "C"]
    assert cola.esta_vacia()

def test_listas_ligadas_permiten_valores_repetidos():
    cola = ColaLigada()
    deque = DequeLigada()
    for valor in ("A", "A", "B", "B"):
        cola.encolar(valor)
        deque.agregar_final(valor)
    assert [cola.desencolar() for _ in range(4)] == ["A", "A", "B", "B"]
    assert [deque.quitar_inicio() for _ in range(4)] == ["A", "A", "B", "B"]

# aqui aparecen algunos errores de sintaxis pero en el arcchivo pruebas publicas no hay problema para correr las pruebas 