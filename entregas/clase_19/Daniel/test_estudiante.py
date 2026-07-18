# pruebas propias, Daniel


def test_validacion_acepta_orden_vacio_si_grafo_esta_vacio():
    assert es_orden_topologico({}, [])


def test_validacion_con_orden_none_es_falso():
    assert not es_orden_topologico({"A": []}, None)


def test_cursos_aristas_aisladas_y_desconectadas():
    aristas = [(0, 1), (3, 4)]
    orden = ordenar_cursos(6, aristas)
    assert orden is not None
    validar_orden_cursos(6, aristas, orden)


def test_cursos_acepta_tuplas_de_tuplas():
    entrada = ((0, 1), (1, 2))
    assert ordenar_cursos(3, entrada) == [0, 1, 2]


def test_cursos_ciclo_lejos_de_la_fuente():
    assert ordenar_cursos(4, [(0, 1), (1, 2), (2, 3), (3, 1)]) is None


def test_normalizar_con_multiples_aristas_hacia_el_mismo_destino():
    grafo = {"A": ["C"], "B": ["C"]}
    assert normalizar_grafo_dirigido(grafo) == {"A": ["C"], "B": ["C"], "C": []}


def test_grados_entrada_con_autoarista():
    assert grados_entrada({"A": ["A"]}) == {"A": 1}


def test_cursos_valores_booleanos_disfrazados_de_enteros():
    with pytest.raises(TypeError):
        ordenar_cursos(2, [(True, 1)])
    with pytest.raises(TypeError):
        ordenar_cursos(True, [])




