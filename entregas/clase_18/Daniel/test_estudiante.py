def test_costo_reparacion_no_muta_y_rechaza_costo_float ():
    carreteras = [(0, 1, 2)]
    copia = carreteras.copy()
    assert costo_reparacion(2, carreteras) == 2
    assert carreteras == copia
    with pytest.raises(TypeError):
        costo_reparacion(2, [(0, 1, 2.0)])

def test_dijkstra_rechaza_cantidad_de_ciudades_invalida():
    with pytest.raises(TypeError):
        costo_reparacion("3", [])
    with pytest.raises(ValueError):
        costo_reparacion(-1, [])

def test_kruskal_rechaza_aristas_con_extremos_fuera_de_rango():
    with pytest.raises(IndexError):
        kruskal(3, [(0, 3, 1)])
    with pytest.raises(IndexError):
        kruskal(3, [(3, 0, 1)])

def test_costo_reparacion_rechaza_aristas_con_extremos_fuera_de_rango():
    with pytest.raises(IndexError):
        costo_reparacion(3, [(0, 3, 1)])
    with pytest.raises(IndexError):
        costo_reparacion(3, [(3, 0, 1)])

def test_kruskal_rechaza_aristas_con_peso_no_finito ():
    with pytest.raises(ValueError):
        kruskal(2, [(0, 1, math.inf)])
    with pytest.raises(ValueError):
        kruskal(2, [(0, 1, -math.inf)])
    with pytest.raises(ValueError):
        kruskal(2, [(0, 1, math.nan)])

def test_kruskal_rechaza_aristas_con_extremos_booleanos():
    with pytest.raises(TypeError):
        kruskal(2, [(True, 1, 1)])
    with pytest.raises(TypeError):
        kruskal(2, [(0, False, 1)])

        # las cosas ya estandefinidas en los tests publicos.
