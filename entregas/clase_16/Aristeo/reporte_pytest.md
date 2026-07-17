# reporte_pytest
## Codigo usado
```
py evaluar.py entregas/clase_16/Aristeo clase_16/tests entregas/clase_16/Aristeo/test_estudiante.py
```
## Salida
``` py
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_16
configfile: pytest.ini
plugins: anyio-4.14.1
collected 23 items                                                                                                                                                                                                        

clase_16\tests\test_publico_dijkstra_robusto.py::test_calcula_distancias_y_predecesores_conocidos PASSED                                                                                                            [  4%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_no_muta_listas_de_adyacencia PASSED                                                                                                                           [  8%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_incluye_vecino_que_no_es_clave PASSED                                                                                                                         [ 13%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-1] PASSED                                                                                                                              [ 17%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-0.5] PASSED                                                                                                                            [ 21%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[inf] PASSED                                                                                                                            [ 26%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[-inf] PASSED                                                                                                                           [ 30%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[nan] PASSED                                                                                                                            [ 34%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[True] PASSED                                                                                                                         [ 39%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[3] PASSED                                                                                                                            [ 43%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[None] PASSED                                                                                                                         [ 47%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_arista_con_forma_incorrecta PASSED                                                                                                                    [ 52%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_origen_inexistente PASSED                                                                                                                             [ 56%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_destino_inalcanzable_conserva_infinito_y_camino_vacio PASSED                                                                                                  [ 60%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_origen_igual_a_destino PASSED                                                                                                                                 [ 65%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_reconstruccion_rechaza_ciclo PASSED                                                                                                                           [ 69%]
clase_16::test_bool_no_se_acepta_como_peso <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                                [ 73%]
clase_16::test_vecino_implicito_y_no_mutacion <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                             [ 78%]
clase_16::test_entrada_obsoleta_heap <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                                      [ 82%]
clase_16::test_nan_o_infinito_lanzan_value_error <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                          [ 86%]
clase_16::test_ciclo_de_predecesores_lanza_value_error <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                    [ 91%]
clase_16::test_grafo_no_es_mapping <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                                        [ 95%]
clase_16::test_nodo_no_es_str <- ..\entregas\clase_16\Aristeo\test_estudiante.py PASSED                                                                                                                             [100%]

=================================================================================================== 23 passed in 0.06s ===================================================================================================
```
## Pruebas realizadas
23
## PRuebas aporbadas
23
## Errores
0
## Que prueban
- test_calcula_distancias_y_predecesores_conocidos
- test_no_muta_listas_de_adyacencia
- test_incluye_vecino_que_no_es_clave
- test_rechaza_peso_negativo[-1]
- test_rechaza_peso_negativo[-0.5]
- test_rechaza_peso_no_finito[inf] 
- test_rechaza_peso_no_finito[-inf]
- test_rechaza_peso_no_finito[nan]
- test_rechaza_peso_no_numerico[True]
- test_rechaza_peso_no_numerico[3] 
- test_rechaza_peso_no_numerico[None]
- test_rechaza_arista_con_forma_incorrecta 
- test_rechaza_origen_inexistente
- test_destino_inalcanzable_conserva_infinito_y_camino_vacio
- test_origen_igual_a_destino
- test_reconstruccion_rechaza_ciclo
- test_bool_no_se_acepta_como_peso
- test_vecino_implicito_y_no_mutacion
- test_entrada_obsoleta_heap
- test_nan_o_infinito_lanzan_value_error
- test_ciclo_de_predecesores_lanza_value_error
- test_grafo_no_es_mapping
- test_nodo_no_es_str

## Mis pruebas
- test_bool_no_se_acepta_como_peso
- test_vecino_implicito_y_no_mutacion
- test_entrada_obsoleta_heap
- test_nan_o_infinito_lanzan_value_error
- test_ciclo_de_predecesores_lanza_value_error
- test_grafo_no_es_mapping
- test_nodo_no_es_str
