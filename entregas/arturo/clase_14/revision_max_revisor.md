# Revisión de PR Max

El código se ve que esta implementado de manera correcta.

## Resumen

En resumidas cuentas el trabajo esta bien echo, lo unico que yo llegaria a cambiar es que el notebook se entrego de manera bastante simple, deberias de ser más especifico

## Código

A mi no me gustan los docstrings siento que estorban, yo se los quitaria, pero no por eso estan mal.

## Pruebas

def test_max1():
    heap = HeapMin([2, 5, 4, 8, 9, 7, 10])
    heap.insertar(1)
    
    assert heap.minimo() == 1
    assert heap.tamano() == 8
    assert heap.cumple_propiedad_heap()

def test_max2():

    heap = HeapMin([1, 2, 4, 3, 5, 7, 6, 9])
    assert heap.extraer_min() == 1
    assert heap.minimo() == 2 
    assert heap.cumple_propiedad_heap()

def test_max3():
    piedras_extremas = [1000, 1000, 500, 500, 1, 1, 45, 45]
    assert ultima_piedra(piedras_extremas) == 0

## Fortalezas

El trabajo se entrego de manera limpia y ordenada.

## Mejoras

Las pruebas son un poco simples

## Salida completa de pytes

Ejecutando:
C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe -m pytest -v C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_14\tests C:\Users\0286761\Documents\GitHub\EstructurasDatos\entregas\clase_14\arturo\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_14
configfile: pytest.ini
collecting ... collected 22 items

clase_14\tests\test_publico_heap.py::test_heap_nuevo_esta_vacio PASSED   [  4%]
clase_14\tests\test_publico_heap.py::test_insertar_un_valor_y_consultar_minimo PASSED [  9%]
clase_14\tests\test_publico_heap.py::test_insertar_varios_conserva_minimo_y_propiedad PASSED [ 13%]
clase_14\tests\test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente PASSED [ 18%]
clase_14\tests\test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer PASSED [ 22%]
clase_14\tests\test_publico_heap.py::test_duplicados_y_negativos PASSED  [ 27%]
clase_14\tests\test_publico_heap.py::test_construir_heap_reemplaza_contenido PASSED [ 31%]
clase_14\tests\test_publico_heap.py::test_varios_sift_up PASSED          [ 36%]
clase_14\tests\test_publico_heap.py::test_varios_sift_down PASSED        [ 40%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras0-0] PASSED [ 45%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras1-5] PASSED [ 50%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras2-0] PASSED [ 54%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras3-1] PASSED [ 59%]
clase_14\tests\test_publico_heap.py::test_insercion_varios_cambios_ARTURO PASSED [ 63%]
clase_14\tests\test_publico_heap.py::test_extraccion_desciende_varios_niveles_ARTURO PASSED [ 68%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra_casos_extremos_ARTURO PASSED [ 72%]
clase_14\tests\test_publico_heap.py::test_max1 PASSED                    [ 77%]
clase_14\tests\test_publico_heap.py::test_max2 PASSED                    [ 81%]
clase_14\tests\test_publico_heap.py::test_max3 PASSED                    [ 86%]
clase_14::test_insercion_varios_cambios_ARTURO <- ..\entregas\clase_14\arturo\test_estudiante.py PASSED [ 90%]
clase_14::test_extraccion_desciende_varios_niveles_ARTURO <- ..\entregas\clase_14\arturo\test_estudiante.py PASSED [ 95%]
clase_14::test_ultima_piedra_casos_extremos_ARTURO <- ..\entregas\clase_14\arturo\test_estudiante.py PASSED [100%]

============================= 22 passed in 0.03s ==============================

Todos los test, tanto los publicos, como los mios, como los de arturo, fueron superados correctamente con su implementacion.
## Conclusión

El trbajo se entrego correctamente, y sin ningun tipo de problemas.

## Checklist del revisor

- [x] Descargué la rama.
- [x] Ejecuté pruebas públicas.
- [x] Ejecuté mis pruebas.
- [x] Agregué `revision_nombre.md`.
- [x] Pegué salida completa de pytest.
- [x] Hice comentarios útiles.