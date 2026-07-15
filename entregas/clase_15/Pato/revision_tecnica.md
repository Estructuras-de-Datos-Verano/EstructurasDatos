# Revision hecha por Leo

## 1. Confirma rama y archivos.
Todo está perfecto, excepto por el detalle del nombre de la rama

## 2. Resume el enfoque sin reescribir la solución.
Se implementó la solución Dijkstra

## 3. Revisa inicialización, relajación, heap y entradas obsoletas.
Lo tiene bien implementado

## 4. Revisa reconstrucción, errores y no mutación.
Lo tiene bien implementado

## 5. Ejecuta pruebas públicas y propias con `pytest -v`. Pega la salida completa.
Ejecutando:
C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_15\tests C:\Users\0254049\Documents\GitHub\EstructurasDatos\entregas\clase_15\LEO\test_estudiante.py

============================================= test session starts ==============================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
collected 14 items                                                                                              

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED         [  7%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED                   [ 14%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED              [ 21%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED                     [ 28%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED                  [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED                         [ 42%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED                               [ 50%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED                             [ 57%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED                        [ 64%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED                          [ 71%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED                            [ 78%]
clase_15::test_distancia_mejora_y_descarta_entrada_obsoleta_LEO <- ..\entregas\clase_15\LEO\test_estudiante.py PASSED [ 85%]
clase_15::test_destino_inalcanzable_LEO <- ..\entregas\clase_15\LEO\test_estudiante.py PASSED             [ 92%]
clase_15::test_ruta_indirecta_es_mejor_que_directa_LEO <- ..\entregas\clase_15\LEO\test_estudiante.py PASSED [100%]

============================================== 14 passed in 0.05s ==============================================

## 6. Escribe fortalezas y mejoras accionables.
Todo salió perfecto tanto en las pruebas como en la implementación y los .md y hay que implementar docstrings en las pruebas

## 7. Solicita respuesta del autor con checklist
- [ ] La rama cumple `clase-15-nombre`.
- [ ] Solo modifiqué `entregas/clase_15/nombre/`.
- [ ] Entregué los cinco archivos obligatorios.
- [ ] Respondí todas las preguntas del notebook en `notebook.md`.
- [ ] Usé las firmas, type hints y docstrings solicitados.
- [ ] No muté el grafo.
- [ ] Rechacé pesos negativos.
- [ ] Probé entradas obsoletas e inalcanzables.
- [ ] Guardé la salida completa de pytest.
- [ ] Realicé o recibí revisión técnica.
- [ ] No agregué `.DS_Store`, `__pycache__` ni `.pyc`.