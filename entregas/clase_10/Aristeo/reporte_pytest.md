## Comando ejecutado
``
python -m pytest -v
``
# Salidas completa

``
============================================================================== test session starts ==============================================================================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\SCHOOL\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\SCHOOL\Documents\EstructurasDatos\clase_10
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.12.1
collected 12 items                                                                                                                                                               

tests/test_publico_recorridos.py::test_existen_funciones_requeridas PASSED                                                                                                 [  8%]
tests/test_publico_recorridos.py::test_bfs_en_grafo_simple PASSED                                                                                                          [ 16%]
tests/test_publico_recorridos.py::test_dfs_en_grafo_simple PASSED                                                                                                          [ 25%]
tests/test_publico_recorridos.py::test_bfs_en_grafo_con_ciclo PASSED                                                                                                       [ 33%]
tests/test_publico_recorridos.py::test_dfs_en_grafo_con_ciclo PASSED                                                                                                       [ 41%]
tests/test_publico_recorridos.py::test_grafo_desconectado_solo_visita_componente_del_origen PASSED                                                                         [ 50%]
tests/test_publico_recorridos.py::test_registro_bfs_contiene_cola PASSED                                                                                                   [ 58%]
tests/test_publico_recorridos.py::test_registro_dfs_contiene_pila PASSED                                                                                                   [ 66%]
tests/test_publico_recorridos.py::test_bfs_encuentra_camino_en_red_no_ponderada PASSED                                                                                     [ 75%]
tests/test_publico_recorridos.py::test_todo_bfs_y_dfs_ordenes_distintos PASSED                                                                                             [ 83%]
tests/test_publico_recorridos.py::test_todo_nodo_aislado PASSED                                                                                                            [ 91%]
tests/test_publico_recorridos.py::test_todo_no_visita_repetidos PASSED                                                                                                     [100%]

============================================================================== 12 passed in 2.17s ===============================================================================
``

---

El codigo funcionó correctamente
# Cuántas pruebas se ejecutaron:
12
# Cuántas pasaron:
12
# Si hubo errores:
No
# Qué comportamiento verifican:
- Existan las funciones requeridas (bfs, dfs, registrar_bfs, registrar_dfs y guardar_visualizacion_recorrido).
- El recorrido BFS visite los nodos en el orden correcto.
- El recorrido DFS visite los nodos en el orden correcto.
- Ambos algoritmos funcionen correctamente en grafos con ciclos.
- Solo se recorra la componente conexa del nodo de origen en grafos desconectados.
- Los registros de BFS y DFS incluyan la información esperada (cola o pila y línea de pseudocódigo).
- BFS encuentre correctamente el recorrido en una red no ponderada.
- BFS y DFS produzcan órdenes de recorrido diferentes cuando corresponde.
- No se visiten nodos repetidos.
- Los algoritmos funcionen correctamente con un nodo aislado.

# Qué prueba diseñaste tú
- Verificar que BFS y DFS produzcan órdenes de recorrido diferentes.
- Probar un grafo con un nodo aislado.
- Comprobar que en un grafo con ciclos no se visiten nodos repetidos.
# Qué caso todavía falta probar.
Cuando el nodo de origen no existe en el grafo