# Arturo Prudencio Bonilla

## 1. ¿Un BST siempre es eficiente?
    No siempre, pues si es un arbol degenerado la complejidad de busqueda pierde su eficiencia y se convierte en O(n)
## 2. Lista vs BST
    Un BST es una estrcutura de datos que se puede aprovechar mucho pero no siempre, como ya respondi en la pregunta anterior, cuando los datos se comportan de manera creciente y ordenada, una lista y un BST son practicamente lo mismo, por lo que un BST para bsqueda es mejor que una lista, siempre y cuando no se de el caso ya mencionado 
## 3. Altura y comparaciones
    Ya teniamos una forma de obtener la altura de un nodo o un arbol, pero ahora teorizo que la altura de un nodo es la cantidad de comparaciones necesarias para buscar a ese mismo nodo, esta hipotecis esta alimentada por las multiples pruebas y preguntas a lo largo de esta clase que revelan este patron para lso casos vistos
## 4. Árbol balanceado vs árbol degenerado
    Un arbol balanceado es el caso ideal, cuando la estrcutura BST luce su maximo potencial para buscar datos, mientras que en el otro polo esta el arbol degenerado, el cual es el peor caso, donde cada nodo tiene a lo mas un hijo lo que lo convierte en un analogo a la lista
## 5. Orden de inserción
    EL orden de insercion importa mucho pues si los datos se insertan de manera ordenada y creciente siempre caeremos en u arbol degenerado, mientras que si lo hacemos de otro modo podemos tener un arbol balanceado; Aun me queda la duda de si al igual que con el orden de insercion creciente, algun otro tipo de orden de insercion especifico nos da siempre un arbol balanceado
## 6. Complejidad
    La complejidad para los dos casos mas relevantes (arboles balanceados y degenerados) cambia mucho con muchos datos, porque mientras que la compejidad de los degenerados es lineal O(n), la de los balanceados es O(logn), lo cual hace mucha diferencia cuando el objetio es trabajar con muchisimos datos
## 7. Experimentos y evidencia
    En esta clase, mis experiementos se limitaron a hacer pruebas con arboles balanceado y degenerados, poner a prueba mis funciones y sobre todo comprobar que el compitramiento esperado es correcto y la implementacion tambien, a su vez esta como evidencia de esto el archivo llamado reporte_pytest en donde hay un compendio del resultados de las pruebas publica y las mias 
## 8. Animaciones
    Sinceramnete no me sirvieron de mucho en esta clase, pues para cuando avance por esa seccion aun tenian errores, por lo que poco o nada puedo decir de estas
## 9. Pruebas propias
    En mis pruebas comprobe dos comportamientos basicos pero indispensables para el codigo, comporbar que la altura de un arbol degenerado es la misma que la cantidad de nodos que hay.

    Por otro lado, en mi seguda prueba, corrobore que mis dos funciones, contien y compaacion_busqueda son complementrias: esto porque contiene te dice si el arbol contiene el dato buscado y la otra funcion nos dice cuantas comparaciones necesito para encontrarlo
## 10. Revisión técnica del PR
clase_12\tests\test_publico_bst_balance.py::test_nodo_guarda_valor_y_empieza_sin_hijos PASSED                                                                                                                       [  6%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_vacio PASSED                                                                                                                                       [ 13%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_con_raiz PASSED                                                                                                                                    [ 20%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_balanceado PASSED                                                                                                                                  [ 26%]
clase_12\tests\test_publico_bst_balance.py::test_altura_de_arbol_degenerado PASSED                                                                                                                                  [ 33%]
clase_12\tests\test_publico_bst_balance.py::test_inorden_sigue_regresando_valores_ordenados PASSED                                                                                                                  [ 40%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_balanceado PASSED                                                                                                             [ 46%]
clase_12\tests\test_publico_bst_balance.py::test_busqueda_con_conteo_de_comparaciones_degenerado PASSED                                                                                                             [ 53%]
clase_12\tests\test_publico_bst_balance.py::test_duplicados_no_aumentan_cantidad_de_nodos PASSED                                                                                                                    [ 60%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_balanceada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol balanceado.)                                                                 [ 66%]
clase_12\tests\test_publico_bst_balance.py::test_todo_busqueda_degenerada SKIPPED (TODO alumno: diseña una prueba de búsqueda en árbol degenerado.)                                                                 [ 73%]
clase_12\tests\test_publico_bst_balance.py::test_todo_insercion_ordenada_altura_maxima SKIPPED (TODO alumno: diseña una prueba de altura máxima por inserción ordenada.)                                            [ 80%]
clase_12::test_busqueda_en_arbol_balanceado_cuenta_comparaciones_correctas PASSED                                                                                                                                   [ 86%]
clase_12::test_insercion_ordenada_produce_altura_maxima_y_arbol_degenerado PASSED                                                                                                                                   [ 93%]
clase_12::test_recorrido_preorden_y_postorden_son_coherentes PASSED                                                                                                                                                 [100%]

============================================================================================= 12 passed, 3 skipped in 0.05s ==============================================================================================

como observación constructiva: te puedo decir que esta bien hecho quiza te falte un poco de concicidad a la hora de responde preguntas pero todo bien.

## 11. Problemas relacionados
    Hay multiples problemas relacionados pero yo destaco '98. Validate Binary Search Tree'; pues me parece muy interesate agregar un nuevo parametro para validar un BST y ademas da pie a una implementacion mas robusta 
## 12. Pregunta abierta
    ¿En mi implementacion, que pasa con la funcion 'comparacion_busqueda' si le das un valor que no esta en el arbol?