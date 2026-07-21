import pytest
from implementacion import PerfilProblema, evaluar_propuesta, es_aplicable

def test_distingue_bfs_dijkstra():
    "Diferencia camino sin pesos (BFS) de positivos (Dijkstra)."
    perfil = PerfilProblema("camino_minimo", True, "sin_pesos")
    valido, _ = evaluar_propuesta(perfil, "BFS", "cola")
    assert valido

def test_distingue_01bfs_bfs():
    "Diferencia deque 0/1 de cola pura."
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    valido, _ = evaluar_propuesta(perfil, "0-1 BFS", "deque")
    assert valido

def test_distingue_dijkstra_kruskal():
    "Kruskal no es para rutas directas."
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    assert es_aplicable("Kruskal", perfil)

def test_distingue_bfs_kahn():
    "Kahn requiere dirigir precedencias."
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    assert es_aplicable("Kahn", perfil)

def test_pesos_negativos_rechazados():
    "Fuera del alcance estudiado."
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    valido, errores = evaluar_propuesta(perfil, "Dijkstra", "heap")
    assert not valido
    assert "fuera del alcance" in errores[0].lower()

def test_kruskal_pesos_negativos():
    "Kruskal sí tolera negativos para ordenar aristas."
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    assert es_aplicable("Kruskal", perfil)

def test_falla_estructura():
    "Fallo aislado solo en la estructura de datos."
    perfil = PerfilProblema("camino_minimo", True, "sin_pesos")
    valido, errores = evaluar_propuesta(perfil, "BFS", "heap")
    assert not valido

def test_perfil_invalido():
    "Lanza ValueError para vocabulario no soportado."
    with pytest.raises(ValueError):
        PerfilProblema("invento", True, "sin_pesos")
        evaluar_propuesta(PerfilProblema("invento", True, "sin_pesos"), "BFS", "cola")