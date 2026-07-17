# Clase 13: Revisión de PR
#### Nombre: Patricio Navarro

## Resumen
Se revisaron los archivos de `notebook`, `discusion`  y se puso a prueba el codigo de `implementacion` con las pruebas básicas, del compañero y las mías.

## Código
El código en general se ve muy bien hecho, está bien implementada la recursión dentro de las funciones del árbol AVL, así como `TypeErrors` para manejar errores de dedo. Yo hice todo de forma muy parecida.

## Pruebas
```python
def test_insercion_descendente():
    """Insertar una secuencia descendente no debe degenerar el AVL."""
    
    arbol = construir([50, 40, 30, 20, 10])
    assert arbol.inorden() == [10, 20, 30, 40, 50]
    assert arbol.altura() == 3
    assert arbol.esta_balanceado()

def test_insercion_valores_negativos():
    """El AVL debe manejar correctamente números negativos y el cero."""
    
    arbol = construir([0, -10, 5, -20])
    assert arbol.contiene(-10)
    assert arbol.contiene(0)
    assert not arbol.contiene(-5)
    assert arbol.inorden() == [-20, -10, 0, 5]
    assert arbol.esta_balanceado()

def test_alturas_internas_nodos():
    
    arbol = construir([20, 10, 30, 40])
    
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 20
    assert arbol.raiz.altura == 3
    assert arbol.raiz.izquierdo is not None
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.izquierdo.altura == 1
    assert arbol.raiz.derecho is not None
    assert arbol.raiz.derecho.valor == 30
    assert arbol.raiz.derecho.altura == 2
    assert arbol.raiz.derecho.derecho is not None
    assert arbol.raiz.derecho.derecho.valor == 40
    assert arbol.raiz.derecho.derecho.altura == 1
    assert arbol.esta_balanceado()
```

## Fortalezas
- Código claro.
- Manejo de excepciones.
- Uso de recursión para recorrer el árbol al insertar.
- Comportamiento esperado.

## Mejoras
- Solo en vez de usar un `if` con tres `and` se podrían hacer dos `if` anidados, esto le da mayor claridad al código aunque funcione igual.

## Salida completa de pytest
Ejecutando:
C:\Users\HP\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pytest -v C:\Users\HP\OneDrive\Documents\GitHub\EstructurasDatos\clase_13\tests C:\Users\HP\OneDrive\Documents\GitHub\EstructurasDatos\entregas\clase_13\arturo\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\HP\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\OneDrive\Documents\GitHub\EstructurasDatos\clase_13
configfile: pytest.ini
collecting ... collected 15 items

clase_13\tests\test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED [  6%]
clase_13\tests\test_publico_avl.py::test_arbol_vacio PASSED              [ 13%]
clase_13\tests\test_publico_avl.py::test_insercion_y_busqueda_basica PASSED [ 20%]
clase_13\tests\test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha PASSED [ 26%]
clase_13\tests\test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda PASSED [ 33%]
clase_13\tests\test_publico_avl.py::test_caso_lr_aplica_rotacion_doble PASSED [ 40%]
clase_13\tests\test_publico_avl.py::test_caso_rl_aplica_rotacion_doble PASSED [ 46%]
clase_13\tests\test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED [ 53%]
clase_13\tests\test_publico_avl.py::test_duplicados_no_se_insertan PASSED [ 60%]
clase_13::test_rotacion_simple_ll <- ..\entregas\clase_13\arturo\test_estudiante.py PASSED [ 66%]
clase_13::test_rotacion_doble_lr <- ..\entregas\clase_13\arturo\test_estudiante.py PASSED [ 73%]
clase_13::test_propiedades_generales <- ..\entregas\clase_13\arturo\test_estudiante.py PASSED [ 80%]
clase_13::test_insercion_descendente <- ..\entregas\clase_13\arturo\test_estudiante.py PASSED [ 86%]
clase_13::test_insercion_valores_negativos <- ..\entregas\clase_13\arturo\test_estudiante.py PASSED [ 93%]
clase_13::test_alturas_internas_nodos <- ..\entregas\clase_13\arturo\test_estudiante.py PASSED [100%]

============================= 15 passed in 0.31s ==============================

## Conclusión
El código está bien hecho, tiene el comportamiento esperado y pasó todas las pruebas sin problema.