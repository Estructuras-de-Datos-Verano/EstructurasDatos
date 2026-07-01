"""Pruebas guiadas para las implementaciones de cola."""

import sys
from pathlib import Path

# Agregar el directorio src al path para que los imports funcionen
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

from src.colas import ColaDeque, ColaLista, cargar_cola, vaciar_cola


IMPLEMENTACIONES = [ColaLista, ColaDeque]


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_cola_recien_creada_esta_vacia(ClaseCola):
    cola = ClaseCola()
    assert cola.esta_vacia()
    assert cola.tamano() == 0


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_encolar_cambia_estado(ClaseCola):
    cola = ClaseCola()
    cola.encolar("dato")
    assert not cola.esta_vacia()
    assert cola.tamano() == 1


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_desencolar_respeta_fifo(ClaseCola):
    cola = ClaseCola()
    cola.encolar("primero")
    cola.encolar("segundo")
    cola.encolar("tercero")
    assert cola.desencolar() == "primero"
    assert cola.desencolar() == "segundo"
    assert cola.desencolar() == "tercero"
    assert cola.esta_vacia()


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_frente_no_elimina(ClaseCola):
    cola = ClaseCola()
    cola.encolar(10)
    cola.encolar(20)
    assert cola.frente() == 10
    assert cola.tamano() == 2
    assert cola.desencolar() == 10


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_desencolar_en_cola_vacia_lanza_error(ClaseCola):
    cola = ClaseCola()
    with pytest.raises(IndexError):
        cola.desencolar()


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_frente_en_cola_vacia_lanza_error(ClaseCola):
    cola = ClaseCola()
    with pytest.raises(IndexError):
        cola.frente()


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_tamano_aumenta_y_disminuye(ClaseCola):
    cola = ClaseCola()
    cola.encolar("a")
    cola.encolar("b")
    assert cola.tamano() == 2
    cola.desencolar()
    assert cola.tamano() == 1


@pytest.mark.parametrize("ClaseCola", IMPLEMENTACIONES)
def test_vaciar_cola_regresa_elementos_en_orden(ClaseCola):
    cola = cargar_cola(ClaseCola(), ["ana", "beto", "carla"])
    assert vaciar_cola(cola) == ["ana", "beto", "carla"]
    assert cola.esta_vacia()


def test_todo_agregar_prueba_propia():
    """TODO alumno: agrega una prueba propia relacionada con FIFO."""

    assert True

