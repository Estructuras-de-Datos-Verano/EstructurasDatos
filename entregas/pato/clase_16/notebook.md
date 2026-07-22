# Clase 16: Notebook
#### Nombre: Patricio Navarro

## Pregunta inicial
¿Cómo se convierte en una implementación confiable, reutilizable y testeable?
- Cuando los contratos que se establecieron y el comportamiento esperado si es lo que se busca en el código y se utilizan métodos o lógica de otras implementaciones similares que ya son confiables, reutilizables y que fueron testeadas.

## De algoritmo correcto a software confiable
¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?
- Que no solo sea una traducción.
- Que el código sea robusto.
- Que tenga claras y cumpla las rpomesas que hace.

## Un orden profesional de lectura
¿Por qué conviene leer firma y docstring antes que el while principal?
- Para saber por qué necesitas un while, y qué es lo que tiene que hacer el programa mientras está en el ciclo.
- Entender el comportamiento que buscas antes que el código en sí.

## Tipos como decisiones de diseño
¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?
- Que aceptar mapping/sequence te habla de objetos con lo que espera trabajr, con pares de clave, valor o con tuplas. Mientras que exigir dict/list te habla de un objeto específico, limitando más con lo que se puede trabajar.

## Normalización y copia defensiva
¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?
- Que se alteren los valores de la entrada.
- Reduce el número de condiciones que se deben validar y por tanto la posibilidad de un error en la lógica.

## TypeError y ValueError cuentan historias distintas
¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?
- TypeError cuando el tipo de valor no es correcto, no es un mapping o están intercambiadas las posiciones de los pesos y los strings.
- ValueError cuando viola las condiciones, el dominio del problema, como el que el peso sea negativo o que sea infinito, etc.

## Bool, Nan e infinito
¿Por qué True y NaN requieren comprobaciones específicas?
- Porque son instancias de `int` y de `float`, entonces se podrían aceptar pero romerían el comportamiento, por lo que se deben manejar sus casos de antemano.

## Vecinos implícitos y representación total
¿Qué fallo evita resultado.setdefault(vecino, [])?
- Busca todos los vecinos de una entrada, y si no lo encuentra lo agrega, así se evitan hoyos y errores de lectura.

## El contrato de Dijkstra
¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?
- Para no tener que reptir dos veces la función buscando distintos resultados, y así también devolver más información en una sola llamada.

## Estado inicial y tablas totales
¿Qué invariante establecen las comprensiones antes del while?
- Que cada clave exista en ambos mapas.

## El guard clause de entradas obsoletas
¿Qué garantiza la comparación inmediatamente posterior a heappop?
- Que si la primer distancia que se extrae es igual a la segunda distancia, entonces la puedes quitar, porque son las mismas y una de ellas ya no te sirve realmente. Si son distintas entonces sí conviene seguir buscando en las aristas.

## Relajación y actualización atómica
¿Qué datos deben actualizarse juntos cuando una candidata mejora?
- El costo.
- Los predecesores.
- La distancia de los vecinos.

## Reconstruir es otro problema 
¿Qué diferencia hay entre destino inalcanzable y destino ausente?
- Si es inalcanzable devuele `[]` para marcar que no hayuna ruta que te pueda llear hasta ahí, en cambio si es ausente entonces marca un KeyError pues seguramente no está en la lista.

## Coordinación sin duplicación
¿Qué responsabilidades delega camino_minimo?
- Reconstruir el camino.
- Relajación.
- Recorrer el grafo.

## Del contrato a una matriz de pruebas
¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?
- Que sea alcanzable el destino, la lista de predecesores.

## Auditoría de una implementación frágil
**Actividad**
| Contrato | Entrada mínima | Observado | Esperado | Test propuesto |
| --- | --- | --- | --- | --- |
| **peso no negativo** | `{"A": [("B", -1)], "B": []}`, origen `"A"` | Se ejecuta y registra un costo inválido `{'A': 0.0, 'B': -1.0}`. | Detención inmediata con `ValueError`. | `test_rechaza_pesos_negativos()` |
| **vecino implícito** | `{"A": [("B", 5)]}`, origen `"A"` | Falla con `KeyError: 'B'` al intentar leer `distancias["B"]`. | Ejecución exitosa con `distancias["B"] == 5.0`. | `test_vecino_implicito_se_incluye()` |
| **origen válido** | `{"A": [("B", 1)]}`, origen `"X"` | Ejecuta y asigna `{"X": 0.0}`, dejando a `"A"` inalcanzable. | Detención inmediata con `KeyError`. | `test_origen_ausente_se_rechaza()` |
| **entrada obsoleta** | `{"A": [("B", 10), ("C", 1)], "C": [("B", 1)]}`, origen `"A"` | Procesa inútilmente la tupla `(10.0, "B")` (revisa sus vecinos 2 veces). | Descarta la tupla antigua y revisa vecinos de "B" solo 1 vez. | `test_ignora_entradas_obsoletas()` |
| **representación** | `{"A": [("B", True)]}`, origen `"A"` | El booleano se opera matemáticamente y se acepta como costo `1.0`. | Detención con `TypeError` indicando tipo inválido. | `test_rechaza_peso_booleano()` |

¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?
- Origen ausente.
- Pesos negativos.
- Entradas obsoletas.

## Clínica de depuración
¿Qué información mínima debe contener un reporte de fallo útil?
- Prueba que falló.
- Donde en el código falló.
- El tipo de error.
- Posible solución.

## Revisión profesional de código
¿Qué hace que un comentario de revisión sea accionable y verificable?
- Que no solo lo califique, sino que además dé razones y explique por qué esa calificación, posibles mejoras o problemas, y un caso donde se ejemplifique.

## Complejidad sin perder robustez
¿La normalización cambia la complejidad asintótica de Dijkstra?
- No, no diría que se mantiene igual pero el cambio es mínimo porque se aborsbe en otras operaciones.

## Cuatro algoritmos, cuatro operaciones dominantes
¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?
- cola FIFO para el menor número de aristas, porque el primer nodo que enceuntra lo saca y así va contando.
- min-heap para menor suma no negativa porque así puedes ir sacando los mínimos en orden de prioridad.
- ordenamiento + conjuntos disjuntos, para así un árbol expandirlo sin repetir información o intersectar.
- grafos + cola para respetar dependencias.

## Cierre
¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?
- Cuando se hace con robustez, con copias defensivas, manejo de errores y excepciones, condiciones claras y pruebas.

