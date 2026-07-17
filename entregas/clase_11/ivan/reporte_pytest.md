- comando ejecutado:
´´´ text
C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_11/ivan clase_11/tests
- salida completa;
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_11/ivan clase_11/tests
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_11\tests

================================================================ test session starts ================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_11
configfile: pytest.ini
plugins: anyio-4.7.0
collected 12 items                                                                                                                                   

clase_11\tests\test_publico_arboles.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                      [  8%]
clase_11\tests\test_publico_arboles.py::test_crear_arbol_vacio PASSED                                                                          [ 16%]
clase_11\tests\test_publico_arboles.py::test_arbol_vacio_no_contiene_valores PASSED                                                            [ 25%]
clase_11\tests\test_publico_arboles.py::test_insertar_un_valor PASSED                                                                          [ 33%]
clase_11\tests\test_publico_arboles.py::test_buscar_valor_existente_e_inexistente PASSED                                                       [ 41%]
clase_11\tests\test_publico_arboles.py::test_insertar_varios_valores_inorden_ordenado PASSED                                                   [ 50%]
clase_11\tests\test_publico_arboles.py::test_altura_de_arbol_con_varios_niveles PASSED                                                         [ 58%]
clase_11\tests\test_publico_arboles.py::test_no_insertar_duplicados PASSED                                                                     [ 66%]
clase_11\tests\test_publico_arboles.py::test_todo_preorden PASSED                                                                              [ 75%]
clase_11\tests\test_publico_arboles.py::test_todo_postorden PASSED                                                                             [ 83%]
clase_11\tests\test_publico_arboles.py::test_todo_insercion_en_orden_creciente PASSED                                                          [ 91%]
clase_11\tests\test_publico_arboles.py::test_todo_repetido_no_aparece_dos_veces PASSED                                                         [100%]

================================================================ 12 passed in 0.05s =================================================================;
´´´

- interpretación: Se ejecutaron todas bien ;
- cuántas pruebas se ejecutaron: 12;
- cuántas pasaron: 12 ;
- si hubo errores: No ;
- qué comportamiento verifican: Escenarios límite como árboles vacíos, verificar que no se dupliquen nodos, que el órden de búsqueda sea correcto (y funcione), que la raíz sea la correcta, inserciones correctas, que no se inserten valores dobles, etc;
- qué prueba diseñaste tú en `test_estudiante.py`: Pruebas que verifican que las alturas se midan correctamente en árboles nulos o unitarios y que un árbol dado se vea como se tiene que ver construyéndolo usando insertar;
- qué caso todavía falta probar: Me gustaría otra prueba que construya al diccionario y cheque su forma pero en vez de usar el atributo que use el método inorden.