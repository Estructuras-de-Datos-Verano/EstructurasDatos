python -m pytest -v

---
==================================================================== test session starts =====================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_06
configfile: pytest.ini
collected 7 items                                                                                                                                             

tests/test_publico_josephus.py::test_validar_n_rechaza_cero PASSED                                                                                      [ 14%]
tests/test_publico_josephus.py::test_formatear_salida PASSED                                                                                            [ 28%]
tests/test_publico_josephus.py::test_caso_minimo PASSED                                                                                                 [ 42%]
tests/test_publico_josephus.py::test_caso_dos_ninos PASSED                                                                                              [ 57%]
tests/test_publico_josephus.py::test_ejemplo_oficial PASSED                                                                                             [ 71%]
tests/test_publico_josephus.py::test_resultado_contiene_todos_los_ninos_una_vez PASSED                                                                  [ 85%]
tests/test_publico_josephus.py::test_resolver_desde_texto_si_existe PASSED                                                                              [100%]

===================================================================== 7 passed in 0.01s ======================================================================

---
7 pruebas, 7 pasaron, verifican: validar n, formatear salida, caso minimo, caso dos niuños, ejemplo oficial, test_resultado_contiene_todos_los_ninos_una_vez y test_resolver_desde_texto_si_existe
,