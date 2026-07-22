"""Pruebas públicas de listas ligadas, BFS y 0-1 BFS."""

from math import inf, isinf

import pytest

from implementacion import (
    ColaLigada,
    DequeLigada,
    NodoDoble,
    NodoSimple,
    bfs_camino,
    bfs_predecesores,
    camino_cero_uno,
    cero_uno_bfs,
    reconstruir_camino,
)


def test_exporta_los_dos_tipos_de_nodo():
    assert NodoSimple(3).valor == 3
    assert NodoDoble("A").valor == "A"


def test_cola_comienza_vacia_y_admite_valores_repetidos():
    cola = ColaLigada()
    assert cola.esta_vacia() and len(cola) == 0
    cola.encolar("A")
    cola.encolar("A")
    assert cola.primero() == "A" and len(cola) == 2
    assert [cola.desencolar(), cola.desencolar()] == ["A", "A"]


def test_cola_respeta_fifo_y_tamano():
    cola = ColaLigada()
    for valor in ("A", "B", "C"):
        cola.encolar(valor)
    assert cola.primero() == "A"
    assert len(cola) == 3
    assert [cola.desencolar() for _ in range(3)] == ["A", "B", "C"]
    assert cola.esta_vacia()


def test_cola_vacia_falla_y_puede_reutilizarse():
    cola = ColaLigada()
    with pytest.raises(IndexError):
        cola.primero()
    with pytest.raises(IndexError):
        cola.desencolar()
    cola.encolar(1)
    assert cola.desencolar() == 1
    cola.encolar(2)
    assert (cola.primero(), cola.desencolar(), len(cola)) == (2, 2, 0)


def test_cola_restaurada_no_conserva_extremos():
    cola = ColaLigada()
    cola.encolar("único")
    retirado = cola._frente
    cola.desencolar()
    assert cola._frente is None and cola._final is None
    assert retirado is not None and retirado.siguiente is None


def test_deque_opera_por_ambos_extremos():
    deque = DequeLigada()
    deque.agregar_final("B")
    deque.agregar_inicio("A")
    deque.agregar_final("C")
    assert (deque.primero(), deque.ultimo(), len(deque)) == ("A", "C", 3)
    assert deque.quitar_inicio() == "A"
    assert deque.quitar_final() == "C"
    assert deque.quitar_inicio() == "B"
    assert deque.esta_vacia()


def test_deque_comienza_vacia_y_admite_valores_repetidos():
    deque = DequeLigada()
    assert deque.esta_vacia() and len(deque) == 0
    deque.agregar_inicio("A")
    deque.agregar_final("A")
    assert deque.primero() == deque.ultimo() == "A"
    assert deque.quitar_inicio() == deque.quitar_final() == "A"


def test_deque_vacia_falla_y_puede_reutilizarse():
    deque = DequeLigada()
    for operacion in (deque.primero, deque.ultimo, deque.quitar_inicio, deque.quitar_final):
        with pytest.raises(IndexError):
            operacion()
    deque.agregar_inicio(1)
    assert deque.quitar_final() == 1
    deque.agregar_final(2)
    assert deque.quitar_inicio() == 2


def test_deque_desconecta_nodos_retirados():
    deque = DequeLigada()
    for valor in (1, 2, 3):
        deque.agregar_final(valor)
    primero = deque._inicio
    ultimo = deque._final
    deque.quitar_inicio()
    deque.quitar_final()
    assert primero is not None and primero.anterior is None and primero.siguiente is None
    assert ultimo is not None and ultimo.anterior is None and ultimo.siguiente is None
    assert deque._inicio is deque._final
    assert deque._inicio is not None
    assert deque._inicio.anterior is None and deque._inicio.siguiente is None


def grafo_bfs():
    return {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["B", "C", "F"],
        "F": ["D", "E"],
    }


def test_bfs_conserva_orden_de_vecinos_y_camino_minimo():
    predecesores = bfs_predecesores(grafo_bfs(), "A")
    assert predecesores == {
        "A": None, "B": "A", "C": "A", "D": "B", "E": "B", "F": "D"
    }
    assert bfs_camino(grafo_bfs(), "A", "F") == ["A", "B", "D", "F"]


def test_bfs_identidad_camino_directo_y_direccion():
    grafo = {"A": ["B"], "B": []}
    assert bfs_camino(grafo, "A", "A") == ["A"]
    assert bfs_camino(grafo, "A", "B") == ["A", "B"]
    assert bfs_camino(grafo, "B", "A") == []


def test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none():
    grafo = {"A": ["B"], "B": ["C"], "C": ["A"], "X": []}
    pred = bfs_predecesores(grafo, "A")
    assert pred == {"A": None, "B": "A", "C": "B", "X": None}
    assert bfs_camino(grafo, "A", "X") == []


def test_bfs_incluye_vecino_implicito_y_no_muta_entrada():
    grafo = {"A": ["B"]}
    copia = {nodo: vecinos.copy() for nodo, vecinos in grafo.items()}
    assert bfs_camino(grafo, "A", "B") == ["A", "B"]
    assert grafo == copia and "B" not in grafo


def test_bfs_rechaza_origen_o_destino_ausentes():
    with pytest.raises(KeyError, match="origen"):
        bfs_predecesores({"A": []}, "X")
    with pytest.raises(KeyError, match="destino"):
        bfs_camino({"A": []}, "A", "X")


def test_reconstruir_cubre_identidad_inalcanzable_y_ciclo():
    assert reconstruir_camino({"A": None}, "A", "A") == ["A"]
    assert reconstruir_camino({"A": None, "X": None}, "A", "X") == []
    with pytest.raises(ValueError, match="ciclo"):
        reconstruir_camino({"A": None, "B": "C", "C": "B"}, "A", "B")


def grafo_01():
    return {
        "A": [("B", 0), ("C", 1)],
        "B": [("D", 0), ("E", 1)],
        "C": [("D", 0)],
        "D": [("F", 1)],
        "E": [("F", 0)],
        "F": [],
    }


def test_cero_uno_bfs_calcula_distancias_y_predecesores():
    distancias, pred = cero_uno_bfs(grafo_01(), "A")
    assert distancias == {"A": 0, "B": 0, "C": 1, "D": 0, "E": 1, "F": 1}
    assert pred["B"] == "A" and pred["D"] == "B" and pred["F"] == "D"
    assert camino_cero_uno(grafo_01(), "A", "F") == (1, ["A", "B", "D", "F"])


def test_cero_uno_prefiere_mas_aristas_si_cuestan_menos():
    grafo = {"A": [("X", 1), ("B", 0)], "B": [("C", 0)], "C": [("X", 0)], "X": []}
    assert camino_cero_uno(grafo, "A", "X") == (0, ["A", "B", "C", "X"])


def test_cero_uno_con_solo_pesos_cero():
    grafo = {"A": [("B", 0)], "B": [("C", 0)], "C": []}
    assert camino_cero_uno(grafo, "A", "C") == (0, ["A", "B", "C"])


def test_cero_uno_con_solo_pesos_uno():
    grafo = {"A": [("B", 1)], "B": [("C", 1)], "C": []}
    assert camino_cero_uno(grafo, "A", "C") == (2, ["A", "B", "C"])


def test_cero_uno_actualiza_una_mejora_posterior():
    grafo = {"A": [("X", 1), ("B", 0)], "B": [("C", 0)], "C": [("X", 0)], "X": []}
    distancias, pred = cero_uno_bfs(grafo, "A")
    assert distancias["X"] == 0 and pred["X"] == "C"


def test_cero_uno_identidad_e_inalcanzable():
    grafo = {"A": [], "X": []}
    assert camino_cero_uno(grafo, "A", "A") == (0, ["A"])
    costo, camino = camino_cero_uno(grafo, "A", "X")
    assert isinf(costo) and camino == []


def test_cero_uno_incluye_vecino_implicito_y_no_muta_entrada():
    grafo = {"A": [("B", 0)]}
    copia = {nodo: aristas.copy() for nodo, aristas in grafo.items()}
    distancias, _ = cero_uno_bfs(grafo, "A")
    assert distancias == {"A": 0, "B": 0}
    assert grafo == copia and "B" not in grafo


@pytest.mark.parametrize("peso", [True, False, 0.0, "1", None])
def test_cero_uno_rechaza_peso_de_tipo_incorrecto(peso):
    with pytest.raises(TypeError, match="entero 0 o 1"):
        cero_uno_bfs({"A": [("B", peso)]}, "A")


@pytest.mark.parametrize("peso", [-1, 2, 8])
def test_cero_uno_rechaza_entero_fuera_del_dominio(peso):
    with pytest.raises(ValueError, match="0 o 1"):
        cero_uno_bfs({"A": [("B", peso)]}, "A")


def test_cero_uno_rechaza_forma_y_nodos_invalidos():
    with pytest.raises(ValueError, match="dos elementos"):
        cero_uno_bfs({"A": [("B", 0, "extra")]}, "A")
    with pytest.raises(TypeError, match="vecino"):
        cero_uno_bfs({"A": [(3, 0)]}, "A")
    with pytest.raises(KeyError, match="origen"):
        cero_uno_bfs({"A": []}, "X")
    with pytest.raises(KeyError, match="destino"):
        camino_cero_uno({"A": []}, "A", "X")


def test_constante_infinito_es_compatible_con_contrato():
    distancias, pred = cero_uno_bfs({"A": [], "X": []}, "A")
    assert distancias["X"] == inf and pred["X"] is None


# TODO: agrega pruebas de secuencias largas y alternadas en ambas estructuras.
# TODO: diseña un grafo 0-1 donde una distancia sea mejorada después de descubrirse.
