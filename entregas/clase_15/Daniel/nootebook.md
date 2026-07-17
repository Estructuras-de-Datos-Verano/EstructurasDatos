# Clase 15: Caminos mínimos y Dijkstra

## Pregunta inicial

¿Cómo encontramos el camino de menor costo cuando las aristas no cuestan lo mismo?
- puede ser con un arbol bien balanceado un AVL

**Responde esta pregunta en notebook.md.**

## 1. Por qué BFS ya no basta


**Pregunta adicional:** ¿Qué camino elegiría una estrategia que solo compara niveles y cuál debería elegir si optimizamos costo total?
- el que tiene menos pasos aunque cueste mas memoria

**Responde esta pregunta en notebook.md.**

**Pregunta:** ¿Por qué contar aristas ya no es suficiente en un grafo ponderado?
- por que al ser ponderado tiene mas peso de un lado y no siempre va a ser el acimo mas eficiente.

**Responde esta pregunta en notebook.md.**

## 2. Recordatorio de BFS


**Pregunta:** ¿En qué condición BFS sí garantiza caminos de costo mínimo?
- cuando todos los nodos valen lo mismo.

**Responde esta pregunta en notebook.md.**

## 3. Red de ciudades conductora


**Actividad manual:** enumera al menos dos caminos de A a E y suma sus pesos. No decidas todavía cuál usará el algoritmo.
1st A -> B -> D -> E = 8
2ND A -> C -> E = 8

**Responde esta pregunta en notebook.md.**


**Pregunta:** ¿Qué representan nodos, aristas y pesos en esta red?
- pasos po donde puede pasar con distintos costos por pasar por cada uno

**Responde esta pregunta en notebook.md.**

## 4. Distancias tentativas


**Pregunta:** ¿Qué significa infinito en la tabla de distancias?
- que no conocemos un camino

**Responde esta pregunta en notebook.md.**

## 5. Relajación



**Pregunta:** ¿Qué tres valores comparamos al relajar una arista?
el valor de la arista, si existe un camino y si es el mas economico en cuatos a costo

**Responde esta pregunta en notebook.md.**

## 6. Mejoras sucesivas



**Pregunta:** ¿Por qué actualizar una distancia no obliga a borrar inmediatamente su entrada anterior del heap?
- por que simplemente si llega una mas optima ignora a la anterior y se chingó. 

**Responde esta pregunta en notebook.md.**

## 7. Descubrimiento de la cola de prioridad



**Pregunta:** ¿Qué componente del par funciona como prioridad y cuál como elemento?
- la distancia es la prioridad y el nodo el elemento

**Responde esta pregunta en notebook.md.**


## 8. Algoritmo de Dijkstra



**Pregunta:** ¿Qué problema resuelve Dijkstra y qué restricción tienen los pesos?
- es un arbol el cual tiene prioridades de acuerdo al costo de sus nodos y justo trata de encontrar el camino con menos peso

**Responde esta pregunta en notebook.md.**

## 9. Pseudocódigo y entradas obsoletas



**Actividad:** subraya en el pseudocódigo las tres operaciones que dependen directamente de la Clase 14.
distancia[origen] = 0
candidata = distancia[actual] + peso
distancia[vecino] = candidata


**Responde esta pregunta en notebook.md.**

**Pregunta:** ¿En qué momento se ignora una entrada obsoleta?
cuando extraemos el minimo y asi trabajamos sobre eso.

**Responde esta pregunta en notebook.md.**

## 10. Recorrido manual mínimo


**Pregunta:** ¿Cuál es el orden de extracción vigente en el ejemplo mínimo?
[0,1,3,4]

**Responde esta pregunta en notebook.md.**

## 11. Recorrido manual intermedio
| Extracción vigente | Mejoras producidas | Distancias después | Predecesores que cambian |
| --- | --- | --- | --- |
| `(0,A)` | B=4, C=1 | A0 B4 C1 D∞ E∞ | B←A, C←A |
| `(1,C)` | B=3, D=6 | A0 B3 C1 D6 E∞ | B←C, D←C |
| `(3,B)` |B=3 D=4 |A0 B3 C1 D4 E∞ |A-B Y C-B |
| `(4,D)` |D=4 E=7 |A0 B3 C1 D4 E7 |C-D A-D |
| `(7,E)` |E=7 A=0 |A0 B3 C1 D4 E7 |C-E A-E|



**Responde esta pregunta en notebook.md.**


**Pregunta:** ¿Cuáles son las distancias finales desde A en la red conductora?
4 y 1

**Responde esta pregunta en notebook.md.**

## 12. Reconstrucción del camino



**Pregunta:** ¿Por qué recorremos predecesores desde el destino y después invertimos?
- porque la secuencia se obtuvo de destino a origen, así que la invertimos:

**Responde esta pregunta en notebook.md.**

## 13. Visualización interactiva



**Actividad:** en “Entradas obsoletas”, pausa antes de extraer `(10,B)` y predice la decisión.
- predigo que ahora va a dejar en el camino que estaba antes por que ahora la b vale mas 

**Responde esta pregunta en notebook.md.**


**Pregunta:** ¿Qué tres representaciones deben permanecer sincronizadas en cada paso?
- El mapa visual: Para ver qué camino estamos siguiendo y qué nodo está activo en ese momento.  La tabla de control: Donde anotamos a lápiz las distancias provisionales y de qué nodo venimos.  El heap (cola): La lista de tareas pendientes, ordenada de lo más barato a lo más caro. 

**Responde esta pregunta en notebook.md.**

## 14. Implementación



**Pregunta:** ¿Qué responsabilidad tiene cada una de las tres funciones de la entrega?
- dijkstra: Es el motor; calcula los costos mínimos y quién es el predecesor de cada nodo desde el origen.  reconstruir_camino: Sigue el rastro de predecesores hacia atrás (desde el destino al origen) y lo voltea para darnos la ruta en orden.  camino_minimo: Coordina todo; llama a las dos funciones anteriores para darnos el costo total y la lista de paradas.  

**Responde esta pregunta en notebook.md.**

## 15. Complejidad


**Pregunta:** ¿De dónde proviene el factor logarítmico de Dijkstra con heap?
 
- Viene de meter y sacar nodos del heap. Como esta estructura se acomoda sola para mantener el camino más barato en la cima, cada operación de agregar o quitar elementos nos cuesta un paso de reordenamiento equivalente a O(log V)

**Responde esta pregunta en notebook.md.**

## 16. Problema guiado: entrega urgente


**Pregunta:** ¿Cuál es el costo y camino mínimo de A a E en la red conductora?
Costo: 7  Camino: ['A', 'C', 'B', 'D', 'E']  (Dar esta vuelta es mucho más barato que ir directo por A a B a E, que costaría 11).

**Responde esta pregunta en notebook.md.**

## 17. Limitaciones y pesos negativos



**Pregunta:** ¿Por qué una arista negativa rompe la decisión codiciosa de Dijkstra?
Porque Dijkstra asume que conforme avanzas por el mapa, el costo del viaje solo puede subir. Dijkstra ya habrá cerrado los nodos anteriores dándolos por definitivos y nunca regresará a corregir la ruta.


## 18. Pruebas y revisión técnica



**Pregunta adicional:** ¿Qué afirmaciones comprobarías además del costo mínimo para validar la reconstrucción?
Que el camino empiece en el origen y termine en el destino.

Que todas las calles de la ruta existan de verdad en el mapa original.

Que no haya bucles infinitos (pasar por el mismo nodo dos veces).

Que la suma real de los pesos del camino coincida con el costo prometido.

**Responde esta pregunta en notebook.md.**


**Pregunta:** ¿Qué caso de prueba demuestra que manejamos entradas obsoletas correctamente?
- Un caso donde tengas una ruta directa cara (A -> B de costo 10) y una ruta indirecta barata (A -> C -> B de costo 3).  El heap tendrá guardadas ambas opciones para llegar a B. El código debe usar la de 3 y, al sacar la de 10, detectar que ya conoce un camino mejor e ignorarla sin volver a procesarla.  


**Responde esta pregunta en notebook.md.**

## 19. Práctica adicional



**Pregunta:** ¿Qué operación dominante indica que un problema puede resolverse con Dijkstra?
Tener que buscar la ruta acumulada más barata en un mapa con costos no negativos, eligiendo siempre la opción más corta y prometedora que tengamos a la mano.  

**Responde esta pregunta en notebook.md.**

## 20. Cierre




### Comprueba tu comprensión

**Pregunta:** ¿Qué cadena de decisiones transforma el problema ponderado en Dijkstra?
Costos reales: Queremos sumar distancias o dinero en lugar de solo contar paradas. 
Tabla de apuntes: Creamos un registro de costos provisionales y predecesores para no perdernos. 
Relajación: Comparamos caminos constantemente y nos quedamos con el más barato.  
Estrategia codiciosa: Decidimos explorar primero el camino pendiente más económico.  
Min-heap: Usamos esta estructura para encontrar ese mínimo al instante.  
Pesos no negativos: Prohibimos los costos negativos para asegurar que la estrategia de no mirar atrás funcione. 

**Responde esta pregunta en notebook.md.**




