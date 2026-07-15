# reporte_pytest
## Codigo usado
```
py evaluar.py entregas/clase_15/Aristeo clase_15/tests entregas/clase_15/Aristeo/test_estudiante.py
```
## Salida
```
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
plugins: anyio-4.14.1
collected 14 items                                                                                                                                                                                                        

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED                                                                                                                   [  7%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED                                                                                                                             [ 14%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED                                                                                                                        [ 21%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED                                                                                                                               [ 28%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED                                                                                                                            [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED                                                                                                                                   [ 42%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED                                                                                                                                         [ 50%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED                                                                                                                                       [ 57%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED                                                                                                                                  [ 64%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED                                                                                                                                    [ 71%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED                                                                                                                                      [ 78%]
clase_15::test_distancia_mejora_multiples_veces <- ..\entregas\clase_15\Aristeo\test_estudiante.py PASSED                                                                                                           [ 85%]
clase_15::test_destino_inalcanzable <- ..\entregas\clase_15\Aristeo\test_estudiante.py PASSED                                                                                                                       [ 92%]
clase_15::test_ruta_indirecta_supera_directa_costosa <- ..\entregas\clase_15\Aristeo\test_estudiante.py PASSED                                                                                                      [100%]

=================================================================================================== 14 passed in 0.04s ===================================================================================================
```
## Pruebas hechas
14
## Pruebas pasadas
14
## Errores
0
## Que prueba 
- test_origen_tiene_distancia_cero_y_sin_predecesor
- test_bfs_no_basta_cuando_pesos_difieren
- test_red_ciudades_calcula_distancias_minimas
- test_predecesores_reconstruyen_camino
- test_nodo_inalcanzable_conserva_infinito
- test_camino_del_origen_a_si_mismo
- test_pesos_cero_son_validos 
- test_peso_negativo_se_rechaza
- test_origen_inexistente_se_rechaza 
- test_vecino_implicito_se_incluye
- test_no_muta_el_grafo_recibido
- test_distancia_mejora_multiples_veces
- test_destino_inalcanzable
- test_ruta_indirecta_supera_directa_costosa
## Pruebas propias
- test_distancia_mejora_multiples_veces
- test_destino_inalcanzable
- test_ruta_indirecta_supera_directa_costosa
