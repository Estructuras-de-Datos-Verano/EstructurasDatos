# Reporte
## Comando: Primero cd entregas/clase_06/ivan y luego python -m pytest -v
## Salida:  PS C:\Users\0286945\Documents\GitHub\EstructurasDatos\entregas\clase_06\ivan> python -m pytest -v
========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286945\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286945\Documents\GitHub\EstructurasDatos\entregas\clase_06
configfile: pytest.ini
plugins: anyio-4.14.0
collected 7 items                                                                                                                                                                                        

tests\test_publico_josephus.py::test_validar_n_rechaza_cero PASSED                                                                                                                                 [ 14%]
tests\test_publico_josephus.py::test_formatear_salida PASSED                                                                                                                                       [ 28%]
tests\test_publico_josephus.py::test_caso_minimo PASSED                                                                                                                                            [ 42%]
tests\test_publico_josephus.py::test_caso_dos_ninos PASSED                                                                                                                                         [ 57%]
tests\test_publico_josephus.py::test_ejemplo_oficial PASSED                                                                                                                                        [ 71%]
tests\test_publico_josephus.py::test_resultado_contiene_todos_los_ninos_una_vez PASSED                                                                                                             [ 85%]
tests\test_publico_josephus.py::test_resolver_desde_texto_si_existe PASSED                                                                                                                         [100%]

=========================================================================================== 7 passed in 0.03s ===========================================================================================
## Interpretación: Se ejecutaron correctamente las pruebas de los 7 tests públicos. En este caso, todas pasaron y verifica casos cuando la longitud del deque es cero, verifica el formateo de los formatos de los enteros, hace un caso mínimo para probar funcionalidad con un niño, luego con dos, luego ejecuta un ejemplo, después checa que todos los niños aparecen una sola vez y finalmente checa que la función de resolver desde texto funcione