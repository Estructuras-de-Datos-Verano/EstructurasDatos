"""Pruebas propias para la Clase 17: Listas ligadas, BFS y 0-1 BFS."""

import pytest
from math import inf

from implementacion import (
    ColaLigada,
    DequeLigada,
    bfs_camino,
    camino_cero_uno,
    cero_uno_bfs
)

def test_cola_respeta_orden_fifo():
    """
    Regla: La cola devuelve los elementos estrictamente en el orden en que entraron (FIFO).
    Entrada: Encolar 1, 2 y 3.
    Resultado esperado: Desencolar devuelve 1, luego 2, luego 3.
    Razón: BFS depende totalmente del orden FIFO para procesar el grafo por capas.
    """
    cola = ColaLigada()
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    
    assert cola.desencolar() == 1
    assert cola.desencolar() == 2
    assert cola.desencolar() == 3
    assert cola.esta_vacia()


def test_cola_se_reutiliza_despues_de_vaciarse():
    """
    Regla: Vaciar la cola restaura ambos extremos y permite reutilizarla.
    Entrada: Encolar "A", desencolar "A", y luego encolar "B".
    Resultado esperado: La cola no se rompe y el primero es "B".
    Razón: Evita que queden referencias residuales o "basura" en la memoria de una lista usada.
    """
    cola = ColaLigada()
    cola.encolar("A")
    cola.desencolar()
    
    assert cola.esta_vacia()
    
    cola.encolar("B")
    assert cola.primero() == "B"
    assert cola.desencolar() == "B"


def test_deque_operaciones_combinadas_extremos():
    """
    Regla: La deque mantiene consistencia al insertar y quitar desde ambos extremos cruzados.
    Entrada: Agregar al inicio "Centro", al final "Derecha", al inicio "Izquierda".
    Resultado esperado: Tamaño 3, inicio es "Izquierda", final es "Derecha".
    Razón: 0-1 BFS inyectará nodos en ambos lados dinámicamente; los enlaces bidireccionales no deben colapsar.
    """
    deque = DequeLigada()
    deque.agregar_inicio("Centro")
    deque.agregar_final("Derecha")
    deque.agregar_inicio("Izquierda")
    
    assert len(deque) == 3
    assert deque.quitar_inicio() == "Izquierda"
    assert deque.quitar_final() == "Derecha"
    assert deque.quitar_inicio() == "Centro"
    assert deque.esta_vacia()


def test_deque_reutilizacion_extremos():
    """
    Regla: Al igual que la cola, la deque debe restablecer inicio y final al vaciarse por completo.
    Entrada: Llenar por un extremo, vaciar por el otro, y volver a insertar.
    Resultado esperado: Las nuevas inserciones no lanzan error y actualizan el tamaño correctamente.
    Razón: Una deque mal implementada podría dejar un `_inicio` fantasma que rompa iteraciones futuras.
    """
    deque = DequeLigada()
    deque.agregar_final(10)
    deque.quitar_inicio()
    
    deque.agregar_inicio(20)
    assert deque.ultimo() == 20
    assert deque.quitar_final() == 20


def test_bfs_maneja_ciclos_sin_quedarse_atrapado():
    """
    Regla: BFS debe ignorar nodos ya descubiertos para evitar bucles infinitos.
    Entrada: Grafo cíclico A -> B -> C -> A.
    Resultado esperado: Camino de A a C es [A, B, C], no se repite A.
    Razón: En grafos reales los ciclos son comunes; volver a encolar un nodo ya visitado agota la memoria.
    """
    grafo = {"A": ["B"], "B": ["C"], "C": ["A"]}
    camino = bfs_camino(grafo, "A", "C")
    assert camino == ["A", "B", "C"]


def test_bfs_destino_inalcanzable():
    """
    Regla: Si no hay conexión entre origen y destino, devuelve una lista vacía.
    Entrada: Grafo desconectado A -> B, X -> Y. Buscar camino de A a X.
    Resultado esperado: [] (lista vacía).
    Razón: Es el comportamiento estándar (contrato) para un destino que existe en el grafo pero no en la componente conexa del origen.
    """
    grafo = {"A": ["B"], "B": [], "X": ["Y"], "Y": []}
    camino = bfs_camino(grafo, "A", "X")
    assert camino == []


def test_cero_uno_bfs_elige_ruta_mas_larga_pero_barata():
    """
    Regla: 0-1 BFS prioriza el costo (0) por encima del número de aristas.
    Entrada: Un camino corto de 1 arista que cuesta 1, y un camino largo de 3 aristas que cuestan 0.
    Resultado esperado: Selecciona el camino largo con costo 0.
    Razón: Demuestra que la estructura DequeLigada está adelantando correctamente los costos 0, superando al BFS tradicional.
    """
    grafo = {
        "A": [("Destino", 1), ("Paso1", 0)],
        "Paso1": [("Paso2", 0)],
        "Paso2": [("Destino", 0)],
        "Destino": []
    }
    costo, camino = camino_cero_uno(grafo, "A", "Destino")
    assert costo == 0
    assert camino == ["A", "Paso1", "Paso2", "Destino"]


def test_cero_uno_bfs_rechaza_pesos_invalidos():
    """
    Regla: Solo se permiten pesos de valor entero 0 o 1.
    Entrada: Arista con peso True (booleano) y arista con peso 2 (entero fuera de rango).
    Resultado esperado: TypeError para el booleano y ValueError para el 2.
    Razón: El algoritmo matemático 0-1 asume incrementos exactos. Booleanos y números > 1 rompen la validez de la deque como estructura prioritaria.
    """
    # Prueba booleano
    with pytest.raises(TypeError):
        cero_uno_bfs({"A": [("B", True)]}, "A")
        
    # Prueba valor > 1
    with pytest.raises(ValueError):
        cero_uno_bfs({"A": [("B", 2)]}, "A")