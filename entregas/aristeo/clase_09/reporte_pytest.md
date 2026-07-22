# reporte_pytest

### Comando ejecutado:

```
cd clase_09
py -m pytest tests/test_publico_grafos.py -vv
```

### Salida completa:
```
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_09
configfile: pytest.ini
collected 20 items                                                             

tests/test_publico_grafos.py::test_existen_clases_requeridas PASSED      [  5%]
tests/test_publico_grafos.py::test_existen_funciones_auxiliares PASSED   [ 10%]
tests/test_publico_grafos.py::test_crear_grafo_vacio[GrafoListaAdyacencia] PASSED [ 15%]
tests/test_publico_grafos.py::test_crear_grafo_vacio[GrafoMatrizAdyacencia] PASSED [ 20%]
tests/test_publico_grafos.py::test_agregar_vertice[GrafoListaAdyacencia] PASSED [ 25%]
tests/test_publico_grafos.py::test_agregar_vertice[GrafoMatrizAdyacencia] PASSED [ 30%]
tests/test_publico_grafos.py::test_agregar_arista_agrega_vertices[GrafoListaAdyacencia] PASSED [ 35%]
tests/test_publico_grafos.py::test_agregar_arista_agrega_vertices[GrafoMatrizAdyacencia] PASSED [ 40%]
tests/test_publico_grafos.py::test_arista_no_dirigida_aparece_en_ambos_sentidos[GrafoListaAdyacencia] PASSED [ 45%]
tests/test_publico_grafos.py::test_arista_no_dirigida_aparece_en_ambos_sentidos[GrafoMatrizAdyacencia] PASSED [ 50%]
tests/test_publico_grafos.py::test_vecinos_en_grafo_pequeno[GrafoListaAdyacencia] PASSED [ 55%]
tests/test_publico_grafos.py::test_vecinos_en_grafo_pequeno[GrafoMatrizAdyacencia] PASSED [ 60%]
tests/test_publico_grafos.py::test_convertir_a_networkx PASSED           [ 65%]
tests/test_publico_grafos.py::test_todo_arista_duplicada_no_aumenta_conteo[GrafoListaAdyacencia] PASSED [ 70%]
tests/test_publico_grafos.py::test_todo_arista_duplicada_no_aumenta_conteo[GrafoMatrizAdyacencia] PASSED [ 75%]
tests/test_publico_grafos.py::test_todo_mismas_vecindades_en_ambas_implementaciones PASSED [ 80%]
tests/test_publico_grafos.py::test_todo_vertice_sin_vecinos[GrafoListaAdyacencia] PASSED [ 85%]
tests/test_publico_grafos.py::test_todo_vertice_sin_vecinos[GrafoMatrizAdyacencia] PASSED [ 90%]
tests/test_publico_grafos.py::test_todo_contiene_arista[GrafoListaAdyacencia] PASSED [ 95%]
tests/test_publico_grafos.py::test_todo_contiene_arista[GrafoMatrizAdyacencia] PASSED [100%]

============================= 20 passed in 0.14s ==============================
```
### Interpretación:

Valida las operaciones básicas de un grafo, la ejecución muestra que todas las pruebas definidas pasan, lo que indica que la implementación satisface los requisitos básicos: creación y conteo de vértices/aristas, adición de aristas (con creación implícita de vértices), vecindades correctas, detección de aristas, conversión a NetworkX y manejo de aristas duplicadas.

### Cuántas pruebas se ejecutaron:
20 pruebas
### Cuántas pasaron:
20 pruebas
### Si hubo errores:
no (0 errores)

### Qué comportamiento verifican:

- Existencia de las clases y funciones públicas esperadas.
- Creación de grafos vacíos sin vértices ni aristas.
- Agregar vértices y aristas produce los efectos esperados.
- Aristas no dirigidas aparecen en ambos vértices.
- `vecinos()` devuelve las vecindades esperadas.
- `cantidad_vertices()` y `cantidad_aristas()` reflejan la estructura.
- `convertir_a_networkx()` construye un `nx.Graph` equivalente.
- Agregar la misma arista repetidas veces no incrementa el conteo.
- Ambas implementaciones (`GrafoListaAdyacencia` y `GrafoMatrizAdyacencia`) producen las mismas vecindades para el grafo de prueba.

### Qué prueba diseñaste tú:

- `test_todo_arista_duplicada_no_aumenta_conteo`
- `test_todo_mismas_vecindades_en_ambas_implementaciones`
- `test_todo_vertice_sin_vecinos`
- `test_todo_contiene_arista`

Esas pruebas verifican comportamiento público adicional: manejo de
duplicados, paridad entre implementaciones, existencia de vértices
aislados y verificación de `contiene_arista()`.

### Qué caso todavía falta probar:

- Eliminación de vértices y aristas (operaciones de borrado no están cubiertas).
- Lazos (aristas `A`--`A`) y su tratamiento por las implementaciones.
- Casos de entrada inválida (vértices no-string, cadenas vacías).
- Rendimiento y memoria con grafos grandes (escala).
- Comportamiento con grafos dirigidos o ponderados (extensiones).