# Reporte de Ejecución de Pruebas: Ordenamiento Topológico

Has obtenido un excelente porcentaje de aprobación en tu suite de pruebas. Sin embargo, hay **4 fallos específicos** relacionados con la validación de tipos, excepciones incorrectas y el orden de los elementos. A continuación, se presenta el análisis detallado y las acciones necesarias para corregirlos.

---

##  Resumen de la Suite

| Estado del Test | Cantidad | Porcentaje |
| :--- | :---: | :---: |
| **Pasados (PASSED)** | 65 | 94.2% |
| **Fallados (FAILED)** | 4 | 5.8% |
| **Total de Casos** | **69** | **100%** |

***Tiempo total de ejecución:** 0.16 segundos.

---

##  Análisis Detallado de Errores

Todos los fallos se concentran en el archivo `tests/test_publico_ordenamiento_topologico.py`. Aquí tienes el desglose de por qué fallan:

### 1. Conservación del orden de aparición
* **Test:** `test_normalizar_conserva_orden_de_primera_aparicion`
* **Error:** `AssertionError: assert ['A', 'B', 'C'] == ['A', 'C', 'B']`
* **Causa:** La función `normalizar_grafo_dirigido` está devolviendo las llaves/nodos en un orden incorrecto. Al procesar `{"A": ["C"], "B": []}`, tu código guardó los nodos como `['A', 'B', 'C']` (probablemente iterando solo sobre las llaves del diccionario original primero). Sin embargo, el test espera `['A', 'C', 'B']`, respetando que el nodo `"C"` apareció como vecino antes de evaluar la llave `"B"`.
* **Solución:** Modifica el algoritmo de recolección de nodos para que recorra el diccionario llave por llave y, al mismo tiempo, extraiga los vecinos en ese instante antes de pasar a la siguiente llave.

### 2. Excepción no lanzada (`TypeError`)
* **Test:** `test_normalizar_rechaza_adyacencia_invalida[vecinos3]` (parámetro: `{"B"}`)
* **Error:** `Failed: DID NOT RAISE TypeError`
* **Causa:** El test espera que si se pasa un conjunto (`set`) como valor de adyacencia, la función lance un `TypeError`. Tu código actual lo aceptó sin protestar, provocando que la prueba fallara al no capturar la excepción configurada con `pytest.raises(TypeError)`.
* **Solución:** Añade una validación estricta de tipos. Si el valor de la adyacencia es un `set`, lanza explícitamente un `TypeError`.

### 3. Tipo de excepción incorrecta (`ValueError` vs `TypeError`)
* **Tests:** 
  * `test_cursos_rechaza_pares_mal_formados[par2]` (parámetro: `[0]`)
  * `test_cursos_rechaza_pares_mal_formados[par3]` (parámetro: `["01"]`)
* **Error:** El bloque del test espera un `ValueError` mediante `with pytest.raises(ValueError):`, pero tu implementación en `implementacion.py` está lanzando un `TypeError`.
* **Causa:** Tu código de producción detecta correctamente que la estructura del par de dependencias es inválida, pero la firma de la excepción no coincide con lo requerido por el diseño de la prueba.
* **Solución:** Ve a `implementacion.py` (aproximadamente en la línea 128) y cambia el tipo de excepción de `TypeError` a `ValueError`:
  ```python
  # Cambiar esto:
  raise TypeError("Cada par de dependencias debe ser una lista o tupla.")
  
  # Por esto:
  raise ValueError("Cada par de dependencias debe ser una lista o tupla.")