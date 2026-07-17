# Reporte pytest

Comando ejecutado:
```bash
pytest -v
```

Salida completa:
```text
============================= test session starts ==============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0282193\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0282193\Documents\GitHub\EstructurasDatos\clase_09
configfile: pytest.ini
testpaths: tests
collected 20 items

tests/test_publico_grafos.py::test_existen_clases_requeridas PASSED
tests/test_publico_grafos.py::test_existen_funciones_auxiliares PASSED
tests/test_publico_grafos.py::test_crear_grafo_vacio[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_crear_grafo_vacio[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_agregar_vertice[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_agregar_vertice[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_agregar_arista_agrega_vertices[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_agregar_arista_agrega_vertices[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_arista_no_dirigida_aparece_en_ambos_sentidos[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_arista_no_dirigida_aparece_en_ambos_sentidos[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_vecinos_en_grafo_pequeno[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_vecinos_en_grafo_pequeno[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_convertir_a_networkx PASSED
tests/test_publico_grafos.py::test_arista_duplicada_no_aumenta_conteo[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_arista_duplicada_no_aumenta_conteo[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_mismas_vecindades_en_ambas_implementaciones PASSED
tests/test_publico_grafos.py::test_vertice_sin_vecinos[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_vertice_sin_vecinos[GrafoMatrizAdyacencia] PASSED
tests/test_publico_grafos.py::test_contiene_arista[GrafoListaAdyacencia] PASSED
tests/test_publico_grafos.py::test_contiene_arista[GrafoMatrizAdyacencia] PASSED
```

Interpretación:
- Al inicio las pruebas salieron mal porque la implementación aún tenía stubs y mostraba `NotImplementedError`.
- También se detectó que pytest estaba importando una versión incompleta del módulo, por lo que fue necesario dejar la implementación completa en ambos archivos usados por las pruebas.
- Después de completar las operaciones del grafo y corregir la ruta de importación, todas las pruebas quedaron correctas.

Resumen:
- Pruebas ejecutadas: 20
- Pruebas pasaron: 20
- Errores: ninguno

Lo que verifican estas pruebas:
- Que los grafos puedan crearse vacíos.
- Que se agreguen vértices y aristas correctamente.
- Que las aristas no dirigidas funcionen en ambos sentidos.
- Que vecinos, contención de aristas y conteo de aristas sean correctos.
- Que la conversión a NetworkX funcione.

Prueba diseñada:
- Se agregó una prueba para verificar que agregar una arista duplicada no incremente el número de aristas y que las dos implementaciones mantengan las mismas vecindades.

Caso que todavía falta probar:
- Un grafo con múltiples componentes desconectados o con pesos y dirección, para validar comportamientos más complejos.
