def test_cola_admite_valores_numericos_y_none():
    # Variante de test_cola_comienza_vacia_y_admite_valores_repetidos
    cola = ColaLigada()
    assert cola.esta_vacia() and len(cola) == 0
    cola.encolar(42)
    cola.encolar(None)
    assert cola.primero() == 42 and len(cola) == 2
    assert [cola.desencolar(), cola.desencolar()] == [42, None]


def test_cola_respeta_fifo_con_enteros():
    # Variante de test_cola_respeta_fifo_y_tamano
    cola = ColaLigada()
    for valor in (10, 20, 30):
        cola.encolar(valor)
    assert cola.primero() == 10
    assert len(cola) == 3
    assert [cola.desencolar() for _ in range(3)] == [10, 20, 30]
    assert cola.esta_vacia()


def test_deque_opera_por_ambos_extremos_numeros():
    # Variante de test_deque_opera_por_ambos_extremos
    deque = DequeLigada()
    deque.agregar_final(200)
    deque.agregar_inicio(100)
    deque.agregar_final(300)
    assert (deque.primero(), deque.ultimo(), len(deque)) == (100, 300, 3)
    assert deque.quitar_inicio() == 100
    assert deque.quitar_final() == 300
    assert deque.quitar_inicio() == 200
    assert deque.esta_vacia()


def test_deque_comienza_vacia_con_booleanos():
    # Variante de test_deque_comienza_vacia_y_admite_valores_repetidos
    deque = DequeLigada()
    assert deque.esta_vacia() and len(deque) == 0
    deque.agregar_inicio(True)
    deque.agregar_final(True)
    assert deque.primero() == deque.ultimo() is True
    assert deque.quitar_inicio() == deque.quitar_final() is True


def test_bfs_camino_lineal_largo():
    # Variante de test_bfs_identidad_camino_directo_y_direccion
    grafo = {"1": ["2"], "2": ["3"], "3": []}
    assert bfs_camino(grafo, "1", "1") == ["1"]
    assert bfs_camino(grafo, "1", "3") == ["1", "2", "3"]
    assert bfs_camino(grafo, "3", "1") == []


def test_bfs_ignora_nodos_aislados():
    # Variante de test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none
    grafo = {"N1": ["N2"], "N2": ["N3"], "N3": [], "Aislado": []}
    pred = bfs_predecesores(grafo, "N1")
    assert pred == {"N1": None, "N2": "N1", "N3": "N2", "Aislado": None}
    assert bfs_camino(grafo, "N1", "Aislado") == []


def test_cero_uno_bfs_calcula_distancias_y_predecesores_lineal():
    # Variante de test_cero_uno_bfs_calcula_distancias_y_predecesores
    grafo = {
        "N1": [("N2", 1)],
        "N2": [("N3", 0)],
        "N3": [],
    }
    distancias, pred = cero_uno_bfs(grafo, "N1")
    assert distancias == {"N1": 0, "N2": 1, "N3": 1}
    assert pred["N2"] == "N1" and pred["N3"] == "N2"
    assert camino_cero_uno(grafo, "N1", "N3") == (1, ["N1", "N2", "N3"])


def test_cero_uno_con_solo_pesos_cero_alternativo():
    # Variante de test_cero_uno_con_solo_pesos_cero
    grafo = {"X": [("Y", 0)], "Y": [("Z", 0)], "Z": []}
    assert camino_cero_uno(grafo, "X", "Z") == (0, ["X", "Y", "Z"])