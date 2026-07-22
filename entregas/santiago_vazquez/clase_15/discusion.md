## Diferencia entre distancia por aristas y por pesos.

Establecer distancias infinitas provisionales, aplicar relajaciones de aristas basadas en acumulaciones de costo y utilizar una cola de prioridad para procesar siempre el camino más prometedor.

## Significado de distancia tentativa.

Es la estimación provisional del costo mínimo hacia un nodo. Comienza en infinito para nodos no descubiertos y disminuye a medida que se relajan las aristas. 

## Relajación con un ejemplo numérico.

Si la distancia tentativa actual al nodo $U$ es $3$, y existe una arista dirigida de U a V con peso 2, la distancia candidata para V es 3 + 2 = 5. Si la distancia tentativa guardada en V era 9, se actualiza a 5 por ser menor.

## Razón para usar min-heap.

Permite obtener el nodo con la menor distancia acumulada conocida en tiempo constante O(1) y reestructurar la prioridad en tiempo logarítmico O(log V), garantizando la estrategia codiciosa.

## Entrada obsoleta y eliminación perezosa.

Cuando un nodo se actualiza, se inserta una nueva tupla (nueva_distancia, nodo) en el heap. La tupla anterior se queda ahí; cuando eventualmente es extraída por heappop, se valida contra el diccionario y se ignora perezosamente si su distancia es mayor.

## Reconstrucción mediante predecesores.

Consiste en tomar el diccionario de predecesores e iterar hacia atrás partiendo desde el nodo destino hasta alcanzar el origen. Al final, se invierte la lista resultante para obtener el sentido correcto.

## Complejidad temporal y espacial.

La complejidad temporal con min-heap es de O((V + E) log V), donde cada arista puede provocar una inserción en el heap y cada nodo una extracción. La complejidad espacial es O(V + E) para almacenar las estructuras auxiliares y el grafo.

## Restricción de pesos no negativos.

Si existieran aristas negativas, Dijkstra podría cerrar un nodo con un costo subóptimo definitivo, fallando en su principio codicioso al no poder recalcular caminos ya procesados.

## Caso donde BFS falla.

En un grafo con aristas A a B de peso 10 y una ruta alternativa A a C a B con pesos 1 y 2 respectivamente. BFS escogerá el camino de una arista (A a B) con costo 10, ignorando la ruta óptima de costo 3.

## Evidencia de tus pruebas.

Se diseñaron escenarios robustos evaluando múltiples actualizaciones al mismo nodo, aislamiento de componentes y selección correcta sobre aristas directas costosas.

## Hallazgo de la revisión técnica.

Se confirmó la importancia de implementar la guarda if dist_actual != distancias[u]: continue inmediatamente después del heappop para evitar reprocesamientos innecesarios y optimizar el rendimiento.