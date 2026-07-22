# Reporte_pytest
## Comando ejecutado
```bash
python -m pytest -v
```
## Salida completa
```bash
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_11
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.14.1
collected 12 items                                                                                                                                                                                                        

tests/test_publico_arboles.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                                                                    [  8%]
tests/test_publico_arboles.py::test_crear_arbol_vacio PASSED                                                                                                                                                        [ 16%]
tests/test_publico_arboles.py::test_arbol_vacio_no_contiene_valores PASSED                                                                                                                                          [ 25%]
tests/test_publico_arboles.py::test_insertar_un_valor PASSED                                                                                                                                                        [ 33%]
tests/test_publico_arboles.py::test_buscar_valor_existente_e_inexistente PASSED                                                                                                                                     [ 41%]
tests/test_publico_arboles.py::test_insertar_varios_valores_inorden_ordenado PASSED                                                                                                                                 [ 50%]
tests/test_publico_arboles.py::test_altura_de_arbol_con_varios_niveles PASSED                                                                                                                                       [ 58%]
tests/test_publico_arboles.py::test_no_insertar_duplicados PASSED                                                                                                                                                   [ 66%]
tests/test_publico_arboles.py::test_todo_preorden PASSED                                                                                                                                                            [ 75%]
tests/test_publico_arboles.py::test_todo_postorden PASSED                                                                                                                                                           [ 83%]
tests/test_publico_arboles.py::test_todo_insercion_en_orden_creciente PASSED                                                                                                                                        [ 91%]
tests/test_publico_arboles.py::test_todo_repetido_no_aparece_dos_veces PASSED                                                                                                                                       [100%]

=================================================================================================== 12 passed in 0.05s ===================================================================================================
```
## Interpretación
Todo salió bien 

## Cuántas pruebas se ejecutaron:
12
## Cuántas pasaron:
12 de 12
## ¿Hubo errores?
No, ninguna prueba falló ni lanzó una excepción inesperada.
### Qué comportamiento verifican:
  - `test_arbol_vacio_al_crear`: estado inicial correcto (`esta_vacio`, `altura`, `inorden` sobre un árbol nuevo).
  - `test_preorden_de_arbol_con_varios_niveles` y `test_postorden_de_arbol_con_varios_niveles`: orden exacto de visita de nodos en un árbol con varios niveles, no solo en un árbol trivial.
  - `test_altura_de_arbol_degenerado`: que la altura crece correctamente en el peor caso (árbol convertido en una sola rama).
  - `test_busqueda_de_valor_inexistente`: que `contiene` no da falsos positivos con valores cercanos a los existentes.
  - `test_no_permite_valores_duplicados`: que insertar un valor repetido no altera la estructura del árbol.
  - `test_arbol_con_valores_negativos`: que el invariante de orden funciona igual con valores negativos y positivos mezclados.

## Prueba que diseñé yo
las de test_estudiante, post orden, deuplicados, repetidos, preorden, orden creciente.

## Qué caso todavía falta probar
insercion decreciente
