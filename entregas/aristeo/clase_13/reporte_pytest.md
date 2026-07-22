## Comando ejecutado
```
evaluar.py entregas/clase_13/nombre clase_13/tests
```

## Salida completa
```
================================================================================================== test session starts ===================================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_13
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.14.1
collected 9 items                                                                                                                                                                                                         

tests/test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED                                                                                                                                       [ 11%]
tests/test_publico_avl.py::test_arbol_vacio PASSED                                                                                                                                                                  [ 22%]
tests/test_publico_avl.py::test_insercion_y_busqueda_basica PASSED                                                                                                                                                  [ 33%]
tests/test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha PASSED                                                                                                                                              [ 44%]
tests/test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda PASSED                                                                                                                                            [ 55%]
tests/test_publico_avl.py::test_caso_lr_aplica_rotacion_doble PASSED                                                                                                                                                [ 66%]
tests/test_publico_avl.py::test_caso_rl_aplica_rotacion_doble PASSED                                                                                                                                                [ 77%]
tests/test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED                                                                                                                               [ 88%]
tests/test_publico_avl.py::test_duplicados_no_se_insertan PASSED                                                                                                                                                    [100%]

=================================================================================================== 9 passed in 0.06s ====================================================================================================
```
## Interpretación
Todo jaló muy bien.
## Número de pruebas
9 pruebas
## Cuántas pasaron
Todas, las 9
## Qué comportamiento verifican
- test_nodo_avl_guarda_valor_y_altura_inicial
- test_arbol_vacio 
- test_insercion_y_busqueda_basica 
- test_caso_ll_aplica_rotacion_derecha
- test_caso_rr_aplica_rotacion_izquierda 
- test_caso_lr_aplica_rotacion_doble 
- test_caso_rl_aplica_rotacion_doble
- test_altura_se_mantiene_baja_con_insercion_ordenada 
- test_duplicados_no_se_insertan 

## Qué pruebas diseñaste tú
``` python 
def test_rotacion_simple_rr():
    """
    Verifica que una inserción secuencial ascendente (10, 20, 30)
    provoque una rotación simple a la izquierda (Caso RR) y la raíz cambie a 20.
    """
    arbol = ArbolAVL()
    arbol.insertar(10)
    arbol.insertar(20)
    arbol.insertar(30)
    
    assert arbol.raiz.valor == 20
    assert arbol.esta_balanceado()
    assert arbol.inorden() == [10, 20, 30]

def test_rotacion_doble_lr():
    """
    Verifica que el caso Izquierda-Derecha (LR) balancee correctamente el árbol
    mediante una rotación doble (izquierda sobre el hijo, derecha sobre la raíz).
    """
    arbol = ArbolAVL()
    arbol.insertar(30)
    arbol.insertar(10)
    arbol.insertar(20)
    
    assert arbol.raiz.valor == 20
    assert arbol.altura() == 2
    assert arbol.inorden() == [10, 20, 30]

def test_propiedad_inorden_y_balance_masivo():
    """
    Inserta múltiples elementos desordenados y valida que el recorrido inorden
    permanezca perfectamente ordenado y la propiedad AVL se mantenga intacta.
    """
    arbol = ArbolAVL()
    valores = [50, 25, 75, 15, 35, 60, 120, 10, 68]
    
    for v in valores:
        arbol.insertar(v)
        
    assert arbol.esta_balanceado()
    assert arbol.inorden() == sorted(valores)
```
## Qué caso importante todavía falta probar.
Inserciones que disparan re-balanceos múltiples