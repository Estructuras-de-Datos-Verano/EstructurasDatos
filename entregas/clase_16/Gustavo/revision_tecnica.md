# Revisión hecha por Leo

Contrato: se prometieron 5 pruebas y solo fueron 3
Entrada: eran 5 mínimas
Observado: solo fueron 3
Impacto: importa porque no verifica al 100% lo que se debía 
Acción: debió implementarlo
Verificación: así se verificará que todo esté 100% en orden 

Contrato: se prometieron 6 documentos 
Entrada: eran 6
Observado: fueron 5
Impacto: importa porque no es lo que se pidió
Acción: debió agregar el sexto documento
Verificación: así estará tod lo que se solicitó



## una fortaleza específica
Toda la implementación está perfecta

## un contrato incumplido o caso no cubierto
se prometieron 5 pruebas y solo fueron 3

## entrada reproducible
Sí

## test ejecutado
Ejecutando:
C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe -m pytest -v C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_16\tests C:\Users\0254049\Documents\GitHub\EstructurasDatos\entregas\clase_16\LEO\test_estudiante.py

============================================= test session starts ==============================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0254049\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0254049\Documents\GitHub\EstructurasDatos\clase_16
configfile: pytest.ini
collected 27 items                                                                                              

clase_16\tests\test_publico_dijkstra_robusto.py::test_calcula_distancias_y_predecesores_conocidos PASSED  [  3%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_no_muta_listas_de_adyacencia PASSED                 [  7%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_incluye_vecino_que_no_es_clave PASSED               [ 11%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-1] PASSED                    [ 14%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_negativo[-0.5] PASSED                  [ 18%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[inf] PASSED                  [ 22%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[-inf] PASSED                 [ 25%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_finito[nan] PASSED                  [ 29%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[True] PASSED               [ 33%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[3] PASSED                  [ 37%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_peso_no_numerico[None] PASSED               [ 40%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_arista_con_forma_incorrecta PASSED          [ 44%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_rechaza_origen_inexistente PASSED                   [ 48%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_destino_inalcanzable_conserva_infinito_y_camino_vacio PASSED [ 51%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_origen_igual_a_destino PASSED                       [ 55%]
clase_16\tests\test_publico_dijkstra_robusto.py::test_reconstruccion_rechaza_ciclo PASSED                 [ 59%]
clase_16::test_grafo_debe_ser_mapping_LEO <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED           [ 62%]
clase_16::test_nombres_de_nodos_y_vecinos_deben_ser_str_LEO[grafo0] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED [ 66%]
clase_16::test_nombres_de_nodos_y_vecinos_deben_ser_str_LEO[grafo1] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED [ 70%]
clase_16::test_entrada_obsoleta_LEO <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED                 [ 74%]
clase_16::test_bool_no_se_acepta_como_peso_LEO[True] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED [ 77%]
clase_16::test_bool_no_se_acepta_como_peso_LEO[False] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED [ 81%]
clase_16::test_vecino_implicito_y_no_mutacion_LEO <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED   [ 85%]
clase_16::test_pesos_no_finitos_LEO[nan] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED            [ 88%]
clase_16::test_pesos_no_finitos_LEO[inf] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED            [ 92%]
clase_16::test_pesos_no_finitos_LEO[-inf] <- ..\entregas\clase_16\LEO\test_estudiante.py PASSED           [ 96%]
clase_16::test_ciclo_de_predecesores_LEO <- ..\entregas\clase_16\LEO\test_estudiante.py FAILED            [100%]

=================================================== FAILURES ===================================================
________________________________________ test_ciclo_de_predecesores_LEO ________________________________________

    def test_ciclo_de_predecesores_LEO():
        """
        Verifica que reconstruir_camino detecte un ciclo
        en el diccionario de predecesores.
        """
        predecesores = {"A": "B", "B": "A"}
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

entregas\clase_16\LEO\test_estudiante.py:70: Failed
=========================================== short test summary info ============================================
FAILED clase_16::test_ciclo_de_predecesores_LEO - Failed: DID NOT RAISE ValueError
========================================= 1 failed, 26 passed in 0.09s =========================================


NO pasó el test del ciclo, no se detectó el error

## recomendación localizada
Debería prestar mas atención a lo que indica el documento practica_16.md

# #respuesta del autor
