## Reporte de pytest 

## Comando ejecutado

```bash
python evaluar.py entregas/clase_19/ivan clase_19/tests entregas/clase_19/ivan/test_estudiante.py
```

## Salida completa de `pytest -v`

```powershell

PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_19/ivan clase_19/tests entregas/clase_19/ivan/test_estudiante.py
>> 
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_19\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_19\ivan\test_estudiante.py

============================================================================= test session starts =============================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_19
configfile: pytest.ini
plugins: anyio-4.7.0
collected 133 items                                                                                                                                                            

clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_vacio PASSED                                                                                     [  0%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_copia_defensiva_y_no_comparte_listas PASSED                                                      [  1%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_vecino_implicito_y_aislado PASSED                                                                [  2%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_elimina_duplicados_establemente PASSED                                                           [  3%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_conserva_orden_de_primera_aparicion PASSED                                                       [  3%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[grafo0] PASSED                                                   [  4%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[AB] PASSED                                                       [  5%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[3] PASSED                                                        [  6%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_grafo_que_no_es_mapping[None] PASSED                                                     [  6%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_nodo_no_string PASSED                                                                    [  7%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_vecino_no_string PASSED                                                                  [  8%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[B] PASSED                                                            [  9%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[3] PASSED                                                            [  9%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[None] PASSED                                                         [ 10%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_rechaza_adyacencia_invalida[vecinos3] PASSED                                                     [ 11%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_normalizar_acepta_tuplas_y_no_muta PASSED                                                                   [ 12%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_vacio PASSED                                                                                         [ 12%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_cadena PASSED                                                                                        [ 13%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_varias_fuentes PASSED                                                                                [ 14%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_grados_vecino_implicito_duplicados_y_aislado PASSED                                                         [ 15%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_vacio PASSED                                                                                          [ 15%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_un_nodo PASSED                                                                                        [ 16%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_cadena PASSED                                                                                         [ 17%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_varias_fuentes_y_varios_ordenes PASSED                                                                [ 18%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_ciclo_simple PASSED                                                                                   [ 18%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_ciclo_parcial_no_devuelve_prefijo PASSED                                                              [ 19%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_autoarista PASSED                                                                                     [ 20%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_desconectado_aciclico_y_aislado PASSED                                                                [ 21%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_vecino_implicito_y_duplicado PASSED                                                                   [ 21%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_orden_no_muta_entrada PASSED                                                                                [ 22%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_orden_principal_y_alternativo PASSED                                                             [ 23%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden0] PASSED                                                         [ 24%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden1] PASSED                                                         [ 24%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden2] PASSED                                                         [ 25%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden3] PASSED                                                         [ 26%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_rechaza_ordenes_invalidos[orden4] PASSED                                                         [ 27%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_validacion_grafo_ciclico_no_acepta_orden PASSED                                                             [ 27%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_cero_y_uno PASSED                                                                                    [ 28%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_sin_prerrequisitos_incluye_todos PASSED                                                              [ 29%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_cadena PASSED                                                                                        [ 30%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_varias_dependencias_y_orden_no_unico PASSED                                                          [ 30%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_ciclo_y_auto_dependencia PASSED                                                                      [ 31%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_dependencia_duplicada_se_ignora PASSED                                                               [ 32%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par0] PASSED                                                               [ 33%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par1] PASSED                                                               [ 33%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par2] PASSED                                                               [ 34%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_indices_invalidos[par3] PASSED                                                               [ 35%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[True] PASSED                                                       [ 36%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[2.0] PASSED                                                        [ 36%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[2] PASSED                                                          [ 37%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_de_tipo_invalido[None] PASSED                                                       [ 38%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_cantidad_negativa PASSED                                                                     [ 39%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par0] PASSED                                                       [ 39%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par1] PASSED                                                       [ 40%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par2] PASSED                                                       [ 41%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_extremos_de_tipo_invalido[par3] PASSED                                                       [ 42%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par0] PASSED                                                              [ 42%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par1] PASSED                                                              [ 43%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par2] PASSED                                                              [ 44%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_rechaza_pares_mal_formados[par3] PASSED                                                              [ 45%]
clase_19\tests\test_publico_ordenamiento_topologico.py::test_cursos_no_muta_y_funcion_complementaria_reutilizable PASSED                                                 [ 45%]
clase_19::test_normalizar_vacio PASSED                                                                                                                                   [ 46%]
clase_19::test_normalizar_copia_defensiva_y_no_comparte_listas PASSED                                                                                                    [ 47%]
clase_19::test_normalizar_vecino_implicito_y_aislado PASSED                                                                                                              [ 48%]
clase_19::test_normalizar_elimina_duplicados_establemente PASSED                                                                                                         [ 48%]
clase_19::test_normalizar_conserva_orden_de_primera_aparicion PASSED                                                                                                     [ 49%]
clase_19::test_normalizar_rechaza_grafo_que_no_es_mapping[grafo0] PASSED                                                                                                 [ 50%]
clase_19::test_normalizar_rechaza_grafo_que_no_es_mapping[AB] PASSED                                                                                                     [ 51%]
clase_19::test_normalizar_rechaza_grafo_que_no_es_mapping[3] PASSED                                                                                                      [ 51%]
clase_19::test_normalizar_rechaza_grafo_que_no_es_mapping[None] PASSED                                                                                                   [ 52%]
clase_19::test_normalizar_rechaza_nodo_no_string PASSED                                                                                                                  [ 53%]
clase_19::test_normalizar_rechaza_vecino_no_string PASSED                                                                                                                [ 54%]
clase_19::test_normalizar_rechaza_adyacencia_invalida[B] PASSED                                                                                                          [ 54%]
clase_19::test_normalizar_rechaza_adyacencia_invalida[3] PASSED                                                                                                          [ 55%]
clase_19::test_normalizar_rechaza_adyacencia_invalida[None] PASSED                                                                                                       [ 56%]
clase_19::test_normalizar_rechaza_adyacencia_invalida[vecinos3] PASSED                                                                                                   [ 57%]
clase_19::test_normalizar_acepta_tuplas_y_no_muta PASSED                                                                                                                 [ 57%]
clase_19::test_grados_vacio PASSED                                                                                                                                       [ 58%]
clase_19::test_grados_cadena PASSED                                                                                                                                      [ 59%]
clase_19::test_grados_varias_fuentes PASSED                                                                                                                              [ 60%]
clase_19::test_grados_vecino_implicito_duplicados_y_aislado PASSED                                                                                                       [ 60%]
clase_19::test_orden_vacio PASSED                                                                                                                                        [ 61%]
clase_19::test_orden_un_nodo PASSED                                                                                                                                      [ 62%]
clase_19::test_orden_cadena PASSED                                                                                                                                       [ 63%]
clase_19::test_orden_varias_fuentes_y_varios_ordenes PASSED                                                                                                              [ 63%]
clase_19::test_orden_ciclo_simple PASSED                                                                                                                                 [ 64%]
clase_19::test_orden_ciclo_parcial_no_devuelve_prefijo PASSED                                                                                                            [ 65%]
clase_19::test_orden_autoarista PASSED                                                                                                                                   [ 66%]
clase_19::test_orden_desconectado_aciclico_y_aislado PASSED                                                                                                              [ 66%]
clase_19::test_orden_vecino_implicito_y_duplicado PASSED                                                                                                                 [ 67%]
clase_19::test_orden_no_muta_entrada PASSED                                                                                                                              [ 68%]
clase_19::test_validacion_orden_principal_y_alternativo PASSED                                                                                                           [ 69%]
clase_19::test_validacion_rechaza_ordenes_invalidos[orden0] PASSED                                                                                                       [ 69%]
clase_19::test_validacion_rechaza_ordenes_invalidos[orden1] PASSED                                                                                                       [ 70%]
clase_19::test_validacion_rechaza_ordenes_invalidos[orden2] PASSED                                                                                                       [ 71%]
clase_19::test_validacion_rechaza_ordenes_invalidos[orden3] PASSED                                                                                                       [ 72%]
clase_19::test_validacion_rechaza_ordenes_invalidos[orden4] PASSED                                                                                                       [ 72%]
clase_19::test_validacion_grafo_ciclico_no_acepta_orden PASSED                                                                                                           [ 73%]
clase_19::test_cursos_cero_y_uno PASSED                                                                                                                                  [ 74%]
clase_19::test_cursos_sin_prerrequisitos_incluye_todos PASSED                                                                                                            [ 75%]
clase_19::test_cursos_cadena PASSED                                                                                                                                      [ 75%]
clase_19::test_cursos_varias_dependencias_y_orden_no_unico PASSED                                                                                                        [ 76%]
clase_19::test_cursos_ciclo_y_auto_dependencia PASSED                                                                                                                    [ 77%]
clase_19::test_cursos_dependencia_duplicada_se_ignora PASSED                                                                                                             [ 78%]
clase_19::test_cursos_rechaza_indices_invalidos[par0] PASSED                                                                                                             [ 78%]
clase_19::test_cursos_rechaza_indices_invalidos[par1] PASSED                                                                                                             [ 79%]
clase_19::test_cursos_rechaza_indices_invalidos[par2] PASSED                                                                                                             [ 80%]
clase_19::test_cursos_rechaza_indices_invalidos[par3] PASSED                                                                                                             [ 81%]
clase_19::test_cursos_rechaza_cantidad_de_tipo_invalido[True] PASSED                                                                                                     [ 81%]
clase_19::test_cursos_rechaza_cantidad_de_tipo_invalido[2.0] PASSED                                                                                                      [ 82%]
clase_19::test_cursos_rechaza_cantidad_de_tipo_invalido[2] PASSED                                                                                                        [ 83%]
clase_19::test_cursos_rechaza_cantidad_de_tipo_invalido[None] PASSED                                                                                                     [ 84%]
clase_19::test_cursos_rechaza_cantidad_negativa PASSED                                                                                                                   [ 84%]
clase_19::test_cursos_rechaza_extremos_de_tipo_invalido[par0] PASSED                                                                                                     [ 85%]
clase_19::test_cursos_rechaza_extremos_de_tipo_invalido[par1] PASSED                                                                                                     [ 86%]
clase_19::test_cursos_rechaza_extremos_de_tipo_invalido[par2] PASSED                                                                                                     [ 87%]
clase_19::test_cursos_rechaza_extremos_de_tipo_invalido[par3] PASSED                                                                                                     [ 87%]
clase_19::test_cursos_rechaza_pares_mal_formados[par0] PASSED                                                                                                            [ 88%]
clase_19::test_cursos_rechaza_pares_mal_formados[par1] PASSED                                                                                                            [ 89%]
clase_19::test_cursos_rechaza_pares_mal_formados[par2] PASSED                                                                                                            [ 90%]
clase_19::test_cursos_rechaza_pares_mal_formados[par3] PASSED                                                                                                            [ 90%]
clase_19::test_cursos_no_muta_y_funcion_complementaria_reutilizable PASSED                                                                                               [ 91%]
clase_19::test_propio_varios_ordenes_validos PASSED                                                                                                                      [ 92%]
clase_19::test_propio_ciclo_simple PASSED                                                                                                                                [ 93%]
clase_19::test_propio_ciclo_parcial PASSED                                                                                                                               [ 93%]
clase_19::test_propio_vecino_implicito PASSED                                                                                                                            [ 94%]
clase_19::test_propio_dependencias_duplicadas PASSED                                                                                                                     [ 95%]
clase_19::test_propio_orden_incorrecto PASSED                                                                                                                            [ 96%]
clase_19::test_propio_no_mutacion[grafo_entrada0-estado_esperado0] PASSED                                                                                                [ 96%]
clase_19::test_propio_no_mutacion[grafo_entrada1-estado_esperado1] PASSED                                                                                                [ 97%]
clase_19::test_propio_no_mutacion[grafo_entrada2-estado_esperado2] PASSED                                                                                                [ 98%]
clase_19::test_propio_autoarista PASSED                                                                                                                                  [ 99%]
clase_19::test_propio_indice_valido PASSED                                                                                                                               [100%]

============================================================================= 133 passed in 0.43s =============================================================================

```

## Resumen

#### - Cantidad de pruebas:
133
#### - Pruebas aprobadas:
133
#### - Errores o fallos:
No

## Evidencia técnica

#### - Prueba propia más importante:
`test_propio_dependencias_duplicadas`

#### - Invariante protegido:
Garantiza que cada reducción numérica en el registro de dependencias represente estrictamente una única arista satisfecha, impidiendo que un nodo se quede bloqueado de forma indefinida o que su grado de entrada adquiera un valor negativo.

#### - Ejemplo de unión redundante:
Declarar dos veces seguidas la relación `(0, 1)` dentro de la lista de prerrequisitos en `ordenar_cursos`, o ingresar la estructura `{"A": ["B", "B"]}`.

#### - Ejemplo de arista rechazada:
La segunda aparición de la arista dirigida `A → B` durante la etapa de normalización, la cual es descartada por el algoritmo para evitar un aumento artificial en el conteo de restricciones del nodo destino.

#### - Resultado de un grafo desconectado:
Si el grafo completo carece de ciclos, devuelve una secuencia lineal válida que integra exitosamente a todos los nodos de las componentes aisladas; si existe un ciclo en cualquier componente, el resultado total será `None`.


## Corrección después de un fallo

#### Describe el comportamiento inicial, el contrato roto, la corrección localizada y el resultado posterior.

**Comportamiento inicial:** 
El algoritmo incrementaba el grado de entrada de un nodo destino múltiples veces si una misma relación de dependencia aparecía repetida en los datos de entrada. Al procesar el nodo origen, el contador del vecino se reducía pero jamás alcanzaba el cero, provocando un bloqueo indefinido (un ciclo fantasma) que causaba que la función fallara devolviendo `None`.

**Contrato roto:** 
Se violaba la invariante fundamental de la cola de disponibles, la cual exige de forma estricta que un elemento ingrese a la estructura de procesamiento únicamente cuando su grado de entrada real sea exactamente igual a cero (es decir, cuando todos sus prerrequisitos únicos e individuales se hayan resuelto por completo).

**Corrección localizada:** 
Se implementó un filtro de unicidad dentro de la etapa de `normalizar_grafo_dirigido`. Antes de insertar un elemento en la secuencia de sucesores de una clave, se incorporó una comprobación condicional explícita (`if sucesor not in normalizado[nodo]:`) para descartar aristas redundantes.

**Resultado posterior:** 
El diccionario generado por `grados_entrada` ahora mapea el número real de restricciones del grafo. La prueba `test_propio_dependencias_duplicadas` se ejecuta con éxito, permitiendo que las entradas con uniones duplicadas se resuelvan en un orden lineal correcto sin alterar la longitud final de la secuencia ni generar bloqueos.