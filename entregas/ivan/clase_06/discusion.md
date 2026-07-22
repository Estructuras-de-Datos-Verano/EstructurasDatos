1. Lectura estratégica.
Tenemos un problema en el que usando una algoritmo simple para resolverlo (con listas y loop) tiene un límite de tamaño y va a fallar. Por eso nos surge naturalmente la opción de usar una estructura de datos que no requiera mover de posicion todos los elementos y que permita solo borrar el que esta a la izquierda.
2. Elección de estructura.
Deque es un buen candidato porque tiene la opción de popleft en vez de pop(i) y además permite tener colas. Se me ocurrió primero solo usar listas, pero vi que la complejidad iba a ser muy grande. 
3. Diseño del algoritmo.
Ya pensando en el deque como un círculo: 
INICIO
Validar(n)
Inicializar el vivos= deque(range(1,n+1)) y una lista vacía
Mientras vivos:
    Si hay un único vivo:
        Se elimina y añade a la lista de eliminados
    Si hay más:
        El primero lo movemos a la cola
        El segundo le hacemos popleft
        Lo metemos en la lista de eliminados
Regrsa lista de eliminados
4. Pruebas.
Todas pasaron exitosamente. La prueba de validar_n_rechaza_cero verifica que la longitud no sea vacia. Solo faltó verificar que este algoritmo si pueda superar el techo n = 2x10^5
5. Complejidad.
Lineal. Deque permite hacer operaciones con colas o eliminar en cualquier sentido con complejidad constante. Como hacemos operaciones por cada elemento del deque, la complejidad depende de la longitud de este. 
¿Cuántos niños se eliminan? Se eliminan exactamente n niños. El ciclo principal del algoritmo no se detiene hasta que la estructura que contiene a los niños vivos quede completamente vacía. Esto nos da una Complejidad Temporal de $\mathcal{O}(n)$ (lineal). El tiempo de ejecución del programa crecerá en proporción directa al tamaño de la entrada.
¿Qué estructura permite que esas operaciones sean eficientes? La estructura de datos que hace que este algoritmo sea óptimo es el deque del módulo collections de Python.
¿Por qué es eficiente? Porque el deque es como una lista doble con colas. ¿Cuánta memoria adicional se usa?Notación Big-O (Espacio): $\mathcal{O}(n)$ (lineal).El algoritmo requiere almacenar a los niños en memoria durante su ejecución. Específicamente, utilizas dos estructuras adicionales:La cola vivos, que al inicio del programa almacena exactamente los n elementos. La lista eliminados, que al final del programa almacena los n elementos en su nuevo orden.Dado que el espacio físico que ocupan estas estructuras en la memoria RAM del computador escala de forma estrictamente proporcional a la cantidad de niños introducidos, la complejidad espacial es lineal.
6. Contraste.
Si elegiría deque aún, con un probema ligeramente distinto solo haría falta cambiar la lógica dentro del while.
7. Pregunta abierta.
¿ Cual podría ser ese problema ligeramente distinto?