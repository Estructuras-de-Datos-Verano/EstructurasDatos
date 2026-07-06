Comando ejecutado: cd clase_07; python -m pytest -v
Salida: ========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286945\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286945\Documents\GitHub\EstructurasDatos\clase_07
configfile: pytest.ini
testpaths: tests
collected 7 items                                                                                                                                                                                        

tests/test_publico_nearest_smaller.py::test_ejemplo_oficial_nearest_smaller PASSED                                                                                                                 [ 14%]
tests/test_publico_nearest_smaller.py::test_arreglo_creciente PASSED                                                                                                                               [ 28%]
tests/test_publico_nearest_smaller.py::test_arreglo_decreciente PASSED                                                                                                                             [ 42%]
tests/test_publico_nearest_smaller.py::test_todo_valores_iguales PASSED                                                                                                                            [ 57%]
tests/test_publico_nearest_smaller.py::test_todo_error_comparacion_estricta PASSED                                                                                                                 [ 71%]
tests/test_publico_nearest_smaller.py::test_todo_caso_limite PASSED                                                                                                                                [ 85%]
tests/test_publico_nearest_smaller.py::test_todo_variante_nearest_greater PASSED                                                                                                                   [100%]

=========================================================================================== 7 passed in 0.02s ===========================================================================================
Interpretación: Funciona correctamente la función con listas crecientes, decrecientes, monótonas, con comparación estricta da error.
Ejecuciones: Todas se ejectutaron
Pasaron: Todas
Pruebas que diseñé: 
def test_valores_mayores_decreciente():
    """Si la lista va bajando, cada número tiene como mayor cercano al de su izquierda."""
    assert valores_mayores_cercanos([30, 20, 10]) == [0, 1, 2]

def test_valores_menores_creciente():
    """Si la lista va subiendo, cada número tiene como menor cercano al de su izquierda."""
    assert valores_mayores_cercanos([10, 20, 30]) == [0, 1, 2]
def test_valores_menores_negativos():
    """Debe comportarse igual con los signos negativos"""
    assert valores_menores_cercanos([-2, -1, 0]) == [0, 1, 2]
Caso faltante: Ninguno