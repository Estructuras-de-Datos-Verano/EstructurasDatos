# Reporte de pytest — Clase 17

## Comando ejecutado
**Aclaración:** Le cambié la etiqueta de text para que se vea bien y sea legible
```bash
    python evaluar.py entregas/clase_17/ivan clase_17/tests entregas/clase_17/ivan/test_estudiante.py
```

## Salida completa de `pytest -v`

```powershell
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_17/ivan clase_17/tests entregas/clase_17/ivan/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_17\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_17\ivan\test_estudiante.py

============================================================================ test session starts =============================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_17
configfile: pytest.ini
plugins: anyio-4.7.0
collected 76 items                                                                                                                                                            

clase_17\tests\test_publico_estructuras_bfs.py::test_exporta_los_dos_tipos_de_nodo PASSED                                                                               [  1%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_comienza_vacia_y_admite_valores_repetidos PASSED                                                              [  2%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_respeta_fifo_y_tamano PASSED                                                                                  [  3%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_vacia_falla_y_puede_reutilizarse PASSED                                                                       [  5%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cola_restaurada_no_conserva_extremos PASSED                                                                        [  6%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_opera_por_ambos_extremos PASSED                                                                              [  7%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_comienza_vacia_y_admite_valores_repetidos PASSED                                                             [  9%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_vacia_falla_y_puede_reutilizarse PASSED                                                                      [ 10%]
clase_17\tests\test_publico_estructuras_bfs.py::test_deque_desconecta_nodos_retirados PASSED                                                                            [ 11%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_conserva_orden_de_vecinos_y_camino_minimo PASSED                                                               [ 13%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_identidad_camino_directo_y_direccion PASSED                                                                    [ 14%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none PASSED                                                         [ 15%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_incluye_vecino_implicito_y_no_muta_entrada PASSED                                                              [ 17%]
clase_17\tests\test_publico_estructuras_bfs.py::test_bfs_rechaza_origen_o_destino_ausentes PASSED                                                                       [ 18%]
clase_17\tests\test_publico_estructuras_bfs.py::test_reconstruir_cubre_identidad_inalcanzable_y_ciclo PASSED                                                            [ 19%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_bfs_calcula_distancias_y_predecesores PASSED                                                              [ 21%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_prefiere_mas_aristas_si_cuestan_menos PASSED                                                              [ 22%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_con_solo_pesos_cero PASSED                                                                                [ 23%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_con_solo_pesos_uno PASSED                                                                                 [ 25%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_actualiza_una_mejora_posterior PASSED                                                                     [ 26%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_identidad_e_inalcanzable PASSED                                                                           [ 27%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_incluye_vecino_implicito_y_no_muta_entrada PASSED                                                         [ 28%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[True] PASSED                                                              [ 30%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[False] PASSED                                                             [ 31%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[0.0] PASSED                                                               [ 32%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[1] PASSED                                                                 [ 34%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_peso_de_tipo_incorrecto[None] PASSED                                                              [ 35%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_entero_fuera_del_dominio[-1] PASSED                                                               [ 36%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_entero_fuera_del_dominio[2] PASSED                                                                [ 38%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_entero_fuera_del_dominio[8] PASSED                                                                [ 39%]
clase_17\tests\test_publico_estructuras_bfs.py::test_cero_uno_rechaza_forma_y_nodos_invalidos PASSED                                                                    [ 40%]
clase_17\tests\test_publico_estructuras_bfs.py::test_constante_infinito_es_compatible_con_contrato PASSED                                                               [ 42%]
clase_17::test_exporta_los_dos_tipos_de_nodo PASSED                                                                                                                     [ 43%]
clase_17::test_cola_comienza_vacia_y_admite_valores_repetidos PASSED                                                                                                    [ 44%]
clase_17::test_cola_respeta_fifo_y_tamano PASSED                                                                                                                        [ 46%]
clase_17::test_cola_vacia_falla_y_puede_reutilizarse PASSED                                                                                                             [ 47%]
clase_17::test_cola_restaurada_no_conserva_extremos PASSED                                                                                                              [ 48%]
clase_17::test_deque_opera_por_ambos_extremos PASSED                                                                                                                    [ 50%]
clase_17::test_deque_comienza_vacia_y_admite_valores_repetidos PASSED                                                                                                   [ 51%]
clase_17::test_deque_vacia_falla_y_puede_reutilizarse PASSED                                                                                                            [ 52%]
clase_17::test_deque_desconecta_nodos_retirados PASSED                                                                                                                  [ 53%]
clase_17::test_bfs_conserva_orden_de_vecinos_y_camino_minimo PASSED                                                                                                     [ 55%]
clase_17::test_bfs_identidad_camino_directo_y_direccion PASSED                                                                                                          [ 56%]
clase_17::test_bfs_termina_en_un_ciclo_y_deja_inalcanzable_en_none PASSED                                                                                               [ 57%]
clase_17::test_bfs_incluye_vecino_implicito_y_no_muta_entrada PASSED                                                                                                    [ 59%]
clase_17::test_bfs_rechaza_origen_o_destino_ausentes PASSED                                                                                                             [ 60%]
clase_17::test_reconstruir_cubre_identidad_inalcanzable_y_ciclo PASSED                                                                                                  [ 61%]
clase_17::test_cero_uno_bfs_calcula_distancias_y_predecesores PASSED                                                                                                    [ 63%]
clase_17::test_cero_uno_prefiere_mas_aristas_si_cuestan_menos PASSED                                                                                                    [ 64%]
clase_17::test_cero_uno_con_solo_pesos_cero PASSED                                                                                                                      [ 65%]
clase_17::test_cero_uno_con_solo_pesos_uno PASSED                                                                                                                       [ 67%]
clase_17::test_cero_uno_actualiza_una_mejora_posterior PASSED                                                                                                           [ 68%]
clase_17::test_cero_uno_identidad_e_inalcanzable PASSED                                                                                                                 [ 69%]
clase_17::test_cero_uno_incluye_vecino_implicito_y_no_muta_entrada PASSED                                                                                               [ 71%]
clase_17::test_cero_uno_rechaza_peso_de_tipo_incorrecto[True] PASSED                                                                                                    [ 72%]
clase_17::test_cero_uno_rechaza_peso_de_tipo_incorrecto[False] PASSED                                                                                                   [ 73%]
clase_17::test_cero_uno_rechaza_peso_de_tipo_incorrecto[0.0] PASSED                                                                                                     [ 75%]
clase_17::test_cero_uno_rechaza_peso_de_tipo_incorrecto[1] PASSED                                                                                                       [ 76%]
clase_17::test_cero_uno_rechaza_peso_de_tipo_incorrecto[None] PASSED                                                                                                    [ 77%]
clase_17::test_cero_uno_rechaza_entero_fuera_del_dominio[-1] PASSED                                                                                                     [ 78%]
clase_17::test_cero_uno_rechaza_entero_fuera_del_dominio[2] PASSED                                                                                                      [ 80%]
clase_17::test_cero_uno_rechaza_entero_fuera_del_dominio[8] PASSED                                                                                                      [ 81%]
clase_17::test_cero_uno_rechaza_forma_y_nodos_invalidos PASSED                                                                                                          [ 82%]
clase_17::test_constante_infinito_es_compatible_con_contrato PASSED                                                                                                     [ 84%]
clase_17::test_1_cola_ligada_fifo PASSED                                                                                                                                [ 85%]
clase_17::test_2_cola_ligada_reutilizacion_despues_de_vaciarla PASSED                                                                                                   [ 86%]
clase_17::test_3_deque_ligada_operaciones_combinadas PASSED                                                                                                             [ 88%]
clase_17::test_4_deque_ligada_reutilizacion_despues_de_vaciarla PASSED                                                                                                  [ 89%]
clase_17::test_5_bfs_con_ciclo PASSED                                                                                                                                   [ 90%]
clase_17::test_6_bfs_con_destino_inalcanzable PASSED                                                                                                                    [ 92%]
clase_17::test_7_cero_uno_bfs_con_ruta_de_mas_aristas_pero_menor_costo PASSED                                                                                           [ 93%]
clase_17::test_8_cero_uno_bfs_con_peso_invalido PASSED                                                                                                                  [ 94%]
clase_17::test_9_origen_igual_destino PASSED                                                                                                                            [ 96%]
clase_17::test_10_vecino_implicito_en_nodos_sumidero PASSED                                                                                                             [ 97%]
clase_17::test_11_no_mutacion_del_grafo_usuario PASSED                                                                                                                  [ 98%]
clase_17::test_12_mejora_posterior_de_caminos_ya_descubiertos PASSED                                                                                                    [100%]

============================================================================= 76 passed in 0.37s =============================================================================
```

## Resumen cuantitativo

- Cantidad total de pruebas: 76
- Pruebas aprobadas: 76
- Errores o fallos: Ninguno.

## Evidencia técnica

- Prueba propia más importante: test_7_cero_uno_bfs_con_ruta_de_mas_aristas_pero_menor_costo()
- Invariante que protegió: La regla de priorizar rutas de menor peso.
- Fallo de referencias encontrado: No entiendo que quiere decir eso. Si se refiere a las referencias a algún nodo, no hubo ningún fallo, porque las funciones como desencolar se encargan de dejar como 'None' a cualquier antecesor/sucesor de un nodo borrado.
- Caso de BFS que resultó más informativo: Todo lo que falló en algún momento respecto a BFS fue por el mismo error de validar antes de tener variable, así que ninguno.
- Caso de 0-1 BFS que resultó más informativo: El de el siguiente grafo. 
```python
grafo = {
        "A": [("B", 1), ("C", 0)],
        "C": [("D", 0)],
        "D": [("B", 0)],
        "B": []
    }
```

## Comparación antes y después

Describe el fallo inicial, la corrección localizada y el resultado de volver a ejecutar públicas y propias.
Tuve muchos en intentos anteriores por dos cosas: 
1. Los regex esperados por las pruebas públicas no coincidían con mis raises (esto creo que es un error de diseño de esas pruebas la verdad, debió haber venido en las instrucciones que teníamos que escribir ciertas palabras en los raise)
2. Errores de validación en mis implementación. No aparecían y había errores con casos límite, o los agregué en lugares incorrectos y asigné accesos a variables/comparaciones cuando aún no existían esos datos. 