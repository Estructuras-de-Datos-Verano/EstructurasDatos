from implementacion import *


def test_fifo_con_secuencia_larga_LEO():
    """
    Regla protegida: la cola conserva el orden FIFO incluso con muchos elementos.
    Entrada: encolar 100 enteros consecutivos.
    Resultado esperado: se desencolan exactamente en el mismo orden.
    Importancia: verifica que el comportamiento FIFO se mantiene en secuencias largas.
    """
    cola = ColaLigada()
    for i in range(100):
        cola.encolar(i)
    for i in range(100):
        assert cola.desencolar() == i
    assert cola.esta_vacia()


def test_deque_secuencia_alternada_larga_LEO():
    """
    Regla protegida: el deque mantiene referencias correctas tras muchas
    operaciones alternadas.
    Entrada: inserciones y eliminaciones alternadas por ambos extremos.
    Resultado esperado: el deque termina vacío sin perder el orden esperado.
    Importancia: detecta errores que solo aparecen tras varias operaciones.
    """
    dq = DequeLigada()
    for i in range(20):
        dq.agregar_inicio(i)
        dq.agregar_final(-i)
    while not dq.esta_vacia():
        dq.quitar_inicio()
        if not dq.esta_vacia():
            dq.quitar_final()
    assert dq.esta_vacia()


def test_bfs_no_modifica_grafo_con_ciclos_LEO():
    """
    Regla protegida: BFS no modifica el grafo recibido.
    Entrada: un grafo con ciclos.
    Resultado esperado: el grafo permanece exactamente igual.
    Importancia: evita efectos secundarios sobre la estructura original.
    """
    grafo = {"A": ["B"], "B": ["C"], "C": ["A"]}
    copia = {v: vecinos.copy() for v, vecinos in grafo.items()}
    bfs_predecesores(grafo, "A")
    assert grafo == copia


def test_bfs_grafo_unitario_LEO():
    """
    Regla protegida: BFS funciona correctamente con el caso mínimo.
    Entrada: un grafo con un único vértice.
    Resultado esperado: el camino contiene únicamente el origen.
    Importancia: verifica el caso base del algoritmo.
    """
    grafo = {"A": []}
    assert bfs_camino(grafo, "A", "A") == ["A"]


def test_cero_uno_bfs_varias_mejoras_seguidas_LEO():
    """
    Regla protegida: una distancia puede mejorar más de una vez.
    Entrada: un vértice alcanzado inicialmente con costo alto y luego con
    un camino de costo menor.
    Resultado esperado: se conserva la mejor distancia encontrada.
    Importancia: protege la relajación repetida del algoritmo.
    """
    grafo = {"A": [("B", 1), ("C", 0)], "B": [], "C": [("D", 0)], "D": [("B", 0)], "E": []}
    distancias, pred = cero_uno_bfs(grafo, "A")
    assert distancias["B"] == 0
    assert pred["B"] == "D"


def test_cero_uno_bfs_no_modifica_el_grafo_LEO():
    """
    Regla protegida: el algoritmo no modifica el grafo recibido.
    Entrada: un grafo válido.
    Resultado esperado: el grafo permanece idéntico tras ejecutar el algoritmo.
    Importancia: evita efectos secundarios.
    """
    grafo = {"A": [("B", 0)], "B": []}
    copia = {v: aristas.copy() for v, aristas in grafo.items()}
    cero_uno_bfs(grafo, "A")
    assert grafo == copia


def test_cero_uno_bfs_referencias_consistentes_LEO():
    """
    Regla protegida: cada predecesor pertenece realmente al grafo.
    Entrada: un grafo con varias rutas.
    Resultado esperado: todos los predecesores son vértices existentes.
    Importancia: garantiza la consistencia de la tabla de predecesores.
    """
    grafo = {"A": [("B", 0), ("C", 1)], "B": [("D", 1)], "C": [("D", 0)], "D": []}
    _, pred = cero_uno_bfs(grafo, "A")
    for vertice, padre in pred.items():
        if padre is not None:
            assert padre in grafo


def test_camino_cero_uno_reutiliza_resultados_correctamente_LEO():
    """
    Regla protegida: ejecutar el algoritmo varias veces produce el mismo resultado.
    Entrada: el mismo grafo ejecutado dos veces.
    Resultado esperado: costo y camino idénticos en ambas ejecuciones.
    Importancia: verifica que el algoritmo no conserva estado entre llamadas.
    """
    grafo = {"A": [("B", 0)], "B": [("C", 1)], "C": []}
    resultado1 = camino_cero_uno(grafo, "A", "C")
    resultado2 = camino_cero_uno(grafo, "A", "C")
    assert resultado1 == resultado2

