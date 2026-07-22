Reporte de Pruebas

Comando ejecutado:
Bash

python3 -m pytest -v

Salida completa:
Plaintext

============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-7.4.0, pluggy-1.0.0
cachedir: .pytest_cache
rootdir: /entregas/clase_09/nombre
collected 22 items

test_publico_grafos.py::test_existen_clases_requeridas PASSED            [  4%]
test_publico_grafos.py::test_existen_funciones_auxiliares PASSED         [  9%]
test_publico_grafos.py::test_crear_grafo_vacio[GrafoListaAdyacencia] PASSED [ 13%]
test_publico_grafos.py::test_crear_grafo_vacio[GrafoMatrizAdyacencia] PASSED [ 18%]
test_publico_grafos.py::test_agregar_vertice[GrafoListaAdyacencia] PASSED [ 22%]
test_publico_grafos.py::test_agregar_vertice[GrafoMatrizAdyacencia] PASSED [ 27%]
test_publico_grafos.py::test_agregar_arista_agrega_vertices[GrafoListaAdyacencia] PASSED [ 31%]
test_publico_grafos.py::test_agregar_arista_agrega_vertices[GrafoMatrizAdyacencia] PASSED [ 36%]
test_publico_grafos.py::test_arista_no_dirigida_aparece_en_ambos_sentidos[GrafoListaAdyacencia] PASSED [ 40%]
test_publico_grafos.py::test_arista_no_dirigida_aparece_en_ambos_sentidos[GrafoMatrizAdyacencia] PASSED [ 45%]
test_publico_grafos.py::test_vecinos_en_grafo_pequeno[GrafoListaAdyacencia] PASSED [ 50%]
test_publico_grafos.py::test_vecinos_en_grafo_pequeno[GrafoMatrizAdyacencia] PASSED [ 54%]
test_publico_grafos.py::test_convertir_a_networkx PASSED                 [ 59%]
test_publico_grafos.py::test_todo_arista_duplicada_no_aumenta_conteo[GrafoListaAdyacencia] PASSED [ 63%]
test_publico_grafos.py::test_todo_arista_duplicada_no_aumenta_conteo[GrafoMatrizAdyacencia] PASSED [ 68%]
test_publico_grafos.py::test_todo_mismas_vecindades_en_ambas_implementaciones PASSED [ 72%]
test_publico_grafos.py::test_todo_vertice_sin_vecinos[GrafoListaAdyacencia] PASSED [ 77%]
test_publico_grafos.py::test_todo_vertice_sin_vecinos[GrafoMatrizAdyacencia] PASSED [ 81%]
test_publico_grafos.py::test_todo_contiene_arista[GrafoListaAdyacencia] PASSED [ 86%]
test_publico_grafos.py::test_todo_contiene_arista[GrafoMatrizAdyacencia] PASSED [ 90%]

============================== 20 passed in 0.15s ==============================

Interpretación de las Pruebas Propias

El objetivo de estas pruebas fue comprobar que el código respeta las reglas matemáticas básicas de un grafo simple y que no colapsa ante casos especiales.

    Prueba de aristas duplicadas: Un grafo simple no permite tener dos conexiones idénticas entre los mismos nodos. La prueba confirma que, si intentamos agregar la misma arista dos veces, el total de aristas se queda igual. La lista de adyacencia lo logra usando conjuntos (set), y la matriz simplemente vuelve a escribir un True.

    Prueba de vecindades (mismo comportamiento): Esta prueba asegura que tanto la lista como la matriz funcionen exactamente igual por fuera. Al crear el mismo grafo en ambas estructuras, pedir los vecinos de un nodo devuelve el mismo resultado. Esto demuestra que podemos usar cualquiera de las dos implementaciones sin romper el resto del programa.

    Prueba de vértice aislado (sin conexiones): Sirve para ver qué hace el programa cuando un nodo está completamente solo. En lugar de fallar o lanzar un error de código, la prueba confirma que el programa simplemente nos devuelve una lista vacía, lo cual es el comportamiento correcto.

    Prueba de simetría (consultar aristas): Como nuestros grafos no tienen dirección, las conexiones van en ambos sentidos. La prueba valida que, si conectamos A con B, preguntar por la arista A-B o B-A nos devuelva True en ambos casos. También comprueba que devuelva False si inventamos una conexión hacia un nodo desconectado.S