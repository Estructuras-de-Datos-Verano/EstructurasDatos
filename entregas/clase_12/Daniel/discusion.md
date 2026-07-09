# Discusión técnica

## 1. ¿Un BST siempre es eficiente?
- en general si
## 2. Lista vs BST
- gana el Bst
## 3. Altura y comparaciones
- en este caso si es mas eficiente el BST
## 4. Árbol balanceado vs árbol degenerado
- me gusta mas el arbol degenerado
## 5. Orden de inserción
- depende del problema pero el visto en clase fue muy instructivo
## 6. Complejidad 
- esta clase no fue tan dificil
## 7. Experimentos y evidencia 
- se cumplieron todos
## 8. Animaciones
- muy instructivas
## 9. Pruebas propias
- dificil cokearlas pero si salieron
## 10. Revisión técnica del PR
- Ejecutando:
C:\Program Files\Python314\python.exe -m pytest -v C:\Users\0285489\Documents\GitHub\EstructurasDatos\clase_12\tests C:\Users\0285489\Documents\GitHub\EstructurasDatos\entregas\clase_12\Santiago_Vazquez\test_estudiante.py

========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0285489\Documents\GitHub\EstructurasDatos\clase_12
configfile: pytest.ini
collected 18 items                                                                                                                                                                                       

clase_12\tests\test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                                      [  5%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                                                                      [ 11%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                                                                   [ 16%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                                                                 [ 22%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                                                                 [ 27%]
clase_12\tests\test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                                 [ 33%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                            [ 38%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                            [ 44%]
clase_12\tests\test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                                   [ 50%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_balanceada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol balanceado.)                                                [ 55%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_degenerada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol degenerado.)                                                [ 61%]
clase_12\tests\test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima SKIPPED (TODO alumno: diseña una prueba de altura máxima por inserción ordenada.)                           [ 66%]
clase_12\tests\test_publico_bst_balance.py::test_arbol_totalmente_vacio PASSED                                                                                                                     [ 72%]
clase_12\tests\test_publico_bst_balance.py::test_arbol_con_un_solo_nodo PASSED                                                                                                                     [ 77%]
clase_12\tests\test_publico_bst_balance.py::test_arbol_en_linea_recta PASSED                                                                                                                       [ 83%]
clase_12::test_arbol_totalmente_vacio PASSED                                                                                                                                                       [ 88%]
clase_12::test_arbol_con_un_solo_nodo PASSED                                                                                                                                                       [ 94%]
clase_12::test_arbol_en_linea_recta PASSED                                                                                                                                                         [100%]

===================================================================================== 15 passed, 3 skipped in 0.04s =====================================================================================


### Observacion:


Pasaron 15 limpitas

3 skippearon 

Su código aguantó mis pruebas  (`test_arbol_totalmente_vacio`, `test_arbol_con_un_solo_nodo` y el de la línea recta). Eso significa que programó bien los punteros, no se mueren cuando encuentra un `None` y calcula la altura y la degeneración sin problemas.

En la consola saltaron 3 SKIPPED (`test_todo_busqueda_balanceada`, `test_todo_busqueda_degenerada` y `test_todo_insercion_ordenada_altura_maxima`). O sea, se le olvidó borrar el `@pytest.mark.skip` y no programó las pruebas obligatorias que venían como tarea. Su árbol funciona, pero dejó la entrega a medias.

Revisar el PR de alguien más no es solo ver si el código truena o no. Al cruzar los archivos saltó al tiro que, aunque su lógica matemática está bien, se le barrió por completo limpiar los pendientes del entregable.

## 11. Problemas relacionados
- la verdad de pie a una amplia gama de problemas que se pueden solucionar con esto
## 12. Pregunta abierta
- por que los arboles crecen logaritmicamente en sus iteraciones?