# Reporte Pytest
**Comando:** python evaluar.py entregas/clase_16/ivan clase_16/tests entregas/clase_16/ivan/test_estudiante.py ;
**Salida completa:** PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_16/ivan clase_16/tests entregas/clase_16/ivan/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_16\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_16\ivan\test_estudiante.py

============================================================================= test session starts =============================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_16
configfile: pytest.ini
plugins: anyio-4.7.0
collected 40 items                                                                                                                                                             

clase_16\tests\test_publico_dijkstra_robusto.py::test_calcula_distancias_y_predecesores_conocidos PASSED                                                                 [  2%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_no_muta_listas_de_adyacencia PASSED                                                                                [  5%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_incluye_vecino_que_no_es_clave PASSED                                                                              [  7%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-1] PASSED                                                                                   [ 10%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-0.5] PASSED                                                                                 [ 12%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[inf] PASSED                                                                                 [ 15%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[-inf] PASSED                                                                                [ 17%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[nan] PASSED                                                                                 [ 20%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[True] PASSED                                                                              [ 22%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[3] PASSED                                                                                 [ 25%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[None] PASSED                                                                              [ 27%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_arista_con_forma_incorrecta PASSED                                                                         [ 30%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_origen_inexistente PASSED                                                                                  [ 32%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_destino_inalcanzable_conserva_infinito_y_camino_vacio PASSED                                                       [ 35%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_origen_igual_a_destino PASSED                                                                                      [ 37%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_reconstruccion_rechaza_ciclo PASSED                                                                                [ 40%]
clase_16::test_calcula_distancias_y_predecesores_conocidos <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                        [ 42%]
clase_16::test_no_muta_listas_de_adyacencia <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                       [ 45%]
clase_16::test_incluye_vecino_que_no_es_clave <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                     [ 47%]
clase_16::test_rechaza_peso_negativo[-1] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                          [ 50%]
clase_16::test_rechaza_peso_negativo[-0.5] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                        [ 52%]
clase_16::test_rechaza_peso_no_finito[inf] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                        [ 55%]
clase_16::test_rechaza_peso_no_finito[-inf] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                       [ 57%]
clase_16::test_rechaza_peso_no_finito[nan] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                        [ 60%]
clase_16::test_rechaza_peso_no_numerico[True] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                     [ 62%]
clase_16::test_rechaza_peso_no_numerico[3] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                        [ 65%]
clase_16::test_rechaza_peso_no_numerico[None] <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                     [ 67%]
clase_16::test_rechaza_arista_con_forma_incorrecta <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                [ 70%]
clase_16::test_rechaza_origen_inexistente <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                         [ 72%]
clase_16::test_destino_inalcanzable_conserva_infinito_y_camino_vacio <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                              [ 75%]
clase_16::test_origen_igual_a_destino <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                             [ 77%]
clase_16::test_reconstruccion_rechaza_ciclo <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                       [ 80%]
clase_16::test_grafo_no_mapping <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                                   [ 82%]
clase_16::test_nodo_no_str <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                                        [ 85%]
clase_16::test_vecino_no_str <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                                      [ 87%]
clase_16::test_entrada_obsoleta <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                                   [ 90%]
clase_16::test_rechaza_peso_booleano <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                              [ 92%]
clase_16::test_vecino_implicito_y_no_mutacion <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                     [ 95%]
clase_16::test_rechaza_nan_e_infinito <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                             [ 97%]
clase_16::test_detecta_ciclo_predecesores <- ..\entregas\clase_16\ivan\test_estudiante.py PASSED                                                                         [100%]

============================================================================= 40 passed in 0.14s ============================================================================== ; 
**Número de pruebas:** 40
### Fallo convertido en regresión automatizada
Si el diccionario de predecesores venía malformado con un ciclo (por ejemplo, B apunta a C, y C apunta a B), la función `reconstruir_camino` se quedaba atrapada en un `while` infinito si no llegaba al origen.

**La prueba de regresión (test):**
Para evitar que esto vuelva a pasar, creamos la prueba automatizada `test_detecta_ciclo_predecesores`. Esta prueba inyecta deliberadamente un diccionario circular:
`{"Inicio": None, "A": "B", "B": "C", "C": "B"}`
Y afirma mediante `pytest.raises` que el sistema debe lanzar un `ValueError` con la palabra "ciclo" en lugar de colgarse.

**Solución implementada:**
En el código principal de `reconstruir_camino`, agregamos un conjunto (set) llamado `visitados`. En cada iteración del bucle, revisamos si el nodo actual ya está en `visitados`; si es así, lanzamos el error, rompiendo el ciclo y haciendo que la prueba pase.