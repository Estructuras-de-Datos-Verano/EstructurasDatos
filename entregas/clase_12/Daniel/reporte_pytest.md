comando ejecutado;
 pytest -v

salida completa;
tests/test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                                               [  6%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                                                                               [ 13%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                                                                            [ 20%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                                                                          [ 26%]
tests/test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                                                                          [ 33%]
tests/test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                                          [ 40%]
tests/test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                                     [ 46%]
tests/test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                                     [ 53%]
tests/test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                                            [ 60%]
tests/test_publico_bst_balance.py::test_todo_busqueda_balanceada PASSED                                                                                                                            [ 66%]
tests/test_publico_bst_balance.py::test_todo_busqueda_degenerada PASSED                                                                                                                            [ 73%]
tests/test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima PASSED                                                                                                               [ 80%]
tests/test_publico_bst_balance.py::test_busqueda_en_arbol_balanceado_cuenta_comparaciones_correctas PASSED                                                                                         [ 86%]
tests/test_publico_bst_balance.py::test_insercion_ordenada_produce_altura_maxima_y_arbol_degenerado PASSED                                                                                         [ 93%]
tests/test_publico_bst_balance.py::test_recorrido_preorden_y_postorden_son_coherentes PASSED                                                                                                       [100%]

========================================================================================== 15 passed in 0.03s ===========================================================================================
 
interpretación; todas pasaron
cuántas pruebas se ejecutaron;
15
cuántas pasaron; 15
si hubo errores; no
qué comportamiento verifican;los mencionados en su nombre
qué prueba diseñaste tú; donde cuanta la comparaciones correctas
qué caso todavía falta probar. ninguno