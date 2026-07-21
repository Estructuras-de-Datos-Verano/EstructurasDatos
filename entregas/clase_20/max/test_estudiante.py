import pytest

from implementacion import (
    PerfilProblema,
    es_aplicable,
    evaluar_propuesta,
    explicar_descarte,
    seleccionar_estrategia,
    validar_perfil,
)


def test_max1():
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    assert es_aplicable("Dijkstra", perfil)
    assert not es_aplicable("BFS", perfil)
    mensaje = explicar_descarte("BFS", perfil)
    assert "Dijkstra" in mensaje or "aristas" in mensaje.lower()


def test_max2():
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    assert es_aplicable("0-1 BFS", perfil)
    assert not es_aplicable("BFS", perfil)


def test_max3():
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    assert es_aplicable("Kruskal", perfil)
    assert not es_aplicable("Dijkstra", perfil)
    mensaje = explicar_descarte("Dijkstra", perfil)
    assert "optimizar" in mensaje.lower() or "camino" in mensaje.lower()


def test_max4():
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    assert es_aplicable("Kahn", perfil)
    assert not es_aplicable("BFS", perfil)
    mensaje = explicar_descarte("BFS", perfil)
    assert "camino" in mensaje.lower() or "optimizar" in mensaje.lower()


def test_max5():
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert decision.estructura is None
    assert decision.advertencia != ""


def test_max6():
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kruskal"
    assert decision.estructura == "Union-Find"


def test_max7():
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "cola")
    assert not valida
    assert len(errores) == 1 
    assert "Estructura incorrecta" in errores[0] or "heap" in errores[0].lower()


def test_max8():
    with pytest.raises(ValueError):
        validar_perfil(PerfilProblema("encontrar_ciclo", True, "sin_pesos"))
    with pytest.raises(ValueError):
        validar_perfil(PerfilProblema("camino_minimo", True, "flotantes"))
    with pytest.raises(TypeError):
        validar_perfil(PerfilProblema("camino_minimo", "Sí", "sin_pesos"))