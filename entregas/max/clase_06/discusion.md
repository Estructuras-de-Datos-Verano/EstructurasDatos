### 1. Lectura estratégica

El problema pide que en un circulo en el que esten colocados una cantidad n de niños, en el cual, giremos en un solo orden, ya sea horario o contrahorario y en este circulo de niños vamos a saltarnos al primero y noviviremos al segundo y así sucesivamente el numero de pasasos que queramos o por defecto hasta que novivamnos a todos los niños en el circulo.

### 2. Elección de estructura

¿Por qué una cola?

    Poruqe lo que tiene una cola a diferencia de una pila es el FIFO en lugar del LIFO en donde podremos modificar tanto el final como el frente de la lista, y de esta maner darle este efecto circular sin la necesidad de utilizar estructuras más complejas como lo pueden ser las matrices que utilizamos en las graficas del primer semestre para dar este efecto circular.

¿Qué otra estructura consideraste?

    Así como lo scabo de mencionar, antes de leer el notebook completo, lo primero que se ocurrio fue ocupar matices al estilo del juego de la vida en primer semestre para ver que celda esta viva y cual no.

¿Por qué la descartaste?

    Porque en primer lugar no sabría como eliminar una matriz de una lista y como podiramos indexarlas para formar la lista final del orden en el que se fueron elimando estas matrices, luego, tengo la sensación que adicional a todo esto que acabo de mencionar, es bastante más suceptible a generar errores.

### 3. Diseño del algoritmo

El algoritmo que utilice nes practicamente igual al peseudocódigo del notebook, en donde defino las dos listas, la de los vivos y novivos, luego la de novivos la inicio en cero y la de vivos la inicio con el numero de participantes A.K.A niños, entonces primero se va a modificar la de los vivos moviendo al final al niño actual que sera el que estamos salvando, luego a novividos vamos a agregar a el niño actual, que sera diferente al que acabamos de salvar por obvias razones, y luego vamos a volver a actualizar la lista de vivos y así voy a repetit el proceso hasta el número de pasos indicado, y al final te va a regresar la lista en el orden en el que se fueron desviviendo los niños.

### 4. Pruebas

La prueba publica que utilice fue:

    ```text
    def cargar_modulo():
        """Carga la solución del estudiante o, si no existe, el código base."""

        try:
            return import_module("implementacion")
        except ModuleNotFoundError:
            return import_module("src.josephus")

    ```

Lo que verifica esta prueba es que se importen las librerias que necesitamos utilizar de manera correcta, esto es importante para correr las demas pruebas necesarias y los códigos y funciones en genelar

Mi propocisión de prueba es:
    ```text
    def test_max():
    n = 10
    orden = modulo.orden_eliminacion(n)
    assert len(orden) == n
    ```

### 5. Complejidad

- ¿Cuántos niños se eliminan?
    Depende del número de pasod, ya que se van a eliminar el mismo número de niños que de pasos.

- ¿Cuántas veces se mueve o procesa cada niño?
    Depende, se procesa una vez si se salva y se mueve a la derecha para repetir el ciclo o se elimina y la unicamente que se vaya a procesar dos veces es que se salve, se mueva a la derecha y cuando llegue el numero de pasos necesario se elimine.

- ¿Qué estructura permite que esas operaciones sean eficientes?
    El hecho que las colas las hagamos con deque, si no no podriamos alcanzar el número maximo poruqe el reacomodo de las listas sería masivo

- ¿Cuánta memoria adicional se usa?
    El uso de memoria crece de manera exponencial

Al ocupar el tipo de pilas deque lo que hace es que crezca de manera logaritmica el tiempo, osea no se va a tardar tanto en cuestión de tiempo y recursos computacionales.


### 6. Contraste

Si el problema cambiara ligeramente, ¿seguirías usando una cola?

    Depende de los cambios, di dejamos de utilizar el ciculo si, ya que en una linea utiliariamos una pila o simplemente una lista, si agregamos prarametros de hacerlo cada 3 niños en lugara de cada dos o desvivivr dos en lugar de uno, pero concervando lo ciclico si mantendría el deque para el mismo sstema peor con diferentes parametros.

### 7. Pregunta abierta

¿Que sistima deberiamos de utilizar para matar al niño que este al frente del que estamos seleccionando en un circulo? Porque los deque no pueden modificar datos intermedios, solo orillas.