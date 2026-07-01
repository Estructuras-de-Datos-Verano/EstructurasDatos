# Actividad 15 clase 05
## Leonardo Daniel Arenas Serafín

### 1. ¿Cuál es la diferencia más importante entre una pila y una cola?

La diferencia está en que la Pila sigue un comportamiento LIFO (Last In, First Out), mientras que la cola sigue un comportamiento FIFO (First In, First Out). Es decir, en las pilas el último elemento agregado es el primero que va a salir, mientras que en las colas, el primer elemento en ser agregado será el primerp en salir.

### 2. ¿Cuál implementación fue más clara para ti?

Ambas, la verdad es que las implementaciones son muy claras y no dejan lugar a ninguna duda. Lo único que podría no estar tan claro es saber cómo es que funciona popleft() para el deque, pero fuera de esi todo es muy claro

### 3. ¿Cuál implementación parece más eficiente para muchas extracciones?

Definitivamente Deque, pues demostramos en el ejercicio 6 del notebook que es mucho menos complejo.

### 4. ¿Qué aprendiste al usar `pytest` con dos implementaciones?

Aprendí que una de las ventajas de definir las estructuras como TDAs y el tener una interfaz abstracta es que al hacer pruebas en pytest, podemos hacer las mismas pruebas con implementaciones totalmente diferentes usando el @pytest.mark.parametrize.

### 5. ¿Dónde usarías una cola en un problema de Matemáticas Aplicadas?

Tal vez lo usaría para tener un recuento de matrices asociadas a ecuaciones lineales por resolver.

### 6. ¿Qué duda te queda?

¿Y si si?