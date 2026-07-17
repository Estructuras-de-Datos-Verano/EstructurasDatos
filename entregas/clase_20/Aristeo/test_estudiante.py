import pytest
from implementacion import PerfilProblema, seleccionar_estrategia, es_aplicable, explicar_descarte, evaluar_propuesta

def test_distincion_bfs_vs_dijkstra_pesos():
    """1. Distingue entre BFS (sin pesos) y Dijkstra (con pesos generales)"""
    perfil_sin = PerfilProblema("camino_minimo", True, "sin_pesos")
    perfil_con = PerfilProblema("camino_minimo", True, "no_negativos")
    
    assert seleccionar_estrategia(perfil_sin).algoritmo == "BFS"
    assert seleccionar_estrategia(perfil_con).algoritmo == "Dijkstra"
    assert "Dijkstra" in explicar_descarte("BFS", perfil_con)

def test_distincion_01_bfs_vs_bfs():
    """2. Comprueba que pesos 0/1 requieran 0-1 BFS en lugar de un BFS convencional."""
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    assert seleccionar_estrategia(perfil).algoritmo == "0-1 BFS"
    assert not es_aplicable("BFS", perfil)

def test_distincion_dijkstra_vs_kruskal():
    """3. Valida la diferencia entre camino mínimo a origen vs conexión global (MST)."""
    perfil_mst = PerfilProblema("conexion_minima", False, "no_negativos")
    assert seleccionar_estrategia(perfil_mst).algoritmo == "Kruskal"
    assert not es_aplicable("Dijkstra", perfil_mst)

def test_distincion_bfs_vs_kahn():
    """4. Confirma que las dependencias requieran Kahn a pesar de que ambos usen cola."""
    perfil_dep = PerfilProblema("orden_dependencias", True, "sin_pesos")
    assert seleccionar_estrategia(perfil_dep).algoritmo == "Kahn"
    assert "Kahn" in explicar_descarte("BFS", perfil_dep)

def test_pesos_negativos_fuera_del_alcance():
    """5. Los caminos mínimos con pesos negativos deben abortar sin inventar algoritmos."""
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert "pesos negativos" in decision.advertencia

def test_kruskal_con_peso_negativo():
    """6. Kruskal es inmune a los pesos negativos en MST."""
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    assert seleccionar_estrategia(perfil).algoritmo == "Kruskal"

def test_error_solo_de_estructura():
    """7. Detecta fallos donde el algoritmo es correcto pero la estructura es inapropiada."""
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "cola")
    assert not valida
    assert any("heap" in err for err in errores)

def test_perfil_invalido():
    """8. Asegura el robustecimiento frente a vocabularios no contemplados."""
    perfil = PerfilProblema("objetivo_fantasma", True, "sin_pesos")
    with pytest.raises(ValueError):
        seleccionar_estrategia(perfil)