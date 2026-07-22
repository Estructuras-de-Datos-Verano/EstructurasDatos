"""Pruebas propias de la Clase 19.

"""

from implementacion import (
    orden_topologico,
    es_orden_topologico,
)

def test_varios_ordenes_validos():
    """
    Regla: Si varios nodos tienen grado cero, el orden topológico no es único.
    Entrada: {"A": ["C"], "B": ["C"]} (A y B apuntan a C).
    Esperado: ["A", "B", "C"] o ["B", "A", "C"].
    Relevancia: Demuestra que la prueba debe verificar por propiedades (usando es_orden_topologico) y no comparando contra una lista exacta, ya que hay múltiples caminos correctos.
    """
    grafo = {"A": ["C"], "B": ["C"]}
    orden = orden_topologico(grafo)
    assert orden is not None
    assert es_orden_topologico(grafo, orden)

def test_ciclo_simple():
    """
    Regla: Un ciclo cerrado impide que los grados de entrada lleguen a cero.
    Entrada: {"A": ["B"], "B": ["A"]} (Pescadilla que se muerde la cola).
    Esperado: None.
    Relevancia: Valida que el algoritmo detecte correctamente la dependencia circular total y retorne None en lugar de quedarse en un bucle infinito o retornar una lista vacía.
    """
    grafo = {"A": ["B"], "B": ["A"]}
    orden = orden_topologico(grafo)
    assert orden is None

def test_ciclo_parcial():
    """
    Regla: Un ciclo en cualquier parte del grafo invalida todo el ordenamiento.
    Entrada: {"X": ["Y"], "A": ["B"], "B": ["C"], "C": ["A"]} (Un componente válido y un ciclo).
    Esperado: None.
    Relevancia: Asegura que el algoritmo no devuelva arreglos truncados o a medias. Aunque X e Y se puedan procesar, el ciclo A-B-C invalida el proceso completo por la comparación de longitudes.
    """
    grafo = {"X": ["Y"], "A": ["B"], "B": ["C"], "C": ["A"]}
    orden = orden_topologico(grafo)
    assert orden is None

def test_vecino_implicito():
    """
    Regla: Los destinos que no aparecen como llaves en el diccionario deben incluirse en el orden.
    Entrada: {"A": ["B"]} (B no es una llave principal explícita).
    Esperado: ["A", "B"].
    Relevancia: Protege contra errores `KeyError` y asegura que la normalización agregue correctamente los nodos destino como nodos sin sucesores.
    """
    grafo = {"A": ["B"]}
    orden = orden_topologico(grafo)
    assert orden == ["A", "B"]

def test_dependencias_duplicadas():
    """
    Regla: Las dependencias repetidas entre los mismos nodos se cuentan una sola vez.
    Entrada: {"A": ["B", "B", "B"]} (A apunta a B tres veces).
    Esperado: ["A", "B"].
    Relevancia: Asegura que la normalización funcione limpiando duplicados. Si no se limpiaran, el nodo B se quedaría con grado de entrada 3, bajando solo a 2 cuando se procese A, y bloqueando el grafo entero.
    """
    grafo = {"A": ["B", "B", "B"]}
    orden = orden_topologico(grafo)
    assert orden == ["A", "B"]

def test_orden_incorrecto():
    """
    Regla: Una secuencia donde un destino aparece antes que su origen es inválida.
    Entrada: Grafo {"A": ["B"]} y secuencia candidata ["B", "A"].
    Esperado: False.
    Relevancia: Valida la lógica de `es_orden_topologico`. Confirma que el validador revisa las posiciones y rechaza listas donde los prerrequisitos se toman después de la materia dependiente.
    """
    grafo = {"A": ["B"]}
    secuencia_invalida = ["B", "A"]
    es_valido = es_orden_topologico(grafo, secuencia_invalida)
    assert es_valido is False

