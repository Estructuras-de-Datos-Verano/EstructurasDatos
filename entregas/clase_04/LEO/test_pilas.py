"""Pruebas guiadas para las implementaciones de pila."""

import pytest

from src.pilas import PilaDeque, PilaLista, PilaTupla


IMPLEMENTACIONES = [PilaLista, PilaDeque, PilaTupla]


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_pila_recien_creada_esta_vacia(ClasePila):
    pila = ClasePila()
    assert pila.esta_vacia()
    assert pila.tamano() == 0


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_push_cambia_estado(ClasePila):
    pila = ClasePila()
    pila.push("dato")
    assert not pila.esta_vacia()
    assert pila.tamano() == 1


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_pop_respeta_lifo(ClasePila):
    pila = ClasePila()
    pila.push("primero")
    pila.push("segundo")
    assert pila.pop() == "segundo"
    assert pila.pop() == "primero"
    assert pila.esta_vacia()


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_peek_no_elimina(ClasePila):
    pila = ClasePila()
    pila.push(10)
    pila.push(20)
    assert pila.peek() == 20
    assert pila.tamano() == 2


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_pop_en_pila_vacia_lanza_error(ClasePila):
    pila = ClasePila()
    with pytest.raises(IndexError):
        pila.pop()


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_peek_en_pila_vacia_lanza_error(ClasePila):
    pila = ClasePila()
    with pytest.raises(IndexError):
        pila.peek()


@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_tamano_aumenta_y_disminuye(ClasePila):
    pila = ClasePila()
    pila.push("a")
    pila.push("b")
    assert pila.tamano() == 2
    pila.pop()
    assert pila.tamano() == 1

@pytest.mark.parametrize("ClasePila", IMPLEMENTACIONES)
def test_todo_agregar_prueba_con_tres_elementos(ClasePila):
    """TODO alumno: agrega una prueba propia con tres elementos."""
    pila = ClasePila()
    pila.push("L")
    pila.push("E")
    pila.push("O")
    assert pila.tamano() == 3
    assert pila.peek() == "O"
    assert pila.pop() == "O"
    assert pila.tamano() == 2
    assert pila.peek() == "E"
    assert pila.pop() == "E"
    assert pila.tamano() == 1
    assert pila.peek() == "L"
    assert pila.pop() == "L"
    assert pila.tamano() == 0
    assert pila.esta_vacia()

