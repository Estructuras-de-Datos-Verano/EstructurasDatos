# José Daniel Molina Carrillo
# Clase 16: Implementación robusta de Dijkstra

## Pregunta inicial

Ya entendemos la idea de Dijkstra. ¿Cómo se convierte en una implementación confiable, reutilizable y testeable?
- Se vuelve confiable cuando defines con total claridad qué tipo de datos va a recibir, cómo va a reaccionar si le pasas algo incorrecto y cuando separas la lógica de calcular las distancias de la lógica de reconstruir la ruta final.

¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?
- En el pseudocódigo asumes que todo el camino está "limpio". Al programar de verdad, te toca validar que los datos que te den sean correctos, manejar los errores de forma clara, asegurar que no vas a modificar o "romper" los datos que el usuario te pasó, y garantizar que la función sirva para cualquier caso real, no solo para uno. 

¿Por qué conviene leer firma y docstring antes que el while principal? 
- qué gasolina acepta (entradas), qué velocidad alcanza (salidas) y qué garantías te da (contrato). Si no entiendes el objetivo, el código del bucle no tendrá sentido.

¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list? 
- Mapping y Sequence permiten que tu código sea flexible y acepte más tipos de datos que se comporten como listas o diccionarios.

¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra? 
- Filtra datos inválidos y hace una copia propia del grafo para no alterar la información original del usuario.

¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación? 
- TypeError si el tipo de dato es incorrecto y ValueError si el tipo es correcto pero el valor no tiene sentido.

¿Por qué True y NaN requieren comprobaciones específicas?  
- Porque Python confunde True con el número 1, y NaN rompe las comparaciones y el orden de prioridad del heap.

¿Qué fallo evita resultado.setdefault(vecino, [])?  
- Evita que el programa falle por "clave inexistente" al procesar un nodo de llegada que no tiene salidas registradas.

¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?
- Porque calcula las rutas hacia todos los destinos a la vez; así tienes la información lista para armar cualquier ruta después.

¿Qué invariante establecen las comprensiones antes del while? 
- Que todos los nodos queden registrados desde el inicio como inalcanzables(con el simbolo de infinito) y sin un camino previo. 

¿Qué garantiza la comparación inmediatamente posterior a heappop? 
- Evita perder tiempo procesando rutas viejas o repetidas si ya encontramos un atajo mejor para ese nodo.

¿Qué datos deben actualizarse juntos cuando una candidata mejora?  
- La distancia más corta, el nodo previo y la nueva prioridad en la lista de pendientes.

¿Qué diferencia hay entre destino inalcanzable y destino ausente? 
- El inalcanzable existe pero no hay cómo llegar, el ausente no existe en el mapa,lanza error.  

¿Qué responsabilidades delega camino_minimo? 
- Delega calcular costos a dijkstra y trazar la ruta a reconstruir_camino, actuando solo como puente entre ambas.

¿Qué dimensión del contrato no se verifica al probar únicamente el costo final? 
- No valida si la ruta tomada fue la correcta, si se alteraron los datos del usuario o cómo reacciona el código ante fallas.

¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?  
- Acepta booleanos como distancias, no detecta si falta el origen y se rompe con destinos que no tienen salidas propias.


¿Qué información mínima debe contener un reporte de fallo útil?  
- Los datos de entrada, qué esperabas, qué pasó en su lugar y la línea exacta donde ocurrió el error.

¿Qué hace que un comentario de revisión sea accionable y verificable? 
- Que señale un error con un ejemplo concreto, explique el impacto y proponga la solución y una prueba exacta. 

¿La normalización cambia la complejidad asintótica de Dijkstra? 
- No, limpiar los datos al inicio es sumamente rápido y su costo queda absorbido por el algoritmo principal.

¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?  
- BFS usa cola FIFO, Dijkstra usa min-heap, Kruskal usa ordenamiento/conjuntos disjuntos y Topológico usa conteo de dependencias/cola. 

¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad? 
- Leer en orden: lo que promete , cómo se protege , cómo calcula  y cómo se defiende con pruebas.  