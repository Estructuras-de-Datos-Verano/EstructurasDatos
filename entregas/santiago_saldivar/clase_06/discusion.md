### 1. Lectura estratégica

¿Qué estpa pidiendo el problema?
El problema pide el orden en que son eliminados los niños.

¿Qué información debemos recordar?
El orden de eliminación

### 2. Elección de estructura

¿Por qué una cola?
Porque nos permite trabajar intuitivamente con el primer elemento de la lista.

¿Qué otra estrucura consideraste?
Una pila, que podría hacerlo pero empezando desde atrás.

¿Por qué la descartaste?
Porque es más intuitivo ir en orden.

### 3. Diseño del algoritmo

Explica el algoritmo antes del código.

Primero revisamos que el número que recibimos sea correcto: no podemos tener niños medios ni negativos. Luego, hacemos un deque, objeto con FIFO que nos permite trabajar con los elementos del frente, que tenga todos los enteros de 1 hasta el número que recibimos. Luego, abrimos una lista vacía que se llama "eliminados". Ahí agregaremos en orden cada niño que eliminemos. Iniciamos un bucle con while, que revisará que la lista NO esté vacía continuamente. Siempre y cuando esta condición se cumpla, pasa a una condicional. En ésta hay dos opciones. Primero, si sólo hay un niño, lo agrega a eliminados y nos regresa esa lista con un sólo elemento. Si hay más, regresa al primero que tope al final de la lista. Luego, al segundo, lo manda a eliminados. Sigue así hasta que se acaben los niños.

### 4. Pruebas

Escoge una prueba pública.

def test_caso_minimo():
    assert modulo.orden_eliminacion(1) == [1]


Explica qué propiedad verifica.

Verifica que el caso básico de un solo niño funcione correctamente.

Propón una prueba adicional.

Prueba que verifica que el primer  número en salir durante el caso mayor a 1 sea exactamente 2.

### 5. Complejidad

La complejidad es lineal. Según aumentan los niños, aumenta de forma constante.

### 6. Contraste

Si el problema cambiara ligeramente, ¿seguirías usando una cola?

Depende de cómo cambie, pero en general, no.

¿Por qué?

Siempre y cuando sea necesario trabajar con los elementos del inicio, lo seguiría haciendo. Por ejemplo, si sólo cambia el orden de eliminación: quitar el primero y salvar el segundo, no tendría sentido cambiar.

### 7. Pregunta abierta

¿Cómo cambiaría la implementación si necesito comenzar a iterar en un punto distinto del inicio? ¿Seguiría siendo útil una pila?