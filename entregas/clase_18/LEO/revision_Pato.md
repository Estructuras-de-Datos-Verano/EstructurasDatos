# Clase 18: Revisión PR
#### Nombre: Patricio Navarro

1. Confirma rama y archivos.
    - Error en nombre de la rama, era `clase-18-Leo` en vez de `clase-18_Leo`.
    - Los archivos bien.
2. Resume el enfoque sin reescribir la solución.
    - Llevar una iteración que lleve un contador con costos e identifique si cae en un bucle.
3. Revisión
    - La implementación es robusta, tiene bien definidios los tipos de errores y se ve bien resuelto.
5. Ejecuta pruebas públicas y propias con `pytest -v`.
6. Pega la salida completa.
Ejecutando:
C:\Users\0261331\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\0261331\Documents\GitHub\EstructurasDatos\clase_18\tests C:\Users\0261331\Documents\GitHub\EstructurasDatos\entregas\clase_18\LEO\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0261331\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0261331\Documents\GitHub\EstructurasDatos\clase_18
configfile: pytest.ini
collecting ... collected 70 items

clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_cero_elementos PASSED [  1%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_un_elemento PASSED [  2%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_inicialmente_separado PASSED [  4%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_efectiva_repetida_y_reflexiva PASSED [  5%]
clase_18\tests\test_publico_union_find_kruskal.py::test_transitividad_conectividad_y_tamano PASSED [  7%]
clase_18\tests\test_publico_union_find_kruskal.py::test_compresion_no_cambia_particion_ni_contador PASSED [  8%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[True] PASSED [ 10%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[False] PASSED [ 11%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3.0] PASSED [ 12%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3] PASSED [ 14%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[None] PASSED [ 15%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_negativa PASSED [ 17%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[-1] PASSED [ 18%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[3] PASSED [ 20%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[True] PASSED [ 21%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1.0] PASSED [ 22%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1] PASSED [ 24%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[None] PASSED [ 25%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_grafo_conductor_costo_y_v_menos_uno PASSED [ 27%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_cero_y_un_vertice PASSED [ 28%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_dos_vertices_y_una_arista PASSED [ 30%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_triangulo_rechaza_ciclo PASSED [ 31%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_desconectado_devuelve_none PASSED [ 32%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_admite_pesos_negativos_y_cero PASSED [ 34%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_empates_verifica_propiedades_no_lista_exacta PASSED [ 35%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_aristas_paralelas_y_autoaristas PASSED [ 37%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_no_modifica_aristas PASSED [ 38%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[True] PASSED [ 40%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3.0] PASSED [ 41%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3] PASSED [ 42%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[None] PASSED [ 44%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_negativo PASSED [ 45%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista0] PASSED [ 47%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista1] PASSED [ 48%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[True] PASSED [ 50%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0.0] PASSED [ 51%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0] PASSED [ 52%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[None] PASSED [ 54%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[-1] PASSED [ 55%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[2] PASSED [ 57%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[True] PASSED [ 58%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[3] PASSED [ 60%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[None] PASSED [ 61%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[peso3] PASSED [ 62%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[inf] PASSED [ 64%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[-inf] PASSED [ 65%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[nan] PASSED [ 67%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_red_conectada_y_resultado_entero PASSED [ 68%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_desconectada_y_una_ciudad PASSED [ 70%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_no_muta_y_rechaza_costo_float PASSED [ 71%]
clase_18::test_union_une_componentes_grandes_LEO PASSED                  [ 72%]
clase_18::test_union_repetida_no_modifica_tamano_LEO PASSED              [ 74%]
clase_18::test_transitividad_cadena_larga_LEO PASSED                     [ 75%]
clase_18::test_tamano_componente_despues_de_varias_uniones_LEO PASSED    [ 77%]
clase_18::test_kruskal_descarta_camino_que_forma_ciclo_LEO PASSED        [ 78%]
clase_18::test_kruskal_grafo_con_un_vertice_aislado_LEO PASSED           [ 80%]
clase_18::test_union_efectiva_reduce_componentes PASSED                  [ 81%]
clase_18::test_union_repetida_no_reduce_componentes PASSED               [ 82%]
clase_18::test_transitividad_y_conectividad PASSED                       [ 84%]
clase_18::test_tamano_componente_actualizado PASSED                      [ 85%]
clase_18::test_kruskal_arista_rechazada_por_ciclo PASSED                 [ 87%]
clase_18::test_kruskal_grafo_desconectado PASSED                         [ 88%]
clase_18::test_union_find_indice_negativo PASSED                         [ 90%]
clase_18::test_kruskal_peso_negativo PASSED                              [ 91%]
clase_18::test_kruskal_aristas_paralelas PASSED                          [ 92%]
clase_18::test_kruskal_autoaristas PASSED                                [ 94%]
clase_18::test_kruskal_empates_valida_propiedades PASSED                 [ 95%]
clase_18::test_kruskal_un_vertice PASSED                                 [ 97%]
clase_18::test_kruskal_no_muta_entrada PASSED                            [ 98%]
clase_18::test_union_find_compresion_caminos PASSED                      [100%]

============================= 70 passed in 0.07s ==============================
7. Escribe fortalezas y mejoras accionables.
- Honestamente lo veo muy bien, podrías agregar un atributo de `_num_elementos` para poder acceder directamente al numero de elementos pero no es del todo necesario y el código funcionó sin problema.
8. Solicita respuesta del autor con checklist.
- [  ] Entregué exactamente cinco archivos.
- [ x ] Respondí fuera del notebook.
- [ x ] Probé índices negativos y `bool`.
- [ x ] La unión redundante no altera contador.
- [ x ] Implementé compresión y unión por tamaño.
- [ x ] No muté las aristas.
- [ x ] Admití pesos negativos y rechacé no finitos.
- [ x ] Detecté grafo desconectado.
- [ x ] No exigí un MST específico con empates.
- [ x ] Agregué seis pruebas explicadas.
- [ x ] Guardé la salida completa de `pytest -v`.
- [ x ] No agregué cachés.