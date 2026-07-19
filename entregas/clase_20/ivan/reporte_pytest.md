# Reporte de pruebas — Clase 20

# Nombre: José Iván Reyna Blanco

## Entorno y comandos
``` bash

python evaluar.py entregas/clase_20/ivan clase_20/tests entregas/clase_20/ivan/test_estudiante.py

```
## Salida completa de pruebas públicas

```powershell
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_20/ivan clase_20/tests entregas/clase_20/ivan/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_20\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_20\ivan\test_estudiante.py

==================================================================================== test session starts ====================================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_20
configfile: pytest.ini
plugins: anyio-4.7.0
collected 68 items                                                                                                                                                                           

clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil0-BFS-cola-capas-O(V+E)] PASSED                                                             [  1%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil1-0-1 BFS-deque-0/1-O(V+E)] PASSED                                                          [  2%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil2-Dijkstra-heap-distancia-log V] PASSED                                                     [  4%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil3-Kruskal-Union-Find-componentes-E log E] PASSED                                            [  5%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_selecciones_fundamentales[perfil4-Kahn-cola + grados de entrada-grado de entrada cero-O(V+E)] PASSED                        [  7%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_bfs_admite_grafo_dirigido_y_no_dirigido PASSED                                                                              [  8%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_kruskal_admite_pesos_negativos PASSED                                                                                       [ 10%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil0] PASSED                                                           [ 11%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil1] PASSED                                                           [ 13%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil2] PASSED                                                           [ 14%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil3] PASSED                                                           [ 16%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil4] PASSED                                                           [ 17%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil0] PASSED                                                                             [ 19%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_vocabulario_desconocido[perfil1] PASSED                                                                             [ 20%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[None] PASSED                                                                                        [ 22%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil1] PASSED                                                                                     [ 23%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil2] PASSED                                                                                     [ 25%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil3] PASSED                                                                                     [ 26%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_tipos_invalidos[perfil4] PASSED                                                                                     [ 27%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_es_aplicable_compara_con_el_contrato_completo PASSED                                                                        [ 29%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_explicar_descarte_nombra_limite_y_recomendacion PASSED                                                                      [ 30%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_explicar_algoritmo_correcto_confirma_operacion PASSED                                                                       [ 32%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_correcta PASSED                                                                                           [ 33%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_detecta_algoritmo_y_estructura PASSED                                                                     [ 35%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_evaluar_propuesta_fuera_de_alcance_no_la_acepta PASSED                                                                      [ 36%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[Bellman-Ford] PASSED                                                         [ 38%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[A*] PASSED                                                                   [ 39%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[] PASSED                                                                     [ 41%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[3] PASSED                                                                    [ 42%]
clase_20\tests\test_publico_seleccion_estrategias.py::test_perfil_y_decision_son_inmutables PASSED                                                                                     [ 44%]
clase_20::test_selecciones_fundamentales[perfil0-BFS-cola-capas-O(V+E)] PASSED                                                                                                         [ 45%]
clase_20::test_selecciones_fundamentales[perfil1-0-1 BFS-deque-0/1-O(V+E)] PASSED                                                                                                      [ 47%]
clase_20::test_selecciones_fundamentales[perfil2-Dijkstra-heap-distancia-log V] PASSED                                                                                                 [ 48%]
clase_20::test_selecciones_fundamentales[perfil3-Kruskal-Union-Find-componentes-E log E] PASSED                                                                                        [ 50%]
clase_20::test_selecciones_fundamentales[perfil4-Kahn-cola + grados de entrada-grado de entrada cero-O(V+E)] PASSED                                                                    [ 51%]
clase_20::test_bfs_admite_grafo_dirigido_y_no_dirigido PASSED                                                                                                                          [ 52%]
clase_20::test_kruskal_admite_pesos_negativos PASSED                                                                                                                                   [ 54%]
clase_20::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil0] PASSED                                                                                                       [ 55%]
clase_20::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil1] PASSED                                                                                                       [ 57%]
clase_20::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil2] PASSED                                                                                                       [ 58%]
clase_20::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil3] PASSED                                                                                                       [ 60%]
clase_20::test_reconoce_fuera_del_alcance_sin_inventar_algoritmo[perfil4] PASSED                                                                                                       [ 61%]
clase_20::test_rechaza_vocabulario_desconocido[perfil0] PASSED                                                                                                                         [ 63%]
clase_20::test_rechaza_vocabulario_desconocido[perfil1] PASSED                                                                                                                         [ 64%]
clase_20::test_rechaza_tipos_invalidos[None] PASSED                                                                                                                                    [ 66%]
clase_20::test_rechaza_tipos_invalidos[perfil1] PASSED                                                                                                                                 [ 67%]
clase_20::test_rechaza_tipos_invalidos[perfil2] PASSED                                                                                                                                 [ 69%]
clase_20::test_rechaza_tipos_invalidos[perfil3] PASSED                                                                                                                                 [ 70%]
clase_20::test_rechaza_tipos_invalidos[perfil4] PASSED                                                                                                                                 [ 72%]
clase_20::test_es_aplicable_compara_con_el_contrato_completo PASSED                                                                                                                    [ 73%]
clase_20::test_explicar_descarte_nombra_limite_y_recomendacion PASSED                                                                                                                  [ 75%]
clase_20::test_explicar_algoritmo_correcto_confirma_operacion PASSED                                                                                                                   [ 76%]
clase_20::test_evaluar_propuesta_correcta PASSED                                                                                                                                       [ 77%]
clase_20::test_evaluar_propuesta_detecta_algoritmo_y_estructura PASSED                                                                                                                 [ 79%]
clase_20::test_evaluar_propuesta_fuera_de_alcance_no_la_acepta PASSED                                                                                                                  [ 80%]
clase_20::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[Bellman-Ford] PASSED                                                                                                     [ 82%]
clase_20::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[A*] PASSED                                                                                                               [ 83%]
clase_20::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[] PASSED                                                                                                                 [ 85%]
clase_20::test_rechaza_algoritmo_no_estudiado_o_tipo_invalido[3] PASSED                                                                                                                [ 86%]
clase_20::test_perfil_y_decision_son_inmutables PASSED                                                                                                                                 [ 88%]
clase_20::test_evaluar_propuesta_rechaza_selecciones_incorrectas[perfil0-BFS-cola-Dijkstra-heap] PASSED                                                                                [ 89%]
clase_20::test_evaluar_propuesta_rechaza_selecciones_incorrectas[perfil1-BFS-cola-0-1 BFS-deque] PASSED                                                                                [ 91%]
clase_20::test_evaluar_propuesta_rechaza_selecciones_incorrectas[perfil2-Dijkstra-heap-Kruskal-Union-Find] PASSED                                                                      [ 92%]
clase_20::test_evaluar_propuesta_rechaza_selecciones_incorrectas[perfil3-BFS-cola-Kahn-grados de entrada] PASSED                                                                       [ 94%]
clase_20::test_pesos_negativos_fuera_del_alcance_rechazados PASSED                                                                                                                     [ 95%]
clase_20::test_kruskal_acepta_pesos_negativos_sin_romper_invariante PASSED                                                                                                             [ 97%]
clase_20::test_error_solo_de_estructura_es_detectado PASSED                                                                                                                            [ 98%]
clase_20::test_rechaza_perfil_con_vocabulario_invalido PASSED                                                                                                                          [100%]

==================================================================================== 68 passed in 0.39s =====================================================================================
```

## Pruebas propias

## Pruebas propias

| Prueba | Regla protegida | Alternativa que distingue | Resultado |
| --- | --- | --- | --- |
| **1. BFS vs Dijkstra** | Costos variables requieren buscar la ruta global más barata, no la de menos saltos. | BFS con cola. | Rechaza la propuesta y exige usar Dijkstra con Heap. |
| **2. 0-1 BFS vs BFS** | Los costos estrictos de 0 o 1 permiten una optimización enviando atajos al frente. | BFS con cola. | Rechaza la propuesta y exige usar 0-1 BFS con Deque. |
| **3. Dijkstra vs Kruskal** | Conectar toda la red al mínimo costo total es distinto a buscar viajes individuales rápidos. | Dijkstra con Heap. | Rechaza la propuesta y exige usar Kruskal con Union-Find. |
| **4. BFS vs Kahn** | Para ordenar dependencias hay que liberar requisitos previos, no solo avanzar niveles. | BFS con cola. | Rechaza la propuesta y exige usar Kahn con grados de entrada. |
| **5. Pesos negativos fuera del alcance** | Los costos que "devuelven dinero" rompen la lógica matemática de los caminos mínimos. | Dijkstra asumiendo que siempre suma. | Rechaza la propuesta y avisa que el caso está fuera de alcance. |
| **6. Kruskal con peso negativo** | Como Kruskal solo ordena conexiones de barata a cara, los costos negativos no lo rompen. | Descartar el algoritmo por tener valores negativos. | Acepta la propuesta como válida y sin errores. |
| **7. Error solo de estructura** | El algoritmo correcto falla si usa una estructura que hace lenta su acción principal. | Dijkstra usando una cola normal. | Rechaza la propuesta avisando únicamente del error de estructura. |
| **8. Perfil inválido** | El código debe protegerse y fallar si recibe escenarios con palabras inventadas. | Intentar adivinar y arrojar un resultado falso. | Detiene el programa y lanza un error de validación inmediato. |

## Falla encontrada y corrección

## Estado final

