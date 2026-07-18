ebe contener:

- comando ejecutado;
- python -m pytest -v
- salida completa;
-  tests/test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil0-BFS-cola-capas-O(V+E)] PASSED                                                                                                                                  [  2%]
tests/test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil1-0-1 BFS-deque-0/1-O(V+E)] PASSED                                                                                                                               [  5%]
tests/test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil2-Dijkstra-heap-distancia-log V] PASSED                                                                                                                          [  7%]
tests/test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil3-Kruskal-Union-Find-componentes-E log E] PASSED                                                                                                                 [ 10%]
tests/test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil4-Kahn-cola + grados de entrada-grado de entrada cero-O(V+E)] PASSED                                                                                             [ 13%]
tests/test_publico_seleccion_estrategias.py::test_bfs_admite_grafo_dirigido_y_no_dirigido PASSED                                                                                                                                                   [ 15%]
tests/test_publico_seleccion_estrategias.py::test_kruskal_admite_pesos_negativos PASSED                                                                                                                                                            [ 18%]
tests/test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil0] PASSED                                                                                                                                [ 21%]
tests/test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil1] PASSED                                                                                                                                [ 23%]
tests/test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil2] FAILED                                                                                                                                [ 26%]
tests/test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil3] PASSED                                                                                                                                [ 28%]
tests/test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil4] PASSED                                                                                                                                [ 31%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil0] PASSED                                                                                                                                                  [ 34%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil1] PASSED                                                                                                                                                  [ 36%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[None] PASSED                                                                                                                                                             [ 39%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil1] PASSED                                                                                                                                                          [ 42%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil2] PASSED                                                                                                                                                          [ 44%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil3] PASSED                                                                                                                                                          [ 47%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil4] PASSED                                                                                                                                                          [ 50%]
tests/test_publico_seleccion_estrategias.py::test_es_aplicable_compara_con_el_contrato_completo PASSED                                                                                                                                             [ 52%]
tests/test_publico_seleccion_estrategias.py::test_explicar_descarte_nombra_limite_y_recomendacion PASSED                                                                                                                                           [ 55%]
tests/test_publico_seleccion_estrategias.py::test_explicar_algoritmo_correcto_confirma_operacion PASSED                                                                                                                                            [ 57%]
tests/test_publico_seleccion_estrategias.py::test_evaluar_propuesta_correcta PASSED                                                                                                                                                                [ 60%]
tests/test_publico_seleccion_estrategias.py::test_evaluar_propuesta_detecta_algoritmo_y_estructura PASSED                                                                                                                                          [ 63%]
tests/test_publico_seleccion_estrategias.py::test_evaluar_propuesta_fuera_de_alcance_no_la_acepta PASSED                                                                                                                                           [ 65%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[Bellman-Ford] PASSED                                                                                                                              [ 68%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[A*] PASSED                                                                                                                                        [ 71%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[] PASSED                                                                                                                                          [ 73%]
tests/test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[3] PASSED                                                                                                                                         [ 76%]
tests/test_publico_seleccion_estrategias.py::test_perfil_y_decision_son_inmutables PASSED                                                                                                                                                          [ 78%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_bfs_vs_dijkstra PASSED                                                                                                                                                                [ 81%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_cero_uno_bfs_vs_bfs PASSED                                                                                                                                                            [ 84%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_dijkstra_vs_kruskal PASSED                                                                                                                                                            [ 86%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_bfs_vs_kahn PASSED                                                                                                                                                                    [ 89%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_pesos_negativos_fuera_alcance PASSED                                                                                                                                                  [ 92%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_kruskal_con_peso_negativo PASSED                                                                                                                                                      [ 94%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_error_solo_estructura PASSED                                                                                                                                                          [ 97%]
tests/test_publico_seleccion_estrategias.py::test_estudiante_perfil_invalido PASSED                                                                                                                                                                [100%]

======================================================================================================================= FAILURES ========================================================================================================================
- interpretación;
- pasaron la mayor parte de las pruebas
- número de pruebas;
- 38
- cuántas pasaron;
- 37
- qué comportamiento verifican;
- los indicados en sus nombres
- qué pruebas diseñaste tú;
las ultimas 8
- qué caso importante todavía falta probar.
- def test_estudiante_perfil_invalido():