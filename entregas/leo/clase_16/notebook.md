# Notebook Clase 16 - Leonardo Daniel Arenas Serafín

#### ¿Cómo se convierte en una implementación confiable, reutilizable y testeable?
Se convierte cuando nos enfocamos en hacer una implementación que detecte errores, que sea asbtracta y que sea fácil de comprender. 

## 1. De algoritmo correcto a software confiable

#### ¿Qué responsabilidades aparecen al pasar del pseudocódigo a una función reutilizable?
Que debemos también revisar que se detecten errores y que acepte cualquier tipo de entrada mínimas diferencias.

## 2. Un orden profesional de lectura

#### ¿Por qué conviene leer firma y docstring antes que el while principal?
Porque es mejor primero entender qué busca el algoritmo para después revisar si está bien implementado que primero revisar sin saber qué busca.

## 3. Tipos como decisiones de dis

#### ¿Qué diferencia práctica existe entre aceptar Mapping/Sequence y exigir dict/list?
Que Mapping acepta cualquier estrutura que tenga elementos relacionados de tipo llave-valor, mientras que dict solo acepta diccionarios. De la misma forma, Sequence acepta todas las estructuras que mantengan orden de índices y list solo acepta listas. Esto permite mayor libertad para aplicar el algoritmo.

## 4. Normalización y copia defensiva

#### ¿Qué dos problemas resuelve _normalizar_grafo antes de ejecutar Dijkstra?
Resuelve el problema de que si no viene una arista explícita en el diccionario que sabemos que está ahí, Dijkstra saltaría error, pero de esta forma se da por hecho que ahí está, también de esta forma evita que hayan dobles revisiones. También verifica que las fronteras del los inputs estén correctas, detecta errores.

## 5. TypeError y ValueError cuentan historias distintas

#### ¿Cuándo corresponde TypeError y cuándo ValueError en esta implementación?
Corresponde TypeError cuando el grafo no es un Mapping con llaves str y valores Sequence. Corresponde  ValueError cuando los pesos son negativos.

## 6. Bool, NaN e infinito

#### ¿Por qué True y NaN requieren comprobaciones específicas?
Porque True se puede confundir al ser una instancia de int y NaN no puede ser comparable con floats.

## 7. Vecinos implícitos y representación total

#### ¿Qué fallo evita resultado.setdefault(vecino, [])?
Evita que no se detecten aristas implícitas en el grafo, como en una lista de adyacencia dirigida.

## 8. El contrato de dijkstra

#### ¿Por qué dijkstra devuelve dos diccionarios en lugar de un camino?
Porque dijkstra no quiere saber cuál es el camino mínimo para llegar de un lugar a otro, sino que simplemente busca mappear el grafo para saber cuales son todos los caminos y así otra función pueda encontrar el camino mínimo para cualesquiera origen y destino. Así evitamos hacer trabajos dobles al buscar dos caminos distintos.

## 9. Estado inicial y tablas totales

#### ¿Qué invariante establecen las comprensiones antes del while?
Que todos los nodos aparezcan con una distancia infinita pues todavía no han sido analizadas. Y que todos los nodos tengas predecesores None pues todavía no sabemos nada de ellos. Así inciliazamos el heap con el origen con distancia 0.0 pues no tiene costo iniciar.

## 10. El guard clause de entradas obsoletas

#### ¿Qué garantiza la comparación inmediatamente posterior a heappop?
Poder saber si el camino en donde estamos cambia en algo o es obsoleto.

## 11. Relajación y actualización atómica


#### ¿Qué datos deben actualizarse juntos cuando una candidata mejora?
Se debe dde actualizar la distancia del camino hasta el momento, es decir, la candidata. Se debe de actualizar el elemento en donde ahora estamos y se debe de actualizar este par en el heap para continuar los caminos y que no se haga obsoleto inmediatamente.


## 12. Reconstruir es otro problema

#### ¿Qué diferencia hay entre destino inalcanzable y destino ausente?
Un destino inalcanzable se da cuando entramos en un bucle que continua sin interrupción pero que nunca llega al destino esperado, pero siempre hay camino. Un destino ausente es cuando de plano el nodo que buscamos no está en el grafo.

## 13. Coordinación sin duplicación

#### ¿Qué responsabilidades delega camino_minimo?
No tiene responsabilidades con el análisis de los caminos. Simplemente dice cuál es el camino mínimo, lo único que tiene que hacer es saber detectar si es que no existe el destino y lanzar un error o lanzar una lista vacía si es que el destino es inalcanzable.

## 14. Del contrato a una matriz de pruebas

#### ¿Qué dimensión del contrato no se verifica al probar únicamente el costo final?
No se revisa que los pesos sean int o floats: TypeError. No se revisa que los pesos sean negativos: ValueError. No verifica que stén los vecinos implícitos. Los grafos solamente pueden ser diccionarios y sus valores listas, lo que restringe la frontera. No verifica que el origen se encuentre dentro del grafo.

| Contrato | Entrada mínima | Observado | Esperado | Test propuesto |
| --- | --- | --- | --- | --- |
| peso no negativo | 0.0 | int/float | < 0 | if peso < 0: raise ValuError |
| vecino implícito | [] | list | nodo: [vecino implícito] | if vecino not in grafo.keys(): grafo[vecino] = [] |
| origen válido | origen: [] | [] | origen: [] | if origen not in grafo.keys(): raise ValueError |
| entrada obsoleta | [] | [] | [] | If grafo[nodo] == []: continue |
| representación | nodo: [] | key: value | nodo: [vecinos]  | if grafo not mapping[str, sequence(str, float)]: raise TypeEror |

## 15. Auditoría de una implementación frágil

#### ¿Qué tres fallos reproducibles encuentras en dijkstra_para_revisar?
No valida que los pesos sean int o float y que sean no negativos. No incluye vecinos implícitos. Procesa entradas obsoletas.

## 16. Clínica de depuración

#### ¿Qué información mínima debe contener un reporte de fallo útil?
Un reporte útil incluye comando, entrada, esperado, observado y ubicación probable

## 17. Revisión profesional de código

#### ¿Qué hace que un comentario de revisión sea accionable y verificable?
Que expliqué cuál fue el error o la fortaleza y describa por qué es esto, diciendo que prueba pasa, que se acepta y qué cambia.

## 18. Complejidad sin perder robustez

#### ¿La normalización cambia la complejidad asintótica de Dijkstra?
Sí, pues se acerca más a ser logarítmica que lineal.

## 19. Cuatro algoritmos, cuatro operaciones dominantes

#### ¿Qué estructura auxiliar se deriva de la operación dominante en cada algoritmo del cierre?
- BFS: cola FIFO
- Dijkstra: cola de prioridad. Heap
- Kruskal: ordenamiento y conjunos ajenos
- Topológico: grados y colas

## 20. Cierre

#### ¿Qué cadena de lectura convierte una implementación en evidencia de confiabilidad?
Una cadena que valide los tipos de entrada y sus valores, que entienda qué es lo que hace el código y complemente par evitar bucles o errores que no deberían ser.