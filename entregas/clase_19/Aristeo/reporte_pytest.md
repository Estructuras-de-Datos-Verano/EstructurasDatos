# Reporte de pruebas — Clase 19

## Comando ejecutado

```text
py evaluar.py entregas/clase_19/Aristeo clase_19/tests entregas/clase_19/Aristeo/test_estudiante.py
```

## Salida completa de pytest -v

```text
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_19
configfile: pytest.ini
plugins: anyio-4.14.1
collected 67 items                                                                                                                                                                                                        

clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_vacio PASSED                                                                                                                                [  1%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_copia_defensiva_y_no_comparte_listas PASSED                                                                                                 [  2%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_vecino_implicito_y_aislado PASSED                                                                                                           [  4%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_elimina_duplicados_establemente PASSED                                                                                                      [  5%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_conserva_orden_de_primera_aparicion PASSED                                                                                                  [  7%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[grafo0] PASSED                                                                                              [  8%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[AB] PASSED                                                                                                  [ 10%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[3] PASSED                                                                                                   [ 11%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[None] PASSED                                                                                                [ 13%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_nodo_no_string PASSED                                                                                                               [ 14%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_vecino_no_string PASSED                                                                                                             [ 16%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[B] PASSED                                                                                                       [ 17%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[3] PASSED                                                                                                       [ 19%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[None] PASSED                                                                                                    [ 20%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[vecinos3] PASSED                                                                                                [ 22%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_acepta_tuplas_y_no_muta PASSED                                                                                                              [ 23%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_vacio PASSED                                                                                                                                    [ 25%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_cadena PASSED                                                                                                                                   [ 26%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_varias_fuentes PASSED                                                                                                                           [ 28%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_vecino_implicito_duplicados_y_aislado PASSED                                                                                                    [ 29%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_vacio PASSED                                                                                                                                     [ 31%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_un_nodo PASSED                                                                                                                                   [ 32%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_cadena PASSED                                                                                                                                    [ 34%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_varias_fuentes_y_varios_ordenes PASSED                                                                                                           [ 35%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_ciclo_simple PASSED                                                                                                                              [ 37%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_ciclo_parcial_no_devuelve_prefijo PASSED                                                                                                         [ 38%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_autoarista PASSED                                                                                                                                [ 40%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_desconectado_aciclico_y_aislado PASSED                                                                                                           [ 41%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_vecino_implicito_y_duplicado PASSED                                                                                                              [ 43%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_no_muta_entrada PASSED                                                                                                                           [ 44%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_orden_principal_y_alternativo PASSED                                                                                                        [ 46%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden0] PASSED                                                                                                    [ 47%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden1] PASSED                                                                                                    [ 49%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden2] PASSED                                                                                                    [ 50%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden3] PASSED                                                                                                    [ 52%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden4] PASSED                                                                                                    [ 53%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_grafo_ciclico_no_acepta_orden PASSED                                                                                                        [ 55%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_cero_y_uno PASSED                                                                                                                               [ 56%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_sin_prerrequisitos_incluye_todos PASSED                                                                                                         [ 58%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_cadena PASSED                                                                                                                                   [ 59%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_varias_dependencias_y_orden_no_unico PASSED                                                                                                     [ 61%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_ciclo_y_auto_dependencia PASSED                                                                                                                 [ 62%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_dependencia_duplicada_se_ignora PASSED                                                                                                          [ 64%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par0] PASSED                                                                                                          [ 65%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par1] PASSED                                                                                                          [ 67%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par2] PASSED                                                                                                          [ 68%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par3] PASSED                                                                                                          [ 70%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[True] PASSED                                                                                                  [ 71%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[2.0] PASSED                                                                                                   [ 73%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[2] PASSED                                                                                                     [ 74%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[None] PASSED                                                                                                  [ 76%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_negativa PASSED                                                                                                                [ 77%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par0] PASSED                                                                                                  [ 79%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par1] PASSED                                                                                                  [ 80%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par2] PASSED                                                                                                  [ 82%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par3] PASSED                                                                                                  [ 83%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par0] PASSED                                                                                                         [ 85%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par1] PASSED                                                                                                         [ 86%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par2] PASSED                                                                                                         [ 88%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par3] PASSED                                                                                                         [ 89%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_no_muta_y_funcion_complementaria_reutilizable PASSED                                                                                            [ 91%]
clase_19::test_1_varios_ordenes_validos PASSED                                                                                                                                                                      [ 92%]
clase_19::test_2_ciclo_simple PASSED                                                                                                                                                                                [ 94%]
clase_19::test_3_ciclo_parcial_en_una_parte_del_grafo PASSED                                                                                                                                                        [ 95%]
clase_19::test_4_vecino_implicito PASSED                                                                                                                                                                            [ 97%]
clase_19::test_5_dependencias_duplicadas PASSED                                                                                                                                                                     [ 98%]
clase_19::test_6_orden_incorrecto PASSED                                                                                                                                                                            [100%]

=================================================================================================== 67 passed in 0.10s ===================================================================================================
```

## Resumen

- cantidad total de pruebas: 67
- pruebas aprobadas: 67
- errores o fallos: 0
- prueba propia más importante: normalizar_grafo_dirigido
- contrato que protege: que no haya entradasd invalidas.

## Evidencias obligatorias
Pues ya está que sí jala.
### Ejemplo con varios órdenes
También jala.
es_orden_topologico
{"A": ["B", "C"], "B": [], "C": []}
Salida del algoritmo: ["A", "B", "C"]
### Ejemplo con ciclo
Grafo de entrada: {"A": ["B"], "B": ["C"], "C": ["A"]}
Salida del algoritmo: None
### Ejemplo con duplicados
Grafo de entrada: {"A": ["B", "B"], "B": []}
Procesamiento interno: La función de normalización filtra las adyacencias repetidas, transformándolo limpiamente en {"A": ["B"], "B": []}.
## Corrección después de un fallo

Describe el fallo, la causa, el cambio realizado y la prueba de regresión.

