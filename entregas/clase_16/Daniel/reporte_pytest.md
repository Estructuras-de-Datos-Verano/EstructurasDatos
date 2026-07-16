#José Daniel Molina Carrillo

- comando ejecutado;
- python -m pytest -v
- salida completa;
 tests/test_publico_dijkstra_robusto.py::test_calcula_distancias_y_predecesores_conocidos PASSED                                                                                                    [  5%]
tests/test_publico_dijkstra_robusto.py::test_no_muta_listas_de_adyacencia PASSED                                                                                                                   [ 10%]
tests/test_publico_dijkstra_robusto.py::test_incluye_vecino_que_no_es_clave PASSED                                                                                                                 [ 15%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-1] PASSED                                                                                                                      [ 21%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-0.5] PASSED                                                                                                                    [ 26%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[inf] PASSED                                                                                                                    [ 31%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[-inf] PASSED                                                                                                                   [ 36%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[nan] PASSED                                                                                                                    [ 42%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[True] PASSED                                                                                                                 [ 47%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[3] PASSED                                                                                                                    [ 52%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[None] PASSED                                                                                                                 [ 57%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_arista_con_forma_incorrecta PASSED                                                                                                            [ 63%]
tests/test_publico_dijkstra_robusto.py::test_rechaza_origen_inexistente PASSED                                                                                                                     [ 68%]
tests/test_publico_dijkstra_robusto.py::test_destino_inalcanzable_conserva_infinito_y_camino_vacio PASSED                                                                                          [ 73%]
tests/test_publico_dijkstra_robusto.py::test_origen_igual_a_destino PASSED                                                                                                                         [ 78%]
tests/test_publico_dijkstra_robusto.py::test_reconstruccion_rechaza_ciclo PASSED                                                                                                                   [ 84%]
tests/test_publico_dijkstra_robusto.py::test_para_grafo_que_no_sea_mapping PASSED                                                                                                                  [ 89%]
tests/test_publico_dijkstra_robusto.py::test_donde_el_nombre_de_un_nodo_o_vecino_no_sea_str PASSED                                                                                                 [ 94%]
tests/test_publico_dijkstra_robusto.py::test_entrada_obsoleta PASSED                                                                                                                               [100%]

========================================================================================== 19 passed in 0.04s ===========================================================================================
- interpretación;
- el codigo ha corrido correcamente y los tests lo comprueban
- número de pruebas;
- 19
- cuántas pasaron;
- 19
- qué comportamiento verifican;
- los mencionados en el titulo de cada funcón 
- qué pruebas diseñaste tú;
3 test_para_grafo_que_no_sea_mapping, test_donde_el_nombre_de_un_nodo_o_vecino_no_sea_str, test_entrada_obsoleta
- qué caso importante todavía falta probar.
test_para_que_el_grafo_no_sea_mapping
