# Clase 06: Discusión
#### Nombre: Patricio Navarro

### 1. Lectura estratégica

Explica qué pide el problema.

- El problema pide dar el orden de salida de los niños qu quedan eliminados en un juego en el que están acomodados en círculo.

### 2. Elección de estructura

¿Por qué una cola?
- Porque el comportamiento de la solución de ejemplo empieza en la cabeza o el frente de la cola y saca a los primeros dos de forma que va eliminando a uno de cada dos niños. Esto nos dice que su comportamiento es como el FIFO, caractrístico de una cola.

¿Qué otra estructura consideraste?
- Una lista circular, pues parecía también cumplir con el acomodo de datos y ya tenía la forma que queríamos para el juego.

¿Por qué la descartaste?
- Porque no es algo que sepa usar todavía y además no esta tan optimizada como deque, pues necesitas dos referencias para cada nodo y además unir el nodo inicial con el final.

### 3. Diseño del algoritmo

Explica el algoritmo antes del código.
Lo que queríamos era que para una cantidad n de niños, juntar a los primeros dos de hasta el frente, eliminar al segundo, y guardarlo en una lista de eliminados, y al primero mandarlo al final de la cola, después repetir este proceso hasta que solo quedara un niño en la cola. Una vez alcanzado ese punto se terminaría de eliminar el niño y la cola quedaría vacía. 

### 4. Pruebas

Escoge una prueba pública.
- Prueba elegida: `test_caso_dos_ninos`

Explica qué propiedad verifica.
- Verifica que el orden de salida de los niños sea [2, 1]

Propón una prueba adicional.
- Verificar cuando se excede el caso máximo, es decir, cuando n > 2 * 10^5

### 5. Complejidad

Analiza tiempo y memoria.
- En nuestro reporte de pytest, pudimos observar que aun con las pruebas grandes el tiempo para realizarlas todas fue de 0.04 segundos, que es una cantidad muy baja si tomas en cuenta que analizamos el caso maximo y un caso para 1000 niños, además como el comportamiento era muy parecido a una cola al usar deque pudimos hacer una implementación sencilla y eficiente. También considerando el uso de un while y un if, conforme crece el tamaño son más los datos que tenemos que recorrer, por lo que me suena lógico que su eficiencia sea O(n).

##### Preguntas para profundizar en esto:
- ¿Cuántos niños se eliminan?
    * Se deben eliminar todos los niños.
- ¿Cuántas veces se mueve o procesa cada niño?
    * Entre 1 y n veces. Porque en el caso de los 7 niños, en el turno 7 se elimina el 7 tras haber sido movido 6 veces. Dando 7 movimientos. Por lo que parecería que el comportamiento es O(n).
- ¿Qué estructura permite que esas operaciones sean eficientes?
    * Las colas utilizando deque.
- ¿Cuánta memoria adicional se usa?
    * Poca, pues realmente el detalle esta en las variables de paso, y en operar los ciclos.

### 6. Contraste

Si el problema cambiara ligeramente, ¿seguirías usando una cola?
- Probablemente

¿Por qué?
- Porque un cambio ligero puede no afectar en gran medida la solución, sin embargo, sí debería considerarse siempre si hay alguna otra solución mas óptima. Hay muchos tipos de estructuras de datos y la solución casi nunca será única.

### 7. Pregunta abierta

Formula una pregunta técnica interesante relacionada con el problema.
- ¿Qué estructura pudo haber sido más eficiente para resolver el problema?¿Se pued encontrar alguna estructura para que sea O(log(n))?