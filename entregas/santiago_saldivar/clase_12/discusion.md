Santiago Saldívar Garcini

Un BST sólo será eficiente si está balanceado. De lo contrario, hará comparaciones excesivas. 
Si el BST no está balanceado, se parecerá a una lista en su ineficiencia. La lista es muy útil cuando se necesita guardar orden, pero es ineficiente al buscar. El BST busca resolver ese problema, pero si no se usa bien y no se aprovecha, no servirá de nada.
La altura es el máximo nivel. Es igual al número de comparaciones en el peor caso.
Cuando un árbol está balanceado, será eficiente. Los árboles degenerados parecerán listas, lo que los hace ineficientes para lo que se quiere.
El Orden de inserción es importante, porque define si estará o no balanceado. Debería empearce como por la mitad de los valores, e ir agregando chicos y grandes. Si se insertan en orden, no será balanceado.
Si es balanceado la complejidad es O(logn), si no, es O(n).
Los experimentos al respecto se pueden hacer fácilmente. Notamos en el código que el árbol degenerado es más lento. Eso se ve aun mejor en las animaciones.
Las pruebas, además de revisar que funcione todo bien, comparan el balance y el degenere, notando que el primero es más eficiente.
Agregué las pruebas:
    -test_agregado_1_balance_mas_eficiente, compara eficiencia.
    -test_agregado_2_altura_maxima, compara altura.
    -test_agregado_3_busqueda_degenerada, compara crecimiento.

Yo elegí el problema de la sitancia entre nodos, y es una muy buena forma de comparar el balance, porque aumenta dramáticamente si es degenerado.
¿Qué otros errores debo evitar con esta y otras estructuras de datos?

## Revisión Pato:
=========================================================================================== test session starts ===========================================================================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0261331\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0261331\Documents\GitHub\EstructurasDatos\clase_12
configfile: pytest.ini
collected 18 items                                                                                                                                                                                         

clase_12\tests\test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                                        [  5%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                                                                        [ 11%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                                                                     [ 16%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                                                                   [ 22%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                                                                   [ 27%]
clase_12\tests\test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                                   [ 33%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                              [ 38%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                              [ 44%]
clase_12\tests\test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                                     [ 50%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_balanceada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol balanceado.)                                                  [ 55%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_degenerada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol degenerado.)                                                  [ 61%]
clase_12\tests\test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima SKIPPED (TODO alumno: diseña una prueba de altura máxima por inserción ordenada.)                             [ 66%]
clase_12\tests\test_publico_bst_balance.py::test_agregado_1_balance_mas_eficiente PASSED                                                                                                             [ 72%]
clase_12\tests\test_publico_bst_balance.py::test_agregado_2_altura_maxima PASSED                                                                                                                     [ 77%]
clase_12\tests\test_publico_bst_balance.py::test_agregado_3_busqueda_degenerada FAILED                                                                                                               [ 83%]
clase_12\tests\test_publico_bst_balance.py::test_comparaciones_igual_altura PASSED                                                                                                                   [ 88%]
clase_12\tests\test_publico_bst_balance.py::test_cantidad_nodos PASSED                                                                                                                               [ 94%]
clase_12\tests\test_publico_bst_balance.py::test_es_degenerado FAILED                                                                                                                                [100%]

================================================================================================ FAILURES =================================================================================================
___________________________________________________________________________________ test_agregado_3_busqueda_degenerada ___________________________________________________________________________________

    def test_agregado_3_busqueda_degenerada():
        """Verifica que las comparaciones sigan creciendo según se degenera más el árbol."""
    
        valores = [1,2,3,4,5,6,7]
        lista = []
    
        for valor in valores:
            lista.append(valor)
            arbol = construir(lista)
    
            assert arbol.altura() == len(lista)
    
        valores2 = [7,4,10,3] #9,5,12
        auxiliar = [9, 5, 12]
    
    
        for valor in auxiliar:
>           valores2.append(auxiliar.popleft())
                            ^^^^^^^^^^^^^^^^
E           AttributeError: 'list' object has no attribute 'popleft'

clase_12\tests\test_publico_bst_balance.py:149: AttributeError
___________________________________________________________________________________________ test_es_degenerado ____________________________________________________________________________________________

    def test_es_degenerado():
        arbol1 = construir([1, 2, 3, 4])
        arbol2 = ArbolBinarioBusqueda()
        arbol3 = construir([8])
    
        assert arbol1.es_degenerado() == True
        assert arbol2.es_degenerado() == False
>       assert arbol3.es_degenerado() == True
E       assert False == True
E        +  where False = es_degenerado()
E        +    where es_degenerado = <entregas.clase_12.Santiago_Saldivar.implementacion.ArbolBinarioBusqueda object at 0x000001EE7F0D99D0>.es_degenerado

clase_12\tests\test_publico_bst_balance.py:169: AssertionError
========================================================================================= short test summary info =========================================================================================
FAILED clase_12\tests\test_publico_bst_balance.py::test_agregado_3_busqueda_degenerada - AttributeError: 'list' object has no attribute 'popleft'
FAILED clase_12\tests\test_publico_bst_balance.py::test_es_degenerado - assert False == True
================================================================================= 2 failed, 13 passed, 3 skipped in 0.08s =================================================================================

### Observaciones:
- En la prueba de es_degenerado, falló por una diferencia en criterio, solo es si cuando el árbol tiene un elemento, ¿se considera degenerado, o balanceado?
- la prueba 3 falló porque las listas no tienen el atributo `.popleft()`
- En algunas partes del archivo `test_estudiante` faltaron paréntesis cosa que se tuvo que corregir para poder correrlo
- Fuera de eso realmente todo bien.