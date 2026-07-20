# Revisión técnica a Santiago Vázquez

- **Una fortaleza específica:** Mantiene los formatos de entrega de forma correcta. Desarrolla una batería de pruebas unitarias sumamente exhaustiva, validando correctamente casos críticos de tipos (`TypeError`), rangos indexados (`IndexError`), pesos no finitos e infinitos en el algoritmo de Kruskal, así como la invariabilidad ante mutaciones.
- **Un contrato incumplido o caso no cubierto:** Ejecuté mis propias pruebas trayendo de forma temporal su carpeta sobre su implementación y todas pasaron, así que no hay nada no cumplido;
- **Entrada reproducible:** N/A (Se utilizaron todos los casos límite de la batería provista por el estudiante, incluyendo grafos disconexos, componentes de un solo nodo, autoaristas con bucles y validaciones de tipos estrictos, y todos fueron procesados adecuadamente);
- **Test ejecutado:**
```bash
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> git fetch origin pull/179/head
From [https://github.com/Estructuras-de-Datos-Verano/EstructurasDatos](https://github.com/Estructuras-de-Datos-Verano/EstructurasDatos)
 * branch            refs/pull/179/head -> FETCH_HEAD
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> git checkout FETCH_HEAD -- entregas/clase_18/santiago
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_18/santiago clase_18/tests entregas/clase_18/santiago/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_18\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_18\santiago\test_estudiante.py

===================================================================== test session starts =====================================================================
platform win32 -- Python 3.13.0, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_18
configfile: pytest.ini
plugins: anyio-4.7.0
collected 33 items                                                                                                                                             

clase_18\tests\test_publico_union_find.py::test_inicializacion_conjuntos PASSED                                                                          [  3%]
clase_18\tests\test_publico_union_find.py::test_find_con_compresion_rutas PASSED                                                                         [  6%]
clase_18\tests\test_publico_union_find.py::test_union_por_rango PASSED                                                                                   [  9%]
clase_18\tests\test_publico_union_find.py::test_union_mismo_conjunto PASSED                                                                              [ 12%]
clase_18\tests\test_publico_kruskal.py::test_kruskal_grafo_conectado PASSED                                                                              [ 15%]
clase_18\tests\test_publico_kruskal.py::test_kruskal_grafo_disconexo PASSED                                                                              [ 18%]
clase_18\tests\test_publico_kruskal.py::test_kruskal_pesos_negativos PASSED                                                                              [ 21%]
clase_18\tests\test_publico_kruskal.py::test_rechaza_grafo_vacio PASSED                                                                                  [ 24%]
clase_18\tests\test_publico_kruskal.py::test_rechaza_arista_malformada PASSED                                                                            [ 27%]
clase_18\tests\test_publico_kruskal.py::test_rechaza_tipos_invalidos PASSED                                                                              [ 30%]
clase_18\tests\test_publico_kruskal.py::test_rendimiento_grafo_denso PASSED                                                                              [ 33%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_cero_elementos PASSED                                                                     [ 36%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_un_elemento PASSED                                                                        [ 39%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_inicialmente_separado PASSED                                                              [ 42%]
entregas/clase_18/santiago/test_estudiante.py::test_union_efectiva_repetida_y_reflexiva PASSED                                                           [ 45%]
entregas/clase_18/santiago/test_estudiante.py::test_transitividad_conectividad_y_tamano PASSED                                                           [ 48%]
entregas/clase_18/santiago/test_compresion_no_cambia_particion_ni_contador PASSED                                                                        [ 51%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_rechaza_cantidad_de_tipo_invalido PASSED                                                  [ 54%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_rechaza_cantidad_negativa PASSED                                                          [ 57%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_rechaza_indice_fuera_de_rango PASSED                                                      [ 60%]
entregas/clase_18/santiago/test_estudiante.py::test_union_find_rechaza_indice_de_tipo_invalido PASSED                                                    [ 63%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_grafo_conductor_costo_y_v_menos_uno PASSED                                                   [ 66%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_cero_y_un_vertice PASSED                                                                     [ 69%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_dos_vertices_y_una_arista PASSED                                                             [ 72%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_triangulo_rechaza_ciclo PASSED                                                                [ 75%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_desconectado_devuelve_none PASSED                                                             [ 78%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_admite_pesos_negativos_y_cero PASSED                                                           [ 81%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_empates_verifica_propiedades_no_lista_exacta PASSED                                          [ 84%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_aristas_paralelas_y_autoaristas PASSED                                                       [ 87%]
entregas/clase_18/santiago/test_estudiante.py::test_kruskal_no_modifica_aristas PASSED                                                                   [ 90%]
entregas/clase_18/santiago/test_estudiante.py::test_costo_reparacion_red_conectada_y_resultado_entero PASSED                                             [ 93%]
entregas/clase_18/santiago/test_estudiante.py::test_costo_reparacion_desconectada_y_una_ciudad PASSED                                                    [ 96%]
entregas/clase_18/santiago/test_estudiante.py::test_costo_reparacion_no_muta_y_rechaza_costo_float PASSED                                                [100%]

===================================================================== 33 passed in 0.09s ======================================================================
```
- **Recomendación** : Nula
- *** Respuesta en espera ***