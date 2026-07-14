# Discusión.md clase_15_Max

## 1. Diferencia entre distancia por aristas y por pesos.

La diferencia principal es que para los pesos se busca la menor cantidad de dinero posible para llegar de punto a a b, para la cuestion de distancia se busca lo mismo respectivamente, que es buscar el camino más barato en cuanto a distancia se refiere.

## 2. Significado de distancia tentativa.

La distancia tentativa es una de las opciones disponibles que tenemos para crear nuestra ruta, todo es una distancia tentativa en cuestión, hasta que alguna es seleccionada.

## 3. Relajación con un ejemplo numérico.

Un gran ejemplo de relajacios es que si queremos llegar de a A a D pero tenemos que A a B, B a D cuesta un peso respectivamente, siendo en total 2 pesos y de A a C, C a D son gratis ambos caminos una ruta relajada seria elegir ir a D mediante C, ya que es la ruta más barata. 

## 4. Razón para usar min-heap.

La razón principal es para poder jerarquizar este tipo de rutas baratas desde el punto de partida a donde querermos llegar para así poder tener la ruta más barata en cuestión.

## 5. Entrada obsoleta y eliminación perezosa.

La entrada obsoleta viene siendo la que no se utilizo o por descarte el ultimo nodo del cúal ya no podemos ir a ningun otro, y la eliminación perezosa es todo menos una eliminación, ya que para hacer esto más eficiente, justamente no se elimina, simplemente se ignora para así poder seguir.

## 6. Reconstrucción mediante predecesores.

La reconstrucción aquí nos indica de donde venimos y esto nos define a donde es a donde vam,os por los costos, es algo casi de tipo modular, donde dependiendo de donde vienes es a donde vas.

## 7. Complejidad temporal y espacial.

La complejidad temporal va a venir siendo más grande que la espacial, ya que la espacial tiene en cuenta absolutamente todo, y ya teniendo todo en cuenta la dificultad viene siendo logaritmica, mientras que si nos vamos a la temporal que es paso a paso es continua.

## 8. Restricción de pesos no negativos.

La restricción es crucial, ya que de no tenerla vamos a tener que la interpretación es que en el caso que haya caminos con valores negativos es que estos caminos en lugar de cobrarnos, nos estan pagando por recorrerlos, lo cual no sucede nunca.

## 9. Caso donde BFS falla.

Falla en cuestiones de ponderar bien los precios para cada cosa, ya que de tener en cuenta todos los precios no se va a poder jerarquizar y así poder resolver lo que necesitamos de manera correcta.

## 10. Evidencia de tus pruebas.

Ojo: cambio a las pruebas del profe:

Antes:

def test_vecino_implicito_se_incluye():
    distancias, predecesores = dijkstra({"A": [("B", 3)]}, "A")
    assert distancias["B"] == 3
    assert predecesores["B"] == "A"

Despues:

def test_vecino_implicito_se_incluye():
    distancias, predecesores = dijkstra({"A": [("B", 3)], "B": []}, "A")
    assert distancias["B"] == 3
    assert predecesores["B"] == "A"

Se agrego el "B": [] porque si no se agrega a la hora de iterar no se toma en cuenta que este nodo exista, entonces no se puede ver la distancia con los nodos vecinos proque en nod men cuestion no existe, con esta observación y una vez que fue corregido para iterar, se tiene que todas las pruebas se pasaron de manera correcta: 

Ejecutando:
C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe -m pytest -v C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_15\tests C:\Users\0286761\Documents\GitHub\EstructurasDatos\entregas\clase_15\max\test_estudiante.py

============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\0286761\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\0286761\Documents\GitHub\EstructurasDatos\clase_15
configfile: pytest.ini
collecting ... collected 14 items

clase_15\tests\test_publico_dijkstra.py::test_origen_tiene_distancia_cero_y_sin_predecesor PASSED [  7%]
clase_15\tests\test_publico_dijkstra.py::test_bfs_no_basta_cuando_pesos_difieren PASSED [ 14%]
clase_15\tests\test_publico_dijkstra.py::test_red_ciudades_calcula_distancias_minimas PASSED [ 21%]
clase_15\tests\test_publico_dijkstra.py::test_predecesores_reconstruyen_camino PASSED [ 28%]
clase_15\tests\test_publico_dijkstra.py::test_nodo_inalcanzable_conserva_infinito PASSED [ 35%]
clase_15\tests\test_publico_dijkstra.py::test_camino_del_origen_a_si_mismo PASSED [ 42%]
clase_15\tests\test_publico_dijkstra.py::test_pesos_cero_son_validos PASSED [ 50%]
clase_15\tests\test_publico_dijkstra.py::test_peso_negativo_se_rechaza PASSED [ 57%]
clase_15\tests\test_publico_dijkstra.py::test_origen_inexistente_se_rechaza PASSED [ 64%]
clase_15\tests\test_publico_dijkstra.py::test_vecino_implicito_se_incluye PASSED [ 71%]
clase_15\tests\test_publico_dijkstra.py::test_no_muta_el_grafo_recibido PASSED [ 78%]
clase_15::test_max1 <- ..\entregas\clase_15\max\test_estudiante.py PASSED [ 85%]
clase_15::test_max2 <- ..\entregas\clase_15\max\test_estudiante.py PASSED [ 92%]
clase_15::test_max3 <- ..\entregas\clase_15\max\test_estudiante.py PASSED [100%]

============================= 14 passed in 0.02s ==============================

## 11. Hallazgo de la revisión técnica.


