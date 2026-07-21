# Discusion.md
1. Diferencia entre algoritmo correcto y función robusta.
Una función robusta respeta el contrato definido aún en casos límite.
2. Razón de separar normalización.
Tener una copia a prueba de errores sin la necesidad de modificar los datos que se almacenaron en la variable original. Es una garantía secundaria de que los datos del usuario queden protegidos. 
3. Mapping/Sequence frente a dict/list.
Cada uno permite usar objetos de tipo 'clave : valor' e iterables de órden predeterminado y posibles repeticiones. En el notebook escribí un ejemplo en el que hablaba de un grafo implementado como una clase. Dicho grafo deja de ser solo un diccionario, pero funciona como un 'mapping'.
4. TypeError frente a ValueError.
TypeError - El objeto tiene un tipo/clase no deseada.
ValueError - El valor de ese objeto no es deseado. 
5. Bool, NaN e infinito.
Bool - Es realmente un subtipo de int. 
NaN - Es un float que aroja false en comparaciones numéricas.
Inf, -inf - Son floats. E.g. numero_cualquiera < inf == True y numero_cualquiera > -inf == True. 
6. Copia defensiva.
Es lo implementado con normalizar. Protege los datos almacenados por el usuario en la variable original. 
7. Vecino implícito.
Es un vecino con el cual puedes generar aristas si y sólo si éste es el destino. Como no ésta en el diccionario de predecesores ni es una clave del grafo, el uso de la copia defensiva lo añade como una clave para evitar 'KeyError'.
8. Invariante de entradas obsoletas.
Solo se queda la arista que tiene la menor distancia. 
9. Responsabilidades de reconstrucción.
No afectar la variable original, usar una copia defensiva contra los 'KeyError' o 'ValueError'. Debe asegurarse de que dijkstra pueda confiar en que los paramétros de la firma son válidos.
10. Matriz contrato–riesgo–prueba.
Ayuda a identificar las promesas de la función, ver que rasgo del contraro deben cumplir, los riesgos y finalmente con eso construir una prueba. 
11. Complejidad de normalización y Dijkstra.
Normalizar : O(V+E). Dijkstra : O((V+E)log(v))
12. Operación dominante en BFS, Dijkstra, Kruskal y topológico.
Exploración de vecinos y aristas. 