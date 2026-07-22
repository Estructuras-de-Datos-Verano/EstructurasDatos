# Clase 12: Discusión
#### Nombre: Patricio Navarro

## 1. ¿Un BST siempre es eficiente?
- No, cuando está degenerado pierede justamente esa eficiencia para buscar, también tengo dudas quá pasa cuando intentas insertar un nodo intermedio.
## 2. Lista vs BST
- Las listas son mejores para tareas simples, si vas a hacer muchas búsquedas o si necesitas que los datos estén ordenados es mejor un BST.
## 3. Altura y comparaciones
- Tienen una relación 1:1, al menos con las pruebas que hicimos.
## 4. Árbol balanceado vs árbol degenerado
- Un árbol degenerado se comporta como una lista enlazada, es el peor caso para los BST, mientras que un árbol balanceado tiene una complejidad para buscar de O(log(n)) que es mejor que la O(n) de las listas.
## 5. Orden de inserción
- Se empieza de arriba hacia abajo, la raíz es el primer nodo, de ahí nacen dos nodos, menores a la izquierda, mayores a la derecha, no hay repeticiones. Y luego va de izquierda a derecha.
## 6. Complejidad
- O(log(n)) porque en cada búsqueda se descarta un mitad de cada subárbol, descartando muchos datos innecesarios.
## 7. Experimentos y evidencia
- Comprobé que se contaran todos los nodos, pero que la búsqueda no los recorriera todos (en el caso de que no fuera degenerado) y que fuera igual a la altura. 
## 8. Animaciones
- Mostraban de forma clara la relación entre comparaciones y altura y la forma en que realiza la búsqueda un BST.
## 9. Pruebas propias
- 
```python
def test_comparaciones_igual_altura():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.altura() == arbol.comparaciones_busqueda(14)

def test_cantidad_nodos():
    arbol = construir([8, 4, 12, 2, 6, 10, 14])
    assert arbol.cantidad_nodos() == 7

def test_es_degenerado():
    arbol1 = construir([1, 2, 3, 4])
    arbol2 = ArbolBinarioBusqueda()
    arbol3 = construir([8])

    assert arbol1.es_degenerado() == True
    assert arbol2.es_degenerado() == False
    assert arbol3.es_degenerado() == True
```
## 10. Revisión técnica del PR
```
Observación constructiva: Considero que está bien explicado, aunque faltan pruebas en la parte 7 y así, de ahí en fuera está kul.
====================================================================================== test session starts =======================================================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0281528\Documents\GitHub\EstructurasDatos\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0281528\Documents\GitHub\EstructurasDatos\clase_12
configfile: pytest.ini
plugins: anyio-4.14.1
collected 15 items                                                                                                                                                                                

clase_12\tests\test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                               [  6%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                                                               [ 13%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                                                            [ 20%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                                                          [ 26%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                                                          [ 33%]
clase_12\tests\test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                          [ 40%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                     [ 46%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                     [ 53%]
clase_12\tests\test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                            [ 60%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_balanceada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol balanceado.)                                         [ 66%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_degenerada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol degenerado.)                                         [ 73%]
clase_12\tests\test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima SKIPPED (TODO alumno: diseña una prueba de altura máxima por inserción ordenada.)                    [ 80%]
clase_12::test_mi_arbol_vacio_es_degenerado FAILED                                                                                                                                          [ 86%]
clase_12::test_mi_arbol_balanceado_no_es_degenerado PASSED                                                                                                                                  [ 93%]
clase_12::test_mi_conteo_comparaciones_fallidas PASSED                                                                                                                                      [100%]

============================================================================================ FAILURES ============================================================================================
```
## 11. Problemas relacionados
- Subordinates
- Company Queries I
## 12. Pregunta abierta
- ¿Usar recursión para los métodos de u BST es lo más óptimo, o como se podría hacer mejor?