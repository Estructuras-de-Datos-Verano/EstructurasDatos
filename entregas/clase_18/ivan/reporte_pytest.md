
## Reporte de pytest 

## Comando ejecutado

```bash
python evaluar.py entregas/clase_18/ivan clase_18/tests entregas/clase_18/ivan/test_estudiante.py
```

## Salida completa de `pytest -v`

```powershell

PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_18/ivan clase_18/tests entregas/clase_18/ivan/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_18\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_18\ivan\test_estudiante.py

============================================================================= test session starts =============================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_18
configfile: pytest.ini
plugins: anyio-4.7.0
collected 106 items                                                                                                                                                            

clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_cero_elementos PASSED                                                                                 [  0%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_un_elemento PASSED                                                                                    [  1%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_inicialmente_separado PASSED                                                                          [  2%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_efectiva_repetida_y_reflexiva PASSED                                                                       [  3%]
clase_18\tests\test_publico_union_find_kruskal.py::test_transitividad_conectividad_y_tamano PASSED                                                                       [  4%]
clase_18\tests\test_publico_union_find_kruskal.py::test_compresion_no_cambia_particion_ni_contador PASSED                                                                [  5%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[True] PASSED                                                        [  6%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[False] PASSED                                                       [  7%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3.0] PASSED                                                         [  8%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3] PASSED                                                           [  9%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[None] PASSED                                                        [ 10%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_negativa PASSED                                                                      [ 11%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[-1] PASSED                                                              [ 12%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[3] PASSED                                                               [ 13%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[True] PASSED                                                          [ 14%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1.0] PASSED                                                           [ 15%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1] PASSED                                                             [ 16%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[None] PASSED                                                          [ 16%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_grafo_conductor_costo_y_v_menos_uno PASSED                                                               [ 17%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_cero_y_un_vertice PASSED                                                                                 [ 18%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_dos_vertices_y_una_arista PASSED                                                                         [ 19%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_triangulo_rechaza_ciclo PASSED                                                                           [ 20%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_desconectado_devuelve_none PASSED                                                                        [ 21%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_admite_pesos_negativos_y_cero PASSED                                                                     [ 22%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_empates_verifica_propiedades_no_lista_exacta PASSED                                                      [ 23%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_aristas_paralelas_y_autoaristas PASSED                                                                   [ 24%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_no_modifica_aristas PASSED                                                                               [ 25%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[True] PASSED                                                            [ 26%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3.0] PASSED                                                             [ 27%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3] PASSED                                                               [ 28%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[None] PASSED                                                            [ 29%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_negativo PASSED                                                                  [ 30%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista0] PASSED                                                               [ 31%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista1] PASSED                                                               [ 32%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[True] PASSED                                                            [ 33%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0.0] PASSED                                                             [ 33%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0] PASSED                                                               [ 34%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[None] PASSED                                                            [ 35%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[-1] PASSED                                                                [ 36%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[2] PASSED                                                                 [ 37%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[True] PASSED                                                                    [ 38%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[3] PASSED                                                                       [ 39%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[None] PASSED                                                                    [ 40%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[peso3] PASSED                                                                   [ 41%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[inf] PASSED                                                                       [ 42%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[-inf] PASSED                                                                      [ 43%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[nan] PASSED                                                                       [ 44%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_red_conectada_y_resultado_entero PASSED                                                         [ 45%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_desconectada_y_una_ciudad PASSED                                                                [ 46%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_no_muta_y_rechaza_costo_float PASSED                                                            [ 47%]
clase_18::test_union_find_cero_elementos PASSED                                                                                                                          [ 48%]
clase_18::test_union_find_un_elemento PASSED                                                                                                                             [ 49%]
clase_18::test_union_find_inicialmente_separado PASSED                                                                                                                   [ 50%]
clase_18::test_union_efectiva_repetida_y_reflexiva PASSED                                                                                                                [ 50%]
clase_18::test_transitividad_conectividad_y_tamano PASSED                                                                                                                [ 51%]
clase_18::test_compresion_no_cambia_particion_ni_contador PASSED                                                                                                         [ 52%]
clase_18::test_union_find_rechaza_cantidad_de_tipo_invalido[True] PASSED                                                                                                 [ 53%]
clase_18::test_union_find_rechaza_cantidad_de_tipo_invalido[False] PASSED                                                                                                [ 54%]
clase_18::test_union_find_rechaza_cantidad_de_tipo_invalido[3.0] PASSED                                                                                                  [ 55%]
clase_18::test_union_find_rechaza_cantidad_de_tipo_invalido[3] PASSED                                                                                                    [ 56%]
clase_18::test_union_find_rechaza_cantidad_de_tipo_invalido[None] PASSED                                                                                                 [ 57%]
clase_18::test_union_find_rechaza_cantidad_negativa PASSED                                                                                                               [ 58%]
clase_18::test_union_find_rechaza_indice_fuera_de_rango[-1] PASSED                                                                                                       [ 59%]
clase_18::test_union_find_rechaza_indice_fuera_de_rango[3] PASSED                                                                                                        [ 60%]
clase_18::test_union_find_rechaza_indice_de_tipo_invalido[True] PASSED                                                                                                   [ 61%]
clase_18::test_union_find_rechaza_indice_de_tipo_invalido[1.0] PASSED                                                                                                    [ 62%]
clase_18::test_union_find_rechaza_indice_de_tipo_invalido[1] PASSED                                                                                                      [ 63%]
clase_18::test_union_find_rechaza_indice_de_tipo_invalido[None] PASSED                                                                                                   [ 64%]
clase_18::test_kruskal_grafo_conductor_costo_y_v_menos_uno PASSED                                                                                                        [ 65%]
clase_18::test_kruskal_cero_y_un_vertice PASSED                                                                                                                          [ 66%]
clase_18::test_kruskal_dos_vertices_y_una_arista PASSED                                                                                                                  [ 66%]
clase_18::test_kruskal_triangulo_rechaza_ciclo PASSED                                                                                                                    [ 67%]
clase_18::test_kruskal_desconectado_devuelve_none PASSED                                                                                                                 [ 68%]
clase_18::test_kruskal_admite_pesos_negativos_y_cero PASSED                                                                                                              [ 69%]
clase_18::test_kruskal_empates_verifica_propiedades_no_lista_exacta PASSED                                                                                               [ 70%]
clase_18::test_kruskal_aristas_paralelas_y_autoaristas PASSED                                                                                                            [ 71%]
clase_18::test_kruskal_no_modifica_aristas PASSED                                                                                                                        [ 72%]
clase_18::test_kruskal_rechaza_numero_vertices_invalido[True] PASSED                                                                                                     [ 73%]
clase_18::test_kruskal_rechaza_numero_vertices_invalido[3.0] PASSED                                                                                                      [ 74%]
clase_18::test_kruskal_rechaza_numero_vertices_invalido[3] PASSED                                                                                                        [ 75%]
clase_18::test_kruskal_rechaza_numero_vertices_invalido[None] PASSED                                                                                                     [ 76%]
clase_18::test_kruskal_rechaza_numero_vertices_negativo PASSED                                                                                                           [ 77%]
clase_18::test_kruskal_rechaza_arista_mal_formada[arista0] PASSED                                                                                                        [ 78%]
clase_18::test_kruskal_rechaza_arista_mal_formada[arista1] PASSED                                                                                                        [ 79%]
clase_18::test_kruskal_rechaza_extremo_de_tipo_invalido[True] PASSED                                                                                                     [ 80%]
clase_18::test_kruskal_rechaza_extremo_de_tipo_invalido[0.0] PASSED                                                                                                      [ 81%]
clase_18::test_kruskal_rechaza_extremo_de_tipo_invalido[0] PASSED                                                                                                        [ 82%]
clase_18::test_kruskal_rechaza_extremo_de_tipo_invalido[None] PASSED                                                                                                     [ 83%]
clase_18::test_kruskal_rechaza_vertice_fuera_de_rango[-1] PASSED                                                                                                         [ 83%]
clase_18::test_kruskal_rechaza_vertice_fuera_de_rango[2] PASSED                                                                                                          [ 84%]
clase_18::test_kruskal_rechaza_peso_no_numerico[True] PASSED                                                                                                             [ 85%]
clase_18::test_kruskal_rechaza_peso_no_numerico[3] PASSED                                                                                                                [ 86%]
clase_18::test_kruskal_rechaza_peso_no_numerico[None] PASSED                                                                                                             [ 87%]
clase_18::test_kruskal_rechaza_peso_no_numerico[peso3] PASSED                                                                                                            [ 88%]
clase_18::test_kruskal_rechaza_peso_no_finito[inf] PASSED                                                                                                                [ 89%]
clase_18::test_kruskal_rechaza_peso_no_finito[-inf] PASSED                                                                                                               [ 90%]
clase_18::test_kruskal_rechaza_peso_no_finito[nan] PASSED                                                                                                                [ 91%]
clase_18::test_costo_reparacion_red_conectada_y_resultado_entero PASSED                                                                                                  [ 92%]
clase_18::test_costo_reparacion_desconectada_y_una_ciudad PASSED                                                                                                         [ 93%]
clase_18::test_costo_reparacion_no_muta_y_rechaza_costo_float PASSED                                                                                                     [ 94%]
clase_18::test_union_find_valida_indices_negativos PASSED                                                                                                                [ 95%]
clase_18::test_union_mismo_elemento_no_afecta_estructura PASSED                                                                                                          [ 96%]
clase_18::test_union_por_tamano_subordina_arbol_menor PASSED                                                                                                             [ 97%]
clase_18::test_kruskal_acepta_pesos_negativos_correctamente PASSED                                                                                                       [ 98%]
clase_18::test_kruskal_casos_base_cero_o_un_vertice PASSED                                                                                                               [ 99%]
clase_18::test_kruskal_manejo_de_autoaristas_y_paralelas PASSED                                                                                                          [100%]

============================================================================= 106 passed in 0.44s =============================================================================


```

## Resumen

#### - Cantidad de pruebas:
106
#### - Pruebas aprobadas:
106
#### - Errores o fallos:
No

## Evidencia técnica

#### - Prueba propia más importante:
test_kruskal_manejo_de_autoaristas_y_paralelas
#### - Invariante protegido:
Garantiza la ausencia de ciclos y autoenlaces en el bosque, asegurando además la correcta selección del costo mínimo entre aristas paralelas para preservar la optimalidad global del MST.
#### - Ejemplo de unión redundante:
Llamar a `union(0, 3)` después de haber fusionado previamente las componentes `{0, 1}` y `{2, 3}`, lo cual no altera el número de raíces y devuelve `False`[cite: 1].
#### - Ejemplo de arista rechazada:
La arista A–B con costo 4 en el ejemplo conductor, la cual es descartada debido a que sus extremos ya se encuentran conectados por la red elegida, cerrando un ciclo[cite: 1].
#### - Resultado de un grafo desconectado:
La función devuelve `None` debido a que las aristas disponibles se agotan por completo antes de poder seleccionar las V-1 aristas necesarias para integrar la red global[cite: 1].

## Corrección después de un fallo

#### Describe el comportamiento inicial, el contrato roto, la corrección localizada y el resultado posterior.

**Comportamiento inicial:** El método `union` enlazaba de forma directa el nodo `a` debajo del nodo `b` sin resolver primero cuáles eran sus componentes líderes.
**Contrato roto:** Se violaba la invariante estructural de Union-Find, dado que conectar nodos arbitrarios en lugar de sus representantes generaba una representación totalmente inconsistente.
**Corrección localizada:** Se modificó la función para buscar y obtener obligatoriamente ambas raíces mediante `find` antes de realizar cualquier enlace o evaluar tamaños.
***Resultado posterior:** El árbol mantiene una estructura coherente y limpia donde todas las cadenas de padres resuelven de forma correcta hacia una única raíz válida.