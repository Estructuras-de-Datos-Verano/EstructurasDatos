# seccion 1
    Un ejemplo de como en una lista una busqueda puede ser costoso es querer buscar el ultimo dato o un dato que no tenemos certeza de que este en la lista.
    - Esperaria que un BST mejore su eficiencia al poder descartar muchos datos en un solo paso

# seccion 2
    ¿Qué información usa un BST para descartar una parte del árbol que una lista desordenada no tiene?

    Usa las relaciones de valor que hay entre nodos

# seccion 3
    ¿Qué cambió: los datos o la forma del árbol?

    cambiaron los datos y la forma del arbol, al cambiar los datos e insertarlos de manera ordenada, el arbol se convierte en degenerado 
    
# seccion 4
    ¿Por qué la altura es más importante para búsqueda que la cantidad total de nodos por sí sola?

    Porque la altura te dice cuantas comparaciones debes hacer en el peor de los casos, al final de cuentas, si tienes un arbol de altura 15 y el dato que buscas es una hoja del nivel 15, entonces debes hacer 15 comparaciones (esa es mi hipotesis), eso nos dice mas que si solo sabemos cuantos nodos hay en total

# seccion 5
    Describe con tus palabras qué forma tiene un BST degenerado y por qué puede aparecer al insertar valores ordenados.

    Un BST degenerado tiene forma de una line recta en alguna direccion, con los nodos ordenados a modo de lista creciente; aparece al meter los datos de manera ordenada pues los estas insertando siguiendo una cadena de > 

# seccion 6

    ¿Qué relación hay entre profundidad, altura y número de comparaciones?

    A mayor profundidad, mas operaciones realizadas o a realizar, igual que con la altura 

# seccion 7
    ¿La diferencia de comparaciones crece cuando aumenta el tamaño del árbol degenerado?

    Si es degenerado, si y crece linealmente

# seccion 8
    ¿Qué muestran las animaciones sobre comparaciones acumuladas y altura recorrida?

    a mayor altura, mayores comparaciones y de nuevo creo que el numero de comparaciones que necesitas correponde a la altura del nodo que buscas

# seccion 9
    ¿Por qué no basta decir “BST es O(log n)” sin hablar de balance?

    Porque los datos no siempre se comporta de manera esperada o de la mejor manera, por lo que si nos vamos con la finta de que siempre tendremos una complejidad O(log n) es soñar mucho, por eso debemos matizar nuestra estructura para saber cuando si nos sirve y cuando no 


# seccion 10
    LeetCode 98 — Validate Binary Search Tree

    Usa arboles binarios por el simple plantamiento, tambien usa el concepto de subarboles, esto para empezar a crear el problma, pues para que un BST sea valido cada subarbol debe ser a su vez un BST, de lo contrario el ouput sera false

# seccion 11
    ¿Qué problema resuelve permitir `tests_extra`?

    No tener que moverse a la carpeta de la clase en la que estamos

# seccion 12
    ¿Qué debe incluir un comentario técnico útil en el PR?

    Si fallo la prueba, posible motivo por el cual fallo y si se conoce una pista/suguerencia para solucioarlo

# seccion 13
    Necesitamos, antes de empezar a programar, definir bien si la estrcutura que usaremos es eficiente para TODOS los posibles casos que se nos ocurran respecto al problema

# seccion 14

1. ¿Un BST siempre es mejor que una lista?

    No siempre, pues cuando es un arbol degenerado su complejidad es igual o se acercan mucho 

2. ¿Qué relación hay entre altura y comparaciones?

    la altura del nodo es el numero de comparaciones que necesitas para verficar que un dato pertenece al arbol
3. ¿Cómo se degenera un BST?

    Cuando se insertan los datos de manera ordenada
4. ¿Qué evidencia experimental usarías para justificar tu respuesta?

    hay varias pruebas en los test que verifican empiricamente este patron que describo
5. ¿Qué problema relacionado practicarías después?

    el problema de 98. Validate Binary Search Tree; me parece muy interesate agregar un nuevo parametro para validar un BST

