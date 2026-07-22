# Discusión - Práctica 15 (Dijkstra)

**1. Diferencia entre distancia por aristas y por pesos.**
La distancia por aristas solo cuenta la cantidad de "saltos" o tramos físicos entre dos nodos (el enfoque de BFS). La distancia por pesos suma el "costo" o valor numérico de transitar esas aristas (tiempo, dinero, kilómetros), el cual es el enfoque de Dijkstra.

**2. Significado de distancia tentativa.**
Es el costo mínimo conocido *hasta el momento* para llegar a un nodo desde el origen. Se le llama "tentativa" porque mientras el algoritmo no haya extraído definitivamente ese nodo de la cola de prioridad, existe la posibilidad de encontrar un atajo más barato que reduzca ese valor.

**3. Relajación con un ejemplo numérico.**
Relajar es intentar mejorar la distancia a un destino pasando por un nodo intermedio recién descubierto. 
*Ejemplo:* Supongamos que la distancia conocida a `D` es 15. Luego extraemos `B`, cuya distancia desde el origen es 4. Revisamos la arista `B -> D` que tiene un peso de 2. La ruta candidata es 4 + 2 = 6. Como 6 es menor que 15, "relajamos" `D`: actualizamos su distancia a 6 y su predecesor pasa a ser `B`.

**4. Razón para usar min-heap.**
Se utiliza para extraer siempre, de forma rápida y eficiente, el nodo pendiente con la **menor distancia acumulada** (la mayor prioridad). Extraer el mínimo de un min-heap cuesta tiempo logarítmico, a diferencia de buscar linealmente en una lista, lo que haría al algoritmo muy lento.

**5. Entrada obsoleta y eliminación perezosa.**
Cuando relajamos un nodo y descubrimos un camino más barato, lo insertamos al min-heap con su nuevo costo, pero el registro viejo y más caro sigue ahí adentro. En lugar de hacer la operación costosa de buscar y borrar la entrada vieja del heap, hacemos "eliminación perezosa": la dejamos ahí, pero cuando finalmente es extraída, comparamos su costo con la tabla de distancias reales. Como el costo viejo ya no coincide con el mejor costo registrado, simplemente la ignoramos.

**6. Reconstrucción mediante predecesores.**
Dijkstra no guarda la ruta completa en cada paso, sino una "migaja de pan". Cada vez que mejora la distancia a un nodo, anota desde qué ciudad vecina llegó (su predecesor). Para reconstruir la ruta, empezamos en el nodo Destino y viajamos "hacia atrás" leyendo el diccionario de predecesores hasta llegar al Origen, y luego invertimos esa lista.

**7. Complejidad temporal y espacial.**
* **Temporal:** $O((V + E) \log V)$ donde V son los vértices (nodos) y E las aristas. Esto se debe a que revisamos cada vértice y cada arista, y usamos el heap (cuyas operaciones cuestan $\log V$) para ordenarlos.
* **Espacial:** $O(V + E)$ porque necesitamos almacenar en memoria el grafo completo (lista de adyacencia), los diccionarios de distancias y predecesores, y la propia cola de prioridad.

**8. Restricción de pesos no negativos.**
Dijkstra asume que, una vez que procesas la distancia mínima pendiente, esta es definitiva porque seguir avanzando por más aristas siempre sumará más costo (o al menos se mantendrá igual). Una arista de peso negativo rompería esta asunción, porque un camino que parecía caro y se había descartado podría volver a ser el más barato en el futuro, arruinando los cálculos ya confirmados.

**9. Caso donde BFS falla.**
Imagina que de `A` a `D` hay un tramo directo muy congestionado de peso 10. Pero también puedes ir `A -> B` (peso 1) y luego `B -> D` (peso 1), total 2. BFS procesará por niveles y elegirá el camino directo `A -> D` porque solo toma "1 arista", dándonos una ruta con costo 10 y perdiendo el camino de costo 2.

**10. Evidencia de tus pruebas.**
*(Pega aquí un resumen o la salida exitosa de pytest al ejecutar tus pruebas personalizadas)*

**11. Hallazgo de la revisión técnica.**
*(Anota aquí la observación accionable que te dejó tu compañero al revisar tu rama, o la que tú le dejaste al compañero)*