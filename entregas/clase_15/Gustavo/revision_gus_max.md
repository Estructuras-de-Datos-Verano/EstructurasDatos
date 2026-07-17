# Resumen

La entrega de la clase de hoy de mi compañero se realizo correctamente, todos los requisitos se cumplieron de manera correcta y satisfactoria.

## Cambios

No realice cambios, la implementación y el notebook son correctos

## Pruebas

Comando ejecutado:

```bash
py evaluar.py entregas/clase_15/Gustavo clase_15/tests entregas/clase_15/Gustavo/test_estudiante.py
```

Pruebas propias(Max):

```text
def test_max1():
    grafo = {"A": [("B", 0), ("C", 5)], "B": [("C", 0)], "C": []}
    assert camino_minimo(grafo, "A", "C") is not (1, ["A", "B", "C"])


def test_max2():
    grafo = {"A": [("B", 2), ("C", 5)], "B": [("C", 0)], "C": [], "D": []}
    assert camino_minimo(grafo, "A", "D") == (float('inf'),[])


def test_max3():
    grafo = {"A": [("B", 2), ("C", 5)], "B": [("C", 0), ("D", 1)], "C": [("E",1), ("D",5)], "D": [("E",10)], "E": []}
    assert camino_minimo(grafo, "A", "E") == (3, ["A", "B", "C", "E"])
```

Resultado:

========================================================================================== test session starts ==========================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
collected 17 items                                                                                                                                                                                       

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED                                                                                                  [  5%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED                                                                                                            [ 11%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED                                                                                                       [ 17%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED                                                                                                              [ 23%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED                                                                                                           [ 29%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED                                                                                                                  [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED                                                                                                                        [ 41%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED                                                                                                                      [ 47%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED                                                                                                                 [ 52%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED                                                                                                                   [ 58%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED                                                                                                                     [ 64%]
clase_15::test_distancia_mejora_dos_veces_y_deja_obsoletas <- ..\entregas\clase_15\Gustavo\test_estudiante.py PASSED                                                                               [ 70%]
clase_15::test_destino_inalcanzable_devuelve_infinito_y_vacio <- ..\entregas\clase_15\Gustavo\test_estudiante.py PASSED                                                                            [ 76%]
clase_15::test_ruta_indirecta_supera_directa_costosa <- ..\entregas\clase_15\Gustavo\test_estudiante.py PASSED                                                                                     [ 82%]
clase_15::test_max1 <- ..\entregas\clase_15\Gustavo\test_estudiante.py PASSED                                                                                                                      [ 88%]
clase_15::test_max2 <- ..\entregas\clase_15\Gustavo\test_estudiante.py PASSED                                                                                                                      [ 94%]
clase_15::test_max3 <- ..\entregas\clase_15\Gustavo\test_estudiante.py PASSED                                                                                                                      [100%]

========================================================================================== 17 passed in 0.04s ===========================================================================================

## Dificultades

No tuvo, aun que creo que falta limpieza a la hora de implementar las cosas.


## Checklist

- [x] Mi código compila.
- [x] Pasé pruebas públicas.
- [x] Ejecuté `test_estudiante.py`.
- [x] No hay `__pycache__`.
- [x] No hay `.pyc`.
- [x] No hay archivos fuera de mi entrega.
- [x] La rama tiene el nombre correcto.