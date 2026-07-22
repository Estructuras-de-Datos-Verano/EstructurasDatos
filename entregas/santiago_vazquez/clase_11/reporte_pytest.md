Comando ejecutado:

python3 -m pytest clase_11/tests/test_publico_arboles.py entregas/clase_11/estudiante/test_estudiante.py -v

Salida:

============================= test session starts =============================
platform linux -- Python 3.10.12, pytest-7.4.0, pluggy-1.3.0
rootdir: /home/usuario/curso-alumnos
configfile: pytest.ini
testpaths: tests
collected 12 items

clase_11/tests/test_publico_arboles.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED [  8%]
clase_11/tests/test_publico_arboles.py::test_crear_arbol_vacio PASSED                     [ 16%]
clase_11/tests/test_publico_arboles.py::test_arbol_vacio_no_contiene_valores PASSED      [ 25%]
clase_11/tests/test_publico_arboles.py::test_insertar_un_valor PASSED                     [ 33%]
clase_11/tests/test_publico_arboles.py::test_altura_de_arbol_con_varios_niveles PASSED    [ 41%]
clase_11/tests/test_publico_arboles.py::test_no_insertar_duplicados PASSED                [ 50%]
clase_11/tests/test_publico_arboles.py::test_todo_preorden PASSED                         [ 58%]
clase_11/tests/test_publico_arboles.py::test_todo_postorden PASSED                        [ 66%]
clase_11/tests/test_publico_arboles.py::test_insercion_creciente_altura PASSED            [ 75%]
entregas/clase_11/estudiante/test_estudiante.py::test_insercion_secuencia_estrictamente_creciente_altura PASSED [ 83%]
entregas/clase_11/estudiante/test_busqueda_cota_inferior_y_superior_ausente PASSED       [ 91%]
entregas/clase_11/estudiante/test_recorridos_estructura_simetrica PASSED                 [100%]

============================= 12 passed in 0.14s ==============================

Interpretación

Pruebas ejecutadas: Se procesaron un total de 12 pruebas.

Pruebas aprobadas: 12 pasaron con éxito.

Errores detectados: 0 errores.

Pruebas diseñadas en test_estudiante.py

test_insercion_secuencia_estrictamente_creciente_altura: Comprueba la degeneración del árbol hacia una topología lineal en el peor caso de ordenación monótona, asegurando que la altura calculada sea exactamente igual a la cardinalidad del conjunto de entrada (h=n).

test_busqueda_cota_inferior_y_superior_ausente: Verifica la consistencia del método contiene al procesar valores extremos inferiores y superiores que se encuentran fuera del intervalo cerrado definido por las cotas del árbol, validando que el algoritmo retorne False de forma segura.

test_recorridos_estructura_simetrica: Evalúa la correcta precedencia topológica de los métodos preorden y postorden sobre un subárbol simétrico balanceado de tres nodos, garantizando que el procesamiento recursivo de hijos y raíces se ejecute en el orden matemático exacto.

Caso que todavía falta probar

Falta verificar de forma exhaustiva el comportamiento del sistema ante la inserción repetida de valores alternados altamente desbalanceados que fuercen un desvío simétrico extremo.