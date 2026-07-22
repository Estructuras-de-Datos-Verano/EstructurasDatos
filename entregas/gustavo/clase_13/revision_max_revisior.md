# Revisión de PR Max

## Resumen

Mi compañero no le dio tiempo de terminar correctamente la actividad, hay muchas cosas que faltan, y todo por irse a empaquetar papas de forma incorrecta

## Código

El código de mi compañero esta incompleto

## Pruebas



## Fortalezas

La verdad se entiende el porque esta incompleto esto, pero de cualquier manera se ve que tiene una buena base, y que si sabe realmente que esta ocurrriendo, por lo que no hay grandes problemas realmente.

## Mejoras

Como esto no esta terminado, no me atreveria a opinar todavia

## Salida completa de pytest

Ejecutando:
C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe -m pytest -v C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_13\tests

============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_13
configfile: pytest.ini
collecting ... collected 12 items

clase_13\tests\test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED [  8%]
clase_13\tests\test_publico_avl.py::test_arbol_vacio PASSED              [ 16%]
clase_13\tests\test_publico_avl.py::test_insercion_y_busqueda_basica PASSED [ 25%]
clase_13\tests\test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha PASSED [ 33%]
clase_13\tests\test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda PASSED [ 41%]
clase_13\tests\test_publico_avl.py::test_caso_lr_aplica_rotacion_doble PASSED [ 50%]
clase_13\tests\test_publico_avl.py::test_caso_rl_aplica_rotacion_doble PASSED [ 58%]
clase_13\tests\test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED [ 66%]
clase_13\tests\test_publico_avl.py::test_duplicados_no_se_insertan PASSED [ 75%]
clase_13\tests\test_publico_avl.py::testmax1 PASSED                      [ 83%]
clase_13\tests\test_publico_avl.py::testmax2 FAILED                      [ 91%]
clase_13\tests\test_publico_avl.py::testmax3 FAILED                      [100%]

================================== FAILURES ===================================
__________________________________ testmax2 ___________________________________

    def testmax2():
        arbol = construir([1, 2, 5, 6, 7])
>       assert arbol.inorden() == [1, 2, 5, 6, 7, 3, 4, 8, 9]
E       assert [1, 2, 5, 6, 7] == [1, 2, 5, 6, 7, 3, 4, 8, 9]
E         
E         Right contains 4 more items, first extra item: 3
E         
E         Full diff:
E           [
E               1,
E               2,
E               5,
E               6,
E               7,
E         -     3,
E         -     4,
E         -     8,
E         -     9,
E           ]

clase_13\tests\test_publico_avl.py:127: AssertionError
__________________________________ testmax3 ___________________________________

    def testmax3():
        arbol = construir([1, 2, 5, 6, 7])
>       assert arbol.inorden() == [1, 2, 5]
E       assert [1, 2, 5, 6, 7] == [1, 2, 5]
E         
E         Left contains 2 more items, first extra item: 6
E         
E         Full diff:
E           [
E               1,
E               2,
E               5,
E         +     6,
E         +     7,
E           ]

clase_13\tests\test_publico_avl.py:132: AssertionError
=========================== short test summary info ===========================
FAILED clase_13\tests\test_publico_avl.py::testmax2 - assert [1, 2, 5, 6, 7] == [1, 2, 5, 6, 7, 3, 4, 8, 9]
  
  Right contains 4 more items, first extra item: 3
  
  Full diff:
    [
        1,
        2,
        5,
        6,
        7,
  -     3,
  -     4,
  -     8,
  -     9,
    ]
FAILED clase_13\tests\test_publico_avl.py::testmax3 - assert [1, 2, 5, 6, 7] == [1, 2, 5]
  
  Left contains 2 more items, first extra item: 6
  
  Full diff:
    [
        1,
        2,
        5,
  +     6,
  +     7,
    ]
======================== 2 failed, 10 passed in 0.05s =========================


Una vez más, es entendible que el código de mi compañero haya fallado bastantes pruebas (incluyendo las mias) por no haber terminado la implementación de su código.


## Conclusión

Falta por finalizar por completo la actividad, por lo que no hay que alarmarse demasiado.

## Checklist del revisor

- [ x ] Descargué la rama.
- [ x ] Ejecuté pruebas públicas.
- [ x ] Ejecuté mis pruebas.
- [ x ] Agregué `revision_nombre.md`.
- [ x ] Pegué salida completa de pytest.
- [ x ] Hice comentarios útiles.