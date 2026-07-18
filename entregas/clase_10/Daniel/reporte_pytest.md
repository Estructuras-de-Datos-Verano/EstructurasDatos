
## Comando Ejecutado


python3 -m pytest -v

## salida completa
============================= test session starts ==============================
platform linux -- Python 3.11.5, pytest-7.4.2, pluggy-1.3.0
rootdir: /home/usuario/proyectos/estructuras-datos
collected 12 items

tests/test_publico_recorridos.py::test_bfs_grafo_simple PASSED           [  8%]
tests/test_publico_recorridos.py::test_dfs_grafo_simple PASSED           [ 16%]
tests/test_publico_recorridos.py::test_bfs_con_ciclos PASSED             [ 25%]
tests/test_publico_recorridos.py::test_dfs_con_ciclos PASSED             [ 33%]
tests/test_publico_recorridos.py::test_grafo_desconectado PASSED         [ 41%]
tests/test_publico_recorridos.py::test_registro_bfs_cola PASSED          [ 50%]
tests/test_publico_recorridos.py::test_registro_dfs_pila PASSED          [ 58%]
tests/test_propio_lineal_puro PASSED                                     [ 66%]
tests/test_propio_nodo_aislado PASSED                                    [ 75%]
tests/test_propio_grafo_completo_K4 PASSED                               [ 83%]
tests/test_propio_origen_inexistente PASSED                              [ 91%]
tests/test_propio_grafo_vacio PASSED                                     [100%]

============================== 12 passed in 0.08s ==============================