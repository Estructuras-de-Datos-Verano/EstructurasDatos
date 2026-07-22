from __future__ import annotations

import pytest

from implementacion import (
    PerfilProblema,
    es_aplicable,
    evaluar_propuesta,
    seleccionar_estrategia,
    validar_perfil,
)


def test_estudiante_bfs_vs_dijkstra():
    """
    Regla: Para caminos mínimos con pesos no negativos generales, se debe usar Dijkstra + heap.
    Entrada: PerfilProblema("camino_minimo", True, "no_negativos")
    Resultado esperado: El algoritmo seleccionado debe ser 'Dijkstra' y BFS debe declararse no aplicable.
    Alternativa descartada: BFS, porque asume un costo uniforme por arista y fallaría al optimizar distancias acumulativas generales.
    Relevancia: Garantiza que no se ignore la presencia de pesos generales al buscar rutas óptimas.
    """
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    decision = seleccionar_estrategia(perfil)
    
    assert decision.algoritmo == "Dijkstra"
    assert decision.estructura == "heap"
    assert not es_aplicable("BFS", perfil)


def test_estudiante_cero_uno_bfs_vs_bfs():
    """
    Regla: Si el camino mínimo contiene estrictamente pesos 0 y 1, se debe elegir 0-1 BFS + deque.
    Entrada: PerfilProblema("camino_minimo", True, "cero_uno")
    Resultado esperado: Selección de '0-1 BFS' con estructura 'deque'.
    Alternativa descartada: BFS estándar (que ignora pesos) y Dijkstra (que añade un costo extra O(log V) innecesario).
    Relevancia: Protege la especialización del dominio de pesos optimizando a complejidad lineal O(V+E).
    """
    perfil = PerfilProblema("camino_minimo", True, "cero_uno")
    decision = seleccionar_estrategia(perfil)
    
    assert decision.algoritmo == "0-1 BFS"
    assert decision.estructura == "deque"
    assert not es_aplicable("BFS", perfil)


def test_estudiante_dijkstra_vs_kruskal():
    """
    Regla: La conexión global mínima de un grafo no dirigido requiere Kruskal + Union-Find.
    Entrada: PerfilProblema("conexion_minima", False, "no_negativos")
    Resultado esperado: Selección de 'Kruskal' y rechazo de Dijkstra para este objetivo.
    Alternativa descartada: Dijkstra, porque este minimiza caminos individuales desde un origen único, no el costo total de la red.
    Relevancia: Distingue formalmente entre un árbol de caminos mínimos y un árbol de expansión mínima (MST).
    """
    perfil = PerfilProblema("conexion_minima", False, "no_negativos")
    decision = seleccionar_estrategia(perfil)
    
    assert decision.algoritmo == "Kruskal"
    assert decision.estructura == "Union-Find"
    assert not es_aplicable("Dijkstra", perfil)


def test_estudiante_bfs_vs_kahn():
    """
    Regla: Un ordenamiento de dependencias dirigidas sin pesos se resuelve con Kahn + cola/grados.
    Entrada: PerfilProblema("orden_dependencias", True, "sin_pesos")
    Resultado esperado: Selección de 'Kahn'. BFS debe ser descartado para este objetivo.
    Alternativa descartada: BFS, porque procesa por niveles de descubrimiento temporal y no respeta la reducción a cero de los grados de entrada.
    Relevancia: Demuestra que compartir la estructura de datos 'cola' no vuelve equivalentes a dos algoritmos con invariantes opuestos.
    """
    perfil = PerfilProblema("orden_dependencias", True, "sin_pesos")
    decision = seleccionar_estrategia(perfil)
    
    assert decision.algoritmo == "Kahn"
    assert "grados" in decision.estructura
    assert not es_aplicable("BFS", perfil)


def test_estudiante_pesos_negativos_fuera_alcance():
    """
    Regla: Los caminos mínimos en presencia de costos negativos están fuera del alcance de lo estudiado.
    Entrada: PerfilProblema("camino_minimo", True, "incluye_negativos")
    Resultado esperado: Retornar una decisión con algoritmo y estructura en None, junto a una advertencia explicativa.
    Alternativa descartada: Dijkstra, porque las aristas negativas rompen su invariante fundamental de que un nodo extraído ya es óptimo.
    Relevancia: Valida la capacidad de detenerse y rechazar propuestas de manera responsable ante la violación de contratos.
    """
    perfil = PerfilProblema("camino_minimo", True, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    
    assert decision.algoritmo is None
    assert decision.estructura is None
    assert decision.advertencia != ""


def test_estudiante_kruskal_con_peso_negativo():
    """
    Regla: Kruskal es perfectamente capaz de procesar pesos negativos para obtener un MST en grafos no dirigidos.
    Entrada: PerfilProblema("conexion_minima", False, "incluye_negativos")
    Resultado esperado: Selección válida de 'Kruskal'.
    Alternativa descartada: Declarar el problema fuera de alcance. Kruskal solo ordena aristas; un peso negativo no rompe su lógica.
    Relevancia: Evita falsos negativos en la toma de decisiones al comprender que los pesos negativos afectan a Dijkstra pero no a Kruskal.
    """
    perfil = PerfilProblema("conexion_minima", False, "incluye_negativos")
    decision = seleccionar_estrategia(perfil)
    
    assert decision.algoritmo == "Kruskal"
    assert decision.estructura == "Union-Find"


def test_estudiante_error_solo_de_estructura():
    """
    Regla: Al evaluar propuestas, se debe detectar de forma aislada si el algoritmo es correcto pero la estructura es incorrecta.
    Entrada: PerfilProblema("camino_minimo", True, "no_negativos") con propuesta algoritmo="Dijkstra", estructura="cola".
    Resultado esperado: valida=False, y una lista de errores con exactamente 1 fallo enfocado en la estructura.
    Alternativa descartada: Aprobar la propuesta o reportar errores múltiples mezclados.
    Relevancia: Provee mensajes de diagnóstico accionables y granulares para corregir bugs de infraestructura sin alterar la lógica.
    """
    perfil = PerfilProblema("camino_minimo", True, "no_negativos")
    valida, errores = evaluar_propuesta(perfil, "Dijkstra", "cola")
    
    assert not valida
    assert len(errores) == 1
    assert "Estructura incorrecta" in errores[0]


def test_estudiante_perfil_invalido():
    """
    Regla: El sistema debe rechazar inmediatamente vocabularios u objetivos desconocidos lanzando un ValueError.
    Entrada: PerfilProblema("viajante_comercio", True, "sin_pesos")
    Resultado esperado: Lanzamiento de una excepción ValueError al intentar validar o seleccionar estrategia.
    Alternativa descartada: Devolver una decisión vacía o None de manera silenciosa.
    Relevancia: Actúa como una guardavalor estricta en el contrato de entrada para evitar procesamientos corruptos aguas abajo.
    """
    perfil = PerfilProblema("viajante_comercio", True, "sin_pesos")
    
    with pytest.raises(ValueError):
        validar_perfil(perfil)
        
    with pytest.raises(ValueError):
        seleccionar_estrategia(perfil)