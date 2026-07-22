# Guía de revisión técnica — Clase 18 - Hecha por Leo

## 1. Confirma rama y archivos.
Nombre de la rama y del PR correctos. Se subieron exactamente los 5 archivos

## 2. Resume el enfoque sin reescribir la solución.
Se implementó el código de Union-Find y de Kruskal. Se hicieron pruebas para verificar que stuviera bien implementado y se responideron las preguntas de verificación de entendimiento.

## 4. Revisa reconstrucción, errores y no mutación.
Lo hace correctamente según sus pruebas, a continuación se revisará con mis pruebas:

## 5. Ejecuta pruebas públicas y propias con `pytest -v`.
Se ejecutaron las pruebas y todas pasaron, lo que quiere decir que la implementación está correcta

### Pega la salida completa.

Ejecutando:
C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_18\tests C:\Users\0254049\Documents\GitHub\EstructurasDatos\entregas\clase_18\LEO\test_estudiante.py

=========================================================== test session starts ============================================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_18
configfile: pytest.ini
collected 56 items                                                                                                                          

clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_cero_elementos PASSED                                              [  1%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_un_elemento PASSED                                                 [  3%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_inicialmente_separado PASSED                                       [  5%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_efectiva_repetida_y_reflexiva PASSED                                    [  7%]
clase_18\tests\test_publico_union_find_kruskal.py::test_transitividad_conectividad_y_tamano PASSED                                    [  8%]
clase_18\tests\test_publico_union_find_kruskal.py::test_compresion_no_cambia_particion_ni_contador PASSED                             [ 10%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[True] PASSED                     [ 12%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[False] PASSED                    [ 14%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3.0] PASSED                      [ 16%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[3] PASSED                        [ 17%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_de_tipo_invalido[None] PASSED                     [ 19%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_cantidad_negativa PASSED                                   [ 21%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[-1] PASSED                           [ 23%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_fuera_de_rango[3] PASSED                            [ 25%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[True] PASSED                       [ 26%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1.0] PASSED                        [ 28%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[1] PASSED                          [ 30%]
clase_18\tests\test_publico_union_find_kruskal.py::test_union_find_rechaza_indice_de_tipo_invalido[None] PASSED                       [ 32%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_grafo_conductor_costo_y_v_menos_uno PASSED                            [ 33%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_cero_y_un_vertice PASSED                                              [ 35%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_dos_vertices_y_una_arista PASSED                                      [ 37%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_triangulo_rechaza_ciclo PASSED                                        [ 39%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_desconectado_devuelve_none PASSED                                     [ 41%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_admite_pesos_negativos_y_cero PASSED                                  [ 42%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_empates_verifica_propiedades_no_lista_exacta PASSED                   [ 44%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_aristas_paralelas_y_autoaristas PASSED                                [ 46%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_no_modifica_aristas PASSED                                            [ 48%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[True] PASSED                         [ 50%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3.0] PASSED                          [ 51%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[3] PASSED                            [ 53%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_invalido[None] PASSED                         [ 55%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_numero_vertices_negativo PASSED                               [ 57%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista0] PASSED                            [ 58%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_arista_mal_formada[arista1] PASSED                            [ 60%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[True] PASSED                         [ 62%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0.0] PASSED                          [ 64%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[0] PASSED                            [ 66%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_extremo_de_tipo_invalido[None] PASSED                         [ 67%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[-1] PASSED                             [ 69%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_vertice_fuera_de_rango[2] PASSED                              [ 71%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[True] PASSED                                 [ 73%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[3] PASSED                                    [ 75%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[None] PASSED                                 [ 76%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_numerico[peso3] PASSED                                [ 78%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[inf] PASSED                                    [ 80%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[-inf] PASSED                                   [ 82%]
clase_18\tests\test_publico_union_find_kruskal.py::test_kruskal_rechaza_peso_no_finito[nan] PASSED                                    [ 83%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_red_conectada_y_resultado_entero PASSED                      [ 85%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_desconectada_y_una_ciudad PASSED                             [ 87%]
clase_18\tests\test_publico_union_find_kruskal.py::test_costo_reparacion_no_muta_y_rechaza_costo_float PASSED                         [ 89%]
clase_18::test_union_une_componentes_grandes_LEO PASSED                                                                               [ 91%]
clase_18::test_union_repetida_no_modifica_tamano_LEO PASSED                                                                           [ 92%]
clase_18::test_transitividad_cadena_larga_LEO PASSED                                                                                  [ 94%]
clase_18::test_tamano_componente_despues_de_varias_uniones_LEO PASSED                                                                 [ 96%]
clase_18::test_kruskal_descarta_camino_que_forma_ciclo_LEO PASSED                                                                     [ 98%]
clase_18::test_kruskal_grafo_con_un_vertice_aislado_LEO PASSED                                                                        [100%]

============================================================ 56 passed in 0.09s ============================================================


## 6. Escribe fortalezas y mejoras accionables.
Considero que la única mejora accionable es que las respuestas de discusion.md podrían ser más reflexivas

## 7. Solicita respuesta del autor con checklist.

- [ ] Entregué exactamente cinco archivos.
- [ ] Respondí fuera del notebook.
- [ ] Probé índices negativos y `bool`.
- [ ] La unión redundante no altera contador.
- [ ] Implementé compresión y unión por tamaño.
- [ ] No muté las aristas.
- [ ] Admití pesos negativos y rechacé no finitos.
- [ ] Detecté grafo desconectado.
- [ ] No exigí un MST específico con empates.
- [ ] Agregué seis pruebas explicadas.
- [ ] Guardé la salida completa de `pytest -v`.
- [ ] No agregué cachés.