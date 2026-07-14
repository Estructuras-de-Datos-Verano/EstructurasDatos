# reporte_pytest
## Cóigo usado
```
py evaluar.py entregas/clase_14/Aristeo clase_14/tests entregas/clase_14/Aristeo/test_estudiante.py
```
## Salida
```

================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_14
configfile: pytest.ini
collected 17 items                                                                                                                                                                                                        

clase_14\tests\test_publico_heap.py::test_heap_nuevo_esta_vacio PASSED                                                                                                                                              [  5%]
clase_14\tests\test_publico_heap.py::test_insertar_un_valor_y_consultar_minimo PASSED                                                                                                                               [ 11%]
clase_14\tests\test_publico_heap.py::test_insertar_varios_conserva_minimo_y_propiedad PASSED                                                                                                                        [ 17%]
clase_14\tests\test_publico_heap.py::test_extraer_minimo_devuelve_orden_creciente PASSED                                                                                                                            [ 23%]
clase_14\tests\test_publico_heap.py::test_vacio_lanza_error_al_consultar_o_extraer PASSED                                                                                                                           [ 29%]
clase_14\tests\test_publico_heap.py::test_duplicados_y_negativos PASSED                                                                                                                                             [ 35%]
clase_14\tests\test_publico_heap.py::test_construir_heap_reemplaza_contenido PASSED                                                                                                                                 [ 41%]
clase_14\tests\test_publico_heap.py::test_varios_sift_up PASSED                                                                                                                                                     [ 47%]
clase_14\tests\test_publico_heap.py::test_varios_sift_down PASSED                                                                                                                                                   [ 52%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras0-0] PASSED                                                                                                                                          [ 58%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras1-5] PASSED                                                                                                                                          [ 64%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras2-0] PASSED                                                                                                                                          [ 70%]
clase_14\tests\test_publico_heap.py::test_ultima_piedra[piedras3-1] PASSED                                                                                                                                          [ 76%]
clase_14::test_insercion_recorre_varios_niveles_hasta_raiz <- ..\entregas\clase_14\Aristeo\test_estudiante.py PASSED                                                                                                [ 82%]
clase_14::test_extraccion_desciende_multiples_niveles <- ..\entregas\clase_14\Aristeo\test_estudiante.py PASSED                                                                                                     [ 88%]
clase_14::test_ultima_piedra_caso_complejo <- ..\entregas\clase_14\Aristeo\test_estudiante.py PASSED                                                                                                                [ 94%]
clase_14::test_heap_con_muchos_duplicados <- ..\entregas\clase_14\Aristeo\test_estudiante.py PASSED                                                                                                                 [100%]

=================================================================================================== 17 passed in 0.04s ===================================================================================================
```

## Pruebas hechas
17
## Pasadas
17
## Errores
0
## Que comprueban
- test_heap_nuevo_esta_vacio
- test_insertar_un_valor_y_consultar_minimo
- test_insertar_varios_conserva_minimo_y_propiedad
- test_extraer_minimo_devuelve_orden_creciente
- test_vacio_lanza_error_al_consultar_o_extraer
- test_duplicados_y_negativos
- test_construir_heap_reemplaza_contenido
- test_varios_sift_up 
- test_varios_sift_down
- test_ultima_piedra[piedras0-0]
- test_ultima_piedra[piedras1-5]
- test_ultima_piedra[piedras2-0]
- test_ultima_piedra[piedras3-1]
- test_insercion_recorre_varios_niveles_hasta_raiz
- test_heap_con_muchos_duplicados
- test_extraccion_desciende_multiples_niveles
- test_ultima_piedra_caso_complejo

