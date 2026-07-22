# Revisión técninca a Max de Ochoa
- **Una fortaleza específica:** Mantiene los fórmatos de entrega de forma correcta. Respeta el órden de las actividades y ejecuta correctamente tanto las funciones a implementar como los tests;
- **Un contrato incumplido o caso no cubierto:** Ejecuté mis propias pruebas trayendo de forma temporal su carpeta sobre su implementación y todas pasaron, así que no hay nada no cumplido ;
- **Entrada reproducible:** N/A (Se utilizaron todos los casos límite de mi batería, incluyendo grafos con ciclos: `{"Inicio": None, "A": "B", "B": "C", "C": "B"}` y todos fueron procesados adecuadamente).;
- test ejecutado 
```bash
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> git fetch origin pull/162/head
From https://github.com/Estructuras-de-Datos-Verano/EstructurasDatos
 * branch            refs/pull/162/head -> FETCH_HEAD
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> git checkout FETCH_HEAD -- entregas/clase_16/max
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_16/max clase_16/tests entregas/clase_16/max/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_16\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_16\max\test_estudiante.py

===================================================================== test session starts =====================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_16
configfile: pytest.ini
plugins: anyio-4.7.0
collected 19 items                                                                                                                                             

clase_16\tests\test_publico_dijkstra_robusto.py::test_calcula_distancias_y_predecesores_conocidos PASSED                                                 [  5%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_no_muta_listas_de_adyacencia PASSED                                                                [ 10%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_incluye_vecino_que_no_es_clave PASSED                                                              [ 15%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-1] PASSED                                                                   [ 21%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-0.5] PASSED                                                                 [ 26%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[inf] PASSED                                                                 [ 31%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[-inf] PASSED                                                                [ 36%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[nan] PASSED                                                                 [ 42%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[True] PASSED                                                              [ 47%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[3] PASSED                                                                 [ 52%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[None] PASSED                                                              [ 57%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_arista_con_forma_incorrecta PASSED                                                         [ 63%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_origen_inexistente PASSED                                                                  [ 68%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_destino_inalcanzable_conserva_infinito_y_camino_vacio PASSED                                       [ 73%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_origen_igual_a_destino PASSED                                                                      [ 78%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_reconstruccion_rechaza_ciclo PASSED                                                                [ 84%]
clase_16::test_max1 <- ..\entregas\clase_16\max\test_estudiante.py PASSED                                                                                [ 89%]
clase_16::test_max2 <- ..\entregas\clase_16\max\test_estudiante.py PASSED                                                                                [ 94%]
clase_16::test_max3 <- ..\entregas\clase_16\max\test_estudiante.py PASSED                                                                                [100%]

===================================================================== 19 passed in 0.08s ======================================================================
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> git rm -rf entregas/clase_16/max
rm 'entregas/clase_16/max/discusion.md'
rm 'entregas/clase_16/max/implementacion.py'
rm 'entregas/clase_16/max/notebook.md'
rm 'entregas/clase_16/max/reporte_pytest.md'
rm 'entregas/clase_16/max/test_estudiante.py'
``` 
- **Recomendación localizada:** Ninguna;
- **Respuesta del autor:** EN ESPERA.