# Reporte de pruebas — Clase 20

Nombre: Max

## Entorno y comandos

python evaluar.py entregas/clase_20/max clase_20/tests entregas/clase_20/max/test_estudiante.py 

## Salida completa de pruebas públicas

```text
Ejecutando:
C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe -m pytest -v C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_20\tests C:\Users\0286761\Documents\GitHub\EstructurasDatos\entregas\clase_20\max\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_20
configfile: pytest.ini
collecting ... collected 38 items

clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil0-BFS-cola-capas-O(V+E)] PASSED [  2%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil1-0-1 BFS-deque-0/1-O(V+E)] PASSED [  5%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil2-Dijkstra-heap-distancia-log V] PASSED [  7%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil3-Kruskal-Union-Find-componentes-E log E] PASSED [ 10%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil4-Kahn-cola + grados de entrada-grado de entrada cero-O(V+E)] PASSED [ 13%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_bfs_admite_grafo_dirigido_y_no_dirigido PASSED [ 15%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_kruskal_admite_pesos_negativos PASSED [ 18%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil0] PASSED [ 21%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil1] PASSED [ 23%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil2] PASSED [ 26%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil3] PASSED [ 28%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil4] PASSED [ 31%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil0] PASSED [ 34%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil1] PASSED [ 36%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[None] PASSED [ 39%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil1] PASSED [ 42%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil2] PASSED [ 44%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil3] PASSED [ 47%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil4] PASSED [ 50%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_es_aplicable_compara_con_el_contrato_completo PASSED [ 52%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_explicar_descarte_nombra_limite_y_recomendacion PASSED [ 55%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_explicar_algoritmo_correcto_confirma_operacion PASSED [ 57%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_correcta PASSED [ 60%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_detecta_algoritmo_y_estructura PASSED [ 63%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_fuera_de_alcance_no_la_acepta PASSED [ 65%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[Bellman-Ford] PASSED [ 68%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[A*] PASSED [ 71%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[] PASSED [ 73%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[3] PASSED [ 76%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_perfil_y_decision_son_inmutables PASSED [ 78%]
clase_20::test_max1 PASSED                                               [ 81%]
clase_20::test_max2 PASSED                                               [ 84%]
clase_20::test_max3 PASSED                                               [ 86%]
clase_20::test_max4 PASSED                                               [ 89%]
clase_20::test_max5 PASSED                                               [ 92%]
clase_20::test_max6 PASSED                                               [ 94%]
clase_20::test_max7 PASSED                                               [ 97%]
clase_20::test_max8 PASSED                                               [100%]

============================= 38 passed in 0.05s ==============================
```

## Pruebas propias

| Prueba | Regla protegida | Alternativa que distingue | Resultado |
| --- | --- | --- | --- |
| test_max1 | camino minimo | No hay | Correcto |
| test_max2 | Dijkstra | No hay | Correcto |
| test_max3 | Kruskal | No hay | Correcto |
| test_max4 | orden esperado | No hay | Correcto |
| test_max5 | encontrar ciclo | No hay | Correcto |
| test_max6 | Union-Find | No hay | Correcto |
| test_max7 | Negativos | No hay | Correcto |
| test_max8 | Optimizar | No hay | Correcto |

## Falla encontrada y corrección

Hubo muchisimas fallas en mi implementación a la hora de correr los códigos, pero las principales fueron que no saltaba algún raise error o cosas por el estilo.

## Estado final

Todo se completo de manera correcta