## Parte 3 — Pruebas
##Agrega al menos tres pruebas propias y explica qué protegen:
##1. una distancia mejora más de una vez y deja una entrada obsoleta;
##2. un destino es inalcanzable;
##3. una ruta indirecta supera a una arista directa costosa.
##Casos opcionales: empates, peso cero, origen igual a destino, nodo que solo aparece como vecino y entrada no mutada.##

def test_distancia_mejorada_varias_veces():
    grafo = {
        "A": [("B", 10), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2), ("D", 5)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 4
    assert camino == ["A", "C", "B", "D"]


def test_destino_inalcanzable():
    grafo = {
        "A": [("B", 1)],
        "B": [],
        "C": [("D", 1)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == float('inf')
    assert camino == []

def test_entrada_obsoleta():
    grafo = {
        "A": [("B", 10), ("C", 1)],
        "B": [("D", 1)],
        "C": [("D", 5)],
        "D": []
    }
    costo, camino = camino_minimo(grafo, "A", "D")
    assert costo == 6
    assert camino == ["A", "C", "D"]

    # no es necesario definir las cosas que salen en amarillo por que en el pruebas publicas ya se encuentran definidas, solo se deben agregar las pruebas propias que se piden en el enunciado.