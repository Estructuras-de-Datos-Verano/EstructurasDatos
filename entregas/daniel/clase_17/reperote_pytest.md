
- comando ejecutado 
- python -m pytest -v 

- salida completa

- .........FFF..........................                                                                                                                                                                   [100%]
================================================================================================== FAILURES ===================================================================================================
_____________________________________________________________________________ test_bfs_conserva_orden_de_vecinos_y_camino_minimo ______________________________________________________________________________

    def test_bfs_conserva_orden_de_vecinos_y_camino_minimo():
        predecesores = bfs_predecesores(grafo_bfs(), "A")
>       assert predecesores == {
            "A": None, "B": "A", "C": "A", "D": "B", "E": "B", "F": "D"
        }
E       AssertionError: assert {'A': None, '...D': None, ...} == {'A': None, '...'D': 'B', ...}
E         
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'E': None} != {'E': 'B'}
E         {'B': None} != {'B': 'A'}
E         {'D': None...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

tests\test_publico_estructuras_bfs.py:125: AssertionError
________________________________________________________________________________ test_bfs_identidad_camino_directo_y_direccion ________________________________________________________________________________

    def test_bfs_identidad_camino_directo_y_direccion():
        grafo = {"A": ["B"], "B": []}
        assert bfs_camino(grafo, "A", "A") == ["A"]
>       assert bfs_camino(grafo, "A", "B") == ["A", "B"]
E       AssertionError: assert [] == ['A', 'B']
E         
E         Right contains 2 more items, first extra item: 'A'
E         Use -v to get more diff

tests\test_publico_estructuras_bfs.py:134: AssertionError
__________________________________________________________________________ test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none ___________________________________________________________________________

    def test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none():
        grafo = {"A": ["B"], "B": ["C"], "C": ["A"], "X": []}
        pred = bfs_predecesores(grafo, "A")
>       assert pred == {"A": None, "B": "A", "C": "B", "X": None}
E       AssertionError: assert {'A': None, '...ne, 'X': None} == {'A': None, '...B', 'X': None}
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'B': None} != {'B': 'A'}
E         {'C': None} != {'C': 'B'}
E         Use -v to get more diff

tests\test_publico_estructuras_bfs.py:141: AssertionError
=========================================================================================== short test summary info ===========================================================================================
FAILED tests/test_publico_estructuras_bfs.py::test_bfs_conserva_orden_de_vecinos_y_camino_minimo - AssertionError: assert {'A': None, '...D': None, ...} == {'A': None, '...'D': 'B', ...}
FAILED tests/test_publico_estructuras_bfs.py::test_bfs_identidad_camino_directo_y_direccion - AssertionError: assert [] == ['A', 'B']
FAILED tests/test_publico_estructuras_bfs.py::test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none - AssertionError: assert {'A': None, '...ne, 'X': None} == {'A': None, '...B', 'X': None}
3 failed, 35 passed in 0.15s

importancia
- corrieron la mayor  parte de las pruebas
- cuantas totales
- 38
cuantas pasaron 
- 35
- cuales implementaste
- las ultimas 6
- que comportamineto verifican 
- los que menciona en sus titulos
- cual falta
- el que mide la lonjitud del deque