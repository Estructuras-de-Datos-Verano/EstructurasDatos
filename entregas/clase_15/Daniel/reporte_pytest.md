Debe contener:

- comando ejecutado;
- python -m pytest -v 
- salida completa;
- tests/test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED                                                                                                                                                           [  7%]
tests/test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED                                                                                                                                                                     [ 14%]
tests/test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED                                                                                                                                                                [ 21%]
tests/test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED                                                                                                                                                                       [ 28%]
tests/test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED                                                                                                                                                                    [ 35%]
tests/test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED                                                                                                                                                                           [ 42%]
tests/test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED                                                                                                                                                                                 [ 50%]
tests/test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED                                                                                                                                                                               [ 57%]
tests/test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED                                                                                                                                                                          [ 64%]
tests/test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED                                                                                                                                                                            [ 71%]
tests/test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED                                                                                                                                                                              [ 78%]
tests/test_publico_dijkstra.py::test_distancia_mejorada_varias_veces PASSED                                                                                                                                                                        [ 85%]
tests/test_publico_dijkstra.py::test_destino_inalcanzable PASSED                                                                                                                                                                                   [ 92%]
tests/test_publico_dijkstra.py::test_entrada_obsoleta PASSED                                                                                                                                                                                       [100%]

================================================================================================================== 14 passed in 0.04s ===================================================================================================================
- interpretación;
- las pruebas corrieron correctamente por tanto la implementacion esta bien
- número de pruebas;
- 14
- cuántas pasaron;
- 14
- qué comportamiento verifican;
- los que mencionan sus titulos
- qué pruebas diseñaste tú;
- 3 test_distancia_mejorada_varias_veces,  test_destino_inalcanzable,  test_entrada_obsoleta 
- qué caso importante todavía falta probar.
- test_ruta_indirecta_supera_directa_costosa():
