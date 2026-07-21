# Reporte de pytest — Clase 17

## Comando ejecutado

```text
py evaluar.py entregas/clase_17/Aristeo clase_17/tests entregas/clase_17/Aristeo/test_estudiante.py
```

## Salida completa de `pytest -v`

```text
================================================================== test session starts ==================================================================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\SCHOOL\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\SCHOOL\Documents\EstructurasDatos\clase_17
configfile: pytest.ini
plugins: anyio-4.12.1
collected 40 items                                                                                                                                       

clase_17\tests\test_publico_estructuras_bfs.py::test_exporta_los_dos_tipos_de_nodo PASSED                                                          [  2%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_comienza_vacia_y_admite_valores_repetidos PASSED                                         [  5%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_respeta_fifo_y_tamano PASSED                                                             [  7%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_vacia_falla_y_puede_reutilizarse PASSED                                                  [ 10%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_restaurada_no_conserva_extremos PASSED                                                   [ 12%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_opera_por_ambos_extremos PASSED                                                         [ 15%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_comienza_vacia_y_admite_valores_repetidos PASSED                                        [ 17%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_vacia_falla_y_puede_reutilizarse PASSED                                                 [ 20%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_desconecta_nodos_retirados PASSED                                                       [ 22%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_conserva_orden_de_vecinos_y_camino_minimo PASSED                                          [ 25%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_identidad_camino_directo_y_direccion PASSED                                               [ 27%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none PASSED                                    [ 30%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_incluye_vecino_implicito_y_no_muta_entrada PASSED                                         [ 32%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_rechaza_origen_o_destino_ausentes PASSED                                                  [ 35%]
clase_17\tests\test_publico_estructuras_bfs.py::test_reconstruir_cubre_identidad_inalcanzable_y_ciclo PASSED                                       [ 37%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_bfs_calcula_distancias_y_predecesores PASSED                                         [ 40%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_prefiere_mas_aristas_si_cuestan_menos PASSED                                         [ 42%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_con_solo_pesos_cero PASSED                                                           [ 45%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_con_solo_pesos_uno PASSED                                                            [ 47%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_actualiza_una_mejora_posterior PASSED                                                [ 50%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_identidad_e_inalcanzable PASSED                                                      [ 52%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_incluye_vecino_implicito_y_no_muta_entrada PASSED                                    [ 55%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[True] PASSED                                         [ 57%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[False] PASSED                                        [ 60%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[0.0] PASSED                                          [ 62%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[1] PASSED                                            [ 65%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[None] PASSED                                         [ 67%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_entero_fuera_del_dominio[-1] PASSED                                          [ 70%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_entero_fuera_del_dominio[2] PASSED                                           [ 72%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_entero_fuera_del_dominio[8] PASSED                                           [ 75%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_forma_y_nodos_invalidos PASSED                                               [ 77%]
clase_17\tests\test_publico_estructuras_bfs.py::test_constante_infinito_es_compatible_con_contrato PASSED                                          [ 80%]
clase_17::test_1_fifo_cola_ligada PASSED                                                                                                           [ 82%]
clase_17::test_2_reutilizacion_cola_vaciada PASSED                                                                                                 [ 85%]
clase_17::test_3_operaciones_combinadas_deque PASSED                                                                                               [ 87%]
clase_17::test_4_reutilizacion_deque_vaciada PASSED                                                                                                [ 90%]
clase_17::test_5_bfs_con_ciclo PASSED                                                                                                              [ 92%]
clase_17::test_6_bfs_destino_inalcanzable PASSED                                                                                                   [ 95%]
clase_17::test_7_cero_uno_bfs_ruta_mas_larga_menor_costo PASSED                                                                                    [ 97%]
clase_17::test_8_cero_uno_bfs_peso_invalido PASSED                                                                                                 [100%]

================================================================== 40 passed in 0.74s ===================================================================
```

## Resumen cuantitativo

- Cantidad total de pruebas: 40
- Pruebas aprobadas: 40
- Errores o fallos: 0 

## Evidencia técnica

- Prueba propia más importante: test_7_cero_uno_bfs_ruta_mas_larga_menor_costo
- Invariante que protegió: Garantiza que 0-1 BFS elija caminos por peso acumulado mínimo real, y no se comporte como un BFS regular que prefiere la menor cantidad de aristas (saltos).
- Fallo de referencias encontrado:nicialmente, al desencolar o quitar elementos de la deque, los nodos removidos mantenían referencias a sus vecinos (siguiente/anterior), lo que impedía que el recolector de basura los liberara. Se corrigió limpiándolos a None.
- Caso de BFS que resultó más informativo: BFS con destino inalcanzable, donde se verificó que no ocurre un KeyError y devuelve correctamente [].
- Caso de 0-1 BFS que resultó más informativo: El filtrado de tipos defensivo para rechazar booleanos (True/False), previniendo que Python los trate como 1 y 0 respectivamente.


