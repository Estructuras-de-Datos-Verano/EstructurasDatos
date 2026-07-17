- Diferencia entre distancia por aristas y por pesos.

Cuando todas las aristas pesan igual, sólo buscamos que se recorran las menos posibles. En el peso, cada arista vale distinto. Tomamos el camino que sume menos.

- Significado de distancia tentativa.

La distancia que tenemos antes de encontrar la final.

- Relajación con un ejemplo numérico.

Un ejemplo sería un grafo con A, B, C, como el de la clase. A se conecte con B por 1, y B con C por 2. Si A se conecta con C por algo mayor al total 3, conviene más pasar por B, aunque sean más aristas.

- Razón para usar min-heap.

Una min-heap siempre extrae el mínimo. Eso es útil porque queremos sumar lo menos.

- Entrada obsoleta y eliminación perezosa.

La entrada obsoleta y eliminación perezosa funciona porque, a veces, una ruta que parecía funcionar suma más que otra que descartamos. Entonces, hay que conservar rutas antiguas por si sirven.

- Reconstrucción mediante predecesores.

Dijkstra reconstruye desde predecesores, buscando las rutas para llegar a un nodo actual.

- Complejidad temporal y espacial.

Iniciar un diccionario cuesta n para n nodos. Examinar cada arista desde su origen cuesta m para m aristas. Cada extracción tiene costo O(log n)

- Restricción de pesos no negativos.

No puede haber pesos negativos porque Dijkstra sólo espera que el costo aumente.

- Caso donde BFS falla.

Donde no todas las aristas pesan igual.

- Evidencia de tus pruebas.

Ejecutando:
C:\Program Files\Python314\python.exe -m pytest -v C:\Users\0276395\Documents\GitHub\EstructurasDatos\clase_15\tests

============================= test session starts =============================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0 -- C:\Program Files\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0276395\Documents\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
collecting ... collected 14 items

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED [  7%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED [ 14%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED [ 21%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED [ 28%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED [ 42%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED [ 50%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED [ 57%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED [ 64%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED [ 71%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED [ 78%]
clase_15\tests\test_publico_dijkstra.py::test_agregado_1_distancia_mejorada PASSED [ 85%]
clase_15\tests\test_publico_dijkstra.py::test_agregado_2_destino_ausente PASSED [ 92%]
clase_15\tests\test_publico_dijkstra.py::test_agregado_3_ruta_claramente_obsoleta PASSED [100%]

============================= 14 passed in 0.02s ==============================

- Hallazgo de la revisión técnica.


