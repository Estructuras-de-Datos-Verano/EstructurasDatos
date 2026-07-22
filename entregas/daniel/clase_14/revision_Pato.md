# Clase 14: Revision Pato
#### Nombre: Patricio navarro

## Resumen.
Resolvió de buena forma, con un atributo `_arreglo` velto una lista pudo iterar y aplicar las colas de prioridad por el mínimo. Muchas validaciones de una línea bien implementadas.

## Revisión conceptual.
El notebook está bien contestado, creo que faltó la discusión pero en el notebook ya está bien explicado todo. Aunque se equivoca en los índices por ejemplo en uno de los ejercicios guiados.

## Revisión de implementación.
Yo hice algo muy parecido, me confundió un poco que usara lo de `_arreglo` porque parecía que iba ser un intento de encapsular con un método pero no fue así.

## Revisión de pruebas.
Hizo bien los test, cehcando que haya varios cambios, el comportamiento con varios descensos y el caso extremo.

## Salida completa de `pytest -v`.
Ejecutando:
C:\Users\0261331\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\0261331\Documents\GitHub\EstructurasDatos\clase_14\tests C:\Users\0261331\Documents\GitHub\EstructurasDatos\entregas\clase_14\Daniel\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0261331\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0261331\Documents\GitHub\EstructurasDatos\clase_14
configfile: pytest.ini
collecting ... collected 18 items

clase_14\tests\test_publico_heap.py::test_heap_nuevo_esta_vacio FAILED   [  5%]
clase_14\tests\test_publico_heap.py::test_insertar_un_valor_y_consultar_minimo PASSED [ 11%]
clase_14\tests\test_publico_heap.py::test_insertar_varios_conserva_minimo_y_propiedad PASSED [ 16%]
clase_14\tests\test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente FAILED [ 22%]
clase_14\tests\test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer FAILED [ 27%]
clase_14\tests\test_publico_heap.py::test_duplicados_y_negativos FAILED  [ 33%]
clase_14\tests\test_publico_heap.py::test_construir_heap_reemplaza_contenido FAILED [ 38%]
clase_14\tests\test_publico_heap.py::test_varios_sift_up PASSED          [ 44%]
clase_14\tests\test_publico_heap.py::test_varios_sift_down FAILED        [ 50%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras0-0] PASSED [ 55%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras1-5] PASSED [ 61%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras2-0] PASSED [ 66%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras3-1] PASSED [ 72%]
clase_14::test_varios_cambios <- ..\entregas\clase_14\Daniel\test_estudiante.py FAILED [ 77%]
clase_14::test_ultima_piedra_extremo <- ..\entregas\clase_14\Daniel\test_estudiante.py PASSED [ 83%]
clase_14::test_insercion_multiples_cambios <- ..\entregas\clase_14\Daniel\test_estudiante.py FAILED [ 88%]
clase_14::test_extraccion_multiples_descensos <- ..\entregas\clase_14\Daniel\test_estudiante.py FAILED [ 94%]
clase_14::test_ultima_piedra_casos_extremos <- ..\entregas\clase_14\Daniel\test_estudiante.py PASSED [100%]

================================== FAILURES ===================================
_________________________ test_heap_nuevo_esta_vacio __________________________

    def test_heap_nuevo_esta_vacio():
        heap = HeapMin()
>       assert heap.esta_vacio() is True
               ^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'esta_vacio'

clase_14\tests\test_publico_heap.py:10: AttributeError
________________ test_extraer_minimo_devuelve_orden_creciente _________________

    def test_extraer_minimo_devuelve_orden_creciente():
        heap = HeapMin([7, 3, 9, 1, 6, 5])
>       assert [heap.extraer_min() for _ in range(6)] == [1, 3, 5, 6, 7, 9]
                ^^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?

clase_14\tests\test_publico_heap.py:31: AttributeError
________________ test_vacio_lanza_error_al_consultar_o_extraer ________________

    def test_vacio_lanza_error_al_consultar_o_extraer():
        heap = HeapMin()
        with pytest.raises(IndexError):
            heap.minimo()
        with pytest.raises(IndexError):
>           heap.extraer_min()
            ^^^^^^^^^^^^^^^^
E           AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?

clase_14\tests\test_publico_heap.py:40: AttributeError
_________________________ test_duplicados_y_negativos _________________________

    def test_duplicados_y_negativos():
        heap = HeapMin([3, -2, 3, -2, 0])
>       assert [heap.extraer_min() for _ in range(5)] == [-2, -2, 0, 3, 3]
                ^^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?

clase_14\tests\test_publico_heap.py:45: AttributeError
___________________ test_construir_heap_reemplaza_contenido ___________________

    def test_construir_heap_reemplaza_contenido():
        heap = HeapMin([99])
>       heap.construir_heap([8, 4, 7, 1, 5])
        ^^^^^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'construir_heap'

clase_14\tests\test_publico_heap.py:50: AttributeError
____________________________ test_varios_sift_down ____________________________

    def test_varios_sift_down():
        heap = HeapMin([1, 3, 2, 7, 6, 4, 5, 9, 8])
>       assert heap.extraer_min() == 1
               ^^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?

clase_14\tests\test_publico_heap.py:65: AttributeError
_____________________________ test_varios_cambios _____________________________

    def test_varios_cambios():
        heap = HeapMin([10, 20, 15, 30, 40])
        heap.insertar(5)
        assert heap.minimo() == 5
        assert heap.cumple_propiedad_heap()
>       assert heap.extraer_min() == 5
               ^^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?

entregas\clase_14\Daniel\test_estudiante.py:10: AttributeError
______________________ test_insercion_multiples_cambios _______________________

    def test_insercion_multiples_cambios():
        """Prueba que un valor peque±o suba m·ltiples niveles (sift-up) hasta la raÝz."""
    
        heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    
        heap.insertar(5)
    
        assert heap.minimo() == 5
    
>       assert heap.valores == [5, 10, 30, 20, 50, 60, 70, 40]
               ^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'valores'

entregas\clase_14\Daniel\test_estudiante.py:40: AttributeError
_____________________ test_extraccion_multiples_descensos _____________________

    def test_extraccion_multiples_descensos():
        """Prueba que al extraer, la nueva raÝz baje mßs de un nivel (sift-down)."""
    
        heap = HeapMin([5, 10, 15, 20, 25, 30, 35])
    
>       minimo_extraido = heap.extraer_min()
                          ^^^^^^^^^^^^^^^^
E       AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?

entregas\clase_14\Daniel\test_estudiante.py:48: AttributeError
=========================== short test summary info ===========================
FAILED clase_14\tests\test_publico_heap.py::test_heap_nuevo_esta_vacio - AttributeError: 'HeapMin' object has no attribute 'esta_vacio'
FAILED clase_14\tests\test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente - AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?
FAILED clase_14\tests\test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer - AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?
FAILED clase_14\tests\test_publico_heap.py::test_duplicados_y_negativos - AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?
FAILED clase_14\tests\test_publico_heap.py::test_construir_heap_reemplaza_contenido - AttributeError: 'HeapMin' object has no attribute 'construir_heap'
FAILED clase_14\tests\test_publico_heap.py::test_varios_sift_down - AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?
FAILED clase_14::test_varios_cambios - AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?
FAILED clase_14::test_insercion_multiples_cambios - AttributeError: 'HeapMin' object has no attribute 'valores'
FAILED clase_14::test_extraccion_multiples_descensos - AttributeError: 'HeapMin' object has no attribute 'extraer_min'. Did you mean: 'extraer_minimo'?
========================= 9 failed, 9 passed in 0.07s =========================
- Las pruebas fallaron porque en vez de usar `extraer_minimo()` usó `extraer_min()`

## Fortalezas.
- Es claro.
- Funciona. 
- Fácil para cualquiera de leer, porque no abusa de notación por así decirlo. 

## Mejoras.
- Se pudo haber apoyado de mas métodos para verificar que cumple propiedad de min heap en vez de volver a usar las fórmulas completas haciendo un poco repetitivo el código.
- En la solución de la última piedra en vez de usar heapq habría sido mejor probarlo con la clase que hicimos esta clase. 

## Conclusión.
En general bien, son detallitos que afectaron el resultado del pytest pero nada grave, y de no ser por el nombre del método habría funcionado sin problema.

## Respuesta del autor con checklist.
- [ x ] Resumí el enfoque sin reescribir la solución.
- [ x ] Revisé propiedad de heap, índices, sift-up y sift-down.
- [ x ] Revisé nombres, firmas, docstrings y errores.
- [ x ] Ejecuté tests públicos y propios con `pytest -v`.
- [ x ] Incluí la salida completa.
- [ x ] Separé fortalezas de mejoras accionables.
- [ x ] Cerré con una conclusión.
