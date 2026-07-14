
import pytest
from implementacion import HeapMin, ultima_piedra

def test_insercion_recorre_varios_niveles_hasta_raiz():
    """
    Caso 1: Inserción con varios intercambios (sift-up).
    Se inserta un valor que es menor a todos los existentes, obligándolo
    a subir desde la última hoja hasta la raíz.
    """
    datos_iniciales = [10, 20, 30, 40, 50, 60]
    heap = HeapMin(datos_iniciales)
    heap.insertar(5)
    
    assert heap.minimo() == 5, "El valor 5 debería ser la nueva raíz"
    assert heap.tamano() == 7
    assert heap.cumple_propiedad_heap(), "La propiedad min-heap se rompió tras subir el 5"

def test_extraccion_desciende_multiples_niveles():
    """
    Caso 2: Extracción con varios descensos (sift-down).
    Se extrae el mínimo y el valor que sube a la raíz es muy grande,
    obligándolo a descender hasta el último nivel posible.
    """
    datos = [1, 10, 20, 100, 110, 120, 130]
    heap = HeapMin(datos)
    minimo_extraido = heap.extraer_min()
    
    assert minimo_extraido == 1
    assert heap.minimo() == 10, "El nuevo mínimo tras extraer 1 debe ser 10"
    assert heap.cumple_propiedad_heap(), "La propiedad se rompió tras bajar el 130"

def test_ultima_piedra_caso_complejo():
    """
    Caso 3: Caso extremo de ultima_piedra.
    Se prueba con una secuencia donde las diferencias generan nuevas 
    piedras que deben reordenarse varias veces en el heap.
    """
    piedras = [10, 8, 7, 6, 5]
    resultado = ultima_piedra(piedras)
    
    assert resultado == 2, "La última piedra debería pesar 2 tras todas las colisiones"

def test_heap_con_muchos_duplicados():
    """
    Caso extra: Verifica que el heap maneje correctamente múltiples
    valores idénticos, manteniendo la estabilidad de la estructura.
    """
    datos = [5, 5, 5, 5, 5]
    heap = HeapMin(datos)
    
    heap.insertar(5)
    assert heap.tamano() == 6
    assert heap.extraer_min() == 5
    assert heap.cumple_propiedad_heap()