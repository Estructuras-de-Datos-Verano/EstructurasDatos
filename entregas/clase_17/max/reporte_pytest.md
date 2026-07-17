# Reporte de pytest — Clase 17

## Comando ejecutado

```text
pytest -v

```

## Salida completa de `pytest -v`

```text

============================= test session starts =============================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.0.0
rootdir: C:\Users\Alumno\Documents\GitHub\EstructurasDatos\clase_17
collected 8 items

tests/test_publico_bfs.py::test_cola_vacia PASSED [ 12%]
tests/test_publico_bfs.py::test_cola_se_reutiliza_despues_de_vaciarse PASSED [ 25%]
tests/test_publico_bfs.py::test_bfs_camino_basico PASSED [ 37%]
tests/test_publico_bfs.py::test_bfs_inalcanzable PASSED  [ 50%]
tests/test_publico_01bfs.py::test_deque_extremos PASSED [ 62%]
tests/test_publico_01bfs.py::test_01bfs_mejor_camino PASSED [ 75%]
tests/test_publico_01bfs.py::test_validacion_tipos_peso PASSED [ 87%]
tests/test_publico_01bfs.py::test_ciclo_ValueError PASSED [100%]

============================== 8 passed in 0.03s ==============================

```

## Resumen cuantitativo

- Cantidad total de pruebas: 8
- Pruebas aprobadas: 8
- Errores o fallos:0

## Evidencia técnica

- Prueba propia más importante:
- Invariante que protegió: Que tanto el frente como el final se seteen a None cuando retiras el ultimo nodo de la ColaLigada.
- Fallo de referencias encontrado: Al principio no estaba limpiando el retirado.siguiente = None, entonces jalaba basura de otras pruebas.
- Caso de BFS que resultó más informativo: El de buscar un destino que no tiene conexiones (inalcanzable), porque me obligo a retornar [] limpio.
- Caso de 0-1 BFS que resultó más informativo: En donde hay una arista directa que cuesta 1 y una larga que cuesta puros ceros, obligando a usar deque.agregar_inicio y cambiar predecesores.

## Comparación antes y después

Al principio las pruebas de la cola fallaban si metia algo, lo sacaba (dejandola vacia) y trataba de volver a encolar, porque mi variable final seguia apuntando al nodo viejo. Lo corregi localizando el if de cuando el tamaño se vuelve 0 y actualice tanto frente=None como final=None, volvi a correr pytest y todo paso sin broncas.
