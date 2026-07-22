# reporte_pytest
## Comando ejecutado
```
python -m pytest -v
```
## Salida completa
```
====================================================================================== test session starts =======================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_12
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.14.1
collected 12 items                                                                                                                                                                                

tests/test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                                        [  8%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                                                                        [ 16%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                                                                     [ 25%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                                                                   [ 33%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                                                                   [ 41%]
tests/test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                                   [ 50%]
tests/test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                              [ 58%]
tests/test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                              [ 66%]
tests/test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                                     [ 75%]
tests/test_publico_bst_balance.py::test_todo_busqueda_balanceada PASSED                                                                                                                     [ 83%]
tests/test_publico_bst_balance.py::test_todo_busqueda_degenerada PASSED                                                                                                                     [ 91%]
tests/test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima PASSED                                                                                                        [100%]

======================================================================================= 12 passed in 0.04s =======================================================================
```
## Interpretación
Todas las pruebas jalaron
## Cuántas pruebas se ejecutaron
12
## Cuántas pasaron
12
## Si hubo errores
No hubo errores
## Qué comportamiento verifican
- test_nodo_guarda_valor_y_empieza_sin_hijos
- test_altura_de_arbol_vacio
- test_altura_de_arbol_con_raiz
- test_altura_de_arbol_balanceado
- test_altura_de_arbol_degenerado
- test_inorden_sigue_regresando_valores_ordenados
- test_busqueda_con_conteo_de_comparaciones_balanceado
- test_busqueda_con_conteo_de_comparaciones_degenerado
- test_duplicados_no_aumentan_cantidad_de_nodos
- test_todo_busqueda_balanceada
- test_todo_busqueda_degenerada
## Qué prueba diseñaste tú
- test_todo_busqueda_balanceada
- test_todo_busqueda_degenerada
- test_todo_insercion_ordenada_altura_maxima
## Qué caso todavía falta probar.
arbol degenerado hacia la izquierda.