def test_TIAGO_1_bool_no_pasa():
    """
    No toma False como 0.
    """
    with pytest.raises(TypeError, match="numérico"):
        dijkstra({"C": [("F", False)]}, "C")

def test_TIAGO_2_vecino_implícito():
    """
    Revisa que tome vecinos implícitos.
    """
    distancias, predecesores = dijkstra({"A": [("B", 1), ("C", 2)]}, "A")
    assert predecesores["B"] == "A"
    assert predecesores["C"] == "A"

def test_TIAGO_3_entrada_obsoleta():
    """
    Revisa que no tome la entrada obsoleta
    """
    distancias, predecesores = dijkstra({"A": [("B", 1), ("C", 20)], "B": [("C", 3)]}, "A")

    assert distancias == {"A":0 , "B": 1, "C":4}

def test_TIAGO_4_NaN_o_infinito_no_pasan():
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", math.inf)]}, "A")
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", -math.inf)]}, "A")
    with pytest.raises(ValueError, match="finito"):
        dijkstra({"A": [("B", math.nan)]}, "A")

def test_TIAGO_5_predecesores():
    """
    Revisa que tome vecinos implícitos.
    """
    distancias, predecesores = dijkstra({"A": [("B", 1), ("C", 2), ("D", 5)],
                                         "B": [("C", 3), ("D",4)],
                                         "C": [("D", 7)],
                                         "D": []
                                         }, "A")
    assert predecesores["D"] == ["A", "B", "C"]
   