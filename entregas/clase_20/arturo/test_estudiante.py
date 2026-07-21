import pytest
from implementacion import (
    PerfilProblema,
    seleccionar_estrategia,
    evaluar_propuesta,
    validar_perfil,
    explicar_descarte
)

def test_bfs_vs_dijkstra():
    """
    Regla: BFS minimiza el número de aristas (costo uniforme), mientras que Dijkstra 
    minimiza la suma de pesos variados no negativos.
    Prueba: Evaluar dos perfiles de camino mínimo, uno sin pesos y otro con pesos no negativos.
    """
    perfil_bfs = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="sin_pesos")
    perfil_dijkstra = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="no_negativos")
    
    dec_bfs = seleccionar_estrategia(perfil_bfs)
    dec_dijkstra = seleccionar_estrategia(perfil_dijkstra)
    
    assert dec_bfs.algoritmo == "BFS", "Sin pesos debe usar BFS."
    assert dec_dijkstra.algoritmo == "Dijkstra", "Pesos no negativos deben usar Dijkstra."
    assert "Dijkstra" in explicar_descarte("BFS", perfil_dijkstra), "Debe explicar que BFS no optimiza sumas."


def test_01_bfs_vs_bfs():
    """
    Regla: Si los pesos se limitan estrictamente a 0 y 1, 0-1 BFS debe preferirse 
    sobre BFS y Dijkstra porque explota el dominio binario para lograr O(V+E).
    """
    perfil_01 = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="cero_uno")
    
    decision = seleccionar_estrategia(perfil_01)
    
    assert decision.algoritmo == "0-1 BFS", "El dominio 0 y 1 debe resolverse con 0-1 BFS."
    assert decision.estructura == "deque", "Debe usar un deque para priorizar 0 al frente."
    assert "costo uniforme" in explicar_descarte("BFS", perfil_01)


def test_dijkstra_vs_kruskal():
    """
    Regla: Dijkstra busca caminos mínimos desde un origen, mientras que Kruskal 
    conecta todos los nodos minimizando el costo total de la red (MST).
    Prueba: El objetivo distingue el algoritmo aunque compartan un grafo no dirigido y ponderado.
    """
    perfil_caminos = PerfilProblema(objetivo="camino_minimo", dirigido=False, tipo_pesos="no_negativos")
    perfil_red = PerfilProblema(objetivo="conexion_minima", dirigido=False, tipo_pesos="no_negativos")
    
    dec_caminos = seleccionar_estrategia(perfil_caminos)
    dec_red = seleccionar_estrategia(perfil_red)
    
    assert dec_caminos.algoritmo == "Dijkstra", "Buscar caminos es trabajo de Dijkstra."
    assert dec_red.algoritmo == "Kruskal", "Conectar una red global es trabajo de Kruskal."


def test_bfs_vs_kahn():
    """
    Regla: Aunque ambos usan una cola, Kahn organiza precedencias dirigidas (dependencias),
    mientras que BFS recorre por capas buscando rutas.
    """
    perfil_ruta = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="sin_pesos")
    perfil_dependencias = PerfilProblema(objetivo="orden_dependencias", dirigido=True, tipo_pesos="sin_pesos")
    
    dec_ruta = seleccionar_estrategia(perfil_ruta)
    dec_dependencias = seleccionar_estrategia(perfil_dependencias)
    
    assert dec_ruta.algoritmo == "BFS", "El objetivo de rutas sin peso es BFS."
    assert dec_dependencias.algoritmo == "Kahn", "El objetivo de ordenar tareas es Kahn."
    assert "grados de entrada" in dec_dependencias.estructura, "Kahn debe usar cola + grados de entrada."


def test_pesos_negativos_fuera_del_alcance():
    """
    Regla: Ninguno de los algoritmos estudiados para caminos mínimos soporta 
    pesos negativos generales (rompe el invariante de Dijkstra).
    """
    perfil_negativo = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="incluye_negativos")
    decision = seleccionar_estrategia(perfil_negativo)
    
    assert decision.algoritmo is None, "No se debe inventar un algoritmo no estudiado."
    assert decision.advertencia != "", "Debe explicar que se violó el contrato de Dijkstra."


def test_kruskal_con_peso_negativo():
    """
    Regla: A diferencia de los caminos mínimos, Kruskal (MST) sí soporta pesos 
    negativos, ya que estos simplemente se ordenan primero al unir componentes.
    """
    perfil_mst_negativo = PerfilProblema(objetivo="conexion_minima", dirigido=False, tipo_pesos="incluye_negativos")
    decision = seleccionar_estrategia(perfil_mst_negativo)
    
    assert decision.algoritmo == "Kruskal", "Kruskal sí aplica para MST con pesos negativos."
    assert decision.estructura == "Union-Find"


def test_error_solo_de_estructura():
    """
    Regla: Evaluar una propuesta donde el algoritmo sugerido es correcto, pero 
    se propone una estructura ineficiente o incorrecta.
    """
    perfil = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="no_negativos")
    
    # Propone Dijkstra (correcto) pero con una cola simple (incorrecto, debe ser heap)
    es_valida, errores = evaluar_propuesta(perfil, algoritmo="Dijkstra", estructura="cola")
    
    assert es_valida is False, "La propuesta debe ser rechazada por la estructura."
    assert len(errores) > 0
    assert any("estructura" in error.lower() for error in errores), "El error debe mencionar la estructura equivocada."


def test_perfil_invalido():
    """
    Regla: El validador debe rechazar estrictamente objetivos o tipos de peso
    que no pertenezcan a los dominios conocidos, previniendo fallos silenciosos.
    """
    perfil_objetivo_falso = PerfilProblema(objetivo="encontrar_tesoro", dirigido=True, tipo_pesos="sin_pesos")
    perfil_peso_falso = PerfilProblema(objetivo="camino_minimo", dirigido=True, tipo_pesos="flotantes")
    
    with pytest.raises(ValueError, match="Objetivo desconocido"):
        validar_perfil(perfil_objetivo_falso)
        
    with pytest.raises(ValueError, match="Tipo de pesos desconocido"):
        validar_perfil(perfil_peso_falso)