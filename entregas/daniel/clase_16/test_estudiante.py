def test_para_grafo_que_no_sea_mapping():
    with pytest.raises(TypeError, match="Mapping"):
        dijkstra([("A", [("B", 1)])], "A")

def test_donde_el_nombre_de_un_nodo_o_vecino_no_sea_str():
    with pytest.raises(TypeError, match="cadena de texto"):
        dijkstra({1: [("B", 1)]}, 1)
    with pytest.raises(TypeError, match="cadena de texto"):
        dijkstra({"A": [(2, 1)]}, "A")

def test_entrada_obsoleta():
    grafo = {"A": [("B", 1)], "B": [("C", 2)], "C": []}
    distancias, predecesores = dijkstra(grafo, "A")
    grafo["B"] = []
    with pytest.raises(KeyError):
        reconstruir_camino(predecesores, "A", "C")


# estos sonlos test que sugeria el enunciado que hicieramos para probar la robustez de la implementacion de dijkstra
# pytest y dijkstra estan definidos en el entorno de pruebas, por lo que no es necesario importarlos ni definirlos en este archivo.