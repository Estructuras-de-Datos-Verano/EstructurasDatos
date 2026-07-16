# Reporte de pytest — Clase 18

## Comando ejecutado

```text
py evaluar.py entregas/clase_18/Aristeo clase_18/tests entregas/clase_18/Aristeo/test_estudiante.py
```

## Salida completa de `pytest -v`

```text
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_18
configfile: pytest.ini
plugins: anyio-4.14.1
collected 62 items                                                                                                                                                                                                        

clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_cero_elementos PASSED                                                                                                                            [  1%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_un_elemento PASSED                                                                                                                               [  3%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_inicialmente_separado PASSED                                                                                                                     [  4%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_efectiva_repetida_y_reflexiva PASSED                                                                                                                  [  6%]
clase_18\tests\test_publico_union_find_kruskal.py::test_transitividad_conectividad_y_tamano PASSED                                                                                                                  [  8%]
clase_18\tests\test_publico_union_find_kruskal.py::test_compresion_no_cambia_particion_ni_contador PASSED                                                                                                           [  9%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[True] PASSED                                                                                                   [ 11%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[False] PASSED                                                                                                  [ 12%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3.0] PASSED                                                                                                    [ 14%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3] PASSED                                                                                                      [ 16%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[None] PASSED                                                                                                   [ 17%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_negativa PASSED                                                                                                                 [ 19%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[-1] PASSED                                                                                                         [ 20%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[3] PASSED                                                                                                          [ 22%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[True] PASSED                                                                                                     [ 24%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1.0] PASSED                                                                                                      [ 25%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1] PASSED                                                                                                        [ 27%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[None] PASSED                                                                                                     [ 29%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_grafo_conductor_costo_y_v_menos_uno PASSED                                                                                                          [ 30%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_cero_y_un_vertice PASSED                                                                                                                            [ 32%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_dos_vertices_y_una_arista PASSED                                                                                                                    [ 33%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_triangulo_rechaza_ciclo PASSED                                                                                                                      [ 35%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_desconectado_devuelve_none PASSED                                                                                                                   [ 37%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_admite_pesos_negativos_y_cero PASSED                                                                                                                [ 38%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_empates_verifica_propiedades_no_lista_exacta PASSED                                                                                                 [ 40%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_aristas_paralelas_y_autoaristas PASSED                                                                                                              [ 41%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_no_modifica_aristas PASSED                                                                                                                          [ 43%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[True] PASSED                                                                                                       [ 45%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3.0] PASSED                                                                                                        [ 46%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3] PASSED                                                                                                          [ 48%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[None] PASSED                                                                                                       [ 50%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_negativo PASSED                                                                                                             [ 51%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista0] PASSED                                                                                                          [ 53%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista1] PASSED                                                                                                          [ 54%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[True] PASSED                                                                                                       [ 56%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0.0] PASSED                                                                                                        [ 58%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0] PASSED                                                                                                          [ 59%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[None] PASSED                                                                                                       [ 61%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[-1] PASSED                                                                                                           [ 62%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[2] PASSED                                                                                                            [ 64%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[True] PASSED                                                                                                               [ 66%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[3] PASSED                                                                                                                  [ 67%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[None] PASSED                                                                                                               [ 69%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[peso3] PASSED                                                                                                              [ 70%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[inf] PASSED                                                                                                                  [ 72%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[-inf] PASSED                                                                                                                 [ 74%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[nan] PASSED                                                                                                                  [ 75%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_red_conectada_y_resultado_entero PASSED                                                                                                    [ 77%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_desconectada_y_una_ciudad PASSED                                                                                                           [ 79%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_no_muta_y_rechaza_costo_float PASSED                                                                                                       [ 80%]
clase_18::test_estudiante_1_union_efectiva PASSED                                                                                                                                                                   [ 82%]
clase_18::test_estudiante_2_union_repetida PASSED                                                                                                                                                                   [ 83%]
clase_18::test_estudiante_3_transitividad PASSED                                                                                                                                                                    [ 85%]
clase_18::test_estudiante_4_tamano_componente PASSED                                                                                                                                                                [ 87%]
clase_18::test_estudiante_5_arista_rechazada_por_ciclo PASSED                                                                                                                                                       [ 88%]
clase_18::test_estudiante_6_grafo_desconectado PASSED                                                                                                                                                               [ 90%]
clase_18::test_estudiante_indice_negativo_lanza_error PASSED                                                                                                                                                        [ 91%]
clase_18::test_estudiante_bool_como_indice_lanza_error PASSED                                                                                                                                                       [ 93%]
clase_18::test_estudiante_compresion_de_caminos PASSED                                                                                                                                                              [ 95%]
clase_18::test_estudiante_kruskal_pesos_negativos PASSED                                                                                                                                                            [ 96%]
clase_18::test_estudiante_kruskal_no_mutacion PASSED                                                                                                                                                                [ 98%]
clase_18::test_estudiante_road_reparation_impossible PASSED                                                                                                                                                         [100%]

=================================================================================================== 62 passed in 0.10s ===================================================================================================
```

## Resumen

- Cantidad de pruebas: 62
- Pruebas aprobadas: 62
- Errores o fallos: 0

## Evidencia técnica

- Prueba propia más importante: test_estudiante_4_tamano_componente o test_estudiante_bool_como_indice_lanza_error.

- Invariante protegido: Que los booleanos no son índices ni tamaños válidos.

- Ejemplo de unión redundante: En un `UnionFind` de 3 elementos, tras realizar la unión efectiva de los elementos 0 y 1 mediante uf.union(0, 1).

- Ejemplo de arista rechazada: Un grafo tipo triángulo con 3 vértices y las aristas [(0, 1, 1), (1, 2, 2), (0, 2, 5)]

- Resultado de un grafo desconectado: Al ejecutar kruskal(4, aristas) sobre un grafo de 4 vértices que solo posee las aristas [(0, 1, 1), (2, 3, 2)]

## Corrección después de un fallo
Describe el comportamiento inicial, el contrato roto, la corrección localizada y el resultado posterior.

