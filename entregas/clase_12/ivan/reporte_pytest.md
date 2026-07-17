# Reporte Pytest
- Comando: python evaluar.py entregas/clase_12/ivan clase_12/tests entregas/clase_12/ivan/test_estudiante.py ; 
- Salida: 
```powershell
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_12/ivan clase_12/tests entregas/clase_12/ivan/test_estudiante.py
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_12\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_12\ivan\test_estudiante.py

=================================================================== test session starts ====================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_12
configfile: pytest.ini
plugins: anyio-4.7.0
collected 27 items                                                                                                                                          

clase_12\tests\test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                         [  3%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                         [  7%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                      [ 11%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                    [ 14%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                    [ 18%]
clase_12\tests\test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                    [ 22%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                               [ 25%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                               [ 29%]
clase_12\tests\test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                      [ 33%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_balanceada PASSED                                                                      [ 37%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_degenerada PASSED                                                                      [ 40%]
clase_12\tests\test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima PASSED                                                         [ 44%]
clase_12::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                           [ 48%]
clase_12::test_altura_de_arbol_vacio PASSED                                                                                                           [ 51%]
clase_12::test_altura_de_arbol_con_raiz PASSED                                                                                                        [ 55%]
clase_12::test_altura_de_arbol_balanceado PASSED                                                                                                      [ 59%]
clase_12::test_altura_de_arbol_degenerado PASSED                                                                                                      [ 62%]
clase_12::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                      [ 66%]
clase_12::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                 [ 70%]
clase_12::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                 [ 74%]
clase_12::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                        [ 77%]
clase_12::test_todo_busqueda_balanceada PASSED                                                                                                        [ 81%]
clase_12::test_todo_busqueda_degenerada PASSED                                                                                                        [ 85%]
clase_12::test_todo_insercion_ordenada_altura_maxima PASSED                                                                                           [ 88%]
clase_12::test_altura_base PASSED                                                                                                                     [ 92%]
clase_12::test_buscar_inexistente PASSED                                                                                                              [ 96%]
clase_12::test_degenerado PASSED                                                                                                                      [100%]

==================================================================== 27 passed in 0.13s ====================================================================
```
- Interpretación: Las pruebas se ejecutaron correctamente gracias a la buena implementación, un diseño adecuado de pruebas propias y por haber modificado temporalmente los 
```python 
@pytest.mark.skip(reason="TODO alumno: diseña una prueba de búsqueda en árbol degenerado.") 
``` 
;
- Cuántas pruebas se ejecutaron: 27;
- Cuántas pasaron: 27;
- Si hubo errores: No los hubo;
- Qué comportamiento verifican: Casos base (BST's unitarios o vacíos) con altura, búsqueda, inserción, degeneración, bugs de duplicar, etc ;
- Qué prueba diseñaste: 
```python
def test_altura_base():
    """
    Verifica que la altura del árbol vacío es cero y que la altura del árbol unitario es uno
    """
    arbol_2 = ArbolBinarioBusqueda()
    arbol_2.insertar(2)
    arbol = ArbolBinarioBusqueda()
    assert arbol.altura() == 0
    assert arbol_2.altura() == 1

def test_buscar_inexistente():
    """
    Verifica que buscar un valor en un árbol vacío sea False y que buscar un valor inexistente en uno unitario sea False
    """
    arbol_2 = ArbolBinarioBusqueda()
    arbol_2.insertar(2)
    arbol = ArbolBinarioBusqueda()
    assert arbol.contiene(4) == False
    assert arbol_2.contiene(4) == False

def test_degenerado():
    """
    Verifica que el árbol vacío no sea degenerado y que un árbol degenerado es reconocido por el método correctamente
    """
    arbol_2 = ArbolBinarioBusqueda()
    arbol = ArbolBinarioBusqueda()
    for valor in range(10):
        arbol.insertar(valor)
    assert arbol.es_degenerado() == True
    assert arbol_2.es_degenerado() == False
```
 ;
- Qué caso todavía falta probar: Tamaños muy grandes o inserciones a nodos que no son hojas en BST's balanceados. 