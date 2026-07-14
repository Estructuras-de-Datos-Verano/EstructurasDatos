# Revisión de PR

## Resumen

    El código presenta una implementación sólida y funcional de un Árbol AVL. Maneja el auto-balanceo correctamente mediante rotaciones simples y dobles tras cada inserción recursiva. La lógica matemática para calcular las alturas y los factores de balance es precisa y mantiene la complejidad de las operaciones de búsqueda e inserción en O(log n).

## Código
    LA verdad, la estructura esta bien, pero a nivel codigo tiene un error, raiz, no debe estar en el constructor del nodo, debe estar en el del ArbolAVL, por eso mis pruebas y otras fallaron

## Pruebas
    Las pruebas corroban el funcionamiento esperado pero hubo muchos errores, mas adelante detallo que fallo 

## Fortalezas
    Las fortalezas de tu entrega radican en la buena implementacion de los metodos con recursividad, el uso de validaiones con isintance.

## Mejoras
    Cambia el constructor de las dos clase, como ya dije, el atributo de raiz debe estar en la clase de AbolAVL, esto es lo que genera todos los errores en las pruebas ejecutadas

## Salida completa de pytest

Ejecutando:
C:\Users\0255295\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe -m pytest -v C:\Users\0255295\Documents\GitHub\EstructurasDatos\clase_13\tests

============================================================================================================= test session starts ==============================================================================================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0255295\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0255295\Documents\GitHub\EstructurasDatos\clase_13
configfile: pytest.ini
plugins: anyio-4.14.0
collected 12 items                                                                                                                                                                                                                              

clase_13\tests\test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED                                                                                                                                                    [  8%]
clase_13\tests\test_publico_avl.py::test_arbol_vacio FAILED                                                                                                                                                                               [ 16%]
clase_13\tests\test_publico_avl.py::test_insercion_y_busqueda_basica PASSED                                                                                                                                                               [ 25%]
clase_13\tests\test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha FAILED                                                                                                                                                           [ 33%]
clase_13\tests\test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda FAILED                                                                                                                                                         [ 41%]
clase_13\tests\test_publico_avl.py::test_caso_lr_aplica_rotacion_doble FAILED                                                                                                                                                             [ 50%]
clase_13\tests\test_publico_avl.py::test_caso_rl_aplica_rotacion_doble FAILED                                                                                                                                                             [ 58%]
clase_13\tests\test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED                                                                                                                                            [ 66%]
clase_13\tests\test_publico_avl.py::test_duplicados_no_se_insertan PASSED                                                                                                                                                                 [ 75%]
clase_13\tests\test_publico_avl.py::test_rotacion_simple_ll_ARTURO FAILED                                                                                                                                                                 [ 83%]
clase_13\tests\test_publico_avl.py::test_rotacion_doble_lr_ARTURO FAILED                                                                                                                                                                  [ 91%]
clase_13\tests\test_publico_avl.py::test_propiedades_generales_ARTURO PASSED                                                                                                                                                              [100%]

=================================================================================================================== FAILURES ===================================================================================================================
_______________________________________________________________________________________________________________ test_arbol_vacio _______________________________________________________________________________________________________________

    def test_arbol_vacio():
        """Un AVL vacío tiene altura 0, recorrido vacío y está balanceado."""
    
        arbol = ArbolAVL()
>       assert arbol.raiz is None
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:35: AttributeError
_____________________________________________________________________________________________________ test_caso_ll_aplica_rotacion_derecha _____________________________________________________________________________________________________

    def test_caso_ll_aplica_rotacion_derecha():
        """El patrón LL debe producir una rotación derecha local."""
    
        arbol = construir([30, 20, 10])
>       assert arbol.raiz.valor == 20
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:58: AttributeError
____________________________________________________________________________________________________ test_caso_rr_aplica_rotacion_izquierda ____________________________________________________________________________________________________

    def test_caso_rr_aplica_rotacion_izquierda():
        """El patrón RR debe producir una rotación izquierda local."""
    
        arbol = construir([10, 20, 30])
>       assert arbol.raiz.valor == 20
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:70: AttributeError
______________________________________________________________________________________________________ test_caso_lr_aplica_rotacion_doble ______________________________________________________________________________________________________

    def test_caso_lr_aplica_rotacion_doble():
        """El patrón LR debe aplicar izquierda en el hijo y derecha en el nodo."""
    
        arbol = construir([30, 10, 20])
>       assert arbol.raiz.valor == 20
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:82: AttributeError
______________________________________________________________________________________________________ test_caso_rl_aplica_rotacion_doble ______________________________________________________________________________________________________

    def test_caso_rl_aplica_rotacion_doble():
        """El patrón RL debe aplicar derecha en el hijo e izquierda en el nodo."""
    
        arbol = construir([10, 30, 20])
>       assert arbol.raiz.valor == 20
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:94: AttributeError
________________________________________________________________________________________________________ test_rotacion_simple_ll_ARTURO ________________________________________________________________________________________________________

    def test_rotacion_simple_ll_ARTURO():
        """
        Prueba de Rotación Simple (Caso LL).
    
        Se insertan tres valores en orden descendente (30, 20, 10) para forzar
        un peso excesivo en el subárbol izquierdo de la raíz. El árbol debe
        detectar un factor de balance > 1 y aplicar una rotación derecha.
        """
        arbol = ArbolAVL()
        arbol.insertar(30)
        arbol.insertar(20)
        arbol.insertar(10)
    
        # La nueva raíz debe ser 20, con 10 a la izquierda y 30 a la derecha
>       assert arbol.raiz is not None
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:133: AttributeError
________________________________________________________________________________________________________ test_rotacion_doble_lr_ARTURO _________________________________________________________________________________________________________

    def test_rotacion_doble_lr_ARTURO():
        """
        Prueba de Rotación Doble (Caso LR).
    
        Se insertan valores (30, 10, 20) de forma que el desbalance ocurra en
        el hijo derecho del subárbol izquierdo. El árbol debe aplicar primero
        una rotación izquierda en el nodo 10 y luego una rotación derecha en la raíz.
        """
        arbol = ArbolAVL()
        arbol.insertar(30)
        arbol.insertar(10)
        arbol.insertar(20)
    
        # El resultado estructural debe ser idéntico al caso LL
>       assert arbol.raiz is not None
               ^^^^^^^^^^
E       AttributeError: 'ArbolAVL' object has no attribute 'raiz'

clase_13\tests\test_publico_avl.py:155: AttributeError
=========================================================================================================== short test summary info ============================================================================================================
FAILED clase_13\tests\test_publico_avl.py::test_arbol_vacio - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
FAILED clase_13\tests\test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
FAILED clase_13\tests\test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
FAILED clase_13\tests\test_publico_avl.py::test_caso_lr_aplica_rotacion_doble - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
FAILED clase_13\tests\test_publico_avl.py::test_caso_rl_aplica_rotacion_doble - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
FAILED clase_13\tests\test_publico_avl.py::test_rotacion_simple_ll_ARTURO - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
FAILED clase_13\tests\test_publico_avl.py::test_rotacion_doble_lr_ARTURO - AttributeError: 'ArbolAVL' object has no attribute 'raiz'
========================================================================================================= 7 failed, 5 passed in 0.14s ==========================================================================================================


## Conclusión

Es un general es una buena implementacion optimizada, solo:

Reitero los cambios:


    - Eliminar la propiedad @property def raiz dentro de la clase NodoAVL, ya que mezcla responsabilidades. Un nodo no debería saber sobre la "raíz" general ni acceder a atributos que no posee.