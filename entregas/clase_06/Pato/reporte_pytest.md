# Clase 06: Reporte PYTEST
### Nombre: Patricio Navarro

### Comando utilizado: `pytest -v`

## Resultados:
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0261331\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0261331\Documents\GitHub\EstructurasDatos\clase_06
configfile: pytest.ini
testpaths: tests
collecting ... collected 9 items

tests/test_publico_josephus.py::test_validar_n_rechaza_cero PASSED       [ 11%]
tests/test_publico_josephus.py::test_formatear_salida SKIPPED (forma...) [ 22%]
tests/test_publico_josephus.py::test_caso_minimo PASSED                  [ 33%]
tests/test_publico_josephus.py::test_caso_dos_ninos PASSED               [ 44%]
tests/test_publico_josephus.py::test_ejemplo_oficial PASSED              [ 55%]
tests/test_publico_josephus.py::test_resultado_contiene_todos_los_ninos_una_vez PASSED [ 66%]
tests/test_publico_josephus.py::test_resolver_desde_texto_si_existe SKIPPED [ 77%]
tests/test_publico_josephus.py::test_caso_maximo PASSED                  [ 88%]
tests/test_publico_josephus.py::test_caso_grande PASSED                  [100%]

=========================== short test summary info ===========================
SKIPPED [1] tests\test_publico_josephus.py:35: formatear_salida solo existe en el c¾digo base de apoyo
SKIPPED [1] tests\test_publico_josephus.py:60: resolver_desde_texto solo existe en el c¾digo base de apoyo
======================== 7 passed, 2 skipped in 0.02s =========================

## Interpretación
La implementacón utilizada si cumple con los criterios mínimos que pide el problema, tanto en el orden en que deben salir los eliminados, así como que no admita que no haya niños o que se repitan. Además se salto dos casos ya que nosotros no usamos ni `formatear_salida()` ni `resolver_desde_texto()`.

### Número de pruebas: 9
### Pruebas pasadas: 7
### Pruebas saltadas: 2

## Pruebas que verifican:
1. Que haya niños.
2. Los casos para cuando hay un niño, dos niños, y el ejemplo oficial.
3. Que todos los niños solo estén contenidos una vez.
4. Un caso grande con n = 1000 y el caso maximo para n según la restricción del problema, se midió a través del tamaño de los eliminados en dichos casos asegurando que todos los niños estuvieran dentro de la lista.

### Prueba que falta: Para cuando se rebase el límite de niños.

