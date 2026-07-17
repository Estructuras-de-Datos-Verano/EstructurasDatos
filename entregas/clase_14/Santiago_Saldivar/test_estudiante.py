import pytest

from implementacion import HeapMin, ultima_piedra

def test_agregado_1_insercion_con_varios_cambios():
    """Revisa que los cambios no afecten al mínimo si no es necesario."""
    lista = [1,2,3,9,10,11,5,4]
    heap = HeapMin()
    for valor in lista:
        heap.insertar(valor)
        assert heap.minimo() == 1

def test_agregado_2_extraccion_que_descienda_mas_de_un_nivel():
    """Revisa que deje el máximo hasta el nivel más bajo."""
    lista = [1,2,3,9,10,11,5,4]
    heap = HeapMin(lista)  
    
    for i in range(len(lista)):
        valor = heap.extraer_min()
        assert valor <= 11

def test_agregado_3_caso_ultima_piedra():
    """Casos de última piedra."""
    assert ultima_piedra([]) == 0
    assert ultima_piedra([1,1,5000]) == 4998
    assert ultima_piedra([1,2,3,4,5,6,7,8,9,10]) == ultima_piedra([10,9,8,7,6,5,4,3,2,1])
 




