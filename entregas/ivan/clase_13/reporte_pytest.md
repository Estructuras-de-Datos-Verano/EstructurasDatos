# Reporte de Pytest
-**Comando ejecutado:**
```bash
python evaluar.py entregas/clase_13/ivan clase_13/tests
```
;
- **Salida completa:**
```powershell
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_13/ivan clase_13/tests
Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_13\tests

==================================================================== test session starts =====================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_13
configfile: pytest.ini
plugins: anyio-4.7.0
collected 9 items                                                                                                                                             

clase_13\tests\test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED                                                                  [ 11%]
clase_13\tests\test_publico_avl.py::test_arbol_vacio PASSED                                                                                             [ 22%]
clase_13\tests\test_publico_avl.py::test_insercion_y_busqueda_basica PASSED                                                                             [ 33%]
clase_13\tests\test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha PASSED                                                                         [ 44%]
clase_13\tests\test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda PASSED                                                                       [ 55%]
clase_13\tests\test_publico_avl.py::test_caso_lr_aplica_rotacion_doble PASSED                                                                           [ 66%]
clase_13\tests\test_publico_avl.py::test_caso_rl_aplica_rotacion_doble PASSED                                                                           [ 77%]
clase_13\tests\test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED                                                          [ 88%]
clase_13\tests\test_publico_avl.py::test_duplicados_no_se_insertan PASSED                                                                               [100%]

===================================================================== 9 passed in 0.06s ======================================================================
``` 
;
- **Interpretación:**
Todas las pruebas fueron exitosas. Las implementaciones siguieron una lógica adecuada, respetan las convenciones/invariante además del contrato incluso en casos límite
;
- **Número de pruebas:** 9;
- **Cuántas pasaron:** 9;
- **Qué comportamiento verifican:** Inserción y búsqueda, rotaciones simples y dobles, casos límite con alturas e inserciones, inserción de duplicados, etc. ;
- **Qué pruebas diseñaste tú:** Las que verifican rotación simple ascendente (para verificar inorden principalmente), rotaciones dobles y propiedades generales con el decorador de parametrización de pytest (lo vemos en clases futuras) para verificar varios casos
Código:
```python
def test_rotacion_simple_rr_ascendente():
    """Verifica que una inserción netamente ascendente aplique rotaciones simples RR."""
    
    arbol = construir([10, 20, 30, 40, 50])
    
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 20
    assert arbol.raiz.izquierdo.valor == 10
    assert arbol.raiz.derecho.valor == 40
    assert arbol.raiz.derecho.izquierdo.valor == 30
    assert arbol.raiz.derecho.derecho.valor == 50
    assert arbol.esta_balanceado()


def test_rotacion_doble_lr_zigzag():
    """Comprueba que un patrón de inserción en zigzag (LR) detone la rotación doble."""
    
    arbol = construir([50, 20, 30])
    
    assert arbol.raiz is not None
    assert arbol.raiz.valor == 30
    assert arbol.raiz.izquierdo.valor == 20
    assert arbol.raiz.derecho.valor == 50
    assert arbol.altura() == 2
    assert arbol.esta_balanceado()


@pytest.mark.parametrize("valores, esperado_inorden, esperada_altura", [
    ([10, 20, 30], [10, 20, 30], 2),                                 # Caso básico
    ([5, 5, 5, 5], [5], 1),                                          # Ignora duplicados
    ([-10, 0, 10, -5], [-10, -5, 0, 10], 3),                         # Valores negativos
    ([100, 50, 150, 25, 75, 125, 175], [25, 50, 75, 100, 125, 150, 175], 3) # Árbol perfecto
])
def test_propiedades_generales_avl(valores, esperado_inorden, esperada_altura):
    """Verifica que el árbol mantenga inorden ordenado, altura correcta y balance ante múltiples casos."""
    
    arbol = construir(valores)
    
    # Se validan tres rasgos generales de la implementación simultáneamente
    assert arbol.inorden() == esperado_inorden
    assert arbol.altura() == esperada_altura
    assert arbol.esta_balanceado()
```
;
- **Qué caso importante todavía falta probar:** Me gustaría probar que las rotaciones dobles en desbalances de tamaño >= abs(2) realmente disminuyan la complejidad espacio-temporal.