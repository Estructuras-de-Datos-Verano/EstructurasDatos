from implementacion import orden_topologico, es_orden_topologico

def test_varios_ordenes():
    # Verifica validacion universal para varias fuentes y multiples ordenes de resolucion posibles.
    grafo = {"A": ["C"], "B": ["C"]}
    orden = orden_topologico(grafo)
    assert orden is not None
    assert es_orden_topologico(grafo, orden)

def test_ciclo_simple():
    # Detecta un ciclo basico de dependencias que vuelve sobre si mismo, debiendo retornar None.
    grafo = {"A": ["B"], "B": ["C"], "C": ["A"]}
    assert orden_topologico(grafo) is None

def test_ciclo_parcial():
    # Asegura que un ciclo encapsulado inhabilite la operacion global, incluso con nodos libres.
    grafo = {"D": ["E"], "A": ["B"], "B": ["C"], "C": ["A"]}
    assert orden_topologico(grafo) is None

def test_vecino_implicito():
    # Prueba la normalizacion y agregado al orden de destinos declarados en valores, sin clave propia.
    grafo = {"A": ["B"]}
    orden = orden_topologico(grafo)
    assert orden == ["A", "B"]

def test_dependencia_duplicada():
    # Mide la resiliencia al duplicado: la clave B debe asimilarse unicamente una vez en la operacion.
    grafo = {"A": ["B", "B"]}
    orden = orden_topologico(grafo)
    assert orden == ["A", "B"]

def test_orden_incorrecto():
    # Validacion estricta contra arreglos mal colocados: fallar si antecedente es superado por posterior.
    grafo = {"A": ["B", "C"]}
    assert es_orden_topologico(grafo, ["B", "C", "A"]) is False