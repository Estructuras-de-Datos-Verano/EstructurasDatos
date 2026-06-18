# Clase 3

### Nombre: Patricio Navarro Burgos

## ¿Qué es un TDA?

- Es un tipo de dato que nosotros creamos, que no se define como tal pero que tiene su propio tipo de operaciones y un comportamiento esperado.

## Diferencia entre implementación e interfaz

- La interfaz es la forma en la que el usuario interactúa con el programa, no sabe que hace en el fondo, solo su comportamiento, sus operaciones y confía en que funciona.
- La implementación, por otro lado, es el conjunto de algoritmos que definen las operaciones, y la forma en la que trabaja realmente el programa. 

## Problema donde usaría una pila

- Lo usaría en un videojuego por ejemplo, donde puedas equipar al personaje con distintas cosas. Claro que un personaje puede tener varios atributos, entonces puedes hacer una pila para cada tipo de atributo o equipo para que el comportamiento sea más como el esperado de una pila.

## Prueba mínima en lenguaje natural

- Si la pila esta vacía y hago un $x.pila.apilar("y")$ entonces la pila ahora contiene a $y$.
- Si la pila esta vacía y usamos $x.pila.esta \_ vacia()$ entonces regresa un $True$, en caso contrario $False$.
- Si la pila tiene dos elementos y usamos $x.pila.desapilar()$, entonces el último elemento que se agregó a la pila se debe eliminar y solo quedar el primer elemento que se agregó a la misma.
- Si la pila tiene tres elementos y usamos $x.pila.peek()$, entonces regresa el último elemento que se agregó a la pila. Este es el tope.
- Si la pila esta vacía y se usa $x.pila.peek()$, entonces regresa un $None$.

## Pregunta sobre la clase

- ¿Se puede hacer una pila que en vez de utilizar el comportamiento LIFO, haga un comportamiento FIFO (First In, First Out)?