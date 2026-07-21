from implementacion import *

def test_bfs_vs_dijkstra_sin_pesos_LEO():
    """
    Regla: un camino mínimo sin pesos debe resolverse con BFS.
    Entrada: camino mínimo con un grafo sin pesos.
    Resultado esperado: se selecciona BFS y no Dijkstra.
    Alternativa descartada: Dijkstra, porque introduciría una prioridad
    innecesaria cuando todas las aristas tienen el mismo costo.
    Relevancia: diferencia entre caminos sin pesos y con pesos positivos.
    """
    perfil = PerfilProblema("camino_minimo", True, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "BFS"
    assert decision.algoritmo != "Dijkstra"


def test_01_bfs_vs_bfs_cero_uno_LEO():
    """
    Regla: cuando los pesos son únicamente 0 y 1 debe elegirse 0-1 BFS.
    Entrada: camino mínimo con pesos cero/uno.
    Resultado esperado: algoritmo 0-1 BFS.
    Alternativa descartada: BFS, ya que ignora el costo de las aristas.
    Relevancia: distingue el dominio especial de pesos 0 y 1.
    """
    perfil = PerfilProblema("camino_minimo", False, "cero_uno")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "0-1 BFS"
    assert decision.algoritmo != "BFS"


def test_dijkstra_vs_kruskal_objetivos_distintos_LEO():
    """
    Regla: el objetivo determina el algoritmo aunque existan pesos positivos.
    Entrada: conexión mínima con pesos no negativos.
    Resultado esperado: Kruskal.
    Alternativa descartada: Dijkstra, porque calcula caminos mínimos y no
    árboles de expansión mínima.
    Relevancia: separa claramente dos problemas clásicos de grafos.
    """
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kruskal"
    assert decision.algoritmo != "Dijkstra"


def test_bfs_vs_kahn_dependencias_LEO():
    """
    Regla: ordenar dependencias requiere Kahn.
    Entrada: grafo dirigido sin pesos cuyo objetivo es ordenar tareas.
    Resultado esperado: algoritmo Kahn.
    Alternativa descartada: BFS, ya que recorrer por niveles no produce
    necesariamente un orden topológico válido.
    Relevancia: diferencia recorrido de ordenamiento topológico.
    """
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kahn"
    assert decision.algoritmo != "BFS"


def test_pesos_negativos_fuera_del_alcance_LEO():
    """
    Regla: los caminos mínimos con pesos negativos quedan fuera del alcance.
    Entrada: camino mínimo con pesos negativos.
    Resultado esperado: ningún algoritmo recomendado.
    Alternativa descartada: Dijkstra, porque no admite pesos negativos.
    Relevancia: verifica que no se inventen algoritmos no estudiados.
    """
    perfil = PerfilProblema("camino_minimo", False, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert decision.estructura is None
    assert decision.advertencia != ""


def test_kruskal_con_pesos_negativos_sigue_siendo_valido_LEO():
    """
    Regla: Kruskal funciona aunque existan aristas con peso negativo.
    Entrada: conexión mínima en un grafo no dirigido con pesos negativos.
    Resultado esperado: Kruskal.
    Alternativa descartada: declarar el problema fuera del alcance.
    Relevancia: comprueba una propiedad característica de Kruskal.
    """
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    valida, errores = evaluar_propuesta(perfil, "Kruskal", "Union-Find")
    assert valida
    assert errores == []


def test_error_solo_de_estructura_LEO():
    """
    Regla: una estructura incorrecta debe detectarse aunque el algoritmo sea
    correcto.
    Entrada: Dijkstra acompañado de una cola.
    Resultado esperado: un único error asociado a la estructura.
    Alternativa descartada: marcar también el algoritmo como incorrecto.
    Relevancia: verifica que evaluar_propuesta distingue ambos conceptos.
    """
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "cola")
    assert not valida
    assert len(errores) == 1
    assert "estructura" in errores[0].lower()


def test_perfil_invalido_dirigido_no_bool_LEO():
    """
    Regla: el atributo dirigido debe ser exactamente bool.
    Entrada: dirigido como cadena.
    Resultado esperado: TypeError.
    Alternativa descartada: aceptar valores equivalentes a verdadero.
    Relevancia: protege el contrato de PerfilProblema.
    """
    perfil = PerfilProblema("camino_minimo", "True", "sin_pesos")
    with pytest.raises(TypeError):
        validar_perfil(perfil)