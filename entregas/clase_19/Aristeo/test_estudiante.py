"""Pruebas propias exigidas por la Práctica 19."""

from implementacion import (
    orden_topologico,
    es_orden_topologico,
    ordenar_cursos,
)


def test_1_varios_ordenes_validos():
    """
    Regla: Si hay fuentes independientes en paralelo, existen múltiples respuestas.
    Entrada: Un grafo con dos tareas libres ('A' y 'B') que convergen en 'C'.
    Resultado esperado: Ambos órdenes son válidos bajo es_orden_topologico.
    Relevancia: Desmitifica que el ordenamiento sea unívoco y evalúa por propiedades.
    """
    grafo = {"A": ["C"], "B": ["C"]}
    orden_obtenido = orden_topologico(grafo)
    
    assert orden_obtenido is not None
    assert es_orden_topologico(grafo, orden_obtenido)
    # Verificamos manualmente que las dos secuencias teóricas son válidas
    assert es_orden_topologico(grafo, ["A", "B", "C"])
    assert es_orden_topologico(grafo, ["B", "A", "C"])


def test_2_ciclo_simple():
    """
    Regla: Si un grafo contiene un bucle circular completo, es imposible ordenarlo.
    Entrada: A -> B -> A.
    Resultado esperado: Debe retornar None (no un prefijo parcial).
    Relevancia: Protege contra bucles infinitos y asegura la detección total del ciclo.
    """
    grafo = {"A": ["B"], "B": ["A"]}
    assert orden_topologico(grafo) is None


def test_3_ciclo_parcial_en_una_parte_del_grafo():
    """
    Regla: Un ciclo parcial en cualquier componente invalida la secuencia completa.
    Entrada: D -> E (con grado cero inicializable) junto a un ciclo aislado A -> B -> C -> A.
    Resultado esperado: Debe retornar None, rechazando entregar prefijos acíclicos ("D", "E").
    Relevancia: Valida el requerimiento de cobertura completa antes de certificar un DAG.
    """
    grafo = {"D": ["E"], "A": ["B"], "B": ["C"], "C": ["A"]}
    assert orden_topologico(grafo) is None


def test_4_vecino_implicito():
    """
    Regla: Los vecinos que aparecen en listas de adyacencia pero no como claves deben indexarse.
    Entrada: "A" apunta a "B", pero "B" no se declara explícitamente en el diccionario original.
    Resultado esperado: ['A', 'B'] (B se procesa de forma segura al quedarse sin precedencias).
    Relevancia: Evita KeyErrors y robustece la etapa de normalización defensiva.
    """
    grafo = {"A": ["B"]}
    assert orden_topologico(grafo) == ["A", "B"]


def test_5_dependencias_duplicadas():
    """
    Regla: Los prerrequisitos repetidos se limpian y cuentan una única vez.
    Entrada: Una arista duplicada redundante en la entrada [(0, 1), (0, 1)].
    Resultado esperado: [0, 1] sin errores de bloqueo por reducciones inválidas.
    Relevancia: Comprueba que el contador de grados inicial no se corrompa por redundancia.
    """
    prerrequisitos = [(0, 1), (0, 1)]
    assert ordenar_cursos(2, prerrequisitos) == [0, 1]


def test_6_orden_incorrecto():
    """
    Regla: es_orden_topologico debe rechazar secuencias que violen las aristas del grafo.
    Entrada: Grafo A -> B y la secuencia incorrecta u omitida ["B", "A"].
    Resultado esperado: False.
    Relevancia: Asegura que el validador inspeccione de forma fidedigna la condición posicional u < v.
    """
    grafo = {"A": ["B"]}
    assert not es_orden_topologico(grafo, ["B", "A"])