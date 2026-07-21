## Reporte pytest Clase 14 - José Iván Reyna Blanco


## Comando
python evaluar.py entregas/clase_14/ivan clase_14/tests entregas/clase_14/ivan/test_estudiante.py

## Salida completa:

```powershell
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_14/ivan clase_14/tests entregas/clase_14/ivan/test_estudiante.py

Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_14\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_14\ivan\test_estudiante.py

===================================================================== test session starts =====================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_14
configfile: pytest.ini
plugins: anyio-4.7.0
collected 29 items                                                                                                                                             

clase_14\tests\test_publico_heap.py::test_heap_nuevo_esta_vacio PASSED                                                                                   [  3%]
clase_14\tests\test_publico_heap.py::test_insertar_un_valor_y_consultar_minimo PASSED                                                                    [  6%]
clase_14\tests\test_publico_heap.py::test_insertar_varios_conserva_minimo_y_propiedad PASSED                                                             [ 10%]
clase_14\tests\test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente PASSED                                                                 [ 13%]
clase_14\tests\test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer PASSED                                                                [ 17%]
clase_14\tests\test_publico_heap.py::test_duplicados_y_negativos PASSED                                                                                  [ 20%]
clase_14\tests\test_publico_heap.py::test_construir_heap_reemplaza_contenido PASSED                                                                      [ 24%]
clase_14\tests\test_publico_heap.py::test_varios_sift_up PASSED                                                                                          [ 27%]
clase_14\tests\test_publico_heap.py::test_varios_sift_down PASSED                                                                                        [ 31%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras0-0] PASSED                                                                               [ 34%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras1-5] PASSED                                                                               [ 37%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras2-0] PASSED                                                                               [ 41%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras3-1] PASSED                                                                               [ 44%]
clase_14::test_heap_nuevo_esta_vacio <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                              [ 48%]
clase_14::test_insertar_un_valor_y_consultar_minimo <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                               [ 51%]
clase_14::test_insertar_varios_conserva_minimo_y_propiedad <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                        [ 55%]
clase_14::test_extraer_minimo_devuelve_orden_creciente <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                            [ 58%]
clase_14::test_vacio_lanza_error_al_consultar_o_extraer <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                           [ 62%]
clase_14::test_duplicados_y_negativos <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                             [ 65%]
clase_14::test_construir_heap_reemplaza_contenido <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                 [ 68%]
clase_14::test_varios_sift_up <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                                     [ 72%]
clase_14::test_varios_sift_down <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                                   [ 75%]
clase_14::test_ultima_piedra[piedras0-0] <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                          [ 79%]
clase_14::test_ultima_piedra[piedras1-5] <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                          [ 82%]
clase_14::test_ultima_piedra[piedras2-0] <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                          [ 86%]
clase_14::test_ultima_piedra[piedras3-1] <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                          [ 89%]
clase_14::test_insercion_multiples_cambios <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                        [ 93%]
clase_14::test_extraccion_multiples_niveles <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                       [ 96%]
clase_14::test_ultima_piedra_caso_extremo <- ..\entregas\clase_14\ivan\test_estudiante.py PASSED                                                         [100%]

===================================================================== 29 passed in 0.12s ======================================================================
```
## Número de pruebas
29

## Aprobadas
29

## Errores
Ninguno

## Prueba propia
Inserción de mútiples cambios, niveles y test de última piedra en caso extremo.
```python
def test_insercion_multiples_cambios():
    # Insertar un mínimo global en un heap ya formado hará que suba hasta la raíz
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    heap.insertar(5)
    assert heap.minimo() == 5
    assert heap.cumple_propiedad_heap()


def test_extraccion_multiples_niveles():
    # Al extraer el 10, el 70 sube a la raíz y tiene que hacer sift-down intercambiándose con el 20 y luego con el 40
    heap = HeapMin([10, 20, 30, 40, 50, 60, 70])
    minimo = heap.extraer_min()
    assert minimo == 10
    assert heap.minimo() == 20
    assert heap.cumple_propiedad_heap()


def test_ultima_piedra_caso_extremo():
    # Caso donde todas las piedras tienen el mismo peso y son una cantidad impar
    assert ultima_piedra([100, 100, 100, 100, 100]) == 100
    # Caso con un peso masivo que pulveriza al resto en cascada
    assert ultima_piedra([1000, 500, 250, 250]) == 0

```

## Caso pendiente.
Ninguno.
