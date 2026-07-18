import pytest
from implementacion import (
    normalizar_grafo_dirigido,
    orden_topologico,
    es_orden_topologico
)

def test_estudiante_varios_ordenes_validos():
    """1. Acepta múltiples caminos topológicos cuando existen empates."""
    grafo = {"A": ["C"], "B": ["C"]}
    assert es_orden_topologico(grafo, ["A", "B", "C"]) is True
    assert es_orden_topologico(grafo, ["B", "A", "C"]) is True

def test_estudiante_ciclo_simple():
    """2. Detecta un bloqueo circular directo y devuelve None."""
    grafo_con_ciclo = {"A": ["B"], "B": ["A"]}
    assert orden_topologico(grafo_con_ciclo) is None

def test_estudiante_ciclo_parcial():
    """3. Detecta ciclos aislados dentro del grafo, rechazando prefijos."""
    grafo_parcial = {
        "X": ["Y"],      
        "A": ["B"],      
        "B": ["C"], 
        "C": ["A"]       
    }
    assert orden_topologico(grafo_parcial) is None

def test_estudiante_vecino_implicito():
    """4. Descubre y normaliza correctamente los nodos sumidero."""
    grafo_incompleto = {"A": ["B"]}
    normalizado = normalizar_grafo_dirigido(grafo_incompleto)
    
    assert "B" in normalizado
    assert normalizado["B"] == []
    assert orden_topologico(grafo_incompleto) == ["A", "B"]

def test_estudiante_dependencias_duplicadas():
    """5. Ignora las flechas redundantes para no alterar el grado de entrada."""
    grafo_duplicado = {"A": ["B", "B"]}
    
    normalizado = normalizar_grafo_dirigido(grafo_duplicado)
    assert normalizado["A"] == ["B"]  
    assert orden_topologico(grafo_duplicado) == ["A", "B"]

def test_estudiante_orden_incorrecto():
    """6. El validador rechaza secuencias que rompen el tiempo o cobertura."""
    grafo = {"A": ["B", "C"]}
    
    assert es_orden_topologico(grafo, ["B", "A", "C"]) is False    
    assert es_orden_topologico(grafo, ["A", "B"]) is False
    assert es_orden_topologico(grafo, ["A", "B", "B"]) is False