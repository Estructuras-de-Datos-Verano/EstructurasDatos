import pytest
from implementacion import (
    ColaLigada, DequeLigada, bfs_camino, cero_uno_bfs, camino_cero_uno
)

def test_cola_ligada_fifo():
    # Test: La cola ligada cumple con el orden FIFO.
    c = ColaLigada[str]()
    c.encolar("A")
    c.encolar("B")
    assert len(c) == 2
    assert c.desencolar() == "A"
    assert c.desencolar() == "B"
    assert c.esta_vacia()

def test_cola_ligada_reutilizacion():
    # Test: La cola se puede vaciar y volver a utilizar limpiando extremos.
    c = ColaLigada[str]()
    c.encolar("A")
    c.desencolar()
    assert c.esta_vacia()
    c.encolar("B")
    assert c.primero() == "B"
    assert c.desencolar() == "B"
    assert c.esta_vacia()

def test_deque_operaciones_combinadas():
    # Test: Deque admite operaciones en ambos extremos.
    d = DequeLigada[str]()
    d.agregar_inicio("B")
    d.agregar_final("C")
    d.agregar_inicio("A")
    assert len(d) == 3
    assert d.quitar_inicio() == "A"
    assert d.quitar_final() == "C"
    assert d.quitar_inicio() == "B"
    assert d.esta_vacia()

def test_deque_reutilizacion():
    # Test: La deque se puede vaciar y volver a utilizar correctamente.
    d = DequeLigada[str]()
    d.agregar_inicio("X")
    assert d.quitar_final() == "X"
    assert d.esta_vacia()
    d.agregar_final("Y")
    assert d.quitar_inicio() == "Y"
    assert d.esta_vacia()

def test_bfs_con_ciclo():
    # Test: BFS no entra en bucle infinito ante la presencia de un ciclo.
    grafo = {"A": ["B"], "B": ["C"], "C": ["A", "D"], "D": []}
    camino = bfs_camino(grafo, "A", "D")
    assert camino == ["A", "B", "C", "D"]

def test_bfs_destino_inalcanzable():
    # Test: BFS retorna una lista vacía si no hay conexión al destino.
    grafo = {"A": ["B"], "B": [], "C": ["D"], "D": []}
    camino = bfs_camino(grafo, "A", "D")
    assert camino == []

def test_cero_uno_bfs_ruta_optima():
    # Test: 0-1 BFS prioriza el camino de menor costo sobre menor aristas.
    grafo = {
        "A": [("B", 1), ("C", 0)],
        "C": [("D", 0)],
        "D": [("B", 0)],
        "B": []
    }
    costo, camino = camino_cero_uno(grafo, "A", "B")
    assert costo == 0.0
    assert camino == ["A", "C", "D", "B"]

def test_cero_uno_bfs_peso_invalido():
    # Test: Pesos fuera de 0 y 1 o booleanos lanzan excepciones de contrato.
    grafo_invalido = {"A": [("B", 2)]}
    with pytest.raises(ValueError):
        cero_uno_bfs(grafo_invalido, "A")
    grafo_bool = {"A": [("B", True)]}
    with pytest.raises(TypeError):
        cero_uno_bfs(grafo_bool, "A")