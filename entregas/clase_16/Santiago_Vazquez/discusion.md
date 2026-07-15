

## Diferencia entre algoritmo correcto y función robusta.

El algoritmo correcto es un concepto matemático que asume datos perfectos; la función robusta es software real que valida tipos de entrada, previene la mutación de datos ajenos y lanza excepciones descriptivas ante fallos en producción.

## Razón de separar normalización.

Mantiene el núcleo de Dijkstra enfocado únicamente en optimizar distancias  y permite probar, depurar o reutilizar la lógica de limpieza de datos de forma independiente sin ensuciar el bucle principal.

## Mapping/Sequence frente a dict/list.

Mapping y Sequence son interfaces abstractas que permiten al usuario pasar cualquier estructura compatible (como defaultdict o tuplas), mientras que dict y list acoplan rígidamente tu código a tipos de datos concretos.

## TypeError frente a ValueError.

Lanzas TypeError cuando te pasan un tipo de dato incompatible con el que físicamente no se puede operar (como un string por peso), y ValueError cuando el tipo es correcto pero su valor viola las reglas lógicas (como un peso negativo).

## Bool, NaN e infinito.

Los booleanos se evalúan como enteros (1 y 0) corrompiendo cálculos de forma silenciosa; NaN destruye las comparaciones del heap arruinando el orden de prioridad; e infinito actúa como el valor neutro inicial para buscar mínimos.

## Copia defensiva.

Duplicar el grafo de entrada evita efectos secundarios desastrosos, garantizando que tu función de consulta nunca altere, mutile o corrompa la estructura de datos original que el cliente necesita seguir usando en su aplicación.

## Vecino implícito.

Ocurre cuando un nodo es destino de una arista pero no está declarado como clave de origen; gestionarlo defensivamente evita que el programa falle con un KeyError al intentar explorar las salidas de nodos sumidero.

## Invariante de entradas obsoletas.

Consiste en descartar inmediatamente los nodos extraídos de la cola de prioridad cuya distancia sea mayor que el costo mínimo ya registrado, evitando procesar de manera redundante registros duplicados y desactualizados.

## Responsabilidades de reconstrucción.

Dijkstra solo debe calcular costos mínimos y registrar predecesores; reconstruir la ruta final es un problema diferente de búsqueda inversa (backtracking) que debe delegarse a una función auxiliar para no mezclar tareas.

## Matriz contrato–riesgo–prueba.

Es una técnica de diseño que conecta cada promesa documentada de tu función (contrato) con sus posibles fallos en el mundo real (riesgo) y los casos de prueba unitarios específicos para blindarla contra regresiones.

## Complejidad de normalización y Dijkstra.

La normalización toma tiempo lineal O(V + E) y Dijkstra O((V+E) log V); al sumarlas secuencialmente, el término superior domina, demostrando que robustecer el código con validaciones no penaliza el rendimiento asintótico.

## Operación dominante en BFS, Dijkstra, Kruskal y topológico.

Cada algoritmo se rige por su estructura clave: BFS por el encolado FIFO (O(1)), Dijkstra por extraer el mínimo del heap (O(log V)), Kruskal por Union-Find (O(alpha)) y el orden topológico por actualizar el grado de entrada.