def test_estudiante_bfs_vs_dijkstra():
    
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Dijkstra"
    assert not es_aplicable("BFS", perfil)


def test_estudiante_cero_uno_bfs_vs_bfs():
    
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "0-1 BFS"
    assert decision.estructura == "deque"


def test_estudiante_dijkstra_vs_kruskal():
    
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kruskal"
    assert not es_aplicable("Dijkstra", perfil)


def test_estudiante_bfs_vs_kahn():
    
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kahn"
    assert "grados de entrada" in decision.estructura


def test_estudiante_pesos_negativos_fuera_alcance():
    
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert len(decision.advertencia) > 0


def test_estudiante_kruskal_con_peso_negativo():
    
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kruskal"


def test_estudiante_error_solo_estructura():
   
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "cola")
    assert not valida
    assert any("heap" in error or "Estructura" in error for error in errores)


def test_estudiante_perfil_invalido():
    
    perfil_corrupto = PerfilProblema("camino_minimo", 1, "sin_pesos") 
    with pytest.raises(TypeError):
        validar_perfil(perfil_corrupto)
# no hay pedo por las casas que parecen errores en los test publicas si jala 
