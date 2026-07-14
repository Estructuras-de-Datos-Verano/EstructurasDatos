Debe contener:

- comando ejecutado; python -m pytest -v 
- salida completa; 
tests/test_publico_heap.py::test_heap_nuevo_esta_vacio PASSED                                                                                                                                      [  6%]
tests/test_publico_heap.py::test_insertar_un_valor_y_consultar_minimo PASSED                                                                                                                       [ 13%]
tests/test_publico_heap.py::test_insertar_varios_conserva_minimo_y_propiedad PASSED                                                                                                                [ 20%]
tests/test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente PASSED                                                                                                                    [ 26%]
tests/test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer PASSED                                                                                                                   [ 33%]
tests/test_publico_heap.py::test_duplicados_y_negativos PASSED                                                                                                                                     [ 40%]
tests/test_publico_heap.py::test_construir_heap_reemplaza_contenido PASSED                                                                                                                         [ 46%]
tests/test_publico_heap.py::test_varios_sift_up PASSED                                                                                                                                             [ 53%]
tests/test_publico_heap.py::test_varios_sift_down PASSED                                                                                                                                           [ 60%]
tests/test_publico_heap.py::test_ultima_piedra[piedras0-0] PASSED                                                                                                                                  [ 66%]
tests/test_publico_heap.py::test_ultima_piedra[piedras1-5] PASSED                                                                                                                                  [ 73%]
tests/test_publico_heap.py::test_ultima_piedra[piedras2-0] PASSED                                                                                                                                  [ 80%]
tests/test_publico_heap.py::test_ultima_piedra[piedras3-1] PASSED                                                                                                                                  [ 86%]
tests/test_publico_heap.py::test_varios_cambios PASSED                                                                                                                                             [ 93%]
tests/test_publico_heap.py::test_ultima_piedra_extremo PASSED                                                                                                                                      [100%]

========================================================================================== 15 passed in 0.03s ===========================================================================================

- interpretación;
- pasaron todas las pruebas
- número de pruebas;
- 15 pruebas
- cuántas pasaron;
- las 15
- qué comportamiento verifican;
- todos los mencionados en el nombre de la función
- qué pruebas diseñaste tú;
- 3  ultima piedra, varios cambios y ultima piedra extreo
- qué caso importante todavía falta probar.
- def test_grande _antidad_de_elementos