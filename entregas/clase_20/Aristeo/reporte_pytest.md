# Reporte de pruebas — Clase 20

Nombre: Aristeo

## Entorno y comandos
```text
python3 evaluar.py entregas/clase_20/Aristeo clase_20/tests entregas/clase_20/Aristeo/test_estudiante.py
```
## Salida completa de pruebas públicas


``` py
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_20
configfile: pytest.ini
plugins: anyio-4.14.1
collected 38 items                                                                                                                                                                                                        

clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil0-BFS-cola-capas-O(V+E)] PASSED                                                                                          [  2%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil1-0-1 BFS-deque-0/1-O(V+E)] PASSED                                                                                       [  5%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil2-Dijkstra-heap-distancia-log V] PASSED                                                                                  [  7%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil3-Kruskal-Union-Find-componentes-E log E] PASSED                                                                         [ 10%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil4-Kahn-cola + grados de entrada-grado de entrada cero-O(V+E)] PASSED                                                     [ 13%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_bfs_admite_grafo_dirigido_y_no_dirigido PASSED                                                                                                           [ 15%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_kruskal_admite_pesos_negativos PASSED                                                                                                                    [ 18%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil0] PASSED                                                                                        [ 21%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil1] PASSED                                                                                        [ 23%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil2] PASSED                                                                                        [ 26%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil3] PASSED                                                                                        [ 28%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil4] PASSED                                                                                        [ 31%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil0] PASSED                                                                                                          [ 34%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil1] PASSED                                                                                                          [ 36%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[None] PASSED                                                                                                                     [ 39%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil1] PASSED                                                                                                                  [ 42%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil2] PASSED                                                                                                                  [ 44%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil3] PASSED                                                                                                                  [ 47%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil4] PASSED                                                                                                                  [ 50%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_es_aplicable_compara_con_el_contrato_completo PASSED                                                                                                     [ 52%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_explicar_descarte_nombra_limite_y_recomendacion PASSED                                                                                                   [ 55%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_explicar_algoritmo_correcto_confirma_operacion PASSED                                                                                                    [ 57%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_correcta PASSED                                                                                                                        [ 60%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_detecta_algoritmo_y_estructura PASSED                                                                                                  [ 63%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_fuera_de_alcance_no_la_acepta PASSED                                                                                                   [ 65%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[Bellman-Ford] PASSED                                                                                      [ 68%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[A*] PASSED                                                                                                [ 71%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[] PASSED                                                                                                  [ 73%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[3] PASSED                                                                                                 [ 76%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_perfil_y_decision_son_inmutables PASSED                                                                                                                  [ 78%]
clase_20::test_distincion_bfs_vs_dijkstra_pesos PASSED                                                                                                                                                              [ 81%]
clase_20::test_distincion_01_bfs_vs_bfs PASSED                                                                                                                                                                      [ 84%]
clase_20::test_distincion_dijkstra_vs_kruskal PASSED                                                                                                                                                                [ 86%]
clase_20::test_distincion_bfs_vs_kahn PASSED                                                                                                                                                                        [ 89%]
clase_20::test_pesos_negativos_fuera_del_alcance PASSED                                                                                                                                                             [ 92%]
clase_20::test_kruskal_con_peso_negativo PASSED                                                                                                                                                                     [ 94%]
clase_20::test_error_solo_de_estructura PASSED                                                                                                                                                                      [ 97%]
clase_20::test_perfil_invalido PASSED                                                                                                                                                                               [100%]

=================================================================================================== 38 passed in 0.08s ===================================================================================================
```

## Pruebas propias

| Prueba | Regla protegida | Alternativa que distingue | Resultado |
| --- | --- | --- | --- |
| `test_distincion_bfs_vs_dijkstra_pesos` | El camino mínimo con pesos no negativos generales exige Dijkstra. | Distingue de BFS regular (que asume costo uniforme). | **PASSED** |
| `test_distincion_01_bfs_vs_bfs` | Dominios con pesos acotados a {0, 1} usan 0-1 BFS con Deque. | Evita el costo de Dijkstra o el error de BFS regular. | **PASSED** |
| `test_distincion_dijkstra_vs_kruskal` | Conexión global mínima requiere Kruskal (MST). | Distingue de Dijkstra (caminos mínimos desde un origen). | **PASSED** |
| `test_distincion_bfs_vs_kahn` | El orden de dependencias requiere Kahn (cola + grados de entrada). | Evita la desorganización de dependencias de un BFS común. | **PASSED** |
| `test_pesos_negativos_fuera_del_alcance` | Los caminos mínimos con pesos negativos son rechazados preventivamente. | Evita ciclos de costo infinitamente negativo. | **PASSED** |
| `test_kruskal_con_peso_negativo` | Kruskal en MST sí admite y procesa correctamente pesos negativos. | Protege que no se catalogue como "fuera de alcance" erróneamente. | **PASSED** |
| `test_error_solo_de_estructura` | Valida el acoplamiento óptimo Algoritmo - Estructura Dominante. | Rechaza combinaciones correctas de algoritmo pero con estructura ineficiente. | **PASSED** |
| `test_perfil_invalido` | Lanza `ValueError` al recibir strings de entrada corruptos o fuera de catálogo. | Previene la contaminación o procesamiento de datos corruptos. | **PASSED** |

## Falla encontrada y corrección
Al principio seleccionar_estrategia me returneaba implícitamente None, para corregirlo se usan elifs y se garantizamos que los caminos nos den una instancia completa de DecisionAlgoritmica.
## Estado final
Todo jaló aunque se tuvo que corregir la implementación, uts.
