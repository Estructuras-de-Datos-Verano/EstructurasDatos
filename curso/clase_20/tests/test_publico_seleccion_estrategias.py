"""Pruebas públicas de la Clase 20; se ejecutan contra implementacion.py."""

from __future__ import annotations

import pytest

from implementacion import (
    DecisionAlgoritmica,
    PerfilProblema,
    es_aplicable,
    evaluar_propuesta,
    explicar_descarte,
    seleccionar_estrategia,
    validar_perfil,
)


@pytest.mark.parametrize(
    ("perfil", "algoritmo", "estructura", "operacion", "complejidad"),
    [
        (PerfilProblema("camino_minimo", False, "sin_pesos"), "BFS", "cola", "capas", "O(V+E)"),
        (PerfilProblema("camino_minimo", True, "cero_uno"), "0-1 BFS", "deque", "0/1", "O(V+E)"),
        (PerfilProblema("camino_minimo", True, "no_negativos"), "Dijkstra", "heap", "distancia", "log V"),
        (PerfilProblema("conexion_minima", False, "no_negativos"), "Kruskal", "Union-Find", "componentes", "E log E"),
        (PerfilProblema("orden_dependencias", True, "sin_pesos"), "Kahn", "cola + grados de entrada", "grado de entrada cero", "O(V+E)"),
    ],
)
def test_selecciones_fundamentales(perfil, algoritmo, estructura, operacion, complejidad):
    decision = seleccionar_estrategia(perfil)
    assert isinstance(decision, DecisionAlgoritmica)
    assert decision.algoritmo == algoritmo
    assert decision.estructura == estructura
    assert operacion in decision.operacion_dominante
    assert complejidad in decision.complejidad
    assert decision.advertencia == ""


def test_bfs_admite_grafo_dirigido_y_no_dirigido():
    assert seleccionar_estrategia(PerfilProblema("camino_minimo", True, "sin_pesos")).algoritmo == "BFS"
    assert seleccionar_estrategia(PerfilProblema("camino_minimo", False, "sin_pesos")).algoritmo == "BFS"


def test_kruskal_admite_pesos_negativos():
    decision = seleccionar_estrategia(PerfilProblema("conexion_minima", False, "incluye_negativos"))
    assert decision.algoritmo == "Kruskal"


@pytest.mark.parametrize(
    "perfil",
    [
        PerfilProblema("camino_minimo", True, "incluye_negativos"),
        PerfilProblema("conexion_minima", True, "no_negativos"),
        PerfilProblema("conexion_minima", False, "sin_pesos"),
        PerfilProblema("orden_dependencias", False, "sin_pesos"),
        PerfilProblema("orden_dependencias", True, "no_negativos"),
    ],
)
def test_reconoce_fuera_del_alcance_sin_inventar_algoritmo(perfil):
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert decision.estructura is None
    assert decision.complejidad is None
    assert decision.advertencia


@pytest.mark.parametrize(
    "perfil",
    [
        PerfilProblema("otro", True, "sin_pesos"),
        PerfilProblema("camino_minimo", True, "decimales"),
    ],
)
def test_rechaza_vocabulario_desconocido(perfil):
    with pytest.raises(ValueError):
        validar_perfil(perfil)


@pytest.mark.parametrize(
    "perfil",
    [
        None,
        {"objetivo": "camino_minimo"},
        PerfilProblema(1, True, "sin_pesos"),
        PerfilProblema("camino_minimo", 1, "sin_pesos"),
        PerfilProblema("camino_minimo", True, 0),
    ],
)
def test_rechaza_tipos_invalidos(perfil):
    with pytest.raises(TypeError):
        validar_perfil(perfil)


def test_es_aplicable_compara_con_el_contrato_completo():
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    assert es_aplicable("0-1 BFS", perfil)
    assert not es_aplicable("BFS", perfil)
    assert not es_aplicable("Dijkstra", perfil)


def test_explicar_descarte_nombra_limite_y_recomendacion():
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    texto = explicar_descarte("BFS", perfil)
    assert "número de aristas" in texto
    assert "Dijkstra" in texto


def test_explicar_algoritmo_correcto_confirma_operacion():
    texto = explicar_descarte("Kahn", PerfilProblema("orden_dependencias", True, "sin_pesos"))
    assert "sí aplica" in texto and "grado de entrada cero" in texto


def test_evaluar_propuesta_correcta():
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    assert evaluar_propuesta(perfil, "Kruskal", "Union-Find") == (True, [])


def test_evaluar_propuesta_detecta_algoritmo_y_estructura():
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "BFS", "cola")
    assert not valida and len(errores) == 2
    assert any("Dijkstra" in error for error in errores)
    assert any("heap" in error for error in errores)


def test_evaluar_propuesta_fuera_de_alcance_no_la_acepta():
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "heap")
    assert not valida and "pesos negativos" in errores[0]


@pytest.mark.parametrize("algoritmo", ["Bellman-Ford", "A*", "", 3])
def test_rechaza_algoritmo_no_estudiado_o_tipo_invalido(algoritmo):
    perfil = PerfilProblema("camino_minimo", True, "sin_pesos")
    excepcion = TypeError if not isinstance(algoritmo, str) else ValueError
    with pytest.raises(excepcion):
        es_aplicable(algoritmo, perfil)


def test_perfil_y_decision_son_inmutables():
    perfil = PerfilProblema("camino_minimo", False, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    with pytest.raises(Exception):
        perfil.objetivo = "otro"
    with pytest.raises(Exception):
        decision.algoritmo = "otro"
