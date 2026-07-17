## Diferencia entre algoritmo correcto y función robusta.

Un algoritmo correcto puede funcionar en general, pero una función robusta se blinda contra casos que podríamos no haber previsto.

## Razón de separar normalización.

Separar la normalización permite tenerla aparte, y aplicar en general.

## Mapping/Sequence frente a dict/list.

Mapping y Secuence nos permiten acceder a claves, sin ser necesariamente un diccionario, siendo más versátiles.

## TypeError frente a ValueError.

TypeError verifica la clase: int, str, list... Value, el valor, como que un número sea positivo.

## Bool, NaN e infinito.

Bool, NaN e infinito son similares a ints, pero funcionan distinto. Infinito, por ejemplo, es parte de la librería math de python.

## Copia defensiva.

Una copia defensiva trabaja con una réplica del grafo original, al que no se modifica, y valida todo lo necesario para que fluya correctamente.

## Vecino implícito.

Vecino implícito es una de las cosas que debemos considerar al blindar la función. Si no es robusta, no podrá incluir los vecinos implícitos. Se romperá si no hay la clave.

## Invariante de entradas obsoletas.

No hay que apresurarse a borrar entradas obsoletas. De ahí, eliminación perezosa, por ejemplo.

## Responsabilidades de reconstrucción.

Reconstruir ya no depende de dijkstra, sino de recontruir camino. Esta fucnión aplica dijkstra internamente para que funcione bien.

## Matriz contrato–riesgo–prueba.

Es necesario probar el código y detectar riesgos para que no se rompa cuando lo use alguien más.

## Complejidad de normalización y Dijkstra.

La complejidad no cambia mucho, pero aumenta al hacer más operaciones.

## Operación dominante en BFS, Dijkstra, Kruskal y topológico.

FIFO, min-heap, ordenamiento + conjuntos disjuntos, grados + cola, respectivamente. Lo que necesite cada caso específico determina qué algoritmo usamos.