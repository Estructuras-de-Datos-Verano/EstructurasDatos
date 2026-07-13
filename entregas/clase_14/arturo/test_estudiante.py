import pytest

from entregas.clase_14.arturo.implementacion import HeapMin, ultima_piedra

def test_insercion_varios_cambios_ARTURO():
    """
    Prueba que al insertar un número muy pequeño, el método _subir (sift-up)
    haga múltiples intercambios hasta llevar el elemento a la raíz.
    """
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    

    heap.insertar(5)
    
    assert heap.minimo() == 5
    assert heap.cumple_propiedad_heap()


def test_extraccion_desciende_varios_niveles_ARTURO():
    """
    Prueba que al extraer la raíz, la hoja que ocupa su lugar baje (sift-down)
    múltiples niveles intercambiándose con los hijos menores.
    """

    heap = HeapMin([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])
    

    extraido = heap.extraer_min()
    
    assert extraido == 10
    assert heap.minimo() == 20
    assert heap.cumple_propiedad_heap()


def test_ultima_piedra_casos_extremos_ARTURO():
    """
    Prueba escenarios poco comunes para el algoritmo de la última piedra.
    """
    # Caso 1: Una piedra masiva contra un "enjambre" de piedras pequeñas.
    # La piedra de 100 se estrellará una por una con las de 1, restando 1 en cada choque.
    assert ultima_piedra([100, 1, 1, 1, 1, 1]) == 95

    # Caso 2: Muchas piedras de idéntico peso pero cantidad impar.
    # Todas se destruyen entre sí por pares y debe sobrar exactamente una intacta.
    assert ultima_piedra([99] * 101) == 99

    # Caso 3: Muchas piedras de idéntico peso pero cantidad par.
    # Todas se destruyen entre sí sin dejar rastro.
    assert ultima_piedra([99] * 100) == 0