# Discusión técnica

## 1. Problema que resuelve AVL
Resuelve el alto costo de explorar árboles degenerados mediante el rebalanceo[cite: 5]. En un árbol sin balancear, el peor caso requeriría recorrer n nodos más la raíz.

## 2. Factor de balance
Se calcula con la diferencia entre la altura izquierda y derecha. Un factor de 2 denota carga a la izquierda, aunque cuestiono esa lógica en un BST porque en un BST todos los nodos a la izquierda son menores y tiene más sentido decir carga de -2 si hay más elementos menores.

## 3. Rotaciones e invariante BST
Las rotaciones rebalancean el árbol moviendo un subárbol desbalanceado. Estas operaciones nunca alteran el invariante del árbol, manteniendo intacto el orden de recorrido inorden.

## 4. Casos LL RR LR RL
El patrón LL aplica rotación derecha local y RR rotación izquierda local. LR aplica rotación izquierda en hijo y derecha en nodo, mientras RL aplica derecha en hijo e izquierda en nodo[cite: 3].

## 5. Complejidad
Sin AVL, la búsqueda de un elemento puede implicar comparar con todos los n nodos. El balanceo continuo previene esta degeneración estructural para mantener búsquedas eficientes.

## 6. Pruebas propias
Se agregaron exitosamente tres pruebas para evaluar un orden descendente, inserción de negativos y alturas internas. Adicionalmente validan la prevención de árboles degenerados.

## 7. Revisión técnica recibida

## 8. Revisión técnica realizada

También por las faltas justificadas no entré en la dinámica de asignar revisiones. Sin embargo, ejecuté mis pruebas en la rama de Leo porque es quien me hubiera tocado si hubiera estado (según yo y lo que sé de quién faltó). Todas pasaron y la salida fue: 
```powershell
PS C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos> python evaluar.py entregas/clase_13/LEO clase_13/tests entregas/clase_13/Pato/test_estudiante.py

Ejecutando:
C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe -m pytest -v C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_13\tests C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\entregas\clase_13\Pato\test_estudiante.py

==================================================================== test session starts =====================================================================
platform win32 -- Python 3.12.5, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\josei\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\josei\OneDrive\Documentos\GitHub\EstructurasDatos\clase_13
configfile: pytest.ini
plugins: anyio-4.7.0
collected 12 items                                                                                                                                            

clase_13\tests\test_publico_avl.py::test_nodo_avl_guarda_valor_y_altura_inicial PASSED                                                                  [  8%]
clase_13\tests\test_publico_avl.py::test_arbol_vacio PASSED                                                                                             [ 16%]
clase_13\tests\test_publico_avl.py::test_insercion_y_busqueda_basica PASSED                                                                             [ 25%]
clase_13\tests\test_publico_avl.py::test_caso_ll_aplica_rotacion_derecha PASSED                                                                         [ 33%]
clase_13\tests\test_publico_avl.py::test_caso_rr_aplica_rotacion_izquierda PASSED                                                                       [ 41%]
clase_13\tests\test_publico_avl.py::test_caso_lr_aplica_rotacion_doble PASSED                                                                           [ 50%]
clase_13\tests\test_publico_avl.py::test_caso_rl_aplica_rotacion_doble PASSED                                                                           [ 58%]
clase_13\tests\test_publico_avl.py::test_altura_se_mantiene_baja_con_insercion_ordenada PASSED                                                          [ 66%]
clase_13\tests\test_publico_avl.py::test_duplicados_no_se_insertan PASSED                                                                               [ 75%]
clase_13::test_insercion_descendente <- ..\entregas\clase_13\Pato\test_estudiante.py PASSED                                                             [ 83%]
clase_13::test_insercion_valores_negativos <- ..\entregas\clase_13\Pato\test_estudiante.py PASSED                                                       [ 91%]
clase_13::test_alturas_internas_nodos <- ..\entregas\clase_13\Pato\test_estudiante.py PASSED                                                            [100%]

===================================================================== 12 passed in 0.10s =====================================================================
```
## 9. Pregunta abierta

¿Qué pasaría con el rendimiento general si modificamos el invariante para permitir una diferencia de altura de 2 en lugar de 1? ¿El ahorro en rotaciones justificaría el costo extra al buscar elementos?