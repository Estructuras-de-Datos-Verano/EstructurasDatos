

##  Comando Ejecutado

Para asegurarnos de que Python encontrara correctamente los archivos de nuestra carpeta de entrega sin enredarse con las rutas, usamos el script oficial del curso:

```bash
python3 evaluar.py entregas/clase_11/mi_nombre clase_11/tests


============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: /home/usuario/proyectos/curso-alumnos
collected 12 items

clase_11/tests/test_publico_arboles.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED [  8%]
clase_11/tests/test_publico_arboles.py::test_crear_arbol_vacio PASSED                     [ 16%]
clase_11/tests/test_publico_arboles.py::test_arbol_vacio_no_contiene_valores PASSED       [ 25%]
clase_11/tests/test_publico_arboles.py::test_insertar_un_valor PASSED                     [ 33%]
clase_11/tests/test_publico_arboles.py::test_buscar_valor_existente_e_inexistente PASSED   [ 41%]
clase_11/tests/test_publico_arboles.py::test_insertar_varios_valores_inorden_ordenado PASSED [ 50%]
clase_11/tests/test_publico_arboles.py::test_altura_de_arbol_con_varios_niveles PASSED    [ 58%]
clase_11/tests/test_publico_arboles.py::test_no_insertar_duplicados PASSED                [ 66%]
test_estudiante.py::test_todo_preorden PASSED                                              [ 75%]
test_estudiante.py::test_todo_postorden PASSED                                             [ 83%]
test_estudiante.py::test_todo_insercion_en_orden_creciente PASSED                          [ 91%]
test_estudiante.py::test_todo_repetido_no_aparece_dos_veces PASSED                         [100%]

============================== 12 passed in 0.06s ==============================