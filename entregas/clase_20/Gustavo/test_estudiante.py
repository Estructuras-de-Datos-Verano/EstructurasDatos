"""Pruebas propias del estudiante para la Clase 20."""

import pytest

from entregas.clase_20.Gustavo.implementacion import (
    PerfilProblema,
    seleccionar_estrategia,
    evaluar_propuesta,
    validar_perfil,
    es_aplicable
)

def test_bfs_vs_dijkstra():
    """
    Regla: Caminos con pesos no negativos requieren Dijkstra, no BFS[cite: 1].
    Entrada: PerfilProblema("camino_minimo", True, "no_negativos").
    Resultado esperado: Rechazar la propuesta de BFS.
    Alternativa descartada: BFS con cola.
    Relevancia: Evita usar un algoritmo que minimiza el número de saltos cuando lo que importa es la suma de los pesos[cite: 1].
    """
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "BFS", "cola")
    assert not valida
    assert any("Dijkstra" in error for error in errores)


def test_cero_uno_bfs_vs_bfs():
    """
    Regla: Pesos 0/1 permiten optimizar la extracción usando un deque[cite: 1].
    Entrada: PerfilProblema("camino_minimo", True, "cero_uno").
    Resultado esperado: 0-1 BFS con deque.
    Alternativa descartada: BFS normal (ignoraría los pesos) o Dijkstra (incurriría en un costo innecesario de O(V log V))[cite: 1].
    Relevancia: Distingue la especialización matemática sobre el dominio de pesos restringido[cite: 1].
    """
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "0-1 BFS"
    assert decision.estructura == "deque"


def test_dijkstra_vs_kruskal():
    """
    Regla: Conexión mínima global minimiza toda la red, caminos mínimos solo desde un origen[cite: 1].
    Entrada: PerfilProblema("conexion_minima", False, "no_negativos").
    Resultado esperado: Kruskal.
    Alternativa descartada: Dijkstra.
    Relevancia: Demuestra que un árbol de predecesores formado por rutas más cortas (Dijkstra) no garantiza el costo mínimo total de la red (MST)[cite: 1].
    """
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kruskal"
    assert not es_aplicable("Dijkstra", perfil)


def test_bfs_vs_kahn():
    """
    Regla: Las precedencias dirigidas (dependencias) se resuelven liberando grados cero[cite: 1].
    Entrada: PerfilProblema("orden_dependencias", True, "sin_pesos").
    Resultado esperado: Kahn usando cola + grados de entrada.
    Alternativa descartada: BFS.
    Relevancia: Aunque Kahn y BFS comparten la cola como estructura, el significado de lo que entra en ella (el invariante) es completamente distinto[cite: 1].
    """
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kahn"
    assert "grados" in decision.estructura


def test_pesos_negativos_fuera_de_alcance():
    """
    Regla: Dijkstra rompe su invariante central con aristas negativas[cite: 1].
    Entrada: PerfilProblema("camino_minimo", True, "incluye_negativos").
    Resultado esperado: El motor debe indicar que no hay algoritmo aplicable (None).
    Alternativa descartada: Forzar Dijkstra asumiendo valores absolutos.
    Relevancia: Demuestra madurez al rechazar el problema con precisión antes que devolver datos falsos[cite: 1].
    """
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo is None
    assert "Contrato violado" in decision.advertencia


def test_kruskal_con_peso_negativo():
    """
    Regla: Kruskal sí soporta aristas con pesos negativos[cite: 1].
    Entrada: PerfilProblema("conexion_minima", False, "incluye_negativos").
    Resultado esperado: Kruskal y Union-Find.
    Alternativa descartada: Rechazar el perfil (como sí pasaría en caminos mínimos).
    Relevancia: A diferencia de Dijkstra, un peso negativo no rompe a Kruskal; simplemente esa arista aparecerá antes al ordenarlas[cite: 1].
    """
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    assert decision.algoritmo == "Kruskal"
    assert decision.estructura == "Union-Find"


def test_error_solo_de_estructura():
    """
    Regla: Evaluar una propuesta debe detectar si el algoritmo es correcto pero la estructura no.
    Entrada: Perfil de orden topológico proponiendo Kahn (correcto) pero con un heap (incorrecto).
    Resultado esperado: Falla en la validación especificando el error estructural.
    Alternativa descartada: Aceptar la propuesta a medias.
    Relevancia: Subraya que la complejidad asintótica se logra solo combinando la operación dominante con la estructura ideal[cite: 1].
    """
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    valida, errores = evaluar_propuesta(perfil, "Kahn", "heap")
    assert not valida
    assert any("Estructura incorrecta" in error for error in errores)
    assert not any("Algoritmo incorrecto" in error for error in errores)


def test_perfil_invalido():
    """
    Regla: El perfil no puede contener vocabulario no registrado[cite: 2].
    Entrada: PerfilProblema("viaje_espacial", True, "sin_pesos").
    Resultado esperado: Levantar ValueError.
    Alternativa descartada: Continuar ejecución y devolver un fallo silencioso.
    Relevancia: Evita procesar problemas mal modelados desde el inicio (fail-fast).
    """
    perfil = PerfilProblema("viaje_espacial", True, "sin_pesos")
    with pytest.raises(ValueError):
        validar_perfil(perfil)