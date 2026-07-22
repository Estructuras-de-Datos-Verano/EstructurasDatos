# Notebook.md - José Iván Reyna Blanco
## Parte 1 - Auditoría antes de editar
**Tabla de auditoría (dijkstra_para_revisar.py)**
| Contrato | Entrada mínima | Observado | Esperado | Test propuesto |
| peso no negativo | `grafo={"A": [("B", -1)]}, origen="A"` | Algoritmo asume distancias correctas pero puede arrojar resultados erróneos o caer en bucle infinito si hay ciclos negativos. | Lanzar una excepción indicando que Dijkstra no admite pesos negativos. | `test_rechaza_aristas_con_peso_negativo()` |
| vecino implícito | `grafo={"A": [("B", 1)]}, origen="A"` | Lanza `KeyError: 'B'` al intentar leer `distancias[vecino]` porque el nodo destino no se declaró como clave del diccionario principal. | Inicializar al vecino en las distancias sobre la marcha o rechazar el grafo por estar malformado. | `test_maneja_vecino_destino_no_declarado()` |
| origen válido | `grafo={"A": []}, origen="X"` | Lanza `KeyError: 'X'` al intentar inicializar `distancias[origen] = 0.0`. | Lanzar una excepción de control con un mensaje claro especificando que el origen no pertenece al grafo. | `test_falla_suave_si_origen_no_existe()` |
| entrada obsoleta | `grafo={"A": [("B", 5), ("C", 1)], "C": [("B", 1)], "B": []}, origen="A"` | Extrae y procesa el nodo "B" dos veces del heap, afectando el rendimiento innecesariamente. | Comprobar `if distancia > distancias[actual]: continue` nada más extraer del heap para omitir el cálculo obsoleto. | `test_ignora_entradas_obsoletas_en_heap()` |
| representación | `grafo={"A": [("B", 2), ("C", 2)]}, origen="A"` | En caso de empate en distancia, el heap compara los strings de los nodos. Fallaría con `TypeError` si los nodos no fueran directamente comparables. | Usar una tupla de 3 elementos `(distancia, id_secuencia, nodo)` para garantizar un desempate estable. | `test_desempata_nodos_sin_comparar_ids()` |
**Auditoría**
***Hallazgo 1: Acepta pesos negativos***
1. Contrato incumplido: El algoritmo de Dijkstra exige que todos los pesos sean números no negativos.
2. Entrada mínima reproducible: grafo={"A": [("B", -2)]}, origen="A"
3. Resultado observado: El algoritmo procesa el peso negativo y calcula una distancia final de -2.0, lo cual invalida la premisa de Dijkstra y  puede generar bucles infinitos en grafos cíclicos.
4. Resultado esperado: La función debe rechazar la entrada y lanzar un ValueError.
5. Prueba automatizada:
```python
def test_rechaza_pesos_negativos():
    with pytest.raises(ValueError, match="no puede ser negativo"):
        dijkstra_para_revisar({"A": [("B", -1)]}, "A")
```
6. Cambio localizado: Agregar una validación dentro del bucle de descompresión de aristas: if peso < 0: raise ValueError("Peso negativo").
***Hallazgo 2: No incluye vecinos implícitos***
1. Contrato incumplido: Todo nodo destino debe existir como clave en los diccionarios de resultados, incluso si no tiene aristas de salida.
2. Entrada mínima reproducible: grafo={"A": [("B", 1.0)]}, origen="A"
3. Resultado observado: Lanza KeyError: 'B' al evaluar la condición if candidata < distancias[vecino]: porque "B" no fue inicializado en el diccionario de distancias.
4. Resultado esperado: Devolver { 'A': 0.0, 'B': 1.0 } en distancias y { 'A': None, 'B': 'A' } en predecesores.
5. Prueba automatizada:
```python
def test_maneja_vecinos_implicitos():
    dist, pred = dijkstra_para_revisar({"A": [("B", 1.0)]}, "A")
    assert dist["B"] == 1.0
    assert pred["B"] == "A"
```
6. Cambio localizado: Crear un paso de pre-procesamiento o llamar a una función _normalizar_grafo antes de crear los diccionarios para asegurar que todo vecino tenga una entrada [] en el grafo si no existe.
***Hallazgo 3: No rechaza origen ausente***
1. Contrato incumplido: El nodo de origen debe pertenecer explícitamente al grafo.
2. Entrada mínima reproducible: grafo={"A": []}, origen="X"
3. Resultado observado: Lanza KeyError: 'X' en la línea distancias[origen] = 0.0.
4. Resultado esperado: Fallar de manera controlada con un ValueError claro indicando que el nodo de partida es inválido.
5. Prueba automatizada:
```python
def test_falla_si_origen_no_existe():
    with pytest.raises(ValueError, match="origen no pertenece"):
        dijkstra_para_revisar({"A": []}, "X")
```
6. Cambio localizado: Agregar al principio de la función: if origen not in grafo: raise ValueError(...).
***Hallazgo 4: No valida tipos de datos y representaciones***
1. Contrato incumplido: Protección de tipo y desempate estable.
2. Entrada mínima: grafo={"A": [("B", True)]}, origen="A"
3. Resultado observado: Suma el booleano como si fuera 1.0. En empates, heapq asume que los nodos son strings comparables.
4. Resultado esperado: Lanzar TypeError.
5. Prueba automatizada:
```python
def test_rechaza_peso_booleano():
    with pytest.raises(TypeError):
        dijkstra_para_revisar({"A": [("B", True)]}, "A")
```
6. Cambio localizado: Validación estricta de tipos isinstance(peso, float) y not isinstance(peso, bool) en la fase de normalización.
### Comprueba tu comprehensión
**Pregunta:** ¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable? Lograr que el pseudocódigo no funcione sólo con ejemplos puntuales, sino que funcione en casos límite y que sea capaz de rechazar usos que no respeten un contrato exigido.
**Pregunta:** ¿Por qué conviene leer firma y docstring antes que el while principal? En este caso porque hay 'typos' como una coma extra a la derecha del último argumento y además porque desde la firma puede verse que no verifica pesos negativos y en el dosctring se ve que la función no está completa. En general, porque pueden haber errores de implementación desde antes de la primer línea de código. 
**Pregunta:** ¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list? Cada una permite usar objetos de tipo llave-valor o iterables con órden predeterminado y repeticiones sin necesidad de ser solo diccionarios y listas. Por ejemplo, cualquier implementación que herede el contrato mínimo de una clase abstracta 'GrafoAbstracto' se puede comportar como un diccionario, aunque para python sea un 'map' distinto. 
**Pregunta:** ¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?
1- Garantiza datos válidos: Revisa y limpia la entrada (comprueba que los pesos no sean negativos, que los tipos de datos sean correctos, etc) para que el algoritmo asuma que la información es segura.
2- Protege los datos originales (Copia defensiva): Crea un clon independiente del grafo (incluyendo sus listas internas) para que cualquier modificación que el algoritmo necesite hacer no altere la variable original.
**Pregunta:** ¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?
-TypeError: El objeto no es de la clase/tipo deseado.
-ValueError: El valor no está en un rango deseado. 
**Pregunta:** ¿Por qué True y NaN requieren comprobaciones específicas? Porque True es declase 'int' y NaN es un float que arroja siempre False en comparaciones. 
**Pregunta:** ¿Qué fallo evita resultado.setdefault(vecino, [])? Evita un error de tipo 'KeyError' durante el bucle de Dijkstra. Al asegurar que todos los nodos destino (incluso los que no tienen aristas de salida) existan como claves en el diccionario principal, se garantiza que el algoritmo no falle al intentar consultar sus vecinos o al intentar leer y actualizar su valor en los diccionarios de distancias y predecesores.
**Pregunta:** ¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino? La función calcula caminos mínimos a cualquier nodo posible. Se tiene entonces como output un 'tupple' de diccionarios, dónde uno contiene la distancia mínima para alcanzar cada vértice y otro el predecesor de cada vértice. Entonces con esos diccionarios es fácil fijar un destino, sumar las distancias mínimas asociadas a cada nodo en predecesores y devolver un camino con su peso total. 
**Pregunta:** ¿Qué invariante establecen las comprensiones antes del while? Cada clave interna existe en ambos mapas; `distancias[n]` es el menor costo descubierto hasta el momento; cada par del heap es una candidatura.
**Pregunta:** ¿Qué garantiza la comparación inmediatamente posterior a heappop? Que el último 'tupple' en el heap sea el mejor candidato hasta el momento. 
**Pregunta:** ¿Qué datos deben actualizarse juntos cuando una candidata mejora? La distancia, el predecesor y la última entrada del heap.
**Pregunta:** ¿Qué diferencia hay entre destino inalcanzable y destino ausente? Si el destino es inalcanzable -> '[]'. Si es ausente -> 'KeyError'.
**Pregunta:** ¿Qué responsabilidades delega camino_minimo? Cálculo, reconstrucción y coordinación. 
**Pregunta:** ¿Qué dimensión del contrato no se verifica al probar únicamente el costo final? Si solo pruebas el costo final (el diccionario de distancias), no estás verificando el camino o ruta (el diccionario de predecesores). El algoritmo podría calcular que llegar al destino cuesta 10, pero registrar una ruta completamente equivocada o con saltos inválidos. Además, al probar solo el resultado numérico, tampoco verificas promesas secundarias como la "no mutación" (asegurarte de que la variable original no fue alterada).
**Pregunta:** ¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar? Origen no existe, pesos negativos y pesos booleanos. 
**Pregunta:** ¿Qué información mínima debe contener un reporte de fallo útil? Comando, entrada, esperado, observado y ubicación probable.
**Pregunta:** ¿Qué hace que un comentario de revisión sea accionable y verificable? Enfoque -> Comportamiento -> Prueba sugerida -> Proponer cambio mínimo posible que respete el contrato. 
**Pregunta:** ¿La normalización cambia la complejidad asintótica de Dijkstra? No. Lo costoso es ejecutar el algoritmo. Normalizar realmente no añade complejidad adicional porque su complejidad es de menor órden que algo logarítmico. 
**Pregunta:** ¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre? Está tal cuál en la tabla. 
procesar por orden de descubrimiento - cola FIFO ; extraer menor distancia tentativa - min-heap ; 
unir componentes sin crear ciclo - ordenamiento + conjuntos disjuntos ; 
retirar nodos con grado de entrada cero - grados + cola ; 
**Pregunta:** ¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad? Igual. Contraro - Riesgo - Prueba mínima. 