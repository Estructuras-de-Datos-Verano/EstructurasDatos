"""Pruebas guiadas para las implementaciones de pila."""

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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


def test_todo_agregar_prueba_con_tres_elementos():
    """TODO alumno: agrega una prueba propia con tres elementos."""

    assert True
