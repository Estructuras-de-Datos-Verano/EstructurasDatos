# Discusion - Arturo Prudencio Bonilla

## Diferencia entre distancia por aristas y por pesos.
En grafos no ponderados, la distancia significa simplemente el número de aristas que componen un camino. Sin embargo, en grafos ponderados, la distancia significa la suma total de los pesos a lo largo del camino

Por eso es diferente como debemos recorrerlos y con que estructura
## Significado de distancia tentativa.
Se le llama distancia tentativa a la mejor distancia o costo mínimo que se conoce hasta un momento dado durante la ejecución del algoritmo. Es tentativa porque permanece abierta a ser modificada si el algoritmo descubre posteriormente otra ruta más barata para llegar a ese mismo nodo.

## Relajación con un ejemplo numérico.
Relajar una arista significa intentar mejorar la mejor distancia conocida hacia un nodo destino utilizando dicha arista: Por ejemplo, si tenemos una distancia registrada al nodo B de 4, y existe una arista de B hacia D con un peso de 2, calculamos una candidata: $4 + 2 = 6$. Si la distancia actual conocida hacia D era 10, la candidata es mejor ($6 < 10$), por lo que la distancia de D se actualiza a 6 y su nodo predecesor pasa a ser B

## Razón para usar min-heap.
Se usa porque el algoritmo requiere extraer y procesar siempre el nodo que tenga la menor distancia acumulada conocida en cada paso

## Entrada obsoleta y eliminación perezosa.
Cuando se descubre un camino mejor hacia un nodo, se inserta la nueva candidatura en el heap, pero la candidatura vieja (ahora obsoleta) se deja ahí porque intentar buscarla y borrarla complicaría la implementación

## Reconstrucción mediante predecesores.
El mapa de predecesores funciona como una cadena que apunta hacia atrás, registrando desde qué nodo anterior se llegó al actual con el menor costo

Para reconstruir la ruta, se inicia en el nodo destino y se siguen estos apuntadores en reversa hasta alcanzar el origen. Como la secuencia se obtuvo de destino a origen, el último paso consiste en invertir la lista resultante para presentar el camino correcto.

## Complejidad temporal y espacial.


## Restricción de pesos no negativos.
Necesitamos pesos no negativos pues el enfoque del algorito es: una vez que se extrae la menor distancia vigente de la cola, ninguna ruta futura podrá regresar a ese nodo con un costo menor. Si existieran pesos negativos, esta garantía se rompería

## Caso donde BFS falla.
BFS falla en grafos ponderados porque prioriza niveles (menos aristas) sobre costos

## Evidencia de tus pruebas.
Ejecutando:
C:\Users\0255295\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe -m pytest -v C:\Users\0255295\Documents\GitHub\EstructurasDatos\clase_15\tests C:\Users\0255295\Documents\GitHub\EstructurasDatos\entregas\clase_15\arturo\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0255295\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0255295\Documents\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
plugins: anyio-4.14.0
collecting ... collected 17 items

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED [  5%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED [ 11%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED [ 17%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED [ 23%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED [ 29%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED [ 41%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED [ 47%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED [ 52%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED [ 58%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED [ 64%]
clase_15\tests\test_publico_dijkstra.py::test_distancia_mejora_al_menos_dos_veces_ARTURO PASSED [ 70%]
clase_15\tests\test_publico_dijkstra.py::test_destino_inalcanzable_devuelve_infinito_y_lista_vacia_ARTURO PASSED [ 76%]
clase_15\tests\test_publico_dijkstra.py::test_entrada_obsoleta_ruta_directa_costosa_ARTURO PASSED [ 82%]
clase_15::test_distancia_mejora_al_menos_dos_veces_ARTURO <- ..\entregas\clase_15\arturo\test_estudiante.py PASSED [ 88%]
clase_15::test_destino_inalcanzable_devuelve_infinito_y_lista_vacia_ARTURO <- ..\entregas\clase_15\arturo\test_estudiante.py PASSED [ 94%]
clase_15::test_entrada_obsoleta_ruta_directa_costosa_ARTURO <- ..\entregas\clase_15\arturo\test_estudiante.py PASSED [100%]

============================= 17 passed in 0.04s ==============================

## Hallazgo de la revisión técnica.