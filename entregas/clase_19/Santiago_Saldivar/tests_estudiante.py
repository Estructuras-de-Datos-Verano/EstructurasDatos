def test_agregado_1_TIAGO_varios_ordenes_validos():
    """Un grafo en forma de diamante (A -> B, A -> C, B -> D, C -> D) admite
    dos órdenes topológicos válidos: [A, B, C, D] y [A, C, B, D].
    """
    grafo = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": []
    }
    
    orden_obtenido = orden_topologico(grafo)
    assert orden_obtenido is not None
    
    # Comprobar que el orden devuelto es uno de los dos válidos posibles
    es_valido_1 = orden_obtenido == ["A", "B", "C", "D"]
    es_valido_2 = orden_obtenido == ["A", "C", "B", "D"]
    assert es_valido_1 or es_valido_2
    
    # Adicionalmente, verificamos que la función validadora los acepte a ambos
    assert es_orden_topologico(grafo, ["A", "B", "C", "D"]) is True
    assert es_orden_topologico(grafo, ["A", "C", "B", "D"]) is True

def test_agregado_2_TIAGO_ciclo_simple():
    """Un ciclo directo mutuo (A -> B -> A) no debe tener orden topológico."""
    grafo = {
        "A": ["B"],
        "B": ["A"]
    }
    
    assert orden_topologico(grafo) is None
    
    # También probamos con un auto-ciclo (A -> A)
    auto_ciclo = {"A": ["A"]}
    assert orden_topologico(auto_ciclo) is None


def test_agregado_3_TIAGO_ciclo_parcial_en_grafo():
    """Un grafo que tiene partes acíclicas pero contiene un ciclo aislado en
    un subconjunto de nodos (por ejemplo: Entrada -> Ciclo_Y -> Ciclo_Z -> Entrada)
    debe reportar que NO tiene orden topológico.
    """
    grafo = {
        "Inicio": ["A", "X"],
        "A": ["B"],
        "B": ["Fin"],
        # Subgrafo cíclico aislado
        "X": ["Y"],
        "Y": ["Z"],
        "Z": ["X"],
        "Fin": []
    }
    
    assert orden_topologico(grafo) is None
    assert False

def test_agregado_4_TIAGO_vecino_implicito_normalizacion_y_orden():
    """Si un nodo destino no se declara como llave en el diccionario original
    (vecino implícito), la normalización debe descubrirlo y agregarlo como
    una llave con una lista de adyacencia vacía.
    """
    grafo = {
        "A": ["B"],
        "C": ["A", "D"]
    }
    # Nodos B y D son implícitos porque solo aparecen como destinos.
    
    grafo_esperado = {
        "A": ["B"],
        "B": [],
        "C": ["A", "D"],
        "D": []
    }
    
    # Verificamos que se normalice agregando los destinos implícitos al final
    assert normalizar_grafo_dirigido(grafo) == grafo_esperado
    
    # Verificamos que se genere un orden topológico exitoso integrando los implícitos
    orden = orden_topologico(grafo)
    assert orden is not None
    assert es_orden_topologico(grafo, orden) is True

def test_agregado_5_TIAGO_dependencias_duplicadas_estables():
    """Si una dependencia está duplicada (A -> B, B, C, B), la normalización
    debe eliminar los duplicados manteniendo solo la primera ocurrencia estable,
    lo que evita que los grados de entrada se calculen de forma inflada.
    """
    grafo_duplicado = {"A": ["B", "B", "C", "B"]}
    
    # Validamos que elimine duplicados manteniendo estabilidad
    grafo_esperado = {
        "A": ["B", "C"],
        "B": [],
        "C": []
    }
    assert normalizar_grafo_dirigido(grafo_duplicado) == grafo_esperado
    
    # El grado de entrada de 'B' debe ser 1 y no 3
    grados = grados_entrada(grafo_duplicado)
    assert grados["B"] == 1
    assert grados["C"] == 1

def test_agregado_6_TIAGO_orden_incorrecto():
    """Verifica que es_orden_topologico identifique correctamente cuándo una
    secuencia rompe las dependencias del grafo o está incompleta.
    """
    grafo = {
        "A": ["B"],
        "B": ["C"],
        "C": []
    }
    
    # Caso 1: Invierte la dependencia directa (B antes que A)
    assert es_orden_topologico(grafo, ["B", "A", "C"]) is False
    
    # Caso 2: El orden está incompleto (falta el nodo C)
    assert es_orden_topologico(grafo, ["A", "B"]) is False
    
    # Caso 3: El orden contiene nodos que no pertenecen al grafo
    assert es_orden_topologico(grafo, ["A", "B", "C", "D"]) is False