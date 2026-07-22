comando ejecutado;
- python -m pytest -v
salida completa;
tests/test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED                                                                                                                      [  8%]
tests/test_publico_avl.py::test_arbol_vacio PASSED                                                                                                                                                 [ 16%]
tests/test_publico_avl.py::test_insercion_y_busqueda_basica PASSED                                                                                                                                 [ 25%]
tests/test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha PASSED                                                                                                                             [ 33%]
tests/test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda PASSED                                                                                                                           [ 41%]
tests/test_publico_avl.py::test_caso_lr_aplica_rotacion_doble PASSED                                                                                                                               [ 50%]
tests/test_publico_avl.py::test_caso_rl_aplica_rotacion_doble PASSED                                                                                                                               [ 58%]
tests/test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED                                                                                                              [ 66%]
tests/test_publico_avl.py::test_duplicados_no_se_insertan PASSED                                                                                                                                   [ 75%]
tests/test_publico_avl.py::test_arbol_grande PASSED                                                                                                                                                [ 83%]
tests/test_publico_avl.py::test_numeros_negativos PASSED                                                                                                                                           [ 91%]
tests/test_publico_avl.py::test_mezcla_numeros_positivos_y_negativos PASSED                                                                                                                        [100%]

========================================================================================== 12 passed in 0.03s ==========================================================================================


interpretación;
 - es decir pasaron todas las pruebas
número de pruebas;
- 12 pruebas totales, 9 publicas y tres propias
cuántas pasaron;
- las 12 pasaron
qué comportamiento verifican; +
- los mencionados en sus respectivoas titulos
qué pruebas diseñaste tú;
- tres la de arbol grande, numeros negativos y mezcla numeros positivos y negativoas
qué caso importante todavía falta probar.
 puede ser un arbol grande de numeros positivos 