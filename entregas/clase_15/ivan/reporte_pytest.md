Comando: python evaluar.py entregas/clase_15/ivan clase_15/tests entregas/clase_15/ivan/test_estudiante.py;
Salida:
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos>  python evaluar.py entregas/clase_15/ivan clase_15/tests entregas/clase_15/ivan/test_estudiante.py;
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_15\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_15\ivan\test_estudiante.py

============================================================================ test session starts =============================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
plugins: anyio-4.7.0
collected 14 items                                                                                                                                                            

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED                                                                       [  7%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED                                                                                 [ 14%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED                                                                            [ 21%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED                                                                                   [ 28%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED                                                                                [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED                                                                                       [ 42%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED                                                                                             [ 50%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED                                                                                           [ 57%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED                                                                                      [ 64%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED                                                                                        [ 71%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED                                                                                          [ 78%]
clase_15::test_camino_mejora_dos_veces <- ..\entregas\clase_15\ivan\test_estudiante.py PASSED                                                                           [ 85%]
clase_15::test_destino_inalcanzable <- ..\entregas\clase_15\ivan\test_estudiante.py PASSED                                                                              [ 92%]
clase_15::test_entrada_obsoleta_con_ruta_directa_costosa <- ..\entregas\clase_15\ivan\test_estudiante.py PASSED                                                         [100%]

============================================================================= 14 passed in 0.09s =============================================================================;
Cantidad de pruebas: 14;
Ningún error, pasaron 14;
Casos propios: 
- Un camino que mejora dos veces
- Destino Inalcanzable
- Entrada obsoleta
