```text
============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.1.2, pluggy-1.0.0
collected 6 items

test_publico_nearest_smaller.py::test_ejemplo_oficial_nearest_smaller PASSED [ 16%]
test_publico_nearest_smaller.py::test_arreglo_creciente PASSED            [ 33%]
test_publico_nearest_smaller.py::test_arreglo_decreciente PASSED          [ 50%]
test_publico_nearest_smaller.py::test_todo_valores_iguales PASSED         [ 66%]
test_publico_nearest_smaller.py::test_todo_error_comparacion_estricta PASSED [ 83%]
test_publico_nearest_smaller.py::test_todo_caso_limite PASSED             [100%]

============================== 6 passed in 0.03s ===============================

Comando ejecutado:
`python3 -m pytest -v test_publico_nearest_smaller.py`

Pruebas ejecutadas: 6

Pruebas que pasaron: 6

Errores/Fallos: 0

Comportamientos verificados: Arreglos monótonos (crecientes y decrecientes), el ejemplo oficial de CSES, manejo de valores repetidos y vectores de tamaño uno.

Prueba diseñada por mí: Verificación de arreglos constantes [3, 3, 3] y el caso donde usar > falla [2, 2].

Caso que todavía falta probar: Arreglos masivos (ej. 105 elementos) para certificar empíricamente que la complejidad no degenera a O(n2) lanzando un Timeout.